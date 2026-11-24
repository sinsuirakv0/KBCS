# v15.7.4 → v16.0.0 · 最優先の変更候補 (61)

[一覧の目次](README.md)

<a id="compare-2ce4b479ffebf5b416fcc51f6152aa7f"></a>

### [`00afcc94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afcc94.md) → [`00b5ca18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5ca18.md) _ZN8firebase15CleanupNotifier15UnregisterOwnerENSt6__ndk114__map_iteratorINS1_15__tree_iteratorINS1_12__value_typeIPvPS0_EEPNS1_11__tree_nod

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdece0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdece0.md) · 呼出先 5件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bde750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde750.md)
- 新版 呼出元 1件 [`00c5b7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b7a0.md) · 呼出先 5件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5b1d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1d0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 34.72% / 新版 34.72%

CFGの説明率　旧版 10.34% / 新版 4.05%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_condition` 1件, `unresolved_branch_alignment` 8件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afcc94"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afcc94"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afcc98"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afcc94",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afcc98",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afcc9c",
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
      "00b5ca18",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b5ca1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b5ca20",
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

- 旧版 [`00afcc94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afcc94.md#insn-00afcc94) · [`00afcc98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afcc94.md#insn-00afcc98) · [`00afcc9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afcc94.md#insn-00afcc9c)

~~~diff
- 00afcc94 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00afcc94 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00afcc94 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00afcc94 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00afcc94 bytes f657bda9
- 00afcc98 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00afcc98 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00afcc98 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00afcc98 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afcc98 bytes f44f01a9
- 00afcc9c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00afcc9c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00afcc9c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00afcc9c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afcc9c bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e96b6db1f1e633dc79a4c0b9b46b9ae"></a>

### [`00afcdb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afcdb4.md) → [`00b5cb38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5cb38.md) _ZN8firebase15CleanupNotifier11FindByOwnerEPv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bddd90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd90.md) · 呼出先 2件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)
- 新版 呼出元 1件 [`00c5a7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7f0.md) · 呼出先 2件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 19.44% / 新版 19.44%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afcdb4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afcdb4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afcdb8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afcdb4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afcdb8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afcdc4",
      "READ",
      [
        "storage",
        "00c1b998",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b5cb38",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b5cb3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b5cb48",
      "READ",
      [
        "storage",
        "00c9b398",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afcdb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afcdb4.md#insn-00afcdb4) · [`00afcdb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afcdb4.md#insn-00afcdb8) · [`00afcdd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afcdb4.md#insn-00afcdd4)

~~~diff
- 00afcdb4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00afcdb4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00afcdb4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00afcdb4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00afcdb4 bytes f44fbea9
- 00afcdb8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00afcdb8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00afcdb8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00afcdb8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afcdb8 bytes fd7b01a9
- 00afcdd4 ["INT_ADD", "register:40f0:8", ["const:afcdd4:8", "const:4:8"]]
- 00afcdd4 ["CALL", null, ["callee:00c5a600:8"]]
- 00afcdd4 bytes 93830394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1c6a6145e4fb3184f3a13cfffca6eab"></a>

### [`00afce44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afce44.md) → [`00b5cbc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5cbc8.md) _ZNSt6__ndk16__treeINS_12__value_typeIPvPFvS2_EEENS_19__map_value_compareIS2_S5_NS_4lessIS2_EELb1EEENS_9allocatorIS5_EEE7destroyEPNS_11__tre

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bded00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bded00.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bded00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bded00.md)
- 新版 呼出元 1件 [`00c5b7c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b7c0.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5b7c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b7c0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 81.25% / 新版 81.25%

CFGの説明率　旧版 50.00% / 新版 7.69%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afce48"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afce48"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afce4c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afce48",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afce4c",
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
      "00b5cbcc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b5cbd0",
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

- 旧版 [`00afce48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afce44.md#insn-00afce48) · [`00afce4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afce44.md#insn-00afce4c) · [`00afce60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afce44.md#insn-00afce60)
- 新版 [`00b5cbe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5cbc8.md#insn-00b5cbe4)

~~~diff
- 00afce48 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00afce48 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00afce48 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00afce48 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00afce48 bytes f44fbea9
- 00afce4c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00afce4c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00afce4c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00afce4c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afce4c bytes fd7b01a9
- 00afce60 ["INT_ADD", "register:40f0:8", ["const:afce60:8", "const:4:8"]]
- 00afce60 ["CALL", null, ["callee:00c5b7c0:8"]]
+ 00b5cbe4 ["INT_ADD", "register:40f0:8", ["const:b5cbe4:8", "const:4:8"]]
+ 00b5cbe4 ["CALL", null, ["callee:00c5b7c0:8"]]
- 00afce60 bytes a8870394
+ 00b5cbe4 bytes f7fa0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-813a9d3b852335c3b4a60b9b14b9b24f"></a>

### [`00afce84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afce84.md) → [`00b5cc08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5cc08.md) _ZNSt6__ndk16__treeINS_12__value_typeIPvPN8firebase15CleanupNotifierEEENS_19__map_value_compareIS2_S6_NS_4lessIS2_EELb1EEENS_9allocatorIS6_E

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bded10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bded10.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bded10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bded10.md)
- 新版 呼出元 1件 [`00c5b7d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b7d0.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5b7d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b7d0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 81.25% / 新版 81.25%

CFGの説明率　旧版 50.00% / 新版 7.69%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afce88"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afce88"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afce8c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afce88",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afce8c",
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
      "00b5cc0c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b5cc10",
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

- 旧版 [`00afce88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afce84.md#insn-00afce88) · [`00afce8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afce84.md#insn-00afce8c) · [`00afcea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afce84.md#insn-00afcea0)
- 新版 [`00b5cc24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5cc08.md#insn-00b5cc24)

~~~diff
- 00afce88 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00afce88 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00afce88 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00afce88 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00afce88 bytes f44fbea9
- 00afce8c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00afce8c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00afce8c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00afce8c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afce8c bytes fd7b01a9
- 00afcea0 ["INT_ADD", "register:40f0:8", ["const:afcea0:8", "const:4:8"]]
- 00afcea0 ["CALL", null, ["callee:00c5b7d0:8"]]
+ 00b5cc24 ["INT_ADD", "register:40f0:8", ["const:b5cc24:8", "const:4:8"]]
+ 00b5cc24 ["CALL", null, ["callee:00c5b7d0:8"]]
- 00afcea0 bytes 9c870394
+ 00b5cc24 bytes ebfa0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-acec3a22db9b30249ad0e20faf131b0a"></a>

### [`00afcefc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afcefc.md) → [`00b5cc80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5cc80.md) _ZN8firebase4PathC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bded30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bded30.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b7f0.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 57.14% / 新版 57.14%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afcefc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afcefc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b5cc80"
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
      "unmatched:00afcefc",
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
      "00b5cc80",
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

- 旧版 [`00afcefc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afcefc.md#insn-00afcefc) · [`00afcf0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afcefc.md#insn-00afcf0c) · [`00afcf14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afcefc.md#insn-00afcf14)
- 新版 [`00b5cc90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5cc80.md#insn-00b5cc90)

~~~diff
- 00afcefc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00afcefc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00afcefc ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 00afcefc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00afcefc bytes fd7bbfa9
- 00afcf0c ["INT_ADD", "register:40f0:8", ["const:afcf0c:8", "const:4:8"]]
- 00afcf0c ["CALL", null, ["callee:00c5b7f0:8"]]
+ 00b5cc90 ["INT_ADD", "register:40f0:8", ["const:b5cc90:8", "const:4:8"]]
+ 00b5cc90 ["CALL", null, ["callee:00c5b7f0:8"]]
- 00afcf0c bytes 89870394
+ 00b5cc90 bytes d8fa0394
- 00afcf14 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00afcf14 ["RETURN", null, ["register:0:8"]]
- 00afcf14 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b040d94e91c2d668e922db651cfeb3da"></a>

### [`00afcf18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afcf18.md) → [`00b5cc9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5cc9c.md) _ZN8firebase4Path16NormalizeSlashesERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bded30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bded30.md) · 呼出先 3件 [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bded50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bded50.md) [`00bded70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bded70.md)
- 新版 呼出元 1件 [`00c5b7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b7f0.md) · 呼出先 3件 [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c5b810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b810.md) [`00c5b830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b830.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 63.71% / 新版 63.71%

CFGの説明率　旧版 9.30% / 新版 3.92%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 14件, `unresolved_branch_alignment` 14件, `unresolved_store_alignment` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afcf1c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afcf1c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afcf20"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afcf1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afcf20",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afcf24",
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
      "00b5cca0",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b5cca4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b5cca8",
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

- 旧版 [`00afcf1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afcf18.md#insn-00afcf1c) · [`00afcf20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afcf18.md#insn-00afcf20) · [`00afcf24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afcf18.md#insn-00afcf24)

~~~diff
- 00afcf1c ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00afcf1c ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00afcf1c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00afcf1c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afcf1c bytes fc6f01a9
- 00afcf20 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00afcf20 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00afcf20 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00afcf20 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afcf20 bytes fa6702a9
- 00afcf24 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00afcf24 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00afcf24 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00afcf24 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afcf24 bytes f85f03a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9bc35e0c6d2ca3b9fb98c8f2c342855"></a>

### [`00afd108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd108.md) → [`00b5ce8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5ce8c.md) _ZN8firebase4PathC2ERKNSt6__ndk16vectorINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS6_IS8_EEEE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`00afd2ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd2ac.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00b5d030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5d/00b5d030.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 72.73% / 新版 72.73%

CFGの説明率　旧版 16.67% / 新版 11.36%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afd10c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afd10c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afd110"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afd10c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afd110",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afd114",
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
      "00b5ce90",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b5ce94",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b5ce98",
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

- 旧版 [`00afd10c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd108.md#insn-00afd10c) · [`00afd110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd108.md#insn-00afd110) · [`00afd114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd108.md#insn-00afd114)

~~~diff
- 00afd10c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00afd10c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00afd10c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00afd10c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afd10c bytes f85f02a9
- 00afd110 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00afd110 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00afd110 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00afd110 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afd110 bytes f65703a9
- 00afd114 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00afd114 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00afd114 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00afd114 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afd114 bytes f44f04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14b9234d06aadf588e2f4e9d3a91f453"></a>

### [`00afd2ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd2ac.md) → [`00b5d030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5d/00b5d030.md) FUN_00b5d030

採用 · 移動量 `+0x5fd84` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`00afd108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd108.md) [`00afd23c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd23c.md) [`00afdc48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afdc48.md) [`00afddf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afddf8.md) · 呼出先 3件 [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdb7a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7a0.md) [`00bded80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bded80.md)
- 新版 呼出元 4件 [`00b5ce8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5ce8c.md) [`00b5cfc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5c/00b5cfc0.md) [`00b5d9cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5d/00b5d9cc.md) [`00b5db7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5d/00b5db7c.md) · 呼出先 3件 [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c581f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c581f0.md) [`00c5b840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b840.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 75.83% / 新版 75.83%

CFGの説明率　旧版 34.29% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 8件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afd2ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afd2b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afd2b0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afd2ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afd2b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afd2b4",
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
      "00b5d030",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b5d034",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b5d038",
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

- 旧版 [`00afd2ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd2ac.md#insn-00afd2ac) · [`00afd2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd2ac.md#insn-00afd2b0) · [`00afd2b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd2ac.md#insn-00afd2b4)

~~~diff
- 00afd2ac ["COPY", "tmp:0:8", ["register:40b8:8"]]
- 00afd2ac ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00afd2ac ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00afd2ac bytes f70f1cf8
- 00afd2b0 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00afd2b0 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00afd2b0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00afd2b0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afd2b0 bytes f65701a9
- 00afd2b4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00afd2b4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00afd2b4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00afd2b4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afd2b4 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fba786a3898258264053654fdbedce39"></a>

### [`00afd48c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd48c.md) → [`00b5d210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5d/00b5d210.md) _ZNK8firebase4Path8GetChildERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00afaa08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afaa08.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bded30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bded30.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00b5a78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a78c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c5b7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b7f0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 65.31% / 新版 65.31%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afd4b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afd4ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afd4f0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afd4b4",
      "PARAM",
      [
        "storage",
        "0029583d",
        null,
        null
      ]
    ],
    [
      "unmatched:00afd4b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afd4e0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57b80"
      ]
    ]
  ],
  "added": [
    [
      "00b5d238",
      "PARAM",
      [
        "storage",
        "002a5276",
        null,
        null
      ]
    ],
    [
      "00b5d23c",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00b5d264",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57b80"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afd4b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd48c.md#insn-00afd4b8) · [`00afd4c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd48c.md#insn-00afd4c0) · [`00afd4d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd48c.md#insn-00afd4d8)
- 新版 [`00b5d244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5d/00b5d210.md#insn-00b5d244)

~~~diff
- 00afd4b8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00afd4b8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffd8:8"]]
- 00afd4b8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00afd4b8 bytes a8831df8
- 00afd4c0 ["INT_ADD", "register:40f0:8", ["const:afd4c0:8", "const:4:8"]]
- 00afd4c0 ["CALL", null, ["callee:00b5a78c:8"]]
+ 00b5d244 ["INT_ADD", "register:40f0:8", ["const:b5d244:8", "const:4:8"]]
+ 00b5d244 ["CALL", null, ["callee:00b5a78c:8"]]
- 00afd4c0 bytes 52f5ff97
+ 00b5d244 bytes 52f5ff97
- 00afd4d8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00afd4d8 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00afd4d8 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00afd4d8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "const:1:8"]]
- 00afd4d8 bytes 2115939a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21af203187453f6fcd5c615de2215875"></a>

### [`00afd550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd550.md) → [`00b5d2d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5d/00b5d2d4.md) _ZNK8firebase4Path8GetChildERKS0_

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00afaa08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afaa08.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bded30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bded30.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00b5a78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a78c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c5b7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b7f0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.22% / 新版 61.22%

CFGの説明率　旧版 25.00% / 新版 11.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afd554"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afd558"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afd558"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afd554",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afd558",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afd55c",
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
      "00b5d2d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b5d2dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b5d2e0",
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

- 旧版 [`00afd554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd550.md#insn-00afd554) · [`00afd558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd550.md#insn-00afd558) · [`00afd55c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd550.md#insn-00afd55c)

~~~diff
- 00afd554 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:40:8"]]
- 00afd554 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00afd554 bytes f52300f9
- 00afd558 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00afd558 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00afd558 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00afd558 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afd558 bytes f44f05a9
- 00afd55c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00afd55c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00afd55c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00afd55c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afd55c bytes fd7b06a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab42ba433738363eb55096047e062771"></a>

### [`00afd614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd614.md) → [`00b5d398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5d/00b5d398.md) _ZNK8firebase4Path9GetParentEv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bde230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde230.md) [`00bde970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde970.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5acb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5acb0.md) [`00c5b3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b3f0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 70.00% / 新版 70.00%

CFGの説明率　旧版 19.05% / 新版 10.53%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 5件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afd618"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afd61c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afd61c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afd618",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afd61c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afd620",
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
      "00b5d39c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b5d3a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b5d3a4",
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

- 旧版 [`00afd618`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd614.md#insn-00afd618) · [`00afd61c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd614.md#insn-00afd61c) · [`00afd620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd614.md#insn-00afd620)

~~~diff
- 00afd618 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00afd618 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00afd618 bytes f51300f9
- 00afd61c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00afd61c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00afd61c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00afd61c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afd61c bytes f44f03a9
- 00afd620 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00afd620 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00afd620 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00afd620 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afd620 bytes fd7b04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac19a6b4aed90440ffe69a33fefa5dcc"></a>

### [`00afd7a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd7a0.md) → [`00b5d524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5d/00b5d524.md) _ZNK8firebase4Path8IsParentERKS0_

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment

命令の説明率　旧版 82.76% / 新版 82.76%

CFGの説明率　旧版 60.61% / 新版 46.51%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

アドレスに依存する影響 `unresolved_branch_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00afd7a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00afd7ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00afd7dc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afd7a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5d540"
      ]
    ],
    [
      "unmatched:00afd7ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5d604"
      ]
    ],
    [
      "unmatched:00afd7e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5d574"
      ]
    ]
  ],
  "added": [
    [
      "00b5d528",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5d540"
      ]
    ],
    [
      "00b5d530",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5d604"
      ]
    ],
    [
      "00b5d568",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5d574"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afd7a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd7a0.md#insn-00afd7a4) · [`00afd7ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd7a0.md#insn-00afd7ac) · [`00afd7dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd7a0.md#insn-00afd7dc)

~~~diff
- 00afd7a4 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00afd7a4 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00afd7a4 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00afd7a4 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00afd7a4 bytes c8000037
- 00afd7ac ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00afd7ac ["CBRANCH", null, ["local:b22:8", "tmp:0:1"]]
- 00afd7ac bytes a90600b4
- 00afd7dc ["COPY", "tmp:0:8", ["register:4060:8"]]
- 00afd7dc ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00afd7dc ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00afd7dc ["COPY", "register:4048:8", ["tmp:0:8"]]
- 00afd7dc bytes 8901899a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9a45e428edd01f935567fbd37c9ed38"></a>

### [`00afd888`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd888.md) → [`00b5d60c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5d/00b5d60c.md) _ZNK8firebase4Path14GetDirectoriesEv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bded40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bded40.md) · 呼出先 6件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md) [`00bde7d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde7d0.md)
- 新版 呼出元 1件 [`00c5b800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b800.md) · 呼出先 6件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md) [`00c5b250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b250.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 82.26% / 新版 82.26%

CFGの説明率　旧版 25.40% / 新版 18.60%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_condition` 5件, `unresolved_branch_alignment` 12件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afdaa8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afdad0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b5d82c"
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
      "00b5d660",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00afdb38"
      ]
    ],
    [
      "unmatched:00afd92c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00afdb38"
      ]
    ],
    [
      "00b5d6d8",
      "PARAM",
      [
        "storage",
        "0029583d",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b5d660",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5d8bc"
      ]
    ],
    [
      "00b5d6b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5d8bc"
      ]
    ],
    [
      "00b5d6d8",
      "PARAM",
      [
        "storage",
        "002a5276",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afd8d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd888.md#insn-00afd8d4) · [`00afd918`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd888.md#insn-00afd918) · [`00afd91c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd888.md#insn-00afd91c)

~~~diff
- 00afd8d4 ["COPY", "tmp:0:8", ["register:4060:8"]]
- 00afd8d4 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00afd8d4 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00afd8d4 ["COPY", "register:4060:8", ["tmp:0:8"]]
- 00afd8d4 bytes 8c01899a
- 00afd918 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00afd918 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00afd918 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00afd918 ["COPY", "register:4068:8", ["tmp:0:8"]]
- 00afd918 bytes 0d038a9a
- 00afd91c ["COPY", "tmp:0:8", ["register:4060:8"]]
- 00afd91c ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00afd91c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00afd91c ["COPY", "register:4060:8", ["tmp:0:8"]]
- 00afd91c bytes 8c01899a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70e3be881b45195060bcecb4c062fbc6"></a>

### [`00afdc48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afdc48.md) → [`00b5d9cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5d/00b5d9cc.md) _ZNK8firebase4Path17PopFrontDirectoryEv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00afd2ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd2ac.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bded30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bded30.md) [`00bded40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bded40.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00b5d030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5d/00b5d030.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5b7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b7f0.md) [`00c5b800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b800.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 67.74% / 新版 67.74%

CFGの説明率　旧版 28.12% / 新版 20.45%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 5件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afdc4c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afdc50"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afdc50"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afdc4c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afdc50",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afdc54",
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
      "00b5d9d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b5d9d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b5d9d8",
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

- 旧版 [`00afdc4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afdc48.md#insn-00afdc4c) · [`00afdc50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afdc48.md#insn-00afdc50) · [`00afdc54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afdc48.md#insn-00afdc54)

~~~diff
- 00afdc4c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:40:8"]]
- 00afdc4c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00afdc4c bytes f52300f9
- 00afdc50 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00afdc50 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00afdc50 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00afdc50 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afdc50 bytes f44f05a9
- 00afdc54 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00afdc54 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00afdc54 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00afdc54 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afdc54 bytes fd7b06a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d313ee458b5a3e7dcf73f513e0641e78"></a>

### [`00afe37c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afe/00afe37c.md) → [`00b5e100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5e/00b5e100.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7reserveEm

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00bdb7a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7a0.md) · 呼出先 4件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 1件 [`00c581f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c581f0.md) · 呼出先 4件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 94.44% / 新版 91.89%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afe398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afe/00afe37c.md#insn-00afe398) · [`00afe3d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afe/00afe37c.md#insn-00afe3d8) · [`00afe3f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afe/00afe37c.md#insn-00afe3f0)
- 新版 [`00b5e11c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5e/00b5e100.md#insn-00b5e11c) · [`00b5e15c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5e/00b5e100.md#insn-00b5e15c) · [`00b5e174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5e/00b5e100.md#insn-00b5e174)

~~~diff
- 00afe398 ["CBRANCH", null, ["local:b24:8", "register:102:1"]]
+ 00b5e11c ["CBRANCH", null, ["local:b25:8", "register:102:1"]]
- 00afe398 bytes a2080054
+ 00b5e11c bytes a2080054
- 00afe3d8 ["CBRANCH", null, ["local:b23:8", "register:101:1"]]
+ 00b5e15c ["CBRANCH", null, ["local:b24:8", "register:101:1"]]
- 00afe3d8 bytes e0050054
+ 00b5e15c bytes e0050054
- 00afe3f0 ["INT_RIGHT", "tmp:0:4", ["register:40c0:4", "const:0:4"]]
- 00afe3f0 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00afe3f0 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00afe3f0 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00b5e174 ["INT_RIGHT", "tmp:0:4", ["register:40c0:4", "const:0:4"]]
+ 00b5e174 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00b5e174 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00b5e174 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00afe3f0 bytes d8020037
+ 00b5e174 bytes d8020037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57ab8a2951f07eb5a79bde11a97c1b31"></a>

### [`00afe4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afe/00afe4b0.md) → [`00b5e234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5e/00b5e234.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertIPKcEENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr38__li

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bded60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bded60.md) · 呼出先 7件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdda90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda90.md)
- 新版 呼出元 1件 [`00c5b820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b820.md) · 呼出先 7件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c5a4e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4e0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 93.12% / 新版 93.12%

CFGの説明率　旧版 58.97% / 新版 53.49%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00afe51c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00afe52c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00afe548"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5e290",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00afe524"
      ]
    ],
    [
      "unmatched:00afe51c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5e2b4"
      ]
    ],
    [
      "unmatched:00afe520",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5e300"
      ]
    ]
  ],
  "added": [
    [
      "00b5e290",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5e2a8"
      ]
    ],
    [
      "00b5e2a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5e2b4"
      ]
    ],
    [
      "00b5e2a4",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5e300"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afe51c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afe/00afe4b0.md#insn-00afe51c) · [`00afe52c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afe/00afe4b0.md#insn-00afe52c) · [`00afe548`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afe/00afe4b0.md#insn-00afe548)

~~~diff
- 00afe51c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00afe51c ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00afe51c ["CBRANCH", null, ["local:b8:8", "tmp:1:1"]]
- 00afe51c bytes a9000054
- 00afe52c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00afe52c ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00afe52c ["CBRANCH", null, ["local:b14:8", "tmp:1:1"]]
- 00afe52c bytes 88020054
- 00afe548 ["CBRANCH", null, ["local:b50:8", "register:102:1"]]
- 00afe548 bytes c2120054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-418fa9c9c7353d55c2e66d4ebdcf1db8"></a>

### [`00afe7a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afe/00afe7a4.md) → [`00b5e528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5e/00b5e528.md) _ZN8firebase17FutureBackingDataD1Ev

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdedd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdedd0.md) · 呼出先 10件 [`00b00d00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00d00.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddc50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc50.md)
- 新版 呼出元 1件 [`00c5b890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b890.md) · 呼出先 10件 [`00b60a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60a84.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a6a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a6a0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.14% / 新版 98.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5e55c",
      "incomplete_value": false,
      "site": "00b5e560",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c0000:8"
          ],
          [
            "leaf",
            "const:90d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00afe7d8",
      "incomplete_value": false,
      "site": "00afe7dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2af000:8"
          ],
          [
            "leaf",
            "const:349:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5e584",
      "incomplete_value": false,
      "site": "00b5e588",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b2000:8"
          ],
          [
            "leaf",
            "const:576:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00afe800",
      "incomplete_value": false,
      "site": "00afe804",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:eb5:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b5e6ac",
      "value": [
        "leaf",
        "ram:c5a6a0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00afe928",
      "value": [
        "leaf",
        "ram:bddc50:8"
      ]
    },
    "ordinal": 14,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5e55c",
      "PARAM",
      [
        "storage",
        "002af349",
        null,
        "string"
      ]
    ],
    [
      "00b5e584",
      "PARAM",
      [
        "storage",
        "002a1eb5",
        null,
        "string"
      ]
    ],
    [
      "00b5e5bc",
      "READ",
      [
        "storage",
        "00c1b9a8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b5e55c",
      "PARAM",
      [
        "storage",
        "002c090d",
        null,
        "string"
      ]
    ],
    [
      "00b5e584",
      "PARAM",
      [
        "storage",
        "002b2576",
        null,
        "string"
      ]
    ],
    [
      "00b5e5bc",
      "READ",
      [
        "storage",
        "00c9b3a8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afe7dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afe/00afe7a4.md#insn-00afe7dc) · [`00afe804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afe/00afe7a4.md#insn-00afe804) · [`00afe928`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afe/00afe7a4.md#insn-00afe928)
- 新版 [`00b5e560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5e/00b5e528.md#insn-00b5e560) · [`00b5e588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5e/00b5e528.md#insn-00b5e588) · [`00b5e6ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5e/00b5e528.md#insn-00b5e6ac)

~~~diff
- 00afe7dc ["INT_ADD", "register:40f0:8", ["const:afe7dc:8", "const:4:8"]]
- 00afe7dc ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b5e560 ["INT_ADD", "register:40f0:8", ["const:b5e560:8", "const:4:8"]]
+ 00b5e560 ["CALL", null, ["callee:00c5ac00:8"]]
- 00afe7dc bytes 697e0394
+ 00b5e560 bytes a8f10394
- 00afe804 ["INT_ADD", "register:40f0:8", ["const:afe804:8", "const:4:8"]]
- 00afe804 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b5e588 ["INT_ADD", "register:40f0:8", ["const:b5e588:8", "const:4:8"]]
+ 00b5e588 ["CALL", null, ["callee:00c5ac00:8"]]
- 00afe804 bytes 5f7e0394
+ 00b5e588 bytes 9ef10394
- 00afe928 ["INT_ADD", "register:40f0:8", ["const:afe928:8", "const:4:8"]]
- 00afe928 ["CALL", null, ["ram:bddc50:8"]]
+ 00b5e6ac ["INT_ADD", "register:40f0:8", ["const:b5e6ac:8", "const:4:8"]]
+ 00b5e6ac ["CALL", null, ["ram:c5a6a0:8"]]
- 00afe928 bytes ca7c0394
+ 00b5e6ac bytes fdef0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c66a36c13818a901b1dc04681a6187a3"></a>

### [`00afeb24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afe/00afeb24.md) → [`00b5e8a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5e/00b5e8a8.md) _ZN8firebase26ReferenceCountedFutureImplD2Ev

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00bdddf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdddf0.md) [`00bdee20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdee20.md) · 呼出先 11件 [`00b012e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b012e0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddc50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc50.md)
- 新版 呼出元 2件 [`00c5a850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a850.md) [`00c5b8d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b8d0.md) · 呼出先 11件 [`00b60ef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60ef8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a6a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a6a0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 88.10% / 新版 88.10%

CFGの説明率　旧版 42.00% / 新版 55.26%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b5e8d4",
      "incomplete_value": true,
      "site": "00b5e8d8",
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
      "definition_site": "00afeb50",
      "incomplete_value": true,
      "site": "00afeb54",
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
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00afec28"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00afec58"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5e8c8",
      "READ",
      [
        "storage",
        "00c1b8b0",
        null,
        "pointer"
      ]
    ],
    [
      "00b5e8d8",
      "DATA",
      [
        "storage",
        "00c108a0",
        null,
        "undefined1[120]"
      ]
    ],
    [
      "00b5e988",
      "PARAM",
      [
        "storage",
        "0029039e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b5e8c8",
      "READ",
      [
        "storage",
        "00c9b2b0",
        null,
        "pointer"
      ]
    ],
    [
      "00b5e8d8",
      "DATA",
      [
        "storage",
        "00c8ffc0",
        null,
        "undefined1[120]"
      ]
    ],
    [
      "00b5e988",
      "PARAM",
      [
        "storage",
        "0029f8d5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afebd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afe/00afeb24.md#insn-00afebd0) · [`00afec28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afe/00afeb24.md#insn-00afec28) · [`00afec58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afe/00afeb24.md#insn-00afec58)
- 新版 [`00b5e954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5e/00b5e8a8.md#insn-00b5e954)

~~~diff
- 00afebd0 ["INT_ADD", "register:40f0:8", ["const:afebd0:8", "const:4:8"]]
- 00afebd0 ["CALL", null, ["callee:00c5b390:8"]]
+ 00b5e954 ["INT_ADD", "register:40f0:8", ["const:b5e954:8", "const:4:8"]]
+ 00b5e954 ["CALL", null, ["callee:00c5b390:8"]]
- 00afebd0 bytes 507f0394
+ 00b5e954 bytes 8ff20394
- 00afec28 ["INT_NOTEQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00afec28 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 00afec28 bytes c9ffffb5
- 00afec58 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00afec58 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 00afec58 bytes 61ffff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a93cede75660b1c91fb16c23fa9e562"></a>

### [`00afed40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afe/00afed40.md) → [`00b5eac4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5e/00b5eac4.md) _ZN8firebase26ReferenceCountedFutureImpl13AllocInternalEiPvPFvS1_E

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bddfc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfc0.md) · 呼出先 11件 [`00b00d00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00d00.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)
- 新版 呼出元 1件 [`00c5aa40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa40.md) · 呼出先 11件 [`00b60a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60a84.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 88.44% / 新版 88.44%

CFGの説明率　旧版 33.33% / 新版 44.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `call_target` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 5件, `unresolved_store_alignment` 5件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afed80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afedb4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afedb4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afed80",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afee1c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5eb68"
      ]
    ],
    [
      "00b5ec44",
      "PARAM",
      [
        "storage",
        "00b00d00",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b5eb04",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00b5eb84",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5eb68"
      ]
    ],
    [
      "00b5ec44",
      "PARAM",
      [
        "storage",
        "00b60a84",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afed80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afe/00afed40.md#insn-00afed80) · [`00afed84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afe/00afed40.md#insn-00afed84) · [`00afedb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afe/00afed40.md#insn-00afedb4)
- 新版 [`00b5eb08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5e/00b5eac4.md#insn-00b5eb08)

~~~diff
- 00afed80 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:48:8"]]
- 00afed80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00afed80 bytes e82700f9
- 00afed84 ["INT_ADD", "register:40f0:8", ["const:afed84:8", "const:4:8"]]
- 00afed84 ["CALL", null, ["callee:00c57a90:8"]]
+ 00b5eb08 ["INT_ADD", "register:40f0:8", ["const:b5eb08:8", "const:4:8"]]
+ 00b5eb08 ["CALL", null, ["callee:00c57a90:8"]]
- 00afed84 bytes af700394
+ 00b5eb08 bytes e2e30394
- 00afedb4 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00afedb4 ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 00afedb4 ["COPY", "tmp:2:8", ["register:4048:8"]]
- 00afedb4 ["INT_ADD", "tmp:3:8", ["register:4000:8", "const:48:8"]]
- 00afedb4 bytes 1fa404a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4874794c38a0be844d55cfe43d2ad09"></a>

### [`00aff05c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00aff05c.md) → [`00b5ede0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5e/00b5ede0.md) _ZN8firebase10FutureBaseaSEOS0_

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bded90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bded90.md) · 呼出先 6件 [`00b00d00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00d00.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddda0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddda0.md)
- 新版 呼出元 1件 [`00c5b850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b850.md) · 呼出先 6件 [`00b60a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60a84.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a800.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 91.82% / 新版 91.82%

CFGの説明率　旧版 21.21% / 新版 30.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00aff0b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5ee3c",
      "incomplete_value": true,
      "site": "00b5ee40",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "old": null,
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5ee94",
      "incomplete_value": false,
      "site": "00b5eea0",
      "value": [
        "leaf",
        "const:b60a84:8"
      ]
    },
    "old": {
      "definition_site": "00aff110",
      "incomplete_value": false,
      "site": "00aff11c",
      "value": [
        "leaf",
        "const:b00d00:8"
      ]
    },
    "ordinal": 7,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5ee94",
      "PARAM",
      [
        "storage",
        "00b00d00",
        null,
        null
      ]
    ],
    [
      "00b5ef10",
      "PARAM",
      [
        "storage",
        "00b00d00",
        null,
        null
      ]
    ],
    [
      "unmatched:00aff0b0",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b5ee94",
      "PARAM",
      [
        "storage",
        "00b60a84",
        null,
        null
      ]
    ],
    [
      "00b5ef10",
      "PARAM",
      [
        "storage",
        "00b60a84",
        null,
        null
      ]
    ],
    [
      "00b5ee34",
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

- 旧版 [`00aff0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00aff05c.md#insn-00aff0b0) · [`00aff0bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00aff05c.md#insn-00aff0bc) · [`00aff11c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00aff05c.md#insn-00aff11c)
- 新版 [`00b5ee40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5e/00b5ede0.md#insn-00b5ee40) · [`00b5eea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5e/00b5ede0.md#insn-00b5eea0)

~~~diff
- 00aff0b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aff0b0 ["INT_ADD", "register:40f0:8", ["const:aff0b0:8", "const:4:8"]]
- 00aff0b0 ["CALLIND", null, ["register:0:8"]]
- 00aff0b0 bytes 00013fd6
- 00aff0bc ["INT_ADD", "register:40f0:8", ["const:aff0bc:8", "const:4:8"]]
- 00aff0bc ["CALL", null, ["callee:00c5a610:8"]]
+ 00b5ee40 ["INT_ADD", "register:40f0:8", ["const:b5ee40:8", "const:4:8"]]
+ 00b5ee40 ["CALL", null, ["callee:00c5a610:8"]]
- 00aff0bc bytes dd7a0394
+ 00b5ee40 bytes f4ed0394
- 00aff11c ["INT_ADD", "register:40f0:8", ["const:aff11c:8", "const:4:8"]]
- 00aff11c ["CALL", null, ["callee:00c5a800:8"]]
+ 00b5eea0 ["INT_ADD", "register:40f0:8", ["const:b5eea0:8", "const:4:8"]]
+ 00b5eea0 ["CALL", null, ["callee:00c5a800:8"]]
- 00aff11c bytes 217b0394
+ 00b5eea0 bytes 58ee0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51322daa1761ab30e22408a75e2a6eef"></a>

### [`00aff214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00aff214.md) → [`00b5ef98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5e/00b5ef98.md) _ZN8firebase26ReferenceCountedFutureImpl11BackingDataEPNS_17FutureBackingDataE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 1件 [`00bddfb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfb0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5aa30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa30.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-515235173744e33cae7c1bece43523a3"></a>

### [`00aff21c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00aff21c.md) → [`00b5efa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5e/00b5efa0.md) _ZN8firebase26ReferenceCountedFutureImpl15SetBackingErrorEPNS_17FutureBackingDataEiPKc

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bddff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddff0.md) · 呼出先 2件 [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bde230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde230.md)
- 新版 呼出元 1件 [`00c5aa70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa70.md) · 呼出先 2件 [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c5acb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5acb0.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 58.82% / 新版 58.82%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aff21c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aff21c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aff220"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aff21c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aff220",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b5efbc",
      "PARAM",
      [
        "storage",
        "002967d9",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b5efa0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b5efa4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b5efbc",
      "PARAM",
      [
        "storage",
        "002a630e",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aff21c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00aff21c.md#insn-00aff21c) · [`00aff220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00aff21c.md#insn-00aff220) · [`00aff234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00aff21c.md#insn-00aff234)

~~~diff
- 00aff21c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00aff21c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00aff21c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00aff21c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aff21c bytes f44fbea9
- 00aff220 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aff220 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aff220 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00aff220 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aff220 bytes fd7b01a9
- 00aff234 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00aff234 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00aff234 ["COPY", "tmp:0:8", ["register:4018:8"]]
- 00aff234 ["COPY", "register:4098:8", ["tmp:0:8"]]
- 00aff234 bytes 1301839a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4291f10a9f3d6a1dd3892472f3024788"></a>

### [`00aff260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00aff260.md) → [`00b5efe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5e/00b5efe4.md) _ZN8firebase26ReferenceCountedFutureImpl13CompleteProxyEPNS_17FutureBackingDataE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bddfd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfd0.md) · 呼出先 4件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdee00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdee00.md)
- 新版 呼出元 1件 [`00c5aa50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa50.md) · 呼出先 4件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a9a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a9a0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 91.07% / 新版 91.07%

CFGの説明率　旧版 47.62% / 新版 58.82%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aff284"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b5f008"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aff28c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aff284",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aff28c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5f094"
      ]
    ],
    [
      "00b5f04c",
      "READ",
      [
        "storage",
        "00c1b9a8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b5f008",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00b5f010",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5f094"
      ]
    ],
    [
      "00b5f04c",
      "READ",
      [
        "storage",
        "00c9b3a8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aff284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00aff260.md#insn-00aff284) · [`00aff28c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00aff260.md#insn-00aff28c) · [`00aff2e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00aff260.md#insn-00aff2e8)

~~~diff
- 00aff284 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00aff284 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00aff284 bytes e80700f9
- 00aff28c ["INT_EQUAL", "tmp:0:1", ["register:40c0:8", "const:0:8"]]
- 00aff28c ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 00aff28c bytes 380400b4
- 00aff2e8 ["CBRANCH", null, ["local:b8:8", "register:101:1"]]
- 00aff2e8 bytes 40ffff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eec25443f5f35b62a9dd78678e5786f2"></a>

### [`00aff340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00aff340.md) → [`00b5f0c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5f/00b5f0c4.md) _ZN8firebase26ReferenceCountedFutureImpl14CompleteHandleERKNS_12FutureHandleE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bddfe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfe0.md) · 呼出先 3件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 1件 [`00c5aa60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa60.md) · 呼出先 3件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 88.64% / 新版 88.64%

CFGの説明率　旧版 10.34% / 新版 17.65%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aff37c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b5f100"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5f0e0",
      "incomplete_value": true,
      "site": "00b5f0e4",
      "value": [
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
    },
    "old": null,
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
      "unmatched:00aff3a8",
      "PARAM",
      [
        "storage",
        "002a70e8",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00aff3c0",
      "PARAM",
      [
        "storage",
        "002a2e07",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b5f12c",
      "PARAM",
      [
        "storage",
        "002b7c50",
        null,
        "string"
      ]
    ],
    [
      "00b5f144",
      "PARAM",
      [
        "storage",
        "002b350f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aff360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00aff340.md#insn-00aff360) · [`00aff37c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00aff340.md#insn-00aff37c) · [`00aff3ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00aff340.md#insn-00aff3ac)
- 新版 [`00b5f0e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5f/00b5f0c4.md#insn-00b5f0e4) · [`00b5f130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5f/00b5f0c4.md#insn-00b5f130)

~~~diff
- 00aff360 ["INT_ADD", "register:40f0:8", ["const:aff360:8", "const:4:8"]]
- 00aff360 ["CALL", null, ["callee:00c5a600:8"]]
+ 00b5f0e4 ["INT_ADD", "register:40f0:8", ["const:b5f0e4:8", "const:4:8"]]
+ 00b5f0e4 ["CALL", null, ["callee:00c5a600:8"]]
- 00aff360 bytes 307a0394
+ 00b5f0e4 bytes 47ed0394
- 00aff37c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00aff37c ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00aff37c ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00aff37c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00aff37c bytes 0831899a
- 00aff3ac ["INT_ADD", "register:40f0:8", ["const:aff3ac:8", "const:4:8"]]
- 00aff3ac ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b5f130 ["INT_ADD", "register:40f0:8", ["const:b5f130:8", "const:4:8"]]
+ 00b5f130 ["CALL", null, ["callee:00c5ac00:8"]]
- 00aff3ac bytes 757b0394
+ 00b5f130 bytes b4ee0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06f482f6a30a24b138b47ec3e2f48542"></a>

### [`00aff3f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00aff3f0.md) → [`00b5f174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5f/00b5f174.md) _ZN8firebase26ReferenceCountedFutureImpl17BackingFromHandleEm

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde000.md) · 呼出先 2件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)
- 新版 呼出元 1件 [`00c5aa80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa80.md) · 呼出先 2件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 39.39% / 新版 39.39%

CFGの説明率　旧版 3.45% / 新版 9.09%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aff3f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aff3f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aff3f4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aff3f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aff3f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aff3f8",
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
      "00b5f174",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b5f178",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b5f17c",
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

- 旧版 [`00aff3f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00aff3f0.md#insn-00aff3f0) · [`00aff3f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00aff3f0.md#insn-00aff3f4) · [`00aff3f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00aff3f0.md#insn-00aff3f8)

~~~diff
- 00aff3f0 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00aff3f0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00aff3f0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aff3f0 bytes f50f1df8
- 00aff3f4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00aff3f4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00aff3f4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00aff3f4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aff3f4 bytes f44f01a9
- 00aff3f8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aff3f8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aff3f8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00aff3f8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aff3f8 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-739c3d4c952fc8663baef46ec5f9907f"></a>

### [`00aff474`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00aff474.md) → [`00b5f1f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5f/00b5f1f8.md) _ZN8firebase26ReferenceCountedFutureImpl27ReleaseMutexAndRunCallbacksERKNS_12FutureHandleE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde010.md) · 呼出先 10件 [`00b00d00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00d00.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)
- 新版 呼出元 1件 [`00c5aa90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa90.md) · 呼出先 10件 [`00b60a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60a84.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 47.80% / 新版 47.80%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 16件, `store_condition` 4件, `unresolved_branch_alignment` 16件, `unresolved_call_alignment` 12件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 23件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aff478"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aff478"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aff47c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aff478",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aff47c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aff480",
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
      "00b5f1fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b5f200",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b5f204",
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

- 旧版 [`00aff478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00aff474.md#insn-00aff478) · [`00aff47c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00aff474.md#insn-00aff47c) · [`00aff480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00aff474.md#insn-00aff480)

~~~diff
- 00aff478 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00aff478 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00aff478 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00aff478 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aff478 bytes fc6f05a9
- 00aff47c ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00aff47c ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00aff47c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00aff47c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aff47c bytes fa6706a9
- 00aff480 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00aff480 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00aff480 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00aff480 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aff480 bytes f85f07a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-211469be99d9e78de5b14dc9b7943b22"></a>

### [`00aff7a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00aff7a8.md) → [`00b5f52c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5f/00b5f52c.md) _ZN8firebase26ReferenceCountedFutureImpl11RunCallbackEPNS_10FutureBaseEPFvRKS1_PvES5_

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 72.00% / 新版 72.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 4件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aff7a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aff7ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aff7ac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aff7a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aff7ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aff7b0",
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
      "00b5f52c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b5f530",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b5f534",
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

- 旧版 [`00aff7a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00aff7a8.md#insn-00aff7a8) · [`00aff7ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00aff7a8.md#insn-00aff7ac) · [`00aff7b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00aff7a8.md#insn-00aff7b0)

~~~diff
- 00aff7a8 ["COPY", "tmp:0:8", ["register:40b8:8"]]
- 00aff7a8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00aff7a8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aff7a8 bytes f70f1cf8
- 00aff7ac ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00aff7ac ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00aff7ac ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00aff7ac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aff7ac bytes f65701a9
- 00aff7b0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00aff7b0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00aff7b0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00aff7b0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aff7b0 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-657998c12f321b857c342e15503a116f"></a>

### [`00aff80c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00aff80c.md) → [`00b5f590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5f/00b5f590.md) _ZNK8firebase26ReferenceCountedFutureImpl11is_orphanedEv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde1f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde1f0.md) · 呼出先 2件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)
- 新版 呼出元 1件 [`00c5ac70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac70.md) · 呼出先 2件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aff80c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aff80c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aff810"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aff80c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aff810",
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
      "00b5f590",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b5f594",
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

- 旧版 [`00aff80c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00aff80c.md#insn-00aff80c) · [`00aff810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00aff80c.md#insn-00aff810) · [`00aff824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00aff80c.md#insn-00aff824)
- 新版 [`00b5f5a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5f/00b5f590.md#insn-00b5f5a8)

~~~diff
- 00aff80c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00aff80c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00aff80c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00aff80c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aff80c bytes f44fbea9
- 00aff810 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aff810 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aff810 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00aff810 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aff810 bytes fd7b01a9
- 00aff824 ["INT_ADD", "register:40f0:8", ["const:aff824:8", "const:4:8"]]
- 00aff824 ["CALL", null, ["callee:00c5a600:8"]]
+ 00b5f5a8 ["INT_ADD", "register:40f0:8", ["const:b5f5a8:8", "const:4:8"]]
+ 00b5f5a8 ["CALL", null, ["callee:00c5a600:8"]]
- 00aff824 bytes ff780394
+ 00b5f5a8 bytes 16ec0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8be0b10c4b69d5aafe9d3d1a4e79f8ea"></a>

### [`00aff8a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00aff8a8.md) → [`00b5f62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5f/00b5f62c.md) _ZN8firebase26ReferenceCountedFutureImpl26UnregisterFutureForCleanupEPNS_10FutureBaseE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdddb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdddb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5a810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a810.md)

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aff8ac",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5a810"
      ]
    ]
  ],
  "added": [
    [
      "00b5f630",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5a810"
      ]
    ]
  ]
}
~~~


<a id="compare-44b36b5227f23bba7647b39bad8bb2cb"></a>

### [`00aff94c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00aff94c.md) → [`00b5f6d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5f/00b5f6d0.md) _ZN8firebase26ReferenceCountedFutureImpl13ReleaseFutureERKNS_12FutureHandleE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde750.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5b1d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1d0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 82.19% / 新版 82.19%

CFGの説明率　旧版 23.81% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 6件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00affa38"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b5f7bc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aff97c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aff97c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5f7e0"
      ]
    ],
    [
      "unmatched:00aff998",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5f708"
      ]
    ],
    [
      "unmatched:00aff9a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5f7e0"
      ]
    ]
  ],
  "added": [
    [
      "00b5f700",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5f7e0"
      ]
    ],
    [
      "00b5f71c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5f708"
      ]
    ],
    [
      "00b5f724",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5f7e0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aff97c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00aff94c.md#insn-00aff97c) · [`00aff990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00aff94c.md#insn-00aff990) · [`00aff998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00aff94c.md#insn-00aff998)

~~~diff
- 00aff97c ["INT_EQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
- 00aff97c ["CBRANCH", null, ["local:b30:8", "tmp:0:1"]]
- 00aff97c bytes 0a0700b4
- 00aff990 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00aff990 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00aff990 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00aff990 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00aff990 bytes b5328a9a
- 00aff998 ["INT_NOTEQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
- 00aff998 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00aff998 bytes 6affffb5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd305a4e5f96138bd72a67c14206a088"></a>

### [`00affa70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00affa70.md) → [`00b5f7f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5f/00b5f7f4.md) _ZNK8firebase26ReferenceCountedFutureImpl15GetFutureStatusERKNS_12FutureHandleE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 26.32% / 新版 35.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00affa70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00affa74"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00affa74"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00affa70",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00affa74",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00affa78",
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
      "00b5f7f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b5f7f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b5f7fc",
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

- 旧版 [`00affa70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00affa70.md#insn-00affa70) · [`00affa74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00affa70.md#insn-00affa74) · [`00affa78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00affa70.md#insn-00affa78)

~~~diff
- 00affa70 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00affa70 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00affa70 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00affa70 bytes f50f1df8
- 00affa74 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00affa74 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00affa74 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00affa74 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00affa74 bytes f44f01a9
- 00affa78 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00affa78 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00affa78 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00affa78 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00affa78 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a42b39bd2e4b1f522532bfec23405631"></a>

### [`00affb18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00affb18.md) → [`00b5f89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5f/00b5f89c.md) _ZNK8firebase26ReferenceCountedFutureImpl14GetFutureErrorERKNS_12FutureHandleE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 78.57% / 新版 78.57%

CFGの説明率　旧版 15.38% / 新版 26.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `return_value_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00affb18"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00affb1c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00affb1c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00affb18",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00affb1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00affb20",
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
      "00b5f89c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b5f8a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b5f8a4",
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

- 旧版 [`00affb18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00affb18.md#insn-00affb18) · [`00affb1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00affb18.md#insn-00affb1c) · [`00affb20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00affb18.md#insn-00affb20)

~~~diff
- 00affb18 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00affb18 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00affb18 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00affb18 bytes f50f1df8
- 00affb1c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00affb1c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00affb1c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00affb1c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00affb1c bytes f44f01a9
- 00affb20 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00affb20 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00affb20 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00affb20 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00affb20 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e99c231cd00b986c200c203e31a066c9"></a>

### [`00affbc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00affbc0.md) → [`00b5f944`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5f/00b5f944.md) _ZNK8firebase26ReferenceCountedFutureImpl21GetFutureErrorMessageERKNS_12FutureHandleE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 79.17% / 新版 79.17%

CFGの説明率　旧版 37.50% / 新版 52.94%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00affbc0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00affbc4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00affbc4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00affbc0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00affbc4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00affbc8",
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
      "00b5f944",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b5f948",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b5f94c",
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

- 旧版 [`00affbc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00affbc0.md#insn-00affbc0) · [`00affbc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00affbc0.md#insn-00affbc4) · [`00affbc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00affbc0.md#insn-00affbc8)

~~~diff
- 00affbc0 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00affbc0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00affbc0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00affbc0 bytes f50f1df8
- 00affbc4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00affbc4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00affbc4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00affbc4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00affbc4 bytes f44f01a9
- 00affbc8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00affbc8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00affbc8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00affbc8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00affbc8 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce8bfbdff1014599a52aeee6bb9a3439"></a>

### [`00affc80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00affc80.md) → [`00b5fa04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5f/00b5fa04.md) _ZNK8firebase26ReferenceCountedFutureImpl15GetFutureResultERKNS_12FutureHandleE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 81.82% / 新版 81.82%

CFGの説明率　旧版 17.39% / 新版 23.53%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `return_value_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00affc80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00affc84"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00affc84"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00affc80",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00affc84",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00affc88",
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
      "00b5fa04",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b5fa08",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b5fa0c",
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

- 旧版 [`00affc80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00affc80.md#insn-00affc80) · [`00affc84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00affc80.md#insn-00affc84) · [`00affc88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00affc80.md#insn-00affc88)

~~~diff
- 00affc80 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00affc80 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00affc80 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00affc80 bytes f50f1df8
- 00affc84 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00affc84 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00affc84 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00affc84 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00affc84 bytes f44f01a9
- 00affc88 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00affc88 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00affc88 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00affc88 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00affc88 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20cdb9445847d2d563424240cf7c4a5e"></a>

### [`00affd30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00affd30.md) → [`00b5fab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5f/00b5fab4.md) _ZN8firebase26ReferenceCountedFutureImpl21AddCompletionCallbackERKNS_12FutureHandleEPFvRKNS_10FutureBaseEPvES7_PFvS7_Eb

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bde010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde010.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5aa90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa90.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 79.82% / 新版 79.82%

CFGの説明率　旧版 6.45% / 新版 11.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00affdf4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00affe58"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00affe90"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00affda0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5fb58"
      ]
    ],
    [
      "unmatched:00affdf8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57ab0"
      ]
    ],
    [
      "unmatched:00affe38",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5fc40"
      ]
    ]
  ],
  "added": [
    [
      "00b5fb24",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5fb58"
      ]
    ],
    [
      "00b5fbbc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5fc40"
      ]
    ],
    [
      "00b5fbc4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5fbd8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00affd88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00affd30.md#insn-00affd88) · [`00affda0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00affd30.md#insn-00affda0) · [`00affdb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00affd30.md#insn-00affdb4)
- 新版 [`00b5fb0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5f/00b5fab4.md#insn-00b5fb0c)

~~~diff
- 00affd88 ["INT_ADD", "register:40f0:8", ["const:affd88:8", "const:4:8"]]
- 00affd88 ["CALL", null, ["callee:00c5a600:8"]]
+ 00b5fb0c ["INT_ADD", "register:40f0:8", ["const:b5fb0c:8", "const:4:8"]]
+ 00b5fb0c ["CALL", null, ["callee:00c5a600:8"]]
- 00affd88 bytes a6770394
+ 00b5fb0c bytes bdea0394
- 00affda0 ["INT_EQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
- 00affda0 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
- 00affda0 bytes aa0100b4
- 00affdb4 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00affdb4 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00affdb4 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00affdb4 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00affdb4 bytes 08318a9a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb2b6ab693adad1dce8a92843c4b1286"></a>

### [`00affee4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00affee4.md) → [`00b5fc68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5f/00b5fc68.md) _ZN8firebase26ReferenceCountedFutureImpl24RemoveCompletionCallbackERKNS_12FutureHandleENS_6detail24CompletionCallbackHandleE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 73.60% / 新版 73.60%

CFGの説明率　旧版 26.39% / 新版 35.85%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 7件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00affee8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00affeec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00affeec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00affee8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00affeec",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00affef0",
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
      "00b5fc6c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b5fc70",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b5fc74",
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

- 旧版 [`00affee8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00affee4.md#insn-00affee8) · [`00affeec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00affee4.md#insn-00affeec) · [`00affef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00affee4.md#insn-00affef0)

~~~diff
- 00affee8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:30:8"]]
- 00affee8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 00affee8 bytes f71b00f9
- 00affeec ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00affeec ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00affeec ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00affeec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00affeec bytes f65704a9
- 00affef0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00affef0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00affef0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00affef0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00affef0 bytes f44f05a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da58143d972a2f40959bc21007666d26"></a>

### [`00b000d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b000d8.md) → [`00b5fe5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5f/00b5fe5c.md) _ZN8firebase26ReferenceCountedFutureImpl27AddCompletionCallbackLambdaERKNS_12FutureHandleENSt6__ndk18functionIFvRKNS_10FutureBaseEEEEb

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`00b002e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b002e8.md) [`00b00320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00320.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00b6006c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b6006c.md) [`00b600a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b600a4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 81.82% / 新版 81.82%

CFGの説明率　旧版 11.48% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_condition` 2件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 12件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b000e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b000e8"
    }
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00b5fef4",
      "incomplete_value": false,
      "site": "00b5fef4",
      "value": [
        "leaf",
        "const:b6006c:8"
      ]
    },
    "old": {
      "definition_site": "00b00170",
      "incomplete_value": false,
      "site": "00b00170",
      "value": [
        "leaf",
        "const:b002e8:8"
      ]
    },
    "ordinal": 12,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b000e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b00128",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5fed0"
      ]
    ],
    [
      "00b5fef4",
      "DATA",
      [
        "storage",
        "00b002e8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b5fe6c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b5feac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b5fed0"
      ]
    ],
    [
      "00b5fef4",
      "DATA",
      [
        "storage",
        "00b6006c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b000e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b000d8.md#insn-00b000e8) · [`00b00108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b000d8.md#insn-00b00108) · [`00b00128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b000d8.md#insn-00b00128)
- 新版 [`00b5fe8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5f/00b5fe5c.md#insn-00b5fe8c)

~~~diff
- 00b000e8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b000e8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b000e8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b000e8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b000e8 bytes fd7b04a9
- 00b00108 ["INT_ADD", "register:40f0:8", ["const:b00108:8", "const:4:8"]]
- 00b00108 ["CALL", null, ["callee:00c57a90:8"]]
+ 00b5fe8c ["INT_ADD", "register:40f0:8", ["const:b5fe8c:8", "const:4:8"]]
+ 00b5fe8c ["CALL", null, ["callee:00c57a90:8"]]
- 00b00108 bytes ce6b0394
+ 00b5fe8c bytes 01df0394
- 00b00128 ["CBRANCH", null, ["local:b10:8", "register:101:1"]]
- 00b00128 bytes 20010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92c47ff92abae6ce392a357e4d307826"></a>

### [`00b00320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00320.md) → [`00b600a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b600a4.md) FUN_00b600a4

採用 · 移動量 `+0x5fd84` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`00b000d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b000d8.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00b5fe5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5f/00b5fe5c.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 70.00% / 新版 77.78%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0035c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00320.md#insn-00b0035c)
- 新版 [`00b600e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b600a4.md#insn-00b600e0)

~~~diff
- 00b0035c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b0035c ["INT_ADD", "register:40f0:8", ["const:b0035c:8", "const:4:8"]]
- 00b0035c ["CALLIND", null, ["register:0:8"]]
+ 00b600e0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b600e0 ["INT_ADD", "register:40f0:8", ["const:b600e0:8", "const:4:8"]]
+ 00b600e0 ["CALLIND", null, ["register:0:8"]]
- 00b0035c bytes 00013fd6
+ 00b600e0 bytes 00013fd6
~~~


<a id="compare-45b65b0391bab9a75bc84037e0263481"></a>

### [`00b00430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00430.md) → [`00b601b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b601b4.md) _ZNK8firebase26ReferenceCountedFutureImpl17IsRunningCallbackEv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b00430"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b00430"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b00434"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b00430",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b00434",
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
      "00b601b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b601b8",
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

- 旧版 [`00b00430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00430.md#insn-00b00430) · [`00b00434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00430.md#insn-00b00434) · [`00b00448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00430.md#insn-00b00448)
- 新版 [`00b601cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b601b4.md#insn-00b601cc)

~~~diff
- 00b00430 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b00430 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b00430 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b00430 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b00430 bytes f44fbea9
- 00b00434 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b00434 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b00434 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b00434 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b00434 bytes fd7b01a9
- 00b00448 ["INT_ADD", "register:40f0:8", ["const:b00448:8", "const:4:8"]]
- 00b00448 ["CALL", null, ["callee:00c5a600:8"]]
+ 00b601cc ["INT_ADD", "register:40f0:8", ["const:b601cc:8", "const:4:8"]]
+ 00b601cc ["CALL", null, ["callee:00c5a600:8"]]
- 00b00448 bytes f6750394
+ 00b601cc bytes 0de90394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-859c7b2b5cb0c88d85b384662fcf77d6"></a>

### [`00b005bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b005bc.md) → [`00b60340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60340.md) _ZN8firebase26ReferenceCountedFutureImpl14SetContextDataERKNS_12FutureHandleEPvPFvS4_E

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdede0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdede0.md) · 呼出先 3件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 1件 [`00c5b8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b8a0.md) · 呼出先 3件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.92% / 新版 97.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b603f0",
      "incomplete_value": false,
      "site": "00b603f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:aae:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0066c",
      "incomplete_value": false,
      "site": "00b00670",
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
            "const:e32:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b603f0",
      "PARAM",
      [
        "storage",
        "002a7e32",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b603f0",
      "PARAM",
      [
        "storage",
        "002b8aae",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b00670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b005bc.md#insn-00b00670) · [`00b005e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b005bc.md#insn-00b005e8) · [`00b005f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b005bc.md#insn-00b005f4)
- 新版 [`00b603f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60340.md#insn-00b603f4) · [`00b6036c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60340.md#insn-00b6036c) · [`00b60378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60340.md#insn-00b60378)

~~~diff
- 00b00670 ["INT_ADD", "register:40f0:8", ["const:b00670:8", "const:4:8"]]
- 00b00670 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b603f4 ["INT_ADD", "register:40f0:8", ["const:b603f4:8", "const:4:8"]]
+ 00b603f4 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b00670 bytes c4760394
+ 00b603f4 bytes 03ea0394
- 00b005e8 ["INT_ADD", "register:40f0:8", ["const:b005e8:8", "const:4:8"]]
- 00b005e8 ["CALL", null, ["callee:00c5a600:8"]]
+ 00b6036c ["INT_ADD", "register:40f0:8", ["const:b6036c:8", "const:4:8"]]
+ 00b6036c ["CALL", null, ["callee:00c5a600:8"]]
- 00b005e8 bytes 8e750394
+ 00b6036c bytes a5e80394
- 00b005f4 ["INT_ADD", "register:40f0:8", ["const:b005f4:8", "const:4:8"]]
- 00b005f4 ["CALL", null, ["callee:00c5a600:8"]]
+ 00b60378 ["INT_ADD", "register:40f0:8", ["const:b60378:8", "const:4:8"]]
+ 00b60378 ["CALL", null, ["callee:00c5a600:8"]]
- 00b005f4 bytes 8b750394
+ 00b60378 bytes a2e80394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f350309aeff6a914321870ef13125fb"></a>

### [`00b0067c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b0067c.md) → [`00b60400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60400.md) _ZN8firebase26ReferenceCountedFutureImpl15LastResultProxyEi

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdedf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdedf0.md) · 呼出先 15件 [`00b00a84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00a84.md) [`00b00d00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00d00.md) [`00b010f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b010f8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00c5b8b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b8b0.md) · 呼出先 15件 [`00b60808`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60808.md) [`00b60a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60a84.md) [`00b60d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60d10.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 98.06% / 新版 98.06%

CFGの説明率　旧版 81.13% / 新版 74.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 3件, `unresolved_branch_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b007cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b60550"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b604b8",
      "incomplete_value": false,
      "site": "00b604c4",
      "value": [
        "leaf",
        "const:b60a84:8"
      ]
    },
    "old": {
      "definition_site": "00b00734",
      "incomplete_value": false,
      "site": "00b00740",
      "value": [
        "leaf",
        "const:b00d00:8"
      ]
    },
    "ordinal": 6,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b604b8",
      "PARAM",
      [
        "storage",
        "00b00d00",
        null,
        null
      ]
    ],
    [
      "unmatched:00b007cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6057c"
      ]
    ],
    [
      "00b6056c",
      "PARAM",
      [
        "storage",
        "00b00d00",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b604b8",
      "PARAM",
      [
        "storage",
        "00b60a84",
        null,
        null
      ]
    ],
    [
      "00b60550",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6057c"
      ]
    ],
    [
      "00b6056c",
      "PARAM",
      [
        "storage",
        "00b60a84",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b00740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b0067c.md#insn-00b00740) · [`00b007cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b0067c.md#insn-00b007cc) · [`00b007f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b0067c.md#insn-00b007f4)
- 新版 [`00b604c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60400.md#insn-00b604c4) · [`00b60578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60400.md#insn-00b60578)

~~~diff
- 00b00740 ["INT_ADD", "register:40f0:8", ["const:b00740:8", "const:4:8"]]
- 00b00740 ["CALL", null, ["callee:00c5a800:8"]]
+ 00b604c4 ["INT_ADD", "register:40f0:8", ["const:b604c4:8", "const:4:8"]]
+ 00b604c4 ["CALL", null, ["callee:00c5a800:8"]]
- 00b00740 bytes 98750394
+ 00b604c4 bytes cfe80394
- 00b007cc ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00b007cc ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 00b007cc bytes 600100b4
- 00b007f4 ["INT_ADD", "register:40f0:8", ["const:b007f4:8", "const:4:8"]]
- 00b007f4 ["CALL", null, ["callee:00c5a800:8"]]
+ 00b60578 ["INT_ADD", "register:40f0:8", ["const:b60578:8", "const:4:8"]]
+ 00b60578 ["CALL", null, ["callee:00c5a800:8"]]
- 00b007f4 bytes 6b750394
+ 00b60578 bytes a2e80394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c237ff416f71ea9c1509dea2d9f4c066"></a>

### [`00b00a84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00a84.md) → [`00b60808`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60808.md) FUN_00b60808

採用 · 移動量 `+0x5fd84` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b0067c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b0067c.md) · 呼出先 6件 [`00b00d00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00d00.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddda0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddda0.md)
- 新版 呼出元 1件 [`00b60400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60400.md) · 呼出先 6件 [`00b60a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60a84.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a800.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 93.24% / 新版 93.24%

CFGの説明率　旧版 80.00% / 新版 72.73%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b00b14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b00b1c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b60898"
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
      "00b60890",
      "READ",
      [
        "storage",
        "00c1b9a8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b00b10",
      "READ",
      [
        "storage",
        "010a0d58",
        "_ZN8firebase26ReferenceCountedFutureImpl14kInvalidHandleE",
        "undefined8"
      ]
    ],
    [
      "unmatched:00b00b18",
      "READ",
      [
        "storage",
        "010a0d60",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b60890",
      "READ",
      [
        "storage",
        "00c9b3a8",
        null,
        "pointer"
      ]
    ],
    [
      "00b60894",
      "READ",
      [
        "storage",
        "01125c18",
        "_ZN8firebase26ReferenceCountedFutureImpl14kInvalidHandleE",
        "undefined8"
      ]
    ],
    [
      "00b6089c",
      "READ",
      [
        "storage",
        "01125c20",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b00b14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00a84.md#insn-00b00b14) · [`00b00b1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00a84.md#insn-00b00b1c) · [`00b00b20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00a84.md#insn-00b00b20)

~~~diff
- 00b00b14 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b00b14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00b00b14 bytes a90200f9
- 00b00b1c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:8:8"]]
- 00b00b1c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b00b1c bytes a00600f9
- 00b00b20 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00b00b20 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 00b00b20 bytes 600100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2fcd2838266807c6b3e0620ad4181682"></a>

### [`00b00bac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00bac.md) → [`00b60930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60930.md) _ZN8firebase10CleanupMgrEPNS_6detail18FutureApiInterfaceE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-9cf593fe15003493c32ca8dc8786ce7d"></a>

### [`00b00bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00bb4.md) → [`00b60938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60938.md) _ZN8firebase26ReferenceCountedFutureImpl18ForceReleaseFutureERKNS_12FutureHandleE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdee10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdee10.md) · 呼出先 2件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)
- 新版 呼出元 1件 [`00c5b8c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b8c0.md) · 呼出先 2件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 80.43% / 新版 80.43%

CFGの説明率　旧版 35.71% / 新版 31.25%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b00bb4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b00bb4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b00bb8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b00bb4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b00bb8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b00bbc",
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
      "00b60938",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b6093c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b60940",
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

- 旧版 [`00b00bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00bb4.md#insn-00b00bb4) · [`00b00bb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00bb4.md#insn-00b00bb8) · [`00b00bbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00bb4.md#insn-00b00bbc)

~~~diff
- 00b00bb4 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b00bb4 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b00bb4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b00bb4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b00bb4 bytes f657bda9
- 00b00bb8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b00bb8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b00bb8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b00bb8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b00bb8 bytes f44f01a9
- 00b00bbc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b00bbc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b00bbc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b00bbc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b00bbc bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3052778d47778c55cb64de709550cb41"></a>

### [`00b00d08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00d08.md) → [`00b60a8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60a8c.md) _ZN8firebase12FutureHandleD2Ev

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b01370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01370.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md) · 呼出先 1件 [`00bdddb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdddb0.md)
- 新版 呼出元 2件 [`00b60f88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60f88.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) · 呼出先 1件 [`00c5a810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a810.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件, `store_condition` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b00d18"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b60a9c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b60aa8",
      "incomplete_value": true,
      "site": "00b60aac",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "old": {
      "definition_site": "00b00d24",
      "incomplete_value": true,
      "site": "00b00d28",
      "value": [
        "live",
        "register:4000:8"
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
      "unmatched:00b00d18",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b60ad0"
      ]
    ]
  ],
  "added": [
    [
      "00b60a9c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b60ad0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b00d18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00d08.md#insn-00b00d18) · [`00b00d28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00d08.md#insn-00b00d28)
- 新版 [`00b60aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60a8c.md#insn-00b60aac) · [`00b60a9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60a8c.md#insn-00b60a9c)

~~~diff
- 00b00d18 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b00d18 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b00d18 bytes a80100b4
- 00b00d28 ["INT_ADD", "register:40f0:8", ["const:b00d28:8", "const:4:8"]]
- 00b00d28 ["CALL", null, ["callee:00c5a810:8"]]
+ 00b60aac ["INT_ADD", "register:40f0:8", ["const:b60aac:8", "const:4:8"]]
+ 00b60aac ["CALL", null, ["callee:00c5a810:8"]]
- 00b00d28 bytes 22740394
+ 00b60aac bytes 59e70394
+ 00b60a9c ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b60a9c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b60a9c bytes a80100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ade7fdb4c7eb608c45cf90481dbbade"></a>

### [`00b00db8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00db8.md) → [`00b60b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60b3c.md) _ZN8firebase12FutureHandleaSERKS0_

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bddfa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfa0.md) · 呼出先 3件 [`00b00d00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00d00.md) [`00bddda0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddda0.md) [`00bdddb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdddb0.md)
- 新版 呼出元 1件 [`00c5aa20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa20.md) · 呼出先 3件 [`00b60a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60a84.md) [`00c5a800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a800.md) [`00c5a810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a810.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 94.29% / 新版 94.29%

CFGの説明率　旧版 12.50% / 新版 14.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b00dd0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b60b54"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b60b58",
      "incomplete_value": true,
      "site": "00b60b60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "leaf",
            "const:c8:8"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b00dd0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b60b7c"
      ]
    ],
    [
      "00b60ba8",
      "PARAM",
      [
        "storage",
        "00b00d00",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b60b54",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b60b7c"
      ]
    ],
    [
      "00b60ba8",
      "PARAM",
      [
        "storage",
        "00b60a84",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b00dd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00db8.md#insn-00b00dd0) · [`00b00ddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00db8.md#insn-00b00ddc) · [`00b00e30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00db8.md#insn-00b00e30)
- 新版 [`00b60b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60b3c.md#insn-00b60b60) · [`00b60bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60b3c.md#insn-00b60bb4)

~~~diff
- 00b00dd0 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b00dd0 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b00dd0 bytes 480100b4
- 00b00ddc ["INT_ADD", "register:40f0:8", ["const:b00ddc:8", "const:4:8"]]
- 00b00ddc ["CALL", null, ["callee:00c5a810:8"]]
+ 00b60b60 ["INT_ADD", "register:40f0:8", ["const:b60b60:8", "const:4:8"]]
+ 00b60b60 ["CALL", null, ["callee:00c5a810:8"]]
- 00b00ddc bytes f5730394
+ 00b60b60 bytes 2ce70394
- 00b00e30 ["INT_ADD", "register:40f0:8", ["const:b00e30:8", "const:4:8"]]
- 00b00e30 ["CALL", null, ["callee:00c5a800:8"]]
+ 00b60bb4 ["INT_ADD", "register:40f0:8", ["const:b60bb4:8", "const:4:8"]]
+ 00b60bb4 ["CALL", null, ["callee:00c5a800:8"]]
- 00b00e30 bytes dc730394
+ 00b60bb4 bytes 13e70394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1290f453a07c9d6cf59b8ad5f43bafe"></a>

### [`00b00e44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00e44.md) → [`00b60bc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60bc8.md) _ZN8firebase12FutureHandleC1EOS0_

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdeda0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeda0.md) · 呼出先 3件 [`00b00d00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00d00.md) [`00bddda0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddda0.md) [`00bdddb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdddb0.md)
- 新版 呼出元 1件 [`00c5b860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b860.md) · 呼出先 3件 [`00b60a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60a84.md) [`00c5a800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a800.md) [`00c5a810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a810.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 33.33% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b60c00",
      "incomplete_value": false,
      "site": "00b60c04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:b60000:8"
          ],
          [
            "leaf",
            "const:a84:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b00e7c",
      "incomplete_value": false,
      "site": "00b00e80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:b00000:8"
          ],
          [
            "leaf",
            "const:d00:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b00e8c",
      "incomplete_value": true,
      "site": "00b00e90",
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
            "const:c8:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b00e88",
      "incomplete_value": true,
      "site": "00b00e90",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "ordinal": 1,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b00e7c",
      "PARAM",
      [
        "storage",
        "00b00d00",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b60c00",
      "PARAM",
      [
        "storage",
        "00b60a84",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b00e80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00e44.md#insn-00b00e80) · [`00b00e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00e44.md#insn-00b00e90) · [`00b00e6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00e44.md#insn-00b00e6c)
- 新版 [`00b60c04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60bc8.md#insn-00b60c04) · [`00b60c14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60bc8.md#insn-00b60c14) · [`00b60bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60bc8.md#insn-00b60bf0)

~~~diff
- 00b00e80 ["INT_ADD", "register:40f0:8", ["const:b00e80:8", "const:4:8"]]
- 00b00e80 ["CALL", null, ["callee:00c5a800:8"]]
+ 00b60c04 ["INT_ADD", "register:40f0:8", ["const:b60c04:8", "const:4:8"]]
+ 00b60c04 ["CALL", null, ["callee:00c5a800:8"]]
- 00b00e80 bytes c8730394
+ 00b60c04 bytes ffe60394
- 00b00e90 ["INT_ADD", "register:40f0:8", ["const:b00e90:8", "const:4:8"]]
- 00b00e90 ["CALL", null, ["callee:00c5a810:8"]]
+ 00b60c14 ["INT_ADD", "register:40f0:8", ["const:b60c14:8", "const:4:8"]]
+ 00b60c14 ["CALL", null, ["callee:00c5a810:8"]]
- 00b00e90 bytes c8730394
+ 00b60c14 bytes ffe60394
- 00b00e6c ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00b00e6c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b60bf0 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
+ 00b60bf0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b00e6c bytes 490100b4
+ 00b60bf0 bytes 490100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-121bb18b0c823828280d81e7814ce2b9"></a>

### [`00b00ea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00ea4.md) → [`00b60c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60c28.md) _ZN8firebase12FutureHandleaSEOS0_

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdedb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdedb0.md) · 呼出先 3件 [`00b00d00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00d00.md) [`00bddda0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddda0.md) [`00bdddb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdddb0.md)
- 新版 呼出元 1件 [`00c5b870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b870.md) · 呼出先 3件 [`00b60a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60a84.md) [`00c5a800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a800.md) [`00c5a810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a810.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.30% / 新版 97.30%

CFGの説明率　旧版 66.67% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b60c8c",
      "incomplete_value": false,
      "site": "00b60c94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:b60000:8"
          ],
          [
            "leaf",
            "const:a84:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b00f08",
      "incomplete_value": false,
      "site": "00b00f10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:b00000:8"
          ],
          [
            "leaf",
            "const:d00:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b00f1c",
      "incomplete_value": true,
      "site": "00b00f20",
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
            "const:c8:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b00f18",
      "incomplete_value": true,
      "site": "00b00f20",
      "value": [
        "live",
        "register:40a0:8"
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
      "unmatched:00b00f08",
      "PARAM",
      [
        "storage",
        "00b00d00",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b60c8c",
      "PARAM",
      [
        "storage",
        "00b60a84",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b00f10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00ea4.md#insn-00b00f10) · [`00b00f20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00ea4.md#insn-00b00f20) · [`00b00ec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00ea4.md#insn-00b00ec8)
- 新版 [`00b60c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60c28.md#insn-00b60c94) · [`00b60ca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60c28.md#insn-00b60ca4) · [`00b60c4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60c28.md#insn-00b60c4c)

~~~diff
- 00b00f10 ["INT_ADD", "register:40f0:8", ["const:b00f10:8", "const:4:8"]]
- 00b00f10 ["CALL", null, ["callee:00c5a800:8"]]
+ 00b60c94 ["INT_ADD", "register:40f0:8", ["const:b60c94:8", "const:4:8"]]
+ 00b60c94 ["CALL", null, ["callee:00c5a800:8"]]
- 00b00f10 bytes a4730394
+ 00b60c94 bytes dbe60394
- 00b00f20 ["INT_ADD", "register:40f0:8", ["const:b00f20:8", "const:4:8"]]
- 00b00f20 ["CALL", null, ["callee:00c5a810:8"]]
+ 00b60ca4 ["INT_ADD", "register:40f0:8", ["const:b60ca4:8", "const:4:8"]]
+ 00b60ca4 ["CALL", null, ["callee:00c5a810:8"]]
- 00b00f20 bytes a4730394
+ 00b60ca4 bytes dbe60394
- 00b00ec8 ["INT_ADD", "register:40f0:8", ["const:b00ec8:8", "const:4:8"]]
- 00b00ec8 ["CALL", null, ["callee:00c5a810:8"]]
+ 00b60c4c ["INT_ADD", "register:40f0:8", ["const:b60c4c:8", "const:4:8"]]
+ 00b60c4c ["CALL", null, ["callee:00c5a810:8"]]
- 00b00ec8 bytes ba730394
+ 00b60c4c bytes f1e60394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-221a7fa0f913f4b3929a2b5b4bd37906"></a>

### [`00b00f38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00f38.md) → [`00b60cbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60cbc.md) _ZN8firebase12FutureHandle6DetachEv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change` · `reordered`

- 旧版 呼出元 1件 [`00bddf70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf70.md) · 呼出先 1件 [`00bdddb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdddb0.md)
- 新版 呼出元 1件 [`00c5a9f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a9f0.md) · 呼出先 1件 [`00c5a810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a810.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 33.33% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b00f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00f38.md#insn-00b00f48) · [`00b00f58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00f38.md#insn-00b00f58) · [`00b00f6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00f38.md#insn-00b00f6c)
- 新版 [`00b60ccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60cbc.md#insn-00b60ccc) · [`00b60cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60cbc.md#insn-00b60cdc) · [`00b60cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60cbc.md#insn-00b60cf0)

~~~diff
- 00b00f48 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b00f48 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b60ccc ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b60ccc ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b00f48 bytes 680100b4
+ 00b60ccc bytes 680100b4
- 00b00f58 ["INT_ADD", "register:40f0:8", ["const:b00f58:8", "const:4:8"]]
- 00b00f58 ["CALL", null, ["callee:00c5a810:8"]]
+ 00b60cdc ["INT_ADD", "register:40f0:8", ["const:b60cdc:8", "const:4:8"]]
+ 00b60cdc ["CALL", null, ["callee:00c5a810:8"]]
- 00b00f58 bytes 96730394
+ 00b60cdc bytes cde60394
- 00b00f6c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b00f6c ["INT_ADD", "register:40f0:8", ["const:b00f6c:8", "const:4:8"]]
- 00b00f6c ["CALLIND", null, ["register:0:8"]]
+ 00b60cf0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b60cf0 ["INT_ADD", "register:40f0:8", ["const:b60cf0:8", "const:4:8"]]
+ 00b60cf0 ["CALLIND", null, ["register:0:8"]]
- 00b00f6c bytes 00013fd6
+ 00b60cf0 bytes 00013fd6
~~~


<a id="compare-321c83a72c074ab5401a78b7b6f0ebc5"></a>

### [`00b00f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00f80.md) → [`00b43a88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43a88.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalIvEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS5_iS7_RKT0_

採用 · 移動量 `+0x42b08` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change` · `reordered`

- 旧版 呼出元 1件 [`00bdee00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdee00.md) · 呼出先 8件 [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddfd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfd0.md) [`00bddfe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfe0.md)
- 新版 呼出元 1件 [`00c5a9a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a9a0.md) · 呼出先 10件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5aa30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa30.md) [`00c5aa50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa50.md) [`00c5aa60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa60.md)

変更の種類 branch_condition_or_target, branch_count, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_count, unresolved_return_alignment

命令の説明率　旧版 21.98% / 新版 30.30%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_count` 6件, `call_argument_candidate` 2件, `call_count` 3件, `store_count` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b00f80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b00f80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b00f84"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b00f80",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b00f84",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b00f88",
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
      "00b43a88",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b43a8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b43a90",
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

- 旧版 [`00b00f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00f80.md#insn-00b00f80) · [`00b00f84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00f80.md#insn-00b00f84) · [`00b00f88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00f80.md#insn-00b00f88)

~~~diff
- 00b00f80 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b00f80 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b00f80 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00b00f80 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b00f80 bytes f85fbca9
- 00b00f84 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b00f84 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b00f84 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b00f84 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b00f84 bytes f65701a9
- 00b00f88 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b00f88 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b00f88 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b00f88 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b00f88 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b20cf64b120e2e38f33272d328c71a9f"></a>

### [`00b010fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b010fc.md) → [`00b60d14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60d14.md) _ZNSt6__ndk16vectorIN8firebase12FutureHandleENS_9allocatorIS2_EEE21__push_back_slow_pathIRKS2_EEvOT_

採用 · 移動量 `+0x5fc18` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdee40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdee40.md) · 呼出先 6件 [`00b00d00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00d00.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bddda0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddda0.md) [`00bdddb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdddb0.md)
- 新版 呼出元 1件 [`00c5b8f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b8f0.md) · 呼出先 6件 [`00b60a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60a84.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a800.md) [`00c5a810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a810.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 78.51% / 新版 78.51%

CFGの説明率　旧版 45.45% / 新版 34.88%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 7件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b01110"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b01110"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b01188"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b01110",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b0118c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b60dd4"
      ]
    ],
    [
      "00b60dc0",
      "PARAM",
      [
        "storage",
        "00b00d00",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b60d28",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b60da4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b60dd4"
      ]
    ],
    [
      "00b60dc0",
      "PARAM",
      [
        "storage",
        "00b60a84",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b01110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b010fc.md#insn-00b01110) · [`00b01188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b010fc.md#insn-00b01188) · [`00b0118c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b010fc.md#insn-00b0118c)

~~~diff
- 00b01110 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b01110 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b01110 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b01110 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b01110 bytes fd7b05a9
- 00b01188 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00b01188 ["INT_ADD", "register:40b0:8", ["register:40b0:8", "const:8:8"]]
- 00b01188 ["STORE", null, ["const:1b1:8", "register:40b0:8", "tmp:0:8"]]
- 00b01188 bytes c08e00f8
- 00b0118c ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00b0118c ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00b0118c bytes 800100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9530f44db8310cded8f225daab463f05"></a>

### [`00b01390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01390.md) → [`00b60fa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60fa8.md) _ZN8firebase17ModuleInitializerC1Ev

採用 · 移動量 `+0x5fc18` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bddd80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd80.md) [`00bddde0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddde0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5a7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7e0.md) [`00c5a840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a840.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_value, unresolved_return_alignment

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `store_value` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b60fc0",
      "incomplete_value": true,
      "site": "00b60fc4",
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
      "definition_site": "00b013a8",
      "incomplete_value": true,
      "site": "00b013ac",
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
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b013f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b61008"
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
      "00b60fb8",
      "READ",
      [
        "storage",
        "00c1b9d8",
        null,
        "pointer"
      ]
    ],
    [
      "00b60fc4",
      "DATA",
      [
        "storage",
        "00c109b8",
        null,
        "undefined1[32]"
      ]
    ]
  ],
  "added": [
    [
      "00b60fb8",
      "READ",
      [
        "storage",
        "00c9b3e8",
        null,
        "pointer"
      ]
    ],
    [
      "00b60fc4",
      "DATA",
      [
        "storage",
        "00c900d8",
        null,
        "undefined1[32]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b013f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01390.md#insn-00b013f0) · [`00b0139c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01390.md#insn-00b0139c)
- 新版 [`00b61008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60fa8.md#insn-00b61008) · [`00b60fb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b60/00b60fa8.md#insn-00b60fb4)

~~~diff
- 00b013f0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b013f0 ["RETURN", null, ["register:0:8"]]
- 00b013f0 bytes c0035fd6
+ 00b61008 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b61008 ["RETURN", null, ["register:0:8"]]
+ 00b61008 bytes c0035fd6
- 00b0139c ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00b60fb4 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00b0139c bytes c80800d0
+ 00b60fb4 bytes c80900f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19e0bb858fb78dbc08fca6eea62447b2"></a>

### [`00b013f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b013f4.md) → [`00b6100c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b61/00b6100c.md) _ZN8firebase17ModuleInitializerD1Ev

採用 · 移動量 `+0x5fc18` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md) [`00bdddf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdddf0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) [`00c5a850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a850.md)

変更の種類 branch_condition_or_target, call, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 66.67% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b01414"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b6102c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b01418"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b01408",
      "READ",
      [
        "storage",
        "00c1b9d8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b01414",
      "DATA",
      [
        "storage",
        "00c109b8",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "unmatched:00b01418",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6105c"
      ]
    ]
  ],
  "added": [
    [
      "00b61020",
      "READ",
      [
        "storage",
        "00c9b3e8",
        null,
        "pointer"
      ]
    ],
    [
      "00b6102c",
      "DATA",
      [
        "storage",
        "00c900d8",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "00b61030",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6105c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b01414`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b013f4.md#insn-00b01414) · [`00b01418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b013f4.md#insn-00b01418) · [`00b01430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b013f4.md#insn-00b01430)
- 新版 [`00b61048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b61/00b6100c.md#insn-00b61048)

~~~diff
- 00b01414 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00b01414 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b01414 bytes 080000f9
- 00b01418 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 00b01418 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b01418 bytes 740100b4
- 00b01430 ["INT_ADD", "register:40f0:8", ["const:b01430:8", "const:4:8"]]
- 00b01430 ["CALL", null, ["ram:bddc40:8"]]
+ 00b61048 ["INT_ADD", "register:40f0:8", ["const:b61048:8", "const:4:8"]]
+ 00b61048 ["CALL", null, ["ram:c5a690:8"]]
- 00b01430 bytes 04720394
+ 00b61048 bytes 92e50394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c501d0f1658707198c9fe087d7c24cd8"></a>

### [`00b01454`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01454.md) → [`00b6106c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b61/00b6106c.md) _ZN8firebase17ModuleInitializerD0Ev

採用 · 移動量 `+0x5fc18` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md) [`00bdddf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdddf0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) [`00c5a850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a850.md)

変更の種類 branch_condition_or_target, call, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 70.83% / 新版 70.83%

CFGの説明率　旧版 66.67% / 新版 57.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b01474"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b6108c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b610a8",
      "value": [
        "leaf",
        "ram:c5a690:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b01490",
      "value": [
        "leaf",
        "ram:bddc40:8"
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
      "unmatched:00b01468",
      "READ",
      [
        "storage",
        "00c1b9d8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b01474",
      "DATA",
      [
        "storage",
        "00c109b8",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "00b610a8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bddc40"
      ]
    ]
  ],
  "added": [
    [
      "00b61080",
      "READ",
      [
        "storage",
        "00c9b3e8",
        null,
        "pointer"
      ]
    ],
    [
      "00b6108c",
      "DATA",
      [
        "storage",
        "00c900d8",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "00b610a8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a690"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b01474`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01454.md#insn-00b01474) · [`00b01490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01454.md#insn-00b01490) · [`00b01498`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01454.md#insn-00b01498)
- 新版 [`00b610a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b61/00b6106c.md#insn-00b610a8) · [`00b610b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b61/00b6106c.md#insn-00b610b0)

~~~diff
- 00b01474 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00b01474 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b01474 bytes 080000f9
- 00b01490 ["INT_ADD", "register:40f0:8", ["const:b01490:8", "const:4:8"]]
- 00b01490 ["CALL", null, ["ram:bddc40:8"]]
+ 00b610a8 ["INT_ADD", "register:40f0:8", ["const:b610a8:8", "const:4:8"]]
+ 00b610a8 ["CALL", null, ["ram:c5a690:8"]]
- 00b01490 bytes ec710394
+ 00b610a8 bytes 7ae50394
- 00b01498 ["INT_ADD", "register:40f0:8", ["const:b01498:8", "const:4:8"]]
- 00b01498 ["CALL", null, ["ram:bdddf0:8"]]
+ 00b610b0 ["INT_ADD", "register:40f0:8", ["const:b610b0:8", "const:4:8"]]
+ 00b610b0 ["CALL", null, ["ram:c5a850:8"]]
- 00b01498 bytes 56720394
+ 00b610b0 bytes e8e50394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-384d7921217f3415f8cc91424f25ad1f"></a>

### [`00b014b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b014b4.md) → [`00b610cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b61/00b610cc.md) _ZN8firebase17ModuleInitializer10InitializeEPNS_3AppEPvPFNS_10InitResultES2_S3_E

採用 · 移動量 `+0x5fc18` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bdeea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeea0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5b950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b950.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 90.70% / 新版 90.70%

CFGの説明率　旧版 66.67% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b01548"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b61160"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b01544"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b01540",
      "PARAM",
      [
        "storage",
        "002a1ed7",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b01544",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ac00"
      ]
    ],
    [
      "unmatched:00b01548",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b61110"
      ]
    ]
  ],
  "added": [
    [
      "00b61158",
      "PARAM",
      [
        "storage",
        "002b2598",
        null,
        "string"
      ]
    ],
    [
      "00b6115c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ac00"
      ]
    ],
    [
      "00b61160",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b61110"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b01544`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b014b4.md#insn-00b01544) · [`00b01548`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b014b4.md#insn-00b01548) · [`00b01554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b014b4.md#insn-00b01554)
- 新版 [`00b6116c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b61/00b610cc.md#insn-00b6116c)

~~~diff
- 00b01544 ["INT_ADD", "register:40f0:8", ["const:b01544:8", "const:4:8"]]
- 00b01544 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b01544 bytes 0f730394
- 00b01548 ["INT_NOTEQUAL", "tmp:0:1", ["register:40b8:8", "const:0:8"]]
- 00b01548 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b01548 bytes 97fdffb5
- 00b01554 ["INT_ADD", "register:40f0:8", ["const:b01554:8", "const:4:8"]]
- 00b01554 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b6116c ["INT_ADD", "register:40f0:8", ["const:b6116c:8", "const:4:8"]]
+ 00b6116c ["CALL", null, ["callee:00c5ac00:8"]]
- 00b01554 bytes 0b730394
+ 00b6116c bytes a5e60394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c736eebe96eabfc3e8a1e343eac785a"></a>

### [`00b01560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01560.md) → [`00b61178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b61/00b61178.md) _ZN8firebase17ModuleInitializer10InitializeEPNS_3AppEPvPKPFNS_10InitResultES2_S3_Em

採用 · 移動量 `+0x5fc18` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdeea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeea0.md) · 呼出先 14件 [`00b01714`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01714.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md)
- 新版 呼出元 1件 [`00c5b950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b950.md) · 呼出先 14件 [`00b6132c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b61/00b6132c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 87.16% / 新版 87.16%

CFGの説明率　旧版 47.83% / 新版 36.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `call_target` 1件, `unresolved_call_alignment` 6件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b016d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b612e8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b015ac",
      "incomplete_value": true,
      "site": "00b015b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:18:8"
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
      "00b611bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b0168c"
      ]
    ],
    [
      "unmatched:00b015cc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bddc40"
      ]
    ],
    [
      "unmatched:00b015fc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bddc40"
      ]
    ]
  ],
  "added": [
    [
      "00b611bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b612a4"
      ]
    ],
    [
      "00b611e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a690"
      ]
    ],
    [
      "00b61214",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a690"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b015b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01560.md#insn-00b015b4) · [`00b015cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01560.md#insn-00b015cc) · [`00b015e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01560.md#insn-00b015e8)
- 新版 [`00b611cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b61/00b61178.md#insn-00b611cc) · [`00b61200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b61/00b61178.md#insn-00b61200)

~~~diff
- 00b015b4 ["INT_ADD", "register:40f0:8", ["const:b015b4:8", "const:4:8"]]
- 00b015b4 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00b611cc ["INT_ADD", "register:40f0:8", ["const:b611cc:8", "const:4:8"]]
+ 00b611cc ["CALL", null, ["callee:00c5aa00:8"]]
- 00b015b4 bytes 73720394
+ 00b611cc bytes 0de60394
- 00b015cc ["INT_ADD", "register:40f0:8", ["const:b015cc:8", "const:4:8"]]
- 00b015cc ["CALL", null, ["ram:bddc40:8"]]
- 00b015cc bytes 9d710394
- 00b015e8 ["INT_ADD", "register:40f0:8", ["const:b015e8:8", "const:4:8"]]
- 00b015e8 ["CALL", null, ["callee:00c5aa40:8"]]
+ 00b61200 ["INT_ADD", "register:40f0:8", ["const:b61200:8", "const:4:8"]]
+ 00b61200 ["CALL", null, ["callee:00c5aa40:8"]]
- 00b015e8 bytes 76720394
+ 00b61200 bytes 10e60394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86eed32eab65decff6ccbb89f60101a2"></a>

### [`00b01950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01950.md) → [`00b61584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b61/00b61584.md) _ZN8firebase11AppCallback19NotifyAllAppCreatedEPNS_3AppEPNSt6__ndk13mapINS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEENS_10In

採用 · 移動量 `+0x5fc34` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde8f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde8f0.md) · 呼出先 8件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bde730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde730.md)
- 新版 呼出元 1件 [`00c5b370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b370.md) · 呼出先 8件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5b1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1b0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 97.46% / 新版 97.46%

CFGの説明率　旧版 87.80% / 新版 83.72%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b615f8",
      "incomplete_value": true,
      "site": "00b615f8",
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
              "LOAD"
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
      "definition_site": "00b019c4",
      "incomplete_value": true,
      "site": "00b019c4",
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
              "LOAD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b01b00"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b61734"
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
      "00b615dc",
      "READ",
      [
        "storage",
        "00c1b9c0",
        null,
        "pointer"
      ]
    ],
    [
      "00b615e0",
      "READ",
      [
        "storage",
        "010a0d70",
        "_ZN8firebase11AppCallback16callbacks_mutex_E",
        "undefined8"
      ]
    ],
    [
      "00b615f0",
      "READ",
      [
        "storage",
        "00c1b9b8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b615dc",
      "READ",
      [
        "storage",
        "00c9b3c0",
        null,
        "pointer"
      ]
    ],
    [
      "00b615e0",
      "READ",
      [
        "storage",
        "01125c30",
        "_ZN8firebase11AppCallback16callbacks_mutex_E",
        "undefined8"
      ]
    ],
    [
      "00b615f0",
      "READ",
      [
        "storage",
        "00c9b3b8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b019b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01950.md#insn-00b019b4) · [`00b01b00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01950.md#insn-00b01b00) · [`00b01b20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01950.md#insn-00b01b20)
- 新版 [`00b615e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b61/00b61584.md#insn-00b615e8)

~~~diff
- 00b019b4 ["INT_ADD", "register:40f0:8", ["const:b019b4:8", "const:4:8"]]
- 00b019b4 ["CALL", null, ["callee:00c5a600:8"]]
+ 00b615e8 ["INT_ADD", "register:40f0:8", ["const:b615e8:8", "const:4:8"]]
+ 00b615e8 ["CALL", null, ["callee:00c5a600:8"]]
- 00b019b4 bytes 9b700394
+ 00b615e8 bytes 06e40394
- 00b01b00 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b01b00 ["CBRANCH", null, ["local:b26:8", "tmp:0:1"]]
- 00b01b00 bytes 21010054
- 00b01b20 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b01b20 ["RETURN", null, ["register:0:8"]]
- 00b01b20 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18bf5a87655624afcd19f603d391fa7d"></a>

### [`00b01b28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01b28.md) → [`00b6175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b61/00b6175c.md) _ZN8firebase11AppCallback21NotifyAllAppDestroyedEPNS_3AppE

採用 · 移動量 `+0x5fc34` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde900.md) · 呼出先 2件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)
- 新版 呼出元 1件 [`00c5b380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b380.md) · 呼出先 2件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 88.68% / 新版 88.68%

CFGの説明率　旧版 82.61% / 新版 73.08%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 6件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b01b28"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b01b28"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b01b2c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b01b28",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b01b2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b01b30",
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
      "00b6175c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b61760",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b61764",
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

- 旧版 [`00b01b28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01b28.md#insn-00b01b28) · [`00b01b2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01b28.md#insn-00b01b2c) · [`00b01b30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01b28.md#insn-00b01b30)

~~~diff
- 00b01b28 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b01b28 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b01b28 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b01b28 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b01b28 bytes f657bda9
- 00b01b2c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b01b2c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b01b2c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b01b2c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b01b2c bytes f44f01a9
- 00b01b30 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b01b30 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b01b30 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b01b30 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b01b30 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ceae8f9a4e8048f94153201a09b1c7eb"></a>

### [`00b01bfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01bfc.md) → [`00b61830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b61/00b61830.md) _ZN8firebase11AppCallback16GetEnabledByNameEPKc

採用 · 移動量 `+0x5fc34` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bddd70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd70.md) · 呼出先 9件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00c5a7d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7d0.md) · 呼出先 9件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 87.80% / 新版 87.80%

CFGの説明率　旧版 55.00% / 新版 45.83%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b01c0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b01c0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b01c10"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b01c0c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b01c10",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b01c24",
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
      "00b61840",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b61844",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b61858",
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

- 旧版 [`00b01c0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01bfc.md#insn-00b01c0c) · [`00b01c10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01bfc.md#insn-00b01c10) · [`00b01c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01bfc.md#insn-00b01c24)

~~~diff
- 00b01c0c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b01c0c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b01c0c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b01c0c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b01c0c bytes f44f05a9
- 00b01c10 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b01c10 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b01c10 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b01c10 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b01c10 bytes fd7b06a9
- 00b01c24 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00b01c24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b01c24 bytes e80f00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24e3dcc029aacf57fa72c764ea9b2a90"></a>

### [`00b01d44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01d44.md) → [`00b61978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b61/00b61978.md) _ZN8firebase11AppCallback16SetEnabledByNameEPKcb

採用 · 移動量 `+0x5fc34` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 10件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 84.38% / 新版 84.38%

CFGの説明率　旧版 55.00% / 新版 37.93%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b01d58"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b01d58"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b01d5c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b01d58",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b01d5c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b01d74",
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
      "00b6198c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b61990",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b619a8",
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

- 旧版 [`00b01d58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01d44.md#insn-00b01d58) · [`00b01d5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01d44.md#insn-00b01d5c) · [`00b01d74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01d44.md#insn-00b01d74)

~~~diff
- 00b01d58 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b01d58 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b01d58 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b01d58 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b01d58 bytes f44f06a9
- 00b01d5c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b01d5c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b01d5c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00b01d5c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b01d5c bytes fd7b07a9
- 00b01d74 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00b01d74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b01d74 bytes e80f00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ed93fa36b0aede8538b2c74ba18de58"></a>

### [`00b01ec4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01ec4.md) → [`00b61af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b61/00b61af8.md) _ZN8firebase11AppCallback13SetEnabledAllEb

採用 · 移動量 `+0x5fc34` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bde2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2b0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5ad30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad30.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 89.19% / 新版 89.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b61b30",
      "incomplete_value": true,
      "site": "00b61b30",
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
              "LOAD"
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
      "definition_site": "00b01efc",
      "incomplete_value": true,
      "site": "00b01efc",
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
              "LOAD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b61b1c",
      "incomplete_value": true,
      "site": "00b61b20",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
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
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b01ee8",
      "incomplete_value": true,
      "site": "00b01eec",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
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
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b61b50",
      "incomplete_value": true,
      "site": "00b61b54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4000:8"
          ],
          [
            "leaf",
            "const:5da:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b01f1c",
      "incomplete_value": true,
      "site": "00b01f20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4000:8"
          ],
          [
            "leaf",
            "const:382:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b61b10",
      "READ",
      [
        "storage",
        "00c1b9c0",
        null,
        "pointer"
      ]
    ],
    [
      "00b61b18",
      "READ",
      [
        "storage",
        "010a0d70",
        "_ZN8firebase11AppCallback16callbacks_mutex_E",
        "undefined8"
      ]
    ],
    [
      "00b61b28",
      "READ",
      [
        "storage",
        "00c1b9b8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b61b10",
      "READ",
      [
        "storage",
        "00c9b3c0",
        null,
        "pointer"
      ]
    ],
    [
      "00b61b18",
      "READ",
      [
        "storage",
        "01125c30",
        "_ZN8firebase11AppCallback16callbacks_mutex_E",
        "undefined8"
      ]
    ],
    [
      "00b61b28",
      "READ",
      [
        "storage",
        "00c9b3b8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b01eec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01ec4.md#insn-00b01eec) · [`00b01f20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01ec4.md#insn-00b01f20) · [`00b01ed8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01ec4.md#insn-00b01ed8)
- 新版 [`00b61b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b61/00b61af8.md#insn-00b61b20) · [`00b61b54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b61/00b61af8.md#insn-00b61b54) · [`00b61b0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b61/00b61af8.md#insn-00b61b0c)

~~~diff
- 00b01eec ["INT_ADD", "register:40f0:8", ["const:b01eec:8", "const:4:8"]]
- 00b01eec ["CALL", null, ["callee:00c5a600:8"]]
+ 00b61b20 ["INT_ADD", "register:40f0:8", ["const:b61b20:8", "const:4:8"]]
+ 00b61b20 ["CALL", null, ["callee:00c5a600:8"]]
- 00b01eec bytes 4d6f0394
+ 00b61b20 bytes b8e20394
- 00b01f20 ["INT_ADD", "register:40f0:8", ["const:b01f20:8", "const:4:8"]]
- 00b01f20 ["CALL", null, ["callee:00c5ad30:8"]]
+ 00b61b54 ["INT_ADD", "register:40f0:8", ["const:b61b54:8", "const:4:8"]]
+ 00b61b54 ["CALL", null, ["callee:00c5ad30:8"]]
- 00b01f20 bytes e4700394
+ 00b61b54 bytes 77e40394
- 00b01ed8 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00b61b0c ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00b01ed8 bytes c80800d0
+ 00b61b0c bytes c80900d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9adc07d1fee3b46cf560eb95cef8a577"></a>

### [`00b01fec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01fec.md) → [`00b61c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b61/00b61c20.md) _ZN8firebase11AppCallback11AddCallbackEPS0_

採用 · 移動量 `+0x5fc34` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 1件 [`00bddd60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd60.md) · 呼出先 11件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00c5a7c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7c0.md) · 呼出先 11件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_condition

命令の説明率　旧版 96.82% / 新版 96.82%

CFGの説明率　旧版 90.70% / 新版 92.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_condition` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b61c5c",
      "incomplete_value": true,
      "site": "00b61c5c",
      "value": [
        "INT_NOTEQUAL",
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
              "LOAD"
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
      "definition_site": "00b02028",
      "incomplete_value": true,
      "site": "00b02028",
      "value": [
        "INT_NOTEQUAL",
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
              "LOAD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b61d2c",
      "incomplete_value": false,
      "site": "00b61d30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b4000:8"
          ],
          [
            "leaf",
            "const:5e4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b020f8",
      "incomplete_value": false,
      "site": "00b020fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a3000:8"
          ],
          [
            "leaf",
            "const:dc5:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b61d7c",
      "incomplete_value": false,
      "site": "00b61d80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b4000:8"
          ],
          [
            "leaf",
            "const:62d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b02148",
      "incomplete_value": false,
      "site": "00b0214c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a3000:8"
          ],
          [
            "leaf",
            "const:e0e:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b61c54",
      "READ",
      [
        "storage",
        "00c1b9b8",
        null,
        "pointer"
      ]
    ],
    [
      "00b61c58",
      "READ",
      [
        "storage",
        "010a0d68",
        "_ZN8firebase11AppCallback10callbacks_E",
        "undefined8"
      ]
    ],
    [
      "00b61c7c",
      "WRITE",
      [
        "storage",
        "010a0d68",
        "_ZN8firebase11AppCallback10callbacks_E",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b61c54",
      "READ",
      [
        "storage",
        "00c9b3b8",
        null,
        "pointer"
      ]
    ],
    [
      "00b61c58",
      "READ",
      [
        "storage",
        "01125c28",
        "_ZN8firebase11AppCallback10callbacks_E",
        "undefined8"
      ]
    ],
    [
      "00b61c7c",
      "WRITE",
      [
        "storage",
        "01125c28",
        "_ZN8firebase11AppCallback10callbacks_E",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b020fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01fec.md#insn-00b020fc) · [`00b0214c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01fec.md#insn-00b0214c) · [`00b02014`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01fec.md#insn-00b02014)
- 新版 [`00b61d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b61/00b61c20.md#insn-00b61d30) · [`00b61d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b61/00b61c20.md#insn-00b61d80) · [`00b61c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b61/00b61c20.md#insn-00b61c48)

~~~diff
- 00b020fc ["INT_ADD", "register:40f0:8", ["const:b020fc:8", "const:4:8"]]
- 00b020fc ["CALL", null, ["callee:00c5a9e0:8"]]
+ 00b61d30 ["INT_ADD", "register:40f0:8", ["const:b61d30:8", "const:4:8"]]
+ 00b61d30 ["CALL", null, ["callee:00c5a9e0:8"]]
- 00b020fc bytes 996f0394
+ 00b61d30 bytes 2ce30394
- 00b0214c ["INT_ADD", "register:40f0:8", ["const:b0214c:8", "const:4:8"]]
- 00b0214c ["CALL", null, ["callee:00c5ad30:8"]]
+ 00b61d80 ["INT_ADD", "register:40f0:8", ["const:b61d80:8", "const:4:8"]]
+ 00b61d80 ["CALL", null, ["callee:00c5ad30:8"]]
- 00b0214c bytes 59700394
+ 00b61d80 bytes ece30394
- 00b02014 ["COPY", "register:40c8:8", ["const:c1b000:8"]]
+ 00b61c48 ["COPY", "register:40c8:8", ["const:c9b000:8"]]
- 00b02014 bytes d90800b0
+ 00b61c48 bytes d90900d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b8571c238666561570cfec1b0819df3"></a>

### [`00b02260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02260.md) → [`00b61e94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b61/00b61e94.md) _ZN8firebase16StaticFutureData26CleanupFutureDataForModuleEPKv

採用 · 移動量 `+0x5fc34` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdee90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdee90.md) · 呼出先 5件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdddf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdddf0.md) [`00bde750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde750.md)
- 新版 呼出元 1件 [`00c5b940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b940.md) · 呼出先 5件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a850.md) [`00c5b1d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1d0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 94.20% / 新版 94.20%

CFGの説明率　旧版 72.41% / 新版 77.78%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `unresolved_branch_alignment` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b61ec8",
      "incomplete_value": true,
      "site": "00b61ec8",
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
              "LOAD"
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
      "definition_site": "00b02294",
      "incomplete_value": true,
      "site": "00b02294",
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
              "LOAD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b022d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b61f04"
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
      "00b61ea8",
      "READ",
      [
        "storage",
        "00c1b9d0",
        null,
        "pointer"
      ]
    ],
    [
      "00b61eb0",
      "READ",
      [
        "storage",
        "010a0d78",
        "_ZN8firebase16StaticFutureData16s_futures_mutex_E",
        "undefined8"
      ]
    ],
    [
      "00b61ec0",
      "READ",
      [
        "storage",
        "00c1b9c8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b61ea8",
      "READ",
      [
        "storage",
        "00c9b3d0",
        null,
        "pointer"
      ]
    ],
    [
      "00b61eb0",
      "READ",
      [
        "storage",
        "01125c38",
        "_ZN8firebase16StaticFutureData16s_futures_mutex_E",
        "undefined8"
      ]
    ],
    [
      "00b61ec0",
      "READ",
      [
        "storage",
        "00c9b3c8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b02284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02260.md#insn-00b02284) · [`00b02294`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02260.md#insn-00b02294) · [`00b022d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02260.md#insn-00b022d0)
- 新版 [`00b61eb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b61/00b61e94.md#insn-00b61eb8) · [`00b61ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b61/00b61e94.md#insn-00b61ec8)

~~~diff
- 00b02284 ["INT_ADD", "register:40f0:8", ["const:b02284:8", "const:4:8"]]
- 00b02284 ["CALL", null, ["callee:00c5a600:8"]]
+ 00b61eb8 ["INT_ADD", "register:40f0:8", ["const:b61eb8:8", "const:4:8"]]
+ 00b61eb8 ["CALL", null, ["callee:00c5a600:8"]]
- 00b02284 bytes 676e0394
+ 00b61eb8 bytes d2e10394
- 00b02294 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b02294 ["CBRANCH", null, ["local:b18:8", "tmp:0:1"]]
+ 00b61ec8 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b61ec8 ["CBRANCH", null, ["local:b16:8", "tmp:0:1"]]
- 00b02294 bytes 680600b4
+ 00b61ec8 bytes 680600b4
- 00b022d0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b022d0 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00b022d0 ["CBRANCH", null, ["local:b18:8", "tmp:1:1"]]
- 00b022d0 bytes 88040054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41e28c4a419de71f9cf28b214ca4905c"></a>

### [`00b02374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02374.md) → [`00b61fa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b61/00b61fa8.md) _ZN8firebase16StaticFutureData22GetFutureDataForModuleEPKvi

採用 · 移動量 `+0x5fc34` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdee80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdee80.md) · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddde0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddde0.md) [`00bde760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde760.md)
- 新版 呼出元 1件 [`00c5b930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b930.md) · 呼出先 5件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a840.md) [`00c5b1e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1e0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 96.12% / 新版 96.12%

CFGの説明率　旧版 74.42% / 新版 78.05%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b61fe8",
      "incomplete_value": true,
      "site": "00b61fe8",
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
              "LOAD"
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
      "definition_site": "00b023b4",
      "incomplete_value": true,
      "site": "00b023b4",
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
              "LOAD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b02440"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b62074"
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
      "00b61fc4",
      "READ",
      [
        "storage",
        "00c1b9d0",
        null,
        "pointer"
      ]
    ],
    [
      "00b61fd0",
      "READ",
      [
        "storage",
        "010a0d78",
        "_ZN8firebase16StaticFutureData16s_futures_mutex_E",
        "undefined8"
      ]
    ],
    [
      "00b61fe0",
      "READ",
      [
        "storage",
        "00c1b9c8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b61fc4",
      "READ",
      [
        "storage",
        "00c9b3d0",
        null,
        "pointer"
      ]
    ],
    [
      "00b61fd0",
      "READ",
      [
        "storage",
        "01125c38",
        "_ZN8firebase16StaticFutureData16s_futures_mutex_E",
        "undefined8"
      ]
    ],
    [
      "00b61fe0",
      "READ",
      [
        "storage",
        "00c9b3c8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b023a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02374.md#insn-00b023a4) · [`00b02440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02374.md#insn-00b02440) · [`00b0250c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02374.md#insn-00b0250c)
- 新版 [`00b61fd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b61/00b61fa8.md#insn-00b61fd8)

~~~diff
- 00b023a4 ["INT_ADD", "register:40f0:8", ["const:b023a4:8", "const:4:8"]]
- 00b023a4 ["CALL", null, ["callee:00c5a600:8"]]
+ 00b61fd8 ["INT_ADD", "register:40f0:8", ["const:b61fd8:8", "const:4:8"]]
+ 00b61fd8 ["CALL", null, ["callee:00c5a600:8"]]
- 00b023a4 bytes 1f6e0394
+ 00b61fd8 bytes 8ae10394
- 00b02440 ["INT_EQUAL", "tmp:0:1", ["register:40c8:8", "const:0:8"]]
- 00b02440 ["CBRANCH", null, ["local:b18:8", "tmp:0:1"]]
- 00b02440 bytes 190200b4
- 00b0250c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b0250c ["RETURN", null, ["register:0:8"]]
- 00b0250c bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd8fa28ee677c2d2f44edd3e9d3046bc"></a>

### [`00b02754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02754.md) → [`00b62388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b62/00b62388.md) _ZN8firebase19CreateApiIdentifierEPKcPv

採用 · 移動量 `+0x5fc34` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdeeb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeeb0.md) · 呼出先 2件 [`00b027f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b027f4.md) [`00bdb7a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7a0.md)
- 新版 呼出元 1件 [`00c5b960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b960.md) · 呼出先 2件 [`00b62428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b62/00b62428.md) [`00c581f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c581f0.md)

変更の種類 constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_store_alignment

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b02760"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b02760"
    }
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b623d4",
      "incomplete_value": false,
      "site": "00b623d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1125000:8"
          ],
          [
            "leaf",
            "const:c48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b027a0",
      "incomplete_value": false,
      "site": "00b027a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a0000:8"
          ],
          [
            "leaf",
            "const:d88:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b02760",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b623a4",
      "READ",
      [
        "storage",
        "010a0d88",
        null,
        "undefined4"
      ]
    ],
    [
      "00b623d4",
      "WRITE",
      [
        "storage",
        "010a0d88",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00b62394",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b623a4",
      "READ",
      [
        "storage",
        "01125c48",
        null,
        "undefined4"
      ]
    ],
    [
      "00b623d4",
      "WRITE",
      [
        "storage",
        "01125c48",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b02760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02754.md#insn-00b02760) · [`00b027a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02754.md#insn-00b027a0)
- 新版 [`00b623d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b62/00b62388.md#insn-00b623d4) · [`00b62394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b62/00b62388.md#insn-00b62394)

~~~diff
- 00b02760 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b02760 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b02760 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b02760 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b02760 bytes fd7b03a9
- 00b027a0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d88:8"]]
- 00b027a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
+ 00b623d4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c48:8"]]
+ 00b623d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00b027a0 bytes 09890db9
+ 00b623d4 bytes 09490cb9
+ 00b62394 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00b62394 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00b62394 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
+ 00b62394 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00b62394 bytes fd7b03a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-866175fa1ec092c7d65bc585bebe690e"></a>

### [`00b02898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02898.md) → [`00b624f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b62/00b624f0.md) FUN_00b624f0

採用 · 移動量 `+0x5fc58` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b01714`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01714.md) · 呼出先 12件 [`00b01714`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01714.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md)
- 新版 呼出元 1件 [`00b6132c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b61/00b6132c.md) · 呼出先 12件 [`00b6132c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b61/00b6132c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 93.33% / 新版 82.35%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 2件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b62580",
      "incomplete_value": false,
      "site": "00b62584",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ae000:8"
          ],
          [
            "leaf",
            "const:18b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b02928",
      "incomplete_value": false,
      "site": "00b0292c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29d000:8"
          ],
          [
            "leaf",
            "const:e71:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b6258c",
      "value": [
        "leaf",
        "ram:b6132c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b02934",
      "value": [
        "leaf",
        "ram:b01714:8"
      ]
    },
    "ordinal": 7,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b625b4",
      "incomplete_value": false,
      "site": "00b625b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2af000:8"
          ],
          [
            "leaf",
            "const:34f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0295c",
      "incomplete_value": false,
      "site": "00b02960",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29e000:8"
          ],
          [
            "leaf",
            "const:f2c:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b62580",
      "PARAM",
      [
        "storage",
        "0029de71",
        null,
        "string"
      ]
    ],
    [
      "00b6258c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00b01714"
      ]
    ],
    [
      "00b625b4",
      "PARAM",
      [
        "storage",
        "0029ef2c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b62580",
      "PARAM",
      [
        "storage",
        "002ae18b",
        null,
        "string"
      ]
    ],
    [
      "00b6258c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00b6132c"
      ]
    ],
    [
      "00b625b4",
      "PARAM",
      [
        "storage",
        "002af34f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0292c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02898.md#insn-00b0292c) · [`00b02934`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02898.md#insn-00b02934) · [`00b02960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02898.md#insn-00b02960)
- 新版 [`00b62584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b62/00b624f0.md#insn-00b62584) · [`00b6258c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b62/00b624f0.md#insn-00b6258c) · [`00b625b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b62/00b624f0.md#insn-00b625b8)

~~~diff
- 00b0292c ["INT_ADD", "register:40f0:8", ["const:b0292c:8", "const:4:8"]]
- 00b0292c ["CALL", null, ["callee:00c5abe0:8"]]
+ 00b62584 ["INT_ADD", "register:40f0:8", ["const:b62584:8", "const:4:8"]]
+ 00b62584 ["CALL", null, ["callee:00c5abe0:8"]]
- 00b0292c bytes 0d6e0394
+ 00b62584 bytes 97e10394
- 00b02934 ["INT_ADD", "register:40f0:8", ["const:b02934:8", "const:4:8"]]
- 00b02934 ["CALL", null, ["ram:b01714:8"]]
+ 00b6258c ["INT_ADD", "register:40f0:8", ["const:b6258c:8", "const:4:8"]]
+ 00b6258c ["CALL", null, ["ram:b6132c:8"]]
- 00b02934 bytes 78fbff97
+ 00b6258c bytes 68fbff97
- 00b02960 ["INT_ADD", "register:40f0:8", ["const:b02960:8", "const:4:8"]]
- 00b02960 ["CALL", null, ["callee:00c5a8a0:8"]]
+ 00b625b8 ["INT_ADD", "register:40f0:8", ["const:b625b8:8", "const:4:8"]]
+ 00b625b8 ["CALL", null, ["callee:00c5a8a0:8"]]
- 00b02960 bytes 386d0394
+ 00b625b8 bytes bae00394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a53bff315fc1f539ef72ffcfb972d6b"></a>

### [`00b02d48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02d48.md) → [`00b629a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b62/00b629a0.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN8firebase11AppCallbackEEENS_19__map_value_

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdeee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeee0.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`00c5b990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b990.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 98.61% / 新版 98.61%

CFGの説明率　旧版 93.33% / 新版 90.32%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b02d70"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b629c8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "CONDITIONAL_JUMP",
        "00b02d70"
      ],
      [
        "CONDITIONAL_JUMP",
        "00b629c8"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b629c8",
      "incomplete_value": true,
      "site": "00b62a90",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b02d70",
      "incomplete_value": true,
      "site": "00b02e38",
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
    "ordinal": 13,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b02d70",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b62a90"
      ]
    ]
  ],
  "added": [
    [
      "00b629c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b62a90"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b02d70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02d48.md#insn-00b02d70) · [`00b02d90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02d48.md#insn-00b02d90)
- 新版 [`00b629c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b62/00b629a0.md#insn-00b629c8) · [`00b629e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b62/00b629a0.md#insn-00b629e8)

~~~diff
- 00b02d70 ["INT_EQUAL", "tmp:0:1", ["register:40b8:8", "const:0:8"]]
- 00b02d70 ["CBRANCH", null, ["local:b17:8", "tmp:0:1"]]
- 00b02d70 bytes 570600b4
+ 00b629c8 ["INT_EQUAL", "tmp:0:1", ["register:40b8:8", "const:0:8"]]
+ 00b629c8 ["CBRANCH", null, ["local:b18:8", "tmp:0:1"]]
+ 00b629c8 bytes 570600b4
- 00b02d90 ["BRANCH", null, ["local:b5:8"]]
+ 00b629e8 ["BRANCH", null, ["local:b6:8"]]
- 00b02d90 bytes 07000014
+ 00b629e8 bytes 07000014
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-674c97ddeb8e42279228c91d357dab7d"></a>

### [`00b02ec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02ec0.md) → [`00b62b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b62/00b62b18.md) _ZN8firebase7VariantaSERKS0_

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bddaa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddaa0.md) · 呼出先 11件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9e0.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 1件 [`00c5a4f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4f0.md) · 呼出先 11件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a430.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 69.86% / 新版 69.86%

CFGの説明率　旧版 38.89% / 新版 39.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 18件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 5件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b03030"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b62c88"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b030fc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b02f18",
      "DATA",
      [
        "storage",
        "002f6059",
        "switchD_00b02f20::switchdataD_002f6059",
        "byte"
      ]
    ],
    [
      "unmatched:00b02f34",
      "PARAM",
      [
        "storage",
        "0029dea1",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b02f38",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5a8a0"
      ]
    ]
  ],
  "added": [
    [
      "00b62b70",
      "DATA",
      [
        "storage",
        "0030bbc9",
        "switchD_00b62b78::switchdataD_0030bbc9",
        "byte"
      ]
    ],
    [
      "00b62b8c",
      "PARAM",
      [
        "storage",
        "002ae1bb",
        null,
        "string"
      ]
    ],
    [
      "00b62b90",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5a8a0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b02f38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02ec0.md#insn-00b02f38) · [`00b02f5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02ec0.md#insn-00b02f5c) · [`00b02fb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02ec0.md#insn-00b02fb0)
- 新版 [`00b62bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b62/00b62b18.md#insn-00b62bb4) · [`00b62c08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b62/00b62b18.md#insn-00b62c08)

~~~diff
- 00b02f38 ["INT_ADD", "register:40f0:8", ["const:b02f38:8", "const:4:8"]]
- 00b02f38 ["CALL", null, ["callee:00c5a8a0:8"]]
- 00b02f38 bytes c26b0394
- 00b02f5c ["INT_ADD", "register:40f0:8", ["const:b02f5c:8", "const:4:8"]]
- 00b02f5c ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b62bb4 ["INT_ADD", "register:40f0:8", ["const:b62bb4:8", "const:4:8"]]
+ 00b62bb4 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b02f5c bytes 896c0394
+ 00b62bb4 bytes 13e00394
- 00b02fb0 ["INT_ADD", "register:40f0:8", ["const:b02fb0:8", "const:4:8"]]
- 00b02fb0 ["CALL", null, ["callee:00c5a8a0:8"]]
+ 00b62c08 ["INT_ADD", "register:40f0:8", ["const:b62c08:8", "const:4:8"]]
+ 00b62c08 ["CALL", null, ["callee:00c5a8a0:8"]]
- 00b02fb0 bytes a46b0394
+ 00b62c08 bytes 26df0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3bf6262a42b9075535c675072a4341ca"></a>

### [`00b03204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b03204.md) → [`00b62e5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b62/00b62e5c.md) _ZN8firebase7Variant5ClearENS0_4TypeE

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b03204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b03204.md) [`00bdd9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9e0.md) · 呼出先 6件 [`00b03204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b03204.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bdef70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdef70.md)
- 新版 呼出元 2件 [`00b62e5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b62/00b62e5c.md) [`00c5a430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a430.md) · 呼出先 6件 [`00b62e5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b62/00b62e5c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ba20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba20.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 66.02% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_condition` 4件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b03464"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b630bc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b032b0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b0323c",
      "DATA",
      [
        "storage",
        "002f6064",
        "switchD_00b03244::switchdataD_002f6064",
        "byte"
      ]
    ],
    [
      "unmatched:00b032b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b62f24"
      ]
    ],
    [
      "00b62f20",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b032b4"
      ]
    ]
  ],
  "added": [
    [
      "00b62e94",
      "DATA",
      [
        "storage",
        "0030bbd4",
        "switchD_00b62e9c::switchdataD_0030bbd4",
        "byte"
      ]
    ],
    [
      "00b62f08",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b62f24"
      ]
    ],
    [
      "00b62f20",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b62f0c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b032b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b03204.md#insn-00b032b0) · [`00b03340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b03204.md#insn-00b03340) · [`00b033a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b03204.md#insn-00b033a0)
- 新版 [`00b62f98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b62/00b62e5c.md#insn-00b62f98) · [`00b62ff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b62/00b62e5c.md#insn-00b62ff8)

~~~diff
- 00b032b0 ["CBRANCH", null, ["local:b16:8", "register:101:1"]]
- 00b032b0 bytes e0000054
- 00b03340 ["INT_ADD", "register:40f0:8", ["const:b03340:8", "const:4:8"]]
- 00b03340 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b62f98 ["INT_ADD", "register:40f0:8", ["const:b62f98:8", "const:4:8"]]
+ 00b62f98 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b03340 bytes 906b0394
+ 00b62f98 bytes 1adf0394
- 00b033a0 ["INT_ADD", "register:40f0:8", ["const:b033a0:8", "const:4:8"]]
- 00b033a0 ["CALL", null, ["callee:00c5ba20:8"]]
+ 00b62ff8 ["INT_ADD", "register:40f0:8", ["const:b62ff8:8", "const:4:8"]]
+ 00b62ff8 ["CALL", null, ["callee:00c5ba20:8"]]
- 00b033a0 bytes f46e0394
+ 00b62ff8 bytes 8ae20394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ec9d2d56e1fba6af4840600250f1be5"></a>

### [`00b034c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b034c0.md) → [`00b63118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b63/00b63118.md) _ZNK8firebase7Variant14mutable_stringEv

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdef30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdef30.md) · 呼出先 3件 [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde740.md)
- 新版 呼出元 1件 [`00c5b9e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b9e0.md) · 呼出先 3件 [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5b1c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1c0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 73.91% / 新版 62.96%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b03514"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b63178",
      "incomplete_value": false,
      "site": "00b63180",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bf000:8"
          ],
          [
            "leaf",
            "const:81b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b03520",
      "incomplete_value": false,
      "site": "00b03528",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ae000:8"
          ],
          [
            "leaf",
            "const:3d6:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b631c4",
      "incomplete_value": false,
      "site": "00b631c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2be000:8"
          ],
          [
            "leaf",
            "const:5ff:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0356c",
      "incomplete_value": false,
      "site": "00b03570",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ad000:8"
          ],
          [
            "leaf",
            "const:3a7:8"
          ]
        ]
      ]
    },
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
      "unmatched:00b034dc",
      "READ",
      [
        "storage",
        "00c1b9e0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b03510",
      "PARAM",
      [
        "storage",
        "002ad3a7",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b03514",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5a8a0"
      ]
    ]
  ],
  "added": [
    [
      "00b63134",
      "READ",
      [
        "storage",
        "00c9b3f0",
        null,
        "pointer"
      ]
    ],
    [
      "00b63168",
      "PARAM",
      [
        "storage",
        "002be5ff",
        null,
        "string"
      ]
    ],
    [
      "00b6316c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5a8a0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b03514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b034c0.md#insn-00b03514) · [`00b03528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b034c0.md#insn-00b03528) · [`00b03570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b034c0.md#insn-00b03570)
- 新版 [`00b63180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b63/00b63118.md#insn-00b63180) · [`00b631c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b63/00b63118.md#insn-00b631c8)

~~~diff
- 00b03514 ["INT_ADD", "register:40f0:8", ["const:b03514:8", "const:4:8"]]
- 00b03514 ["CALL", null, ["callee:00c5a8a0:8"]]
- 00b03514 bytes 4b6a0394
- 00b03528 ["INT_ADD", "register:40f0:8", ["const:b03528:8", "const:4:8"]]
- 00b03528 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b63180 ["INT_ADD", "register:40f0:8", ["const:b63180:8", "const:4:8"]]
+ 00b63180 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b03528 bytes 166b0394
+ 00b63180 bytes a0de0394
- 00b03570 ["INT_ADD", "register:40f0:8", ["const:b03570:8", "const:4:8"]]
- 00b03570 ["CALL", null, ["callee:00c5a8a0:8"]]
+ 00b631c8 ["INT_ADD", "register:40f0:8", ["const:b631c8:8", "const:4:8"]]
+ 00b631c8 ["CALL", null, ["callee:00c5a8a0:8"]]
- 00b03570 bytes 346a0394
+ 00b631c8 bytes b6dd0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb312999421031c93b893bc0a7ff4857"></a>

### [`00b035c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b035c0.md) → [`00b63218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b63/00b63218.md) _ZN8firebase7Variant16set_mutable_blobEPKvm

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdef20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdef20.md) · 呼出先 5件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9e0.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bdefa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefa0.md)
- 新版 呼出元 1件 [`00c5b9d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b9d0.md) · 呼出先 5件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5a430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a430.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ba50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba50.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 72.97% / 新版 72.97%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b03614"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b6326c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6322c",
      "incomplete_value": true,
      "site": "00b63238",
      "value": [
        "live",
        "register:4010:8"
      ]
    },
    "old": null,
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
      "unmatched:00b03614",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b63298"
      ]
    ],
    [
      "unmatched:00b0361c",
      "PARAM",
      [
        "storage",
        "002ab03f",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b03620",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5a8a0"
      ]
    ]
  ],
  "added": [
    [
      "00b6326c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b63298"
      ]
    ],
    [
      "00b63274",
      "PARAM",
      [
        "storage",
        "002bbe08",
        null,
        "string"
      ]
    ],
    [
      "00b63278",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5a8a0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b035e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b035c0.md#insn-00b035e0) · [`00b03604`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b035c0.md#insn-00b03604) · [`00b03614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b035c0.md#insn-00b03614)
- 新版 [`00b63238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b63/00b63218.md#insn-00b63238) · [`00b6325c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b63/00b63218.md#insn-00b6325c)

~~~diff
- 00b035e0 ["INT_ADD", "register:40f0:8", ["const:b035e0:8", "const:4:8"]]
- 00b035e0 ["CALL", null, ["callee:00c5ba50:8"]]
+ 00b63238 ["INT_ADD", "register:40f0:8", ["const:b63238:8", "const:4:8"]]
+ 00b63238 ["CALL", null, ["callee:00c5ba50:8"]]
- 00b035e0 bytes 706e0394
+ 00b63238 bytes 06e20394
- 00b03604 ["INT_ADD", "register:40f0:8", ["const:b03604:8", "const:4:8"]]
- 00b03604 ["CALL", null, ["callee:00c5a430:8"]]
+ 00b6325c ["INT_ADD", "register:40f0:8", ["const:b6325c:8", "const:4:8"]]
+ 00b6325c ["CALL", null, ["callee:00c5a430:8"]]
- 00b03604 bytes f7680394
+ 00b6325c bytes 75dc0394
- 00b03614 ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
- 00b03614 bytes 60010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67c0d12f3815266892c928c7858159e9"></a>

### [`00b03654`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b03654.md) → [`00b632ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b63/00b632ac.md) _ZN8firebase7VariantaSEOS0_

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdd9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9f0.md) · 呼出先 3件 [`00bdd9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9e0.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 1件 [`00c5a440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a440.md) · 呼出先 3件 [`00c5a430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a430.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 14.81% / 新版 18.18%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b03740"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b03744"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b03744"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b036a8",
      "DATA",
      [
        "storage",
        "002f607a",
        "switchD_00b036b0::switchdataD_002f607a",
        "byte"
      ]
    ],
    [
      "00b63308",
      "COMPUTED_JUMP",
      [
        "local_branch",
        "unmatched:00b0374c"
      ]
    ],
    [
      "unmatched:00b036f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6337c"
      ]
    ]
  ],
  "added": [
    [
      "00b63300",
      "DATA",
      [
        "storage",
        "0030bbea",
        "switchD_00b63308::switchdataD_0030bbea",
        "byte"
      ]
    ],
    [
      "00b63308",
      "COMPUTED_JUMP",
      [
        "local_branch",
        "00b633a4"
      ]
    ],
    [
      "00b63350",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6337c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b036f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b03654.md#insn-00b036f8) · [`00b03704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b03654.md#insn-00b03704) · [`00b03720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b03654.md#insn-00b03720)
- 新版 [`00b63378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b63/00b632ac.md#insn-00b63378)

~~~diff
- 00b036f8 ["CBRANCH", null, ["local:b12:8", "register:101:1"]]
- 00b036f8 bytes 60010054
- 00b03704 ["INT_ADD", "register:40f0:8", ["const:b03704:8", "const:4:8"]]
- 00b03704 ["CALL", null, ["callee:00c5a8a0:8"]]
- 00b03704 bytes cf690394
- 00b03720 ["INT_ADD", "register:40f0:8", ["const:b03720:8", "const:4:8"]]
- 00b03720 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b63378 ["INT_ADD", "register:40f0:8", ["const:b63378:8", "const:4:8"]]
+ 00b63378 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b03720 bytes 986a0394
+ 00b63378 bytes 22de0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9c9ffcfa0efec4363bad74e3e4a26c1"></a>

### [`00b0376c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b0376c.md) → [`00b633c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b63/00b633c4.md) _ZNK8firebase7VarianteqERKS0_

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b0376c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b0376c.md) [`00bdef40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdef40.md) · 呼出先 5件 [`00b0376c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b0376c.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9d0.md)
- 新版 呼出元 2件 [`00b633c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b63/00b633c4.md) [`00c5b9f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b9f0.md) · 呼出先 5件 [`00b633c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b63/00b633c4.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5b450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b450.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 70.37% / 新版 70.37%

CFGの説明率　旧版 49.38% / 新版 54.79%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 24件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 9件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0376c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b03770"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b03770"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b0376c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b03770",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b03774",
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
      "00b633c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b633c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b633cc",
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

- 旧版 [`00b0376c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b0376c.md#insn-00b0376c) · [`00b03770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b0376c.md#insn-00b03770) · [`00b03774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b0376c.md#insn-00b03774)

~~~diff
- 00b0376c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00b0376c ["STORE", null, ["const:1b1:8", "register:8:8", "register:5100:8"]]
- 00b0376c bytes e80f1cfc
- 00b03770 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b03770 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b03770 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b03770 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b03770 bytes f65701a9
- 00b03774 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b03774 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b03774 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b03774 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b03774 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-014e1283fd43a94ee064112291b90d90"></a>

### [`00b03ce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b03ce8.md) → [`00b63940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b63/00b63940.md) _ZNK8firebase7VariantltERKS0_

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde720.md) · 呼出先 5件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9d0.md) [`00bdef40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdef40.md)
- 新版 呼出元 1件 [`00c5b1a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1a0.md) · 呼出先 5件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5b450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b450.md) [`00c5b9f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b9f0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 64.01% / 新版 64.01%

CFGの説明率　旧版 34.82% / 新版 41.49%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 30件, `unresolved_branch_alignment` 11件, `unresolved_call_alignment` 25件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b03cfc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b03cfc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b03d00"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b03cfc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b03d00",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b63964",
      "READ",
      [
        "storage",
        "00c1b9e0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b63954",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b63958",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b63964",
      "READ",
      [
        "storage",
        "00c9b3f0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b03cfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b03ce8.md#insn-00b03cfc) · [`00b03d00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b03ce8.md#insn-00b03d00) · [`00b03d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b03ce8.md#insn-00b03d4c)

~~~diff
- 00b03cfc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b03cfc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b03cfc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b03cfc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b03cfc bytes f44f05a9
- 00b03d00 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b03d00 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b03d00 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b03d00 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b03d00 bytes fd7b06a9
- 00b03d4c ["COPY", "tmp:0:4", ["register:40c0:4"]]
- 00b03d4c ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b03d4c ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00b03d4c ["INT_ZEXT", "register:4050:8", ["tmp:0:4"]]
- 00b03d4c bytes 0a03881a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4988b75d1622b427c98d0f98e4ff71c"></a>

### [`00b04554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b04554.md) → [`00b641ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b64/00b641ac.md) _ZNK8firebase7Variant14assert_is_typeENS0_4TypeE

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bddcb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddcb0.md) · 呼出先 2件 [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 1件 [`00c5a700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a700.md) · 呼出先 2件 [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b641d8",
      "incomplete_value": false,
      "site": "00b641e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ae000:8"
          ],
          [
            "leaf",
            "const:1bb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b04580",
      "incomplete_value": false,
      "site": "00b04588",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29d000:8"
          ],
          [
            "leaf",
            "const:ea1:8"
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
      "00b641d8",
      "PARAM",
      [
        "storage",
        "0029dea1",
        null,
        "string"
      ]
    ],
    [
      "00b641ec",
      "READ",
      [
        "storage",
        "00c1b9e0",
        null,
        "pointer"
      ]
    ],
    [
      "00b641f8",
      "PARAM",
      [
        "storage",
        "0029ef54",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b641d8",
      "PARAM",
      [
        "storage",
        "002ae1bb",
        null,
        "string"
      ]
    ],
    [
      "00b641ec",
      "READ",
      [
        "storage",
        "00c9b3f0",
        null,
        "pointer"
      ]
    ],
    [
      "00b641f8",
      "PARAM",
      [
        "storage",
        "002af377",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b04588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b04554.md#insn-00b04588) · [`00b0457c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b04554.md#insn-00b0457c) · [`00b04580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b04554.md#insn-00b04580)
- 新版 [`00b641e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b64/00b641ac.md#insn-00b641e0) · [`00b641d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b64/00b641ac.md#insn-00b641d4) · [`00b641d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b64/00b641ac.md#insn-00b641d8)

~~~diff
- 00b04588 ["INT_ADD", "register:40f0:8", ["const:b04588:8", "const:4:8"]]
- 00b04588 ["CALL", null, ["callee:00c5a8a0:8"]]
+ 00b641e0 ["INT_ADD", "register:40f0:8", ["const:b641e0:8", "const:4:8"]]
+ 00b641e0 ["CALL", null, ["callee:00c5a8a0:8"]]
- 00b04588 bytes 2e660394
+ 00b641e0 bytes b0d90394
- 00b0457c ["COPY", "register:4000:8", ["const:29d000:8"]]
+ 00b641d4 ["COPY", "register:4000:8", ["const:2ae000:8"]]
- 00b0457c bytes c0bcffb0
+ 00b641d4 bytes 40baffd0
- 00b04580 ["COPY", "tmp:0:8", ["const:ea1:8"]]
- 00b04580 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b04580 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b04580 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b641d8 ["COPY", "tmp:0:8", ["const:1bb:8"]]
+ 00b641d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b641d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b641d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b04580 bytes 00843a91
+ 00b641d8 bytes 00ec0691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a4045b37d146e4aa7c04226f036a07b"></a>

### [`00b045b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b045b4.md) → [`00b6420c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b64/00b6420c.md) _ZNK8firebase7Variant18assert_is_not_typeENS0_4TypeE

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b64234",
      "incomplete_value": false,
      "site": "00b6423c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ae000:8"
          ],
          [
            "leaf",
            "const:1bb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b045dc",
      "incomplete_value": false,
      "site": "00b045e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29d000:8"
          ],
          [
            "leaf",
            "const:ea1:8"
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
      "00b64234",
      "PARAM",
      [
        "storage",
        "0029dea1",
        null,
        "string"
      ]
    ],
    [
      "00b64244",
      "READ",
      [
        "storage",
        "00c1b9e0",
        null,
        "pointer"
      ]
    ],
    [
      "00b64250",
      "PARAM",
      [
        "storage",
        "0029968e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b64234",
      "PARAM",
      [
        "storage",
        "002ae1bb",
        null,
        "string"
      ]
    ],
    [
      "00b64244",
      "READ",
      [
        "storage",
        "00c9b3f0",
        null,
        "pointer"
      ]
    ],
    [
      "00b64250",
      "PARAM",
      [
        "storage",
        "002a94ed",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b045e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b045b4.md#insn-00b045e4) · [`00b045d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b045b4.md#insn-00b045d8) · [`00b045dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b045b4.md#insn-00b045dc)
- 新版 [`00b6423c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b64/00b6420c.md#insn-00b6423c) · [`00b64230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b64/00b6420c.md#insn-00b64230) · [`00b64234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b64/00b6420c.md#insn-00b64234)

~~~diff
- 00b045e4 ["INT_ADD", "register:40f0:8", ["const:b045e4:8", "const:4:8"]]
- 00b045e4 ["CALL", null, ["callee:00c5a8a0:8"]]
+ 00b6423c ["INT_ADD", "register:40f0:8", ["const:b6423c:8", "const:4:8"]]
+ 00b6423c ["CALL", null, ["callee:00c5a8a0:8"]]
- 00b045e4 bytes 17660394
+ 00b6423c bytes 99d90394
- 00b045d8 ["COPY", "register:4000:8", ["const:29d000:8"]]
+ 00b64230 ["COPY", "register:4000:8", ["const:2ae000:8"]]
- 00b045d8 bytes c0bcffb0
+ 00b64230 bytes 40baffd0
- 00b045dc ["COPY", "tmp:0:8", ["const:ea1:8"]]
- 00b045dc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b045dc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b045dc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b64234 ["COPY", "tmp:0:8", ["const:1bb:8"]]
+ 00b64234 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b64234 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b64234 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b045dc bytes 00843a91
+ 00b64234 bytes 00ec0691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8071e543755dd5c608e1605e6e791597"></a>

### [`00b04608`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b04608.md) → [`00b64260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b64/00b64260.md) _ZNK8firebase7Variant16assert_is_stringEv

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bddcd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddcd0.md) · 呼出先 2件 [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 1件 [`00c5a720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a720.md) · 呼出先 2件 [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 81.48% / 新版 81.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b642a0",
      "incomplete_value": false,
      "site": "00b642a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2be000:8"
          ],
          [
            "leaf",
            "const:5ff:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b04648",
      "incomplete_value": false,
      "site": "00b0464c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ad000:8"
          ],
          [
            "leaf",
            "const:3a7:8"
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
      "00b642a0",
      "PARAM",
      [
        "storage",
        "002ad3a7",
        null,
        "string"
      ]
    ],
    [
      "00b642b0",
      "READ",
      [
        "storage",
        "00c1b9e0",
        null,
        "pointer"
      ]
    ],
    [
      "00b642bc",
      "PARAM",
      [
        "storage",
        "002ae3d6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b642a0",
      "PARAM",
      [
        "storage",
        "002be5ff",
        null,
        "string"
      ]
    ],
    [
      "00b642b0",
      "READ",
      [
        "storage",
        "00c9b3f0",
        null,
        "pointer"
      ]
    ],
    [
      "00b642bc",
      "PARAM",
      [
        "storage",
        "002bf81b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0464c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b04608.md#insn-00b0464c) · [`00b04644`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b04608.md#insn-00b04644) · [`00b04648`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b04608.md#insn-00b04648)
- 新版 [`00b642a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b64/00b64260.md#insn-00b642a4) · [`00b6429c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b64/00b64260.md#insn-00b6429c) · [`00b642a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b64/00b64260.md#insn-00b642a0)

~~~diff
- 00b0464c ["INT_ADD", "register:40f0:8", ["const:b0464c:8", "const:4:8"]]
- 00b0464c ["CALL", null, ["callee:00c5a8a0:8"]]
+ 00b642a4 ["INT_ADD", "register:40f0:8", ["const:b642a4:8", "const:4:8"]]
+ 00b642a4 ["CALL", null, ["callee:00c5a8a0:8"]]
- 00b0464c bytes fd650394
+ 00b642a4 bytes 7fd90394
- 00b04644 ["COPY", "register:4000:8", ["const:2ad000:8"]]
+ 00b6429c ["COPY", "register:4000:8", ["const:2be000:8"]]
- 00b04644 bytes 40bdffb0
+ 00b6429c bytes c0baffd0
- 00b04648 ["COPY", "tmp:0:8", ["const:3a7:8"]]
- 00b04648 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b04648 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b04648 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b642a0 ["COPY", "tmp:0:8", ["const:5ff:8"]]
+ 00b642a0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b642a0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b642a0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b04648 bytes 009c0e91
+ 00b642a0 bytes 00fc1791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d742ca419e570d6bb9c5360cf1b20990"></a>

### [`00b04674`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b04674.md) → [`00b642cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b64/00b642cc.md) _ZNK8firebase7Variant14assert_is_blobEv

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bde710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde710.md) · 呼出先 2件 [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 1件 [`00c5b190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b190.md) · 呼出先 2件 [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 78.26% / 新版 78.26%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b642fc",
      "incomplete_value": false,
      "site": "00b64300",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bb000:8"
          ],
          [
            "leaf",
            "const:e08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b046a4",
      "incomplete_value": false,
      "site": "00b046a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ab000:8"
          ],
          [
            "leaf",
            "const:3f:8"
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
      "00b642fc",
      "PARAM",
      [
        "storage",
        "002ab03f",
        null,
        "string"
      ]
    ],
    [
      "00b6430c",
      "READ",
      [
        "storage",
        "00c1b9e0",
        null,
        "pointer"
      ]
    ],
    [
      "00b64318",
      "PARAM",
      [
        "storage",
        "00297538",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b642fc",
      "PARAM",
      [
        "storage",
        "002bbe08",
        null,
        "string"
      ]
    ],
    [
      "00b6430c",
      "READ",
      [
        "storage",
        "00c9b3f0",
        null,
        "pointer"
      ]
    ],
    [
      "00b64318",
      "PARAM",
      [
        "storage",
        "002a70d9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b046a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b04674.md#insn-00b046a8) · [`00b046a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b04674.md#insn-00b046a0) · [`00b046a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b04674.md#insn-00b046a4)
- 新版 [`00b64300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b64/00b642cc.md#insn-00b64300) · [`00b642f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b64/00b642cc.md#insn-00b642f8) · [`00b642fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b64/00b642cc.md#insn-00b642fc)

~~~diff
- 00b046a8 ["INT_ADD", "register:40f0:8", ["const:b046a8:8", "const:4:8"]]
- 00b046a8 ["CALL", null, ["callee:00c5a8a0:8"]]
+ 00b64300 ["INT_ADD", "register:40f0:8", ["const:b64300:8", "const:4:8"]]
+ 00b64300 ["CALL", null, ["callee:00c5a8a0:8"]]
- 00b046a8 bytes e6650394
+ 00b64300 bytes 68d90394
- 00b046a0 ["COPY", "register:4000:8", ["const:2ab000:8"]]
+ 00b642f8 ["COPY", "register:4000:8", ["const:2bb000:8"]]
- 00b046a0 bytes 20bdfff0
+ 00b642f8 bytes a0bafff0
- 00b046a4 ["COPY", "tmp:0:8", ["const:3f:8"]]
- 00b046a4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b046a4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b046a4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b642fc ["COPY", "tmp:0:8", ["const:e08:8"]]
+ 00b642fc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b642fc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b642fc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b046a4 bytes 00fc0091
+ 00b642fc bytes 00203891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c989ad6633d9962edb295e895776f88"></a>

### [`00b046d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b046d0.md) → [`00b64328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b64/00b64328.md) _ZNK8firebase7Variant8AsStringEv

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bddcc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddcc0.md) · 呼出先 10件 [`00b04874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b04874.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md)
- 新版 呼出元 1件 [`00c5a710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a710.md) · 呼出先 10件 [`00b644cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b64/00b644cc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b643b8",
      "incomplete_value": false,
      "site": "00b643c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ad000:8"
          ],
          [
            "leaf",
            "const:d7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b04760",
      "incomplete_value": false,
      "site": "00b04768",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29c000:8"
          ],
          [
            "leaf",
            "const:e77:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b643ec",
      "incomplete_value": false,
      "site": "00b643f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a9000:8"
          ],
          [
            "leaf",
            "const:51f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b04794",
      "incomplete_value": false,
      "site": "00b0479c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:299000:8"
          ],
          [
            "leaf",
            "const:6c0:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b6436c",
      "DATA",
      [
        "storage",
        "002f60a8",
        "switchD_00b04720::switchdataD_002f60a8",
        "byte"
      ]
    ],
    [
      "00b643b8",
      "PARAM",
      [
        "storage",
        "0029ce77",
        null,
        null
      ]
    ],
    [
      "00b643ec",
      "PARAM",
      [
        "storage",
        "002996c0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6436c",
      "DATA",
      [
        "storage",
        "0030bc18",
        "switchD_00b64378::switchdataD_0030bc18",
        "byte"
      ]
    ],
    [
      "00b643b8",
      "PARAM",
      [
        "storage",
        "002ad0d7",
        null,
        null
      ]
    ],
    [
      "00b643ec",
      "PARAM",
      [
        "storage",
        "002a951f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b04768`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b046d0.md#insn-00b04768) · [`00b0479c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b046d0.md#insn-00b0479c) · [`00b04708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b046d0.md#insn-00b04708)
- 新版 [`00b643c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b64/00b64328.md#insn-00b643c0) · [`00b643f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b64/00b64328.md#insn-00b643f4) · [`00b64360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b64/00b64328.md#insn-00b64360)

~~~diff
- 00b04768 ["INT_ADD", "register:40f0:8", ["const:b04768:8", "const:4:8"]]
- 00b04768 ["CALL", null, ["callee:00b644cc:8"]]
+ 00b643c0 ["INT_ADD", "register:40f0:8", ["const:b643c0:8", "const:4:8"]]
+ 00b643c0 ["CALL", null, ["callee:00b644cc:8"]]
- 00b04768 bytes 43000094
+ 00b643c0 bytes 43000094
- 00b0479c ["INT_ADD", "register:40f0:8", ["const:b0479c:8", "const:4:8"]]
- 00b0479c ["CALL", null, ["callee:00b644cc:8"]]
+ 00b643f4 ["INT_ADD", "register:40f0:8", ["const:b643f4:8", "const:4:8"]]
+ 00b643f4 ["CALL", null, ["callee:00b644cc:8"]]
- 00b0479c bytes 36000094
+ 00b643f4 bytes 36000094
- 00b04708 ["COPY", "register:4040:8", ["const:2f6000:8"]]
+ 00b64360 ["COPY", "register:4040:8", ["const:30b000:8"]]
- 00b04708 bytes 88bfffd0
+ 00b64360 bytes 28bdfff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-902fbf7ed773d26b167f29dd5ce91282"></a>

### [`00b04874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b04874.md) → [`00b644cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b64/00b644cc.md) FUN_00b644cc

採用 · 移動量 `+0x5fc58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b046d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b046d0.md) · 呼出先 2件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bde2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2d0.md)
- 新版 呼出元 1件 [`00b64328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b64/00b64328.md) · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5ad50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 71.05% / 新版 71.05%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b048c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b048c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b048cc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b048c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b048cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b048d0",
      "READ",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b64520",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00b64524",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00b64528",
      "READ",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b048c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b04874.md#insn-00b048c8) · [`00b048cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b04874.md#insn-00b048cc) · [`00b048e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b04874.md#insn-00b048e0)

~~~diff
- 00b048c8 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b048c8 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00b048c8 ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffffc8:8"]]
- 00b048c8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b048c8 bytes abab3ca9
- 00b048cc ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b048cc ["COPY", "tmp:1:8", ["register:4060:8"]]
- 00b048cc ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffffd8:8"]]
- 00b048cc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b048cc bytes a9b33da9
- 00b048e0 ["INT_ADD", "tmp:0:8", ["register:40e8:8", "const:ffffffffffffffa0:8"]]
- 00b048e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5020:16"]]
- 00b048e0 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00b048e0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5000:16"]]
- 00b048e0 bytes a1033dad
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f47405cf251c3ed01ca303a39b147fa"></a>

### [`00b04a00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b04a00.md) → [`00b64658`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b64/00b64658.md) _ZNK8firebase7Variant8AsDoubleEv

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb770.md) [`00bdd9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9e0.md) [`00bddaa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddaa0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c581c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c581c0.md) [`00c5a430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a430.md) [`00c5a4f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4f0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 87.10% / 新版 87.10%

CFGの説明率　旧版 80.00% / 新版 74.07%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b04a00"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b04a04"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b04a04"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b04a00",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b04a04",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b04a08",
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
      "00b64658",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b6465c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b64660",
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

- 旧版 [`00b04a00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b04a00.md#insn-00b04a00) · [`00b04a04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b04a00.md#insn-00b04a04) · [`00b04a08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b04a00.md#insn-00b04a08)

~~~diff
- 00b04a00 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b04a00 ["STORE", null, ["const:1b1:8", "register:8:8", "register:5100:8"]]
- 00b04a00 bytes e80f1dfc
- 00b04a04 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b04a04 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b04a04 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b04a04 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b04a04 bytes f44f01a9
- 00b04a08 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b04a08 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b04a08 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b04a08 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b04a08 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dfbbef300ec5e510ad8e6888bd024087"></a>

### [`00b04af8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b04af8.md) → [`00b64750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b64/00b64750.md) _ZNK8firebase7Variant6AsBoolEv

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9e0.md) [`00bdef40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdef40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a430.md) [`00c5b9f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b9f0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 44.74% / 新版 42.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b04c2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b04cb8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b64884"
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
      "unmatched:00b04c2c",
      "DATA",
      [
        "storage",
        "002967d9",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b04c2c",
      "WRITE",
      [
        "storage",
        "Stack[-0xa8]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b04c30",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b9f0"
      ]
    ]
  ],
  "added": [
    [
      "00b64884",
      "DATA",
      [
        "storage",
        "002a630e",
        null,
        "undefined1"
      ]
    ],
    [
      "00b64884",
      "WRITE",
      [
        "storage",
        "Stack[-0xa8]",
        null,
        null
      ]
    ],
    [
      "00b64888",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b9f0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b04c2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b04af8.md#insn-00b04c2c) · [`00b04c30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b04af8.md#insn-00b04c30) · [`00b04c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b04af8.md#insn-00b04c88)
- 新版 [`00b648e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b64/00b64750.md#insn-00b648e0)

~~~diff
- 00b04c2c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:58:8"]]
- 00b04c2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b04c2c bytes e82f00f9
- 00b04c30 ["INT_ADD", "register:40f0:8", ["const:b04c30:8", "const:4:8"]]
- 00b04c30 ["CALL", null, ["callee:00c5b9f0:8"]]
- 00b04c30 bytes c4680394
- 00b04c88 ["INT_ADD", "register:40f0:8", ["const:b04c88:8", "const:4:8"]]
- 00b04c88 ["CALL", null, ["callee:00c5b9f0:8"]]
+ 00b648e0 ["INT_ADD", "register:40f0:8", ["const:b648e0:8", "const:4:8"]]
+ 00b648e0 ["CALL", null, ["callee:00c5b9f0:8"]]
- 00b04c88 bytes ae680394
+ 00b648e0 bytes 44dc0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf55b0f19af4202cd7c8482e803a5666"></a>

### [`00b04d5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b04d5c.md) → [`00b649b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b64/00b649b4.md) _ZN8firebase7Variant8TypeNameENS0_4TypeE

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde170.md) · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 1件 [`00c5abf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5abf0.md) · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_return_alignment

命令の説明率　旧版 68.00% / 新版 68.00%

CFGの説明率　旧版 66.67% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b649e0",
      "incomplete_value": true,
      "site": "00b649e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4048:8"
          ],
          [
            "leaf",
            "const:c4c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b04d88",
      "incomplete_value": true,
      "site": "00b04d88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4048:8"
          ],
          [
            "leaf",
            "const:d8c:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b649f8",
      "incomplete_value": false,
      "site": "00b649fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a9000:8"
          ],
          [
            "leaf",
            "const:525:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b04da0",
      "incomplete_value": false,
      "site": "00b04da4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:299000:8"
          ],
          [
            "leaf",
            "const:6c6:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b04dbc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b649c4",
      "READ",
      [
        "storage",
        "010a0d8c",
        null,
        "undefined1"
      ]
    ],
    [
      "00b649e0",
      "WRITE",
      [
        "storage",
        "010a0d8c",
        null,
        "undefined1"
      ]
    ],
    [
      "00b649f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b04da8"
      ]
    ]
  ],
  "added": [
    [
      "00b649c4",
      "READ",
      [
        "storage",
        "01125c4c",
        null,
        "undefined1"
      ]
    ],
    [
      "00b649e0",
      "WRITE",
      [
        "storage",
        "01125c4c",
        null,
        "undefined1"
      ]
    ],
    [
      "00b649f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b64a00"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b04d88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b04d5c.md#insn-00b04d88) · [`00b04da4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b04d5c.md#insn-00b04da4) · [`00b04dbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b04d5c.md#insn-00b04dbc)
- 新版 [`00b649e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b64/00b649b4.md#insn-00b649e0) · [`00b649fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b64/00b649b4.md#insn-00b649fc)

~~~diff
- 00b04d88 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00b04d88 ["INT_ADD", "tmp:1:8", ["register:4048:8", "const:d8c:8"]]
- 00b04d88 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b649e0 ["COPY", "tmp:0:4", ["register:4040:4"]]
+ 00b649e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "const:c4c:8"]]
+ 00b649e0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b04d88 bytes 28313639
+ 00b649e0 bytes 28313139
- 00b04da4 ["INT_ADD", "register:40f0:8", ["const:b04da4:8", "const:4:8"]]
- 00b04da4 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b649fc ["INT_ADD", "register:40f0:8", ["const:b649fc:8", "const:4:8"]]
+ 00b649fc ["CALL", null, ["callee:00c5ac00:8"]]
- 00b04da4 bytes f7640394
+ 00b649fc bytes 81d80394
- 00b04dbc ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b04dbc ["RETURN", null, ["register:0:8"]]
- 00b04dbc bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f23c419116f53f03a363e74c2de8ee2"></a>

### [`00b04dc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b04dc0.md) → [`00b64a18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b64/00b64a18.md) _ZNSt6__ndk16vectorIN8firebase7VariantENS_9allocatorIS2_EEE6assignIPS2_EENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_constru

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00bdef80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdef80.md) · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdd9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9e0.md) [`00bddaa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddaa0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 1件 [`00c5ba30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba30.md) · 呼出先 5件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a430.md) [`00c5a4f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4f0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 92.31% / 新版 90.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b04e10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b04dc0.md#insn-00b04e10) · [`00b04e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b04dc0.md#insn-00b04e14) · [`00b04e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b04dc0.md#insn-00b04e20)
- 新版 [`00b64a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b64/00b64a18.md#insn-00b64a68) · [`00b64a6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b64/00b64a18.md#insn-00b64a6c) · [`00b64a78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b64/00b64a18.md#insn-00b64a78)

~~~diff
- 00b04e10 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b04e10 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00b04e10 ["CBRANCH", null, ["local:b5:8", "tmp:1:1"]]
+ 00b64a68 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00b64a68 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
+ 00b64a68 ["CBRANCH", null, ["local:b6:8", "tmp:1:1"]]
- 00b04e10 bytes a9010054
+ 00b64a68 bytes a9010054
- 00b04e14 ["INT_EQUAL", "tmp:0:1", ["register:40b0:8", "const:0:8"]]
- 00b04e14 ["CBRANCH", null, ["local:b17:8", "tmp:0:1"]]
+ 00b64a6c ["INT_EQUAL", "tmp:0:1", ["register:40b0:8", "const:0:8"]]
+ 00b64a6c ["CBRANCH", null, ["local:b18:8", "tmp:0:1"]]
- 00b04e14 bytes 960700b4
+ 00b64a6c bytes 960700b4
- 00b04e20 ["CBRANCH", null, ["local:b15:8", "register:101:1"]]
+ 00b64a78 ["CBRANCH", null, ["local:b16:8", "register:101:1"]]
- 00b04e20 bytes 60060054
+ 00b64a78 bytes 60060054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f47d1b6181f197897680005b3e1c58da"></a>

### [`00b04fa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b04fa8.md) → [`00b64c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b64/00b64c00.md) _ZNSt6__ndk16__treeINS_12__value_typeIN8firebase7VariantES3_EENS_19__map_value_compareIS3_S4_NS_4lessIS3_EELb1EEENS_9allocatorIS4_EEE14__ass

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdef50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdef50.md) · 呼出先 5件 [`00bddaa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddaa0.md) [`00bde720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde720.md) [`00bde760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde760.md) [`00bdef60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdef60.md) [`00bdef70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdef70.md)
- 新版 呼出元 1件 [`00c5ba00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba00.md) · 呼出先 5件 [`00c5a4f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4f0.md) [`00c5b1a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1a0.md) [`00c5b1e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1e0.md) [`00c5ba10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba10.md) [`00c5ba20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba20.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 91.53% / 新版 91.53%

CFGの説明率　旧版 55.66% / 新版 52.21%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 1件, `unresolved_branch_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b05058"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b050ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b050ec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b64cb8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b64c78"
      ]
    ],
    [
      "unmatched:00b05058",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b64ca8"
      ]
    ],
    [
      "00b64c88",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b64ca8"
      ]
    ]
  ],
  "added": [
    [
      "00b64c88",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b64c78"
      ]
    ],
    [
      "00b64cb0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b64ca8"
      ]
    ],
    [
      "00b64cb8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b64ca8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b04fa8.md#insn-00b05058) · [`00b050ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b04fa8.md#insn-00b050ac) · [`00b050ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b04fa8.md#insn-00b050ec)

~~~diff
- 00b05058 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b05058 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 00b05058 bytes c8ffffb5
- 00b050ac ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b050ac ["CBRANCH", null, ["local:b24:8", "tmp:0:1"]]
- 00b050ac bytes 480100b4
- 00b050ec ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00b050ec ["CBRANCH", null, ["local:b27:8", "tmp:0:1"]]
- 00b050ec bytes 690000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e26b7d3eeed4fe026ec475ebcd3f937e"></a>

### [`00b0529c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b0529c.md) → [`00b64ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b64/00b64ef4.md) _ZNSt6__ndk16__treeINS_12__value_typeIN8firebase7VariantES3_EENS_19__map_value_compareIS3_S4_NS_4lessIS3_EELb1EEENS_9allocatorIS4_EEE7destro

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00bdef70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdef70.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdd9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9e0.md) [`00bdef70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdef70.md)
- 新版 呼出元 1件 [`00c5ba20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba20.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a430.md) [`00c5ba20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba20.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 50.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b052b0",
      "incomplete_value": true,
      "site": "00b052b8",
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
    "ordinal": 0,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b052b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b0529c.md#insn-00b052b8) · [`00b0529c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b0529c.md#insn-00b0529c) · [`00b052c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b0529c.md#insn-00b052c4)
- 新版 [`00b64f10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b64/00b64ef4.md#insn-00b64f10) · [`00b64ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b64/00b64ef4.md#insn-00b64ef4) · [`00b64f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b64/00b64ef4.md#insn-00b64f1c)

~~~diff
- 00b052b8 ["INT_ADD", "register:40f0:8", ["const:b052b8:8", "const:4:8"]]
- 00b052b8 ["CALL", null, ["callee:00c5ba20:8"]]
+ 00b64f10 ["INT_ADD", "register:40f0:8", ["const:b64f10:8", "const:4:8"]]
+ 00b64f10 ["CALL", null, ["callee:00c5ba20:8"]]
- 00b052b8 bytes 2e670394
+ 00b64f10 bytes c4da0394
- 00b0529c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b0529c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b64ef4 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b64ef4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b0529c bytes c10200b4
+ 00b64ef4 bytes c10200b4
- 00b052c4 ["INT_ADD", "register:40f0:8", ["const:b052c4:8", "const:4:8"]]
- 00b052c4 ["CALL", null, ["callee:00c5ba20:8"]]
+ 00b64f1c ["INT_ADD", "register:40f0:8", ["const:b64f1c:8", "const:4:8"]]
+ 00b64f1c ["CALL", null, ["callee:00c5ba20:8"]]
- 00b052c4 bytes 2b670394
+ 00b64f1c bytes c1da0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da22690256dcd76c9b2f4bb18273a7a5"></a>

### [`00b053d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b053d4.md) → [`00b6502c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b6502c.md) _ZN8firebase5MutexC1ENS0_4ModeE

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bdde20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde20.md) · 呼出先 6件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bdefd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefd0.md) [`00bdefe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefe0.md) [`00bdeff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeff0.md)
- 新版 呼出元 2件 [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a880.md) · 呼出先 6件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ba80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba80.md) [`00c5ba90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba90.md) [`00c5baa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5baa0.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 72.34% / 新版 72.34%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_value` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b053d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b053dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b053dc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b053d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b053dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b053e0",
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
      "00b65030",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b65034",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b65038",
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

- 旧版 [`00b053d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b053d4.md#insn-00b053d8) · [`00b053dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b053d4.md#insn-00b053dc) · [`00b053e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b053d4.md#insn-00b053e0)

~~~diff
- 00b053d8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00b053d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00b053d8 bytes f50b00f9
- 00b053dc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b053dc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b053dc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b053dc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b053dc bytes f44f02a9
- 00b053e0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b053e0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b053e0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b053e0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b053e0 bytes fd7b03a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed65c4fc4d4415396fa1057e19b7514f"></a>

### [`00b054b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b054b8.md) → [`00b65110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65110.md) _ZN8firebase5Mutex7AcquireEv

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 1件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) · 呼出先 2件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde820.md)
- 新版 呼出元 1件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) · 呼出先 2件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5b2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2a0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 50.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b65134",
      "PARAM",
      [
        "storage",
        "0029ce7b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b65134",
      "PARAM",
      [
        "storage",
        "002ad0db",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b054c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b054b8.md#insn-00b054c0) · [`00b054c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b054b8.md#insn-00b054c4) · [`00b054cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b054b8.md#insn-00b054cc)
- 新版 [`00b65118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65110.md#insn-00b65118) · [`00b6511c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65110.md#insn-00b6511c) · [`00b65124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65110.md#insn-00b65124)

~~~diff
- 00b054c0 ["INT_ADD", "register:40f0:8", ["const:b054c0:8", "const:4:8"]]
- 00b054c0 ["CALL", null, ["callee:00c5b2a0:8"]]
+ 00b65118 ["INT_ADD", "register:40f0:8", ["const:b65118:8", "const:4:8"]]
+ 00b65118 ["CALL", null, ["callee:00c5b2a0:8"]]
- 00b054c0 bytes d8640394
+ 00b65118 bytes 62d80394
- 00b054c4 ["INT_EQUAL", "tmp:0:1", ["register:4000:4", "const:0:4"]]
- 00b054c4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b6511c ["INT_EQUAL", "tmp:0:1", ["register:4000:4", "const:0:4"]]
+ 00b6511c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b054c4 bytes 60000034
+ 00b6511c bytes 60000034
- 00b054cc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b054cc ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b65124 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b65124 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b054cc bytes 61000054
+ 00b65124 bytes 61000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35f393a2e63046e1a309240ab9bdc0ef"></a>

### [`00b05510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05510.md) → [`00b65168`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65168.md) _ZN8firebase3app19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEENS_4util16Clas

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_value, call, call_count, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 56.25% / 新版 56.25%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b05510"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b05514"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b05514"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b05510",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b05514",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b65178",
      "READ",
      [
        "storage",
        "010a0d90",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b65168",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b6516c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b65178",
      "READ",
      [
        "storage",
        "01125c50",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05510.md#insn-00b05510) · [`00b05514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05510.md#insn-00b05514) · [`00b05534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05510.md#insn-00b05534)

~~~diff
- 00b05510 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b05510 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b05510 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b05510 bytes f30f1ef8
- 00b05514 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b05514 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b05514 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b05514 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b05514 bytes fd7b01a9
- 00b05534 ["INT_ADD", "register:40f0:8", ["const:b05534:8", "const:4:8"]]
- 00b05534 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b05534 bytes d7620394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e6b35cb4281ea88ad4ded93f5925b21"></a>

### [`00b05550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05550.md) → [`00b651a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b651a8.md) _ZN8firebase3app19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEE

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b651d4",
      "incomplete_value": true,
      "site": "00b651d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0557c",
      "incomplete_value": true,
      "site": "00b0557c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d90:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b651bc",
      "incomplete_value": true,
      "site": "00b651bc",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b05564",
      "incomplete_value": true,
      "site": "00b05564",
      "value": [
        "INT_NOTEQUAL",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b651c4",
      "incomplete_value": false,
      "site": "00b651cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b6000:8"
          ],
          [
            "leaf",
            "const:c6b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0556c",
      "incomplete_value": false,
      "site": "00b05574",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a6000:8"
          ],
          [
            "leaf",
            "const:1a7:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b651b8",
      "READ",
      [
        "storage",
        "010a0d90",
        null,
        "undefined8"
      ]
    ],
    [
      "00b651c4",
      "PARAM",
      [
        "storage",
        "002a61a7",
        null,
        "string"
      ]
    ],
    [
      "00b651d4",
      "WRITE",
      [
        "storage",
        "010a0d90",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b651b8",
      "READ",
      [
        "storage",
        "01125c50",
        null,
        "undefined8"
      ]
    ],
    [
      "00b651c4",
      "PARAM",
      [
        "storage",
        "002b6c6b",
        null,
        "string"
      ]
    ],
    [
      "00b651d4",
      "WRITE",
      [
        "storage",
        "01125c50",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05574`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05550.md#insn-00b05574) · [`00b0557c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05550.md#insn-00b0557c) · [`00b0555c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05550.md#insn-00b0555c)
- 新版 [`00b651cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b651a8.md#insn-00b651cc) · [`00b651d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b651a8.md#insn-00b651d4) · [`00b651b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b651a8.md#insn-00b651b4)

~~~diff
- 00b05574 ["INT_ADD", "register:40f0:8", ["const:b05574:8", "const:4:8"]]
- 00b05574 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b651cc ["INT_ADD", "register:40f0:8", ["const:b651cc:8", "const:4:8"]]
+ 00b651cc ["CALL", null, ["callee:00c5ab10:8"]]
- 00b05574 bytes c7620394
+ 00b651cc bytes 51d60394
- 00b0557c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d90:8"]]
- 00b0557c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b651d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c50:8"]]
+ 00b651d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b0557c bytes 60ca06f9
+ 00b651d4 bytes 602a06f9
- 00b0555c ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b651b4 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00b0555c bytes d32c00f0
+ 00b651b4 bytes 132e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07d7827b58abd99631353ee2799c18ca"></a>

### [`00b05590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05590.md) → [`00b651e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b651e8.md) _ZN8firebase3app10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 70.59% / 新版 70.59%

CFGの説明率　旧版 25.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b055c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b65218"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b651fc",
      "incomplete_value": true,
      "site": "00b651fc",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b055a4",
      "incomplete_value": true,
      "site": "00b055a4",
      "value": [
        "INT_NOTEQUAL",
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
      "00b651f8",
      "READ",
      [
        "storage",
        "010a0d90",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b055b0",
      "PARAM",
      [
        "storage",
        "002a61a7",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b055b8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ],
  "added": [
    [
      "00b651f8",
      "READ",
      [
        "storage",
        "01125c50",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65208",
      "PARAM",
      [
        "storage",
        "002b6c6b",
        null,
        "string"
      ]
    ],
    [
      "00b65210",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b055a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05590.md#insn-00b055a4) · [`00b055b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05590.md#insn-00b055b8) · [`00b055c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05590.md#insn-00b055c0)
- 新版 [`00b651fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b651e8.md#insn-00b651fc)

~~~diff
- 00b055a4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b055a4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b651fc ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b651fc ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b055a4 bytes 080100b5
+ 00b651fc bytes 080100b5
- 00b055b8 ["INT_ADD", "register:40f0:8", ["const:b055b8:8", "const:4:8"]]
- 00b055b8 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b055b8 bytes b6620394
- 00b055c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d90:8"]]
- 00b055c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b055c0 bytes 60ca06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64797999b5069cfb59c0ca99132cbafb"></a>

### [`00b055d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b055d4.md) → [`00b6522c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b6522c.md) _ZN8firebase3app10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b6525c",
      "incomplete_value": true,
      "site": "00b6525c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05604",
      "incomplete_value": true,
      "site": "00b05604",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d90:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b65240",
      "incomplete_value": true,
      "site": "00b65240",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b055e8",
      "incomplete_value": true,
      "site": "00b055e8",
      "value": [
        "INT_NOTEQUAL",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b65248",
      "incomplete_value": false,
      "site": "00b65254",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b6000:8"
          ],
          [
            "leaf",
            "const:c6b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b055f0",
      "incomplete_value": false,
      "site": "00b055fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a6000:8"
          ],
          [
            "leaf",
            "const:1a7:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b6523c",
      "READ",
      [
        "storage",
        "010a0d90",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65248",
      "PARAM",
      [
        "storage",
        "002a61a7",
        null,
        "string"
      ]
    ],
    [
      "00b6525c",
      "WRITE",
      [
        "storage",
        "010a0d90",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6523c",
      "READ",
      [
        "storage",
        "01125c50",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65248",
      "PARAM",
      [
        "storage",
        "002b6c6b",
        null,
        "string"
      ]
    ],
    [
      "00b6525c",
      "WRITE",
      [
        "storage",
        "01125c50",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b055fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b055d4.md#insn-00b055fc) · [`00b05604`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b055d4.md#insn-00b05604) · [`00b055e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b055d4.md#insn-00b055e0)
- 新版 [`00b65254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b6522c.md#insn-00b65254) · [`00b6525c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b6522c.md#insn-00b6525c) · [`00b65238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b6522c.md#insn-00b65238)

~~~diff
- 00b055fc ["INT_ADD", "register:40f0:8", ["const:b055fc:8", "const:4:8"]]
- 00b055fc ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b65254 ["INT_ADD", "register:40f0:8", ["const:b65254:8", "const:4:8"]]
+ 00b65254 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b055fc bytes a5620394
+ 00b65254 bytes 2fd60394
- 00b05604 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d90:8"]]
- 00b05604 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6525c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c50:8"]]
+ 00b6525c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b05604 bytes 60ca06f9
+ 00b6525c bytes 602a06f9
- 00b055e0 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b65238 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00b055e0 bytes d32c00f0
+ 00b65238 bytes 132e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aec2eb8555620992128d2825a3b3398b"></a>

### [`00b05624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05624.md) → [`00b6527c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b6527c.md) _ZN8firebase3app15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 50.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0567c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b652d4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b652b0",
      "incomplete_value": true,
      "site": "00b652bc",
      "value": [
        "LOAD",
        "8",
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
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:c50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05658",
      "incomplete_value": true,
      "site": "00b05664",
      "value": [
        "LOAD",
        "8",
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
                "const:10a0000:8"
              ],
              [
                "leaf",
                "const:d90:8"
              ]
            ]
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
      "00b65290",
      "READ",
      [
        "storage",
        "010a0d98",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b05658",
      "READ",
      [
        "storage",
        "010a0d90",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b0567c",
      "WRITE",
      [
        "storage",
        "010a0d98",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b65290",
      "READ",
      [
        "storage",
        "01125c58",
        null,
        "undefined1"
      ]
    ],
    [
      "00b652b0",
      "READ",
      [
        "storage",
        "01125c50",
        null,
        "undefined8"
      ]
    ],
    [
      "00b652d4",
      "WRITE",
      [
        "storage",
        "01125c58",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05624.md#insn-00b05664) · [`00b0567c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05624.md#insn-00b0567c)
- 新版 [`00b652bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b6527c.md#insn-00b652bc) · [`00b652d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b6527c.md#insn-00b652d4)

~~~diff
- 00b05664 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b05664 ["INT_ADD", "register:40f0:8", ["const:b05664:8", "const:4:8"]]
- 00b05664 ["CALLIND", null, ["register:0:8"]]
+ 00b652bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b652bc ["INT_ADD", "register:40f0:8", ["const:b652bc:8", "const:4:8"]]
+ 00b652bc ["CALLIND", null, ["register:0:8"]]
- 00b05664 bytes 00013fd6
+ 00b652bc bytes 00013fd6
- 00b0567c ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b0567c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:d98:8"]]
- 00b0567c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b0567c bytes a0623639
+ 00b652d4 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b652d4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:c58:8"]]
+ 00b652d4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b652d4 bytes a0623139
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7cbb96dc5b55adeef7d26012497d57db"></a>

### [`00b05690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05690.md) → [`00b652e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b652e8.md) _ZN8firebase3app12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 39.29% / 新版 39.29%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 7件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b05690"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b05694"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b05694"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b05690",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b05694",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b05698",
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
      "00b652e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b652ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b652f0",
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

- 旧版 [`00b05690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05690.md#insn-00b05690) · [`00b05694`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05690.md#insn-00b05694) · [`00b05698`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05690.md#insn-00b05698)

~~~diff
- 00b05690 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b05690 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b05690 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b05690 bytes f50f1df8
- 00b05694 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b05694 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b05694 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b05694 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b05694 bytes f44f01a9
- 00b05698 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b05698 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b05698 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b05698 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b05698 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1eae7d53accfac770f67308e12b4705"></a>

### [`00b05700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05700.md) → [`00b65358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65358.md) _ZN8firebase3app14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b05740"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b65398"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0571c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b05714",
      "READ",
      [
        "storage",
        "010a0d90",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b0571c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6539c"
      ]
    ],
    [
      "unmatched:00b05724",
      "PARAM",
      [
        "storage",
        "002a61a7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6536c",
      "READ",
      [
        "storage",
        "01125c50",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65374",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6539c"
      ]
    ],
    [
      "00b6537c",
      "PARAM",
      [
        "storage",
        "002b6c6b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0571c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05700.md#insn-00b0571c) · [`00b05738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05700.md#insn-00b05738) · [`00b05740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05700.md#insn-00b05740)
- 新版 [`00b65390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65358.md#insn-00b65390)

~~~diff
- 00b0571c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b0571c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b0571c bytes 410100b5
- 00b05738 ["INT_ADD", "register:40f0:8", ["const:b05738:8", "const:4:8"]]
- 00b05738 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b65390 ["INT_ADD", "register:40f0:8", ["const:b65390:8", "const:4:8"]]
+ 00b65390 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b05738 bytes 56620394
+ 00b65390 bytes e0d50394
- 00b05740 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d90:8"]]
- 00b05740 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b05740 bytes 80ca06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-171dc147bea19837efd1363730b6f863"></a>

### [`00b05770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05770.md) → [`00b653c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b653c8.md) _ZN8firebase3app11GetMethodIdENS0_6MethodE

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b653e4",
      "incomplete_value": false,
      "site": "00b653e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a8000:8"
          ],
          [
            "leaf",
            "const:29a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0578c",
      "incomplete_value": false,
      "site": "00b05790",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:547:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b653f4",
      "incomplete_value": true,
      "site": "00b65400",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0579c",
      "incomplete_value": true,
      "site": "00b057a8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              "INT_LEFT"
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
      "00b653e4",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b653f4",
      "DATA",
      [
        "storage",
        "010a0da0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b653e4",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b653f4",
      "DATA",
      [
        "storage",
        "01125c60",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05770.md#insn-00b05790) · [`00b05788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05770.md#insn-00b05788) · [`00b0578c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05770.md#insn-00b0578c)
- 新版 [`00b653e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b653c8.md#insn-00b653e8) · [`00b653e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b653c8.md#insn-00b653e0) · [`00b653e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b653c8.md#insn-00b653e4)

~~~diff
- 00b05790 ["INT_ADD", "register:40f0:8", ["const:b05790:8", "const:4:8"]]
- 00b05790 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b653e8 ["INT_ADD", "register:40f0:8", ["const:b653e8:8", "const:4:8"]]
+ 00b653e8 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b05790 bytes 7c620394
+ 00b653e8 bytes 06d60394
- 00b05788 ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00b653e0 ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00b05788 bytes 80bcfff0
+ 00b653e0 bytes 00bafff0
- 00b0578c ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b0578c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b0578c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b0578c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b653e4 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00b653e4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b653e4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b653e4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b0578c bytes 001c1591
+ 00b653e4 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-633585372168856edab60fa8e6a83e07"></a>

### [`00b057ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b057ac.md) → [`00b65404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65404.md) _ZN8firebase3app13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b057ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b65444"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b057c8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b057c0",
      "READ",
      [
        "storage",
        "010a0d90",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b057c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b65448"
      ]
    ],
    [
      "unmatched:00b057d0",
      "PARAM",
      [
        "storage",
        "002a61a7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b65418",
      "READ",
      [
        "storage",
        "01125c50",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65420",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b65448"
      ]
    ],
    [
      "00b65428",
      "PARAM",
      [
        "storage",
        "002b6c6b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b057c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b057ac.md#insn-00b057c8) · [`00b057e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b057ac.md#insn-00b057e4) · [`00b057ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b057ac.md#insn-00b057ec)
- 新版 [`00b6543c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65404.md#insn-00b6543c)

~~~diff
- 00b057c8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b057c8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b057c8 bytes 410100b5
- 00b057e4 ["INT_ADD", "register:40f0:8", ["const:b057e4:8", "const:4:8"]]
- 00b057e4 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b6543c ["INT_ADD", "register:40f0:8", ["const:b6543c:8", "const:4:8"]]
+ 00b6543c ["CALL", null, ["callee:00c5ab10:8"]]
- 00b057e4 bytes 2b620394
+ 00b6543c bytes b5d50394
- 00b057ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d90:8"]]
- 00b057ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b057ec bytes 80ca06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14711cb64e47b1785dbb0a7252166591"></a>

### [`00b0581c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b0581c.md) → [`00b65474`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65474.md) _ZN8firebase3app10GetFieldIdENS0_5FieldE

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b65490",
      "incomplete_value": false,
      "site": "00b65494",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a9000:8"
          ],
          [
            "leaf",
            "const:451:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05838",
      "incomplete_value": false,
      "site": "00b0583c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:299000:8"
          ],
          [
            "leaf",
            "const:5f2:8"
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
      "00b65490",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b654a0",
      "DATA",
      [
        "storage",
        "010a0de8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b65490",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b654a0",
      "DATA",
      [
        "storage",
        "01125ca8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0583c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b0581c.md#insn-00b0583c) · [`00b05834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b0581c.md#insn-00b05834) · [`00b05838`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b0581c.md#insn-00b05838)
- 新版 [`00b65494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65474.md#insn-00b65494) · [`00b6548c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65474.md#insn-00b6548c) · [`00b65490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65474.md#insn-00b65490)

~~~diff
- 00b0583c ["INT_ADD", "register:40f0:8", ["const:b0583c:8", "const:4:8"]]
- 00b0583c ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b65494 ["INT_ADD", "register:40f0:8", ["const:b65494:8", "const:4:8"]]
+ 00b65494 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b0583c bytes 51620394
+ 00b65494 bytes dbd50394
- 00b05834 ["COPY", "register:4000:8", ["const:299000:8"]]
+ 00b6548c ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 00b05834 bytes a0bcff90
+ 00b6548c bytes 20baff90
- 00b05838 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b05838 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b05838 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b05838 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b65490 ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00b65490 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b65490 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b65490 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b05838 bytes 00c81791
+ 00b65490 bytes 00441191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e628095c0b4c17210cb339813a93be93"></a>

### [`00b058d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b058d8.md) → [`00b65530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65530.md) _ZN8firebase15options_builder10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 52.94% / 新版 52.94%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b058d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b058dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b058dc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b058d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b058dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b65540",
      "READ",
      [
        "storage",
        "010a0df0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b65530",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b65534",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b65540",
      "READ",
      [
        "storage",
        "01125cb0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b058d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b058d8.md#insn-00b058d8) · [`00b058dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b058d8.md#insn-00b058dc) · [`00b058ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b058d8.md#insn-00b058ec)
- 新版 [`00b65544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65530.md#insn-00b65544)

~~~diff
- 00b058d8 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b058d8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b058d8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b058d8 bytes f30f1ef8
- 00b058dc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b058dc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b058dc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b058dc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b058dc bytes fd7b01a9
- 00b058ec ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b058ec ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b65544 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b65544 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00b058ec bytes 080100b5
+ 00b65544 bytes 080100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3739af79c824400947f84a1bdbf58c6d"></a>

### [`00b0591c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b0591c.md) → [`00b65574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65574.md) _ZN8firebase15options_builder10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 70.59% / 新版 70.59%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0591c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b05920"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b05920"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b0591c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b05920",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b65584",
      "READ",
      [
        "storage",
        "010a0df0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b65574",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b65578",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b65584",
      "READ",
      [
        "storage",
        "01125cb0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0591c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b0591c.md#insn-00b0591c) · [`00b05920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b0591c.md#insn-00b05920) · [`00b05930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b0591c.md#insn-00b05930)
- 新版 [`00b65588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65574.md#insn-00b65588)

~~~diff
- 00b0591c ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b0591c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b0591c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b0591c bytes f30f1ef8
- 00b05920 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b05920 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b05920 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b05920 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b05920 bytes fd7b01a9
- 00b05930 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b05930 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b65588 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b65588 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b05930 bytes 080100b5
+ 00b65588 bytes 080100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

