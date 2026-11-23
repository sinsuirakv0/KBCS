# v15.7.4 → v16.0.0 · 命令位置の検査未完了 (16)

[一覧の目次](README.md)

<a id="compare-c5771d77ba05dfba367b140de0d1d48d"></a>

### [`00b05b64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05b64.md) → [`00b657bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b657bc.md) _ZN8firebase15options_builder10GetFieldIdENS0_5FieldE

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 46.67% / 新版 46.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b05b84"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b657dc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b05b9c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b657d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b05b88"
      ]
    ],
    [
      "unmatched:00b05b80",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b05b84",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ac00"
      ]
    ]
  ],
  "added": [
    [
      "00b657d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b657e0"
      ]
    ],
    [
      "00b657d8",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b657dc",
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

- 旧版 [`00b05b84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05b64.md#insn-00b05b84) · [`00b05b9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05b64.md#insn-00b05b9c)
- 新版 [`00b657dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b657bc.md#insn-00b657dc)

~~~diff
- 00b05b84 ["INT_ADD", "register:40f0:8", ["const:b05b84:8", "const:4:8"]]
- 00b05b84 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b05b84 bytes 7f610394
- 00b05b9c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b05b9c ["RETURN", null, ["register:0:8"]]
- 00b05b9c bytes c0035fd6
+ 00b657dc ["INT_ADD", "register:40f0:8", ["const:b657dc:8", "const:4:8"]]
+ 00b657dc ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b657dc bytes 09d50394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e95435a96b5787e1d09ef53d85ca500"></a>

### [`00b08210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b08/00b08210.md) → [`00b67e68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b67/00b67e68.md) _ZNK8firebase10AppOptionseqERKS0_

採用 · 移動量 `+0x5fc58` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf030.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`00c5bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bae0.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 78.82% / 新版 78.82%

CFGの説明率　旧版 43.62% / 新版 43.39%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 23件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b08340"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b08350"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b08358"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b67f80",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b08358"
      ]
    ],
    [
      "unmatched:00b08340",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6838c"
      ]
    ],
    [
      "unmatched:00b08350",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b08334"
      ]
    ]
  ],
  "added": [
    [
      "00b67f80",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b67fb0"
      ]
    ],
    [
      "00b67f98",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6838c"
      ]
    ],
    [
      "00b67fa8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b67f8c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b08340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b08/00b08210.md#insn-00b08340) · [`00b08350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b08/00b08210.md#insn-00b08350) · [`00b08358`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b08/00b08210.md#insn-00b08358)

~~~diff
- 00b08340 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b08340 ["CBRANCH", null, ["local:b105:8", "tmp:0:1"]]
- 00b08340 bytes a11f0054
- 00b08350 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b08350 ["CBRANCH", null, ["local:b22:8", "tmp:0:1"]]
- 00b08350 bytes 21ffff54
- 00b08358 ["INT_EQUAL", "tmp:0:1", ["register:4010:8", "const:0:8"]]
- 00b08358 ["CBRANCH", null, ["local:b27:8", "tmp:0:1"]]
- 00b08358 bytes 620000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30f99a0775207665f65292b76a82b053"></a>

### [`00b0d27c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d27c.md) → [`00b6d598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d598.md) _ZN11flatbuffers10DefinitionD2Ev

採用 · 移動量 `+0x6031c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9f0.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdeba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeba0.md)
- 新版 呼出元 1件 [`00c5b470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b470.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5b650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b650.md)

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 94.20% / 新版 94.20%

CFGの説明率　旧版 78.38% / 新版 78.38%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0d2bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0d2c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b6d5d8"
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
      "unmatched:00b0d2bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d668"
      ]
    ],
    [
      "unmatched:00b0d2c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d65c"
      ]
    ]
  ],
  "added": [
    [
      "00b6d5d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d668"
      ]
    ],
    [
      "00b6d5e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d65c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0d2bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d27c.md#insn-00b0d2bc) · [`00b0d2c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d27c.md#insn-00b0d2c8)
- 新版 [`00b6d5d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d598.md#insn-00b6d5d8)

~~~diff
- 00b0d2bc ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 00b0d2bc ["CBRANCH", null, ["local:b20:8", "tmp:0:1"]]
- 00b0d2bc bytes 940400b4
- 00b0d2c8 ["CBRANCH", null, ["local:b18:8", "register:101:1"]]
- 00b0d2c8 bytes c0030054
+ 00b6d5d8 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
+ 00b6d5d8 ["CBRANCH", null, ["local:b20:8", "tmp:0:1"]]
+ 00b6d5d8 bytes 940400b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45cf6694b4c8997385f0c8bf32becf53"></a>

### [`00b0d734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d734.md) → [`00b6da68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6da68.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers4TypeEEENS_19__map_value_comp

採用 · 移動量 `+0x60334` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdeb90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeb90.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdeb90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeb90.md)
- 新版 呼出元 1件 [`00c5b640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b640.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5b640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b640.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 40.00% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0d738"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0d738"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0d73c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b0d738",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b0d73c",
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
      "00b6da6c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b6da70",
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

- 旧版 [`00b0d738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d734.md#insn-00b0d738) · [`00b0d73c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d734.md#insn-00b0d73c)
- 新版 [`00b6da6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6da68.md#insn-00b6da6c)

~~~diff
- 00b0d738 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b0d738 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b0d738 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b0d738 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b0d738 bytes f44fbea9
- 00b0d73c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b0d73c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b0d73c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b0d73c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b0d73c bytes fd7b01a9
+ 00b6da6c ["COPY", "tmp:0:8", ["register:40a0:8"]]
+ 00b6da6c ["COPY", "tmp:1:8", ["register:4098:8"]]
+ 00b6da6c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00b6da6c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00b6da6c bytes f44fbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa03f8eae01e9a1c639828f971eadcb5"></a>

### [`00b0e304`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0e304.md) → [`00b6e638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6e638.md) _ZN11flatbuffers19FLATBUFFERS_VERSIONEv

採用 · 移動量 `+0x60334` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0e30c"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b6e640"
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
      "unmatched:00b0e308",
      "DATA",
      [
        "storage",
        "002aa01e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6e63c",
      "DATA",
      [
        "storage",
        "002bbe34",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0e30c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0e304.md#insn-00b0e30c) · [`00b0e304`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0e304.md#insn-00b0e304)
- 新版 [`00b6e640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6e638.md#insn-00b6e640)

~~~diff
- 00b0e30c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b0e30c ["RETURN", null, ["register:0:8"]]
- 00b0e30c bytes c0035fd6
+ 00b6e640 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b6e640 ["RETURN", null, ["register:0:8"]]
+ 00b6e640 bytes c0035fd6
- 00b0e304 ["COPY", "register:4000:8", ["const:2aa000:8"]]
- 00b0e304 bytes e0bcff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61808cdad1c8f9b98d395822a08a50cb"></a>

### [`00b10c0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b10/00b10c0c.md) → [`00b70ad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b70/00b70ad4.md) _ZN11flatbuffers6ToUTF8EjPNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x5fec8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdfa50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfa50.md) · 呼出先 1件 [`00bdda90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda90.md)
- 新版 呼出元 1件 [`00c5c3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c3f0.md) · 呼出先 1件 [`00c5a4e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4e0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 95.28% / 新版 95.28%

CFGの説明率　旧版 87.50% / 新版 80.77%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b10c1c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b10c1c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b70ae4"
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
      "unmatched:00b10c1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b10c30",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b70b08"
      ]
    ]
  ],
  "added": [
    [
      "00b70ae4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b70af8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b70b08"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b10c1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b10/00b10c0c.md#insn-00b10c1c) · [`00b10c30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b10/00b10c0c.md#insn-00b10c30)
- 新版 [`00b70ae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b70/00b70ad4.md#insn-00b70ae4)

~~~diff
- 00b10c1c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b10c1c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b10c1c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b10c1c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b10c1c bytes fd7b04a9
- 00b10c30 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b10c30 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00b10c30 ["CBRANCH", null, ["local:b2:8", "tmp:1:1"]]
- 00b10c30 bytes 88000054
+ 00b70ae4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00b70ae4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00b70ae4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
+ 00b70ae4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00b70ae4 bytes fd7b04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b4168d64c40ceb6f97cd707266ffedb"></a>

### [`00b10e18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b10/00b10e18.md) → [`00b70ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b70/00b70ce0.md) _ZNK11flatbuffers6Parser7IsIdentEPKc

採用 · 移動量 `+0x5fec8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 70.27% / 新版 70.27%

CFGの説明率　旧版 76.92% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b10e7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b70d44"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b10e7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b10/00b10e18.md#insn-00b10e7c) · [`00b10e24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b10/00b10e18.md#insn-00b10e24)
- 新版 [`00b70d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b70/00b70ce0.md#insn-00b70d44) · [`00b70cec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b70/00b70ce0.md#insn-00b70cec)

~~~diff
- 00b10e7c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b10e7c ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00b10e7c ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b10e7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:1:8"]]
- 00b10e7c bytes 4015889a
+ 00b70d44 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b70d44 ["COPY", "tmp:1:8", ["register:4050:8"]]
+ 00b70d44 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
+ 00b70d44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:1:8"]]
+ 00b70d44 bytes 4015889a
- 00b10e24 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:14:8"]]
- 00b10e24 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
- 00b10e24 ["INT_ZEXT", "register:4040:8", ["tmp:1:4"]]
+ 00b70cec ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:1c:8"]]
+ 00b70cec ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
+ 00b70cec ["INT_ZEXT", "register:4040:8", ["tmp:1:4"]]
- 00b10e24 bytes 081440b9
+ 00b70cec bytes 081c40b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44f133e9f4d309fbce34bb14eab1ea93"></a>

### [`00b1145c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b11/00b1145c.md) → [`00b714d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b71/00b714d8.md) _ZNK11flatbuffers6Parser12LookupStructERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x6007c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdfcd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfcd0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c6b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c6b0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 52.63% / 新版 52.63%

CFGの説明率　旧版 66.67% / 新版 57.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1145c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b11460"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b11460"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b1145c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b11460",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b11470",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5c6b0"
      ]
    ]
  ],
  "added": [
    [
      "00b714d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b714dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b714ec",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5c6b0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b1145c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b11/00b1145c.md#insn-00b1145c) · [`00b11460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b11/00b1145c.md#insn-00b11460) · [`00b11470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b11/00b1145c.md#insn-00b11470)

~~~diff
- 00b1145c ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b1145c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b1145c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b1145c bytes f30f1ef8
- 00b11460 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b11460 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b11460 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b11460 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b11460 bytes fd7b01a9
- 00b11470 ["INT_ADD", "register:40f0:8", ["const:b11470:8", "const:4:8"]]
- 00b11470 ["CALL", null, ["callee:00c5c6b0:8"]]
- 00b11470 bytes 183a0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5c0bc76338e3d0621237f30953bd958"></a>

### [`00b12668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b12/00b12668.md) → [`00b7297c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b72/00b7297c.md) _ZN11flatbuffers11SymbolTableINS_8FieldDefEE3AddERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPS1_

採用 · 移動量 `+0x60314` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf260.md) · 呼出先 9件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 1件 [`00c5bca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bca0.md) · 呼出先 9件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 45.95% / 新版 47.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1269c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b126b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b12718"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b1269c",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b126cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b72a0c"
      ]
    ],
    [
      "unmatched:00b126dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b72a10"
      ]
    ]
  ],
  "added": [
    [
      "00b729b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00b729e0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b72a0c"
      ]
    ],
    [
      "00b729f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b72a10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b1269c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b12/00b12668.md#insn-00b1269c) · [`00b126b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b12/00b12668.md#insn-00b126b0) · [`00b126cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b12/00b12668.md#insn-00b126cc)

~~~diff
- 00b1269c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00b1269c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b1269c bytes e80700f9
- 00b126b0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:20:8"]]
- 00b126b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00b126b0 bytes 891200f9
- 00b126cc ["INT_NOTEQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
- 00b126cc ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00b126cc bytes 6a0100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be3ed5d19775298b240cf4dc529e12ce"></a>

### [`00b13e18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b13/00b13e18.md) → [`00b75000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b75/00b75000.md) _ZNK11flatbuffers6Parser29SupportsAdvancedUnionFeaturesEv

採用 · 移動量 `+0x611e8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

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
      "site": "00b13e38"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b75014"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b13e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b13/00b13e18.md#insn-00b13e38) · [`00b13e18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b13/00b13e18.md#insn-00b13e18)
- 新版 [`00b75014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b75/00b75000.md#insn-00b75014)

~~~diff
- 00b13e38 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b13e38 ["RETURN", null, ["register:0:8"]]
- 00b13e38 bytes c0035fd6
+ 00b75014 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b75014 ["RETURN", null, ["register:0:8"]]
+ 00b75014 bytes c0035fd6
- 00b13e18 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:460:8"]]
- 00b13e18 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b13e18 bytes 083042f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-006b31f1c420d8c4e37524da92f0a79d"></a>

### [`00b1f3b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1f/00b1f3b4.md) → [`00b82464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b82/00b82464.md) _ZN11flatbuffers11SymbolTableINS_9StructDefEE3AddERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPS1_

採用 · 移動量 `+0x630b0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change` · `reordered`

- 旧版 呼出元 1件 [`00bdf270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf270.md) · 呼出先 9件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 1件 [`00c5bcb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bcb0.md) · 呼出先 9件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 96.36% / 新版 96.36%

CFGの説明率　旧版 74.29% / 新版 76.47%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1f418"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1f438"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b824c8"
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
      "unmatched:00b1f418",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b824f4"
      ]
    ],
    [
      "unmatched:00b1f438",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b825c0"
      ]
    ]
  ],
  "added": [
    [
      "00b824c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b824f4"
      ]
    ],
    [
      "00b824e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b825c0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b1f418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1f/00b1f3b4.md#insn-00b1f418) · [`00b1f438`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1f/00b1f3b4.md#insn-00b1f438) · [`00b1f564`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1f/00b1f3b4.md#insn-00b1f564)

~~~diff
- 00b1f418 ["INT_NOTEQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
- 00b1f418 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00b1f418 bytes 6a0100b5
- 00b1f438 ["INT_EQUAL", "tmp:0:1", ["register:40d8:8", "const:0:8"]]
- 00b1f438 ["CBRANCH", null, ["local:b19:8", "tmp:0:1"]]
- 00b1f438 bytes db0600b4
- 00b1f564 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b1f564 ["RETURN", null, ["register:0:8"]]
- 00b1f564 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-677baee1290f84ec72317c19fdc97a1e"></a>

### [`00b22e74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b22/00b22e74.md) → [`00b86bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b86/00b86bd4.md) _ZN11flatbuffers11SymbolTableINS_7RPCCallEE3AddERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPS1_

採用 · 移動量 `+0x63d60` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf250.md) · 呼出先 9件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 1件 [`00c5bc90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bc90.md) · 呼出先 9件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 99.09% / 新版 99.09%

CFGの説明率　旧版 75.76% / 新版 69.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b23024"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b86d84"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b23024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b22/00b22e74.md#insn-00b23024) · [`00b22ec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b22/00b22e74.md#insn-00b22ec0)
- 新版 [`00b86d84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b86/00b86bd4.md#insn-00b86d84) · [`00b86c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b86/00b86bd4.md#insn-00b86c20)

~~~diff
- 00b23024 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b23024 ["RETURN", null, ["register:0:8"]]
- 00b23024 bytes c0035fd6
+ 00b86d84 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b86d84 ["RETURN", null, ["register:0:8"]]
+ 00b86d84 bytes c0035fd6
- 00b22ec0 ["BRANCH", null, ["local:b13:8"]]
+ 00b86c20 ["BRANCH", null, ["local:b14:8"]]
- 00b22ec0 bytes 24000014
+ 00b86c20 bytes 24000014
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-705888e330bccdb00a800c127cf68dc8"></a>

### [`00b23244`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b23/00b23244.md) → [`00b86fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b86/00b86fa4.md) _ZN11flatbuffers6Parser13MarkGeneratedEv

採用 · 移動量 `+0x63d60` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 15.71% / 新版 15.71%

CFGの説明率　旧版 9.09% / 新版 9.38%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 10件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2328c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b23290"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b232ac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b2324c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b232b4"
      ]
    ],
    [
      "unmatched:00b23268",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b232a0"
      ]
    ],
    [
      "unmatched:00b23294",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b23280"
      ]
    ]
  ],
  "added": [
    [
      "00b86fac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b87014"
      ]
    ],
    [
      "00b86fc8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b87000"
      ]
    ],
    [
      "00b86ff4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b86fe0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2324c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b23/00b23244.md#insn-00b2324c) · [`00b23268`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b23/00b23244.md#insn-00b23268) · [`00b2328c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b23/00b23244.md#insn-00b2328c)

~~~diff
- 00b2324c ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
- 00b2324c bytes 40030054
- 00b23268 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b23268 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00b23268 ["CBRANCH", null, ["local:b5:8", "tmp:1:1"]]
- 00b23268 bytes c9010054
- 00b2328c ["COPY", "tmp:0:4", ["register:4060:4"]]
- 00b2328c ["INT_ADD", "tmp:1:8", ["register:4078:8", "const:78:8"]]
- 00b2328c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b2328c bytes ece10139
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b75b988076f79f8462b09ad1e0e96f8"></a>

### [`00b25178`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b25/00b25178.md) → [`00b89548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b89/00b89548.md) _ZN11flatbuffers6Parser24ParseProtoCurliesOrIdentEv

採用 · 移動量 `+0x643d0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdf970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf970.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c2f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c2f0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 81.82% / 新版 90.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b251a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b89578"
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
      "unmatched:00b251a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b895cc"
      ]
    ]
  ],
  "added": [
    [
      "00b89578",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b895cc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b251a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b25/00b25178.md#insn-00b251a8) · [`00b25188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b25/00b25178.md#insn-00b25188)
- 新版 [`00b89578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b89/00b89548.md#insn-00b89578)

~~~diff
- 00b251a8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b251a8 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
- 00b251a8 bytes a1020054
+ 00b89578 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b89578 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
+ 00b89578 bytes a1020054
- 00b25188 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:14:8"]]
- 00b25188 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
- 00b25188 ["INT_ZEXT", "register:40a8:8", ["tmp:1:4"]]
- 00b25188 bytes 151440b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14245f9c89b1f4399ba10156818843d5"></a>

### [`00b253cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b25/00b253cc.md) → [`00b89cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b89/00b89cc0.md) _ZN11flatbuffers6Parser22ParseTypeFromProtoTypeEPNS_4TypeE

採用 · 移動量 `+0x648f4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf960.md) · 呼出先 5件 [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md) [`00bdf870`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf870.md) [`00bdf970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf970.md)
- 新版 呼出元 1件 [`00c5c2c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c2c0.md) · 呼出先 5件 [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md) [`00c5c1a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c1a0.md) [`00c5c2f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c2f0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 79.41% / 新版 79.41%

CFGの説明率　旧版 65.00% / 新版 59.09%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b25450"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b89d44"
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
      "00b89d10",
      "READ",
      [
        "storage",
        "00c10de0",
        null,
        "pointer"
      ]
    ],
    [
      "00b89d18",
      "PARAM",
      [
        "storage",
        "002ab06b",
        null,
        "string"
      ]
    ],
    [
      "00b89d18",
      "PARAM",
      [
        "storage",
        "0029df19",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b89d10",
      "READ",
      [
        "storage",
        "00c90468",
        null,
        "pointer"
      ]
    ],
    [
      "00b89d18",
      "PARAM",
      [
        "storage",
        "002bbe42",
        null,
        "string"
      ]
    ],
    [
      "00b89d18",
      "PARAM",
      [
        "storage",
        "002ae233",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b25450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b25/00b253cc.md#insn-00b25450) · [`00b253e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b25/00b253cc.md#insn-00b253e4)
- 新版 [`00b89d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b89/00b89cc0.md#insn-00b89d44) · [`00b89cd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b89/00b89cc0.md#insn-00b89cd8)

~~~diff
- 00b25450 ["COPY", "tmp:0:8", ["register:40c8:8"]]
- 00b25450 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b25450 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b25450 ["COPY", "register:4000:8", ["tmp:0:8"]]
- 00b25450 bytes 2003889a
+ 00b89d44 ["COPY", "tmp:0:8", ["register:40c8:8"]]
+ 00b89d44 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
+ 00b89d44 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00b89d44 ["COPY", "register:4000:8", ["tmp:0:8"]]
+ 00b89d44 bytes 2003889a
- 00b253e4 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:20:8"]]
- 00b253e4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b253e4 ["INT_ZEXT", "register:40c0:8", ["tmp:1:1"]]
+ 00b89cd8 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:28:8"]]
+ 00b89cd8 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b89cd8 ["INT_ZEXT", "register:40c0:8", ["tmp:1:1"]]
- 00b253e4 bytes 18804039
+ 00b89cd8 bytes 18a04039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-649fe55aed1d4d8517fda067866ef6f2"></a>

### [`00b2e1b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2e/00b2e1b4.md) → [`00b95720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b95/00b95720.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEmc

採用 · 移動量 `+0x6756c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdefc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefc0.md) · 呼出先 2件 [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md) [`00bdda90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda90.md)
- 新版 呼出元 1件 [`00c5ba70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba70.md) · 呼出先 2件 [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md) [`00c5a4e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4e0.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 98.04% / 新版 98.04%

CFGの説明率　旧版 84.21% / 新版 88.89%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2e27c"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b957e8"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b2e27c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2e/00b2e1b4.md#insn-00b2e27c) · [`00b2e220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2e/00b2e1b4.md#insn-00b2e220)
- 新版 [`00b957e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b95/00b95720.md#insn-00b957e8) · [`00b9578c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b95/00b95720.md#insn-00b9578c)

~~~diff
- 00b2e27c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b2e27c ["RETURN", null, ["register:0:8"]]
- 00b2e27c bytes c0035fd6
+ 00b957e8 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b957e8 ["RETURN", null, ["register:0:8"]]
+ 00b957e8 bytes c0035fd6
- 00b2e220 ["INT_ADD", "register:40f0:8", ["const:b2e220:8", "const:4:8"]]
- 00b2e220 ["CALL", null, ["callee:00c5a4e0:8"]]
+ 00b9578c ["INT_ADD", "register:40f0:8", ["const:b9578c:8", "const:4:8"]]
+ 00b9578c ["CALL", null, ["callee:00c5a4e0:8"]]
- 00b2e220 bytes 1cbe0294
+ 00b9578c bytes 55130394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4fa23c91d5566e52bebae53c3a5aa0fe"></a>

### [`00b2ed88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2e/00b2ed88.md) → [`00b95aa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b95/00b95aa8.md) _ZNKSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumValEEENS_19__map_value_

採用 · 移動量 `+0x66d20` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change` · `reordered`

- 旧版 呼出元 1件 [`00bdfcb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfcb0.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`00c5c690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c690.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 76.81% / 新版 76.81%

CFGの説明率　旧版 43.48% / 新版 35.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2edc0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2edd4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2ede0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b2edc4",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b95b0c"
      ]
    ],
    [
      "00b95b2c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b2edc8"
      ]
    ],
    [
      "00b95b44",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b2edd8"
      ]
    ]
  ],
  "added": [
    [
      "00b95ae4",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b95b0c"
      ]
    ],
    [
      "00b95b2c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b95ae8"
      ]
    ],
    [
      "00b95b44",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b95af8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2edc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2e/00b2ed88.md#insn-00b2edc0) · [`00b2edd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2e/00b2ed88.md#insn-00b2edd4) · [`00b2ede0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2e/00b2ed88.md#insn-00b2ede0)

~~~diff
- 00b2edc0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b2edc0 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00b2edc0 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b2edc0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "const:1:8"]]
- 00b2edc0 bytes 5515819a
- 00b2edd4 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b2edd4 ["COPY", "tmp:1:4", ["register:4040:4"]]
- 00b2edd4 ["CBRANCH", null, ["const:2:4", "register:102:1"]]
- 00b2edd4 ["INT_NEGATE", "tmp:1:4", ["tmp:0:4"]]
- 00b2edd4 bytes 00219f5a
- 00b2ede0 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00b2ede0 ["COPY", "tmp:1:8", ["register:40a0:8"]]
- 00b2ede0 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b2ede0 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b2ede0 bytes 94b2979a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3691f406eb69434398f260f3c7b5e31"></a>

### [`00b31bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b31bb0.md) → [`00b98f2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98f2c.md) _ZNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE8overflowEi

採用 · 移動量 `+0x6737c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdda90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda90.md) [`00bdefc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefc0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a4e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4e0.md) [`00c5ba70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba70.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 95.62% / 新版 95.62%

CFGの説明率　旧版 87.76% / 新版 91.49%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b31da4"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b99120"
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
      "unmatched:00b31d9c",
      "READ",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b31dc8",
      "READ",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b99118",
      "READ",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b99144",
      "READ",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b31da4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b31bb0.md#insn-00b31da4) · [`00b31c60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b31bb0.md#insn-00b31c60)
- 新版 [`00b99120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98f2c.md#insn-00b99120) · [`00b98fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98f2c.md#insn-00b98fdc)

~~~diff
- 00b31da4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b31da4 ["RETURN", null, ["register:0:8"]]
- 00b31da4 bytes c0035fd6
+ 00b99120 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b99120 ["RETURN", null, ["register:0:8"]]
+ 00b99120 bytes c0035fd6
- 00b31c60 ["INT_ADD", "register:40f0:8", ["const:b31c60:8", "const:4:8"]]
- 00b31c60 ["CALL", null, ["callee:00c5a4e0:8"]]
+ 00b98fdc ["INT_ADD", "register:40f0:8", ["const:b98fdc:8", "const:4:8"]]
+ 00b98fdc ["CALL", null, ["callee:00c5a4e0:8"]]
- 00b31c60 bytes 8caf0294
+ 00b98fdc bytes 41050394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3bb9d5fa48ea2e398ddbfc5e4b6b00e"></a>

### [`00b31dd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b31dd4.md) → [`00b99150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b99/00b99150.md) _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEED2Ev

採用 · 移動量 `+0x6737c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdb150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb150.md) · 呼出先 1件 [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md)
- 新版 呼出元 1件 [`00c57ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ba0.md) · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md)

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
      "site": "00b31de0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b9915c"
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
      "unmatched:00b31dd8",
      "READ",
      [
        "storage",
        "00c1ba50",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b31de0",
      "DATA",
      [
        "storage",
        "00c11220",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b31de4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      "00b99154",
      "READ",
      [
        "storage",
        "00c9b448",
        null,
        "pointer"
      ]
    ],
    [
      "00b9915c",
      "DATA",
      [
        "storage",
        "00c908b0",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "00b99160",
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

- 旧版 [`00b31de0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b31dd4.md#insn-00b31de0) · [`00b31dd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b31dd4.md#insn-00b31dd4)
- 新版 [`00b9915c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b99/00b99150.md#insn-00b9915c)

~~~diff
- 00b31de0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b31de0 ["COPY", "tmp:1:8", ["register:4000:8"]]
- 00b31de0 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:8:8"]]
- 00b31de0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b31de0 bytes 088400f8
+ 00b9915c ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00b9915c ["COPY", "tmp:1:8", ["register:4000:8"]]
+ 00b9915c ["INT_ADD", "register:4000:8", ["register:4000:8", "const:8:8"]]
+ 00b9915c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 00b9915c bytes 088400f8
- 00b31dd4 ["COPY", "register:4040:8", ["const:c1b000:8"]]
- 00b31dd4 bytes 480700d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b443f32ce539ab2438827b0601127be0"></a>

### [`00b31e4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b31e4c.md) → [`00b991c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b99/00b991c8.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE5flushEv

採用 · 移動量 `+0x6737c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdc0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc0a0.md) · 呼出先 3件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdc0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc0a0.md) [`00be01f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01f0.md)
- 新版 呼出元 1件 [`00c58af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58af0.md) · 呼出先 3件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c58af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58af0.md) [`00c5ccf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ccf0.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 54.55% / 新版 54.55%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b31e6c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b991e8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b31f38"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b31e6c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b992a8"
      ]
    ]
  ],
  "added": [
    [
      "00b991e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b992a8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b31e6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b31e4c.md#insn-00b31e6c) · [`00b31f38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b31e4c.md#insn-00b31f38)
- 新版 [`00b991e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b99/00b991c8.md#insn-00b991e8)

~~~diff
- 00b31e6c ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00b31e6c ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 00b31e6c bytes 000600b4
- 00b31f38 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b31f38 ["RETURN", null, ["register:0:8"]]
- 00b31f38 bytes c0035fd6
+ 00b991e8 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00b991e8 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
+ 00b991e8 bytes 000600b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12607f26fc0ce1ad87b425fef5bd5c01"></a>

### [`00b31f3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b31f3c.md) → [`00b992b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b99/00b992b8.md) _ZNKSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strEv

採用 · 移動量 `+0x6737c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change` · `reordered`

- 旧版 呼出元 1件 [`00bdb360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb360.md) · 呼出先 2件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 1件 [`00c57db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57db0.md) · 呼出先 2件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 58.78% / 新版 58.78%

CFGの説明率　旧版 25.37% / 新版 26.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 8件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b31f3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b31f40"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b31f40"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b31f3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b31f40",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b31f44",
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
      "00b992b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b992bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b992c0",
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

- 旧版 [`00b31f3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b31f3c.md#insn-00b31f3c) · [`00b31f40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b31f3c.md#insn-00b31f40) · [`00b31f44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b31f3c.md#insn-00b31f44)

~~~diff
- 00b31f3c ["COPY", "tmp:0:8", ["register:40b8:8"]]
- 00b31f3c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00b31f3c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b31f3c bytes f70f1cf8
- 00b31f40 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b31f40 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b31f40 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b31f40 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b31f40 bytes f65701a9
- 00b31f44 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b31f44 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b31f44 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b31f44 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b31f44 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7da1c6e5089ce642b7f9401319a46fc1"></a>

### [`00b332bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b33/00b332bc.md) → [`00b9a900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9a/00b9a900.md) _ZN11flexbuffers7Builder8WriteAnyERKNS0_5ValueEh

採用 · 移動量 `+0x67644` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdfb50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfb50.md) · 呼出先 2件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00be00e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be00e0.md)
- 新版 呼出元 1件 [`00c5c500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c500.md) · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5cc80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cc80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 68.42% / 新版 68.42%

CFGの説明率　旧版 30.43% / 新版 41.18%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b332c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b332c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b332c4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b332c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b332c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b332d4",
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
      "00b9a904",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b9a908",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b9a918",
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

- 旧版 [`00b332c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b33/00b332bc.md#insn-00b332c0) · [`00b332c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b33/00b332bc.md#insn-00b332c4) · [`00b332d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b33/00b332bc.md#insn-00b332d4)

~~~diff
- 00b332c0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00b332c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00b332c0 bytes f30b00f9
- 00b332c4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b332c4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b332c4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b332c4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b332c4 bytes fd7b02a9
- 00b332d4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00b332d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b332d4 bytes e80700f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6db20ffed4dc45f8d6a661a57c758d74"></a>

### [`00b3370c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b33/00b3370c.md) → [`00b9ad50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9a/00b9ad50.md) _ZNSt6__ndk16vectorIhNS_9allocatorIhEEE6insertIPKhEENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_constructibleIhNS_15iterator

採用 · 移動量 `+0x67644` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be00e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be00e0.md) · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 1件 [`00c5cc80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cc80.md) · 呼出先 5件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 63.64% / 新版 71.01%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 4件, `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b33710"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b33710"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b33714"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b33710",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b33714",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b33718",
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
      "00b9ad54",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b9ad58",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b9ad5c",
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

- 旧版 [`00b33710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b33/00b3370c.md#insn-00b33710) · [`00b33714`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b33/00b3370c.md#insn-00b33714) · [`00b33718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b33/00b3370c.md#insn-00b33718)

~~~diff
- 00b33710 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b33710 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00b33710 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b33710 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b33710 bytes fc6f01a9
- 00b33714 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b33714 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b33714 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b33714 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b33714 bytes fa6702a9
- 00b33718 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b33718 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b33718 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b33718 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b33718 bytes f85f03a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8db2af07dca46c8651e33d4322bf272"></a>

### [`00b33d7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b33/00b33d7c.md) → [`00b994c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b99/00b994c4.md) FUN_00b994c4

採用 · 移動量 `+0x65748` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change` · `reordered`

- 旧版 呼出元 3件 [`00b256e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b25/00b256e4.md) [`00b33c60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b33/00b33c60.md) [`00b4430c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b4430c.md) · 呼出先 4件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 4件 [`00b89fd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b89/00b89fd8.md) [`00b8a110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8a/00b8a110.md) [`00b9b2d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9b/00b9b2d4.md) [`00bafc4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00bafc4c.md) · 呼出先 4件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 86.36% / 新版 86.36%

CFGの説明率　旧版 45.83% / 新版 55.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b33d7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b33d80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b33d80"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b33d7c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b33d80",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b33d84",
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
      "00b994c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b994c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b994cc",
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

- 旧版 [`00b33d7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b33/00b33d7c.md#insn-00b33d7c) · [`00b33d80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b33/00b33d7c.md#insn-00b33d80) · [`00b33d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b33/00b33d7c.md#insn-00b33d84)

~~~diff
- 00b33d7c ["COPY", "tmp:0:8", ["register:40c8:8"]]
- 00b33d7c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 00b33d7c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b33d7c bytes f90f1bf8
- 00b33d80 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b33d80 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b33d80 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b33d80 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b33d80 bytes f85f01a9
- 00b33d84 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b33d84 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b33d84 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b33d84 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b33d84 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62139d4c70df3c4d99193302510fe673"></a>

### [`00b382d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b38/00b382d8.md) → [`00ba1574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba1/00ba1574.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers9NamespaceEEENS_19__map_value

採用 · 移動量 `+0x6929c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change` · `reordered`

- 旧版 呼出元 1件 [`00bdfff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfff0.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`00c5cb60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cb60.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 98.61% / 新版 98.61%

CFGの説明率　旧版 60.00% / 新版 70.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b383f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00ba1690"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b383f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b38/00b382d8.md#insn-00b383f4) · [`00b38300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b38/00b382d8.md#insn-00b38300)
- 新版 [`00ba1690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba1/00ba1574.md#insn-00ba1690) · [`00ba159c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba1/00ba1574.md#insn-00ba159c)

~~~diff
- 00b383f4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b383f4 ["RETURN", null, ["register:0:8"]]
- 00b383f4 bytes c0035fd6
+ 00ba1690 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00ba1690 ["RETURN", null, ["register:0:8"]]
+ 00ba1690 bytes c0035fd6
- 00b38300 ["INT_EQUAL", "tmp:0:1", ["register:40b8:8", "const:0:8"]]
- 00b38300 ["CBRANCH", null, ["local:b19:8", "tmp:0:1"]]
+ 00ba159c ["INT_EQUAL", "tmp:0:1", ["register:40b8:8", "const:0:8"]]
+ 00ba159c ["CBRANCH", null, ["local:b17:8", "tmp:0:1"]]
- 00b38300 bytes 570600b4
+ 00ba159c bytes 570600b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5bd0feb0b6f2f906188bf98f3472033"></a>

### [`00b3ec8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3e/00b3ec8c.md) → [`00ba8698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba8/00ba8698.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmPKcm

採用 · 移動量 `+0x69a0c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change` · `reordered`

- 旧版 呼出元 1件 [`00bdc180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc180.md) · 呼出先 3件 [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bde220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde220.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 1件 [`00c58bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58bd0.md) · 呼出先 3件 [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c5aca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 98.61% / 新版 98.61%

CFGの説明率　旧版 85.71% / 新版 77.42%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3ecc0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00ba86cc"
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
      "unmatched:00b3ecc0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba86e0"
      ]
    ]
  ],
  "added": [
    [
      "00ba86cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba86e0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b3ecc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3e/00b3ec8c.md#insn-00b3ecc0) · [`00b3ecb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3e/00b3ec8c.md#insn-00b3ecb4)
- 新版 [`00ba86cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba8/00ba8698.md#insn-00ba86cc) · [`00ba86c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba8/00ba8698.md#insn-00ba86c0)

~~~diff
- 00b3ecc0 ["CBRANCH", null, ["local:b4:8", "register:102:1"]]
- 00b3ecc0 bytes a2000054
+ 00ba86cc ["CBRANCH", null, ["local:b7:8", "register:102:1"]]
+ 00ba86cc bytes a2000054
- 00b3ecb4 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00b3ecb4 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b3ecb4 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b3ecb4 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00ba86c0 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
+ 00ba86c0 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00ba86c0 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00ba86c0 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b3ecb4 bytes a8000037
+ 00ba86c0 bytes a8000037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30f4fb753588e59f6e56b6a76fc55513"></a>

### [`00b3f03c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3f/00b3f03c.md) → [`00bb211c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb2/00bb211c.md) _ZNKSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumDefEEENS_19__map_value_

採用 · 移動量 `+0x730e0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change` · `reordered`

- 旧版 呼出元 1件 [`00bdfca0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfca0.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`00c5c680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c680.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 85.51% / 新版 85.51%

CFGの説明率　旧版 60.87% / 新版 51.85%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3f03c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3f03c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3f040"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b3f03c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b3f040",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b3f044",
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
      "00bb211c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00bb2120",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bb2124",
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

- 旧版 [`00b3f03c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3f/00b3f03c.md#insn-00b3f03c) · [`00b3f040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3f/00b3f03c.md#insn-00b3f040) · [`00b3f044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3f/00b3f03c.md#insn-00b3f044)

~~~diff
- 00b3f03c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b3f03c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b3f03c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00b3f03c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b3f03c bytes f85fbca9
- 00b3f040 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b3f040 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b3f040 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b3f040 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b3f040 bytes f65701a9
- 00b3f044 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b3f044 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b3f044 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b3f044 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b3f044 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c12740a8e09e2d65dfbb20080481972"></a>

### [`00b3f150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3f/00b3f150.md) → [`00ba8a48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba8/00ba8a48.md) _ZNKSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers9StructDefEEENS_19__map_valu

採用 · 移動量 `+0x698f8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change` · `reordered`

- 旧版 呼出元 1件 [`00bdfcd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfcd0.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`00c5c6b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c6b0.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 82.61% / 新版 82.61%

CFGの説明率　旧版 36.00% / 新版 29.03%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3f16c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3f184"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3f188"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b3f16c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba8b40"
      ]
    ]
  ],
  "added": [
    [
      "00ba8a64",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba8b40"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b3f16c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3f/00b3f150.md#insn-00b3f16c) · [`00b3f184`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3f/00b3f150.md#insn-00b3f184) · [`00b3f188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3f/00b3f150.md#insn-00b3f188)

~~~diff
- 00b3f16c ["INT_EQUAL", "tmp:0:1", ["register:40b8:8", "const:0:8"]]
- 00b3f16c ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 00b3f16c bytes f70600b4
- 00b3f184 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b3f184 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b3f184 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b3f184 ["COPY", "register:40b0:8", ["tmp:0:8"]]
- 00b3f184 bytes 7601899a
- 00b3f188 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b3f188 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00b3f188 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b3f188 ["INT_ADD", "tmp:1:8", ["register:4008:8", "const:1:8"]]
- 00b3f188 bytes 5515819a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ecfba73a17a62e95f15e82802475f17a"></a>

### [`00b3f264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3f/00b3f264.md) → [`00ba8b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba8/00ba8b5c.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers8FieldDefEEENS_19__map_value_

採用 · 移動量 `+0x698f8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdffe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdffe0.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`00c5cb50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cb50.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 75.36% / 新版 75.36%

CFGの説明率　旧版 25.00% / 新版 20.69%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 9件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3f280"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3f2b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3f2bc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b3f280",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba8c54"
      ]
    ],
    [
      "unmatched:00b3f2e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba8b9c"
      ]
    ],
    [
      "00ba8bf8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b3f2b4"
      ]
    ]
  ],
  "added": [
    [
      "00ba8b78",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba8c54"
      ]
    ],
    [
      "00ba8be0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba8b9c"
      ]
    ],
    [
      "00ba8bf8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba8bac"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b3f280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3f/00b3f264.md#insn-00b3f280) · [`00b3f2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3f/00b3f264.md#insn-00b3f2b0) · [`00b3f2bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3f/00b3f264.md#insn-00b3f2bc)

~~~diff
- 00b3f280 ["INT_EQUAL", "tmp:0:1", ["register:40b8:8", "const:0:8"]]
- 00b3f280 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 00b3f280 bytes f70600b4
- 00b3f2b0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b3f2b0 ["COPY", "tmp:1:4", ["register:4040:4"]]
- 00b3f2b0 ["CBRANCH", null, ["const:2:4", "register:102:1"]]
- 00b3f2b0 ["INT_NEGATE", "tmp:1:4", ["tmp:0:4"]]
- 00b3f2b0 bytes 00219f5a
- 00b3f2bc ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00b3f2bc ["COPY", "tmp:1:8", ["register:40a0:8"]]
- 00b3f2bc ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b3f2bc ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b3f2bc bytes 94b2979a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ed7f4387653468cccdaf5c9750f6332"></a>

### [`00b3f498`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3f/00b3f498.md) → [`00ba8584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba8/00ba8584.md) _ZNKSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers5ValueEEENS_19__map_value_co

採用 · 移動量 `+0x690ec` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change` · `reordered`

- 旧版 呼出元 1件 [`00bdfc90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfc90.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`00c5c670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c670.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 81.16% / 新版 81.16%

CFGの説明率　旧版 54.17% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3f4cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3f4d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3f4e4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b3f51c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba85c4"
      ]
    ],
    [
      "00ba8620",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b3f4e8"
      ]
    ]
  ],
  "added": [
    [
      "00ba8608",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba85c4"
      ]
    ],
    [
      "00ba8620",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba85d4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b3f4cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3f/00b3f498.md#insn-00b3f4cc) · [`00b3f4d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3f/00b3f498.md#insn-00b3f4d0) · [`00b3f4e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3f/00b3f498.md#insn-00b3f4e4)

~~~diff
- 00b3f4cc ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b3f4cc ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b3f4cc ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b3f4cc ["COPY", "register:40b0:8", ["tmp:0:8"]]
- 00b3f4cc bytes 7601899a
- 00b3f4d0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b3f4d0 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00b3f4d0 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b3f4d0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "const:1:8"]]
- 00b3f4d0 bytes 5515819a
- 00b3f4e4 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b3f4e4 ["COPY", "tmp:1:4", ["register:4040:4"]]
- 00b3f4e4 ["CBRANCH", null, ["const:2:4", "register:102:1"]]
- 00b3f4e4 ["INT_NEGATE", "tmp:1:4", ["tmp:0:4"]]
- 00b3f4e4 bytes 00219f5a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72d132d9d971c1bfaae51060b4cbaeec"></a>

### [`00b3f7d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3f/00b3f7d0.md) → [`00ba8fb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba8/00ba8fb4.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers5ValueEEENS_19__map_value_com

採用 · 移動量 `+0x697e4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdff40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdff40.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`00c5cab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cab0.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 75.36% / 新版 75.36%

CFGの説明率　旧版 33.33% / 新版 29.63%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 6件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3f848"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3f850"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3f854"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b3f854",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba8ff4"
      ]
    ]
  ],
  "added": [
    [
      "00ba9038",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba8ff4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b3f848`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3f/00b3f7d0.md#insn-00b3f848) · [`00b3f850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3f/00b3f7d0.md#insn-00b3f850) · [`00b3f854`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3f/00b3f7d0.md#insn-00b3f854)

~~~diff
- 00b3f848 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b3f848 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b3f848 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b3f848 ["COPY", "register:40c0:8", ["tmp:0:8"]]
- 00b3f848 bytes 78018a9a
- 00b3f850 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b3f850 ["COPY", "tmp:1:8", ["register:40b0:8"]]
- 00b3f850 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b3f850 ["COPY", "tmp:1:8", ["register:40c0:8"]]
- 00b3f850 bytes c232989a
- 00b3f854 ["INT_EQUAL", "tmp:0:1", ["register:4010:8", "const:0:8"]]
- 00b3f854 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b3f854 bytes e2fdffb4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9cda4ce39880617e0d351bee82d0cad1"></a>

### [`00b3fbb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3f/00b3fbb8.md) → [`00ba9800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba9/00ba9800.md) _ZNKSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers8FieldDefEEENS_19__map_value

採用 · 移動量 `+0x69c48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdfcc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfcc0.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`00c5c6a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c6a0.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 98.55% / 新版 98.55%

CFGの説明率　旧版 91.30% / 新版 87.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3fbf0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00ba9838"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b3fbf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3f/00b3fbb8.md#insn-00b3fbf0) · [`00b3fbd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3f/00b3fbb8.md#insn-00b3fbd4)
- 新版 [`00ba9838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba9/00ba9800.md#insn-00ba9838) · [`00ba981c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba9/00ba9800.md#insn-00ba981c)

~~~diff
- 00b3fbf0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b3fbf0 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00b3fbf0 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b3fbf0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "const:1:8"]]
- 00b3fbf0 bytes 5515819a
+ 00ba9838 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00ba9838 ["COPY", "tmp:1:8", ["register:4050:8"]]
+ 00ba9838 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
+ 00ba9838 ["INT_ADD", "tmp:1:8", ["register:4008:8", "const:1:8"]]
+ 00ba9838 bytes 5515819a
- 00b3fbd4 ["INT_EQUAL", "tmp:0:1", ["register:40b8:8", "const:0:8"]]
- 00b3fbd4 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
+ 00ba981c ["INT_EQUAL", "tmp:0:1", ["register:40b8:8", "const:0:8"]]
+ 00ba981c ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 00b3fbd4 bytes f70600b4
+ 00ba981c bytes f70600b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a605b96b2bc3da320c90405c173b76d"></a>

### [`00b4089c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b40/00b4089c.md) → [`00baa424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baa/00baa424.md) _ZNSt6__ndk114__split_bufferINS_4pairIN11flatbuffers5ValueEPNS2_8FieldDefEEERNS_9allocatorIS6_EEE9push_backEOS6_

採用 · 移動量 `+0x69b88` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdfd20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfd20.md) · 呼出先 3件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 1件 [`00c5c770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c770.md) · 呼出先 3件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 64.94% / 新版 64.94%

CFGの説明率　旧版 33.33% / 新版 25.49%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 5件, `unresolved_store_alignment` 33件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4089c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b408a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b408a0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4089c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b408a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b408a4",
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
      "00baa424",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00baa428",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00baa42c",
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

- 旧版 [`00b4089c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b40/00b4089c.md#insn-00b4089c) · [`00b408a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b40/00b4089c.md#insn-00b408a0) · [`00b408a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b40/00b4089c.md#insn-00b408a4)

~~~diff
- 00b4089c ["COPY", "tmp:0:8", ["register:40c8:8"]]
- 00b4089c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 00b4089c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b4089c bytes f90f1bf8
- 00b408a0 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b408a0 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b408a0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b408a0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b408a0 bytes f85f01a9
- 00b408a4 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b408a4 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b408a4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b408a4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b408a4 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee3cb2f1388ee339f21e227be0a3b858"></a>

### [`00b40dec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b40/00b40dec.md) → [`00baa934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baa/00baa934.md) _ZNSt6__ndk16vectorINS_4pairIN11flatbuffers5ValueEPNS2_8FieldDefEEENS_9allocatorIS6_EEE21__push_back_slow_pathIS6_EEvOT_

採用 · 移動量 `+0x69b48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be00a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be00a0.md) · 呼出先 3件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 1件 [`00c5cc40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cc40.md) · 呼出先 3件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 72.22% / 新版 72.22%

CFGの説明率　旧版 29.63% / 新版 24.24%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 5件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b40eb4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b40ebc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00baa9fc"
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
      "unmatched:00b40e34",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00baaae0"
      ]
    ],
    [
      "unmatched:00b40e64",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00baa9c0"
      ]
    ],
    [
      "unmatched:00b40e74",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00baaad8"
      ]
    ]
  ],
  "added": [
    [
      "00baa97c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00baaae0"
      ]
    ],
    [
      "00baa9ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00baa9c0"
      ]
    ],
    [
      "00baa9bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00baaad8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b40e34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b40/00b40dec.md#insn-00b40e34) · [`00b40e64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b40/00b40dec.md#insn-00b40e64) · [`00b40e70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b40/00b40dec.md#insn-00b40e70)

~~~diff
- 00b40e34 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b40e34 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00b40e34 ["CBRANCH", null, ["local:b20:8", "tmp:1:1"]]
- 00b40e34 bytes 280b0054
- 00b40e64 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b40e64 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00b40e64 ["CBRANCH", null, ["local:b4:8", "tmp:1:1"]]
- 00b40e64 bytes a8000054
- 00b40e70 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b40e70 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00b40e70 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b40e70 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00b40e70 bytes 1531899a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a7cae61fe29cc4b2a839fcf02565b6c"></a>

### [`00b41224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b41/00b41224.md) → [`00bab568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bab/00bab568.md) _ZNSt6__ndk16vectorIN11flatbuffers5ValueENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJS2_EEEvDpOT_

採用 · 移動量 `+0x6a344` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0060.md) · 呼出先 3件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 1件 [`00c5cc00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cc00.md) · 呼出先 3件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 76.40% / 新版 76.40%

CFGの説明率　旧版 34.38% / 新版 32.35%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 4件, `unresolved_store_alignment` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b41224"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b41224"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b41228"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b41224",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b41228",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4122c",
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
      "00bab568",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bab56c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bab570",
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

- 旧版 [`00b41224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b41/00b41224.md#insn-00b41224) · [`00b41228`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b41/00b41224.md#insn-00b41228) · [`00b4122c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b41/00b41224.md#insn-00b4122c)

~~~diff
- 00b41224 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b41224 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b41224 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b41224 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b41224 bytes f657bda9
- 00b41228 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b41228 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b41228 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b41228 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b41228 bytes f44f01a9
- 00b4122c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b4122c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b4122c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b4122c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4122c bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b450854d6eb21995a7f335baa5432c9"></a>

### [`00b42c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b42/00b42c18.md) → [`00bae444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bae/00bae444.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumValEEENS_19__map_value_c

採用 · 移動量 `+0x6b82c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdffa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdffa0.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`00c5cb10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cb10.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 69.23% / 新版 78.26%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b42c64"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bae490"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b42c64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b42/00b42c18.md#insn-00b42c64) · [`00b42c34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b42/00b42c18.md#insn-00b42c34)
- 新版 [`00bae490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bae/00bae444.md#insn-00bae490) · [`00bae460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bae/00bae444.md#insn-00bae460)

~~~diff
- 00b42c64 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b42c64 ["COPY", "tmp:1:4", ["register:4040:4"]]
- 00b42c64 ["CBRANCH", null, ["const:2:4", "register:102:1"]]
- 00b42c64 ["INT_NEGATE", "tmp:1:4", ["tmp:0:4"]]
- 00b42c64 bytes 00219f5a
+ 00bae490 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bae490 ["COPY", "tmp:1:4", ["register:4040:4"]]
+ 00bae490 ["CBRANCH", null, ["const:2:4", "register:102:1"]]
+ 00bae490 ["INT_NEGATE", "tmp:1:4", ["tmp:0:4"]]
+ 00bae490 bytes 00219f5a
- 00b42c34 ["INT_EQUAL", "tmp:0:1", ["register:40b8:8", "const:0:8"]]
- 00b42c34 ["CBRANCH", null, ["local:b16:8", "tmp:0:1"]]
+ 00bae460 ["INT_EQUAL", "tmp:0:1", ["register:40b8:8", "const:0:8"]]
+ 00bae460 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 00b42c34 bytes f70600b4
+ 00bae460 bytes f70600b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8776ca5804450ed62e754c569854fd87"></a>

### [`00b42fa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b42/00b42fa0.md) → [`00bae7cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bae/00bae7cc.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers4TypeEEENS_19__map_value_comp

採用 · 移動量 `+0x6b82c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdff10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdff10.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`00c5ca80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ca80.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 75.00% / 新版 80.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b42fe0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b43050"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bae80c"
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
      "unmatched:00b43050",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bae890"
      ]
    ]
  ],
  "added": [
    [
      "00bae87c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bae890"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b42fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b42/00b42fa0.md#insn-00b42fe0) · [`00b43050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b42/00b42fa0.md#insn-00b43050)
- 新版 [`00bae80c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bae/00bae7cc.md#insn-00bae80c)

~~~diff
- 00b42fe0 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b42fe0 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b42fe0 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b42fe0 ["COPY", "register:40c0:8", ["tmp:0:8"]]
- 00b42fe0 bytes 7801899a
- 00b43050 ["CBRANCH", null, ["local:b14:8", "register:102:1"]]
- 00b43050 bytes a2000054
+ 00bae80c ["COPY", "tmp:0:8", ["register:4058:8"]]
+ 00bae80c ["CBRANCH", null, ["const:2:4", "register:101:1"]]
+ 00bae80c ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00bae80c ["COPY", "register:40c0:8", ["tmp:0:8"]]
+ 00bae80c bytes 7801899a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3523b2360166c60139306c75ce3e691e"></a>

### [`00b4375c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b4375c.md) → [`00baf09c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00baf09c.md) FUN_00baf09c

採用 · 移動量 `+0x6b940` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b430c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b430c0.md) [`00b439c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b439c0.md) · 呼出先 1件 [`00be01b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01b0.md)
- 新版 呼出元 2件 [`00baea00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bae/00baea00.md) [`00baf300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00baf300.md) · 呼出先 1件 [`00c5ccb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ccb0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 96.97% / 新版 96.97%

CFGの説明率　旧版 66.67% / 新版 83.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b437a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00baf0e8"
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
      "unmatched:00b437a8",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00baf0e8",
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

- 旧版 [`00b437a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b4375c.md#insn-00b437a8) · [`00b43790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b4375c.md#insn-00b43790)
- 新版 [`00baf0e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00baf09c.md#insn-00baf0e8) · [`00baf0d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00baf09c.md#insn-00baf0d0)

~~~diff
- 00b437a8 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b437a8 ["INT_ADD", "register:40f0:8", ["const:b437a8:8", "const:4:8"]]
- 00b437a8 ["CALLIND", null, ["register:0:8"]]
- 00b437a8 bytes 20013fd6
+ 00baf0e8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00baf0e8 ["INT_ADD", "register:40f0:8", ["const:baf0e8:8", "const:4:8"]]
+ 00baf0e8 ["CALLIND", null, ["register:0:8"]]
+ 00baf0e8 bytes 20013fd6
- 00b43790 ["INT_ADD", "register:40f0:8", ["const:b43790:8", "const:4:8"]]
- 00b43790 ["CALL", null, ["callee:00c5ccb0:8"]]
+ 00baf0d0 ["INT_ADD", "register:40f0:8", ["const:baf0d0:8", "const:4:8"]]
+ 00baf0d0 ["CALL", null, ["callee:00c5ccb0:8"]]
- 00b43790 bytes 88720294
+ 00baf0d0 bytes f8b60294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8da7ccee45ac63b1d8b3320a58eb57cc"></a>

### [`00b439c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b439c0.md) → [`00baf300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00baf300.md) _ZNSt6__ndk127__insertion_sort_incompleteIRPFbPKN11flatbuffers8FieldDefES4_EPPS2_EEbT0_SA_T_

採用 · 移動量 `+0x6b940` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdfe20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfe20.md) · 呼出先 2件 [`00b4375c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b4375c.md) [`00be01b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01b0.md)
- 新版 呼出元 1件 [`00c5c9b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c9b0.md) · 呼出先 2件 [`00baf09c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00baf09c.md) [`00c5ccb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ccb0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 94.19% / 新版 94.19%

CFGの説明率　旧版 74.60% / 新版 81.03%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b43bac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00baf4ec"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b43be8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00baf340",
      "DATA",
      [
        "storage",
        "002f85c2",
        "switchD_00b43a0c::switchdataD_002f85c2",
        "byte"
      ]
    ],
    [
      "unmatched:00b43be8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00baf584"
      ]
    ],
    [
      "unmatched:00b43b4c",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00baf340",
      "DATA",
      [
        "storage",
        "0030e1de",
        "switchD_00baf34c::switchdataD_0030e1de",
        "byte"
      ]
    ],
    [
      "00baf528",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00baf584"
      ]
    ],
    [
      "00baf48c",
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

- 旧版 [`00b43b4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b439c0.md#insn-00b43b4c) · [`00b43bac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b439c0.md#insn-00b43bac) · [`00b43be8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b439c0.md#insn-00b43be8)

~~~diff
- 00b43b4c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b43b4c ["INT_ADD", "register:40f0:8", ["const:b43b4c:8", "const:4:8"]]
- 00b43b4c ["CALLIND", null, ["register:0:8"]]
- 00b43b4c bytes 00013fd6
- 00b43bac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8:8"]]
- 00b43bac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b43bac bytes 6082803c
- 00b43be8 ["CBRANCH", null, ["local:b39:8", "register:101:1"]]
- 00b43be8 bytes e0020054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-860fe29a6091819a4b97287386cf5bdd"></a>

### [`00b43d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b43d84.md) → [`00baf6c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00baf6c4.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers10ServiceDefEEENS_19__map_val

採用 · 移動量 `+0x6b940` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdfef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfef0.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`00c5ca60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ca60.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 80.65% / 新版 80.65%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b43dc8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b43dfc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b43e04"
    }
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b43dc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b43d84.md#insn-00b43dc8) · [`00b43dfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b43d84.md#insn-00b43dfc) · [`00b43e04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b43d84.md#insn-00b43e04)

~~~diff
- 00b43dc8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b43dc8 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00b43dc8 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b43dc8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "const:1:8"]]
- 00b43dc8 bytes 5515829a
- 00b43dfc ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b43dfc ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b43dfc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b43dfc ["COPY", "register:40c8:8", ["tmp:0:8"]]
- 00b43dfc bytes 3901889a
- 00b43e04 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b43e04 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b43e04 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b43e04 ["COPY", "tmp:1:8", ["register:40c0:8"]]
- 00b43e04 bytes 3633989a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23ef680804a9e401686c723680989afb"></a>

### [`00b43ea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b43ea4.md) → [`00baf7e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00baf7e4.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7RPCCallEEENS_19__map_value_c

採用 · 移動量 `+0x6b940` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdffc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdffc0.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`00c5cb30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cb30.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 85.51% / 新版 85.51%

CFGの説明率　旧版 56.00% / 新版 53.85%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b43ed8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b43edc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b43efc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b43f28",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00baf824"
      ]
    ]
  ],
  "added": [
    [
      "00baf868",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00baf824"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b43ed8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b43ea4.md#insn-00b43ed8) · [`00b43edc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b43ea4.md#insn-00b43edc) · [`00b43efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b43ea4.md#insn-00b43efc)

~~~diff
- 00b43ed8 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b43ed8 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b43ed8 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b43ed8 ["COPY", "register:40b0:8", ["tmp:0:8"]]
- 00b43ed8 bytes 7601899a
- 00b43edc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b43edc ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00b43edc ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b43edc ["INT_ADD", "tmp:1:8", ["register:4008:8", "const:1:8"]]
- 00b43edc bytes 5515819a
- 00b43efc ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00b43efc ["COPY", "tmp:1:8", ["register:40a0:8"]]
- 00b43efc ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b43efc ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b43efc bytes 94b2979a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3d5291f759444485c59aba58d693f3b"></a>

### [`00b43fb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b43fb8.md) → [`00baf8f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00baf8f8.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7RPCCallEEENS_19__map_value_c

採用 · 移動量 `+0x6b940` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdffb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdffb0.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`00c5cb20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cb20.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 45.16% / 新版 41.18%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b43ffc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b44008"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b44014"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b44000",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b4401c"
      ]
    ],
    [
      "unmatched:00b44008",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00baf9e0"
      ]
    ],
    [
      "unmatched:00b44014",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00baf9e0"
      ]
    ]
  ],
  "added": [
    [
      "00baf940",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00baf95c"
      ]
    ],
    [
      "00baf948",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00baf9e0"
      ]
    ],
    [
      "00baf954",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00baf9e0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b43ffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b43fb8.md#insn-00b43ffc) · [`00b44008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b43fb8.md#insn-00b44008) · [`00b44014`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b43/00b43fb8.md#insn-00b44014)

~~~diff
- 00b43ffc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b43ffc ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00b43ffc ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b43ffc ["INT_ADD", "tmp:1:8", ["register:4010:8", "const:1:8"]]
- 00b43ffc bytes 5515829a
- 00b44008 ["CBRANCH", null, ["local:b17:8", "register:102:1"]]
- 00b44008 bytes c2040054
- 00b44014 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b44014 ["CBRANCH", null, ["local:b17:8", "tmp:0:1"]]
- 00b44014 bytes 680400b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-584364ad254e5055e9cc380471ec8520"></a>

### [`00b440d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b440d8.md) → [`00bafa18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00bafa18.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumDefEEENS_19__map_value_c

採用 · 移動量 `+0x6b940` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdff80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdff80.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`00c5caf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5caf0.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.10% / 新版 97.10%

CFGの説明率　旧版 79.17% / 新版 82.61%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b44158"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4415c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bafa98"
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
      "unmatched:00b4415c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bafa58"
      ]
    ]
  ],
  "added": [
    [
      "00bafa9c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bafa58"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b44158`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b440d8.md#insn-00b44158) · [`00b4415c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b440d8.md#insn-00b4415c)
- 新版 [`00bafa98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00bafa18.md#insn-00bafa98)

~~~diff
- 00b44158 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b44158 ["COPY", "tmp:1:8", ["register:40b0:8"]]
- 00b44158 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b44158 ["COPY", "tmp:1:8", ["register:40c0:8"]]
- 00b44158 bytes c232989a
- 00b4415c ["INT_EQUAL", "tmp:0:1", ["register:4010:8", "const:0:8"]]
- 00b4415c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b4415c bytes e2fdffb4
+ 00bafa98 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00bafa98 ["COPY", "tmp:1:8", ["register:40b0:8"]]
+ 00bafa98 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
+ 00bafa98 ["COPY", "tmp:1:8", ["register:40c0:8"]]
+ 00bafa98 bytes c232989a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5859e5ea939102abbd3247c80a0b31e6"></a>

### [`00b4458c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b4458c.md) → [`00bafebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00bafebc.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers9StructDefEEENS_19__map_value

採用 · 移動量 `+0x6b930` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0020.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`00c5cb90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cb90.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 53.85% / 新版 60.87%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b445c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4464c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b44654"
    }
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b445c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b4458c.md#insn-00b445c0) · [`00b4464c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b4458c.md#insn-00b4464c) · [`00b44654`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b4458c.md#insn-00b44654)

~~~diff
- 00b445c0 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b445c0 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b445c0 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b445c0 ["COPY", "register:40b0:8", ["tmp:0:8"]]
- 00b445c0 bytes 7601899a
- 00b4464c ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b4464c ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b4464c ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b4464c ["COPY", "register:40b8:8", ["tmp:0:8"]]
- 00b4464c bytes 77018a9a
- 00b44654 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b44654 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b44654 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b44654 ["COPY", "tmp:1:8", ["register:40b0:8"]]
- 00b44654 bytes e232969a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9fefca343d37cc4ca7d41cb73be5638"></a>

### [`00b447c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b447c0.md) → [`00bb00f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb0/00bb00f0.md) _ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE24__emplace_back_slow_pathIJRS6_EEEvDpOT_

採用 · 移動量 `+0x6b930` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0080.md) · 呼出先 4件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md) [`00bde730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde730.md)
- 新版 呼出元 1件 [`00c5cc20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cc20.md) · 呼出先 4件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md) [`00c5b1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1b0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 84.52% / 新版 84.52%

CFGの説明率　旧版 45.45% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b44874"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b44878"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4487c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b44868",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb01cc"
      ]
    ],
    [
      "unmatched:00b44890",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b4486c"
      ]
    ],
    [
      "unmatched:00b448ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb020c"
      ]
    ]
  ],
  "added": [
    [
      "00bb0198",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb01cc"
      ]
    ],
    [
      "00bb01c0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb019c"
      ]
    ],
    [
      "00bb01dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb020c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b44868`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b447c0.md#insn-00b44868) · [`00b44874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b447c0.md#insn-00b44874) · [`00b44878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b447c0.md#insn-00b44878)

~~~diff
- 00b44868 ["CBRANCH", null, ["local:b14:8", "register:101:1"]]
- 00b44868 bytes a0010054
- 00b44874 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b44874 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "const:fffffffffffffff8:8"]]
- 00b44874 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b44874 bytes 8b821ff8
- 00b44878 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ffffffffffffffe8:8"]]
- 00b44878 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b44878 bytes 80829e3c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c6ba36cc6dbebc7d43012459f3a9a613"></a>

### [`00b44a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b44a44.md) → [`00bb0668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb0/00bb0668.md) _ZNSt6__ndk16__sortIRPFbPKN11flatbuffers9StructDefES4_EPPS2_EEvT0_SA_T_

採用 · 移動量 `+0x6bc24` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdfec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfec0.md) · 呼出先 5件 [`00b450e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b45/00b450e0.md) [`00bdfda0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfda0.md) [`00bdfe30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfe30.md) [`00bdfec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfec0.md) [`00be01c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01c0.md)
- 新版 呼出元 1件 [`00c5ca00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ca00.md) · 呼出先 5件 [`00bb0d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb0/00bb0d04.md) [`00c5c800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c800.md) [`00c5c9c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c9c0.md) [`00c5ca00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ca00.md) [`00c5ccc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ccc0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 96.32% / 新版 96.32%

CFGの説明率　旧版 76.36% / 新版 68.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b44bdc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b44be0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bb0800"
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
      "unmatched:00b44de0",
      "DATA",
      [
        "storage",
        "002f85c8",
        "switchD_00b44de8::switchdataD_002f85c8",
        "byte"
      ]
    ],
    [
      "unmatched:00b44afc",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ],
    [
      "unmatched:00b44b30",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00bb0a04",
      "DATA",
      [
        "storage",
        "0030e1e4",
        "switchD_00bb0a0c::switchdataD_0030e1e4",
        "byte"
      ]
    ],
    [
      "00bb0720",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ],
    [
      "00bb0754",
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

- 旧版 [`00b44ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b44a44.md#insn-00b44ac4) · [`00b44afc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b44a44.md#insn-00b44afc) · [`00b44b30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b44a44.md#insn-00b44b30)

~~~diff
- 00b44ac4 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00b44ac4 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00b44ac4 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b44ac4 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00b44ac4 bytes 28b1889a
- 00b44afc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b44afc ["INT_ADD", "register:40f0:8", ["const:b44afc:8", "const:4:8"]]
- 00b44afc ["CALLIND", null, ["register:0:8"]]
- 00b44afc bytes 00013fd6
- 00b44b30 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b44b30 ["INT_ADD", "register:40f0:8", ["const:b44b30:8", "const:4:8"]]
- 00b44b30 ["CALLIND", null, ["register:0:8"]]
- 00b44b30 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ae4cc5490f2300e52a6f47488255a07"></a>

### [`00b44f5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b44f5c.md) → [`00bb0b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb0/00bb0b80.md) _ZNSt6__ndk17__sort4IRPFbPKN11flatbuffers9StructDefES4_EPPS2_EEjT0_SA_SA_SA_T_

採用 · 移動量 `+0x6bc24` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be01c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01c0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5ccc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ccc0.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 93.81% / 新版 93.81%

CFGの説明率　旧版 70.37% / 新版 65.52%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b44f5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b44f5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b44f60"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b44f5c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b44f60",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b44f64",
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
      "00bb0b80",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00bb0b84",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bb0b88",
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

- 旧版 [`00b44f5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b44f5c.md#insn-00b44f5c) · [`00b44f60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b44f5c.md#insn-00b44f60) · [`00b44f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b44f5c.md#insn-00b44f64)

~~~diff
- 00b44f5c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b44f5c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b44f5c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00b44f5c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b44f5c bytes f85fbca9
- 00b44f60 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b44f60 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b44f60 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b44f60 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b44f60 bytes f65701a9
- 00b44f64 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b44f64 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b44f64 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b44f64 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b44f64 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78b2ba0ddb3298f69a6df0999c3ec84f"></a>

### [`00b450e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b45/00b450e0.md) → [`00bb0d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb0/00bb0d04.md) FUN_00bb0d04

採用 · 移動量 `+0x6bc24` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b44a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b44a44.md) [`00b45344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b45/00b45344.md) · 呼出先 1件 [`00be01c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01c0.md)
- 新版 呼出元 2件 [`00bb0668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb0/00bb0668.md) [`00bb0f68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb0/00bb0f68.md) · 呼出先 1件 [`00c5ccc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ccc0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 98.48% / 新版 98.48%

CFGの説明率　旧版 69.23% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45164"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bb0d88"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b45164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b45/00b450e0.md#insn-00b45164) · [`00b45114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b45/00b450e0.md#insn-00b45114)
- 新版 [`00bb0d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb0/00bb0d04.md#insn-00bb0d88) · [`00bb0d38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb0/00bb0d04.md#insn-00bb0d38)

~~~diff
- 00b45164 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b45164 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00b45164 bytes 090300f9
+ 00bb0d88 ["COPY", "tmp:0:8", ["register:40c0:8"]]
+ 00bb0d88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00bb0d88 bytes 090300f9
- 00b45114 ["INT_ADD", "register:40f0:8", ["const:b45114:8", "const:4:8"]]
- 00b45114 ["CALL", null, ["callee:00c5ccc0:8"]]
+ 00bb0d38 ["INT_ADD", "register:40f0:8", ["const:bb0d38:8", "const:4:8"]]
+ 00bb0d38 ["CALL", null, ["callee:00c5ccc0:8"]]
- 00b45114 bytes 2b6c0294
+ 00bb0d38 bytes e2af0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-661dd4ef378dbfade6bd7e5ea417f4d4"></a>

### [`00b451e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b45/00b451e8.md) → [`00bb0e0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb0/00bb0e0c.md) _ZNSt6__ndk118__insertion_sort_3IRPFbPKN11flatbuffers9StructDefES4_EPPS2_EEvT0_SA_T_

採用 · 移動量 `+0x6bc24` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdfda0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfda0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5c800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c800.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 98.85% / 新版 98.85%

CFGの説明率　旧版 89.66% / 新版 92.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4524c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bb0e70"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b4524c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b45/00b451e8.md#insn-00b4524c) · [`00b45218`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b45/00b451e8.md#insn-00b45218)
- 新版 [`00bb0e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb0/00bb0e0c.md#insn-00bb0e70) · [`00bb0e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb0/00bb0e0c.md#insn-00bb0e3c)

~~~diff
- 00b4524c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b4524c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b4524c bytes 880200f9
+ 00bb0e70 ["COPY", "tmp:0:8", ["register:40a0:8"]]
+ 00bb0e70 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00bb0e70 bytes 880200f9
- 00b45218 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b45218 ["INT_ADD", "register:40f0:8", ["const:b45218:8", "const:4:8"]]
- 00b45218 ["CALLIND", null, ["register:0:8"]]
+ 00bb0e3c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00bb0e3c ["INT_ADD", "register:40f0:8", ["const:bb0e3c:8", "const:4:8"]]
+ 00bb0e3c ["CALLIND", null, ["register:0:8"]]
- 00b45218 bytes 20013fd6
+ 00bb0e3c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ae9a38ba40d7e46ab87ae094ab48299"></a>

### [`00b455f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b45/00b455f4.md) → [`00bb1218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb1/00bb1218.md) FUN_00bb1218

採用 · 移動量 `+0x6bc24` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b290d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b29/00b290d4.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md) [`00bdfc70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfc70.md)
- 新版 呼出元 1件 [`00b8dcb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8d/00b8dcb4.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md) [`00c5c640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c640.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 70.13% / 新版 70.13%

CFGの説明率　旧版 45.83% / 新版 68.75%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b455f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b455f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b455fc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b455f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b455fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b45600",
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
      "00bb121c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00bb1220",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00bb1224",
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

- 旧版 [`00b455f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b45/00b455f4.md#insn-00b455f8) · [`00b455fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b45/00b455f4.md#insn-00b455fc) · [`00b45600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b45/00b455f4.md#insn-00b45600)

~~~diff
- 00b455f8 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b455f8 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b455f8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b455f8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b455f8 bytes fa6704a9
- 00b455fc ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b455fc ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b455fc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b455fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b455fc bytes f85f05a9
- 00b45600 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b45600 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b45600 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b45600 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b45600 bytes f65706a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84b628a56bd4f5e39d7cc3c5753eccf8"></a>

### [`00b45c40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b45/00b45c40.md) → [`00bb1864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb1/00bb1864.md) _ZNSt6__ndk17__sort4IRPFbPKN11flatbuffers7EnumDefES4_EPPS2_EEjT0_SA_SA_SA_T_

採用 · 移動量 `+0x6bc24` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be01a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01a0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5cca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cca0.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 86.60% / 新版 86.60%

CFGの説明率　旧版 25.00% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45cbc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45cc0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45ce0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b45cd4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb1944"
      ]
    ],
    [
      "unmatched:00b45cd0",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00bb18f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb1944"
      ]
    ],
    [
      "00bb18f4",
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

- 旧版 [`00b45cbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b45/00b45c40.md#insn-00b45cbc) · [`00b45cc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b45/00b45c40.md#insn-00b45cc0) · [`00b45cd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b45/00b45c40.md#insn-00b45cd0)

~~~diff
- 00b45cbc ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b45cbc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b45cbc bytes 680200f9
- 00b45cc0 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b45cc0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00b45cc0 bytes c90200f9
- 00b45cd0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b45cd0 ["INT_ADD", "register:40f0:8", ["const:b45cd0:8", "const:4:8"]]
- 00b45cd0 ["CALLIND", null, ["register:0:8"]]
- 00b45cd0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ef7198c0828aaa69c5864a9104eabfe"></a>

### [`00b45dc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b45/00b45dc4.md) → [`00bb19e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb1/00bb19e8.md) FUN_00bb19e8

採用 · 移動量 `+0x6bc24` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b45728`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b45/00b45728.md) [`00b46028`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b46028.md) · 呼出先 1件 [`00be01a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01a0.md)
- 新版 呼出元 2件 [`00bb134c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb1/00bb134c.md) [`00bb1c4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb1/00bb1c4c.md) · 呼出先 1件 [`00c5cca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cca0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 84.85% / 新版 84.85%

CFGの説明率　旧版 18.75% / 新版 23.08%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45dc4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45dc8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45dc8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b45dc4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b45dc8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b45dcc",
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
      "00bb19e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00bb19ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00bb19f0",
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

- 旧版 [`00b45dc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b45/00b45dc4.md#insn-00b45dc4) · [`00b45dc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b45/00b45dc4.md#insn-00b45dc8) · [`00b45dcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b45/00b45dc4.md#insn-00b45dcc)

~~~diff
- 00b45dc4 ["COPY", "tmp:0:8", ["register:40c8:8"]]
- 00b45dc4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 00b45dc4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b45dc4 bytes f90f1bf8
- 00b45dc8 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b45dc8 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b45dc8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b45dc8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b45dc8 bytes f85f01a9
- 00b45dcc ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b45dcc ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b45dcc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b45dcc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b45dcc bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b3cdb35e61ed4de4958819887fbfe35"></a>

### [`00b46720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b46720.md) → [`00bb5084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5084.md) FUN_00bb5084

採用 · 移動量 `+0x6e964` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change` · `reordered`

- 旧版 呼出元 0件  · 呼出先 2件 [`00be01e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01e0.md) [`00be02a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be02a0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5cce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cce0.md) [`00c5cdb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cdb0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 60.00% / 新版 60.00%

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
      "site": "00b46740"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b46744"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bb50a4"
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
      "unmatched:00b46730",
      "READ",
      [
        "storage",
        "00c1b240",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b46740",
      "DATA",
      [
        "storage",
        "00c112a8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b46744",
      "DATA",
      [
        "storage",
        "00c112d0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bb5094",
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ],
    [
      "00bb50a4",
      "DATA",
      [
        "storage",
        "00c90ac0",
        null,
        "pointer"
      ]
    ],
    [
      "00bb50a8",
      "DATA",
      [
        "storage",
        "00c90ae8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b46720.md#insn-00b46740) · [`00b46744`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b46720.md#insn-00b46744)
- 新版 [`00bb50a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5084.md#insn-00bb50a4)

~~~diff
- 00b46740 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b46740 ["COPY", "tmp:1:8", ["register:4000:8"]]
- 00b46740 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:10:8"]]
- 00b46740 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b46740 bytes 090401f8
- 00b46744 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b46744 ["INT_ADD", "register:4098:8", ["register:4098:8", "const:b8:8"]]
- 00b46744 ["STORE", null, ["const:1b1:8", "register:4098:8", "tmp:0:8"]]
- 00b46744 bytes 688e0bf8
+ 00bb50a4 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00bb50a4 ["COPY", "tmp:1:8", ["register:4000:8"]]
+ 00bb50a4 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:10:8"]]
+ 00bb50a4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 00bb50a4 bytes 090401f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a1151e86cfb4c7ca433886ffb438b1e"></a>

### [`00b46b60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b46b60.md) → [`00bb228c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb2/00bb228c.md) _ZN11flatbuffers9DirExistsEPKc

採用 · 移動量 `+0x6b72c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change` · `reordered`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdca10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdca10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59460.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 76.92% / 新版 76.92%

CFGの説明率　旧版 16.67% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b46b64"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b46b64"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bb2290"
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
      "unmatched:00b46b64",
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
      "00bb2290",
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

- 旧版 [`00b46b64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b46b60.md#insn-00b46b64) · [`00b46b60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b46b60.md#insn-00b46b60)
- 新版 [`00bb2290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb2/00bb228c.md#insn-00bb2290)

~~~diff
- 00b46b64 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b46b64 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b46b64 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 00b46b64 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b46b64 bytes fd7b08a9
+ 00bb2290 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00bb2290 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00bb2290 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
+ 00bb2290 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00bb2290 bytes fd7b08a9
- 00b46b60 ["INT_SUB", "register:8:8", ["register:8:8", "const:90:8"]]
- 00b46b60 bytes ff4302d1
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f1cea587f8177c51047d48baabdda43"></a>

### [`00b46ec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b46ec0.md) → [`00bb2270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb2/00bb2270.md) _ZN11flatbuffers8LoadFileEPKcbPNSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE

採用 · 移動量 `+0x6b3b0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change` · `reordered`

- 旧版 呼出元 1件 [`00bdfab0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfab0.md) · 呼出先 1件 [`00b4675c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b4675c.md)
- 新版 呼出元 1件 [`00c5c460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c460.md) · 呼出先 1件 [`00bb22e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb2/00bb22e4.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b46ec4",
      "READ",
      [
        "storage",
        "00c247c8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b46ecc",
      "COMPUTED_JUMP",
      [
        "unresolved_target",
        "00b4675c"
      ]
    ]
  ],
  "added": [
    [
      "00bb2274",
      "READ",
      [
        "storage",
        "00ca42a8",
        null,
        "pointer"
      ]
    ],
    [
      "00bb227c",
      "COMPUTED_JUMP",
      [
        "unresolved_target",
        "00bb22e4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46ec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b46ec0.md#insn-00b46ec0) · [`00b46ec4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b46ec0.md#insn-00b46ec4) · [`00b46ec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b46ec0.md#insn-00b46ec8)

~~~diff
- 00b46ec0 ["COPY", "register:4040:8", ["const:c24000:8"]]
- 00b46ec0 bytes e80600d0
- 00b46ec4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:7c8:8"]]
- 00b46ec4 ["LOAD", "register:4018:8", ["const:1b1:8", "tmp:0:8"]]
- 00b46ec4 bytes 03e543f9
- 00b46ec8 ["INT_AND", "tmp:0:4", ["register:4008:4", "const:1:4"]]
- 00b46ec8 ["INT_ZEXT", "register:4008:8", ["tmp:0:4"]]
- 00b46ec8 bytes 21000012
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ce4ba651fdb8bc1852b2224c2966c91"></a>

### [`00b47194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47194.md) → [`00bb2ac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb2/00bb2ac0.md) FUN_00bb2ac0

採用 · 移動量 `+0x6b92c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00be01e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01e0.md) [`00be02a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be02a0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5cce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cce0.md) [`00c5cdb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cdb0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 73.33% / 新版 73.33%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b471b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b471b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bb2ae0"
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
      "00bb2ad0",
      "READ",
      [
        "storage",
        "00c1b0d0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b471b4",
      "DATA",
      [
        "storage",
        "00c114b0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b471b8",
      "DATA",
      [
        "storage",
        "00c114d8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bb2ad0",
      "READ",
      [
        "storage",
        "00c9aac0",
        null,
        "pointer"
      ]
    ],
    [
      "00bb2ae0",
      "DATA",
      [
        "storage",
        "00c90cc8",
        null,
        "pointer"
      ]
    ],
    [
      "00bb2ae4",
      "DATA",
      [
        "storage",
        "00c90cf0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b471b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47194.md#insn-00b471b4) · [`00b471b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47194.md#insn-00b471b8)
- 新版 [`00bb2ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb2/00bb2ac0.md#insn-00bb2ae0)

~~~diff
- 00b471b4 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b471b4 ["COPY", "tmp:1:8", ["register:4000:8"]]
- 00b471b4 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:8:8"]]
- 00b471b4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b471b4 bytes 098400f8
- 00b471b8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b471b8 ["INT_ADD", "register:4098:8", ["register:4098:8", "const:b0:8"]]
- 00b471b8 ["STORE", null, ["const:1b1:8", "register:4098:8", "tmp:0:8"]]
- 00b471b8 bytes 680e0bf8
+ 00bb2ae0 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00bb2ae0 ["COPY", "tmp:1:8", ["register:4000:8"]]
+ 00bb2ae0 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:8:8"]]
+ 00bb2ae0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 00bb2ae0 bytes 098400f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79c40af744ed0d38cdbd7c1bc9ff7bc9"></a>

### [`00b471d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b471d0.md) → [`00bb2afc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb2/00bb2afc.md) _ZN11flatbuffers14StripExtensionERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x6b92c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde730.md) [`00bde970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde970.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1b0.md) [`00c5b3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b3f0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 76.19% / 新版 76.19%

CFGの説明率　旧版 8.33% / 新版 12.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b471e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b471ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b471f0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b471f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb2b4c"
      ]
    ]
  ],
  "added": [
    [
      "00bb2b1c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb2b4c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b471e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b471d0.md#insn-00b471e8) · [`00b471ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b471d0.md#insn-00b471ec) · [`00b471f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b471d0.md#insn-00b471f0)

~~~diff
- 00b471e8 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b471e8 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b471e8 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b471e8 ["COPY", "register:4018:8", ["tmp:0:8"]]
- 00b471e8 bytes 6301899a
- 00b471ec ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b471ec ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00b471ec ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b471ec ["INT_ADD", "tmp:1:8", ["register:4008:8", "const:1:8"]]
- 00b471ec bytes 4815819a
- 00b471f0 ["INT_EQUAL", "tmp:0:1", ["register:4018:8", "const:0:8"]]
- 00b471f0 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00b471f0 bytes 830100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12896d835c38322e66a0e89b9931bf15"></a>

### [`00b47224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47224.md) → [`00bb2b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb2/00bb2b50.md) _ZN11flatbuffers12GetExtensionERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x6b92c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde740.md) [`00bde970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde970.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b1c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1c0.md) [`00c5b3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b3f0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 45.83% / 新版 45.83%

CFGの説明率　旧版 9.09% / 新版 12.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4723c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b47240"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b47244"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b47244",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb2ba4"
      ]
    ],
    [
      "unmatched:00b4727c",
      "PARAM",
      [
        "storage",
        "002967d9",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b47280",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b1c0"
      ]
    ]
  ],
  "added": [
    [
      "00bb2b70",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb2ba4"
      ]
    ],
    [
      "00bb2ba8",
      "PARAM",
      [
        "storage",
        "002a630e",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb2bac",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b1c0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4723c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47224.md#insn-00b4723c) · [`00b47240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47224.md#insn-00b47240) · [`00b47244`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47224.md#insn-00b47244)

~~~diff
- 00b4723c ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b4723c ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b4723c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b4723c ["COPY", "register:4040:8", ["tmp:0:8"]]
- 00b4723c bytes 6801899a
- 00b47240 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b47240 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00b47240 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b47240 ["INT_ADD", "tmp:1:8", ["register:4008:8", "const:1:8"]]
- 00b47240 bytes 4915819a
- 00b47244 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b47244 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00b47244 bytes a80100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2416292386be5fefac6b020d1548e423"></a>

### [`00b47284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47284.md) → [`00bb2bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb2/00bb2bb0.md) _ZN11flatbuffers9StripPathERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x6b92c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb180.md) [`00bde730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde730.md) [`00bde970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde970.md)
- 新版 呼出元 1件 [`00c5c480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c480.md) · 呼出先 3件 [`00c57bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bd0.md) [`00c5b1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1b0.md) [`00c5b3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b3f0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 88.10% / 新版 88.10%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b472b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b472b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bb2be0"
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
      "00bb2bfc",
      "PARAM",
      [
        "storage",
        "002987ed",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bb2bfc",
      "PARAM",
      [
        "storage",
        "002a85ab",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b472b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47284.md#insn-00b472b4) · [`00b472b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47284.md#insn-00b472b8)
- 新版 [`00bb2be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb2/00bb2bb0.md#insn-00bb2be0)

~~~diff
- 00b472b4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b472b4 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00b472b4 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b472b4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "const:1:8"]]
- 00b472b4 bytes 3715809a
- 00b472b8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b472b8 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b472b8 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b472b8 ["COPY", "register:40b0:8", ["tmp:0:8"]]
- 00b472b8 bytes 16018a9a
+ 00bb2be0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00bb2be0 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00bb2be0 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
+ 00bb2be0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "const:1:8"]]
+ 00bb2be0 bytes 3715809a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5899e0c6344ae0d1df3103564178531f"></a>

### [`00b476bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b476bc.md) → [`00bb31d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb3/00bb31d0.md) _ZN11flatbuffers15EnsureDirExistsERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x6bb14` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b476bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b476bc.md) · 呼出先 6件 [`00b476bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b476bc.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb180.md) [`00bdd400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd400.md)
- 新版 呼出元 1件 [`00bb31d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb3/00bb31d0.md) · 呼出先 6件 [`00bb31d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb3/00bb31d0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bd0.md) [`00c59e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59e50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 69.57% / 新版 69.57%

CFGの説明率　旧版 32.14% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b476c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b476c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b476c4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b476c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b476c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b476c8",
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
      "00bb31d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00bb31d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bb31dc",
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

- 旧版 [`00b476c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b476bc.md#insn-00b476c0) · [`00b476c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b476bc.md#insn-00b476c4) · [`00b476c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b476bc.md#insn-00b476c8)

~~~diff
- 00b476c0 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b476c0 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b476c0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b476c0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b476c0 bytes f85f02a9
- 00b476c4 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b476c4 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b476c4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b476c4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b476c4 bytes f65703a9
- 00b476c8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b476c8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b476c8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b476c8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b476c8 bytes f44f04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-efb8ebe4693effe8f53ae181335ec50c"></a>

### [`00b47ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47ab8.md) → [`00bb534c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb534c.md) FUN_00bb534c

採用 · 移動量 `+0x6d894` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change` · `reordered`

- 旧版 呼出元 0件  · 呼出先 2件 [`00be01e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01e0.md) [`00be02a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be02a0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5cce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cce0.md) [`00c5cdb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cdb0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 61.11% / 新版 61.11%

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
      "site": "00b47ae4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b47ae8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bb5378"
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
      "unmatched:00b47ad0",
      "READ",
      [
        "storage",
        "00c1b240",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b47ae4",
      "DATA",
      [
        "storage",
        "00c112a8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b47ae8",
      "DATA",
      [
        "storage",
        "00c112d0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bb5364",
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ],
    [
      "00bb5378",
      "DATA",
      [
        "storage",
        "00c90ac0",
        null,
        "pointer"
      ]
    ],
    [
      "00bb537c",
      "DATA",
      [
        "storage",
        "00c90ae8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47ae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47ab8.md#insn-00b47ae4) · [`00b47ae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47ab8.md#insn-00b47ae8)
- 新版 [`00bb5378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb534c.md#insn-00bb5378)

~~~diff
- 00b47ae4 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b47ae4 ["COPY", "tmp:1:8", ["register:4000:8"]]
- 00b47ae4 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:10:8"]]
- 00b47ae4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b47ae4 bytes 0a0401f8
- 00b47ae8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b47ae8 ["INT_ADD", "register:4098:8", ["register:4098:8", "const:b8:8"]]
- 00b47ae8 ["STORE", null, ["const:1b1:8", "register:4098:8", "tmp:0:8"]]
- 00b47ae8 bytes 688e0bf8
+ 00bb5378 ["COPY", "tmp:0:8", ["register:4050:8"]]
+ 00bb5378 ["COPY", "tmp:1:8", ["register:4000:8"]]
+ 00bb5378 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:10:8"]]
+ 00bb5378 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 00bb5378 bytes 0a0401f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fda317a3e822037d0a15c8a8d90bf05b"></a>

### [`00b47e44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47e44.md) → [`00bb5690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5690.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEE7seekoffExNS_8ios_base7seekdirEj

採用 · 移動量 `+0x6d84c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00b48678`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48678.md) [`00be02c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be02c0.md) [`00be02d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be02d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bb5ec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5ec4.md) [`00c5cde0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cde0.md) [`00c5cdf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cdf0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 85.42% / 新版 85.42%

CFGの説明率　旧版 47.62% / 新版 58.82%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b47e44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b47e44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b47e48"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b47e44",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b47e48",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b47e4c",
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
      "00bb5690",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bb5694",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bb5698",
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

- 旧版 [`00b47e44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47e44.md#insn-00b47e44) · [`00b47e48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47e44.md#insn-00b47e48) · [`00b47e4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47e44.md#insn-00b47e4c)

~~~diff
- 00b47e44 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b47e44 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b47e44 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b47e44 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b47e44 bytes f657bda9
- 00b47e48 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b47e48 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b47e48 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b47e48 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b47e48 bytes f44f01a9
- 00b47e4c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b47e4c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b47e4c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b47e4c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b47e4c bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ce4520a00dd0ce4573d44ca58e870b9"></a>

### [`00b47f04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47f04.md) → [`00bb5750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5750.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEE7seekposENS_4fposI9mbstate_tEEj

採用 · 移動量 `+0x6d84c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be02c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be02c0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5cde0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cde0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 96.43% / 新版 96.43%

CFGの説明率　旧版 66.67% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b47f68"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00bb57b4"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b47f68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47f04.md#insn-00b47f68) · [`00b47f30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47f04.md#insn-00b47f30)
- 新版 [`00bb57b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5750.md#insn-00bb57b4) · [`00bb577c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5750.md#insn-00bb577c)

~~~diff
- 00b47f68 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b47f68 ["RETURN", null, ["register:0:8"]]
- 00b47f68 bytes c0035fd6
+ 00bb57b4 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00bb57b4 ["RETURN", null, ["register:0:8"]]
+ 00bb57b4 bytes c0035fd6
- 00b47f30 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b47f30 ["INT_ADD", "register:40f0:8", ["const:b47f30:8", "const:4:8"]]
- 00b47f30 ["CALLIND", null, ["register:0:8"]]
+ 00bb577c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bb577c ["INT_ADD", "register:40f0:8", ["const:bb577c:8", "const:4:8"]]
+ 00bb577c ["CALLIND", null, ["register:0:8"]]
- 00b47f30 bytes 00013fd6
+ 00bb577c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d16b215195a165986a3ecafd0ebb5f1"></a>

### [`00b483e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b483e0.md) → [`00bb5c2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5c2c.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEE9pbackfailEi

採用 · 移動量 `+0x6d84c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 63.64% / 新版 70.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b483f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bb5c40"
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
      "unmatched:00b483f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb5c74"
      ]
    ]
  ],
  "added": [
    [
      "00bb5c40",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb5c74"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b483f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b483e0.md#insn-00b483f4) · [`00b483e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b483e0.md#insn-00b483e4)
- 新版 [`00bb5c40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5c2c.md#insn-00bb5c40) · [`00bb5c30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5c2c.md#insn-00bb5c30)

~~~diff
- 00b483f4 ["CBRANCH", null, ["local:b7:8", "register:102:1"]]
- 00b483f4 bytes a2010054
+ 00bb5c40 ["CBRANCH", null, ["local:b6:8", "register:102:1"]]
+ 00bb5c40 bytes a2010054
- 00b483e4 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00b483e4 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00bb5c30 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
+ 00bb5c30 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00b483e4 bytes 290200b4
+ 00bb5c30 bytes 290200b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6fde3c84a3945d1316c41b52c607c8ee"></a>

### [`00b48b94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48b94.md) → [`00bb627c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb627c.md) FUN_00bb627c

採用 · 移動量 `+0x6d6e8` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change` · `reordered`

- 旧版 呼出元 1件 [`00b4aa9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4aa9c.md) · 呼出先 2件 [`00bddc80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc80.md) [`00bdde00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde00.md)
- 新版 呼出元 1件 [`00bb87b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb87b4.md) · 呼出先 2件 [`00c5a6d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a6d0.md) [`00c5a860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a860.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 31.25% / 新版 31.25%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b48b94"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b48b98"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b48b98"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b48b94",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b48b98",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b48ba4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5a860"
      ]
    ]
  ],
  "added": [
    [
      "00bb627c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bb6280",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bb628c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5a860"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48b94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48b94.md#insn-00b48b94) · [`00b48b98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48b94.md#insn-00b48b98) · [`00b48ba4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48b94.md#insn-00b48ba4)

~~~diff
- 00b48b94 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b48b94 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b48b94 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b48b94 bytes f30f1ef8
- 00b48b98 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b48b98 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b48b98 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b48b98 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b48b98 bytes fd7b01a9
- 00b48ba4 ["INT_ADD", "register:40f0:8", ["const:b48ba4:8", "const:4:8"]]
- 00b48ba4 ["CALL", null, ["callee:00c5a860:8"]]
- 00b48ba4 bytes 97540294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8b7ce516a6ec851a7b2a33cb1eca263"></a>

### [`00b48bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48bd4.md) → [`00bb62bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb62bc.md) FUN_00bb62bc

採用 · 移動量 `+0x6d6e8` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b4aa9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4aa9c.md) · 呼出先 2件 [`00bdde00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde00.md) [`00be0470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0470.md)
- 新版 呼出元 1件 [`00bb87b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb87b4.md) · 呼出先 2件 [`00c5a860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a860.md) [`00c5d040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d040.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 69.23% / 新版 69.23%

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
      "site": "00b48bf8"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00bb62e0"
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
      "00bb62d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b48bfc"
      ]
    ],
    [
      "unmatched:00b48bfc",
      "DATA",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b48c04",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5d040"
      ]
    ]
  ],
  "added": [
    [
      "00bb62d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb62e4"
      ]
    ],
    [
      "00bb62e4",
      "DATA",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bb62ec",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5d040"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48bf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48bd4.md#insn-00b48bf8) · [`00b48be4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48bd4.md#insn-00b48be4)
- 新版 [`00bb62e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb62bc.md#insn-00bb62e0) · [`00bb62cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb62bc.md#insn-00bb62cc)

~~~diff
- 00b48bf8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b48bf8 ["RETURN", null, ["register:0:8"]]
- 00b48bf8 bytes c0035fd6
+ 00bb62e0 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00bb62e0 ["RETURN", null, ["register:0:8"]]
+ 00bb62e0 bytes c0035fd6
- 00b48be4 ["INT_ADD", "register:40f0:8", ["const:b48be4:8", "const:4:8"]]
- 00b48be4 ["CALL", null, ["callee:00c5a860:8"]]
+ 00bb62cc ["INT_ADD", "register:40f0:8", ["const:bb62cc:8", "const:4:8"]]
+ 00bb62cc ["CALL", null, ["callee:00c5a860:8"]]
- 00b48be4 bytes 87540294
+ 00bb62cc bytes 65910294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8541cfe1babcc10de477d780e06e2c1"></a>

### [`00b48c08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48c08.md) → [`00bb62f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb62f0.md) _ZN8firebase9messaging8internal36RegisterTerminateOnDefaultAppDestroyEv

採用 · 移動量 `+0x6d6e8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0450.md) · 呼出先 5件 [`00b4950c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b4950c.md) [`00bddd70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd70.md) [`00bddd90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd90.md) [`00bddda0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddda0.md) [`00bdde00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde00.md)
- 新版 呼出元 1件 [`00c5d020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d020.md) · 呼出先 5件 [`00bb7224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7224.md) [`00c5a7d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7d0.md) [`00c5a7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7f0.md) [`00c5a800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a800.md) [`00c5a860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a860.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 31.25% / 新版 31.25%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b48c08"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b48c08"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bb62f0"
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
      "unmatched:00b48c08",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b48c14",
      "PARAM",
      [
        "storage",
        "002f8894",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b48c18",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5a7d0"
      ]
    ]
  ],
  "added": [
    [
      "00bb62f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bb62fc",
      "PARAM",
      [
        "storage",
        "0030e69f",
        null,
        "string"
      ]
    ],
    [
      "00bb6300",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5a7d0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48c08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48c08.md#insn-00b48c08) · [`00b48c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48c08.md#insn-00b48c18) · [`00b48c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48c08.md#insn-00b48c24)

~~~diff
- 00b48c08 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b48c08 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b48c08 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 00b48c08 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b48c08 bytes fd7bbfa9
- 00b48c18 ["INT_ADD", "register:40f0:8", ["const:b48c18:8", "const:4:8"]]
- 00b48c18 ["CALL", null, ["callee:00c5a7d0:8"]]
- 00b48c18 bytes 56540294
- 00b48c24 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b48c24 ["RETURN", null, ["register:0:8"]]
- 00b48c24 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c6a7f83762ade800593e6f43af372071"></a>

### [`00b4926c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b4926c.md) → [`00bb6d5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6d5c.md) _ZN8firebase9messaging20PollableListenerImpl11PollMessageEPNS0_7MessageE

採用 · 移動量 `+0x6daf0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be03a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be03a0.md) · 呼出先 5件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00be0420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0420.md) [`00be0430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0430.md)
- 新版 呼出元 1件 [`00c5cf00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cf00.md) · 呼出先 5件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5cff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cff0.md) [`00c5d000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d000.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 16.98% / 新版 16.98%

CFGの説明率　旧版 20.00% / 新版 28.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4926c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4926c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b49270"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4926c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b49270",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b49280",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5a600"
      ]
    ]
  ],
  "added": [
    [
      "00bb6d5c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bb6d60",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bb6d70",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5a600"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4926c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b4926c.md#insn-00b4926c) · [`00b49270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b4926c.md#insn-00b49270) · [`00b49280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b4926c.md#insn-00b49280)

~~~diff
- 00b4926c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b4926c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b4926c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b4926c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b4926c bytes f44fbea9
- 00b49270 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b49270 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b49270 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b49270 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b49270 bytes fd7b01a9
- 00b49280 ["INT_ADD", "register:40f0:8", ["const:b49280:8", "const:4:8"]]
- 00b49280 ["CALL", null, ["callee:00c5a600:8"]]
- 00b49280 bytes 68520294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ef24eedb0ab70753a750110e7a58d9a"></a>

### [`00b493b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b493b4.md) → [`00bb6ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6ea4.md) _ZN8firebase9messaging20PollableListenerImpl21PollRegistrationTokenEPNSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE

採用 · 移動量 `+0x6daf0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be03c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be03c0.md) · 呼出先 3件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bde230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde230.md)
- 新版 呼出元 1件 [`00c5cf40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cf40.md) · 呼出先 3件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5acb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5acb0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 76.47% / 新版 86.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b493f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b493fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bb6ee8"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b493f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b493b4.md#insn-00b493f8) · [`00b493fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b493b4.md#insn-00b493fc)
- 新版 [`00bb6ee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb6ea4.md#insn-00bb6ee8)

~~~diff
- 00b493f8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b493f8 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00b493f8 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b493f8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:1:8"]]
- 00b493f8 bytes 2115959a
- 00b493fc ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b493fc ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b493fc ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b493fc ["COPY", "register:4010:8", ["tmp:0:8"]]
- 00b493fc bytes 62018a9a
+ 00bb6ee8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00bb6ee8 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00bb6ee8 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
+ 00bb6ee8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:1:8"]]
+ 00bb6ee8 bytes 2115959a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4da9d41b0671219c8b9fe2ccfcefa63a"></a>

### [`00b49650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b49650.md) → [`00bb7368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7368.md) _ZN8firebase9messaging7MessageD2Ev

採用 · 移動量 `+0x6dd18` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0420.md) · 呼出先 3件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be0360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0360.md)
- 新版 呼出元 1件 [`00c5cff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cff0.md) · 呼出先 3件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ced0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ced0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 96.30% / 新版 96.30%

CFGの説明率　旧版 91.49% / 新版 95.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b49650"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b49650"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b49654"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b49650",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b49654",
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
      "00bb7368",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bb736c",
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

- 旧版 [`00b49650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b49650.md#insn-00b49650) · [`00b49654`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b49650.md#insn-00b49654)
- 新版 [`00bb7368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7368.md#insn-00bb7368)

~~~diff
- 00b49650 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b49650 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b49650 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b49650 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b49650 bytes f44fbea9
- 00b49654 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b49654 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b49654 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b49654 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b49654 bytes fd7b01a9
+ 00bb7368 ["COPY", "tmp:0:8", ["register:40a0:8"]]
+ 00bb7368 ["COPY", "tmp:1:8", ["register:4098:8"]]
+ 00bb7368 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00bb7368 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00bb7368 bytes f44fbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c6fcabe55c4be9e086e270e23b5de6b"></a>

### [`00b4996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b4996c.md) → [`00bb7684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7684.md) _ZN8firebase9messaging7MessageC2ERKS1_

採用 · 移動量 `+0x6dd18` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0410.md) · 呼出先 1件 [`00be0430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0430.md)
- 新版 呼出元 1件 [`00c5cfe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cfe0.md) · 呼出先 1件 [`00c5d000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d000.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 94.12% / 新版 94.12%

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
      "site": "00b499d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b499d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b499d8"
    }
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b499d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b4996c.md#insn-00b499d4) · [`00b499d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b4996c.md#insn-00b499d8)
- 新版 [`00bb76ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7684.md#insn-00bb76ec)

~~~diff
- 00b499d4 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:10:8"]]
- 00b499d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b499d4 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00b499d4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5000:16"]]
- 00b499d4 bytes 008300ad
- 00b499d8 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b499d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b499d8 bytes 0003803d
+ 00bb76ec ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:10:8"]]
+ 00bb76ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
+ 00bb76ec ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
+ 00bb76ec ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5000:16"]]
+ 00bb76ec bytes 008300ad
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9862e1a9afede2ae572d478317412225"></a>

### [`00b49d40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b49d40.md) → [`00bb7a58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7a58.md) _ZN8firebase9messaging12NotificationC2ERKS1_

採用 · 移動量 `+0x6dd18` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0350.md) · 呼出先 1件 [`00be0370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0370.md)
- 新版 呼出元 1件 [`00c5cec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cec0.md) · 呼出先 1件 [`00c5cee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cee0.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 95.24% / 新版 95.24%

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
      "site": "00b49d90"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00bb7aa8"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b49d90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b49d40.md#insn-00b49d90) · [`00b49d80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b49d40.md#insn-00b49d80)
- 新版 [`00bb7aa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7a58.md#insn-00bb7aa8) · [`00bb7a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7a58.md#insn-00bb7a98)

~~~diff
- 00b49d90 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b49d90 ["RETURN", null, ["register:0:8"]]
- 00b49d90 bytes c0035fd6
+ 00bb7aa8 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00bb7aa8 ["RETURN", null, ["register:0:8"]]
+ 00bb7aa8 bytes c0035fd6
- 00b49d80 ["INT_ADD", "register:40f0:8", ["const:b49d80:8", "const:4:8"]]
- 00b49d80 ["CALL", null, ["callee:00c5cee0:8"]]
+ 00bb7a98 ["INT_ADD", "register:40f0:8", ["const:bb7a98:8", "const:4:8"]]
+ 00bb7a98 ["CALL", null, ["callee:00c5cee0:8"]]
- 00b49d80 bytes 7c590294
+ 00bb7a98 bytes 12950294
~~~


<a id="compare-3d1e28242bbcb5638fc6f1f04f1ef215"></a>

### [`00b49f30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b49f30.md) → [`00bb7c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7c48.md) _ZNSt6__ndk16vectorIhNS_9allocatorIhEEE6assignIPhEENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_constructibleIhNS_15iterator_

採用 · 移動量 `+0x6dd18` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be04f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be04f0.md) · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bddeb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddeb0.md)
- 新版 呼出元 1件 [`00c5d0c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d0c0.md) · 呼出先 5件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5a910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a910.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 88.16% / 新版 88.16%

CFGの説明率　旧版 58.62% / 新版 73.91%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b49f30"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b49f30"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b49f34"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b49f30",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b49f34",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b49f38",
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
      "00bb7c48",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00bb7c4c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00bb7c50",
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

- 旧版 [`00b49f30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b49f30.md#insn-00b49f30) · [`00b49f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b49f30.md#insn-00b49f34) · [`00b49f38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b49f30.md#insn-00b49f38)

~~~diff
- 00b49f30 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b49f30 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b49f30 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 00b49f30 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b49f30 bytes fa67bba9
- 00b49f34 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b49f34 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b49f34 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b49f34 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b49f34 bytes f85f01a9
- 00b49f38 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b49f38 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b49f38 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b49f38 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b49f38 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-029b16ecc78764bbc7977d2d30e2bd2d"></a>

### [`00b4a060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4a060.md) → [`00bb7d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7d78.md) _ZN8firebase9messaging12NotificationaSERKS1_

採用 · 移動量 `+0x6dd18` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0370.md) · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bde230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde230.md) [`00bde730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde730.md) [`00be0090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0090.md)
- 新版 呼出元 1件 [`00c5cee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cee0.md) · 呼出先 5件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5acb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5acb0.md) [`00c5b1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1b0.md) [`00c5cc30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cc30.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 25.00% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4a094"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4a098"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4a124"
    }
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4a060.md#insn-00b4a094) · [`00b4a098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4a060.md#insn-00b4a098) · [`00b4a124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4a060.md#insn-00b4a124)

~~~diff
- 00b4a094 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b4a094 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00b4a094 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b4a094 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "const:1:8"]]
- 00b4a094 bytes 2115949a
- 00b4a098 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b4a098 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b4a098 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b4a098 ["COPY", "register:4010:8", ["tmp:0:8"]]
- 00b4a098 bytes 62018a9a
- 00b4a124 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b4a124 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b4a124 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b4a124 ["COPY", "register:4008:8", ["tmp:0:8"]]
- 00b4a124 bytes 61018a9a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf26a70b15b64fe3eed232f3fa6f2beb"></a>

### [`00b4a248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4a248.md) → [`00bb7f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7f60.md) _ZNSt6__ndk15dequeIN8firebase9messaging7MessageENS_9allocatorIS3_EEE19__add_back_capacityEv

採用 · 移動量 `+0x6dd18` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be04e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be04e0.md) · 呼出先 9件 [`00ae04c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae04c0.md) [`00b4a45c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4a45c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00c5d0b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d0b0.md) · 呼出先 9件 [`00b3fe98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fe98.md) [`00bb8174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8174.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 80.91% / 新版 80.91%

CFGの説明率　旧版 50.00% / 新版 53.85%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4a24c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4a24c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4a250"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4a24c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4a250",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4a254",
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
      "00bb7f64",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bb7f68",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bb7f6c",
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

- 旧版 [`00b4a24c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4a248.md#insn-00b4a24c) · [`00b4a250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4a248.md#insn-00b4a250) · [`00b4a254`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4a248.md#insn-00b4a254)

~~~diff
- 00b4a24c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b4a24c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b4a24c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b4a24c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4a24c bytes f65704a9
- 00b4a250 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b4a250 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b4a250 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b4a250 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4a250 bytes f44f05a9
- 00b4a254 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b4a254 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b4a254 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b4a254 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4a254 bytes fd7b06a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-34f6b4372444037d39c682da3157201b"></a>

### [`00b4a45c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4a45c.md) → [`00bb8174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8174.md) FUN_00bb8174

採用 · 移動量 `+0x6dd18` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b4a248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4a248.md) · 呼出先 4件 [`00ae04c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae04c0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`00bb7f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7f60.md) · 呼出先 4件 [`00b3fe98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fe98.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 96.25% / 新版 96.25%

CFGの説明率　旧版 69.57% / 新版 80.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4a510"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bb8228"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4a598"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4a510",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb8260"
      ]
    ],
    [
      "unmatched:00b4a594",
      "PARAM",
      [
        "storage",
        "002987f0",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b4a598",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00ae04c0"
      ]
    ]
  ],
  "added": [
    [
      "00bb8228",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb8260"
      ]
    ],
    [
      "00bb82ac",
      "PARAM",
      [
        "storage",
        "002a85ae",
        null,
        "string"
      ]
    ],
    [
      "00bb82b0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00b3fe98"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4a45c.md#insn-00b4a510) · [`00b4a598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4a45c.md#insn-00b4a598)
- 新版 [`00bb8228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8174.md#insn-00bb8228)

~~~diff
- 00b4a510 ["CBRANCH", null, ["local:b12:8", "register:101:1"]]
- 00b4a510 bytes c0010054
- 00b4a598 ["INT_ADD", "register:40f0:8", ["const:b4a598:8", "const:4:8"]]
- 00b4a598 ["CALL", null, ["ram:ae04c0:8"]]
- 00b4a598 bytes ca57fe97
+ 00bb8228 ["CBRANCH", null, ["local:b10:8", "register:101:1"]]
+ 00bb8228 bytes c0010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29702d10848957bca18ef81e5df988dd"></a>

### [`00b4a59c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4a59c.md) → [`00bb82b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb82b4.md) _ZNSt6__ndk114__split_bufferIPN8firebase9messaging7MessageENS_9allocatorIS4_EEE9push_backEOS4_

採用 · 移動量 `+0x6dd18` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be04b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be04b0.md) · 呼出先 4件 [`00ae04c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae04c0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`00c5d080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d080.md) · 呼出先 4件 [`00b3fe98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fe98.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 23.33% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4a6a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bb83c0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4a5d0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4a5d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb8338"
      ]
    ],
    [
      "00bb8348",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b4a6d0"
      ]
    ],
    [
      "unmatched:00b4a6d4",
      "PARAM",
      [
        "storage",
        "002987f0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bb82e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb8338"
      ]
    ],
    [
      "00bb8348",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb83e8"
      ]
    ],
    [
      "00bb83ec",
      "PARAM",
      [
        "storage",
        "002a85ae",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a5d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4a59c.md#insn-00b4a5d0) · [`00b4a6a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4a59c.md#insn-00b4a6a8) · [`00b4a6cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4a59c.md#insn-00b4a6cc)

~~~diff
- 00b4a5d0 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b4a5d0 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00b4a5d0 ["CBRANCH", null, ["local:b9:8", "tmp:1:1"]]
- 00b4a5d0 bytes 89020054
- 00b4a6a8 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b4a6a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b4a6a8 bytes 080300f9
- 00b4a6cc ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b4a6cc ["RETURN", null, ["register:0:8"]]
- 00b4a6cc bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-592a7d867798ea26d0e6898f08852807"></a>

### [`00b4a6dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4a6dc.md) → [`00bb83f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb83f4.md) _ZNSt6__ndk114__split_bufferIPN8firebase9messaging7MessageENS_9allocatorIS4_EEE10push_frontEOS4_

採用 · 移動量 `+0x6dd18` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be04a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be04a0.md) · 呼出先 4件 [`00ae04c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae04c0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`00c5d070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d070.md) · 呼出先 4件 [`00b3fe98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fe98.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 47.83% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4a758"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4a758"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bb8470"
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
      "unmatched:00b4a814",
      "PARAM",
      [
        "storage",
        "002987f0",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b4a818",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00ae04c0"
      ]
    ]
  ],
  "added": [
    [
      "00bb852c",
      "PARAM",
      [
        "storage",
        "002a85ae",
        null,
        "string"
      ]
    ],
    [
      "00bb8530",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00b3fe98"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a758`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4a6dc.md#insn-00b4a758) · [`00b4a818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4a6dc.md#insn-00b4a818)
- 新版 [`00bb8470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb83f4.md#insn-00bb8470)

~~~diff
- 00b4a758 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b4a758 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00b4a758 ["INT_ADD", "tmp:2:8", ["register:4098:8", "const:8:8"]]
- 00b4a758 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4a758 bytes 76a200a9
- 00b4a818 ["INT_ADD", "register:40f0:8", ["const:b4a818:8", "const:4:8"]]
- 00b4a818 ["CALL", null, ["ram:ae04c0:8"]]
- 00b4a818 bytes 2a57fe97
+ 00bb8470 ["COPY", "tmp:0:8", ["register:40b0:8"]]
+ 00bb8470 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 00bb8470 ["INT_ADD", "tmp:2:8", ["register:4098:8", "const:8:8"]]
+ 00bb8470 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00bb8470 bytes 76a200a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ebe400e963316786d92b29e17cbd725"></a>

### [`00b4ab14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4ab14.md) → [`00bb8838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8838.md) _ZN8firebase9messaging18firebase_messaging19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9alloc

採用 · 移動量 `+0x6dd24` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 25.00% / 新版 25.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4ab40"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bb8864"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4ab28"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4ab24",
      "READ",
      [
        "storage",
        "010a0ff8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b4ab28",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b4ab44"
      ]
    ],
    [
      "unmatched:00b4ab34",
      "PARAM",
      [
        "storage",
        "002aa0e2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bb8848",
      "READ",
      [
        "storage",
        "01125ea8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb884c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb8868"
      ]
    ],
    [
      "00bb8858",
      "PARAM",
      [
        "storage",
        "002bae5e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ab28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4ab14.md#insn-00b4ab28) · [`00b4ab38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4ab14.md#insn-00b4ab38) · [`00b4ab40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4ab14.md#insn-00b4ab40)

~~~diff
- 00b4ab28 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b4ab28 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b4ab28 bytes e80000b5
- 00b4ab38 ["INT_ADD", "register:40f0:8", ["const:b4ab38:8", "const:4:8"]]
- 00b4ab38 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b4ab38 bytes 564d0294
- 00b4ab40 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ff8:8"]]
- 00b4ab40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4ab40 bytes 60fe07f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9aab1a99e67f87913912c469270bb80"></a>

### [`00b4ac1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4ac1c.md) → [`00bb8940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8940.md) _ZN8firebase9messaging18firebase_messaging8GetClassEv

採用 · 移動量 `+0x6dd24` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

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
      "site": "00b4ac24"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00bb8948"
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
      "unmatched:00b4ac20",
      "READ",
      [
        "storage",
        "010a0ff8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bb8944",
      "READ",
      [
        "storage",
        "01125ea8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ac24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4ac1c.md#insn-00b4ac24) · [`00b4ac1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4ac1c.md#insn-00b4ac1c)
- 新版 [`00bb8948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8940.md#insn-00bb8948)

~~~diff
- 00b4ac24 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b4ac24 ["RETURN", null, ["register:0:8"]]
- 00b4ac24 bytes c0035fd6
+ 00bb8948 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00bb8948 ["RETURN", null, ["register:0:8"]]
+ 00bb8948 bytes c0035fd6
- 00b4ac1c ["COPY", "register:4040:8", ["const:10a0000:8"]]
- 00b4ac1c bytes a82a00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a89043b897e45f972cb9e0dc5fc6493"></a>

### [`00b4ae20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4ae20.md) → [`00bb8b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8b44.md) _ZN8firebase9messaging18firebase_messaging10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x6dd24` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 46.67% / 新版 46.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4ae40"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bb8b64"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4ae58"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bb8b58",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b4ae44"
      ]
    ],
    [
      "unmatched:00b4ae3c",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b4ae40",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ac00"
      ]
    ]
  ],
  "added": [
    [
      "00bb8b58",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb8b68"
      ]
    ],
    [
      "00bb8b60",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bb8b64",
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

- 旧版 [`00b4ae40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4ae20.md#insn-00b4ae40) · [`00b4ae58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4ae20.md#insn-00b4ae58)
- 新版 [`00bb8b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8b44.md#insn-00bb8b64)

~~~diff
- 00b4ae40 ["INT_ADD", "register:40f0:8", ["const:b4ae40:8", "const:4:8"]]
- 00b4ae40 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b4ae40 bytes d04c0294
- 00b4ae58 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b4ae58 ["RETURN", null, ["register:0:8"]]
- 00b4ae58 bytes c0035fd6
+ 00bb8b64 ["INT_ADD", "register:40f0:8", ["const:bb8b64:8", "const:4:8"]]
+ 00bb8b64 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bb8b64 bytes 27880294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-276f0132a4ad7ccecda35856902877a2"></a>

### [`00b4ae9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4ae9c.md) → [`00bb8bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8bc0.md) _ZN8firebase9messaging27registration_intent_service19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileEN

採用 · 移動量 `+0x6dd24` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4ae9c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4aea0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4aea0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4ae9c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4aea0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4aeac",
      "READ",
      [
        "storage",
        "010a1058",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bb8bc0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bb8bc4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bb8bd0",
      "READ",
      [
        "storage",
        "01125f18",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ae9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4ae9c.md#insn-00b4ae9c) · [`00b4aea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4ae9c.md#insn-00b4aea0) · [`00b4aeb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4ae9c.md#insn-00b4aeb0)

~~~diff
- 00b4ae9c ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b4ae9c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b4ae9c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b4ae9c bytes f30f1ef8
- 00b4aea0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b4aea0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b4aea0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b4aea0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4aea0 bytes fd7b01a9
- 00b4aeb0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b4aeb0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b4aeb0 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76ccd7a8521d170d5a00978fb20c9da1"></a>

### [`00b4afdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4afdc.md) → [`00bb8d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8d00.md) _ZN8firebase9messaging27registration_intent_service12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x6dd24` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 42.86% / 新版 42.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4b018"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4b038"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bb8d3c"
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
      "00bb8d14",
      "READ",
      [
        "storage",
        "010a1058",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b4aff4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b4b03c"
      ]
    ],
    [
      "00bb8d20",
      "READ",
      [
        "storage",
        "010a1060",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bb8d14",
      "READ",
      [
        "storage",
        "01125f18",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb8d18",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb8d60"
      ]
    ],
    [
      "00bb8d20",
      "READ",
      [
        "storage",
        "01125f20",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4aff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4afdc.md#insn-00b4aff4) · [`00b4b014`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4afdc.md#insn-00b4b014) · [`00b4b018`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4afdc.md#insn-00b4b018)

~~~diff
- 00b4aff4 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b4aff4 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00b4aff4 bytes 410200b4
- 00b4b014 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4b014 ["INT_ADD", "register:40f0:8", ["const:b4b014:8", "const:4:8"]]
- 00b4b014 ["CALLIND", null, ["register:0:8"]]
- 00b4b014 bytes 00013fd6
- 00b4b018 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4b018 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4b018 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:60:8"]]
- 00b4b018 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4b018 bytes bf820139
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f1a418b3c35b10d08a2ca09fc75b878"></a>

### [`00b4b0bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4b/00b4b0bc.md) → [`00bb8de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8de0.md) _ZN8firebase9messaging27registration_intent_service11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x6dd24` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 46.67% / 新版 46.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4b0dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bb8e00"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4b0f4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bb8df4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b4b0e0"
      ]
    ],
    [
      "unmatched:00b4b0d8",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b4b0dc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ac00"
      ]
    ]
  ],
  "added": [
    [
      "00bb8df4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb8e04"
      ]
    ],
    [
      "00bb8dfc",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bb8e00",
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

- 旧版 [`00b4b0dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4b/00b4b0bc.md#insn-00b4b0dc) · [`00b4b0f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4b/00b4b0bc.md#insn-00b4b0f4)
- 新版 [`00bb8e00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8de0.md#insn-00bb8e00)

~~~diff
- 00b4b0dc ["INT_ADD", "register:40f0:8", ["const:b4b0dc:8", "const:4:8"]]
- 00b4b0dc ["CALL", null, ["callee:00c5ac00:8"]]
- 00b4b0dc bytes 294c0294
- 00b4b0f4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b4b0f4 ["RETURN", null, ["register:0:8"]]
- 00b4b0f4 bytes c0035fd6
+ 00bb8e00 ["INT_ADD", "register:40f0:8", ["const:bb8e00:8", "const:4:8"]]
+ 00bb8e00 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bb8e00 bytes 80870294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5cc26517875cac1f382a235996d61ae8"></a>

### [`00b4b168`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4b/00b4b168.md) → [`00bb8e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8e8c.md) _ZN8firebase9messaging27registration_intent_service10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x6dd24` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 46.67% / 新版 46.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4b188"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bb8eac"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4b1a0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bb8ea0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b4b18c"
      ]
    ],
    [
      "unmatched:00b4b184",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b4b188",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ac00"
      ]
    ]
  ],
  "added": [
    [
      "00bb8ea0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb8eb0"
      ]
    ],
    [
      "00bb8ea8",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bb8eac",
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

- 旧版 [`00b4b188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4b/00b4b168.md#insn-00b4b188) · [`00b4b1a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4b/00b4b168.md#insn-00b4b1a0)
- 新版 [`00bb8eac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8e8c.md#insn-00bb8eac)

~~~diff
- 00b4b188 ["INT_ADD", "register:40f0:8", ["const:b4b188:8", "const:4:8"]]
- 00b4b188 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b4b188 bytes fe4b0294
- 00b4b1a0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b4b1a0 ["RETURN", null, ["register:0:8"]]
- 00b4b1a0 bytes c0035fd6
+ 00bb8eac ["INT_ADD", "register:40f0:8", ["const:bb8eac:8", "const:4:8"]]
+ 00bb8eac ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bb8eac bytes 55870294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-238391ecbfb52fbaa3802438e9aabcca"></a>

### [`00b4b1a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4b/00b4b1a4.md) → [`00bb8ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8ec8.md) _ZN8firebase9messaging26illegal_argument_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS

採用 · 移動量 `+0x6dd24` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 25.00% / 新版 25.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4b1d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bb8ef4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4b1b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4b1b4",
      "READ",
      [
        "storage",
        "010a1078",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b4b1b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b4b1d4"
      ]
    ],
    [
      "unmatched:00b4b1c4",
      "PARAM",
      [
        "storage",
        "00295455",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bb8ed8",
      "READ",
      [
        "storage",
        "01125f38",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb8edc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb8ef8"
      ]
    ],
    [
      "00bb8ee8",
      "PARAM",
      [
        "storage",
        "002a4e38",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b1b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4b/00b4b1a4.md#insn-00b4b1b8) · [`00b4b1c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4b/00b4b1a4.md#insn-00b4b1c8) · [`00b4b1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4b/00b4b1a4.md#insn-00b4b1d0)

~~~diff
- 00b4b1b8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b4b1b8 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b4b1b8 bytes e80000b5
- 00b4b1c8 ["INT_ADD", "register:40f0:8", ["const:b4b1c8:8", "const:4:8"]]
- 00b4b1c8 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b4b1c8 bytes b24b0294
- 00b4b1d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:78:8"]]
- 00b4b1d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b1d0 bytes 603e00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd357ecc7d809a1404aa278acc6521cb"></a>

### [`00b4b2b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4b/00b4b2b8.md) → [`00bb8fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8fdc.md) _ZN8firebase9messaging26illegal_argument_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x6dd24` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 81.48% / 新版 81.48%

CFGの説明率　旧版 50.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4b310"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bb9034"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4b2f8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bb8ff0",
      "READ",
      [
        "storage",
        "010a1080",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b4b2ec",
      "READ",
      [
        "storage",
        "010a1078",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b4b310",
      "WRITE",
      [
        "storage",
        "010a1080",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bb8ff0",
      "READ",
      [
        "storage",
        "01125f40",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb9010",
      "READ",
      [
        "storage",
        "01125f38",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9034",
      "WRITE",
      [
        "storage",
        "01125f40",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b2f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4b/00b4b2b8.md#insn-00b4b2f8) · [`00b4b310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4b/00b4b2b8.md#insn-00b4b310)
- 新版 [`00bb901c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8fdc.md#insn-00bb901c)

~~~diff
- 00b4b2f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4b2f8 ["INT_ADD", "register:40f0:8", ["const:b4b2f8:8", "const:4:8"]]
- 00b4b2f8 ["CALLIND", null, ["register:0:8"]]
- 00b4b2f8 bytes 00013fd6
- 00b4b310 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4b310 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:80:8"]]
- 00b4b310 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4b310 bytes a0020239
+ 00bb901c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bb901c ["INT_ADD", "register:40f0:8", ["const:bb901c:8", "const:4:8"]]
+ 00bb901c ["CALLIND", null, ["register:0:8"]]
+ 00bb901c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d5b5ee183115286b3bdbef04d662a29"></a>

### [`00b4b324`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4b/00b4b324.md) → [`00bb9048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb9/00bb9048.md) _ZN8firebase9messaging26illegal_argument_exception12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x6dd24` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 64.29% / 新版 64.29%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4b360"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4b380"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bb9084"
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
      "00bb905c",
      "READ",
      [
        "storage",
        "010a1078",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b4b33c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb90a8"
      ]
    ],
    [
      "00bb9068",
      "READ",
      [
        "storage",
        "010a1080",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bb905c",
      "READ",
      [
        "storage",
        "01125f38",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9060",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb90a8"
      ]
    ],
    [
      "00bb9068",
      "READ",
      [
        "storage",
        "01125f40",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b33c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4b/00b4b324.md#insn-00b4b33c) · [`00b4b360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4b/00b4b324.md#insn-00b4b360) · [`00b4b368`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4b/00b4b324.md#insn-00b4b368)

~~~diff
- 00b4b33c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b4b33c ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b4b33c bytes 410200b4
- 00b4b360 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4b360 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4b360 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:80:8"]]
- 00b4b360 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4b360 bytes bf020239
- 00b4b368 ["INT_ADD", "register:40f0:8", ["const:b4b368:8", "const:4:8"]]
- 00b4b368 ["CALL", null, ["callee:00c5ab60:8"]]
- 00b4b368 bytes 5e4b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b378eaec94dc107d97d7604e787ba04c"></a>

### [`00b4b404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4b/00b4b404.md) → [`00bb9128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb9/00bb9128.md) _ZN8firebase9messaging26illegal_argument_exception11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x6dd24` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 26.67% / 新版 26.67%

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
      "site": "00b4b404"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4b408"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4b408"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4b404",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4b408",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bb913c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b4b428"
      ]
    ]
  ],
  "added": [
    [
      "00bb9128",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bb912c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bb913c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb914c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4b/00b4b404.md#insn-00b4b404) · [`00b4b408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4b/00b4b404.md#insn-00b4b408) · [`00b4b424`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4b/00b4b404.md#insn-00b4b424)

~~~diff
- 00b4b404 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b4b404 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b4b404 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b4b404 bytes f30f1ef8
- 00b4b408 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b4b408 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b4b408 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b4b408 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4b408 bytes fd7b01a9
- 00b4b424 ["INT_ADD", "register:40f0:8", ["const:b4b424:8", "const:4:8"]]
- 00b4b424 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b4b424 bytes 574b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6edef351c48e287a33a1716c7a6fbf96"></a>

### [`00b4ea90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4e/00b4ea90.md) → [`00bbcf70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbcf70.md) FUN_00bbcf70

採用 · 移動量 `+0x6e4e0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change` · `reordered`

- 旧版 呼出元 1件 [`00b4cdec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4c/00b4cdec.md) · 呼出先 4件 [`00b4e948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4e/00b4e948.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00be0400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0400.md)
- 新版 呼出元 1件 [`00bbab28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bba/00bbab28.md) · 呼出先 4件 [`00bbcd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbcd98.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5cfb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cfb0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 57.14% / 新版 72.73%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4eabc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bbcf9c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4eaa8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bbcf80",
      "READ",
      [
        "storage",
        "010a10b0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b4eaa8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bbcfac"
      ]
    ],
    [
      "unmatched:00b4eabc",
      "WRITE",
      [
        "storage",
        "010a1148",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bbcf80",
      "READ",
      [
        "storage",
        "01125f70",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbcf88",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bbcfac"
      ]
    ],
    [
      "00bbcf9c",
      "WRITE",
      [
        "storage",
        "01126008",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4eaa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4e/00b4ea90.md#insn-00b4eaa8) · [`00b4eabc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4e/00b4ea90.md#insn-00b4eabc) · [`00b4eac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4e/00b4ea90.md#insn-00b4eac0)

~~~diff
- 00b4eaa8 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 00b4eaa8 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b4eaa8 bytes 340100b4
- 00b4eabc ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00b4eabc ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:148:8"]]
- 00b4eabc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4eabc bytes 09210539
- 00b4eac0 ["INT_ADD", "register:40f0:8", ["const:b4eac0:8", "const:4:8"]]
- 00b4eac0 ["CALL", null, ["ram:b4e948:8"]]
- 00b4eac0 bytes a2ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-460ee850aa42673e82faf4396669503b"></a>

### [`00b4ffa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4f/00b4ffa4.md) → [`00bbe488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbe/00bbe488.md) _ZNK8firebase9messaging8internal13MessageReader20ConsumeTokenReceivedEPKN3com6google8firebase9messaging3cpp23SerializedTokenReceivedE

採用 · 移動量 `+0x6e4e4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 73.68% / 新版 73.68%

CFGの説明率　旧版 57.14% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b4ffa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4f/00b4ffa4.md#insn-00b4ffa4) · [`00b4ffa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4f/00b4ffa4.md#insn-00b4ffa8) · [`00b4ffac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4f/00b4ffa4.md#insn-00b4ffac)

~~~diff
- 00b4ffa4 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00b4ffa4 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
- 00b4ffa4 ["INT_SEXT", "register:4040:8", ["tmp:1:4"]]
- 00b4ffa4 bytes 280080b9
- 00b4ffa8 ["INT_SUB", "register:4040:8", ["register:4008:8", "register:4040:8"]]
- 00b4ffa8 bytes 280008cb
- 00b4ffac ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b4ffac ["LOAD", "tmp:1:2", ["const:1b1:8", "tmp:0:8"]]
- 00b4ffac ["INT_ZEXT", "register:4048:8", ["tmp:1:2"]]
- 00b4ffac bytes 09014079
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af2e8c1094964c16e35c735a905b5471"></a>

### [`00b4fff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4f/00b4fff0.md) → [`00bbe594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbe/00bbe594.md) _ZNSt6__ndk16vectorIhNS_9allocatorIhEEE6assignIN11flatbuffers14VectorIteratorIhhPKhjEEEENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valu

採用 · 移動量 `+0x6e5a4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0580.md) · 呼出先 3件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bddeb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddeb0.md)
- 新版 呼出元 1件 [`00c5d170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d170.md) · 呼出先 3件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a910.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 98.03% / 新版 98.03%

CFGの説明率　旧版 87.32% / 新版 88.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5005c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b500b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bbe600"
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
      "unmatched:00b500b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bbe6cc"
      ]
    ]
  ],
  "added": [
    [
      "00bbe658",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bbe6cc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5005c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4f/00b4fff0.md#insn-00b5005c) · [`00b500b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4f/00b4fff0.md#insn-00b500b4)
- 新版 [`00bbe600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbe/00bbe594.md#insn-00bbe600)

~~~diff
- 00b5005c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b5005c ["COPY", "tmp:1:8", ["register:40b0:8"]]
- 00b5005c ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b5005c ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00b5005c bytes d632889a
- 00b500b4 ["CBRANCH", null, ["local:b22:8", "register:101:1"]]
- 00b500b4 bytes a0030054
+ 00bbe600 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00bbe600 ["COPY", "tmp:1:8", ["register:40b0:8"]]
+ 00bbe600 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
+ 00bbe600 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 00bbe600 bytes d632889a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5456b40f521497d4bac0539f59c324c6"></a>

### [`00b53350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53350.md) → [`00bc1cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1cc4.md) _ZN8firebase13remote_config8internal12config_value11GetMethodIdENS2_6MethodE

採用 · 移動量 `+0x6e974` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 33.33% / 新版 33.33%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53364"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bc1cd8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53370"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b53364",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b53374"
      ]
    ],
    [
      "unmatched:00b5336c",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b53370",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ac00"
      ]
    ]
  ],
  "added": [
    [
      "00bc1cd8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc1ce8"
      ]
    ],
    [
      "00bc1ce0",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bc1ce4",
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

- 旧版 [`00b53364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53350.md#insn-00b53364) · [`00b53370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53350.md#insn-00b53370) · [`00b53388`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53350.md#insn-00b53388)

~~~diff
- 00b53364 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00b53364 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b53364 bytes 8b000054
- 00b53370 ["INT_ADD", "register:40f0:8", ["const:b53370:8", "const:4:8"]]
- 00b53370 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b53370 bytes 842b0294
- 00b53388 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b53388 ["RETURN", null, ["register:0:8"]]
- 00b53388 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3b91ae88755db1b76c5795bf37bf248"></a>

### [`00b533fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b533fc.md) → [`00bc1d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1d70.md) _ZN8firebase13remote_config8internal12config_value10GetFieldIdENS2_5FieldE

採用 · 移動量 `+0x6e974` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 46.67% / 新版 46.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5341c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bc1d90"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53434"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc1d84",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b53420"
      ]
    ],
    [
      "unmatched:00b53418",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b5341c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ac00"
      ]
    ]
  ],
  "added": [
    [
      "00bc1d84",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc1d94"
      ]
    ],
    [
      "00bc1d8c",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bc1d90",
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

- 旧版 [`00b5341c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b533fc.md#insn-00b5341c) · [`00b53434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b533fc.md#insn-00b53434)
- 新版 [`00bc1d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1d70.md#insn-00bc1d90)

~~~diff
- 00b5341c ["INT_ADD", "register:40f0:8", ["const:b5341c:8", "const:4:8"]]
- 00b5341c ["CALL", null, ["callee:00c5ac00:8"]]
- 00b5341c bytes 592b0294
- 00b53434 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b53434 ["RETURN", null, ["register:0:8"]]
- 00b53434 bytes c0035fd6
+ 00bc1d90 ["INT_ADD", "register:40f0:8", ["const:bc1d90:8", "const:4:8"]]
+ 00bc1d90 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bc1d90 bytes 9c630294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5612ab7e41fbc132d31439a0231e6ff"></a>

### [`00b53540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53540.md) → [`00bc1eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1eb4.md) _ZN8firebase13remote_config8internal11config_info8GetClassEv

採用 · 移動量 `+0x6e974` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53548"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00bc1ebc"
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
      "unmatched:00b53544",
      "READ",
      [
        "storage",
        "010a12a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc1eb8",
      "READ",
      [
        "storage",
        "01126168",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53548`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53540.md#insn-00b53548) · [`00b53540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53540.md#insn-00b53540)
- 新版 [`00bc1ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1eb4.md#insn-00bc1ebc)

~~~diff
- 00b53548 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b53548 ["RETURN", null, ["register:0:8"]]
- 00b53548 bytes c0035fd6
+ 00bc1ebc ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00bc1ebc ["RETURN", null, ["register:0:8"]]
+ 00bc1ebc bytes c0035fd6
- 00b53540 ["COPY", "register:4040:8", ["const:10a1000:8"]]
- 00b53540 bytes 682a00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4cb6dfb12e22484258a9c5a75e62fc0d"></a>

### [`00b53744`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53744.md) → [`00bc20b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc20b8.md) _ZN8firebase13remote_config8internal11config_info10GetFieldIdENS2_5FieldE

採用 · 移動量 `+0x6e974` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 46.67% / 新版 46.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53764"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bc20d8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5377c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc20cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b53768"
      ]
    ],
    [
      "unmatched:00b53760",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b53764",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ac00"
      ]
    ]
  ],
  "added": [
    [
      "00bc20cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc20dc"
      ]
    ],
    [
      "00bc20d4",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bc20d8",
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

- 旧版 [`00b53764`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53744.md#insn-00b53764) · [`00b5377c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53744.md#insn-00b5377c)
- 新版 [`00bc20d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc20b8.md#insn-00bc20d8)

~~~diff
- 00b53764 ["INT_ADD", "register:40f0:8", ["const:b53764:8", "const:4:8"]]
- 00b53764 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b53764 bytes 872a0294
- 00b5377c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b5377c ["RETURN", null, ["register:0:8"]]
- 00b5377c bytes c0035fd6
+ 00bc20d8 ["INT_ADD", "register:40f0:8", ["const:bc20d8:8", "const:4:8"]]
+ 00bc20d8 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bc20d8 bytes ca620294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9230704f2061f5c5b09e88e11b453077"></a>

### [`00b53800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53800.md) → [`00bc2174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2174.md) _ZN8firebase13remote_config8internal15config_settings10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x6e974` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 52.94% / 新版 52.94%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53830"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc21a4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53814"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc2184",
      "READ",
      [
        "storage",
        "010a12d0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b53814",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc21a8"
      ]
    ],
    [
      "unmatched:00b53820",
      "PARAM",
      [
        "storage",
        "002a7f3e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc2184",
      "READ",
      [
        "storage",
        "01126198",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2188",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc21a8"
      ]
    ],
    [
      "00bc2194",
      "PARAM",
      [
        "storage",
        "002b8be0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53814`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53800.md#insn-00b53814) · [`00b53828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53800.md#insn-00b53828) · [`00b53830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53800.md#insn-00b53830)

~~~diff
- 00b53814 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b53814 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b53814 bytes 080100b5
- 00b53828 ["INT_ADD", "register:40f0:8", ["const:b53828:8", "const:4:8"]]
- 00b53828 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b53828 bytes 1a2a0294
- 00b53830 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2d0:8"]]
- 00b53830 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53830 bytes 606a01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e1ac8826062ca76fb03a91b38c30df6"></a>

### [`00b53bdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53bdc.md) → [`00bc2550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2550.md) _ZN8firebase13remote_config8internal23config_settings_builder15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x6e974` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 81.48% / 新版 81.48%

CFGの説明率　旧版 40.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53c34"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bc25a8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53c1c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bc2564",
      "READ",
      [
        "storage",
        "010a1300",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b53c10",
      "READ",
      [
        "storage",
        "010a12f8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b53c34",
      "WRITE",
      [
        "storage",
        "010a1300",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bc2564",
      "READ",
      [
        "storage",
        "011261c8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc2584",
      "READ",
      [
        "storage",
        "011261c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc25a8",
      "WRITE",
      [
        "storage",
        "011261c8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53c1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53bdc.md#insn-00b53c1c) · [`00b53c34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53bdc.md#insn-00b53c34)
- 新版 [`00bc2590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2550.md#insn-00bc2590)

~~~diff
- 00b53c1c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b53c1c ["INT_ADD", "register:40f0:8", ["const:b53c1c:8", "const:4:8"]]
- 00b53c1c ["CALLIND", null, ["register:0:8"]]
- 00b53c1c bytes 00013fd6
- 00b53c34 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b53c34 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:300:8"]]
- 00b53c34 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b53c34 bytes a0020c39
+ 00bc2590 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bc2590 ["INT_ADD", "register:40f0:8", ["const:bc2590:8", "const:4:8"]]
+ 00bc2590 ["CALLIND", null, ["register:0:8"]]
+ 00bc2590 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bac3c3c76bd6939e9d0edca8cc83478d"></a>

### [`00b53d28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53d28.md) → [`00bc269c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc269c.md) _ZN8firebase13remote_config8internal23config_settings_builder11GetMethodIdENS2_6MethodE

採用 · 移動量 `+0x6e974` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 26.67% / 新版 26.67%

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
      "site": "00b53d28"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53d2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53d2c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b53d28",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b53d2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bc26b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b53d4c"
      ]
    ]
  ],
  "added": [
    [
      "00bc269c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bc26a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bc26b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc26c0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53d28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53d28.md#insn-00b53d28) · [`00b53d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53d28.md#insn-00b53d2c) · [`00b53d48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53d28.md#insn-00b53d48)

~~~diff
- 00b53d28 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b53d28 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b53d28 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b53d28 bytes f30f1ef8
- 00b53d2c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b53d2c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b53d2c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b53d2c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b53d2c bytes fd7b01a9
- 00b53d48 ["INT_ADD", "register:40f0:8", ["const:b53d48:8", "const:4:8"]]
- 00b53d48 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b53d48 bytes 0e290294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ddd860621ffd4d06ae20950a84013b7"></a>

### [`00b53dd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53dd4.md) → [`00bc2748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc2/00bc2748.md) _ZN8firebase13remote_config8internal23config_settings_builder10GetFieldIdENS2_5FieldE

採用 · 移動量 `+0x6e974` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 33.33% / 新版 33.33%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53de8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bc275c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b53df4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b53de8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b53df8"
      ]
    ],
    [
      "unmatched:00b53df0",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b53df4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ac00"
      ]
    ]
  ],
  "added": [
    [
      "00bc275c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bc276c"
      ]
    ],
    [
      "00bc2764",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bc2768",
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

- 旧版 [`00b53de8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53dd4.md#insn-00b53de8) · [`00b53df4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53dd4.md#insn-00b53df4) · [`00b53e0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53dd4.md#insn-00b53e0c)

~~~diff
- 00b53de8 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00b53de8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b53de8 bytes 8b000054
- 00b53df4 ["INT_ADD", "register:40f0:8", ["const:b53df4:8", "const:4:8"]]
- 00b53df4 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b53df4 bytes e3280294
- 00b53e0c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b53e0c ["RETURN", null, ["register:0:8"]]
- 00b53e0c bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

