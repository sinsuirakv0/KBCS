# v15.7.4 → v16.0.0 · 命令位置の検査未完了 (18)

[一覧の目次](README.md)

<a id="compare-e7b1478001dfc1fe2d6a3acb3938e153"></a>

### [`00b70650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b70/00b70650.md) → [`00bdfb50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdfb50.md) _ZNK8firebase4auth4User16LinkWithProviderEPNS0_21FederatedAuthProviderE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bddd80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd80.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c5a7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7e0.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b70690"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7069c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bdfb90"
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
      "00bdfb60",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b70688"
      ]
    ],
    [
      "unmatched:00b7068c",
      "PARAM",
      [
        "storage",
        "002a5154",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b70690",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ac00"
      ]
    ]
  ],
  "added": [
    [
      "00bdfb60",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdfb88"
      ]
    ],
    [
      "00bdfb8c",
      "PARAM",
      [
        "storage",
        "002b5b82",
        null,
        "string"
      ]
    ],
    [
      "00bdfb90",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ac00"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b70690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b70/00b70650.md#insn-00b70690) · [`00b7069c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b70/00b70650.md#insn-00b7069c)
- 新版 `00bdfb90`（命令位置の公開資料なし）

~~~diff
- 00b70690 ["INT_ADD", "register:40f0:8", ["const:b70690:8", "const:4:8"]]
- 00b70690 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b70690 bytes bcb60194
- 00b7069c ["INT_ADD", "register:40f0:8", ["const:b7069c:8", "const:4:8"]]
- 00b7069c ["CALL", null, ["ram:bdde10:8"]]
- 00b7069c bytes ddb50194
+ 00bdfb90 ["INT_ADD", "register:40f0:8", ["const:bdfb90:8", "const:4:8"]]
+ 00bdfb90 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bdfb90 bytes 1cec0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afc4766aee7af930aa82e2482d3978fe"></a>

### [`00b71a8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b71/00b71a8c.md) → [`00be0f8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be0/00be0f8c.md) _ZN8firebase4auth14FutureCallbackINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEvP7_JNIEnvP8_jobjectNS_4util12FutureR

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b6eef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6eef0.md) · 呼出先 6件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md) [`00bddf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf80.md) [`00be0d20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0d20.md)
- 新版 呼出元 1件 [`00bde3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bde/00bde3f0.md) · 呼出先 6件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) [`00c5aa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa00.md) [`00c5d920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d920.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b71b0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b71b14"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00be100c"
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
      "unmatched:00b71b0c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bddc40"
      ]
    ],
    [
      "unmatched:00b71b14",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bddc40"
      ]
    ]
  ],
  "added": [
    [
      "00be100c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a690"
      ]
    ],
    [
      "00be1014",
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

- 旧版 [`00b71b0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b71/00b71a8c.md#insn-00b71b0c) · [`00b71b14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b71/00b71a8c.md#insn-00b71b14)
- 新版 `00be100c`（命令位置の公開資料なし）

~~~diff
- 00b71b0c ["INT_ADD", "register:40f0:8", ["const:b71b0c:8", "const:4:8"]]
- 00b71b0c ["CALL", null, ["ram:bddc40:8"]]
- 00b71b0c bytes 4db00194
- 00b71b14 ["INT_ADD", "register:40f0:8", ["const:b71b14:8", "const:4:8"]]
- 00b71b14 ["CALL", null, ["ram:bddc40:8"]]
- 00b71b14 bytes 4bb00194
+ 00be100c ["INT_ADD", "register:40f0:8", ["const:be100c:8", "const:4:8"]]
+ 00be100c ["CALL", null, ["ram:c5a690:8"]]
+ 00be100c bytes a1e50194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8944148649eb88d733bd1d5c2f1e4ac3"></a>

### [`00b71fb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b71/00b71fb0.md) → [`00be14b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be14b0.md) _ZNK8firebase4auth4User18GetTokenLastResultEv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddef0.md) [`00bddf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md) [`00c5aa10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa10.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 80.77% / 新版 80.77%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b71ff0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00be14f0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b71fe8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b71fe8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdde10"
      ]
    ],
    [
      "unmatched:00b71ff8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bddf90"
      ]
    ]
  ],
  "added": [
    [
      "00be14e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a870"
      ]
    ],
    [
      "00be14f8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5aa10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b71fe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b71/00b71fb0.md#insn-00b71fe8) · [`00b71ff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b71/00b71fb0.md#insn-00b71ff0) · [`00b71ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b71/00b71fb0.md#insn-00b71ff8)

~~~diff
- 00b71fe8 ["INT_ADD", "register:40f0:8", ["const:b71fe8:8", "const:4:8"]]
- 00b71fe8 ["CALL", null, ["ram:bdde10:8"]]
- 00b71fe8 bytes 8aaf0194
- 00b71ff0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:28:8"]]
- 00b71ff0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b71ff0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b71ff0 bytes 7f1600f9
- 00b71ff8 ["INT_ADD", "register:40f0:8", ["const:b71ff8:8", "const:4:8"]]
- 00b71ff8 ["CALL", null, ["ram:bddf90:8"]]
- 00b71ff8 bytes e6af0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91e1bfdad7ea8510a8f816ca57f6d957"></a>

### [`00b72040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b72040.md) → [`00be1540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1540.md) _ZNK8firebase4auth4User24UpdatePasswordLastResultEv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddef0.md) [`00bddf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md) [`00c5aa10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa10.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 76.92% / 新版 76.92%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b72080"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00be1580"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b72078"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b72078",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdde10"
      ]
    ],
    [
      "unmatched:00b72088",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bddf90"
      ]
    ]
  ],
  "added": [
    [
      "00be1578",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a870"
      ]
    ],
    [
      "00be1588",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5aa10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b72078`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b72040.md#insn-00b72078) · [`00b72080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b72040.md#insn-00b72080) · [`00b72088`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b72040.md#insn-00b72088)

~~~diff
- 00b72078 ["INT_ADD", "register:40f0:8", ["const:b72078:8", "const:4:8"]]
- 00b72078 ["CALL", null, ["ram:bdde10:8"]]
- 00b72078 bytes 66af0194
- 00b72080 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:28:8"]]
- 00b72080 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b72080 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b72080 bytes 7f1600f9
- 00b72088 ["INT_ADD", "register:40f0:8", ["const:b72088:8", "const:4:8"]]
- 00b72088 ["CALL", null, ["ram:bddf90:8"]]
- 00b72088 bytes c2af0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f050177ce5e5d72e16bd64d1b4b7cff6"></a>

### [`00b720d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b720d0.md) → [`00be15d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be15d0.md) _ZNK8firebase4auth4User28LinkWithCredentialLastResultEv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddef0.md) [`00bddf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md) [`00c5aa10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa10.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 65.38% / 新版 65.38%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b720d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b720d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b720d4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b720d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b720d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b720d8",
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
      "00be15d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00be15d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00be15d8",
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

- 旧版 [`00b720d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b720d0.md#insn-00b720d0) · [`00b720d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b720d0.md#insn-00b720d4) · [`00b720d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b720d0.md#insn-00b720d8)

~~~diff
- 00b720d0 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b720d0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b720d0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b720d0 bytes f50f1df8
- 00b720d4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b720d4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b720d4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b720d4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b720d4 bytes f44f01a9
- 00b720d8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b720d8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b720d8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b720d8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b720d8 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-185e04012c7adaaba4ece3ffb41874d9"></a>

### [`00b72280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b72280.md) → [`00be1780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be1780.md) _ZNK8firebase4auth4User31SendEmailVerificationLastResultEv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddef0.md) [`00bddf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md) [`00c5aa10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa10.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 80.77% / 新版 80.77%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b722c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00be17c0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b722b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b722b8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdde10"
      ]
    ],
    [
      "unmatched:00b722c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bddf90"
      ]
    ]
  ],
  "added": [
    [
      "00be17b8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a870"
      ]
    ],
    [
      "00be17c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5aa10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b722b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b72280.md#insn-00b722b8) · [`00b722c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b72280.md#insn-00b722c0) · [`00b722c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b72280.md#insn-00b722c8)

~~~diff
- 00b722b8 ["INT_ADD", "register:40f0:8", ["const:b722b8:8", "const:4:8"]]
- 00b722b8 ["CALL", null, ["ram:bdde10:8"]]
- 00b722b8 bytes d6ae0194
- 00b722c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:28:8"]]
- 00b722c0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b722c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b722c0 bytes 7f1600f9
- 00b722c8 ["INT_ADD", "register:40f0:8", ["const:b722c8:8", "const:4:8"]]
- 00b722c8 ["CALL", null, ["ram:bddf90:8"]]
- 00b722c8 bytes 32af0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eed6d617ffa647cfb5156e0cf1622d85"></a>

### [`00b724c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b724c0.md) → [`00be19c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be1/00be19c0.md) _ZNK8firebase4auth4User16ReloadLastResultEv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddef0.md) [`00bddf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a950.md) [`00c5aa10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa10.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 65.38% / 新版 65.38%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b724c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b724c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b724c4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b724c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b724c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b724c8",
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
      "00be19c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00be19c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00be19c8",
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

- 旧版 [`00b724c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b724c0.md#insn-00b724c0) · [`00b724c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b724c0.md#insn-00b724c4) · [`00b724c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b724c0.md#insn-00b724c8)

~~~diff
- 00b724c0 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b724c0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b724c0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b724c0 bytes f50f1df8
- 00b724c4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b724c4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b724c4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b724c4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b724c4 bytes f44f01a9
- 00b724c8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b724c8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b724c8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b724c8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b724c8 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1d24a4a5ef9340c764fc43ab5ea7b60"></a>

### [`00b729d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b729d8.md) → [`00bef5e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef5e0.md) _ZNSt6__ndk16chrono12steady_clock3nowEv

採用 · 移動量 `+0x7cc08` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdb070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb070.md) · 呼出先 3件 [`00bdb270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb270.md) [`00bdb2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2d0.md) [`00bdc8b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc8b0.md)
- 新版 呼出元 1件 [`00c57ac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ac0.md) · 呼出先 3件 [`00c57cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cc0.md) [`00c57d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d20.md) [`00c59300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59300.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b72a18"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b72a28"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bef620"
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
      "00bef5fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b72a18"
      ]
    ],
    [
      "unmatched:00b72a18",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57cc0"
      ]
    ],
    [
      "unmatched:00b72a24",
      "PARAM",
      [
        "storage",
        "0029568a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bef5fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bef620"
      ]
    ],
    [
      "00bef620",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57cc0"
      ]
    ],
    [
      "00bef62c",
      "PARAM",
      [
        "storage",
        "002a50c3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b72a14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b729d8.md#insn-00b72a14) · [`00b72a18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b729d8.md#insn-00b72a18) · [`00b72a28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b729d8.md#insn-00b72a28)

~~~diff
- 00b72a14 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b72a14 ["RETURN", null, ["register:0:8"]]
- 00b72a14 bytes c0035fd6
- 00b72a18 ["INT_ADD", "register:40f0:8", ["const:b72a18:8", "const:4:8"]]
- 00b72a18 ["CALL", null, ["callee:00c57cc0:8"]]
- 00b72a18 bytes 16a20194
- 00b72a28 ["INT_ADD", "register:40f0:8", ["const:b72a28:8", "const:4:8"]]
- 00b72a28 ["CALL", null, ["callee:00c57d20:8"]]
- 00b72a28 bytes 2aa20194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7cc3f7b73c8af09521dc2c5ad128f6c9"></a>

### [`00b72a30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b72a30.md) → [`00bef638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef638.md) _ZSt18uncaught_exceptionv

採用 · 移動量 `+0x7cc08` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be01f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01f0.md) · 呼出先 1件 [`00be0f00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0f00.md)
- 新版 呼出元 1件 [`00c5ccf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ccf0.md) · 呼出先 1件 [`00c5db00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5db00.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 55.56% / 新版 55.56%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b72a50"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00bef658"
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
      "unmatched:00b72a48",
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
      "00bef650",
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

- 旧版 [`00b72a50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b72a30.md#insn-00b72a50) · [`00b72a3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b72a30.md#insn-00b72a3c)
- 新版 `00bef658`（命令位置の公開資料なし） · `00bef644`（命令位置の公開資料なし）

~~~diff
- 00b72a50 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b72a50 ["RETURN", null, ["register:0:8"]]
- 00b72a50 bytes c0035fd6
+ 00bef658 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00bef658 ["RETURN", null, ["register:0:8"]]
+ 00bef658 bytes c0035fd6
- 00b72a3c ["INT_ADD", "register:40f0:8", ["const:b72a3c:8", "const:4:8"]]
- 00b72a3c ["CALL", null, ["callee:00c5db00:8"]]
+ 00bef644 ["INT_ADD", "register:40f0:8", ["const:bef644:8", "const:4:8"]]
+ 00bef644 ["CALL", null, ["callee:00c5db00:8"]]
- 00b72a3c bytes 31b90194
+ 00bef644 bytes 2fb90194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d11e203c7e3ce31971fa3d90ddde6a8"></a>

### [`00b72b44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b72b44.md) → [`00bef74c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef74c.md) _ZNSt16nested_exceptionD2Ev

採用 · 移動量 `+0x7cc08` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0f50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0f50.md) · 呼出先 1件 [`00bdb4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4a0.md)
- 新版 呼出元 1件 [`00c5db50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5db50.md) · 呼出先 1件 [`00c57ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ef0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

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
      "site": "00b72b54"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bef75c"
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
      "unmatched:00b72b4c",
      "READ",
      [
        "storage",
        "00c1bc40",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b72b54",
      "DATA",
      [
        "storage",
        "00c12c30",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "unmatched:00b72b58",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb4a0"
      ]
    ]
  ],
  "added": [
    [
      "00bef754",
      "READ",
      [
        "storage",
        "00c9b670",
        null,
        "pointer"
      ]
    ],
    [
      "00bef75c",
      "DATA",
      [
        "storage",
        "00c925d8",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "00bef760",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57ef0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b72b54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b72b44.md#insn-00b72b54) · [`00b72b48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b72b44.md#insn-00b72b48)
- 新版 `00bef75c`（命令位置の公開資料なし）

~~~diff
- 00b72b54 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b72b54 ["COPY", "tmp:1:8", ["register:4000:8"]]
- 00b72b54 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:8:8"]]
- 00b72b54 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b72b54 bytes 088400f8
+ 00bef75c ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00bef75c ["COPY", "tmp:1:8", ["register:4000:8"]]
+ 00bef75c ["INT_ADD", "register:4000:8", ["register:4000:8", "const:8:8"]]
+ 00bef75c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 00bef75c bytes 088400f8
- 00b72b48 ["COPY", "register:4040:8", ["const:c1b000:8"]]
- 00b72b48 bytes 480500b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-769ba1d7f3f7ff98ec97bec6adf9748d"></a>

### [`00b72b5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b72b5c.md) → [`00bef764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef764.md) _ZNSt16nested_exceptionD0Ev

採用 · 移動量 `+0x7cc08` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be0f50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5db50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5db50.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b72b70"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bef778"
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
      "unmatched:00b72b70",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be0f50"
      ]
    ]
  ],
  "added": [
    [
      "00bef778",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5db50"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b72b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b72b5c.md#insn-00b72b70)
- 新版 `00bef778`（命令位置の公開資料なし）

~~~diff
- 00b72b70 ["INT_ADD", "register:40f0:8", ["const:b72b70:8", "const:4:8"]]
- 00b72b70 ["CALL", null, ["ram:be0f50:8"]]
- 00b72b70 bytes f8b80194
+ 00bef778 ["INT_ADD", "register:40f0:8", ["const:bef778:8", "const:4:8"]]
+ 00bef778 ["CALL", null, ["ram:c5db50:8"]]
+ 00bef778 bytes f6b80194
~~~


<a id="compare-473b8770c4c3e3482974d38d4bf902be"></a>

### [`00b72bf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b72bf8.md) → [`00bef800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef800.md) _ZNSt6__ndk112__next_primeEm

採用 · 移動量 `+0x7cc08` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdd9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9d0.md) · 呼出先 1件 [`00b73318`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73318.md)
- 新版 呼出元 1件 [`00c5a420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a420.md) · 呼出先 1件 [`00beff20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00beff20.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 92.11% / 新版 92.11%

CFGの説明率　旧版 61.82% / 新版 62.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 15件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b72f24"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7305c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b73064"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bef830",
      "READ",
      [
        "storage",
        "002fa4b4",
        null,
        "undefined4"
      ]
    ],
    [
      "00bef830",
      "READ",
      [
        "storage",
        "002fa484",
        null,
        "undefined4"
      ]
    ],
    [
      "00bef844",
      "READ",
      [
        "storage",
        "002fa454",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00bef830",
      "READ",
      [
        "storage",
        "003102e8",
        null,
        "undefined4"
      ]
    ],
    [
      "00bef830",
      "READ",
      [
        "storage",
        "003102b8",
        null,
        "undefined4"
      ]
    ],
    [
      "00bef844",
      "READ",
      [
        "storage",
        "00310288",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b72f24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b72bf8.md#insn-00b72f24) · [`00b7305c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b72bf8.md#insn-00b7305c) · [`00b73064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b72/00b72bf8.md#insn-00b73064)

~~~diff
- 00b72f24 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b72f24 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b72f24 bytes e3e8ff54
- 00b7305c ["COPY", "tmp:0:8", ["const:0:8"]]
- 00b7305c ["INT_EQUAL", "tmp:1:1", ["register:4078:8", "const:0:8"]]
- 00b7305c ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 00b7305c ["INT_DIV", "tmp:0:8", ["register:4000:8", "register:4078:8"]]
- 00b7305c bytes 1008cf9a
- 00b73064 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b73064 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b73064 bytes e3deff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-efd8a2ec2846b7224ebd3bf3a84408f9"></a>

### [`00b733ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b733ac.md) → [`00beffb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00beffb4.md) _ZNSt6__ndk112bad_weak_ptrD0Ev

採用 · 移動量 `+0x7cc08` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdd940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd940.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a390.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b733c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00beffc8"
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
      "unmatched:00b733c0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdd940"
      ]
    ]
  ],
  "added": [
    [
      "00beffc8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a390"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b733c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b733ac.md#insn-00b733c0)
- 新版 `00beffc8`（命令位置の公開資料なし）

~~~diff
- 00b733c0 ["INT_ADD", "register:40f0:8", ["const:b733c0:8", "const:4:8"]]
- 00b733c0 ["CALL", null, ["ram:bdd940:8"]]
- 00b733c0 bytes 60a90194
+ 00beffc8 ["INT_ADD", "register:40f0:8", ["const:beffc8:8", "const:4:8"]]
+ 00beffc8 ["CALL", null, ["ram:c5a390:8"]]
+ 00beffc8 bytes f2a80194
~~~


<a id="compare-72cec907067ae74b78fb07fe5c02dac9"></a>

### [`00b734bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b734bc.md) → [`00bf00c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf00c4.md) _ZNSt6__ndk119__shared_weak_count16__release_sharedEv

採用 · 移動量 `+0x7cc08` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.77% / 新版 96.77%

CFGの説明率　旧版 33.33% / 新版 22.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b734d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b734bc.md#insn-00b734d8) · [`00b734dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b734bc.md#insn-00b734dc) · [`00b73500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b734bc.md#insn-00b73500)
- 新版 `00bf00e0`（命令位置の公開資料なし） · `00bf00e4`（命令位置の公開資料なし） · `00bf0108`（命令位置の公開資料なし）

~~~diff
- 00b734d8 ["INT_ADD", "register:40f0:8", ["const:b734d8:8", "const:4:8"]]
- 00b734d8 ["CALL", null, ["callee:00c538e0:8"]]
+ 00bf00e0 ["INT_ADD", "register:40f0:8", ["const:bf00e0:8", "const:4:8"]]
+ 00bf00e0 ["CALL", null, ["callee:00c538e0:8"]]
- 00b734d8 bytes 6e8e0194
+ 00bf00e0 bytes 008e0194
- 00b734dc ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00b734dc ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bf00e4 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00bf00e4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b734dc bytes a00000b4
+ 00bf00e4 bytes a00000b4
- 00b73500 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b73500 ["INT_ADD", "register:40f0:8", ["const:b73500:8", "const:4:8"]]
- 00b73500 ["CALLIND", null, ["register:0:8"]]
+ 00bf0108 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bf0108 ["INT_ADD", "register:40f0:8", ["const:bf0108:8", "const:4:8"]]
+ 00bf0108 ["CALLIND", null, ["register:0:8"]]
- 00b73500 bytes 00013fd6
+ 00bf0108 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b3477be64dc30497f2d1bb6a2e88cc1"></a>

### [`00b73538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73538.md) → [`00bf0140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0140.md) _ZNSt6__ndk119__shared_weak_count14__release_weakEv

採用 · 移動量 `+0x7cc08` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) · 呼出先 1件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)
- 新版 呼出元 1件 [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) · 呼出先 1件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 95.45% / 新版 95.45%

CFGの説明率　旧版 40.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b73554"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bf015c"
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
      "unmatched:00b73554",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bf017c"
      ]
    ]
  ],
  "added": [
    [
      "00bf015c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bf017c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b73554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73538.md#insn-00b73554) · [`00b7355c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73538.md#insn-00b7355c)
- 新版 `00bf015c`（命令位置の公開資料なし） · `00bf0164`（命令位置の公開資料なし）

~~~diff
- 00b73554 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b73554 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b73554 bytes 080100b4
+ 00bf015c ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bf015c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bf015c bytes 080100b4
- 00b7355c ["INT_ADD", "register:40f0:8", ["const:b7355c:8", "const:4:8"]]
- 00b7355c ["CALL", null, ["callee:00c538e0:8"]]
+ 00bf0164 ["INT_ADD", "register:40f0:8", ["const:bf0164:8", "const:4:8"]]
+ 00bf0164 ["CALL", null, ["callee:00c538e0:8"]]
- 00b7355c bytes 4d8e0194
+ 00bf0164 bytes df8d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-efeaefca73cd547ea984b024ea7046f6"></a>

### [`00b737b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b737b4.md) → [`00bf03bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf03bc.md) _ZNSt11logic_errorC1EPKc

採用 · 移動量 `+0x7cc08` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdb0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0e0.md) · 呼出先 3件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00c57b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b30.md) · 呼出先 3件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 89.66% / 新版 89.66%

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
      "site": "00b737dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bf03e4"
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
      "unmatched:00b737d4",
      "READ",
      [
        "storage",
        "00c1bc60",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b737dc",
      "DATA",
      [
        "storage",
        "00c16930",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00bf03dc",
      "READ",
      [
        "storage",
        "00c9b690",
        null,
        "pointer"
      ]
    ],
    [
      "00bf03e4",
      "DATA",
      [
        "storage",
        "00c962d8",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b737dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b737b4.md#insn-00b737dc) · [`00b737c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b737b4.md#insn-00b737c8)
- 新版 `00bf03e4`（命令位置の公開資料なし） · `00bf03d0`（命令位置の公開資料なし）

~~~diff
- 00b737dc ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00b737dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b737dc bytes 080000f9
+ 00bf03e4 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00bf03e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00bf03e4 bytes 080000f9
- 00b737c8 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00bf03d0 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00b737c8 bytes 48050090
+ 00bf03d0 bytes 480500f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6950dbb817a9d4fa7103fcc2f80694b4"></a>

### [`00b73a80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73a80.md) → [`00bf0688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0688.md) _ZNSt6__ndk121__throw_runtime_errorEPKc

採用 · 移動量 `+0x7cc08` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0fb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0fb0.md) · 呼出先 4件 [`00bbaeec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaeec.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00be0fc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0fc0.md)
- 新版 呼出元 1件 [`00c5dbb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dbb0.md) · 呼出先 4件 [`00c37934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37934.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c5dbc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dbc0.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 56.25% / 新版 56.25%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b73aa4"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b73abc"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bf06ac"
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
      "unmatched:00b73aa4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be0fc0"
      ]
    ],
    [
      "unmatched:00b73ab4",
      "READ",
      [
        "storage",
        "00c1bc70",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b73ab4",
      "PARAM",
      [
        "storage",
        "00c16ab0",
        "_ZTISt13runtime_error",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00bf06ac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5dbc0"
      ]
    ],
    [
      "00bf06bc",
      "READ",
      [
        "storage",
        "00c9b6a0",
        null,
        "pointer"
      ]
    ],
    [
      "00bf06bc",
      "PARAM",
      [
        "storage",
        "00c96458",
        "_ZTISt13runtime_error",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b73aa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73a80.md#insn-00b73aa4) · [`00b73abc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73a80.md#insn-00b73abc)
- 新版 `00bf06ac`（命令位置の公開資料なし）

~~~diff
- 00b73aa4 ["INT_ADD", "register:40f0:8", ["const:b73aa4:8", "const:4:8"]]
- 00b73aa4 ["CALL", null, ["ram:be0fc0:8"]]
- 00b73aa4 bytes 47b50194
- 00b73abc ["INT_ADD", "register:40f0:8", ["const:b73abc:8", "const:4:8"]]
- 00b73abc ["CALL", null, ["callee:00c57b10:8"]]
- 00b73abc bytes 819d0194
+ 00bf06ac ["INT_ADD", "register:40f0:8", ["const:bf06ac:8", "const:4:8"]]
+ 00bf06ac ["CALL", null, ["ram:c5dbc0:8"]]
+ 00bf06ac bytes 45b50194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2c654aaf64d8e68deff9e107e08cc3d"></a>

### [`00b73eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73eb0.md) → [`00bf0ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0ab8.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE16find_last_not_ofEPKcmm

採用 · 移動量 `+0x7cc08` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bd0.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 96.88% / 新版 96.88%

CFGの説明率　旧版 50.00% / 新版 57.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b73f2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00bf0b34"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b73f2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73eb0.md#insn-00b73f2c) · [`00b73f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73eb0.md#insn-00b73f0c)
- 新版 `00bf0b34`（命令位置の公開資料なし） · `00bf0b14`（命令位置の公開資料なし）

~~~diff
- 00b73f2c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b73f2c ["RETURN", null, ["register:0:8"]]
- 00b73f2c bytes c0035fd6
+ 00bf0b34 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00bf0b34 ["RETURN", null, ["register:0:8"]]
+ 00bf0b34 bytes c0035fd6
- 00b73f0c ["INT_ADD", "register:40f0:8", ["const:b73f0c:8", "const:4:8"]]
- 00b73f0c ["CALL", null, ["callee:00c57bd0:8"]]
+ 00bf0b14 ["INT_ADD", "register:40f0:8", ["const:bf0b14:8", "const:4:8"]]
+ 00bf0b14 ["CALL", null, ["callee:00c57bd0:8"]]
- 00b73f0c bytes 9d9c0194
+ 00bf0b14 bytes 2f9c0194
~~~


<a id="compare-e8156253e1b7b90dca8fc68db182f0dc"></a>

### [`00b73f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73f48.md) → [`00bf0b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0b50.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE17find_first_not_ofEPKcmm

採用 · 移動量 `+0x7cc08` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change` · `reordered`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bd0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 94.29% / 新版 94.29%

CFGの説明率　旧版 46.15% / 新版 54.55%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b73fac"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bf0bb4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b73fd0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b73fac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bf0b98"
      ]
    ]
  ],
  "added": [
    [
      "00bf0bb4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bf0b98"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b73fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73f48.md#insn-00b73fac) · [`00b73fd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73f48.md#insn-00b73fd0)
- 新版 `00bf0bb4`（命令位置の公開資料なし）

~~~diff
- 00b73fac ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b73fac ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b73fac bytes 21ffff54
- 00b73fd0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b73fd0 ["RETURN", null, ["register:0:8"]]
- 00b73fd0 bytes c0035fd6
+ 00bf0bb4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00bf0bb4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bf0bb4 bytes 21ffff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36e880165397fc0409685d84684bacd7"></a>

### [`00b74194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74194.md) → [`00bf0bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0bdc.md) FUN_00bf0bdc

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change` · `reordered`

- 旧版 呼出元 1件 [`00b7445c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b7445c.md) · 呼出先 4件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`00bf0ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0ea4.md) · 呼出先 4件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 98.70% / 新版 98.70%

CFGの説明率　旧版 84.21% / 新版 88.89%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b742bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00bf0d04"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b742bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74194.md#insn-00b742bc) · [`00b741c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74194.md#insn-00b741c4)
- 新版 `00bf0d04`（命令位置の公開資料なし） · `00bf0c0c`（命令位置の公開資料なし）

~~~diff
- 00b742bc ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b742bc ["RETURN", null, ["register:0:8"]]
- 00b742bc bytes c0035fd6
+ 00bf0d04 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00bf0d04 ["RETURN", null, ["register:0:8"]]
+ 00bf0d04 bytes c0035fd6
- 00b741c4 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b741c4 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
+ 00bf0c0c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00bf0c0c ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 00b741c4 bytes e3070054
+ 00bf0c0c bytes e3070054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54322ca1e98cae2ed3ff93c0528d0169"></a>

### [`00b74590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74590.md) → [`00bf0fd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0fd8.md) FUN_00bf0fd8

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b746dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b746dc.md) [`00b75128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75128.md) · 呼出先 5件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 2件 [`00bf1124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1124.md) [`00bf1b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1b70.md) · 呼出先 5件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 77.11% / 新版 77.11%

CFGの説明率　旧版 32.14% / 新版 40.91%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 8件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b746a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bf10f0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b745d0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b745d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bf1070"
      ]
    ],
    [
      "unmatched:00b745e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bf111c"
      ]
    ],
    [
      "unmatched:00b74604",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bf10a0"
      ]
    ]
  ],
  "added": [
    [
      "00bf1020",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bf1070"
      ]
    ],
    [
      "00bf1030",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bf111c"
      ]
    ],
    [
      "00bf104c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bf10a0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b745d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74590.md#insn-00b745d0) · [`00b745d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74590.md#insn-00b745d8) · [`00b745e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74590.md#insn-00b745e8)

~~~diff
- 00b745d0 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b745d0 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b745d0 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b745d0 ["COPY", "register:4048:8", ["tmp:0:8"]]
- 00b745d0 bytes 4901899a
- 00b745d8 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b745d8 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00b745d8 ["CBRANCH", null, ["local:b9:8", "tmp:1:1"]]
- 00b745d8 bytes 89020054
- 00b745e8 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b745e8 ["CBRANCH", null, ["local:b22:8", "tmp:0:1"]]
- 00b745e8 bytes 63070054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac88b84e95f188565ced0c97e84c575e"></a>

### [`00b7479c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b7479c.md) → [`00bf11e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf11e4.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1ERKS5_mmRKS4_

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`0041fddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`004428dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428dc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 75.00% / 新版 81.82%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b747c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b747d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bf1210"
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
      "unmatched:00b747d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bf12b0"
      ]
    ]
  ],
  "added": [
    [
      "00bf1218",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bf12b0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b747c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b7479c.md#insn-00b747c8) · [`00b747d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b7479c.md#insn-00b747d0)
- 新版 `00bf1210`（命令位置の公開資料なし）

~~~diff
- 00b747c8 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b747c8 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b747c8 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b747c8 ["COPY", "register:4048:8", ["tmp:0:8"]]
- 00b747c8 bytes 4901899a
- 00b747d0 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b747d0 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00b747d0 bytes c3040054
+ 00bf1210 ["COPY", "tmp:0:8", ["register:4050:8"]]
+ 00bf1210 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
+ 00bf1210 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00bf1210 ["COPY", "register:4048:8", ["tmp:0:8"]]
+ 00bf1210 bytes 4901899a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c88c97b24900285f6972f3c76ce70574"></a>

### [`00b74d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74d24.md) → [`00bf176c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf176c.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE5eraseEmm

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdcae0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcae0.md) · 呼出先 2件 [`0041fddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md) [`00b74d9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74d9c.md)
- 新版 呼出元 1件 [`00c59530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59530.md) · 呼出先 2件 [`004428dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428dc.md) [`00bf17e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf17e4.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 72.73% / 新版 80.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b74d44"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b74d4c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bf178c"
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
      "unmatched:00b74d4c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bf17e0"
      ]
    ]
  ],
  "added": [
    [
      "00bf1794",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bf17e0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b74d44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74d24.md#insn-00b74d44) · [`00b74d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74d24.md#insn-00b74d4c)
- 新版 `00bf178c`（命令位置の公開資料なし）

~~~diff
- 00b74d44 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b74d44 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b74d44 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b74d44 ["COPY", "register:4048:8", ["tmp:0:8"]]
- 00b74d44 bytes 4901899a
- 00b74d4c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b74d4c ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00b74d4c bytes 63020054
+ 00bf178c ["COPY", "tmp:0:8", ["register:4050:8"]]
+ 00bf178c ["CBRANCH", null, ["const:2:4", "register:101:1"]]
+ 00bf178c ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00bf178c ["COPY", "register:4048:8", ["tmp:0:8"]]
+ 00bf178c bytes 4901899a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c3b46de6da6fa779506cc481ab10be5"></a>

### [`00b75038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75038.md) → [`00bf1a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1a80.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7compareEmmPKc

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`0041fddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 0件  · 呼出先 3件 [`004428dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428dc.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.56% / 新版 97.56%

CFGの説明率　旧版 50.00% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b75094"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bf1adc"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b75094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75038.md#insn-00b75094) · [`00b75060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75038.md#insn-00b75060)
- 新版 `00bf1adc`（命令位置の公開資料なし） · `00bf1aa8`（命令位置の公開資料なし）

~~~diff
- 00b75094 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b75094 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00b75094 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b75094 ["COPY", "tmp:1:8", ["register:40b0:8"]]
- 00b75094 bytes 2931969a
+ 00bf1adc ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00bf1adc ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00bf1adc ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
+ 00bf1adc ["COPY", "tmp:1:8", ["register:40b0:8"]]
+ 00bf1adc bytes 2931969a
- 00b75060 ["INT_ADD", "register:40f0:8", ["const:b75060:8", "const:4:8"]]
- 00b75060 ["CALL", null, ["callee:00c57be0:8"]]
+ 00bf1aa8 ["INT_ADD", "register:40f0:8", ["const:bf1aa8:8", "const:4:8"]]
+ 00bf1aa8 ["CALL", null, ["callee:00c57be0:8"]]
- 00b75060 bytes 4c980194
+ 00bf1aa8 bytes 4e980194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2eab5a1198858ddbde2a5b588768d149"></a>

### [`00b75234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75234.md) → [`00bf1c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1c7c.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7compareEmmRKS5_mm

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 93.18% / 新版 93.18%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7527c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bf1cc4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b752e0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b752dc",
      "PARAM",
      [
        "storage",
        "0029f2c1",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b752e0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0041fdf0"
      ]
    ]
  ],
  "added": [
    [
      "00bf1d24",
      "PARAM",
      [
        "storage",
        "002af6d4",
        null,
        "string"
      ]
    ],
    [
      "00bf1d28",
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

- 旧版 [`00b7527c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75234.md#insn-00b7527c) · [`00b752e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75234.md#insn-00b752e0)
- 新版 `00bf1cc4`（命令位置の公開資料なし）

~~~diff
- 00b7527c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b7527c ["COPY", "tmp:1:8", ["register:4058:8"]]
- 00b7527c ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b7527c ["COPY", "tmp:1:8", ["register:4010:8"]]
- 00b7527c bytes 7331829a
- 00b752e0 ["INT_ADD", "register:40f0:8", ["const:b752e0:8", "const:4:8"]]
- 00b752e0 ["CALL", null, ["ram:41fdf0:8"]]
- 00b752e0 bytes c4aae297
+ 00bf1cc4 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00bf1cc4 ["COPY", "tmp:1:8", ["register:4058:8"]]
+ 00bf1cc4 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
+ 00bf1cc4 ["COPY", "tmp:1:8", ["register:4010:8"]]
+ 00bf1cc4 bytes 7331829a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eaa52b4511488799458523fe284edda2"></a>

### [`00b755f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b755f4.md) → [`00bf203c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf203c.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7replaceEmmRKS5_mm

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`0041fddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md) [`00bdb220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb220.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004428dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428dc.md) [`00c57c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c70.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b75610"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bf2058"
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
      "unmatched:00b75610",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bf207c"
      ]
    ]
  ],
  "added": [
    [
      "00bf2058",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bf207c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b75610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b755f4.md#insn-00b75610) · [`00b7560c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b755f4.md#insn-00b7560c)
- 新版 `00bf2058`（命令位置の公開資料なし）

~~~diff
- 00b75610 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b75610 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b75610 bytes 23010054
+ 00bf2058 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00bf2058 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bf2058 bytes 23010054
- 00b7560c ["COPY", "tmp:0:8", ["register:4020:8"]]
- 00b7560c ["INT_LESSEQUAL", "register:105:1", ["tmp:0:8", "register:4048:8"]]
- 00b7560c ["INT_SBORROW", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00b7560c ["INT_SUB", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00b7560c bytes 290104eb
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9653aad22c8d20b1d33933f072160706"></a>

### [`00b75a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75a68.md) → [`00bf24b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf24b0.md) FUN_00bf24b0

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 17件 [`00b75890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75890.md) [`00b75f6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75f6c.md) [`00b761ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b761ac.md) [`00b761f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b761f4.md) [`00b763a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b763a0.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)
- 新版 呼出元 17件 [`00bf22d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf22d8.md) [`00bf29b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf29b4.md) [`00bf2bf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf2bf4.md) [`00bf2c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf2c3c.md) [`00bf2de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf2de8.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b75a7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bf24c4"
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
      "unmatched:00b75a78",
      "PARAM",
      [
        "storage",
        "002a924c",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b75a7c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0041fdf0"
      ]
    ]
  ],
  "added": [
    [
      "00bf24c0",
      "PARAM",
      [
        "storage",
        "002b9ee3",
        null,
        "string"
      ]
    ],
    [
      "00bf24c4",
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

- 旧版 [`00b75a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75a68.md#insn-00b75a7c) · [`00b75a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75a68.md#insn-00b75a74)
- 新版 `00bf24c4`（命令位置の公開資料なし） · `00bf24bc`（命令位置の公開資料なし）

~~~diff
- 00b75a7c ["INT_ADD", "register:40f0:8", ["const:b75a7c:8", "const:4:8"]]
- 00b75a7c ["CALL", null, ["ram:41fdf0:8"]]
- 00b75a7c bytes dda8e297
+ 00bf24c4 ["INT_ADD", "register:40f0:8", ["const:bf24c4:8", "const:4:8"]]
+ 00bf24c4 ["CALL", null, ["ram:4428f0:8"]]
+ 00bf24c4 bytes 0b41e197
- 00b75a74 ["COPY", "register:4000:8", ["const:2a9000:8"]]
+ 00bf24bc ["COPY", "register:4000:8", ["const:2b9000:8"]]
- 00b75a74 bytes a0b9ff90
+ 00bf24bc bytes 20b6fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19c2a22fc45a100a4925295c262fdb24"></a>

### [`00b75a80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75a80.md) → [`00bf24c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf24c8.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE21__grow_by_and_replaceEmmmmmmPKw

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be1000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1000.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8a4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`00c5dbf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dbf0.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`006d7660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7660.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 94.79% / 新版 94.79%

CFGの説明率　旧版 44.44% / 新版 52.17%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b75b04"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b75b0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b75b8c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b75b0c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bf2570"
      ]
    ],
    [
      "unmatched:00b75b8c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bf25f0"
      ]
    ]
  ],
  "added": [
    [
      "00bf2554",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bf2570"
      ]
    ],
    [
      "00bf25d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bf25f0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b75b04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75a80.md#insn-00b75b04) · [`00b75b0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75a80.md#insn-00b75b0c) · [`00b75b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75a80.md#insn-00b75b8c)

~~~diff
- 00b75b04 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b75b04 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00b75b04 ["COPY", "tmp:2:8", ["register:4048:8"]]
- 00b75b04 ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 00b75b04 bytes 2881889a
- 00b75b0c ["CBRANCH", null, ["local:b7:8", "register:102:1"]]
- 00b75b0c bytes e2000054
- 00b75b8c ["CBRANCH", null, ["local:b15:8", "register:101:1"]]
- 00b75b8c bytes e0000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97de131efe30bdd4675fa6bb9c495ac3"></a>

### [`00b75c00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75c00.md) → [`00bf2648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf2648.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE5rfindEPKwmm

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.96% / 新版 97.96%

CFGの説明率　旧版 47.83% / 新版 55.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b75c78"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bf26c0"
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
      "unmatched:00b75c78",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bf26e8"
      ]
    ]
  ],
  "added": [
    [
      "00bf26c0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bf26e8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b75c78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75c00.md#insn-00b75c78) · [`00b75c3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75c00.md#insn-00b75c3c)
- 新版 `00bf26c0`（命令位置の公開資料なし） · `00bf2684`（命令位置の公開資料なし）

~~~diff
- 00b75c78 ["CBRANCH", null, ["local:b13:8", "register:101:1"]]
- 00b75c78 bytes 40010054
+ 00bf26c0 ["CBRANCH", null, ["local:b11:8", "register:101:1"]]
+ 00bf26c0 bytes 40010054
- 00b75c3c ["INT_EQUAL", "tmp:0:1", ["register:4018:8", "const:0:8"]]
- 00b75c3c ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
+ 00bf2684 ["INT_EQUAL", "tmp:0:1", ["register:4018:8", "const:0:8"]]
+ 00bf2684 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
- 00b75c3c bytes 630300b4
+ 00bf2684 bytes 630300b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4dd32344f3c0925087fbc78a8693f22a"></a>

### [`00b75f6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75f6c.md) → [`00bf29b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf29b4.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6insertEmmw

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be1020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1020.md) · 呼出先 3件 [`00b75a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75a68.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdda50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda50.md)
- 新版 呼出元 1件 [`00c5dc10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dc10.md) · 呼出先 3件 [`00bf24b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf24b0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c5a4a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4a0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 87.21% / 新版 87.21%

CFGの説明率　旧版 39.29% / 新版 45.83%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 5件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b76080"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bf2ac8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b75fc4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b75fd0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bf2a4c"
      ]
    ],
    [
      "unmatched:00b76048",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b7607c"
      ]
    ],
    [
      "unmatched:00b76078",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bf2ad0"
      ]
    ]
  ],
  "added": [
    [
      "00bf2a18",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bf2a4c"
      ]
    ],
    [
      "00bf2a90",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bf2ac4"
      ]
    ],
    [
      "00bf2ac0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bf2ad0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b75fc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75f6c.md#insn-00b75fc4) · [`00b75fd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75f6c.md#insn-00b75fd0) · [`00b76048`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75f6c.md#insn-00b76048)

~~~diff
- 00b75fc4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b75fc4 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b75fc4 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b75fc4 ["COPY", "register:4008:8", ["tmp:0:8"]]
- 00b75fc4 bytes 01018a9a
- 00b75fd0 ["CBRANCH", null, ["local:b5:8", "register:102:1"]]
- 00b75fd0 bytes a2010054
- 00b76048 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b76048 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 00b76048 bytes a3010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f809163bf4b92eef707d604e6e79cd43"></a>

### [`00b763a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b763a0.md) → [`00bf2de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf2de8.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE7replaceEmmmw

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00b75a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75a68.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdda50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda50.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bf24b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf24b0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c5a4a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4a0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.94% / 新版 96.94%

CFGの説明率　旧版 88.46% / 新版 92.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b763cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b763d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bf2e14"
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
      "unmatched:00b763d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bf2f6c"
      ]
    ]
  ],
  "added": [
    [
      "00bf2e1c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bf2f6c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b763cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b763a0.md#insn-00b763cc) · [`00b763d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b763a0.md#insn-00b763d4)
- 新版 `00bf2e14`（命令位置の公開資料なし）

~~~diff
- 00b763cc ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b763cc ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b763cc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b763cc ["COPY", "register:40a0:8", ["tmp:0:8"]]
- 00b763cc bytes 5401889a
- 00b763d4 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b763d4 ["CBRANCH", null, ["local:b17:8", "tmp:0:1"]]
- 00b763d4 bytes 830a0054
+ 00bf2e14 ["COPY", "tmp:0:8", ["register:4050:8"]]
+ 00bf2e14 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
+ 00bf2e14 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00bf2e14 ["COPY", "register:40a0:8", ["tmp:0:8"]]
+ 00bf2e14 bytes 5401889a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98c6a894487b2a0f1d2983d93ccf180f"></a>

### [`00b76694`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b76694.md) → [`00bf30dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf30dc.md) FUN_00bf30dc

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b765f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b765f8.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`00bf3040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3040.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 95.89% / 新版 95.89%

CFGの説明率　旧版 76.00% / 新版 76.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b766f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bf3140"
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
      "unmatched:00b766f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bf31cc"
      ]
    ]
  ],
  "added": [
    [
      "00bf3140",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bf31cc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b766f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b76694.md#insn-00b766f8) · [`00b766d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b76694.md#insn-00b766d0)
- 新版 `00bf3140`（命令位置の公開資料なし） · `00bf3118`（命令位置の公開資料なし）

~~~diff
- 00b766f8 ["CBRANCH", null, ["local:b13:8", "register:102:1"]]
- 00b766f8 bytes 62040054
+ 00bf3140 ["CBRANCH", null, ["local:b13:8", "register:102:1"]]
+ 00bf3140 bytes 62040054
- 00b766d0 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b766d0 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00b766d0 ["CBRANCH", null, ["local:b4:8", "tmp:1:1"]]
+ 00bf3118 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00bf3118 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
+ 00bf3118 ["CBRANCH", null, ["local:b5:8", "tmp:1:1"]]
- 00b766d0 bytes e9010054
+ 00bf3118 bytes e9010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6e804aaae21baed9790ed0f42441006"></a>

### [`00b76a6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b76a6c.md) → [`00bf34b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf34b4.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE4findEwm

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb600.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58050.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 33.33% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b76aa8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bf34f0"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b76aa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b76a6c.md#insn-00b76aa8) · [`00b76a88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b76a6c.md#insn-00b76a88)
- 新版 `00bf34f0`（命令位置の公開資料なし） · `00bf34d0`（命令位置の公開資料なし）

~~~diff
- 00b76aa8 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b76aa8 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b76aa8 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b76aa8 ["COPY", "register:4098:8", ["tmp:0:8"]]
- 00b76aa8 bytes 73018a9a
+ 00bf34f0 ["COPY", "tmp:0:8", ["register:4058:8"]]
+ 00bf34f0 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
+ 00bf34f0 ["COPY", "tmp:0:8", ["register:4050:8"]]
+ 00bf34f0 ["COPY", "register:4098:8", ["tmp:0:8"]]
+ 00bf34f0 bytes 73018a9a
- 00b76a88 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b76a88 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00b76a88 ["CBRANCH", null, ["local:b3:8", "tmp:1:1"]]
+ 00bf34d0 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00bf34d0 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
+ 00bf34d0 ["CBRANCH", null, ["local:b2:8", "tmp:1:1"]]
- 00b76a88 bytes 89020054
+ 00bf34d0 bytes 89020054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-acb03e48cc58faee1f74584e20683bd9"></a>

### [`00b76ae0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b76ae0.md) → [`00bf3528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3528.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6__initEmw

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8a4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`006d7660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7660.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 85.71% / 新版 90.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b76ae4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b76ae4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b76ae8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b76ae4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b76ae8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b76aec",
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
      "00bf352c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bf3530",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bf3534",
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

- 旧版 [`00b76ae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b76ae0.md#insn-00b76ae4) · [`00b76ae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b76ae0.md#insn-00b76ae8) · [`00b76aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b76ae0.md#insn-00b76aec)

~~~diff
- 00b76ae4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b76ae4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b76ae4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b76ae4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b76ae4 bytes fd7bbda9
- 00b76ae8 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b76ae8 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b76ae8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b76ae8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b76ae8 bytes f65701a9
- 00b76aec ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b76aec ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b76aec ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b76aec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b76aec bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a61c33ebfccce9fc610e0ed231a94b1"></a>

### [`00b76c1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b76c1c.md) → [`00bf3664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3664.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE12find_last_ofEPKwmm

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb600.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58050.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.44% / 新版 97.44%

CFGの説明率　旧版 36.36% / 新版 44.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b76c34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b76c1c.md#insn-00b76c34) · [`00b76c48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b76c1c.md#insn-00b76c48) · [`00b76c74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b76c1c.md#insn-00b76c74)
- 新版 `00bf367c`（命令位置の公開資料なし） · `00bf36bc`（命令位置の公開資料なし）

~~~diff
- 00b76c34 ["INT_EQUAL", "tmp:0:1", ["register:4018:8", "const:0:8"]]
- 00b76c34 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00bf367c ["INT_EQUAL", "tmp:0:1", ["register:4018:8", "const:0:8"]]
+ 00bf367c ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b76c34 bytes 230300b4
+ 00bf367c bytes 230300b4
- 00b76c48 ["COPY", "register:40e8:8", ["register:8:8"]]
- 00b76c48 bytes fd030091
- 00b76c74 ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
- 00b76c74 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 00bf36bc ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
+ 00bf36bc ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00b76c74 bytes 750100b4
+ 00bf36bc bytes 750100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-841e09de25f58f5bc9f50dc2a8aa3971"></a>

### [`00b76cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b76cb8.md) → [`00bf3700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3700.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE9__grow_byEmmmmmm

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdda50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda50.md) · 呼出先 5件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8a4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`00c5a4a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4a0.md) · 呼出先 5件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`006d7660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7660.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 91.25% / 新版 91.25%

CFGの説明率　旧版 25.00% / 新版 31.58%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b76d1c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b76d34"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b76d3c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b76d3c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bf3790"
      ]
    ],
    [
      "unmatched:00b76d94",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bf37f8"
      ]
    ]
  ],
  "added": [
    [
      "00bf3784",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bf3790"
      ]
    ],
    [
      "00bf37dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bf37f8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b76d1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b76cb8.md#insn-00b76d1c) · [`00b76d34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b76cb8.md#insn-00b76d34) · [`00b76d3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b76cb8.md#insn-00b76d3c)

~~~diff
- 00b76d1c ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b76d1c ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b76d1c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b76d1c ["COPY", "register:40b8:8", ["tmp:0:8"]]
- 00b76d1c bytes 5701899a
- 00b76d34 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b76d34 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00b76d34 ["COPY", "tmp:2:8", ["register:4048:8"]]
- 00b76d34 ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 00b76d34 bytes 2881889a
- 00b76d3c ["CBRANCH", null, ["local:b7:8", "register:102:1"]]
- 00b76d3c bytes 62000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41dbdb0632e41aa3174f7a91f3d9b08b"></a>

### [`00b76fc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b76fc8.md) → [`00bf3a10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3a10.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE5rfindEwm

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 72.73% / 新版 72.73%

CFGの説明率　旧版 44.44% / 新版 57.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b76fe0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b76fe4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b76fe8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b76fe8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bf3a60"
      ]
    ]
  ],
  "added": [
    [
      "00bf3a30",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bf3a60"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b76fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b76fc8.md#insn-00b76fe0) · [`00b76fe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b76fc8.md#insn-00b76fe4) · [`00b76fe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b76/00b76fc8.md#insn-00b76fe8)

~~~diff
- 00b76fe0 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b76fe0 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b76fe0 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b76fe0 ["COPY", "register:4040:8", ["tmp:0:8"]]
- 00b76fe0 bytes 4801899a
- 00b76fe4 ["COPY", "tmp:0:8", ["register:4060:8"]]
- 00b76fe4 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b76fe4 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b76fe4 ["COPY", "register:4048:8", ["tmp:0:8"]]
- 00b76fe4 bytes 89018b9a
- 00b76fe8 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b76fe8 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00b76fe8 bytes 880100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c02b3b21436de35da8f846f6e9ef833"></a>

### [`00b77138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b77138.md) → [`00bf3b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3b80.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE5eraseEmm

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00b75a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75a68.md) [`00b771b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b771b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bf24b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf24b0.md) [`00bf3bf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3bf8.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 66.67% / 新版 80.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b77158"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b77160"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bf3ba0"
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
      "unmatched:00b77160",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bf3bf4"
      ]
    ]
  ],
  "added": [
    [
      "00bf3ba8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bf3bf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b77158`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b77138.md#insn-00b77158) · [`00b77160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b77138.md#insn-00b77160)
- 新版 `00bf3ba0`（命令位置の公開資料なし）

~~~diff
- 00b77158 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b77158 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b77158 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b77158 ["COPY", "register:4048:8", ["tmp:0:8"]]
- 00b77158 bytes 4901899a
- 00b77160 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b77160 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 00b77160 bytes 63020054
+ 00bf3ba0 ["COPY", "tmp:0:8", ["register:4050:8"]]
+ 00bf3ba0 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
+ 00bf3ba0 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00bf3ba0 ["COPY", "register:4048:8", ["tmp:0:8"]]
+ 00bf3ba0 bytes 4901899a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f5e8ea12d8bba3c92dc88133b4758a9"></a>

### [`00b7724c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b7724c.md) → [`00bf3c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3c94.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6appendERKS5_mm

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00b75a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75a68.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00be1000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1000.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bf24b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf24b0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c5dbf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dbf0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 76.12% / 新版 76.12%

CFGの説明率　旧版 53.33% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b77294"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b772a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b772b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b772cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bf3d38"
      ]
    ]
  ],
  "added": [
    [
      "00bf3d14",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bf3d38"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b77294`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b7724c.md#insn-00b77294) · [`00b772a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b7724c.md#insn-00b772a0) · [`00b772b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b7724c.md#insn-00b772b8)

~~~diff
- 00b77294 ["COPY", "tmp:0:8", ["register:4060:8"]]
- 00b77294 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b77294 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b77294 ["COPY", "register:4058:8", ["tmp:0:8"]]
- 00b77294 bytes 8b018b9a
- 00b772a0 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b772a0 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00b772a0 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b772a0 ["COPY", "tmp:1:8", ["register:4018:8"]]
- 00b772a0 bytes 2631839a
- 00b772b8 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b772b8 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b772b8 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b772b8 ["COPY", "register:4008:8", ["tmp:0:8"]]
- 00b772b8 bytes 4101899a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20635f656a39a23025f5bcef3a9bc221"></a>

### [`00b773f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b773f0.md) → [`00bf3e38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3e38.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE7compareEmmPKwm

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00b75a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75a68.md) [`00be1050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1050.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bf24b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf24b0.md) [`00c5dc40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dc40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.14% / 新版 97.14%

CFGの説明率　旧版 70.00% / 新版 77.78%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b77418"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bf3e60"
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
      "unmatched:00b77418",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bf3ec0"
      ]
    ]
  ],
  "added": [
    [
      "00bf3e60",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bf3ec0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b77418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b773f0.md#insn-00b77418) · [`00b77420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b773f0.md#insn-00b77420)
- 新版 `00bf3e60`（命令位置の公開資料なし） · `00bf3e68`（命令位置の公開資料なし）

~~~diff
- 00b77418 ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
- 00b77418 bytes 00030054
+ 00bf3e60 ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
+ 00bf3e60 bytes 00030054
- 00b77420 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b77420 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00bf3e68 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00bf3e68 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00b77420 bytes c3020054
+ 00bf3e68 bytes c3020054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c6f4237d428e63435f3f03493c096ae4"></a>

### [`00b7747c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b7747c.md) → [`00bf3ec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3ec4.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE7compareEmmPKw

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00b75a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75a68.md) [`00be1010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1010.md) [`00be1050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1050.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bf24b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf24b0.md) [`00c5dc00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dc00.md) [`00c5dc40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dc40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 25.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b774e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bf3f28"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b774e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b7747c.md#insn-00b774e0) · [`00b774a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b7747c.md#insn-00b774a8)
- 新版 `00bf3f28`（命令位置の公開資料なし） · `00bf3ef0`（命令位置の公開資料なし）

~~~diff
- 00b774e0 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b774e0 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b774e0 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b774e0 ["COPY", "tmp:1:8", ["register:4000:8"]]
- 00b774e0 bytes e232809a
+ 00bf3f28 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00bf3f28 ["COPY", "tmp:1:8", ["register:40b8:8"]]
+ 00bf3f28 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
+ 00bf3f28 ["COPY", "tmp:1:8", ["register:4000:8"]]
+ 00bf3f28 bytes e232809a
- 00b774a8 ["INT_ADD", "register:40f0:8", ["const:b774a8:8", "const:4:8"]]
- 00b774a8 ["CALL", null, ["callee:00c5dc00:8"]]
+ 00bf3ef0 ["INT_ADD", "register:40f0:8", ["const:bf3ef0:8", "const:4:8"]]
+ 00bf3ef0 ["CALL", null, ["callee:00c5dc00:8"]]
- 00b774a8 bytes daa60194
+ 00bf3ef0 bytes 44a70194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11207a4de76ebfeed358b2759ecb1739"></a>

### [`00b776a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b776a0.md) → [`00bf40e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf40e8.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE7compareEmmRKS5_mm

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`00be1050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1050.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`00c5dc40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dc40.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 78.26% / 新版 78.26%

CFGの説明率　旧版 33.33% / 新版 44.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b776d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b776d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b776dc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b776e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b7774c"
      ]
    ],
    [
      "00bf414c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b7774c"
      ]
    ],
    [
      "unmatched:00b77750",
      "PARAM",
      [
        "storage",
        "0029f2c1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf412c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bf4194"
      ]
    ],
    [
      "00bf414c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bf4194"
      ]
    ],
    [
      "00bf4198",
      "PARAM",
      [
        "storage",
        "002af6d4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b776d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b776a0.md#insn-00b776d0) · [`00b776d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b776a0.md#insn-00b776d4) · [`00b776dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b776a0.md#insn-00b776dc)

~~~diff
- 00b776d0 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b776d0 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b776d0 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b776d0 ["COPY", "register:4040:8", ["tmp:0:8"]]
- 00b776d0 bytes 48018b9a
- 00b776d4 ["COPY", "tmp:0:8", ["register:4068:8"]]
- 00b776d4 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b776d4 ["COPY", "tmp:0:8", ["register:4060:8"]]
- 00b776d4 ["COPY", "register:4050:8", ["tmp:0:8"]]
- 00b776d4 bytes aa018c9a
- 00b776dc ["COPY", "tmp:0:8", ["register:4078:8"]]
- 00b776dc ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b776dc ["COPY", "tmp:0:8", ["register:4070:8"]]
- 00b776dc ["COPY", "register:4058:8", ["tmp:0:8"]]
- 00b776dc bytes eb018e9a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70722cb4891d36dda6fa03eed775d342"></a>

### [`00b79034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b79034.md) → [`00bf5a7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf5/00bf5a7c.md) _ZNSt6__ndk14stodERKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEEPm

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`00b7b35c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b35c.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb270.md) [`00be1060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1060.md)
- 新版 呼出元 0件  · 呼出先 6件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`00bf7da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf7da4.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cc0.md) [`00c5dc50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dc50.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 69.41% / 新版 69.41%

CFGの説明率　旧版 54.55% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b79104"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b79110"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b79114"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bf5b00",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b7912c"
      ]
    ],
    [
      "unmatched:00b79100",
      "READ",
      [
        "storage",
        "Stack[-0x6f]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b79104",
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
      "00bf5b00",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bf5b74"
      ]
    ],
    [
      "00bf5b48",
      "READ",
      [
        "storage",
        "Stack[-0x6f]",
        null,
        null
      ]
    ],
    [
      "00bf5b4c",
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

- 旧版 [`00b79104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b79034.md#insn-00b79104) · [`00b79110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b79034.md#insn-00b79110) · [`00b79114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b79034.md#insn-00b79114)

~~~diff
- 00b79104 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00b79104 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:18:8"]]
- 00b79104 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b79104 bytes e8630039
- 00b79110 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 00b79110 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b79110 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b79110 bytes ff1700f9
- 00b79114 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00b79114 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:19:8"]]
- 00b79114 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:4"]]
- 00b79114 bytes e99301b8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2701ef2ffe2a84555fb80650347cd0a"></a>

### [`00b79420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b79420.md) → [`00bf5e68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf5/00bf5e68.md) _ZNSt6__ndk19to_stringEl

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdb380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb380.md) · 呼出先 4件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00b7b3e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b3e8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00c57dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57dd0.md) · 呼出先 4件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00bf7e30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf7e30.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 90.37% / 新版 90.37%

CFGの説明率　旧版 87.50% / 新版 91.30%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b795d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bf6020"
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
      "00bf5ed4",
      "DATA",
      [
        "storage",
        "002faa70",
        null,
        null
      ]
    ],
    [
      "00bf5fa8",
      "DATA",
      [
        "storage",
        "002fa9a8",
        null,
        null
      ]
    ],
    [
      "00bf5fb8",
      "DATA",
      [
        "storage",
        "002fa9a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bf5ed4",
      "DATA",
      [
        "storage",
        "003108a8",
        null,
        null
      ]
    ],
    [
      "00bf5fa8",
      "DATA",
      [
        "storage",
        "003107e0",
        null,
        null
      ]
    ],
    [
      "00bf5fb8",
      "DATA",
      [
        "storage",
        "003107e0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b795d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b79420.md#insn-00b795d8) · [`00b79480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b79420.md#insn-00b79480)
- 新版 `00bf6020`（命令位置の公開資料なし） · `00bf5ec8`（命令位置の公開資料なし）

~~~diff
- 00b795d8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b795d8 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b795d8 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b795d8 ["COPY", "register:4040:8", ["tmp:0:8"]]
- 00b795d8 bytes 0801899a
+ 00bf6020 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00bf6020 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
+ 00bf6020 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00bf6020 ["COPY", "register:4040:8", ["tmp:0:8"]]
+ 00bf6020 bytes 0801899a
- 00b79480 ["COPY", "register:4050:8", ["const:2fa000:8"]]
+ 00bf5ec8 ["COPY", "register:4050:8", ["const:310000:8"]]
- 00b79480 bytes 0abcffb0
+ 00bf5ec8 bytes cab8fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de8d1b298283e46d1a280df048fa3972"></a>

### [`00b7963c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b7963c.md) → [`00bf6084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf6/00bf6084.md) _ZNSt6__ndk19to_stringEx

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bddcf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddcf0.md) · 呼出先 4件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00b7b3e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b3e8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00c5a740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a740.md) · 呼出先 4件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00bf7e30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf7e30.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 57.69% / 新版 65.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b79784"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b79794"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b797b0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b796a8",
      "DATA",
      [
        "storage",
        "002faa70",
        null,
        null
      ]
    ],
    [
      "unmatched:00b796ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bf6160"
      ]
    ],
    [
      "unmatched:00b7977c",
      "DATA",
      [
        "storage",
        "002fa9a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bf60f0",
      "DATA",
      [
        "storage",
        "003108a8",
        null,
        null
      ]
    ],
    [
      "00bf6134",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bf6160"
      ]
    ],
    [
      "00bf61c4",
      "DATA",
      [
        "storage",
        "003107e0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b796ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b7963c.md#insn-00b796ec) · [`00b79784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b7963c.md#insn-00b79784) · [`00b79794`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b7963c.md#insn-00b79794)

~~~diff
- 00b796ec ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b796ec ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00b796ec ["CBRANCH", null, ["local:b10:8", "tmp:1:1"]]
- 00b796ec bytes 69010054
- 00b79784 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00b79784 ["COPY", "tmp:1:4", ["register:4040:4"]]
- 00b79784 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:2"]]
- 00b79784 bytes 08000079
- 00b79794 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:2:8"]]
- 00b79794 ["COPY", "tmp:1:4", ["register:4050:4"]]
- 00b79794 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:2"]]
- 00b79794 bytes 0a040079
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f499a8b50773fc4baeb984d0de22e697"></a>

### [`00b7991c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b7991c.md) → [`00bf6364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf6/00bf6364.md) _ZNSt6__ndk19to_stringEm

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdb310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb310.md) · 呼出先 4件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00b7b3e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b3e8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00c57d60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d60.md) · 呼出先 4件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00bf7e30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf7e30.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 73.68% / 新版 73.68%

CFGの説明率　旧版 25.00% / 新版 35.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b79a10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b79a20"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b79a3c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bf639c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b79a4c"
      ]
    ],
    [
      "unmatched:00b79a08",
      "DATA",
      [
        "storage",
        "002fa9a8",
        null,
        null
      ]
    ],
    [
      "unmatched:00b79a18",
      "DATA",
      [
        "storage",
        "002fa9a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bf639c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00bf6494"
      ]
    ],
    [
      "00bf6450",
      "DATA",
      [
        "storage",
        "003107e0",
        null,
        null
      ]
    ],
    [
      "00bf6460",
      "DATA",
      [
        "storage",
        "003107e0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b79a10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b7991c.md#insn-00b79a10) · [`00b79a20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b7991c.md#insn-00b79a20) · [`00b79a3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b7991c.md#insn-00b79a3c)

~~~diff
- 00b79a10 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00b79a10 ["COPY", "tmp:1:4", ["register:4040:4"]]
- 00b79a10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:2"]]
- 00b79a10 bytes 08000079
- 00b79a20 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:2:8"]]
- 00b79a20 ["COPY", "tmp:1:4", ["register:4050:4"]]
- 00b79a20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:2"]]
- 00b79a20 bytes 0a040079
- 00b79a3c ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:6:8"]]
- 00b79a3c ["COPY", "tmp:1:4", ["register:4040:4"]]
- 00b79a3c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:2"]]
- 00b79a3c bytes 080c0079
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b7e8c8462f3c69cd636ecdf2fa2d8c2"></a>

### [`00b79ae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b79ae4.md) → [`00bf652c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf6/00bf652c.md) _ZNSt6__ndk19to_stringEy

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00b7b3e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b3e8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00bf7e30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf7e30.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 80.70% / 新版 80.70%

CFGの説明率　旧版 66.67% / 新版 82.35%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b79bd8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b79be8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b79c04"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b79bd0",
      "DATA",
      [
        "storage",
        "002fa9a8",
        null,
        null
      ]
    ],
    [
      "unmatched:00b79be0",
      "DATA",
      [
        "storage",
        "002fa9a8",
        null,
        null
      ]
    ],
    [
      "unmatched:00b79bec",
      "DATA",
      [
        "storage",
        "002fa9a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bf6618",
      "DATA",
      [
        "storage",
        "003107e0",
        null,
        null
      ]
    ],
    [
      "00bf6628",
      "DATA",
      [
        "storage",
        "003107e0",
        null,
        null
      ]
    ],
    [
      "00bf6634",
      "DATA",
      [
        "storage",
        "003107e0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b79bd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b79ae4.md#insn-00b79bd8) · [`00b79be8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b79ae4.md#insn-00b79be8) · [`00b79c04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b79ae4.md#insn-00b79c04)

~~~diff
- 00b79bd8 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00b79bd8 ["COPY", "tmp:1:4", ["register:4040:4"]]
- 00b79bd8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:2"]]
- 00b79bd8 bytes 08000079
- 00b79be8 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:2:8"]]
- 00b79be8 ["COPY", "tmp:1:4", ["register:4050:4"]]
- 00b79be8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:2"]]
- 00b79be8 bytes 0a040079
- 00b79c04 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:6:8"]]
- 00b79c04 ["COPY", "tmp:1:4", ["register:4040:4"]]
- 00b79c04 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:2"]]
- 00b79c04 bytes 080c0079
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5f06dac986a3a32354674b274070283"></a>

### [`00b79e84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b79e84.md) → [`00bf68cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf6/00bf68cc.md) _ZNSt6__ndk110to_wstringEl

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8a4.md) [`00b7b3e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b3e8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`006d7660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7660.md) [`00bf7e30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf7e30.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 81.56% / 新版 81.56%

CFGの説明率　旧版 73.17% / 新版 83.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b79fcc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b79fdc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b79ff8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bf6938",
      "DATA",
      [
        "storage",
        "002faa70",
        null,
        null
      ]
    ],
    [
      "unmatched:00b79fc4",
      "DATA",
      [
        "storage",
        "002fa9a8",
        null,
        null
      ]
    ],
    [
      "unmatched:00b79fd4",
      "DATA",
      [
        "storage",
        "002fa9a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bf6938",
      "DATA",
      [
        "storage",
        "003108a8",
        null,
        null
      ]
    ],
    [
      "00bf6a0c",
      "DATA",
      [
        "storage",
        "003107e0",
        null,
        null
      ]
    ],
    [
      "00bf6a1c",
      "DATA",
      [
        "storage",
        "003107e0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b79fcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b79e84.md#insn-00b79fcc) · [`00b79fdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b79e84.md#insn-00b79fdc) · [`00b79ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b79e84.md#insn-00b79ff8)

~~~diff
- 00b79fcc ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00b79fcc ["COPY", "tmp:1:4", ["register:4040:4"]]
- 00b79fcc ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:2"]]
- 00b79fcc bytes 08000079
- 00b79fdc ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:2:8"]]
- 00b79fdc ["COPY", "tmp:1:4", ["register:4050:4"]]
- 00b79fdc ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:2"]]
- 00b79fdc bytes 0a040079
- 00b79ff8 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:6:8"]]
- 00b79ff8 ["COPY", "tmp:1:4", ["register:4040:4"]]
- 00b79ff8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:2"]]
- 00b79ff8 bytes 080c0079
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c1802e3f9a14801b9eb9bdfaf2ea13c"></a>

### [`00b7a41c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7a/00b7a41c.md) → [`00bf6e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf6/00bf6e64.md) _ZNSt6__ndk110to_wstringEj

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8a4.md) [`00b7b3e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b3e8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`006d7660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7660.md) [`00bf7e30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf7e30.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 84.95% / 新版 84.95%

CFGの説明率　旧版 57.69% / 新版 68.18%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7a48c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bf6ed4"
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
      "unmatched:00b7a48c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bf6fd4"
      ]
    ],
    [
      "unmatched:00b7a4e0",
      "READ",
      [
        "storage",
        "002b11c0",
        null,
        null
      ]
    ],
    [
      "unmatched:00b7a4e4",
      "READ",
      [
        "storage",
        "002b1a40",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bf6ed4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bf6fd4"
      ]
    ],
    [
      "00bf6f28",
      "READ",
      [
        "storage",
        "002c2800",
        null,
        null
      ]
    ],
    [
      "00bf6f2c",
      "READ",
      [
        "storage",
        "002c3110",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7a48c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7a/00b7a41c.md#insn-00b7a48c) · [`00b7a444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7a/00b7a41c.md#insn-00b7a444)
- 新版 `00bf6ed4`（命令位置の公開資料なし） · `00bf6e8c`（命令位置の公開資料なし）

~~~diff
- 00b7a48c ["CBRANCH", null, ["local:b19:8", "register:102:1"]]
- 00b7a48c bytes 02080054
+ 00bf6ed4 ["CBRANCH", null, ["local:b15:8", "register:102:1"]]
+ 00bf6ed4 bytes 02080054
- 00b7a444 ["INT_ADD", "register:40f0:8", ["const:b7a444:8", "const:4:8"]]
- 00b7a444 ["CALL", null, ["callee:00bf7e30:8"]]
+ 00bf6e8c ["INT_ADD", "register:40f0:8", ["const:bf6e8c:8", "const:4:8"]]
+ 00bf6e8c ["CALL", null, ["callee:00bf7e30:8"]]
- 00b7a444 bytes e9030094
+ 00bf6e8c bytes e9030094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07e48b643dc75a023a39dbaff285e843"></a>

### [`00b7a590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7a/00b7a590.md) → [`00bf6fd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf6/00bf6fd8.md) _ZNSt6__ndk110to_wstringEm

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8a4.md) [`00b7b3e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b3e8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`006d7660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7660.md) [`00bf7e30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf7e30.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 81.65% / 新版 81.65%

CFGの説明率　旧版 41.67% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 4件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7a7b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7a7b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7a7bc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bf70c4",
      "DATA",
      [
        "storage",
        "002fa9a8",
        null,
        null
      ]
    ],
    [
      "00bf70d4",
      "DATA",
      [
        "storage",
        "002fa9a8",
        null,
        null
      ]
    ],
    [
      "00bf70e0",
      "DATA",
      [
        "storage",
        "002fa9a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bf70c4",
      "DATA",
      [
        "storage",
        "003107e0",
        null,
        null
      ]
    ],
    [
      "00bf70d4",
      "DATA",
      [
        "storage",
        "003107e0",
        null,
        null
      ]
    ],
    [
      "00bf70e0",
      "DATA",
      [
        "storage",
        "003107e0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7a6f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7a/00b7a590.md#insn-00b7a6f8) · [`00b7a738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7a/00b7a590.md#insn-00b7a738) · [`00b7a7b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7a/00b7a590.md#insn-00b7a7b8)

~~~diff
- 00b7a6f8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b7a6f8 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b7a6f8 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b7a6f8 ["COPY", "register:4040:8", ["tmp:0:8"]]
- 00b7a6f8 bytes 0801899a
- 00b7a738 ["CBRANCH", null, ["local:b17:8", "register:102:1"]]
- 00b7a738 bytes a2000054
- 00b7a7b8 ["INT_ADD", "tmp:0:8", ["register:4060:8", "const:ffffffffffffffc0:8"]]
- 00b7a7b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5080:16"]]
- 00b7a7b8 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00b7a7b8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5200:16"]]
- 00b7a7b8 bytes 84413ead
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd156418fb6ac057d74e243b49a58181"></a>

### [`00b7a808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7a/00b7a808.md) → [`00bf7250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf7250.md) _ZNSt6__ndk110to_wstringEy

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8a4.md) [`00b7b3e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b3e8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`006d7660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7660.md) [`00bf7e30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf7e30.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 80.38% / 新版 80.38%

CFGの説明率　旧版 55.56% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7aa20"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7aa20"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7aa30"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bf733c",
      "DATA",
      [
        "storage",
        "002fa9a8",
        null,
        null
      ]
    ],
    [
      "00bf734c",
      "DATA",
      [
        "storage",
        "002fa9a8",
        null,
        null
      ]
    ],
    [
      "00bf7358",
      "DATA",
      [
        "storage",
        "002fa9a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bf733c",
      "DATA",
      [
        "storage",
        "003107e0",
        null,
        null
      ]
    ],
    [
      "00bf734c",
      "DATA",
      [
        "storage",
        "003107e0",
        null,
        null
      ]
    ],
    [
      "00bf7358",
      "DATA",
      [
        "storage",
        "003107e0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7aa20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7a/00b7a808.md#insn-00b7aa20) · [`00b7aa30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7a/00b7a808.md#insn-00b7aa30) · [`00b7aa34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7a/00b7a808.md#insn-00b7aa34)

~~~diff
- 00b7aa20 ["INT_ADD", "tmp:0:8", ["register:4060:8", "const:ffffffffffffffe0:8"]]
- 00b7aa20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:50e0:16"]]
- 00b7aa20 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00b7aa20 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:50c0:16"]]
- 00b7aa20 bytes 87193fad
- 00b7aa30 ["INT_ADD", "tmp:0:8", ["register:4060:8", "const:ffffffffffffffc0:8"]]
- 00b7aa30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5080:16"]]
- 00b7aa30 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00b7aa30 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5200:16"]]
- 00b7aa30 bytes 84413ead
- 00b7aa34 ["INT_ADD", "tmp:0:8", ["register:4060:8", "const:20:8"]]
- 00b7aa34 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:50c0:16"]]
- 00b7aa34 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00b7aa34 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5220:16"]]
- 00b7aa34 bytes 864501ad
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89abcbaa233babddd54326da8c47420a"></a>

### [`00b7aa80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7a/00b7aa80.md) → [`00bf74c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf74c8.md) _ZNSt6__ndk19to_stringEf

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdd180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd180.md) · 呼出先 3件 [`00bdefc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefc0.md) [`00be1060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1060.md) [`00be1100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1100.md)
- 新版 呼出元 1件 [`00c59bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59bd0.md) · 呼出先 3件 [`00c5ba70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba70.md) [`00c5dc50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dc50.md) [`00c5dd00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dd00.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 71.43% / 新版 83.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7aae8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7ab14"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bf7530"
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
      "00bf7558",
      "PARAM",
      [
        "storage",
        "002917ad",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bf7558",
      "PARAM",
      [
        "storage",
        "002a0dc6",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7aae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7a/00b7aa80.md#insn-00b7aae8) · [`00b7ab14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7a/00b7aa80.md#insn-00b7ab14)
- 新版 `00bf7530`（命令位置の公開資料なし）

~~~diff
- 00b7aae8 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b7aae8 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b7aae8 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b7aae8 ["COPY", "register:40b8:8", ["tmp:0:8"]]
- 00b7aae8 bytes 5701899a
- 00b7ab14 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b7ab14 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b7ab14 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b7ab14 ["COPY", "register:4000:8", ["tmp:0:8"]]
- 00b7ab14 bytes a002899a
+ 00bf7530 ["COPY", "tmp:0:8", ["register:4050:8"]]
+ 00bf7530 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
+ 00bf7530 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00bf7530 ["COPY", "register:40b8:8", ["tmp:0:8"]]
+ 00bf7530 bytes 5701899a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e6c5cdb294b93821cd0c6e7c56f585a"></a>

### [`00b7b3e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b3e8.md) → [`00bf7e30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf7e30.md) FUN_00bf7e30

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 12件 [`00b792f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b792f8.md) [`00b79420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b79420.md) [`00b7963c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b7963c.md) [`00b79858`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b79858.md) [`00b7991c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b79/00b7991c.md) · 呼出先 0件 
- 新版 呼出元 12件 [`00bf5d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf5/00bf5d40.md) [`00bf5e68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf5/00bf5e68.md) [`00bf6084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf6/00bf6084.md) [`00bf62a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf6/00bf62a0.md) [`00bf6364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf6/00bf6364.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 31.82% / 新版 38.89%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7b4ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7b514"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7b5a0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b7b48c",
      "DATA",
      [
        "storage",
        "002fa9a8",
        null,
        null
      ]
    ],
    [
      "unmatched:00b7b4a8",
      "DATA",
      [
        "storage",
        "002fa9a8",
        null,
        null
      ]
    ],
    [
      "unmatched:00b7b4b4",
      "DATA",
      [
        "storage",
        "002fa9a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bf7ed4",
      "DATA",
      [
        "storage",
        "003107e0",
        null,
        null
      ]
    ],
    [
      "00bf7ef0",
      "DATA",
      [
        "storage",
        "003107e0",
        null,
        null
      ]
    ],
    [
      "00bf7efc",
      "DATA",
      [
        "storage",
        "003107e0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7b4ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b3e8.md#insn-00b7b4ac) · [`00b7b514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b3e8.md#insn-00b7b514) · [`00b7b5a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7b3e8.md#insn-00b7b5a0)

~~~diff
- 00b7b4ac ["COPY", "tmp:0:4", ["register:4050:4"]]
- 00b7b4ac ["INT_ADD", "tmp:1:8", ["register:4000:8", "const:3:8"]]
- 00b7b4ac ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 00b7b4ac bytes 0a300078
- 00b7b514 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 00b7b514 ["INT_ADD", "tmp:1:8", ["register:4000:8", "const:1:8"]]
- 00b7b514 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 00b7b514 bytes 0a100078
- 00b7b5a0 ["COPY", "tmp:0:4", ["register:4058:4"]]
- 00b7b5a0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "const:1:8"]]
- 00b7b5a0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 00b7b5a0 bytes 0b100078
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a90517798fa3abc58a8f730f6593dbae"></a>

### [`00b7d068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d068.md) → [`00bf9ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9ab0.md) _ZNSt6__ndk17promiseIvE13set_exceptionESt13exception_ptr

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`004377fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/004377fc.md) [`00bdb4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4a0.md) [`00bdb510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb510.md) [`00bdb660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb660.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0045a694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a694.md) [`00c57ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ef0.md) [`00c57f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f60.md) [`00c580b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c580b0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 73.68% / 新版 73.68%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7d06c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7d06c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7d070"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b7d06c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b7d070",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b7d098",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb4a0"
      ]
    ]
  ],
  "added": [
    [
      "00bf9ab4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bf9ab8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bf9ae0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57ef0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7d06c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d068.md#insn-00b7d06c) · [`00b7d070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d068.md#insn-00b7d070) · [`00b7d098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d068.md#insn-00b7d098)

~~~diff
- 00b7d06c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b7d06c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b7d06c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b7d06c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b7d06c bytes fd7bbea9
- 00b7d070 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00b7d070 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00b7d070 bytes f30b00f9
- 00b7d098 ["INT_ADD", "register:40f0:8", ["const:b7d098:8", "const:4:8"]]
- 00b7d098 ["CALL", null, ["ram:bdb4a0:8"]]
- 00b7d098 bytes 02790194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-452f97bb2caecf461ad4b3454f6909fa"></a>

### [`00b7d2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d2c0.md) → [`00bf9d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9d08.md) _ZNSt6__ndk15mutex4lockEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdb290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb290.md) · 呼出先 2件 [`00bdb2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2d0.md) [`00bde820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde820.md)
- 新版 呼出元 1件 [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) · 呼出先 2件 [`00c57d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d20.md) [`00c5b2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2a0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 81.82% / 新版 81.82%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7d2e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bf9d30"
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
      "unmatched:00b7d2e4",
      "PARAM",
      [
        "storage",
        "002a1112",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b7d2e8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57d20"
      ]
    ]
  ],
  "added": [
    [
      "00bf9d2c",
      "PARAM",
      [
        "storage",
        "002b175e",
        null,
        "string"
      ]
    ],
    [
      "00bf9d30",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57d20"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7d2e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d2c0.md#insn-00b7d2e8) · [`00b7d2cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d2c0.md#insn-00b7d2cc)
- 新版 `00bf9d30`（命令位置の公開資料なし） · `00bf9d14`（命令位置の公開資料なし）

~~~diff
- 00b7d2e8 ["INT_ADD", "register:40f0:8", ["const:b7d2e8:8", "const:4:8"]]
- 00b7d2e8 ["CALL", null, ["callee:00c57d20:8"]]
- 00b7d2e8 bytes fa770194
+ 00bf9d30 ["INT_ADD", "register:40f0:8", ["const:bf9d30:8", "const:4:8"]]
+ 00bf9d30 ["CALL", null, ["callee:00c57d20:8"]]
+ 00bf9d30 bytes fc770194
- 00b7d2cc ["INT_ADD", "register:40f0:8", ["const:b7d2cc:8", "const:4:8"]]
- 00b7d2cc ["CALL", null, ["callee:00c5b2a0:8"]]
+ 00bf9d14 ["INT_ADD", "register:40f0:8", ["const:bf9d14:8", "const:4:8"]]
+ 00bf9d14 ["CALL", null, ["callee:00c5b2a0:8"]]
- 00b7d2cc bytes 55850194
+ 00bf9d14 bytes 63850194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-052f127bfd6e56862d63339cac079f31"></a>

### [`00b7da8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7da8c.md) → [`00bfa4d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa4d4.md) FUN_00bfa4d4

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b7dd80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7dd80.md) · 呼出先 5件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2a0.md) [`00bdb530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb530.md) [`00be1250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1250.md)
- 新版 呼出元 1件 [`00bfa7c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa7c8.md) · 呼出先 5件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md) [`00c57f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f80.md) [`00c5de50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5de50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 82.35% / 新版 87.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7da90"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7da90"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7da94"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b7da90",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b7da94",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b7da98",
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
      "00bfa4d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bfa4dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bfa4e0",
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

- 旧版 [`00b7da90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7da8c.md#insn-00b7da90) · [`00b7da94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7da8c.md#insn-00b7da94) · [`00b7da98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7da8c.md#insn-00b7da98)

~~~diff
- 00b7da90 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b7da90 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b7da90 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b7da90 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b7da90 bytes fd7bbda9
- 00b7da94 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b7da94 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b7da94 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b7da94 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b7da94 bytes f65701a9
- 00b7da98 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b7da98 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b7da98 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b7da98 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b7da98 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e45654161414296e27118f780dbc1b9f"></a>

### [`00b7dd44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7dd44.md) → [`00bfa78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa78c.md) _ZNSt6__ndk115__thread_structC1Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdb2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2b0.md) · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00c57d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d00.md) · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7dd7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00bfa7c4"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b7dd7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7dd44.md#insn-00b7dd7c) · [`00b7dd5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7dd44.md#insn-00b7dd5c)
- 新版 `00bfa7c4`（命令位置の公開資料なし） · `00bfa7a4`（命令位置の公開資料なし）

~~~diff
- 00b7dd7c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b7dd7c ["RETURN", null, ["register:0:8"]]
- 00b7dd7c bytes c0035fd6
+ 00bfa7c4 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00bfa7c4 ["RETURN", null, ["register:0:8"]]
+ 00bfa7c4 bytes c0035fd6
- 00b7dd5c ["INT_ADD", "register:40f0:8", ["const:b7dd5c:8", "const:4:8"]]
- 00b7dd5c ["CALL", null, ["callee:00c57a90:8"]]
+ 00bfa7a4 ["INT_ADD", "register:40f0:8", ["const:bfa7a4:8", "const:4:8"]]
+ 00bfa7a4 ["CALL", null, ["callee:00c57a90:8"]]
- 00b7dd5c bytes b9740194
+ 00bfa7a4 bytes bb740194
~~~


<a id="compare-705ab3b3c079c96e9054c5e2e2c85d8d"></a>

### [`00b7dd80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7dd80.md) → [`00bfa7c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa7c8.md) _ZNSt6__ndk115__thread_structD1Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdb300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb300.md) · 呼出先 2件 [`00b7da8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7da8c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00c57d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d50.md) · 呼出先 2件 [`00bfa4d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa4d4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 76.47% / 新版 76.47%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7dd84"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7dd84"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7dd88"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b7dd84",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b7dd88",
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
      "00bfa7cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bfa7d0",
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

- 旧版 [`00b7dd84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7dd80.md#insn-00b7dd84) · [`00b7dd88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7dd80.md#insn-00b7dd88)
- 新版 `00bfa7cc`（命令位置の公開資料なし）

~~~diff
- 00b7dd84 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b7dd84 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b7dd84 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b7dd84 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b7dd84 bytes fd7bbea9
- 00b7dd88 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00b7dd88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00b7dd88 bytes f30b00f9
+ 00bfa7cc ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00bfa7cc ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00bfa7cc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00bfa7cc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00bfa7cc bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c5497c1f454fa975d860e62d050ccd6"></a>

### [`00b7dddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7dddc.md) → [`00bfa824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa824.md) FUN_00bfa824

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b7db58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7db58.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00bfa5a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa5a0.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7ddf0"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bfa838"
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
      "unmatched:00b7ddec",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b7ddf0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "00bfa834",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "00bfa838",
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

- 旧版 [`00b7ddf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7dddc.md#insn-00b7ddf0) · [`00b7dde8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7dddc.md#insn-00b7dde8)
- 新版 `00bfa838`（命令位置の公開資料なし） · `00bfa830`（命令位置の公開資料なし）

~~~diff
- 00b7ddf0 ["INT_ADD", "register:40f0:8", ["const:b7ddf0:8", "const:4:8"]]
- 00b7ddf0 ["CALL", null, ["ram:418c38:8"]]
- 00b7ddf0 bytes 926be297
+ 00bfa838 ["INT_ADD", "register:40f0:8", ["const:bfa838:8", "const:4:8"]]
+ 00bfa838 ["CALL", null, ["ram:43b738:8"]]
+ 00bfa838 bytes c003e197
- 00b7dde8 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 00bfa830 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 00b7dde8 bytes 40b9ffd0
+ 00bfa830 bytes e0b5ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7eeeb455a59f4dc726de841ea4f6940e"></a>

### [`00b7ddf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7ddf4.md) → [`00bfa83c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa83c.md) FUN_00bfa83c

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b7dc54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7dc54.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00bfa69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa69c.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "00b7ddf8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7ddf8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bfa840"
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
      "unmatched:00b7ddf8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b7de04",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b7de08",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "00bfa840",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bfa84c",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "00bfa850",
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

- 旧版 [`00b7ddf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7ddf4.md#insn-00b7ddf8) · [`00b7de08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7ddf4.md#insn-00b7de08)
- 新版 `00bfa840`（命令位置の公開資料なし）

~~~diff
- 00b7ddf8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b7ddf8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b7ddf8 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 00b7ddf8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b7ddf8 bytes fd7bbfa9
- 00b7de08 ["INT_ADD", "register:40f0:8", ["const:b7de08:8", "const:4:8"]]
- 00b7de08 ["CALL", null, ["ram:418c38:8"]]
- 00b7de08 bytes 8c6be297
+ 00bfa840 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00bfa840 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00bfa840 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 00bfa840 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00bfa840 bytes fd7bbfa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-349e4fa85c512071af9e9dd0e353396e"></a>

### [`00b7dfa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7dfa0.md) → [`00bfa9e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa9e8.md) _ZNKSt6__ndk113random_device7entropyEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be12b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be12b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5deb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5deb0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 14.29% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7dfdc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bfaa24"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b7dfdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7dfa0.md#insn-00b7dfdc) · [`00b7dfc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7dfa0.md#insn-00b7dfc0)
- 新版 `00bfaa24`（命令位置の公開資料なし） · `00bfaa08`（命令位置の公開資料なし）

~~~diff
- 00b7dfdc ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b7dfdc ["COPY", "tmp:1:4", ["register:4040:4"]]
- 00b7dfdc ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b7dfdc ["COPY", "tmp:1:4", ["register:4048:4"]]
- 00b7dfdc bytes 0831891a
+ 00bfaa24 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00bfaa24 ["COPY", "tmp:1:4", ["register:4040:4"]]
+ 00bfaa24 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
+ 00bfaa24 ["COPY", "tmp:1:4", ["register:4048:4"]]
+ 00bfaa24 bytes 0831891a
- 00b7dfc0 ["INT_ADD", "register:40f0:8", ["const:b7dfc0:8", "const:4:8"]]
- 00b7dfc0 ["CALL", null, ["callee:00c5deb0:8"]]
+ 00bfaa08 ["INT_ADD", "register:40f0:8", ["const:bfaa08:8", "const:4:8"]]
+ 00bfaa08 ["CALL", null, ["callee:00c5deb0:8"]]
- 00b7dfc0 bytes bc8c0194
+ 00bfaa08 bytes 2a8d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-442c24666e42997e0bb3aaa845c088e9"></a>

### [`00b7e07c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e07c.md) → [`00bfaac4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfaac4.md) _ZNSt6__ndk117iostream_categoryEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 45.00% / 新版 45.00%

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
      "site": "00b7e0b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bfab00"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7e0b4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b7e090",
      "READ",
      [
        "storage",
        "010a2088",
        null,
        "undefined1"
      ]
    ],
    [
      "00bfaadc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b7e0ac"
      ]
    ],
    [
      "00bfaae4",
      "DATA",
      [
        "storage",
        "00c24920",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bfaad8",
      "READ",
      [
        "storage",
        "01126f90",
        null,
        "undefined1"
      ]
    ],
    [
      "00bfaadc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bfaaf4"
      ]
    ],
    [
      "00bfaae4",
      "DATA",
      [
        "storage",
        "00ca4400",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7e0a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e07c.md#insn-00b7e0a8) · [`00b7e0b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e07c.md#insn-00b7e0b4) · [`00b7e0b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e07c.md#insn-00b7e0b8)

~~~diff
- 00b7e0a8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b7e0a8 ["RETURN", null, ["register:0:8"]]
- 00b7e0a8 bytes c0035fd6
- 00b7e0b4 ["INT_ADD", "register:40f0:8", ["const:b7e0b4:8", "const:4:8"]]
- 00b7e0b4 ["CALL", null, ["callee:00c57a50:8"]]
- 00b7e0b4 bytes d3730194
- 00b7e0b8 ["INT_EQUAL", "tmp:0:1", ["register:4000:4", "const:0:4"]]
- 00b7e0b8 ["CBRANCH", null, ["local:b1:8", "tmp:0:1"]]
- 00b7e0b8 bytes 00ffff34
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4fd68a7208fb2fe034f47c2d06bc0c1"></a>

### [`00b7e1e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e1e4.md) → [`00bfac2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfac2c.md) _ZNSt6__ndk18ios_base5imbueERKNS_6localeE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd980.md) [`00be12e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be12e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3d0.md) [`00c5dee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dee0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.77% / 新版 96.77%

CFGの説明率　旧版 42.86% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7e1f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e1e4.md#insn-00b7e1f4) · [`00b7e20c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e1e4.md#insn-00b7e20c) · [`00b7e218`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e1e4.md#insn-00b7e218)
- 新版 `00bfac54`（命令位置の公開資料なし） · `00bfac60`（命令位置の公開資料なし）

~~~diff
- 00b7e1f4 ["COPY", "register:40e8:8", ["register:8:8"]]
- 00b7e1f4 bytes fd030091
- 00b7e20c ["INT_ADD", "register:40f0:8", ["const:b7e20c:8", "const:4:8"]]
- 00b7e20c ["CALL", null, ["callee:00c5a3d0:8"]]
+ 00bfac54 ["INT_ADD", "register:40f0:8", ["const:bfac54:8", "const:4:8"]]
+ 00bfac54 ["CALL", null, ["callee:00c5a3d0:8"]]
- 00b7e20c bytes dd7d0194
+ 00bfac54 bytes df7d0194
- 00b7e218 ["INT_ADD", "register:40f0:8", ["const:b7e218:8", "const:4:8"]]
- 00b7e218 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00bfac60 ["INT_ADD", "register:40f0:8", ["const:bfac60:8", "const:4:8"]]
+ 00bfac60 ["CALL", null, ["callee:00c5dee0:8"]]
- 00b7e218 bytes 328c0194
+ 00bfac60 bytes a08c0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d8097c0ec3ff3ad63871429065e2a90"></a>

### [`00b7e2ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e2ac.md) → [`00bfacf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfacf4.md) _ZNSt6__ndk18ios_base5iwordEi

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00b7e6d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e6d4.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bfb11c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb11c.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 66.67% / 新版 76.92%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7e3ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bfadf4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7e3bc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bfade8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b7e3b4"
      ]
    ],
    [
      "unmatched:00b7e3a8",
      "DATA",
      [
        "storage",
        "010a2098",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b7e3ac",
      "WRITE",
      [
        "storage",
        "010a2098",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bfade8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bfadfc"
      ]
    ],
    [
      "00bfadf0",
      "DATA",
      [
        "storage",
        "01126fa0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bfadf4",
      "WRITE",
      [
        "storage",
        "01126fa0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7e3ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e2ac.md#insn-00b7e3ac) · [`00b7e3bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e2ac.md#insn-00b7e3bc)
- 新版 `00bfadf4`（命令位置の公開資料なし）

~~~diff
- 00b7e3ac ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00b7e3ac ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b7e3ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b7e3ac bytes 1f0000f9
- 00b7e3bc ["INT_ADD", "register:40f0:8", ["const:b7e3bc:8", "const:4:8"]]
- 00b7e3bc ["CALL", null, ["callee:00bfb11c:8"]]
- 00b7e3bc bytes c6000094
+ 00bfadf4 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00bfadf4 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bfadf4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bfadf4 bytes 1f0000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-810e4b2a534f7b897b4179091d1dead2"></a>

### [`00b7f358`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f358.md) → [`00bfbda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfbda0.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE6sentryC1ERS3_b

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdcf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf80.md) · 呼出先 5件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdc0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc0a0.md)
- 新版 呼出元 1件 [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md) · 呼出先 5件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c58af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58af0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 95.58% / 新版 95.58%

CFGの説明率　旧版 87.80% / 新版 92.31%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7f3ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7f3f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bfbe34"
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
      "unmatched:00b7f3e8",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b7f3e8",
      "PARAM",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "unmatched:00b7f3ec",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57e80"
      ]
    ]
  ],
  "added": [
    [
      "00bfbe30",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      "00bfbe30",
      "PARAM",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00bfbe34",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57e80"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7f3ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f358.md#insn-00b7f3ec) · [`00b7f3f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f358.md#insn-00b7f3f8)
- 新版 `00bfbe34`（命令位置の公開資料なし）

~~~diff
- 00b7f3ec ["INT_ADD", "register:40f0:8", ["const:b7f3ec:8", "const:4:8"]]
- 00b7f3ec ["CALL", null, ["callee:00c57e80:8"]]
- 00b7f3ec bytes 11700194
- 00b7f3f8 ["INT_ADD", "register:40f0:8", ["const:b7f3f8:8", "const:4:8"]]
- 00b7f3f8 ["CALL", null, ["ram:bdb440:8"]]
- 00b7f3f8 bytes 12700194
+ 00bfbe34 ["INT_ADD", "register:40f0:8", ["const:bfbe34:8", "const:4:8"]]
+ 00bfbe34 ["CALL", null, ["callee:00c57e80:8"]]
+ 00bfbe34 bytes 13700194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e2ed416d0e98d874fb33bdf3b83174f"></a>

### [`00b81230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81230.md) → [`00bfdc78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfdc78.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE4peekEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdcf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 69.77% / 新版 69.77%

CFGの説明率　旧版 7.69% / 新版 12.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b81238"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b81238"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8123c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b81238",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b8123c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b81258",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdcf80"
      ]
    ]
  ],
  "added": [
    [
      "00bfdc80",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bfdc84",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bfdca0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c599d0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b81238`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81230.md#insn-00b81238) · [`00b8123c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81230.md#insn-00b8123c) · [`00b81248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81230.md#insn-00b81248)

~~~diff
- 00b81238 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b81238 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b81238 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b81238 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b81238 bytes fd7b01a9
- 00b8123c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b8123c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b8123c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b8123c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b8123c bytes f44f02a9
- 00b81248 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8:8"]]
- 00b81248 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b81248 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b81248 bytes 1f0400f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b40482b916f200e9347718a827f4deea"></a>

### [`00b81428`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81428.md) → [`00bfde70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfde70.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE8readsomeEPcl

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdcf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 52.94% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b814f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bfdf38"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b814f4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b81458",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdcf80"
      ]
    ],
    [
      "unmatched:00b814e4",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00bfdea0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c599d0"
      ]
    ],
    [
      "00bfdf2c",
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

- 旧版 [`00b81458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81428.md#insn-00b81458) · [`00b814e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81428.md#insn-00b814e4) · [`00b814f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81428.md#insn-00b814f0)

~~~diff
- 00b81458 ["INT_ADD", "register:40f0:8", ["const:b81458:8", "const:4:8"]]
- 00b81458 ["CALL", null, ["ram:bdcf80:8"]]
- 00b81458 bytes ca6e0194
- 00b814e4 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b814e4 ["INT_ADD", "register:40f0:8", ["const:b814e4:8", "const:4:8"]]
- 00b814e4 ["CALLIND", null, ["register:0:8"]]
- 00b814e4 bytes 20013fd6
- 00b814f0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8:8"]]
- 00b814f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b814f0 bytes 600600f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6df9eab760e65d3d7d38415c2811b6b2"></a>

### [`00b819d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b819d4.md) → [`00bfe41c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe41c.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEEC2EPNS_15basic_streambufIcS2_EE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb390.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57de0.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b819d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b819d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b819dc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b819d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b819dc",
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
      "00bfe420",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bfe424",
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

- 旧版 [`00b819d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b819d4.md#insn-00b819d8) · [`00b819dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b819d4.md#insn-00b819dc) · [`00b819e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b819d4.md#insn-00b819e8)

~~~diff
- 00b819d8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b819d8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b819d8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b819d8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b819d8 bytes fd7bbea9
- 00b819dc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00b819dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00b819dc bytes f30b00f9
- 00b819e8 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00b819e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b819e8 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10cef6430a90cacca67c81120e85f6d7"></a>

### [`00b81b04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81b04.md) → [`00bfe54c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe54c.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE6sentryC1ERS3_

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdb410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb410.md) · 呼出先 1件 [`00bdc0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc0a0.md)
- 新版 呼出元 1件 [`00c57e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e60.md) · 呼出先 1件 [`00c58af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58af0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 42.86% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b81b14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81b04.md#insn-00b81b14) · [`00b81b18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81b04.md#insn-00b81b18) · [`00b81b1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81b04.md#insn-00b81b1c)

~~~diff
- 00b81b14 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ffffffffffffffe8:8"]]
- 00b81b14 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b81b14 bytes 08815ef8
- 00b81b18 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b81b18 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00b81b18 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00b81b18 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00b81b18 bytes 2800088b
- 00b81b1c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:20:8"]]
- 00b81b1c ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
- 00b81b1c ["INT_ZEXT", "register:4048:8", ["tmp:1:4"]]
- 00b81b1c bytes 092140b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0f29102c4354086ec3ff52bf38d24a3"></a>

### [`00b825f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b825f4.md) → [`00bff03c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff03c.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE3putEc

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb410.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdb460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb460.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e60.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 86.36% / 新版 86.36%

CFGの説明率　旧版 14.29% / 新版 18.18%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b82634"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bff07c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b82688"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b82634",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bff0bc"
      ]
    ],
    [
      "unmatched:00b82688",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb460"
      ]
    ]
  ],
  "added": [
    [
      "00bff07c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bff0bc"
      ]
    ],
    [
      "00bff0d0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57eb0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b82634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b825f4.md#insn-00b82634) · [`00b82688`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b825f4.md#insn-00b82688)
- 新版 `00bff07c`（命令位置の公開資料なし）

~~~diff
- 00b82634 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00b82634 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00b82634 bytes 000200b4
- 00b82688 ["INT_ADD", "register:40f0:8", ["const:b82688:8", "const:4:8"]]
- 00b82688 ["CALL", null, ["ram:bdb460:8"]]
- 00b82688 bytes 76630194
+ 00bff07c ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00bff07c ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00bff07c bytes 000200b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bad834715b1a4472858dc97a501acfe6"></a>

### [`00b826ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b826ec.md) → [`00bff134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff134.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE5tellpEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b826fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b826ec.md#insn-00b826fc) · [`00b82700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b826ec.md#insn-00b82700) · [`00b82708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b826ec.md#insn-00b82708)
- 新版 `00bff150`（命令位置の公開資料なし）

~~~diff
- 00b826fc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b826fc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b826fc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b826fc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b826fc bytes 0800088b
- 00b82700 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:20:8"]]
- 00b82700 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b82700 ["INT_ZEXT", "register:4048:8", ["tmp:1:1"]]
- 00b82700 bytes 09814039
- 00b82708 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
+ 00bff150 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00b82708 bytes 80000054
+ 00bff150 bytes 80000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4716cb7a330fab155dbe354940d23e04"></a>

### [`00b82a94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82a94.md) → [`00bff4dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff4dc.md) _ZTv0_n24_NSt6__ndk114basic_iostreamIcNS_11char_traitsIcEEED0Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be01e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5cce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cce0.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 71.43% / 新版 71.43%

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
      "site": "00b82a98"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b82a98"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b82a9c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b82a98",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b82a9c",
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
      "00bff4e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bff4e4",
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

- 旧版 [`00b82a98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82a94.md#insn-00b82a98) · [`00b82a9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82a94.md#insn-00b82a9c)
- 新版 `00bff4e0`（命令位置の公開資料なし）

~~~diff
- 00b82a98 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b82a98 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b82a98 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b82a98 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b82a98 bytes fd7bbea9
- 00b82a9c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00b82a9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00b82a9c bytes f30b00f9
+ 00bff4e0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00bff4e0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00bff4e0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00bff4e0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00bff4e0 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d375e4dc7fe8b5de97138bff4f877c82"></a>

### [`00b8506c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b8506c.md) → [`00c01ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01ab4.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE7getlineEPwlw

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be1460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1460.md) · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md)
- 新版 呼出元 1件 [`00c5e060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e060.md) · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 98.26% / 新版 98.26%

CFGの説明率　旧版 90.00% / 新版 92.31%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8515c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00c01ba4"
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
      "unmatched:00b8515c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c01b24"
      ]
    ]
  ],
  "added": [
    [
      "00c01ba4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c01b24"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8515c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b8506c.md#insn-00b8515c) · [`00b850ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b8506c.md#insn-00b850ac)
- 新版 `00c01ba4`（命令位置の公開資料なし） · `00c01af4`（命令位置の公開資料なし）

~~~diff
- 00b8515c ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 00b8515c bytes 00fcff54
+ 00c01ba4 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
+ 00c01ba4 bytes 00fcff54
- 00b850ac ["INT_ADD", "register:40f0:8", ["const:b850ac:8", "const:4:8"]]
- 00b850ac ["CALL", null, ["callee:00c5e020:8"]]
+ 00c01af4 ["INT_ADD", "register:40f0:8", ["const:c01af4:8", "const:4:8"]]
+ 00c01af4 ["CALL", null, ["callee:00c5e020:8"]]
- 00b850ac bytes dd700194
+ 00c01af4 bytes 4b710194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-524c0fcde8a63f1cfd00d354b576c19e"></a>

### [`00b852a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b852a8.md) → [`00c01cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01cf0.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE6ignoreElj

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 72.73% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b85334"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8539c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00c01d7c"
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
      "00c01d60",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b85328"
      ]
    ],
    [
      "00c01dc8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b85390"
      ]
    ],
    [
      "unmatched:00b85334",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00c01d60",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c01d70"
      ]
    ],
    [
      "00c01dc8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c01dd8"
      ]
    ],
    [
      "00c01d7c",
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

- 旧版 [`00b85334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b852a8.md#insn-00b85334) · [`00b8539c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b852a8.md#insn-00b8539c)
- 新版 `00c01d7c`（命令位置の公開資料なし）

~~~diff
- 00b85334 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b85334 ["INT_ADD", "register:40f0:8", ["const:b85334:8", "const:4:8"]]
- 00b85334 ["CALLIND", null, ["register:0:8"]]
- 00b85334 bytes 20013fd6
- 00b8539c ["COPY", "register:0:8", ["register:4048:8"]]
- 00b8539c ["INT_ADD", "register:40f0:8", ["const:b8539c:8", "const:4:8"]]
- 00b8539c ["CALLIND", null, ["register:0:8"]]
- 00b8539c bytes 20013fd6
+ 00c01d7c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00c01d7c ["INT_ADD", "register:40f0:8", ["const:c01d7c:8", "const:4:8"]]
+ 00c01d7c ["CALLIND", null, ["register:0:8"]]
+ 00c01d7c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-acd5972ee48a83589b5ef05a7ae77366"></a>

### [`00b8545c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b8545c.md) → [`00c01ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c01/00c01ea4.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE4peekEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 55.56% / 新版 62.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b854a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00c01ef0"
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
      "unmatched:00b854a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c01f04"
      ]
    ]
  ],
  "added": [
    [
      "00c01ef0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c01f04"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b854a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b8545c.md#insn-00b854a8) · [`00b85484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b8545c.md#insn-00b85484)
- 新版 `00c01ef0`（命令位置の公開資料なし） · `00c01ecc`（命令位置の公開資料なし）

~~~diff
- 00b854a8 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
- 00b854a8 bytes a0000054
+ 00c01ef0 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
+ 00c01ef0 bytes a0000054
- 00b85484 ["INT_ADD", "register:40f0:8", ["const:b85484:8", "const:4:8"]]
- 00b85484 ["CALL", null, ["callee:00c5e020:8"]]
+ 00c01ecc ["INT_ADD", "register:40f0:8", ["const:c01ecc:8", "const:4:8"]]
+ 00c01ecc ["CALL", null, ["callee:00c5e020:8"]]
- 00b85484 bytes e76f0194
+ 00c01ecc bytes 55700194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-155dc23e897836359a181b22b99f42a4"></a>

### [`00b85f18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85f18.md) → [`00c02960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c02/00c02960.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEED0Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be01e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5cce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cce0.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

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
      "site": "00b85f1c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b85f1c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b85f20"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b85f1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b85f20",
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
      "00c02964",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c02968",
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

- 旧版 [`00b85f1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85f18.md#insn-00b85f1c) · [`00b85f20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b85/00b85f18.md#insn-00b85f20)
- 新版 `00c02964`（命令位置の公開資料なし）

~~~diff
- 00b85f1c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b85f1c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b85f1c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b85f1c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b85f1c bytes fd7bbea9
- 00b85f20 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00b85f20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00b85f20 bytes f30b00f9
+ 00c02964 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00c02964 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00c02964 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00c02964 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00c02964 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ab51e242c7bcf58cd0d1b983efff7fd"></a>

### [`00b87c68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b87c68.md) → [`00c046b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c04/00c046b0.md) FUN_00c046b0

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b87bbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b87bbc.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdd980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd980.md) [`00be12e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be12e0.md)
- 新版 呼出元 1件 [`00c04604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c04/00c04604.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5a3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3d0.md) [`00c5dee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dee0.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 97.32% / 新版 97.32%

CFGの説明率　旧版 88.24% / 新版 83.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b87df8"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b87e00"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00c04840"
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
      "unmatched:00b87df8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ],
    [
      "unmatched:00b87e00",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      "00c04840",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57e90"
      ]
    ],
    [
      "00c04848",
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

- 旧版 [`00b87df8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b87c68.md#insn-00b87df8) · [`00b87e00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b87/00b87c68.md#insn-00b87e00)
- 新版 `00c04840`（命令位置の公開資料なし）

~~~diff
- 00b87df8 ["INT_ADD", "register:40f0:8", ["const:b87df8:8", "const:4:8"]]
- 00b87df8 ["CALL", null, ["ram:bdb440:8"]]
- 00b87df8 bytes 924d0194
- 00b87e00 ["INT_ADD", "register:40f0:8", ["const:b87e00:8", "const:4:8"]]
- 00b87e00 ["CALL", null, ["ram:bdb440:8"]]
- 00b87e00 bytes 904d0194
+ 00c04840 ["INT_ADD", "register:40f0:8", ["const:c04840:8", "const:4:8"]]
+ 00c04840 ["CALL", null, ["ram:c57e90:8"]]
+ 00c04840 bytes 944d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-415eec44c3bd5d850013fef4a8d5977e"></a>

### [`00b885f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b885f4.md) → [`00c0503c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c0503c.md) _ZNSt6__ndk114basic_ifstreamIcNS_11char_traitsIcEEE4openERKNS_12basic_stringIcS2_NS_9allocatorIcEEEEj

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00b88f5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88f5c.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdd1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1b0.md) [`00bdd210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd210.md) [`00bdd240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd240.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c059a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c059a4.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c59c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c00.md) [`00c59c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c60.md) [`00c59c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c90.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.87% / 新版 97.87%

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
      "site": "00b8861c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00c05064"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b8861c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b885f4.md#insn-00b8861c) · [`00b88620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b885f4.md#insn-00b88620)
- 新版 `00c05064`（命令位置の公開資料なし） · `00c05068`（命令位置の公開資料なし）

~~~diff
- 00b8861c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b8861c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00b8861c ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b8861c ["INT_ADD", "tmp:1:8", ["register:4008:8", "const:1:8"]]
- 00b8861c bytes 3615819a
+ 00c05064 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00c05064 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00c05064 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
+ 00c05064 ["INT_ADD", "tmp:1:8", ["register:4008:8", "const:1:8"]]
+ 00c05064 bytes 3615819a
- 00b88620 ["INT_EQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
- 00b88620 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00c05068 ["INT_EQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
+ 00c05068 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b88620 bytes 6a0100b4
+ 00c05068 bytes 6a0100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a31baf1cbcf19160970e59ca2487556"></a>

### [`00b88c34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88c34.md) → [`00c0567c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c0567c.md) FUN_00c0567c

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdc0d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc0d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58b20.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 63.64% / 新版 63.64%

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
      "site": "00b88c38"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b88c38"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b88c3c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b88c38",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b88c3c",
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
      "00c05680",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c05684",
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

- 旧版 [`00b88c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88c34.md#insn-00b88c38) · [`00b88c3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88c34.md#insn-00b88c3c)
- 新版 `00c05680`（命令位置の公開資料なし）

~~~diff
- 00b88c38 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b88c38 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b88c38 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b88c38 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b88c38 bytes fd7bbea9
- 00b88c3c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00b88c3c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00b88c3c bytes f30b00f9
+ 00c05680 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00c05680 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00c05680 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00c05680 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00c05680 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ac706f88ae34914d997961a9633d1e9"></a>

### [`00b8a220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a220.md) → [`00c06c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c06c68.md) FUN_00c06c68

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b8a0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a0e0.md) [`00b8a0ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a0ec.md) · 呼出先 4件 [`00be14a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be14a0.md) [`00be14b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be14b0.md) [`00be14c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be14c0.md) [`00be14d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be14d0.md)
- 新版 呼出元 2件 [`00c06b28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c06b28.md) [`00c06b34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c06b34.md) · 呼出先 4件 [`00c5e0a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e0a0.md) [`00c5e0b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e0b0.md) [`00c5e0c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e0c0.md) [`00c5e0d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e0d0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 94.23% / 新版 94.23%

CFGの説明率　旧版 82.61% / 新版 84.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8a234"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8a234"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c06c7c"
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
      "unmatched:00b8a234",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b8a2ec",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00c06c7c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00c06d34",
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

- 旧版 [`00b8a234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a220.md#insn-00b8a234) · [`00b8a2ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a220.md#insn-00b8a2ec)
- 新版 `00c06c7c`（命令位置の公開資料なし）

~~~diff
- 00b8a234 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b8a234 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b8a234 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b8a234 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b8a234 bytes f44f05a9
- 00b8a2ec ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8a2ec ["INT_ADD", "register:40f0:8", ["const:b8a2ec:8", "const:4:8"]]
- 00b8a2ec ["CALLIND", null, ["register:0:8"]]
- 00b8a2ec bytes 00013fd6
+ 00c06c7c ["COPY", "tmp:0:8", ["register:40a0:8"]]
+ 00c06c7c ["COPY", "tmp:1:8", ["register:4098:8"]]
+ 00c06c7c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
+ 00c06c7c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00c06c7c bytes f44f05a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2f036b2df6a5a4ef9ad48373dc74f2d"></a>

### [`00b8a72c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a72c.md) → [`00c07174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c07/00c07174.md) _ZNKSt6__ndk17collateIcE10do_compareEPKcS3_S3_S3_

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 75.00% / 新版 69.23%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8a76c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00c071b4"
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
      "unmatched:00b8a76c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c07188"
      ]
    ]
  ],
  "added": [
    [
      "00c071b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c07188"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8a76c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a72c.md#insn-00b8a76c) · [`00b8a734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a72c.md#insn-00b8a734)
- 新版 `00c071b4`（命令位置の公開資料なし） · `00c0717c`（命令位置の公開資料なし）

~~~diff
- 00b8a76c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b8a76c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b8a76c bytes a1feff54
+ 00c071b4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00c071b4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00c071b4 bytes a1feff54
- 00b8a734 ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
+ 00c0717c ["CBRANCH", null, ["local:b8:8", "register:101:1"]]
- 00b8a734 bytes 00020054
+ 00c0717c bytes 00020054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85d82bf222d4be752ee6518787e761a6"></a>

### [`00b8a8b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a8b8.md) → [`00c07300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c07/00c07300.md) _ZNKSt6__ndk17collateIwE10do_compareEPKwS3_S3_S3_

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 95.45% / 新版 95.45%

CFGの説明率　旧版 25.00% / 新版 27.27%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8a8e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00c07328"
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
      "unmatched:00b8a8e0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c07350"
      ]
    ]
  ],
  "added": [
    [
      "00c07328",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c07350"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8a8e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a8b8.md#insn-00b8a8e0) · [`00b8a8c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8a8b8.md#insn-00b8a8c0)
- 新版 `00c07328`（命令位置の公開資料なし） · `00c07308`（命令位置の公開資料なし）

~~~diff
- 00b8a8e0 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b8a8e0 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00b8a8e0 bytes 43010054
+ 00c07328 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00c07328 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 00c07328 bytes 43010054
- 00b8a8c0 ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
+ 00c07308 ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
- 00b8a8c0 bytes a0010054
+ 00c07308 bytes a0010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd0bc7fec1618636e156c5a7740639e3"></a>

### [`00b8b11c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8b/00b8b11c.md) → [`00c07b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c07/00c07b64.md) FUN_00c07b64

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b8b114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8b/00b8b114.md) · 呼出先 6件 [`00bb92fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb92fc.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdefc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefc0.md) [`00be1520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1520.md) [`00be1530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1530.md)
- 新版 呼出元 1件 [`00c07b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c07/00c07b5c.md) · 呼出先 6件 [`00c35d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35d44.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ba70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba70.md) [`00c5e120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e120.md) [`00c5e130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e130.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 91.63% / 新版 91.63%

CFGの説明率　旧版 55.32% / 新版 52.53%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8b160"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c07ba8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8b1e4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b8b160",
      "WRITE",
      [
        "storage",
        "Stack[-0x180]",
        null,
        null
      ]
    ],
    [
      "00c07c48",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b8b21c"
      ]
    ],
    [
      "unmatched:00b8b20c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c07c80"
      ]
    ]
  ],
  "added": [
    [
      "00c07ba8",
      "WRITE",
      [
        "storage",
        "Stack[-0x180]",
        null,
        null
      ]
    ],
    [
      "00c07c48",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c07c64"
      ]
    ],
    [
      "00c07c54",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c07c80"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8b160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8b/00b8b11c.md#insn-00b8b160) · [`00b8b1e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8b/00b8b11c.md#insn-00b8b1e4) · [`00b8b20c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8b/00b8b11c.md#insn-00b8b20c)

~~~diff
- 00b8b160 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00b8b160 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4028:8"]]
- 00b8b160 bytes e50b00f9
- 00b8b1e4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b8b1e4 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00b8b1e4 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b8b1e4 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "const:1:8"]]
- 00b8b1e4 bytes 3815949a
- 00b8b20c ["CBRANCH", null, ["local:b17:8", "register:101:1"]]
- 00b8b20c bytes 60010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-197515c4a511c68dbaad667f53436a0f"></a>

### [`00b8b558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8b/00b8b558.md) → [`00c07fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c07/00c07fa0.md) FUN_00c07fa0

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b8b550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8b/00b8b550.md) · 呼出先 6件 [`00bb9424`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9424.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdefc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefc0.md) [`00be1520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1520.md) [`00be1530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1530.md)
- 新版 呼出元 1件 [`00c07f98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c07/00c07f98.md) · 呼出先 6件 [`00c35e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35e6c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ba70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba70.md) [`00c5e120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e120.md) [`00c5e130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e130.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 88.05% / 新版 88.05%

CFGの説明率　旧版 50.00% / 新版 48.98%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 13件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8b61c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c08064"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8b620"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b8b61c",
      "WRITE",
      [
        "storage",
        "Stack[-0x168]",
        null,
        null
      ]
    ],
    [
      "00c08084",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b8b658"
      ]
    ],
    [
      "unmatched:00b8b648",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c080bc"
      ]
    ]
  ],
  "added": [
    [
      "00c08064",
      "WRITE",
      [
        "storage",
        "Stack[-0x168]",
        null,
        null
      ]
    ],
    [
      "00c08084",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c080a0"
      ]
    ],
    [
      "00c08090",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c080bc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8b61c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8b/00b8b558.md#insn-00b8b61c) · [`00b8b620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8b/00b8b558.md#insn-00b8b620) · [`00b8b648`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8b/00b8b558.md#insn-00b8b648)

~~~diff
- 00b8b61c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 00b8b61c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 00b8b61c bytes ea1700f9
- 00b8b620 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b8b620 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00b8b620 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b8b620 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "const:1:8"]]
- 00b8b620 bytes 3815949a
- 00b8b648 ["CBRANCH", null, ["local:b17:8", "register:101:1"]]
- 00b8b648 bytes 60010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3a23e5a1fab8372c4ff7cdd317f55d3"></a>

### [`00b8bdd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8b/00b8bdd0.md) → [`00c08818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c08/00c08818.md) FUN_00c08818

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b8bdc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8b/00b8bdc8.md) · 呼出先 6件 [`00bb96a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb96a4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdefc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefc0.md) [`00be1520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1520.md) [`00be1530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1530.md)
- 新版 呼出元 1件 [`00c08810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c08/00c08810.md) · 呼出先 6件 [`00c360ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c360ec.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ba70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba70.md) [`00c5e120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e120.md) [`00c5e130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e130.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 88.84% / 新版 88.84%

CFGの説明率　旧版 74.47% / 新版 70.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8bdd8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8bdd8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8bddc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b8bdd8",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b8bddc",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b8bde0",
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
      "00c08820",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00c08824",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00c08828",
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

- 旧版 [`00b8bdd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8b/00b8bdd0.md#insn-00b8bdd8) · [`00b8bddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8b/00b8bdd0.md#insn-00b8bddc) · [`00b8bde0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8b/00b8bdd0.md#insn-00b8bde0)

~~~diff
- 00b8bdd8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b8bdd8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b8bdd8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:130:8"]]
- 00b8bdd8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b8bdd8 bytes fd7b13a9
- 00b8bddc ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b8bddc ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00b8bddc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:140:8"]]
- 00b8bddc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b8bddc bytes fc6f14a9
- 00b8bde0 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b8bde0 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b8bde0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:150:8"]]
- 00b8bde0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b8bde0 bytes fa6715a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e606c9a6f27696ef386205bb1ca75066"></a>

### [`00b8c648`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8c/00b8c648.md) → [`00c09090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c09/00c09090.md) FUN_00c09090

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b8c640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8c/00b8c640.md) · 呼出先 6件 [`00bb9940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9940.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdefc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefc0.md) [`00be1520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1520.md) [`00be1530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1530.md)
- 新版 呼出元 1件 [`00c09088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c09/00c09088.md) · 呼出先 6件 [`00c36388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36388.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ba70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba70.md) [`00c5e120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e120.md) [`00c5e130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e130.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 88.45% / 新版 88.45%

CFGの説明率　旧版 61.22% / 新版 63.16%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 9件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8c664"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8c664"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8c68c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b8c664",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b8c68c",
      "WRITE",
      [
        "storage",
        "Stack[-0x180]",
        null,
        null
      ]
    ],
    [
      "00c09174",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b8c748"
      ]
    ]
  ],
  "added": [
    [
      "00c090ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00c090d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x180]",
        null,
        null
      ]
    ],
    [
      "00c09174",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c09190"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8c664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8c/00b8c648.md#insn-00b8c664) · [`00b8c68c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8c/00b8c648.md#insn-00b8c68c) · [`00b8c738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8c/00b8c648.md#insn-00b8c738)

~~~diff
- 00b8c664 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b8c664 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b8c664 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:180:8"]]
- 00b8c664 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b8c664 bytes f44f18a9
- 00b8c68c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00b8c68c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4028:8"]]
- 00b8c68c bytes e50b00f9
- 00b8c738 ["CBRANCH", null, ["local:b19:8", "register:101:1"]]
- 00b8c738 bytes 60010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8f7f48f8747500ceaccc22316f68933"></a>

### [`00b8ce9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8c/00b8ce9c.md) → [`00c098e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c09/00c098e4.md) FUN_00c098e4

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b8ce94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8c/00b8ce94.md) · 呼出先 6件 [`00bb9ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9ba0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdefc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefc0.md) [`00be1540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1540.md) [`00be1550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1550.md)
- 新版 呼出元 1件 [`00c098dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c09/00c098dc.md) · 呼出先 6件 [`00c365e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c365e8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ba70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba70.md) [`00c5e140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e140.md) [`00c5e150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e150.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 91.74% / 新版 91.74%

CFGの説明率　旧版 65.52% / 新版 66.28%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8cf5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8cf64"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8cf70"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c09998",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b8cf6c"
      ]
    ],
    [
      "unmatched:00b8cf5c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c099d0"
      ]
    ],
    [
      "unmatched:00b8cf64",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c099bc"
      ]
    ]
  ],
  "added": [
    [
      "00c09998",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c099b4"
      ]
    ],
    [
      "00c099a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c099d0"
      ]
    ],
    [
      "00c099ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c099bc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8cf5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8c/00b8ce9c.md#insn-00b8cf5c) · [`00b8cf64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8c/00b8ce9c.md#insn-00b8cf64) · [`00b8cf70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8c/00b8ce9c.md#insn-00b8cf70)

~~~diff
- 00b8cf5c ["CBRANCH", null, ["local:b10:8", "register:101:1"]]
- 00b8cf5c bytes 60010054
- 00b8cf64 ["INT_NOTEQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
- 00b8cf64 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00b8cf64 bytes 950000b5
- 00b8cf70 ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
- 00b8cf70 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 00b8cf70 bytes d50100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12c9cd4aac88c1d01cb45e62738bb0ac"></a>

### [`00b8dbf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8d/00b8dbf8.md) → [`00c0a640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0a640.md) _ZNSt6__ndk19__num_getIcE17__stage2_int_loopEciPcRS2_RjcRKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPjRSD_S2_

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be1530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1530.md) · 呼出先 1件 [`00bdb180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb180.md)
- 新版 呼出元 1件 [`00c5e130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e130.md) · 呼出先 1件 [`00c57bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bd0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 91.96% / 新版 91.96%

CFGの説明率　旧版 65.85% / 新版 69.23%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8dda0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8ddac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8ddb0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c0a780",
      "READ",
      [
        "storage",
        "00c1bd90",
        null,
        "pointer"
      ]
    ],
    [
      "00c0a784",
      "DATA",
      [
        "storage",
        "002fb026",
        "_ZNSt6__ndk114__num_get_base5__srcE",
        "string"
      ]
    ],
    [
      "unmatched:00b8dd9c",
      "READ",
      [
        "storage",
        "00c1bd90",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c0a780",
      "READ",
      [
        "storage",
        "00c9b7c0",
        null,
        "pointer"
      ]
    ],
    [
      "00c0a784",
      "DATA",
      [
        "storage",
        "00310e5e",
        "_ZNSt6__ndk114__num_get_base5__srcE",
        "string"
      ]
    ],
    [
      "00c0a7e4",
      "READ",
      [
        "storage",
        "00c9b7c0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8dda0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8d/00b8dbf8.md#insn-00b8dda0) · [`00b8ddac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8d/00b8dbf8.md#insn-00b8ddac) · [`00b8ddb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8d/00b8dbf8.md#insn-00b8ddb0)

~~~diff
- 00b8dda0 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b8dda0 ["COPY", "tmp:1:4", ["const:0:4"]]
- 00b8dda0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:4"]]
- 00b8dda0 bytes 3f0100b9
- 00b8ddac ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b8ddac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00b8ddac bytes 490100f9
- 00b8ddb0 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00b8ddb0 ["COPY", "tmp:1:8", ["register:40a0:8"]]
- 00b8ddb0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b8ddb0 bytes 88020039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1df84c13b2663e176950d7bba5168fdb"></a>

### [`00b91060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b91/00b91060.md) → [`00c0daa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0d/00c0daa8.md) _ZNSt6__ndk19__num_getIwE17__stage2_int_loopEwiPcRS2_RjwRKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPjRSD_Pw

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be15b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be15b0.md) · 呼出先 1件 [`00bdb600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb600.md)
- 新版 呼出元 1件 [`00c5e1a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e1a0.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58050.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 89.19% / 新版 89.19%

CFGの説明率　旧版 61.90% / 新版 63.41%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b91204"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b91210"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b91214"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b91134",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c0dad0"
      ]
    ],
    [
      "00c0dbe0",
      "READ",
      [
        "storage",
        "00c1bd90",
        null,
        "pointer"
      ]
    ],
    [
      "00c0dbe8",
      "DATA",
      [
        "storage",
        "002fb026",
        "_ZNSt6__ndk114__num_get_base5__srcE",
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c0db7c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c0dad0"
      ]
    ],
    [
      "00c0dbe0",
      "READ",
      [
        "storage",
        "00c9b7c0",
        null,
        "pointer"
      ]
    ],
    [
      "00c0dbe8",
      "DATA",
      [
        "storage",
        "00310e5e",
        "_ZNSt6__ndk114__num_get_base5__srcE",
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b91098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b91/00b91060.md#insn-00b91098) · [`00b91110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b91/00b91060.md#insn-00b91110) · [`00b91134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b91/00b91060.md#insn-00b91134)

~~~diff
- 00b91098 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b91098 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b91098 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b91098 ["COPY", "register:4040:8", ["tmp:0:8"]]
- 00b91098 bytes 4801899a
- 00b91110 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b91110 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b91110 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00b91110 ["COPY", "register:4040:8", ["tmp:0:8"]]
- 00b91110 bytes 0803809a
- 00b91134 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b91134 ["CBRANCH", null, ["local:b1:8", "tmp:0:1"]]
- 00b91134 bytes a1faff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a339d9d73a59dcf683c02ede9f44dad6"></a>

### [`00b925c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b92/00b925c8.md) → [`00c0f010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0f010.md) _ZNKSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE6do_putES4_RNS_8ios_baseEcy

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b925d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b92/00b925d8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c0f020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0f020.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b925d0",
      "PARAM",
      [
        "storage",
        "0029c262",
        null,
        null
      ]
    ],
    [
      "unmatched:00b925d4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c0f020"
      ]
    ]
  ],
  "added": [
    [
      "00c0f018",
      "PARAM",
      [
        "storage",
        "002ac488",
        null,
        null
      ]
    ],
    [
      "00c0f01c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c0f020"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b925cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b92/00b925c8.md#insn-00b925cc) · [`00b925d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b92/00b925c8.md#insn-00b925d0) · [`00b925d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b92/00b925c8.md#insn-00b925d4)

~~~diff
- 00b925cc ["COPY", "register:4028:8", ["const:29c000:8"]]
- 00b925cc bytes 45b8ffd0
- 00b925d0 ["COPY", "tmp:0:8", ["const:262:8"]]
- 00b925d0 ["INT_CARRY", "register:105:1", ["register:4028:8", "tmp:0:8"]]
- 00b925d0 ["INT_SCARRY", "register:106:1", ["register:4028:8", "tmp:0:8"]]
- 00b925d0 ["INT_ADD", "tmp:1:8", ["register:4028:8", "tmp:0:8"]]
- 00b925d0 bytes a5880991
- 00b925d4 ["BRANCH", null, ["callee:00c0f020:8"]]
- 00b925d4 bytes 01000014
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb6f5662657445df3e05be28a47f1bcb"></a>

### [`00b93334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93334.md) → [`00c0fd7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0fd7c.md) FUN_00c0fd7c

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 14件 [`00b91f10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b91/00b91f10.md) [`00b9215c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b92/00b9215c.md) [`00b923a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b92/00b923a8.md) [`00b925d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b92/00b925d8.md) [`00b92808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b92/00b92808.md) · 呼出先 2件 [`00bde2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2d0.md) [`00be1580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1580.md)
- 新版 呼出元 14件 [`00c0e958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0e958.md) [`00c0eba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0eba4.md) [`00c0edf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0edf0.md) [`00c0f020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0f020.md) [`00c0f250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0f250.md) · 呼出先 2件 [`00c5ad50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad50.md) [`00c5e170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e170.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 97.87% / 新版 97.87%

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
      "site": "00b933ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00c0fe34"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b933ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93334.md#insn-00b933ec) · [`00b9339c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93334.md#insn-00b9339c)
- 新版 `00c0fe34`（命令位置の公開資料なし） · `00c0fde4`（命令位置の公開資料なし）

~~~diff
- 00b933ec ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b933ec ["RETURN", null, ["register:0:8"]]
- 00b933ec bytes c0035fd6
+ 00c0fe34 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00c0fe34 ["RETURN", null, ["register:0:8"]]
+ 00c0fe34 bytes c0035fd6
- 00b9339c ["INT_ADD", "register:40f0:8", ["const:b9339c:8", "const:4:8"]]
- 00b9339c ["CALL", null, ["callee:00c5e170:8"]]
+ 00c0fde4 ["INT_ADD", "register:40f0:8", ["const:c0fde4:8", "const:4:8"]]
+ 00c0fde4 ["CALL", null, ["callee:00c5e170:8"]]
- 00b9339c bytes 79380194
+ 00c0fde4 bytes e3380194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fea8c9f488b0b0aa47f0934602877592"></a>

### [`00b94a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b94/00b94a74.md) → [`00c114bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c11/00c114bc.md) FUN_00c114bc

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 9件 [`00b93644`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93644.md) [`00b93890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93890.md) [`00b93adc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93adc.md) [`00b93d0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93d0c.md) [`00b93f3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93f3c.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8a4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 9件 [`00c1008c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c1008c.md) [`00c102d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c102d8.md) [`00c10524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c10524.md) [`00c10754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c10754.md) [`00c10984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c10984.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`006d7660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7660.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 95.87% / 新版 95.87%

CFGの説明率　旧版 83.78% / 新版 79.49%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b94bf8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00c11640"
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
      "unmatched:00b94bf8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c11664"
      ]
    ]
  ],
  "added": [
    [
      "00c11640",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c11664"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b94bf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b94/00b94a74.md#insn-00b94bf8) · [`00b94a98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b94/00b94a74.md#insn-00b94a98)
- 新版 `00c11640`（命令位置の公開資料なし） · `00c114e0`（命令位置の公開資料なし）

~~~diff
- 00b94bf8 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00b94bf8 ["CBRANCH", null, ["local:b19:8", "tmp:0:1"]]
- 00b94bf8 bytes 2b010054
+ 00c11640 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 00c11640 ["CBRANCH", null, ["local:b21:8", "tmp:0:1"]]
+ 00c11640 bytes 2b010054
- 00b94a98 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00b94a98 ["CBRANCH", null, ["local:b21:8", "tmp:0:1"]]
+ 00c114e0 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00c114e0 ["CBRANCH", null, ["local:b23:8", "tmp:0:1"]]
- 00b94a98 bytes 800c00b4
+ 00c114e0 bytes 800c00b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2fd2756ac89fc4344dc60e7bcc7703a2"></a>

### [`00b9657c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b9657c.md) → [`00c12fc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c12/00c12fc4.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE11do_get_dateES4_S4_RNS_8ios_baseERjP2tm

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdd920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd920.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5a370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a370.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 82.86% / 新版 82.86%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b965e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b965e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00c1302c"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b965e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b9657c.md#insn-00b965e4) · [`00b965e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b9657c.md#insn-00b965e8)
- 新版 `00c1302c`（命令位置の公開資料なし）

~~~diff
- 00b965e4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b965e4 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00b965e4 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b965e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:1:8"]]
- 00b965e4 bytes 4615889a
- 00b965e8 ["COPY", "tmp:0:8", ["register:4060:8"]]
- 00b965e8 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b965e8 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b965e8 ["COPY", "register:4040:8", ["tmp:0:8"]]
- 00b965e8 bytes 88018b9a
+ 00c1302c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00c1302c ["COPY", "tmp:1:8", ["register:4050:8"]]
+ 00c1302c ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
+ 00c1302c ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:1:8"]]
+ 00c1302c bytes 4615889a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7369940c5c9ca5f7a9b88fd710a8df4"></a>

### [`00b96760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b96760.md) → [`00c131a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c131a8.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE17__get_weekdaynameERiRS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b8aca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8a/00b8aca8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c076f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c07/00c076f0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.87% / 新版 97.87%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b96794`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b96760.md#insn-00b96794) · [`00b967b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b96760.md#insn-00b967b8) · [`00b967c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b96/00b96760.md#insn-00b967c4)
- 新版 `00c131dc`（命令位置の公開資料なし） · `00c13200`（命令位置の公開資料なし） · `00c1320c`（命令位置の公開資料なし）

~~~diff
- 00b96794 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b96794 ["INT_ADD", "register:40f0:8", ["const:b96794:8", "const:4:8"]]
- 00b96794 ["CALLIND", null, ["register:0:8"]]
+ 00c131dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c131dc ["INT_ADD", "register:40f0:8", ["const:c131dc:8", "const:4:8"]]
+ 00c131dc ["CALLIND", null, ["register:0:8"]]
- 00b96794 bytes 00013fd6
+ 00c131dc bytes 00013fd6
- 00b967b8 ["INT_ADD", "register:40f0:8", ["const:b967b8:8", "const:4:8"]]
- 00b967b8 ["CALL", null, ["callee:00c076f0:8"]]
+ 00c13200 ["INT_ADD", "register:40f0:8", ["const:c13200:8", "const:4:8"]]
+ 00c13200 ["CALL", null, ["callee:00c076f0:8"]]
- 00b967b8 bytes 3cd1ff97
+ 00c13200 bytes 3cd1ff97
- 00b967c4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b967c4 ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
- 00b967c4 ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
- 00b967c4 ["CBRANCH", null, ["local:b2:8", "tmp:2:1"]]
+ 00c1320c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00c1320c ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
+ 00c1320c ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
+ 00c1320c ["CBRANCH", null, ["local:b4:8", "tmp:2:1"]]
- 00b967c4 bytes 0c020054
+ 00c1320c bytes 0c020054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66716c09c8cff1bc3d4d27640fe1ff36"></a>

### [`00b97470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97470.md) → [`00c13eb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c13eb8.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE17__get_white_spaceERS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be1620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1620.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5e210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e210.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 92.62% / 新版 92.62%

CFGの説明率　旧版 65.67% / 新版 61.97%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b97480"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b97480"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c13ec8"
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
      "unmatched:00b97480",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b975c4",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00c14034"
      ]
    ],
    [
      "00c14050",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b97634"
      ]
    ]
  ],
  "added": [
    [
      "00c13ec8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00c1400c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00c14034"
      ]
    ],
    [
      "00c14050",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c1407c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b97480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97470.md#insn-00b97480) · [`00b97568`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97470.md#insn-00b97568) · [`00b97630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97470.md#insn-00b97630)

~~~diff
- 00b97480 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b97480 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b97480 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b97480 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b97480 bytes f44f03a9
- 00b97568 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b97568 ["INT_ADD", "register:40f0:8", ["const:b97568:8", "const:4:8"]]
- 00b97568 ["CALLIND", null, ["register:0:8"]]
- 00b97568 bytes 00013fd6
- 00b97630 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b97630 ["RETURN", null, ["register:0:8"]]
- 00b97630 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-971666597bfa53985ed7d97161e196f5"></a>

### [`00b97850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97850.md) → [`00c14298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c14298.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE13__get_percentERS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be1630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1630.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5e220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e220.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 92.68% / 新版 92.68%

CFGの説明率　旧版 58.33% / 新版 53.03%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b97860"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b97860"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c142a8"
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
      "unmatched:00b97860",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b97948",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ],
    [
      "unmatched:00b979ec",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00c142a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00c14390",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ],
    [
      "00c14434",
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

- 旧版 [`00b97860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97850.md#insn-00b97860) · [`00b97948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97850.md#insn-00b97948) · [`00b979ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97850.md#insn-00b979ec)

~~~diff
- 00b97860 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b97860 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b97860 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b97860 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b97860 bytes f44f03a9
- 00b97948 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b97948 ["INT_ADD", "register:40f0:8", ["const:b97948:8", "const:4:8"]]
- 00b97948 ["CALLIND", null, ["register:0:8"]]
- 00b97948 bytes 00013fd6
- 00b979ec ["COPY", "register:0:8", ["register:4040:8"]]
- 00b979ec ["INT_ADD", "register:40f0:8", ["const:b979ec:8", "const:4:8"]]
- 00b979ec ["CALLIND", null, ["register:0:8"]]
- 00b979ec bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7f8c1cb15e4609ba1d941bcc70c7f9f"></a>

### [`00b984a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b984a8.md) → [`00c14ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c14ef0.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE17__get_weekdaynameERiRS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b8e180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8e/00b8e180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c0abc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0abc8.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 80.85% / 新版 80.85%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b984ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b984ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b984b0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b984ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b984b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b984b4",
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
      "00c14ef4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00c14ef8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00c14efc",
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

- 旧版 [`00b984ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b984a8.md#insn-00b984ac) · [`00b984b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b984a8.md#insn-00b984b0) · [`00b984b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b984a8.md#insn-00b984b4)

~~~diff
- 00b984ac ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b984ac ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b984ac ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00b984ac ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b984ac bytes fd7bbca9
- 00b984b0 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b984b0 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b984b0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b984b0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b984b0 bytes f85f01a9
- 00b984b4 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b984b4 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b984b4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b984b4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b984b4 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b61c408a67f435cd572d76da2d0291f"></a>

### [`00b99148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99148.md) → [`00c15b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c15/00c15b90.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE12__get_minuteERiRS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b99780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99780.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c161c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c161c8.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 66.67% / 新版 57.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9914c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9914c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b99150"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b9914c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b99150",
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
      "00c15b94",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c15b98",
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

- 旧版 [`00b9914c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99148.md#insn-00b9914c) · [`00b99150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99148.md#insn-00b99150)
- 新版 `00c15b94`（命令位置の公開資料なし）

~~~diff
- 00b9914c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b9914c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b9914c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b9914c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b9914c bytes fd7bbea9
- 00b99150 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b99150 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b99150 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b99150 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b99150 bytes f44f01a9
+ 00c15b94 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00c15b94 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00c15b94 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00c15b94 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00c15b94 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c010709aa3b6e838474f1b7195cab7a"></a>

### [`00b991a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b991a8.md) → [`00c15bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c15/00c15bf0.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE17__get_white_spaceERS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be1650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1650.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5e240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e240.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 94.35% / 新版 94.35%

CFGの説明率　旧版 59.32% / 新版 55.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b991b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b991b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c15c00"
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
      "unmatched:00b991b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b99260",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ],
    [
      "unmatched:00b992dc",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00c15c00",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00c15ca8",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ],
    [
      "00c15d24",
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

- 旧版 [`00b991b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b991a8.md#insn-00b991b8) · [`00b99260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b991a8.md#insn-00b99260) · [`00b992dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b991a8.md#insn-00b992dc)

~~~diff
- 00b991b8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b991b8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b991b8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b991b8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b991b8 bytes f44f03a9
- 00b99260 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b99260 ["INT_ADD", "register:40f0:8", ["const:b99260:8", "const:4:8"]]
- 00b99260 ["CALLIND", null, ["register:0:8"]]
- 00b99260 bytes 00013fd6
- 00b992dc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b992dc ["INT_ADD", "register:40f0:8", ["const:b992dc:8", "const:4:8"]]
- 00b992dc ["CALLIND", null, ["register:0:8"]]
- 00b992dc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b25f03efe8eddfbb894dcd2d19a6920a"></a>

### [`00b99398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99398.md) → [`00c15de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c15/00c15de0.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE11__get_am_pmERiRS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b8e180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b8e/00b8e180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c0abc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0abc8.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 87.93% / 新版 87.93%

CFGの説明率　旧版 69.23% / 新版 56.25%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9939c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9939c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b993a0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b9939c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b993a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b993a4",
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
      "00c15de4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00c15de8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00c15dec",
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

- 旧版 [`00b9939c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99398.md#insn-00b9939c) · [`00b993a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99398.md#insn-00b993a0) · [`00b993a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99398.md#insn-00b993a4)

~~~diff
- 00b9939c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b9939c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b9939c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00b9939c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b9939c bytes fd7bbca9
- 00b993a0 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b993a0 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b993a0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b993a0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b993a0 bytes f85f01a9
- 00b993a4 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b993a4 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b993a4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b993a4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b993a4 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

