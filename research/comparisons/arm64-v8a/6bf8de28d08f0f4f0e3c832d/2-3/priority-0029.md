# v16.0.2 → v16.0.3 · 最優先の変更候補 (29)

[一覧の目次](README.md)

<a id="compare-2d71196f7488ffec443d29c03e76f6d4"></a>

### [`00639880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00639/00639880.md) → [`00639c30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00639/00639c30.md) FUN_00639c30

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00639650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00639/00639650.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00639a00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00639/00639a00.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 81.40% / 新版 81.40%

CFGの説明率　旧版 25.00% / 新版 20.69%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006398c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006398c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00639918"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006398b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00639d3c"
      ]
    ],
    [
      "unmatched:00639930",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00639c6c"
      ]
    ]
  ],
  "added": [
    [
      "00639c60",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00639d3c"
      ]
    ],
    [
      "00639ce0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00639c6c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006398b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00639/00639880.md#insn-006398b0) · [`006398c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00639/00639880.md#insn-006398c4) · [`006398c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00639/00639880.md#insn-006398c8)

~~~diff
- 006398b0 ["CBRANCH", null, ["local:b15:8", "register:101:1"]]
- 006398b0 bytes e0060054
- 006398c4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:10:8"]]
- 006398c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 006398c4 bytes 2a0900f9
- 006398c8 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 006398c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 006398c8 bytes 2001803d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2a364260836e8a38a30139acd83e198"></a>

### [`006399d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00639/006399d8.md) → [`00639d88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00639/00639d88.md) FUN_00639d88

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 97.50% / 新版 97.50%

CFGの説明率　旧版 45.45% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "006399fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00639dac"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "006399fc"
      ],
      [
        "FALL_THROUGH",
        "00639dac"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00639da8",
      "incomplete_value": true,
      "site": "00639db4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:40a8:8"
              ],
              [
                "live",
                "register:40a0:8"
              ]
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
      "definition_site": null,
      "incomplete_value": true,
      "site": "00639a04",
      "value": [
        "live",
        "register:101:1"
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
      "unmatched:006399fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00639e00"
      ]
    ]
  ],
  "added": [
    [
      "00639dac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00639e00"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006399fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00639/006399d8.md#insn-006399fc) · [`006399f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00639/006399d8.md#insn-006399f0)
- 新版 [`00639dac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00639/00639d88.md#insn-00639dac) · [`00639da0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00639/00639d88.md#insn-00639da0)

~~~diff
- 006399fc ["CBRANCH", null, ["local:b14:8", "register:101:1"]]
- 006399fc bytes a0020054
+ 00639dac ["CBRANCH", null, ["local:b12:8", "register:101:1"]]
+ 00639dac bytes a0020054
- 006399f0 ["BRANCH", null, ["local:b3:8"]]
+ 00639da0 ["BRANCH", null, ["local:b4:8"]]
- 006399f0 bytes 02000014
+ 00639da0 bytes 02000014
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1dc3505262ed0fb95d49faee10bcbff"></a>

### [`00639a8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00639/00639a8c.md) → [`00639e3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00639/00639e3c.md) FUN_00639e3c

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00637890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00637/00637890.md) · 呼出先 3件 [`00494650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494650.md) [`00639b34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00639/00639b34.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00637c40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00637/00637c40.md) · 呼出先 3件 [`00494970`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494970.md) [`00639ee4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00639/00639ee4.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 31.58% / 新版 26.09%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00639a8c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00639a8c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00639a90"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00639a8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00639a90",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00639a9c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00639ee4"
      ]
    ]
  ],
  "added": [
    [
      "00639e3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00639e40",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00639e4c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00639ee4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00639a8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00639/00639a8c.md#insn-00639a8c) · [`00639a90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00639/00639a8c.md#insn-00639a90) · [`00639a9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00639/00639a8c.md#insn-00639a9c)

~~~diff
- 00639a8c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00639a8c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00639a8c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00639a8c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00639a8c bytes fd7bbea9
- 00639a90 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00639a90 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00639a90 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00639a90 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00639a90 bytes f44f01a9
- 00639a9c ["INT_ADD", "register:40f0:8", ["const:639a9c:8", "const:4:8"]]
- 00639a9c ["CALL", null, ["callee:00639ee4:8"]]
- 00639a9c bytes 26000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d08af510e1d8cee0373ceeb7a47719f"></a>

### [`00639b34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00639/00639b34.md) → [`00639ee4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00639/00639ee4.md) FUN_00639ee4

採用 · 移動量 `+0x3b0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00639a8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00639/00639a8c.md) [`00b766d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b76/00b766d8.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 2件 [`00639e3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00639/00639e3c.md) [`00b776cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b77/00b776cc.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment

命令の説明率　旧版 70.77% / 新版 70.77%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_branch_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00639b70"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00639b74"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00639b8c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00639bc8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00639f28"
      ]
    ]
  ],
  "added": [
    [
      "00639f78",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00639f28"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00639b70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00639/00639b34.md#insn-00639b70) · [`00639b74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00639/00639b34.md#insn-00639b74) · [`00639b8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00639/00639b34.md#insn-00639b8c)

~~~diff
- 00639b70 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00639b70 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00639b70 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00639b70 ["INT_ADD", "tmp:1:8", ["register:4008:8", "const:1:8"]]
- 00639b70 bytes 3415819a
- 00639b74 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00639b74 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00639b74 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00639b74 ["COPY", "register:40b0:8", ["tmp:0:8"]]
- 00639b74 bytes 16018a9a
- 00639b8c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00639b8c ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00639b8c ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00639b8c ["COPY", "register:40c8:8", ["tmp:0:8"]]
- 00639b8c bytes 39018a9a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14155321dc3c23817a2d5a95906a71fb"></a>

### [`00639d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00639/00639d00.md) → [`0063a0b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063a/0063a0b0.md) FUN_0063a0b0

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call, call_count, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 86.96% / 新版 86.96%

CFGの説明率　旧版 16.67% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0063a0c8",
      "incomplete_value": false,
      "site": "0063a0cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:7c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00639d18",
      "incomplete_value": false,
      "site": "00639d1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:7f0:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00639d40"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "0063a0f0"
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
      "0063a0cc",
      "DATA",
      [
        "storage",
        "00c737f0",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00639d40",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "0063a0cc",
      "DATA",
      [
        "storage",
        "00c747c0",
        null,
        "undefined *"
      ]
    ],
    [
      "0063a0f0",
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

- 旧版 [`00639d40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00639/00639d00.md#insn-00639d40) · [`00639d14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00639/00639d00.md#insn-00639d14)
- 新版 [`0063a0f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063a/0063a0b0.md#insn-0063a0f0) · [`0063a0c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063a/0063a0b0.md#insn-0063a0c4)

~~~diff
- 00639d40 ["COPY", "register:0:8", ["register:4040:8"]]
- 00639d40 ["INT_ADD", "register:40f0:8", ["const:639d40:8", "const:4:8"]]
- 00639d40 ["CALLIND", null, ["register:0:8"]]
- 00639d40 bytes 00013fd6
+ 0063a0f0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0063a0f0 ["INT_ADD", "register:40f0:8", ["const:63a0f0:8", "const:4:8"]]
+ 0063a0f0 ["CALLIND", null, ["register:0:8"]]
+ 0063a0f0 bytes 00013fd6
- 00639d14 ["COPY", "register:4040:8", ["const:c73000:8"]]
+ 0063a0c4 ["COPY", "register:4040:8", ["const:c74000:8"]]
- 00639d14 bytes c83100d0
+ 0063a0c4 bytes c83100d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-477c5bb848d06b7c9b4a37a853492b8f"></a>

### [`00639d5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00639/00639d5c.md) → [`0063a10c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063a/0063a10c.md) FUN_0063a10c

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00639d80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00639d80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00639d84"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00639d80",
      "DATA",
      [
        "storage",
        "00c737f0",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00639d88",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0063a150"
      ]
    ]
  ],
  "added": [
    [
      "0063a130",
      "DATA",
      [
        "storage",
        "00c747c0",
        null,
        "undefined *"
      ]
    ],
    [
      "0063a138",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0063a150"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00639d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00639/00639d5c.md#insn-00639d70) · [`00639d80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00639/00639d5c.md#insn-00639d80) · [`00639d84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00639/00639d5c.md#insn-00639d84)
- 新版 [`0063a120`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063a/0063a10c.md#insn-0063a120)

~~~diff
- 00639d70 ["INT_ADD", "register:40f0:8", ["const:639d70:8", "const:4:8"]]
- 00639d70 ["CALL", null, ["callee:00c58f30:8"]]
+ 0063a120 ["INT_ADD", "register:40f0:8", ["const:63a120:8", "const:4:8"]]
+ 0063a120 ["CALL", null, ["callee:00c58f30:8"]]
- 00639d70 bytes 7c781894
+ 0063a120 bytes 847b1894
- 00639d80 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00639d80 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00639d80 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00639d80 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00639d80 bytes 092800a9
- 00639d84 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:10:8"]]
- 00639d84 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00639d84 bytes 080800f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0977804e253df357a4d60d98073abb5"></a>

### [`00639dac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00639/00639dac.md) → [`0063a15c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063a/0063a15c.md) FUN_0063a15c

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 53.85% / 新版 53.85%

CFGの説明率　旧版 25.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 2件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00639db8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00639db8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00639dbc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00639db8",
      "DATA",
      [
        "storage",
        "00c737f0",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00639dc0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0063a18c"
      ]
    ]
  ],
  "added": [
    [
      "0063a168",
      "DATA",
      [
        "storage",
        "00c747c0",
        null,
        "undefined *"
      ]
    ],
    [
      "0063a170",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0063a18c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00639db8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00639/00639dac.md#insn-00639db8) · [`00639dbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00639/00639dac.md#insn-00639dbc) · [`00639dc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00639/00639dac.md#insn-00639dc0)

~~~diff
- 00639db8 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00639db8 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00639db8 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 00639db8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00639db8 bytes 292800a9
- 00639dbc ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:10:8"]]
- 00639dbc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00639dbc bytes 280800f9
- 00639dc0 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00639dc0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00639dc0 bytes e80000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c17ab8400cad8eb56cda89030393b75"></a>

### [`00639f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00639/00639f70.md) → [`0063a320`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063a/0063a320.md) FUN_0063a320

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0063a338",
      "incomplete_value": false,
      "site": "0063a33c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:840:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00639f88",
      "incomplete_value": false,
      "site": "00639f8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:870:8"
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
      "0063a33c",
      "DATA",
      [
        "storage",
        "00c73870",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0063a33c",
      "DATA",
      [
        "storage",
        "00c74840",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00639f84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00639/00639f70.md#insn-00639f84) · [`00639f88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00639/00639f70.md#insn-00639f88) · [`00639f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00639/00639f70.md#insn-00639f9c)
- 新版 [`0063a334`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063a/0063a320.md#insn-0063a334) · [`0063a338`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063a/0063a320.md#insn-0063a338) · [`0063a34c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063a/0063a320.md#insn-0063a34c)

~~~diff
- 00639f84 ["COPY", "register:4040:8", ["const:c73000:8"]]
+ 0063a334 ["COPY", "register:4040:8", ["const:c74000:8"]]
- 00639f84 bytes c83100d0
+ 0063a334 bytes c83100d0
- 00639f88 ["COPY", "tmp:0:8", ["const:870:8"]]
- 00639f88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00639f88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00639f88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0063a338 ["COPY", "tmp:0:8", ["const:840:8"]]
+ 0063a338 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0063a338 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0063a338 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00639f88 bytes 08c12191
+ 0063a338 bytes 08012191
- 00639f9c ["INT_ADD", "register:40f0:8", ["const:639f9c:8", "const:4:8"]]
- 00639f9c ["CALL", null, ["callee:00c54d90:8"]]
+ 0063a34c ["INT_ADD", "register:40f0:8", ["const:63a34c:8", "const:4:8"]]
+ 0063a34c ["CALL", null, ["callee:00c54d90:8"]]
- 00639f9c bytes 81671894
+ 0063a34c bytes 916a1894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4662b10e4caaaf4cf39d5b38938c32ef"></a>

### [`00639fe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00639/00639fe8.md) → [`0063a398`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063a/0063a398.md) FUN_0063a398

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0063a3b0",
      "incomplete_value": false,
      "site": "0063a3b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:840:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0063a000",
      "incomplete_value": false,
      "site": "0063a004",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:870:8"
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
      "0063a3b4",
      "DATA",
      [
        "storage",
        "00c73870",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0063a3b4",
      "DATA",
      [
        "storage",
        "00c74840",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00639ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00639/00639fe8.md#insn-00639ffc) · [`0063a000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00639/00639fe8.md#insn-0063a000) · [`0063a014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00639/00639fe8.md#insn-0063a014)
- 新版 [`0063a3ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063a/0063a398.md#insn-0063a3ac) · [`0063a3b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063a/0063a398.md#insn-0063a3b0) · [`0063a3c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063a/0063a398.md#insn-0063a3c4)

~~~diff
- 00639ffc ["COPY", "register:4040:8", ["const:c73000:8"]]
+ 0063a3ac ["COPY", "register:4040:8", ["const:c74000:8"]]
- 00639ffc bytes c83100d0
+ 0063a3ac bytes c83100d0
- 0063a000 ["COPY", "tmp:0:8", ["const:870:8"]]
- 0063a000 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0063a000 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0063a000 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0063a3b0 ["COPY", "tmp:0:8", ["const:840:8"]]
+ 0063a3b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0063a3b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0063a3b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0063a000 bytes 08c12191
+ 0063a3b0 bytes 08012191
- 0063a014 ["INT_ADD", "register:40f0:8", ["const:63a014:8", "const:4:8"]]
- 0063a014 ["CALL", null, ["callee:00c54d90:8"]]
+ 0063a3c4 ["INT_ADD", "register:40f0:8", ["const:63a3c4:8", "const:4:8"]]
+ 0063a3c4 ["CALL", null, ["callee:00c54d90:8"]]
- 0063a014 bytes 63671894
+ 0063a3c4 bytes 736a1894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dbeb0d39bb5a3a2d286386282c6b85c6"></a>

### [`0063a0f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063a/0063a0f4.md) → [`0063a4a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063a/0063a4a4.md) FUN_0063a4a4

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0063a4c4",
      "incomplete_value": false,
      "site": "0063a4c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:840:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0063a114",
      "incomplete_value": false,
      "site": "0063a114",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:870:8"
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
      "0063a4c4",
      "DATA",
      [
        "storage",
        "00c73870",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0063a4c4",
      "DATA",
      [
        "storage",
        "00c74840",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0063a104`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063a/0063a0f4.md#insn-0063a104) · [`0063a108`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063a/0063a0f4.md#insn-0063a108) · [`0063a110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063a/0063a0f4.md#insn-0063a110)
- 新版 [`0063a4b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063a/0063a4a4.md#insn-0063a4b4) · [`0063a4b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063a/0063a4a4.md#insn-0063a4b8)

~~~diff
- 0063a104 ["COPY", "register:4048:8", ["const:c73000:8"]]
+ 0063a4b4 ["COPY", "register:4048:8", ["const:c74000:8"]]
- 0063a104 bytes c93100b0
+ 0063a4b4 bytes c93100d0
- 0063a108 ["COPY", "tmp:0:8", ["const:870:8"]]
- 0063a108 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0063a108 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0063a108 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0063a4b8 ["COPY", "tmp:0:8", ["const:840:8"]]
+ 0063a4b8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0063a4b8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0063a4b8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0063a108 bytes 29c12191
+ 0063a4b8 bytes 29012191
- 0063a110 ["COPY", "register:40a0:8", ["register:4000:8"]]
- 0063a110 bytes f40300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-34986ce5ec731868ea05b33f4c455587"></a>

### [`0063a240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063a/0063a240.md) → [`0063a5f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063a/0063a5f0.md) FUN_0063a5f0

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 9件 [`00481470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00481/00481470.md) [`0048243c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00482/0048243c.md) [`00482578`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00482/00482578.md) [`00482b4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00482/00482b4c.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00481790`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00481/00481790.md) [`0048275c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00482/0048275c.md) [`00482898`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00482/00482898.md) [`00482e6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00482/00482e6c.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md)

変更の種類 branch_condition_or_target, call, call_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 90.53% / 新版 90.53%

CFGの説明率　旧版 78.95% / 新版 78.95%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0063a6a0",
      "incomplete_value": false,
      "site": "0063a6a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c66000:8"
              ],
              [
                "leaf",
                "const:5d0:8"
              ]
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
      "definition_site": "0063a2f0",
      "incomplete_value": false,
      "site": "0063a2f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c65000:8"
              ],
              [
                "leaf",
                "const:600:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:10:8"
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
      "site": "0063a3a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0063a754"
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
      "0063a6a4",
      "DATA",
      [
        "storage",
        "00c65610",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0063a3a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0063a79c"
      ]
    ],
    [
      "unmatched:0063a318",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "0063a6a4",
      "DATA",
      [
        "storage",
        "00c665e0",
        null,
        "undefined *"
      ]
    ],
    [
      "0063a754",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0063a79c"
      ]
    ],
    [
      "0063a6c8",
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

- 旧版 [`0063a318`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063a/0063a240.md#insn-0063a318) · [`0063a3a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063a/0063a240.md#insn-0063a3a4)
- 新版 [`0063a6c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063a/0063a5f0.md#insn-0063a6c8)

~~~diff
- 0063a318 ["COPY", "register:0:8", ["register:4040:8"]]
- 0063a318 ["INT_ADD", "register:40f0:8", ["const:63a318:8", "const:4:8"]]
- 0063a318 ["CALLIND", null, ["register:0:8"]]
- 0063a318 bytes 00013fd6
- 0063a3a4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0063a3a4 ["CBRANCH", null, ["local:b24:8", "tmp:0:1"]]
- 0063a3a4 bytes 41020054
+ 0063a6c8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0063a6c8 ["INT_ADD", "register:40f0:8", ["const:63a6c8:8", "const:4:8"]]
+ 0063a6c8 ["CALLIND", null, ["register:0:8"]]
+ 0063a6c8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0ddce0ca5d0c439c75cfa9a2ff5b287"></a>

### [`0063a418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063a/0063a418.md) → [`0063a7c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063a/0063a7c8.md) _INIT_81

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 65.54% / 新版 65.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 2件, `unresolved_store_alignment` 30件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0063a804",
      "incomplete_value": true,
      "site": "0063a820",
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
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:35:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0063a454",
      "incomplete_value": true,
      "site": "0063a470",
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
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:f66:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0063a828",
      "incomplete_value": true,
      "site": "0063a844",
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
                "const:2b8000:8"
              ],
              [
                "leaf",
                "const:48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0063a478",
      "incomplete_value": true,
      "site": "0063a494",
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
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:f79:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0063a4b4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0063a804",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "0063a828",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "0063a848",
      "READ",
      [
        "storage",
        "002b8d6e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0063a804",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "0063a828",
      "READ",
      [
        "storage",
        "002b8048",
        null,
        "string"
      ]
    ],
    [
      "0063a848",
      "READ",
      [
        "storage",
        "002b8e3d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0063a4b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063a/0063a418.md#insn-0063a4b4) · [`0063a4bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063a/0063a418.md#insn-0063a4bc) · [`0063a4c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063a/0063a418.md#insn-0063a4c4)

~~~diff
- 0063a4b4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:51:8"]]
- 0063a4b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 0063a4b4 bytes e013853c
- 0063a4bc ["COPY", "tmp:0:4", ["register:4048:4"]]
- 0063a4bc ["INT_ADD", "tmp:1:8", ["register:8:8", "const:81:8"]]
- 0063a4bc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 0063a4bc bytes e9130878
- 0063a4c4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:88:8"]]
- 0063a4c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 0063a4c4 bytes e98b00b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70062dc6e04f14c386f0591c02634c65"></a>

### [`0063a7e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063a/0063a7e4.md) → [`0063ab94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063a/0063ab94.md) FUN_0063ab94

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0064da2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064d/0064da2c.md) · 呼出先 17件 [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0046e9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e9b0.md) [`0046f0f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046f/0046f0f4.md) [`0046f724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046f/0046f724.md) [`0046f784`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046f/0046f784.md)
- 新版 呼出元 1件 [`0064dddc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064d/0064dddc.md) · 呼出先 17件 [`00448254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448254.md) [`0046ecd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046e/0046ecd0.md) [`0046f414`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046f/0046f414.md) [`0046fa44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046f/0046fa44.md) [`0046faa4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046f/0046faa4.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 81.25% / 新版 81.25%

CFGの説明率　旧版 60.78% / 新版 59.62%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_value` 9件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0063abdc",
      "incomplete_value": true,
      "site": "0063abec",
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
                "const:2a1000:8"
              ],
              [
                "leaf",
                "const:348:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0063a82c",
      "incomplete_value": true,
      "site": "0063a83c",
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
                "const:2a1000:8"
              ],
              [
                "leaf",
                "const:308:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "0063abe0",
      "incomplete_value": true,
      "site": "0063abf0",
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
              "INT_ADD",
              [
                "leaf",
                "const:f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0063a830",
      "incomplete_value": true,
      "site": "0063a840",
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
              "INT_ADD",
              [
                "leaf",
                "const:f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0063abe4",
      "incomplete_value": true,
      "site": "0063abf4",
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
                "const:a90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0063a834",
      "incomplete_value": true,
      "site": "0063a844",
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
                "const:a40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0063a810",
      "READ",
      [
        "storage",
        "00ca5038",
        null,
        "undefined1"
      ]
    ],
    [
      "0063abdc",
      "READ",
      [
        "storage",
        "002a1308",
        null,
        "string"
      ]
    ],
    [
      "0063abe0",
      "READ",
      [
        "storage",
        "002a1317",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0063abc0",
      "READ",
      [
        "storage",
        "00ca5ff8",
        null,
        "undefined1"
      ]
    ],
    [
      "0063abdc",
      "READ",
      [
        "storage",
        "002a1348",
        null,
        "string"
      ]
    ],
    [
      "0063abe0",
      "READ",
      [
        "storage",
        "002a1357",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0063a814`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063a/0063a7e4.md#insn-0063a814) · [`0063a8c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063a/0063a7e4.md#insn-0063a8c0) · [`0063a9f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063a/0063a7e4.md#insn-0063a9f4)
- 新版 [`0063abc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063a/0063ab94.md#insn-0063abc4) · [`0063ac70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063a/0063ab94.md#insn-0063ac70) · [`0063ada4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063a/0063ab94.md#insn-0063ada4)

~~~diff
- 0063a814 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 0063a814 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 0063a814 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 0063a814 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
+ 0063abc4 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
+ 0063abc4 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 0063abc4 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 0063abc4 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 0063a814 bytes a81b0036
+ 0063abc4 bytes a81b0036
- 0063a8c0 ["INT_ADD", "register:40f0:8", ["const:63a8c0:8", "const:4:8"]]
- 0063a8c0 ["CALL", null, ["callee:0047e96c:8"]]
+ 0063ac70 ["INT_ADD", "register:40f0:8", ["const:63ac70:8", "const:4:8"]]
+ 0063ac70 ["CALL", null, ["callee:0047e96c:8"]]
- 0063a8c0 bytes 630ff997
+ 0063ac70 bytes 3f0ff997
- 0063a9f4 ["INT_ADD", "register:40f0:8", ["const:63a9f4:8", "const:4:8"]]
- 0063a9f4 ["CALL", null, ["callee:0046ecd0:8"]]
+ 0063ada4 ["INT_ADD", "register:40f0:8", ["const:63ada4:8", "const:4:8"]]
+ 0063ada4 ["CALL", null, ["callee:0046ecd0:8"]]
- 0063a9f4 bytes efcff897
+ 0063ada4 bytes cbcff897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-efd304617fd1ab9254cfed7c68edccbd"></a>

### [`0063ae18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063a/0063ae18.md) → [`0063b1c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063b/0063b1c8.md) FUN_0063b1c8

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0064ecf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064e/0064ecf8.md) [`006b2bb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b2/006b2bb4.md) · 呼出先 7件 [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`0046d7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d7f0.md) [`0046ee98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046ee98.md) [`0063a7a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063a/0063a7a8.md) [`006dc8bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006dc/006dc8bc.md)
- 新版 呼出元 2件 [`0064f0a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064f/0064f0a8.md) [`006b2f64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006b2/006b2f64.md) · 呼出先 7件 [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md) [`0046db10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046db10.md) [`0046f1b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046f/0046f1b8.md) [`0063ab58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063a/0063ab58.md) [`006dcc6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006dc/006dcc6c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 65.07% / 新版 65.07%

CFGの説明率　旧版 26.13% / 新版 25.66%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_condition` 1件, `unresolved_branch_alignment` 13件, `unresolved_call_alignment` 28件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0063ae18"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0063ae18"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0063ae1c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0063ae18",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:0063ae1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0063ae20",
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
      "0063b1c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "0063b1cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0063b1d0",
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

- 旧版 [`0063ae18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063a/0063ae18.md#insn-0063ae18) · [`0063ae1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063a/0063ae18.md#insn-0063ae1c) · [`0063ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063a/0063ae18.md#insn-0063ae20)

~~~diff
- 0063ae18 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0063ae18 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0063ae18 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 0063ae18 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0063ae18 bytes fd7bbda9
- 0063ae1c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 0063ae1c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 0063ae1c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 0063ae1c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0063ae1c bytes f65701a9
- 0063ae20 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0063ae20 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0063ae20 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0063ae20 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0063ae20 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a96b33d7f709104c3332968c504c155b"></a>

### [`0063b674`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063b/0063b674.md) → [`0063ba24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063b/0063ba24.md) FUN_0063ba24

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0063c60c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063c/0063c60c.md) [`0063cd5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063c/0063cd5c.md) · 呼出先 6件 [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`0046d7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d7f0.md) [`0046ee98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046ee98.md) [`00470120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470120.md) [`0063b804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063b/0063b804.md)
- 新版 呼出元 2件 [`0063c9bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063c/0063c9bc.md) [`0063d10c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063d/0063d10c.md) · 呼出先 6件 [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md) [`0046db10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046db10.md) [`0046f1b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046f/0046f1b8.md) [`00470440`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470440.md) [`0063bbb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063b/0063bbb4.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 30.77% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 2件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0063b794"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0063bb44"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "CONDITIONAL_JUMP",
        "0063b794"
      ],
      [
        "CONDITIONAL_JUMP",
        "0063bb44"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "0063bb30",
      "incomplete_value": true,
      "site": "0063bb70",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "4",
            [
              [
                "live",
                "register:40a0:4"
              ],
              [
                "leaf",
                "const:2:4"
              ]
            ]
          ],
          [
            "leaf",
            "const:0:4"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0063b7c0",
      "value": [
        "live",
        "register:101:1"
      ]
    },
    "ordinal": 20,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0063ba48",
      "DATA",
      [
        "storage",
        "00434fd0",
        null,
        "byte[35]"
      ]
    ],
    [
      "0063ba4c",
      "DATA",
      [
        "storage",
        "00434fc8",
        null,
        "byte[35]"
      ]
    ],
    [
      "unmatched:0063b794",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0063bb68"
      ]
    ]
  ],
  "added": [
    [
      "0063ba48",
      "DATA",
      [
        "storage",
        "00434fd0",
        null,
        "byte[51]"
      ]
    ],
    [
      "0063ba4c",
      "DATA",
      [
        "storage",
        "00434fc8",
        null,
        "byte[51]"
      ]
    ],
    [
      "0063bb44",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0063bb68"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0063b794`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063b/0063b674.md#insn-0063b794) · [`0063b68c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063b/0063b674.md#insn-0063b68c)
- 新版 [`0063bb44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063b/0063ba24.md#insn-0063bb44) · [`0063ba3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063b/0063ba24.md#insn-0063ba3c)

~~~diff
- 0063b794 ["CBRANCH", null, ["local:b8:8", "register:101:1"]]
- 0063b794 bytes 20010054
+ 0063bb44 ["CBRANCH", null, ["local:b8:8", "register:101:1"]]
+ 0063bb44 bytes 20010054
- 0063b68c ["INT_ADD", "register:40f0:8", ["const:63b68c:8", "const:4:8"]]
- 0063b68c ["CALL", null, ["callee:008524fc:8"]]
+ 0063ba3c ["INT_ADD", "register:40f0:8", ["const:63ba3c:8", "const:4:8"]]
+ 0063ba3c ["CALL", null, ["callee:008524fc:8"]]
- 0063b68c bytes b1570894
+ 0063ba3c bytes b05a0894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7030581d8fd4bc6b3fb2f0edfba07d40"></a>

### [`0063b804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063b/0063b804.md) → [`0063bbb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063b/0063bbb4.md) FUN_0063bbb4

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0063b674`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063b/0063b674.md) [`0064da2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064d/0064da2c.md) · 呼出先 16件 [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0046e9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e9b0.md) [`0046f0f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046f/0046f0f4.md) [`0046f724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046f/0046f724.md) [`0046f784`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046f/0046f784.md)
- 新版 呼出元 2件 [`0063ba24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063b/0063ba24.md) [`0064dddc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064d/0064dddc.md) · 呼出先 16件 [`00448254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448254.md) [`0046ecd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046e/0046ecd0.md) [`0046f414`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046f/0046f414.md) [`0046fa44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046f/0046fa44.md) [`0046faa4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046f/0046faa4.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 84.23% / 新版 84.23%

CFGの説明率　旧版 78.18% / 新版 76.79%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 3件, `unresolved_store_alignment` 20件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0063b808"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0063b808"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0063b80c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0063b808",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:0063b80c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:0063b810",
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
      "0063bbb8",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "0063bbbc",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "0063bbc0",
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

- 旧版 [`0063b808`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063b/0063b804.md#insn-0063b808) · [`0063b80c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063b/0063b804.md#insn-0063b80c) · [`0063b810`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063b/0063b804.md#insn-0063b810)

~~~diff
- 0063b808 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0063b808 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0063b808 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:b0:8"]]
- 0063b808 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0063b808 bytes fd7b0ba9
- 0063b80c ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 0063b80c ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 0063b80c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:c0:8"]]
- 0063b80c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0063b80c bytes fc6f0ca9
- 0063b810 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 0063b810 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 0063b810 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:d0:8"]]
- 0063b810 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0063b810 bytes fa670da9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8b28f6a1dcd20eee15780eebde7e493"></a>

### [`0063bcd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063b/0063bcd8.md) → [`0063c088`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063c/0063c088.md) FUN_0063c088

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0063d0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063d/0063d0f0.md) [`0064ecf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064e/0064ecf8.md) · 呼出先 11件 [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`0046d7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d7f0.md) [`0046ee98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046ee98.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md)
- 新版 呼出元 2件 [`0063d4a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063d/0063d4a0.md) [`0064f0a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064f/0064f0a8.md) · 呼出先 11件 [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md) [`0046db10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046db10.md) [`0046f1b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046f/0046f1b8.md) [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 84.27% / 新版 84.27%

CFGの説明率　旧版 53.33% / 新版 54.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `call_target` 1件, `unresolved_branch_alignment` 10件, `unresolved_call_alignment` 21件, `unresolved_store_alignment` 6件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0063bcd8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0063bcd8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0063bcdc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0063bcd8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:0063bcdc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0063bce0",
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
      "0063c088",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "0063c08c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0063c090",
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

- 旧版 [`0063bcd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063b/0063bcd8.md#insn-0063bcd8) · [`0063bcdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063b/0063bcd8.md#insn-0063bcdc) · [`0063bce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063b/0063bcd8.md#insn-0063bce0)

~~~diff
- 0063bcd8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0063bcd8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0063bcd8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 0063bcd8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0063bcd8 bytes fd7bbda9
- 0063bcdc ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 0063bcdc ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 0063bcdc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 0063bcdc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0063bcdc bytes f65701a9
- 0063bce0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0063bce0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0063bce0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0063bce0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0063bce0 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc7918d553d6071e97057794feb1d073"></a>

### [`0063c498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063c/0063c498.md) → [`0063c848`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063c/0063c848.md) FUN_0063c848

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0063d184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063d/0063d184.md) · 呼出先 7件 [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00467b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467b6c.md) [`0046bd94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046b/0046bd94.md) [`0046e7e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e7e0.md) [`004700f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/004700f4.md)
- 新版 呼出元 1件 [`0063d534`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063d/0063d534.md) · 呼出先 7件 [`00467bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467bc0.md) [`00467e8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467e8c.md) [`0046c0b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046c0b4.md) [`0046eb00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046e/0046eb00.md) [`00470414`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470414.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 93.42% / 新版 93.42%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 5件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0063c498"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0063c498"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0063c49c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0063c498",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:0063c49c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:0063c4a0",
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
      "0063c848",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "0063c84c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "0063c850",
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

- 旧版 [`0063c498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063c/0063c498.md#insn-0063c498) · [`0063c49c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063c/0063c498.md#insn-0063c49c) · [`0063c4a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063c/0063c498.md#insn-0063c4a0)

~~~diff
- 0063c498 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0063c498 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0063c498 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 0063c498 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0063c498 bytes fd7bbca9
- 0063c49c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 0063c49c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 0063c49c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 0063c49c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0063c49c bytes f85f01a9
- 0063c4a0 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 0063c4a0 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 0063c4a0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0063c4a0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0063c4a0 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8723399a29daa5908ddf142381fa289b"></a>

### [`0063c60c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063c/0063c60c.md) → [`0063c9bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063c/0063c9bc.md) FUN_0063c9bc

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`006ea5e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ea/006ea5e0.md) [`006ee798`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ee/006ee798.md) [`006f252c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f2/006f252c.md) [`006fb24c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fb/006fb24c.md) [`006fda84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fd/006fda84.md) · 呼出先 13件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`0063b674`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063b/0063b674.md) [`0063cd5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063c/0063cd5c.md) [`00652b4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/00652b4c.md)
- 新版 呼出元 5件 [`006ea990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ea/006ea990.md) [`006eeb48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ee/006eeb48.md) [`006f28dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006f2/006f28dc.md) [`006fb5fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fb/006fb5fc.md) [`006fde34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006fd/006fde34.md) · 呼出先 13件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`0063ba24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063b/0063ba24.md) [`0063d10c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063d/0063d10c.md) [`00652efc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00652/00652efc.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 55.77% / 新版 55.77%

CFGの説明率　旧版 30.14% / 新版 29.93%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 8件, `unresolved_branch_alignment` 32件, `unresolved_call_alignment` 13件, `unresolved_store_alignment` 22件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0063c868"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0063c874"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0063c890"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0063c9e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071bf30"
      ]
    ],
    [
      "0063ca70",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071bf30"
      ]
    ],
    [
      "0063cb0c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071bf30"
      ]
    ]
  ],
  "added": [
    [
      "0063c9e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071c2e0"
      ]
    ],
    [
      "0063ca70",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071c2e0"
      ]
    ],
    [
      "0063cb0c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071c2e0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0063c868`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063c/0063c60c.md#insn-0063c868) · [`0063c874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063c/0063c60c.md#insn-0063c874) · [`0063c890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063c/0063c60c.md#insn-0063c890)

~~~diff
- 0063c868 ["COPY", "tmp:0:8", ["register:4060:8"]]
- 0063c868 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4058:4"]]
- 0063c868 bytes 8b0100b9
- 0063c874 ["INT_ADD", "tmp:0:8", ["register:4060:8", "const:38:8"]]
- 0063c874 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4068:4"]]
- 0063c874 bytes 8d3900b9
- 0063c890 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 0063c890 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 0063c890 ["INT_ADD", "register:4050:8", ["register:4050:8", "const:38:8"]]
- 0063c890 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:4"]]
- 0063c890 bytes 498503b8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3e34ffb2bd67dc59c4f2772d1d33b20"></a>

### [`0063cd5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063c/0063cd5c.md) → [`0063d10c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063d/0063d10c.md) FUN_0063d10c

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`0063c60c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063c/0063c60c.md) [`0064e3bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064e/0064e3bc.md) [`0064e580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064e/0064e580.md) [`006ea5e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ea/006ea5e0.md) · 呼出先 8件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`0063b674`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063b/0063b674.md) [`00652b4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/00652b4c.md) [`0071bf30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071b/0071bf30.md)
- 新版 呼出元 4件 [`0063c9bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063c/0063c9bc.md) [`0064e76c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064e/0064e76c.md) [`0064e930`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064e/0064e930.md) [`006ea990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ea/006ea990.md) · 呼出先 8件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`0063ba24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063b/0063ba24.md) [`00652efc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00652/00652efc.md) [`0071c2e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071c/0071c2e0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 78.85% / 新版 78.85%

CFGの説明率　旧版 20.97% / 新版 19.70%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 2件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 6件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0063ce94"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0063cf8c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0063d244"
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
      "unmatched:0063cd88",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071bf30"
      ]
    ],
    [
      "unmatched:0063cdf4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071bf30"
      ]
    ],
    [
      "unmatched:0063ce28",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0063d444"
      ]
    ]
  ],
  "added": [
    [
      "0063d138",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071c2e0"
      ]
    ],
    [
      "0063d1a4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071c2e0"
      ]
    ],
    [
      "0063d1d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0063d444"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0063cd88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063c/0063cd5c.md#insn-0063cd88) · [`0063cdf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063c/0063cd5c.md#insn-0063cdf4) · [`0063ce28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063c/0063cd5c.md#insn-0063ce28)

~~~diff
- 0063cd88 ["INT_ADD", "register:40f0:8", ["const:63cd88:8", "const:4:8"]]
- 0063cd88 ["CALL", null, ["ram:71bf30:8"]]
- 0063cd88 bytes 6a7c0394
- 0063cdf4 ["INT_ADD", "register:40f0:8", ["const:63cdf4:8", "const:4:8"]]
- 0063cdf4 ["CALL", null, ["ram:71bf30:8"]]
- 0063cdf4 bytes 4f7c0394
- 0063ce28 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0063ce28 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 0063ce28 ["CBRANCH", null, ["local:b46:8", "tmp:1:1"]]
- 0063ce28 bytes 68130054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9894e5133711d248e1b69046b5302fdb"></a>

### [`0063d28c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063d/0063d28c.md) → [`0063d63c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063d/0063d63c.md) FUN_0063d63c

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0063dd50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063d/0063dd50.md) · 呼出先 12件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0048795c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048795c.md) [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md) [`00487e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487e60.md) [`00488698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/00488698.md)
- 新版 呼出元 1件 [`0063e100`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063e/0063e100.md) · 呼出先 12件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00487c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c7c.md) [`00487c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c9c.md) [`00488180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00488/00488180.md) [`004889b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00488/004889b8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 55.90% / 新版 55.90%

CFGの説明率　旧版 29.08% / 新版 27.89%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 4件, `unresolved_branch_alignment` 26件, `unresolved_call_alignment` 9件, `unresolved_store_alignment` 48件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0063d678",
      "incomplete_value": false,
      "site": "0063d67c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:dd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0063d2c8",
      "incomplete_value": false,
      "site": "0063d2cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:e08:8"
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
      "definition_site": "0063d694",
      "incomplete_value": true,
      "site": "0063d6a4",
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
                "const:2bb000:8"
              ],
              [
                "leaf",
                "const:6ba:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0063d2e4",
      "incomplete_value": true,
      "site": "0063d2f4",
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
                "const:2bb000:8"
              ],
              [
                "leaf",
                "const:5dc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0063d698",
      "incomplete_value": true,
      "site": "0063d6a8",
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
              "INT_ADD",
              [
                "leaf",
                "const:a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0063d2e8",
      "incomplete_value": true,
      "site": "0063d2f8",
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
              "INT_ADD",
              [
                "leaf",
                "const:a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0063d67c",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ],
    [
      "0063d694",
      "READ",
      [
        "storage",
        "002bb5dc",
        null,
        "string"
      ]
    ],
    [
      "0063d698",
      "READ",
      [
        "storage",
        "002bb5e6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0063d67c",
      "DATA",
      [
        "storage",
        "00c65dd8",
        null,
        "undefined *"
      ]
    ],
    [
      "0063d694",
      "READ",
      [
        "storage",
        "002bb6ba",
        null,
        "string"
      ]
    ],
    [
      "0063d698",
      "READ",
      [
        "storage",
        "002bb6c4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0063d484`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063d/0063d28c.md#insn-0063d484) · [`0063d490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063d/0063d28c.md#insn-0063d490) · [`0063d494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063d/0063d28c.md#insn-0063d494)

~~~diff
- 0063d484 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:1c:8"]]
- 0063d484 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:4"]]
- 0063d484 bytes 141c00b9
- 0063d490 ["COPY", "tmp:0:8", ["const:0:8"]]
- 0063d490 ["COPY", "tmp:1:8", ["const:0:8"]]
- 0063d490 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 0063d490 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 0063d490 bytes 1ffc02a9
- 0063d494 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:20:8"]]
- 0063d494 ["COPY", "tmp:1:8", ["const:0:8"]]
- 0063d494 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 0063d494 bytes 1f1000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc711fd08f4ddaf9aa26f2bef4eda74e"></a>

### [`0063d954`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063d/0063d954.md) → [`0063dd04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063d/0063dd04.md) FUN_0063dd04

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00641644`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00641/00641644.md) [`00641944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00641/00641944.md) · 呼出先 8件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0063dd08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063d/0063dd08.md) [`00727a28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00727/00727a28.md) [`008003d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00800/008003d0.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 2件 [`006419f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00641/006419f4.md) [`00641cf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00641/00641cf4.md) · 呼出先 8件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`0063e0b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063e/0063e0b8.md) [`00727dd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00727/00727dd8.md) [`00801334`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00801/00801334.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 91.18% / 新版 91.18%

CFGの説明率　旧版 38.82% / 新版 38.82%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `store_condition` 1件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0063d968"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0063d968"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0063d96c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0063d968",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0063d96c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0063da30",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0063ddec"
      ]
    ]
  ],
  "added": [
    [
      "0063dd18",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0063dd1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0063dde0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0063ddec"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0063d968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063d/0063d954.md#insn-0063d968) · [`0063d96c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063d/0063d954.md#insn-0063d96c) · [`0063da30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063d/0063d954.md#insn-0063da30)

~~~diff
- 0063d968 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 0063d968 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 0063d968 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0063d968 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0063d968 bytes f65702a9
- 0063d96c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0063d96c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0063d96c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 0063d96c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0063d96c bytes f44f03a9
- 0063da30 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 0063da30 ["CBRANCH", null, ["local:b17:8", "tmp:0:1"]]
- 0063da30 bytes 680000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3875236446e87b747ae5a4c8fcbfbf82"></a>

### [`0063dd50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063d/0063dd50.md) → [`0063e100`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063e/0063e100.md) FUN_0063e100

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b11e20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b11/00b11e20.md) · 呼出先 28件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00440f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f9c.md) [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md)
- 新版 呼出元 1件 [`00b12e14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b12/00b12e14.md) · 呼出先 28件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`004412bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004412bc.md) [`00448254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448254.md) [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_destination, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 25.52% / 新版 25.52%

CFGの説明率　旧版 9.31% / 新版 9.27%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 20件, `call_target` 1件, `store_condition` 3件, `store_destination` 3件, `unresolved_branch_alignment` 273件, `unresolved_call_alignment` 144件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 471件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0063dd50"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0063dd50"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0063dd54"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0063dd50",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:0063dd54",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:0063dd58",
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
      "0063e100",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "0063e104",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "0063e108",
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

- 旧版 [`0063dd50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063d/0063dd50.md#insn-0063dd50) · [`0063dd54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063d/0063dd50.md#insn-0063dd54) · [`0063dd58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063d/0063dd50.md#insn-0063dd58)

~~~diff
- 0063dd50 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0063dd50 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0063dd50 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffa0:8"]]
- 0063dd50 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0063dd50 bytes fd7bbaa9
- 0063dd54 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 0063dd54 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 0063dd54 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 0063dd54 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0063dd54 bytes fc6f01a9
- 0063dd58 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 0063dd58 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 0063dd58 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0063dd58 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0063dd58 bytes fa6702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e732f768611cc7ad52011b9ff11882a1"></a>

### [`006411b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00641/006411b4.md) → [`00641564`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00641/00641564.md) FUN_00641564

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 6件 [`006465f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00646/006465f0.md) [`0064bec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064b/0064bec8.md) [`0064dc08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064d/0064dc08.md) [`0064df50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064d/0064df50.md) [`0064e1dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064e/0064e1dc.md) · 呼出先 3件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0064133c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00641/0064133c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 6件 [`006469a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00646/006469a0.md) [`0064c278`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064c/0064c278.md) [`0064dfb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064d/0064dfb8.md) [`0064e300`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064e/0064e300.md) [`0064e58c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064e/0064e58c.md) · 呼出先 3件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`006416ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00641/006416ec.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 94.90% / 新版 94.90%

CFGの説明率　旧版 47.22% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00641234"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0064123c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "006415e4"
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
      "unmatched:006411e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006415ac"
      ]
    ],
    [
      "unmatched:006412b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00641648"
      ]
    ]
  ],
  "added": [
    [
      "00641594",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006415ac"
      ]
    ],
    [
      "00641660",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00641648"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006411e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00641/006411b4.md#insn-006411e4) · [`00641224`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00641/006411b4.md#insn-00641224) · [`00641234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00641/006411b4.md#insn-00641234)
- 新版 [`006415d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00641/00641564.md#insn-006415d4)

~~~diff
- 006411e4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 006411e4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 006411e4 bytes c90000b5
- 00641224 ["INT_ADD", "register:40f0:8", ["const:641224:8", "const:4:8"]]
- 00641224 ["CALL", null, ["callee:00c58f30:8"]]
+ 006415d4 ["INT_ADD", "register:40f0:8", ["const:6415d4:8", "const:4:8"]]
+ 006415d4 ["CALL", null, ["callee:00c58f30:8"]]
- 00641224 bytes 4f5b1894
+ 006415d4 bytes 575e1894
- 00641234 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00641234 ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 00641234 ["INT_ADD", "register:4040:8", ["register:4040:8", "const:30:8"]]
- 00641234 ["STORE", null, ["const:1b1:8", "register:4040:8", "tmp:1:8"]]
- 00641234 bytes 1f0d03f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c2ecba49defff13fa146226f2c4305f"></a>

### [`0064172c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00641/0064172c.md) → [`00641adc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00641/00641adc.md) FUN_00641adc

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 9件 [`00641644`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00641/00641644.md) [`00641944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00641/00641944.md) [`00641e1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00641/00641e1c.md) [`006452d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00645/006452d4.md) [`00646024`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00646/00646024.md) · 呼出先 2件 [`004709d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/004709d4.md) [`00641ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00641/00641ba0.md)
- 新版 呼出元 9件 [`006419f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00641/006419f4.md) [`00641cf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00641/00641cf4.md) [`006421cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00642/006421cc.md) [`00645684`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00645/00645684.md) [`006463d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00646/006463d4.md) · 呼出先 2件 [`00470cf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470cf4.md) [`00641f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00641/00641f50.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.41% / 新版 98.41%

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
      "site": "00641bdc",
      "value": [
        "leaf",
        "ram:641f50:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0064182c",
      "value": [
        "leaf",
        "ram:641ba0:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00641c24",
      "value": [
        "leaf",
        "ram:641f50:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00641874",
      "value": [
        "leaf",
        "ram:641ba0:8"
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
      "00641bdc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00641ba0"
      ]
    ],
    [
      "00641c24",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00641ba0"
      ]
    ]
  ],
  "added": [
    [
      "00641bdc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00641f50"
      ]
    ],
    [
      "00641c24",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00641f50"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0064182c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00641/0064172c.md#insn-0064182c) · [`00641874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00641/0064172c.md#insn-00641874) · [`00641858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00641/0064172c.md#insn-00641858)
- 新版 [`00641bdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00641/00641adc.md#insn-00641bdc) · [`00641c24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00641/00641adc.md#insn-00641c24) · [`00641c08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00641/00641adc.md#insn-00641c08)

~~~diff
- 0064182c ["INT_ADD", "register:40f0:8", ["const:64182c:8", "const:4:8"]]
- 0064182c ["CALL", null, ["ram:641ba0:8"]]
+ 00641bdc ["INT_ADD", "register:40f0:8", ["const:641bdc:8", "const:4:8"]]
+ 00641bdc ["CALL", null, ["ram:641f50:8"]]
- 0064182c bytes dd000094
+ 00641bdc bytes dd000094
- 00641874 ["INT_ADD", "register:40f0:8", ["const:641874:8", "const:4:8"]]
- 00641874 ["CALL", null, ["ram:641ba0:8"]]
+ 00641c24 ["INT_ADD", "register:40f0:8", ["const:641c24:8", "const:4:8"]]
+ 00641c24 ["CALL", null, ["ram:641f50:8"]]
- 00641874 bytes cb000094
+ 00641c24 bytes cb000094
- 00641858 ["INT_ADD", "register:40f0:8", ["const:641858:8", "const:4:8"]]
- 00641858 ["CALL", null, ["callee:00470cf4:8"]]
+ 00641c08 ["INT_ADD", "register:40f0:8", ["const:641c08:8", "const:4:8"]]
+ 00641c08 ["CALL", null, ["callee:00470cf4:8"]]
- 00641858 bytes 5fbcf897
+ 00641c08 bytes 3bbcf897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-742bf3ce367a4bc428702074535f7648"></a>

### [`00641e1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00641/00641e1c.md) → [`006421cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00642/006421cc.md) FUN_006421cc

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0064ecf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064e/0064ecf8.md) · 呼出先 4件 [`0064172c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00641/0064172c.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`0064f0a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064f/0064f0a8.md) · 呼出先 4件 [`00641adc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00641/00641adc.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.75% / 新版 97.75%

CFGの説明率　旧版 71.43% / 新版 76.92%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00641e60"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00642210"
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
      "unmatched:00641e5c",
      "DATA",
      [
        "storage",
        "004362b0",
        null,
        "byte[63]"
      ]
    ],
    [
      "unmatched:00641e60",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00642244"
      ]
    ],
    [
      "0064225c",
      "DATA",
      [
        "storage",
        "004362d8",
        null,
        "byte[63]"
      ]
    ]
  ],
  "added": [
    [
      "0064220c",
      "DATA",
      [
        "storage",
        "004362b0",
        null,
        "byte[51]"
      ]
    ],
    [
      "00642210",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00642244"
      ]
    ],
    [
      "0064225c",
      "DATA",
      [
        "storage",
        "004362d8",
        null,
        "byte[51]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00641e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00641/00641e1c.md#insn-00641e60) · [`00641e50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00641/00641e1c.md#insn-00641e50)
- 新版 [`00642210`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00642/006421cc.md#insn-00642210) · [`00642200`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00642/006421cc.md#insn-00642200)

~~~diff
- 00641e60 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00641e60 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00641e60 bytes a90100b4
+ 00642210 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
+ 00642210 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00642210 bytes a90100b4
- 00641e50 ["INT_ADD", "register:40f0:8", ["const:641e50:8", "const:4:8"]]
- 00641e50 ["CALL", null, ["callee:008524fc:8"]]
+ 00642200 ["INT_ADD", "register:40f0:8", ["const:642200:8", "const:4:8"]]
+ 00642200 ["CALL", null, ["callee:008524fc:8"]]
- 00641e50 bytes c03d0894
+ 00642200 bytes bf400894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0649e19a9cae09b5e58e145a965e79f8"></a>

### [`00642050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00642/00642050.md) → [`00642400`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00642/00642400.md) FUN_00642400

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00643130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00643/00643130.md) [`006452d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00645/006452d4.md) · 呼出先 19件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00447734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447734.md) [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`0047e64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e64c.md)
- 新版 呼出元 2件 [`006434e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00643/006434e0.md) [`00645684`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00645/00645684.md) · 呼出先 19件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00447a54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00447/00447a54.md) [`00448254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448254.md) [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`0047e96c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047e/0047e96c.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 84.17% / 新版 84.17%

CFGの説明率　旧版 83.25% / 新版 82.84%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `store_value` 8件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 6件, `unresolved_store_alignment` 18件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006421d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006421e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00642744",
      "incomplete_value": true,
      "site": "00642750",
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
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:1d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00642394",
      "incomplete_value": true,
      "site": "006423a0",
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
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:109:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 35,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006420f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006425e4"
      ]
    ],
    [
      "unmatched:00642188",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00642554"
      ]
    ],
    [
      "unmatched:006421c8",
      "READ",
      [
        "storage",
        "002c2ad0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "006424a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006425e4"
      ]
    ],
    [
      "00642538",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00642554"
      ]
    ],
    [
      "00642578",
      "READ",
      [
        "storage",
        "002c2b20",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006421d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00642/00642050.md#insn-006421d8) · [`006421e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00642/00642050.md#insn-006421e0) · [`006424cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00642/00642050.md#insn-006424cc)
- 新版 [`0064287c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00642/00642400.md#insn-0064287c)

~~~diff
- 006421d8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 006421d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 006421d8 bytes e00b803d
- 006421e0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 006421e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 006421e0 bytes e007803d
- 006424cc ["INT_ADD", "register:40f0:8", ["const:6424cc:8", "const:4:8"]]
- 006424cc ["CALL", null, ["callee:0047e96c:8"]]
+ 0064287c ["INT_ADD", "register:40f0:8", ["const:64287c:8", "const:4:8"]]
+ 0064287c ["CALL", null, ["callee:0047e96c:8"]]
- 006424cc bytes 60f0f897
+ 0064287c bytes 3cf0f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96df9407ccc56f3b25414d15a3ac85ae"></a>

### [`00645010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00645/00645010.md) → [`006453c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00645/006453c0.md) FUN_006453c0

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00643130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00643/00643130.md) · 呼出先 7件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00653174`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00653/00653174.md) [`00653188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00653/00653188.md) [`00653370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00653/00653370.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`006434e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00643/006434e0.md) · 呼出先 7件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00653524`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00653/00653524.md) [`00653538`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00653/00653538.md) [`00653720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00653/00653720.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 82.74% / 新版 82.74%

CFGの説明率　旧版 42.59% / 新版 44.23%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 13件, `unresolved_branch_alignment` 5件, `unresolved_store_alignment` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00645020"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00645020"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00645024"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00645020",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00645024",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0064503c",
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
      "006453d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "006453d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "006453ec",
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

- 旧版 [`00645020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00645/00645010.md#insn-00645020) · [`00645024`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00645/00645010.md#insn-00645024) · [`0064503c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00645/00645010.md#insn-0064503c)

~~~diff
- 00645020 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00645020 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00645020 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00645020 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00645020 bytes f65706a9
- 00645024 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00645024 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00645024 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00645024 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00645024 bytes f44f07a9
- 0064503c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0064503c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0064503c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0064503c bytes a8831ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8735f3bc7414450bf6b15765d3752d8"></a>

### [`00646024`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00646/00646024.md) → [`006463d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00646/006463d4.md) FUN_006463d4

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0064a570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064a/0064a570.md) · 呼出先 5件 [`0064172c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00641/0064172c.md) [`00641ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00641/00641ba0.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`0064a920`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064a/0064a920.md) · 呼出先 5件 [`00641adc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00641/00641adc.md) [`00641f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00641/00641f50.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.44% / 新版 97.44%

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
      "site": "00646408",
      "value": [
        "leaf",
        "ram:641f50:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00646058",
      "value": [
        "leaf",
        "ram:641ba0:8"
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
      "00646408",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00641ba0"
      ]
    ]
  ],
  "added": [
    [
      "00646408",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00641f50"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00646058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00646/00646024.md#insn-00646058) · [`0064604c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00646/00646024.md#insn-0064604c) · [`00646060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00646/00646024.md#insn-00646060)
- 新版 [`00646408`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00646/006463d4.md#insn-00646408) · [`006463fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00646/006463d4.md#insn-006463fc) · [`00646410`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00646/006463d4.md#insn-00646410)

~~~diff
- 00646058 ["INT_ADD", "register:40f0:8", ["const:646058:8", "const:4:8"]]
- 00646058 ["CALL", null, ["ram:641ba0:8"]]
+ 00646408 ["INT_ADD", "register:40f0:8", ["const:646408:8", "const:4:8"]]
+ 00646408 ["CALL", null, ["ram:641f50:8"]]
- 00646058 bytes d2eeff97
+ 00646408 bytes d2eeff97
- 0064604c ["INT_ADD", "register:40f0:8", ["const:64604c:8", "const:4:8"]]
- 0064604c ["CALL", null, ["callee:008524fc:8"]]
+ 006463fc ["INT_ADD", "register:40f0:8", ["const:6463fc:8", "const:4:8"]]
+ 006463fc ["CALL", null, ["callee:008524fc:8"]]
- 0064604c bytes 412d0894
+ 006463fc bytes 40300894
- 00646060 ["INT_ADD", "register:40f0:8", ["const:646060:8", "const:4:8"]]
- 00646060 ["CALL", null, ["callee:008524fc:8"]]
+ 00646410 ["INT_ADD", "register:40f0:8", ["const:646410:8", "const:4:8"]]
+ 00646410 ["CALL", null, ["callee:008524fc:8"]]
- 00646060 bytes 3c2d0894
+ 00646410 bytes 3b300894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ccd7f083712f0f938bab9c385281f45"></a>

### [`0064a570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064a/0064a570.md) → [`0064a920`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064a/0064a920.md) FUN_0064a920

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`006465f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00646/006465f0.md) [`006535e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00653/006535e0.md) · 呼出先 6件 [`00641944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00641/00641944.md) [`00646024`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00646/00646024.md) [`0064df50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064d/0064df50.md) [`0064e1dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064e/0064e1dc.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 2件 [`006469a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00646/006469a0.md) [`00653990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00653/00653990.md) · 呼出先 6件 [`00641cf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00641/00641cf4.md) [`006463d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00646/006463d4.md) [`0064e300`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064e/0064e300.md) [`0064e58c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064e/0064e58c.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 62.50% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "0064a598",
      "incomplete_value": true,
      "site": "0064a5a4",
      "value": [
        "live",
        "register:40a8:8"
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "0064a594",
      "incomplete_value": true,
      "site": "0064a5a4",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "INT_AND",
            "4",
            [
              [
                "live",
                "register:40b0:4"
              ],
              [
                "leaf",
                "const:1:4"
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


#### 変更候補の命令位置

- 旧版 [`0064a5a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064a/0064a570.md#insn-0064a5a4) · [`0064a590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064a/0064a570.md#insn-0064a590) · [`0064a5a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064a/0064a570.md#insn-0064a5a8)
- 新版 [`0064a954`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064a/0064a920.md#insn-0064a954) · [`0064a940`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064a/0064a920.md#insn-0064a940) · [`0064a958`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064a/0064a920.md#insn-0064a958)

~~~diff
- 0064a5a4 ["INT_ADD", "register:40f0:8", ["const:64a5a4:8", "const:4:8"]]
- 0064a5a4 ["CALL", null, ["callee:0064e300:8"]]
+ 0064a954 ["INT_ADD", "register:40f0:8", ["const:64a954:8", "const:4:8"]]
+ 0064a954 ["CALL", null, ["callee:0064e300:8"]]
- 0064a5a4 bytes 6b0e0094
+ 0064a954 bytes 6b0e0094
- 0064a590 ["INT_RIGHT", "tmp:0:4", ["register:4008:4", "const:0:4"]]
- 0064a590 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 0064a590 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 0064a590 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
+ 0064a940 ["INT_RIGHT", "tmp:0:4", ["register:4008:4", "const:0:4"]]
+ 0064a940 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 0064a940 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 0064a940 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 0064a590 bytes e1010036
+ 0064a940 bytes e1010036
- 0064a5a8 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 0064a5a8 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 0064a5a8 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 0064a5a8 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
+ 0064a958 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
+ 0064a958 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 0064a958 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 0064a958 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 0064a5a8 bytes a0040036
+ 0064a958 bytes a0040036
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc62cb9824239eb0262f6c0bdc093f38"></a>

### [`0064a6cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064a/0064a6cc.md) → [`0064aa7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064a/0064aa7c.md) FUN_0064aa7c

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`006465f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00646/006465f0.md) · 呼出先 5件 [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00468e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468e60.md) [`00489f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489f8c.md) [`0048ab70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048ab70.md) [`0048ab78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048ab78.md)
- 新版 呼出元 1件 [`006469a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00646/006469a0.md) · 呼出先 5件 [`00467bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467bc0.md) [`00469180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00469/00469180.md) [`0048a2ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048a/0048a2ac.md) [`0048ae90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048a/0048ae90.md) [`0048ae98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048a/0048ae98.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.41% / 新版 97.41%

CFGの説明率　旧版 25.00% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0064abd0",
      "incomplete_value": false,
      "site": "0064abe4",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "leaf",
            "const:0:4"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0064ac54",
      "incomplete_value": true,
      "site": "0064ac58",
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
                "live",
                "register:4040:8"
              ],
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 12,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`0064a834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064a/0064a6cc.md#insn-0064a834) · [`0064a8a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064a/0064a6cc.md#insn-0064a8a8) · [`0064a734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064a/0064a6cc.md#insn-0064a734)
- 新版 [`0064abe4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064a/0064aa7c.md#insn-0064abe4) · [`0064ac58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064a/0064aa7c.md#insn-0064ac58) · [`0064aae4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064a/0064aa7c.md#insn-0064aae4)

~~~diff
- 0064a834 ["INT_ADD", "register:40f0:8", ["const:64a834:8", "const:4:8"]]
- 0064a834 ["CALL", null, ["callee:0048a2ac:8"]]
+ 0064abe4 ["INT_ADD", "register:40f0:8", ["const:64abe4:8", "const:4:8"]]
+ 0064abe4 ["CALL", null, ["callee:0048a2ac:8"]]
- 0064a834 bytes d6fdf897
+ 0064abe4 bytes b2fdf897
- 0064a8a8 ["INT_ADD", "register:40f0:8", ["const:64a8a8:8", "const:4:8"]]
- 0064a8a8 ["CALL", null, ["callee:0048a2ac:8"]]
+ 0064ac58 ["INT_ADD", "register:40f0:8", ["const:64ac58:8", "const:4:8"]]
+ 0064ac58 ["CALL", null, ["callee:0048a2ac:8"]]
- 0064a8a8 bytes b9fdf897
+ 0064ac58 bytes 95fdf897
- 0064a734 ["INT_ADD", "register:40f0:8", ["const:64a734:8", "const:4:8"]]
- 0064a734 ["CALL", null, ["callee:0048a2ac:8"]]
+ 0064aae4 ["INT_ADD", "register:40f0:8", ["const:64aae4:8", "const:4:8"]]
+ 0064aae4 ["CALL", null, ["callee:0048a2ac:8"]]
- 0064a734 bytes 16fef897
+ 0064aae4 bytes f2fdf897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5ab45fc9dc082c6379f42fa4d887dbb"></a>

### [`0064aa98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064a/0064aa98.md) → [`0064ae48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064a/0064ae48.md) FUN_0064ae48

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0064e3bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064e/0064e3bc.md) [`0064e580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064e/0064e580.md) · 呼出先 19件 [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`0047e64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e64c.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`006c0dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c0/006c0dc8.md)
- 新版 呼出元 2件 [`0064e76c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064e/0064e76c.md) [`0064e930`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064e/0064e930.md) · 呼出先 19件 [`00448254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448254.md) [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md) [`0047e96c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047e/0047e96c.md) [`0047f114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047f/0047f114.md) [`006c1178`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006c1/006c1178.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 87.35% / 新版 87.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `store_destination` 7件, `store_value` 12件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0064b12c",
      "incomplete_value": true,
      "site": "0064b13c",
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
                "const:2a9000:8"
              ],
              [
                "leaf",
                "const:f9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0064ad7c",
      "incomplete_value": true,
      "site": "0064ad8c",
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
                "const:2a9000:8"
              ],
              [
                "leaf",
                "const:ecd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 42,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0064b14c",
      "incomplete_value": true,
      "site": "0064b14c",
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
              [
                "leaf",
                "const:f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0064ad9c",
      "incomplete_value": true,
      "site": "0064ad9c",
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
              [
                "leaf",
                "const:f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 43,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0064b140",
      "incomplete_value": true,
      "site": "0064b154",
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
                "const:4e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0064ad90",
      "incomplete_value": true,
      "site": "0064ada4",
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
                "const:490:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 44,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0064ae84",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "0064ae90",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0064ae98",
      "PARAM",
      [
        "storage",
        "00c738e0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0064ae84",
      "READ",
      [
        "storage",
        "00ca5a38",
        null,
        "undefined8"
      ]
    ],
    [
      "0064ae90",
      "PARAM",
      [
        "storage",
        "00c66ef8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0064ae98",
      "PARAM",
      [
        "storage",
        "00c748b0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0064aae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064a/0064aa98.md#insn-0064aae4) · [`0064aae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064a/0064aa98.md#insn-0064aae8) · [`0064aaf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064a/0064aa98.md#insn-0064aaf4)
- 新版 [`0064ae94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064a/0064ae48.md#insn-0064ae94) · [`0064ae98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064a/0064ae48.md#insn-0064ae98) · [`0064aea4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064a/0064ae48.md#insn-0064aea4)

~~~diff
- 0064aae4 ["COPY", "register:4010:8", ["const:c73000:8"]]
+ 0064ae94 ["COPY", "register:4010:8", ["const:c74000:8"]]
- 0064aae4 bytes 423100b0
+ 0064ae94 bytes 423100d0
- 0064aae8 ["COPY", "tmp:0:8", ["const:8e0:8"]]
- 0064aae8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0064aae8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0064aae8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0064ae98 ["COPY", "tmp:0:8", ["const:8b0:8"]]
+ 0064ae98 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0064ae98 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0064ae98 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0064aae8 bytes 42802391
+ 0064ae98 bytes 42c02291
- 0064aaf4 ["INT_ADD", "register:40f0:8", ["const:64aaf4:8", "const:4:8"]]
- 0064aaf4 ["CALL", null, ["callee:00c596b0:8"]]
+ 0064aea4 ["INT_ADD", "register:40f0:8", ["const:64aea4:8", "const:4:8"]]
+ 0064aea4 ["CALL", null, ["callee:00c596b0:8"]]
- 0064aaf4 bytes fb361894
+ 0064aea4 bytes 033a1894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dafe06b4ceeda30de760501d023ca5a9"></a>

### [`0064b1e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064b/0064b1e8.md) → [`0064b598`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064b/0064b598.md) FUN_0064b598

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0064ecf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064e/0064ecf8.md) · 呼出先 29件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440b40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440b40.md) [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`00473580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/00473580.md)
- 新版 呼出元 1件 [`0064f0a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064f/0064f0a8.md) · 呼出先 29件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00440e60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00440/00440e60.md) [`00448254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448254.md) [`004738a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00473/004738a0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 91.06% / 新版 91.06%

CFGの説明率　旧版 60.12% / 新版 60.49%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 21件, `call_target` 8件, `store_value` 2件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 7件

アドレスに依存する影響 `branch_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0064b1f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0064b1f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0064b1fc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0064b1f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:0064b1fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0064b200",
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
      "0064b5a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "0064b5ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0064b5b0",
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

- 旧版 [`0064b1f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064b/0064b1e8.md#insn-0064b1f8) · [`0064b1fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064b/0064b1e8.md#insn-0064b1fc) · [`0064b200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064b/0064b1e8.md#insn-0064b200)

~~~diff
- 0064b1f8 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 0064b1f8 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 0064b1f8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:110:8"]]
- 0064b1f8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0064b1f8 bytes f85f11a9
- 0064b1fc ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 0064b1fc ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 0064b1fc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:120:8"]]
- 0064b1fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0064b1fc bytes f65712a9
- 0064b200 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0064b200 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0064b200 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:130:8"]]
- 0064b200 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0064b200 bytes f44f13a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31979e3887f4b8060aec83de3bffcfb8"></a>

### [`0064bd94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064b/0064bd94.md) → [`0064c144`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064c/0064c144.md) FUN_0064c144

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`0064b1e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064b/0064b1e8.md) [`008978e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00897/008978e4.md) [`009d3b48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d3/009d3b48.md) · 呼出先 4件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00656d98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00656/00656d98.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 3件 [`0064b598`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064b/0064b598.md) [`00898890`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00898/00898890.md) [`009d4af4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009d4/009d4af4.md) · 呼出先 4件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00657148`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00657/00657148.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 10.53% / 新版 9.52%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0064bddc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0064c18c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0064be64"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0064bddc",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:0064be64",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0064c274"
      ]
    ]
  ],
  "added": [
    [
      "0064c18c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "0064c214",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0064c274"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0064bddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064b/0064bd94.md#insn-0064bddc) · [`0064be34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064b/0064bd94.md#insn-0064be34) · [`0064be64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064b/0064bd94.md#insn-0064be64)
- 新版 [`0064c1e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064c/0064c144.md#insn-0064c1e4)

~~~diff
- 0064bddc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:30:8"]]
- 0064bddc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0064bddc bytes e81b00f9
- 0064be34 ["INT_ADD", "register:40f0:8", ["const:64be34:8", "const:4:8"]]
- 0064be34 ["CALL", null, ["callee:00657148:8"]]
+ 0064c1e4 ["INT_ADD", "register:40f0:8", ["const:64c1e4:8", "const:4:8"]]
+ 0064c1e4 ["CALL", null, ["callee:00657148:8"]]
- 0064be34 bytes d92b0094
+ 0064c1e4 bytes d92b0094
- 0064be64 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0064be64 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 0064be64 bytes 01030054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b29b65d831d34e298c869f8fc1a2d1f5"></a>

### [`0064ca48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064c/0064ca48.md) → [`0064cdf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064c/0064cdf8.md) FUN_0064cdf8

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0064ccb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064c/0064ccb0.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`0064d060`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064d/0064d060.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 18.07% / 新版 18.07%

CFGの説明率　旧版 5.00% / 新版 5.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 11件, `unresolved_call_alignment` 11件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0064ca70"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0064ca88"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0064caa0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0064ce04",
      "READ",
      [
        "storage",
        "00ca6c90",
        null,
        "undefined1"
      ]
    ],
    [
      "0064ce08",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:0064ca68"
      ]
    ],
    [
      "unmatched:0064ca60",
      "READ",
      [
        "storage",
        "00ca6ca0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0064ce04",
      "READ",
      [
        "storage",
        "00ca7c50",
        null,
        "undefined1"
      ]
    ],
    [
      "0064ce08",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0064ce18"
      ]
    ],
    [
      "0064ce10",
      "READ",
      [
        "storage",
        "00ca7c60",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0064ca64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064c/0064ca48.md#insn-0064ca64) · [`0064ca70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064c/0064ca48.md#insn-0064ca70) · [`0064ca7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064c/0064ca48.md#insn-0064ca7c)

~~~diff
- 0064ca64 ["INT_ADD", "register:40f0:8", ["const:64ca64:8", "const:4:8"]]
- 0064ca64 ["CALL", null, ["callee:00c58f50:8"]]
- 0064ca64 bytes 472d1894
- 0064ca70 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 0064ca70 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 0064ca70 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 0064ca70 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 0064ca70 bytes 88000036
- 0064ca7c ["INT_ADD", "register:40f0:8", ["const:64ca7c:8", "const:4:8"]]
- 0064ca7c ["CALL", null, ["callee:00c58f50:8"]]
- 0064ca7c bytes 412d1894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76341246d4328573ff3483d8a991b160"></a>

### [`0064d874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064d/0064d874.md) → [`0064dc24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064d/0064dc24.md) FUN_0064dc24

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00b11e20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b11/00b11e20.md) · 呼出先 10件 [`0048795c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048795c.md) [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md) [`00487e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487e60.md) [`00488698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/00488698.md) [`00b11188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b11/00b11188.md)
- 新版 呼出元 1件 [`00b12e14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b12/00b12e14.md) · 呼出先 10件 [`00487c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c7c.md) [`00487c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c9c.md) [`00488180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00488/00488180.md) [`004889b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00488/004889b8.md) [`00b1217c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b12/00b1217c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 81.11% / 新版 81.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 6件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0064dc58",
      "incomplete_value": false,
      "site": "0064dc64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:dd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0064d8a8",
      "incomplete_value": false,
      "site": "0064d8b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:e08:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0064dc6c",
      "incomplete_value": true,
      "site": "0064dc7c",
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
                "const:2a9000:8"
              ],
              [
                "leaf",
                "const:fdb:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0064d8bc",
      "incomplete_value": true,
      "site": "0064d8cc",
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
                "const:2a9000:8"
              ],
              [
                "leaf",
                "const:f0e:8"
              ]
            ]
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
      "definition_site": "0064dc80",
      "incomplete_value": true,
      "site": "0064dc80",
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
              [
                "leaf",
                "const:d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0064d8d0",
      "incomplete_value": true,
      "site": "0064d8d0",
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
              [
                "leaf",
                "const:d:8"
              ]
            ]
          ]
        ]
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
      "0064dc64",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ],
    [
      "0064dc6c",
      "READ",
      [
        "storage",
        "002a9f0e",
        null,
        "string"
      ]
    ],
    [
      "0064dc74",
      "READ",
      [
        "storage",
        "002a9f1b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0064dc64",
      "DATA",
      [
        "storage",
        "00c65dd8",
        null,
        "undefined *"
      ]
    ],
    [
      "0064dc6c",
      "READ",
      [
        "storage",
        "002a9fdb",
        null,
        "string"
      ]
    ],
    [
      "0064dc74",
      "READ",
      [
        "storage",
        "002a9fe8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0064d8a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064d/0064d874.md#insn-0064d8a0) · [`0064d8a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064d/0064d874.md#insn-0064d8a4) · [`0064d8a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064d/0064d874.md#insn-0064d8a8)
- 新版 [`0064dc50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064d/0064dc24.md#insn-0064dc50) · [`0064dc54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064d/0064dc24.md#insn-0064dc54) · [`0064dc58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064d/0064dc24.md#insn-0064dc58)

~~~diff
- 0064d8a0 ["INT_ADD", "register:40f0:8", ["const:64d8a0:8", "const:4:8"]]
- 0064d8a0 ["CALL", null, ["callee:00488180:8"]]
+ 0064dc50 ["INT_ADD", "register:40f0:8", ["const:64dc50:8", "const:4:8"]]
+ 0064dc50 ["CALL", null, ["callee:00488180:8"]]
- 0064d8a0 bytes 70e9f897
+ 0064dc50 bytes 4ce9f897
- 0064d8a4 ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 0064dc54 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 0064d8a4 bytes a83000f0
+ 0064dc54 bytes c8300090
- 0064d8a8 ["COPY", "tmp:0:8", ["const:e08:8"]]
- 0064d8a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0064d8a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0064d8a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0064dc58 ["COPY", "tmp:0:8", ["const:dd8:8"]]
+ 0064dc58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0064dc58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0064dc58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0064d8a8 bytes 08213891
+ 0064dc58 bytes 08613791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4ecf87061aab6a616a3fa21ca7654d9"></a>

### [`0064da2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064d/0064da2c.md) → [`0064dddc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064d/0064dddc.md) FUN_0064dddc

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0064e580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064e/0064e580.md) · 呼出先 13件 [`0046e7b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e7b0.md) [`0046e7c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e7c0.md) [`0046e9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e9b0.md) [`0046f0f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046f/0046f0f4.md) [`0046f724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046f/0046f724.md)
- 新版 呼出元 1件 [`0064e930`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064e/0064e930.md) · 呼出先 13件 [`0046ead0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046e/0046ead0.md) [`0046eae0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046e/0046eae0.md) [`0046ecd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046e/0046ecd0.md) [`0046f414`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046f/0046f414.md) [`0046fa44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046f/0046fa44.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.85% / 新版 85.85%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0064de2c",
      "incomplete_value": true,
      "site": "0064de2c",
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
                "const:29f000:8"
              ],
              [
                "leaf",
                "const:23e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0064da7c",
      "incomplete_value": true,
      "site": "0064da7c",
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
                "const:29f000:8"
              ],
              [
                "leaf",
                "const:1fe:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0064de20",
      "incomplete_value": true,
      "site": "0064de30",
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
              [
                "leaf",
                "const:7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0064da70",
      "incomplete_value": true,
      "site": "0064da80",
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
              [
                "leaf",
                "const:7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0064dee0",
      "incomplete_value": true,
      "site": "0064def4",
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
                "const:2b3000:8"
              ],
              [
                "leaf",
                "const:efb:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0064db30",
      "incomplete_value": true,
      "site": "0064db44",
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
                "const:2b3000:8"
              ],
              [
                "leaf",
                "const:e1d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0064de1c",
      "READ",
      [
        "storage",
        "0029f1fe",
        null,
        "string"
      ]
    ],
    [
      "0064de20",
      "READ",
      [
        "storage",
        "0029f205",
        null,
        "string"
      ]
    ],
    [
      "0064dee0",
      "READ",
      [
        "storage",
        "002b3e1d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0064de1c",
      "READ",
      [
        "storage",
        "0029f23e",
        null,
        "string"
      ]
    ],
    [
      "0064de20",
      "READ",
      [
        "storage",
        "0029f245",
        null,
        "string"
      ]
    ],
    [
      "0064dee0",
      "READ",
      [
        "storage",
        "002b3efb",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0064da54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064d/0064da2c.md#insn-0064da54) · [`0064da5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064d/0064da2c.md#insn-0064da5c) · [`0064da64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064d/0064da2c.md#insn-0064da64)
- 新版 [`0064de04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064d/0064dddc.md#insn-0064de04) · [`0064de0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064d/0064dddc.md#insn-0064de0c) · [`0064de14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064d/0064dddc.md#insn-0064de14)

~~~diff
- 0064da54 ["INT_ADD", "register:40f0:8", ["const:64da54:8", "const:4:8"]]
- 0064da54 ["CALL", null, ["callee:0063ab94:8"]]
+ 0064de04 ["INT_ADD", "register:40f0:8", ["const:64de04:8", "const:4:8"]]
+ 0064de04 ["CALL", null, ["callee:0063ab94:8"]]
- 0064da54 bytes 64b3ff97
+ 0064de04 bytes 64b3ff97
- 0064da5c ["INT_ADD", "register:40f0:8", ["const:64da5c:8", "const:4:8"]]
- 0064da5c ["CALL", null, ["callee:0063bbb4:8"]]
+ 0064de0c ["INT_ADD", "register:40f0:8", ["const:64de0c:8", "const:4:8"]]
+ 0064de0c ["CALL", null, ["callee:0063bbb4:8"]]
- 0064da5c bytes 6ab7ff97
+ 0064de0c bytes 6ab7ff97
- 0064da64 ["COPY", "tmp:0:8", ["const:1fe:8"]]
- 0064da64 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0064da64 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0064da64 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0064de14 ["COPY", "tmp:0:8", ["const:23e:8"]]
+ 0064de14 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0064de14 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0064de14 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0064da64 bytes 29f90791
+ 0064de14 bytes 29f90891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23a40f0b73a2c2487d28cd429a29b858"></a>

### [`0064dc08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064d/0064dc08.md) → [`0064dfb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064d/0064dfb8.md) FUN_0064dfb8

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00655530`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/00655530.md) · 呼出先 12件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`006411b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00641/006411b4.md) [`00641ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00641/00641ca8.md) [`006b7188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b7/006b7188.md) [`0071bf30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071b/0071bf30.md)
- 新版 呼出元 1件 [`006558e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00655/006558e0.md) · 呼出先 12件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00641564`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00641/00641564.md) [`00642058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00642/00642058.md) [`006b7538`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006b7/006b7538.md) [`0071c2e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071c/0071c2e0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 54.17% / 新版 53.06%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0064de98"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0064e248"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "0064dd04"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0064dd04",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071bf30"
      ]
    ],
    [
      "unmatched:0064dd14",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071d254"
      ]
    ],
    [
      "unmatched:0064dd1c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071bf30"
      ]
    ]
  ],
  "added": [
    [
      "0064e0b4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071c2e0"
      ]
    ],
    [
      "0064e0c4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071d604"
      ]
    ],
    [
      "0064e0cc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071c2e0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0064dd04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064d/0064dc08.md#insn-0064dd04) · [`0064dd14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064d/0064dc08.md#insn-0064dd14) · [`0064dd1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064d/0064dc08.md#insn-0064dd1c)

~~~diff
- 0064dd04 ["INT_ADD", "register:40f0:8", ["const:64dd04:8", "const:4:8"]]
- 0064dd04 ["CALL", null, ["ram:71bf30:8"]]
- 0064dd04 bytes 8b380394
- 0064dd14 ["INT_ADD", "register:40f0:8", ["const:64dd14:8", "const:4:8"]]
- 0064dd14 ["CALL", null, ["ram:71d254:8"]]
- 0064dd14 bytes 503d0394
- 0064dd1c ["INT_ADD", "register:40f0:8", ["const:64dd1c:8", "const:4:8"]]
- 0064dd1c ["CALL", null, ["ram:71bf30:8"]]
- 0064dd1c bytes 85380394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e32f7be225f2d0d6d509d9bc8e02ac3"></a>

### [`0064df50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064d/0064df50.md) → [`0064e300`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064e/0064e300.md) FUN_0064e300

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0064a570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064a/0064a570.md) [`006535e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00653/006535e0.md) · 呼出先 8件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`006411b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00641/006411b4.md) [`00641ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00641/00641ca8.md) [`0071bf30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071b/0071bf30.md) [`0071d18c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071d/0071d18c.md)
- 新版 呼出元 2件 [`0064a920`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064a/0064a920.md) [`00653990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00653/00653990.md) · 呼出先 8件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00641564`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00641/00641564.md) [`00642058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00642/00642058.md) [`0071c2e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071c/0071c2e0.md) [`0071d53c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071d/0071d53c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 76.69% / 新版 76.69%

CFGの説明率　旧版 41.94% / 新版 41.94%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 4件, `store_condition` 1件, `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 6件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0064df7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0064df84"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0064e0b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0064df7c",
      "WRITE",
      [
        "storage",
        "Stack[-0xc0]",
        null,
        null
      ]
    ],
    [
      "unmatched:0064df84",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:0064e004",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0064e3c0"
      ]
    ]
  ],
  "added": [
    [
      "0064e32c",
      "WRITE",
      [
        "storage",
        "Stack[-0xc0]",
        null,
        null
      ]
    ],
    [
      "0064e334",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "0064e3b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0064e3c0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0064df7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064d/0064df50.md#insn-0064df7c) · [`0064df84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064d/0064df50.md#insn-0064df84) · [`0064e004`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064d/0064df50.md#insn-0064e004)

~~~diff
- 0064df7c ["COPY", "tmp:0:8", ["register:8:8"]]
- 0064df7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0064df7c bytes e80300f9
- 0064df84 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0064df84 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0064df84 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0064df84 bytes a8831ff8
- 0064e004 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 0064e004 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
- 0064e004 bytes 680000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d595b1b945af7cd3be3df9a7730284d"></a>

### [`0064e1dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064e/0064e1dc.md) → [`0064e58c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064e/0064e58c.md) FUN_0064e58c

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0064a570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064a/0064a570.md) [`006535e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00653/006535e0.md) · 呼出先 8件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`006411b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00641/006411b4.md) [`00641ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00641/00641ca8.md) [`0071bf30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071b/0071bf30.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 2件 [`0064a920`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064a/0064a920.md) [`00653990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00653/00653990.md) · 呼出先 8件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00641564`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00641/00641564.md) [`00642058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00642/00642058.md) [`0071c2e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071c/0071c2e0.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 branch_condition_or_target, call, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 83.90% / 新版 83.90%

CFGの説明率　旧版 65.91% / 新版 63.04%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件, `store_condition` 1件, `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0064e1e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0064e1e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0064e1e4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0064e1e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:0064e1e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:0064e1e8",
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
      "0064e590",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "0064e594",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "0064e598",
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

- 旧版 [`0064e1e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064e/0064e1dc.md#insn-0064e1e0) · [`0064e1e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064e/0064e1dc.md#insn-0064e1e4) · [`0064e1e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064e/0064e1dc.md#insn-0064e1e8)

~~~diff
- 0064e1e0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0064e1e0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0064e1e0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 0064e1e0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0064e1e0 bytes fd7b06a9
- 0064e1e4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:70:8"]]
- 0064e1e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 0064e1e4 bytes f93b00f9
- 0064e1e8 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 0064e1e8 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 0064e1e8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 0064e1e8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0064e1e8 bytes f85f08a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a5cd7d15d1fa3e64701903013617729"></a>

### [`0064e3bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064e/0064e3bc.md) → [`0064e76c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064e/0064e76c.md) FUN_0064e76c

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`0064e3b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064e/0064e3b4.md) [`0064e580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064e/0064e580.md) [`0064ecf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064e/0064ecf8.md) [`006b3bfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b3/006b3bfc.md) · 呼出先 12件 [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047cacc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047cacc.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0063cd5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063c/0063cd5c.md)
- 新版 呼出元 4件 [`0064e764`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064e/0064e764.md) [`0064e930`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064e/0064e930.md) [`0064f0a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064f/0064f0a8.md) [`006b3fac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006b3/006b3fac.md) · 呼出先 12件 [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md) [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047cdec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047c/0047cdec.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`0063d10c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063d/0063d10c.md)

変更の種類 branch_condition_or_target, call, call_count, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 89.38% / 新版 89.38%

CFGの説明率　旧版 70.59% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0064e814",
      "incomplete_value": true,
      "site": "0064e824",
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
                "const:2c4000:8"
              ],
              [
                "leaf",
                "const:458:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0064e464",
      "incomplete_value": true,
      "site": "0064e474",
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
                "const:2c4000:8"
              ],
              [
                "leaf",
                "const:408:8"
              ]
            ]
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
      "site": "0064e570"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0064e920"
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
      "unmatched:0064e3fc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "unmatched:0064e404",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0047cdec"
      ]
    ],
    [
      "unmatched:0064e408",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "0064e7ac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "0064e7b4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0047cdec"
      ]
    ],
    [
      "0064e7b8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0064e3fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064e/0064e3bc.md#insn-0064e3fc) · [`0064e404`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064e/0064e3bc.md#insn-0064e404) · [`0064e408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064e/0064e3bc.md#insn-0064e408)

~~~diff
- 0064e3fc ["INT_ADD", "register:40f0:8", ["const:64e3fc:8", "const:4:8"]]
- 0064e3fc ["CALL", null, ["ram:47ad34:8"]]
- 0064e3fc bytes 4eb2f897
- 0064e404 ["INT_ADD", "register:40f0:8", ["const:64e404:8", "const:4:8"]]
- 0064e404 ["CALL", null, ["callee:0047cdec:8"]]
- 0064e404 bytes b2b9f897
- 0064e408 ["INT_ADD", "register:40f0:8", ["const:64e408:8", "const:4:8"]]
- 0064e408 ["CALL", null, ["ram:47ad34:8"]]
- 0064e408 bytes 4bb2f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42d3291fe7d5d11b588c1c748b253302"></a>

### [`0064e580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064e/0064e580.md) → [`0064e930`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064e/0064e930.md) FUN_0064e930

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`006b2a00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b2/006b2a00.md) · 呼出先 31件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`00470120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470120.md) [`0048ce8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce8c.md) [`005d8c08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d8/005d8c08.md)
- 新版 呼出元 1件 [`006b2db0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006b2/006b2db0.md) · 呼出先 31件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md) [`00470440`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470440.md) [`0048d1ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1ac.md) [`005d8fb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d8/005d8fb8.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 97.08% / 新版 97.08%

CFGの説明率　旧版 87.95% / 新版 84.88%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `store_condition` 1件, `store_value` 3件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0064ec00",
      "incomplete_value": true,
      "site": "0064ec08",
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
                "const:2c4000:8"
              ],
              [
                "leaf",
                "const:458:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0064e850",
      "incomplete_value": true,
      "site": "0064e858",
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
                "const:2c4000:8"
              ],
              [
                "leaf",
                "const:408:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 43,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0064ece0",
      "incomplete_value": false,
      "site": "0064ece0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:fe8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0064e930",
      "incomplete_value": false,
      "site": "0064e930",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "ordinal": 53,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0064ee64",
      "incomplete_value": false,
      "site": "0064ee64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0064eab4",
      "incomplete_value": false,
      "site": "0064eab4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:118:8"
          ]
        ]
      ]
    },
    "ordinal": 65,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0064e968",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "0064e97c",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0064e984",
      "PARAM",
      [
        "storage",
        "00c738e0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0064e968",
      "READ",
      [
        "storage",
        "00ca5a38",
        null,
        "undefined8"
      ]
    ],
    [
      "0064e97c",
      "PARAM",
      [
        "storage",
        "00c66ef8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0064e984",
      "PARAM",
      [
        "storage",
        "00c748b0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0064e5dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064e/0064e580.md#insn-0064e5dc) · [`0064e8bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064e/0064e580.md#insn-0064e8bc) · [`0064e98c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064e/0064e580.md#insn-0064e98c)
- 新版 [`0064e98c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064e/0064e930.md#insn-0064e98c) · [`0064ec6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064e/0064e930.md#insn-0064ec6c) · [`0064ed3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064e/0064e930.md#insn-0064ed3c)

~~~diff
- 0064e5dc ["INT_ADD", "register:40f0:8", ["const:64e5dc:8", "const:4:8"]]
- 0064e5dc ["CALL", null, ["callee:00c596b0:8"]]
+ 0064e98c ["INT_ADD", "register:40f0:8", ["const:64e98c:8", "const:4:8"]]
+ 0064e98c ["CALL", null, ["callee:00c596b0:8"]]
- 0064e5dc bytes 41281894
+ 0064e98c bytes 492b1894
- 0064e8bc ["INT_ADD", "register:40f0:8", ["const:64e8bc:8", "const:4:8"]]
- 0064e8bc ["CALL", null, ["callee:0046cd24:8"]]
+ 0064ec6c ["INT_ADD", "register:40f0:8", ["const:64ec6c:8", "const:4:8"]]
+ 0064ec6c ["CALL", null, ["callee:0046cd24:8"]]
- 0064e8bc bytes 5278f897
+ 0064ec6c bytes 2e78f897
- 0064e98c ["COPY", "register:0:8", ["register:4040:8"]]
- 0064e98c ["INT_ADD", "register:40f0:8", ["const:64e98c:8", "const:4:8"]]
- 0064e98c ["CALLIND", null, ["register:0:8"]]
+ 0064ed3c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0064ed3c ["INT_ADD", "register:40f0:8", ["const:64ed3c:8", "const:4:8"]]
+ 0064ed3c ["CALLIND", null, ["register:0:8"]]
- 0064e98c bytes 00013fd6
+ 0064ed3c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff0922539f4462c80dad8d8f9e3b7315"></a>

### [`006517b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00651/006517b0.md) → [`00651b60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00651/00651b60.md) FUN_00651b60

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00651ae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00651/00651ae4.md) · 呼出先 10件 [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00468c1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468c1c.md) [`00469c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00469/00469c44.md) [`0046af4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046a/0046af4c.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md)
- 新版 呼出元 1件 [`00651e94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00651/00651e94.md) · 呼出先 10件 [`00467bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467bc0.md) [`00468f3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00468/00468f3c.md) [`00469f64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00469/00469f64.md) [`0046b26c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046b/0046b26c.md) [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.80% / 新版 98.80%

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
      "site": "00651d70",
      "value": [
        "leaf",
        "ram:71d53c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006519c0",
      "value": [
        "leaf",
        "ram:71d18c:8"
      ]
    },
    "ordinal": 21,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00651d74",
      "value": [
        "leaf",
        "ram:71c2e0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006519c4",
      "value": [
        "leaf",
        "ram:71bf30:8"
      ]
    },
    "ordinal": 22,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00651d70",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071d18c"
      ]
    ],
    [
      "00651d74",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071bf30"
      ]
    ]
  ],
  "added": [
    [
      "00651d70",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071d53c"
      ]
    ],
    [
      "00651d74",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071c2e0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006519c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00651/006517b0.md#insn-006519c0) · [`006519c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00651/006517b0.md#insn-006519c4) · [`006517ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00651/006517b0.md#insn-006517ec)
- 新版 [`00651d70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00651/00651b60.md#insn-00651d70) · [`00651d74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00651/00651b60.md#insn-00651d74) · [`00651b9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00651/00651b60.md#insn-00651b9c)

~~~diff
- 006519c0 ["INT_ADD", "register:40f0:8", ["const:6519c0:8", "const:4:8"]]
- 006519c0 ["CALL", null, ["ram:71d18c:8"]]
+ 00651d70 ["INT_ADD", "register:40f0:8", ["const:651d70:8", "const:4:8"]]
+ 00651d70 ["CALL", null, ["ram:71d53c:8"]]
- 006519c0 bytes f32d0394
+ 00651d70 bytes f32d0394
- 006519c4 ["INT_ADD", "register:40f0:8", ["const:6519c4:8", "const:4:8"]]
- 006519c4 ["CALL", null, ["ram:71bf30:8"]]
+ 00651d74 ["INT_ADD", "register:40f0:8", ["const:651d74:8", "const:4:8"]]
+ 00651d74 ["CALL", null, ["ram:71c2e0:8"]]
- 006519c4 bytes 5b290394
+ 00651d74 bytes 5b290394
- 006517ec ["INT_ADD", "register:40f0:8", ["const:6517ec:8", "const:4:8"]]
- 006517ec ["CALL", null, ["callee:00467bc0:8"]]
+ 00651b9c ["INT_ADD", "register:40f0:8", ["const:651b9c:8", "const:4:8"]]
+ 00651b9c ["CALL", null, ["callee:00467bc0:8"]]
- 006517ec bytes 2d58f897
+ 00651b9c bytes 0958f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d34b8ba46fdf8a40a585e496ebfc86a4"></a>

### [`00651ae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00651/00651ae4.md) → [`00651e94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00651/00651e94.md) FUN_00651e94

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`006b34d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b3/006b34d8.md) · 呼出先 24件 [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00467b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467b6c.md) [`00467ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467ba0.md) [`00467f94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467f94.md) [`00468844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468844.md)
- 新版 呼出元 1件 [`006b3888`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006b3/006b3888.md) · 呼出先 24件 [`00467bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467bc0.md) [`00467e8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467e8c.md) [`00467ec0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467ec0.md) [`004682b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00468/004682b4.md) [`00468b64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00468/00468b64.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 86.61% / 新版 86.61%

CFGの説明率　旧版 47.76% / 新版 46.04%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 24件, `call_target` 1件, `unresolved_branch_alignment` 14件, `unresolved_call_alignment` 16件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00651e84"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00651e98"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00651ea4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00651f24",
      "DATA",
      [
        "storage",
        "0042ef64",
        null,
        "byte[43]"
      ]
    ],
    [
      "006521f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00651eb0"
      ]
    ],
    [
      "unmatched:00651e64",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008b89cc"
      ]
    ]
  ],
  "added": [
    [
      "00651f24",
      "DATA",
      [
        "storage",
        "0042ef64",
        null,
        "byte[35]"
      ]
    ],
    [
      "006521f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00652260"
      ]
    ],
    [
      "00652214",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008b89cc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00651c84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00651/00651ae4.md#insn-00651c84) · [`00651c8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00651/00651ae4.md#insn-00651c8c) · [`00651cc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00651/00651ae4.md#insn-00651cc0)
- 新版 [`00652034`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00651/00651e94.md#insn-00652034) · [`0065203c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00651/00651e94.md#insn-0065203c) · [`00652070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00651/00651e94.md#insn-00652070)

~~~diff
- 00651c84 ["INT_ADD", "register:40f0:8", ["const:651c84:8", "const:4:8"]]
- 00651c84 ["CALL", null, ["callee:008b89cc:8"]]
+ 00652034 ["INT_ADD", "register:40f0:8", ["const:652034:8", "const:4:8"]]
+ 00652034 ["CALL", null, ["callee:008b89cc:8"]]
- 00651c84 bytes 67970994
+ 00652034 bytes 669a0994
- 00651c8c ["INT_ADD", "register:40f0:8", ["const:651c8c:8", "const:4:8"]]
- 00651c8c ["CALL", null, ["callee:008b7f1c:8"]]
+ 0065203c ["INT_ADD", "register:40f0:8", ["const:65203c:8", "const:4:8"]]
+ 0065203c ["CALL", null, ["callee:008b7f1c:8"]]
- 00651c8c bytes b9940994
+ 0065203c bytes b8970994
- 00651cc0 ["INT_ADD", "register:40f0:8", ["const:651cc0:8", "const:4:8"]]
- 00651cc0 ["CALL", null, ["callee:008524fc:8"]]
+ 00652070 ["INT_ADD", "register:40f0:8", ["const:652070:8", "const:4:8"]]
+ 00652070 ["CALL", null, ["callee:008524fc:8"]]
- 00651cc0 bytes 24fe0794
+ 00652070 bytes 23010894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bbe63d23c1667d25b1b6c2b0580403e5"></a>

### [`0065258c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/0065258c.md) → [`0065293c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00652/0065293c.md) FUN_0065293c

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`0064133c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00641/0064133c.md) [`007906b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00790/007906b4.md) [`00793960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00793/00793960.md) [`00b2afe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2afe4.md) [`00b2b10c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2b/00b2b10c.md) · 呼出先 4件 [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 5件 [`006416ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00641/006416ec.md) [`00790a90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00790/00790a90.md) [`00793d3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00793/00793d3c.md) [`00b2bfd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b2b/00b2bfd8.md) [`00b2c100`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b2c/00b2c100.md) · 呼出先 4件 [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 79.03% / 新版 79.03%

CFGの説明率　旧版 5.26% / 新版 5.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006525a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006525a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006525b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006525a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:006525b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:006525d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006529e8"
      ]
    ]
  ],
  "added": [
    [
      "00652950",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00652968",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00652984",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006529e8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006525a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/0065258c.md#insn-006525a0) · [`006525b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/0065258c.md#insn-006525b8) · [`006525d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/0065258c.md#insn-006525d4)

~~~diff
- 006525a0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 006525a0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 006525a0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 006525a0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 006525a0 bytes f44f08a9
- 006525b8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 006525b8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 006525b8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 006525b8 bytes a8831ff8
- 006525d4 ["CBRANCH", null, ["local:b10:8", "register:101:1"]]
- 006525d4 bytes 20030054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49331bd3def1dd5d087ead57e9193bb1"></a>

### [`00652724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/00652724.md) → [`00652ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00652/00652ad4.md) FUN_00652ad4

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 6件 [`006409f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00640/006409f0.md) [`0064d680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064d/0064d680.md) [`00658dec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00658/00658dec.md) [`0065ad80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0065a/0065ad80.md) [`006b0290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b0/006b0290.md) · 呼出先 5件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0064133c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00641/0064133c.md) [`00652840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/00652840.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 6件 [`00640da0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00640/00640da0.md) [`0064da30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064d/0064da30.md) [`0065919c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00659/0065919c.md) [`0065b130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0065b/0065b130.md) [`006b0640`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006b0/006b0640.md) · 呼出先 5件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`006416ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00641/006416ec.md) [`00652bf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00652/00652bf0.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 55.00% / 新版 55.00%

CFGの説明率　旧版 4.00% / 新版 3.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_condition` 6件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00652728"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00652728"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0065272c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00652728",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:0065272c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00652730",
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
      "00652ad8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00652adc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00652ae0",
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

- 旧版 [`00652728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/00652724.md#insn-00652728) · [`0065272c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/00652724.md#insn-0065272c) · [`00652730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/00652724.md#insn-00652730)

~~~diff
- 00652728 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00652728 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00652728 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00652728 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00652728 bytes fd7b03a9
- 0065272c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 0065272c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 0065272c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 0065272c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0065272c bytes f85f04a9
- 00652730 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00652730 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00652730 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00652730 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00652730 bytes f65705a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f7fd33c36cf9a30035fa2c427fc736f"></a>

### [`00652840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/00652840.md) → [`00652bf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00652/00652bf0.md) FUN_00652bf0

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00652724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/00652724.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00652ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00652/00652ad4.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment

命令の説明率　旧版 98.11% / 新版 98.11%

CFGの説明率　旧版 88.14% / 新版 85.25%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

アドレスに依存する影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00652968"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00652d18"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": null,
    "old": {
      "definition_site": "006529d0",
      "incomplete_value": true,
      "site": "006529d8",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "ordinal": 5,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00652968",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00652d08"
      ]
    ]
  ],
  "added": [
    [
      "00652d18",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00652d08"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00652968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/00652840.md#insn-00652968) · [`006528a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/00652840.md#insn-006528a8)
- 新版 [`00652d18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00652/00652bf0.md#insn-00652d18) · [`00652c58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00652/00652bf0.md#insn-00652c58)

~~~diff
- 00652968 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00652968 ["CBRANCH", null, ["local:b28:8", "tmp:0:1"]]
- 00652968 bytes 81ffff54
+ 00652d18 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00652d18 ["CBRANCH", null, ["local:b28:8", "tmp:0:1"]]
+ 00652d18 bytes 81ffff54
- 006528a8 ["BRANCH", null, ["local:b29:8"]]
+ 00652c58 ["BRANCH", null, ["local:b30:8"]]
- 006528a8 bytes 31000014
+ 00652c58 bytes 31000014
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c6c0efe0eb1a2541e7369063f09e28a"></a>

### [`00652a98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/00652a98.md) → [`00652e48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00652/00652e48.md) FUN_00652e48

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 8件 [`006409f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00640/006409f0.md) [`0064d680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064d/0064d680.md) [`00652a98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/00652a98.md) [`00652c78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/00652c78.md) [`00658dec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00658/00658dec.md) · 呼出先 2件 [`00652a98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/00652a98.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 8件 [`00640da0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00640/00640da0.md) [`0064da30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064d/0064da30.md) [`00652e48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00652/00652e48.md) [`00653028`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00653/00653028.md) [`0065919c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00659/0065919c.md) · 呼出先 2件 [`00652e48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00652/00652e48.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.78% / 新版 97.78%

CFGの説明率　旧版 59.09% / 新版 59.09%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00652e60",
      "incomplete_value": true,
      "site": "00652e68",
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
    "old": null,
    "ordinal": 0,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00652ab8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/00652a98.md#insn-00652ab8) · [`00652a98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/00652a98.md#insn-00652a98) · [`00652aa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/00652a98.md#insn-00652aa8)
- 新版 [`00652e68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00652/00652e48.md#insn-00652e68) · [`00652e48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00652/00652e48.md#insn-00652e48)

~~~diff
- 00652ab8 ["INT_ADD", "register:40f0:8", ["const:652ab8:8", "const:4:8"]]
- 00652ab8 ["CALL", null, ["local:b0:8"]]
+ 00652e68 ["INT_ADD", "register:40f0:8", ["const:652e68:8", "const:4:8"]]
+ 00652e68 ["CALL", null, ["local:b0:8"]]
- 00652ab8 bytes f8ffff97
+ 00652e68 bytes f8ffff97
- 00652a98 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00652a98 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
+ 00652e48 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00652e48 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00652a98 bytes 810300b4
+ 00652e48 bytes 810300b4
- 00652aa8 ["COPY", "register:40e8:8", ["register:8:8"]]
- 00652aa8 bytes fd030091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8357bbae8749a77ed33e5bad7fdaf7f5"></a>

### [`00652b4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/00652b4c.md) → [`00652efc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00652/00652efc.md) FUN_00652efc

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0063c60c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063c/0063c60c.md) [`0063cd5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063c/0063cd5c.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 2件 [`0063c9bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063c/0063c9bc.md) [`0063d10c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063d/0063d10c.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "00652f08",
      "incomplete_value": false,
      "site": "00652f0c",
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
            "const:5b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00652b58",
      "incomplete_value": false,
      "site": "00652b5c",
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
            "const:f8c:8"
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
      "00652f08",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00652f08",
      "PARAM",
      [
        "storage",
        "002b805b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00652b5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/00652b4c.md#insn-00652b5c) · [`00652b54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/00652b4c.md#insn-00652b54) · [`00652b58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/00652b4c.md#insn-00652b58)
- 新版 [`00652f0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00652/00652efc.md#insn-00652f0c) · [`00652f04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00652/00652efc.md#insn-00652f04) · [`00652f08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00652/00652efc.md#insn-00652f08)

~~~diff
- 00652b5c ["INT_ADD", "register:40f0:8", ["const:652b5c:8", "const:4:8"]]
- 00652b5c ["CALL", null, ["callee:0043bad8:8"]]
+ 00652f0c ["INT_ADD", "register:40f0:8", ["const:652f0c:8", "const:4:8"]]
+ 00652f0c ["CALL", null, ["callee:0043bad8:8"]]
- 00652b5c bytes 17a3f797
+ 00652f0c bytes f3a2f797
- 00652b54 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 00652f04 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 00652b54 bytes 20e3ffb0
+ 00652f04 bytes 20e3ffd0
- 00652b58 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 00652b58 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00652b58 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00652b58 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00652f08 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 00652f08 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00652f08 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00652f08 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00652b58 bytes 00303e91
+ 00652f08 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2abe1922543a87a0583254aac8b405bb"></a>

### [`00652c78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/00652c78.md) → [`00653028`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00653/00653028.md) FUN_00653028

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`0063dd50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063d/0063dd50.md) [`00652c78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/00652c78.md) [`00866da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00866/00866da0.md) · 呼出先 3件 [`00652a98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/00652a98.md) [`00652c78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/00652c78.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 3件 [`0063e100`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063e/0063e100.md) [`00653028`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00653/00653028.md) [`00867d4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00867/00867d4c.md) · 呼出先 3件 [`00652e48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00652/00652e48.md) [`00653028`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00653/00653028.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 65.00% / 新版 65.00%

CFGの説明率　旧版 33.33% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00652c7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00652c7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00652c80"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00652c7c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00652c80",
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
      "0065302c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00653030",
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

- 旧版 [`00652c7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/00652c78.md#insn-00652c7c) · [`00652c80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/00652c78.md#insn-00652c80) · [`00652c98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/00652c78.md#insn-00652c98)
- 新版 [`00653048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00653/00653028.md#insn-00653048)

~~~diff
- 00652c7c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00652c7c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00652c7c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00652c7c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00652c7c bytes fd7bbea9
- 00652c80 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00652c80 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00652c80 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00652c80 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00652c80 bytes f44f01a9
- 00652c98 ["INT_ADD", "register:40f0:8", ["const:652c98:8", "const:4:8"]]
- 00652c98 ["CALL", null, ["local:b0:8"]]
+ 00653048 ["INT_ADD", "register:40f0:8", ["const:653048:8", "const:4:8"]]
+ 00653048 ["CALL", null, ["local:b0:8"]]
- 00652c98 bytes f8ffff97
+ 00653048 bytes f8ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2337f655cb17e8d2d8e4ffd972ff44f4"></a>

### [`00652cc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/00652cc8.md) → [`00653078`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00653/00653078.md) FUN_00653078

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 3件 [`0063dd50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063d/0063dd50.md) [`00652cc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/00652cc8.md) [`00866da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00866/00866da0.md) · 呼出先 2件 [`00652cc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/00652cc8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 3件 [`0063e100`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063e/0063e100.md) [`00653078`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00653/00653078.md) [`00867d4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00867/00867d4c.md) · 呼出先 2件 [`00653078`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00653/00653078.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

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
      "definition_site": "00652cec",
      "incomplete_value": true,
      "site": "00652cf4",
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
                "live",
                "register:40a0:8"
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
    "ordinal": 1,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00652cf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/00652cc8.md#insn-00652cf4) · [`00652cc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/00652cc8.md#insn-00652cc8) · [`00652ce8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/00652cc8.md#insn-00652ce8)
- 新版 [`006530a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00653/00653078.md#insn-006530a4) · [`00653078`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00653/00653078.md#insn-00653078) · [`00653098`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00653/00653078.md#insn-00653098)

~~~diff
- 00652cf4 ["INT_ADD", "register:40f0:8", ["const:652cf4:8", "const:4:8"]]
- 00652cf4 ["CALL", null, ["local:b0:8"]]
+ 006530a4 ["INT_ADD", "register:40f0:8", ["const:6530a4:8", "const:4:8"]]
+ 006530a4 ["CALL", null, ["local:b0:8"]]
- 00652cf4 bytes f5ffff97
+ 006530a4 bytes f5ffff97
- 00652cc8 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00652cc8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00653078 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00653078 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00652cc8 bytes 010200b4
+ 00653078 bytes 010200b4
- 00652ce8 ["INT_ADD", "register:40f0:8", ["const:652ce8:8", "const:4:8"]]
- 00652ce8 ["CALL", null, ["local:b0:8"]]
+ 00653098 ["INT_ADD", "register:40f0:8", ["const:653098:8", "const:4:8"]]
+ 00653098 ["CALL", null, ["local:b0:8"]]
- 00652ce8 bytes f8ffff97
+ 00653098 bytes f8ffff97
~~~


<a id="compare-fd3db3a59ff766294ea36288fa16131f"></a>

### [`00652d0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/00652d0c.md) → [`006530bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00653/006530bc.md) FUN_006530bc

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 8件 [`0063dd50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063d/0063dd50.md) [`00652d0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/00652d0c.md) [`006584c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00658/006584c8.md) [`0084e5f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0084e/0084e5f4.md) [`00865d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00865/00865d00.md) · 呼出先 2件 [`00652d0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/00652d0c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 8件 [`0063e100`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0063e/0063e100.md) [`006530bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00653/006530bc.md) [`00658878`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00658/00658878.md) [`0084f5a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0084f/0084f5a0.md) [`00866cac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00866/00866cac.md) · 呼出先 2件 [`006530bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00653/006530bc.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 83.78% / 新版 83.78%

CFGの説明率　旧版 29.41% / 新版 31.25%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00652d10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00652d10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00652d14"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00652d10",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00652d14",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00652d18",
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
      "006530c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "006530c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "006530c8",
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

- 旧版 [`00652d10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/00652d0c.md#insn-00652d10) · [`00652d14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/00652d0c.md#insn-00652d14) · [`00652d18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/00652d0c.md#insn-00652d18)

~~~diff
- 00652d10 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00652d10 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00652d10 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00652d10 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00652d10 bytes fd7bbda9
- 00652d14 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00652d14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00652d14 bytes f50b00f9
- 00652d18 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00652d18 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00652d18 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00652d18 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00652d18 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7852357d054f96462265f8a2730115a6"></a>

### [`00652da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/00652da0.md) → [`00653150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00653/00653150.md) FUN_00653150

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 7件 [`00642050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00642/00642050.md) [`00677a80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00677/00677a80.md) [`0075ebd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075e/0075ebd8.md) [`00763db0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00763/00763db0.md) [`007647c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/007647c8.md) · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0063678c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00636/0063678c.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 7件 [`00642400`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00642/00642400.md) [`00677e30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00677/00677e30.md) [`0075ef88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075e/0075ef88.md) [`0076418c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00764/0076418c.md) [`00764ba4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00764/00764ba4.md) · 呼出先 6件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00636b3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00636/00636b3c.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 82.50% / 新版 82.50%

CFGの説明率　旧版 41.94% / 新版 41.94%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00652e30"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "006531e0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00652dec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00652e3c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00653254"
      ]
    ],
    [
      "unmatched:00652e90",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "006531ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00653254"
      ]
    ],
    [
      "00653240",
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

- 旧版 [`00652dec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/00652da0.md#insn-00652dec) · [`00652df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/00652da0.md#insn-00652df8) · [`00652e30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/00652da0.md#insn-00652e30)

~~~diff
- 00652dec ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00652dec ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00652dec ["COPY", "tmp:2:8", ["register:4050:8"]]
- 00652dec ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 00652dec bytes 4881889a
- 00652df8 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00652df8 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00652df8 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00652df8 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00652df8 bytes 1631899a
- 00652e30 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00652e30 ["INT_ADD", "register:40a0:8", ["register:40a0:8", "const:10:8"]]
- 00652e30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00652e30 bytes 8006813c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ede7ddcf6ba9f56e8259db7c85760bf"></a>

### [`00652ee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/00652ee0.md) → [`00653290`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00653/00653290.md) FUN_00653290

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00643130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00643/00643130.md) · 呼出先 7件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`00653174`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00653/00653174.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`006434e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00643/006434e0.md) · 呼出先 7件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`00653524`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00653/00653524.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 14.29% / 新版 14.04%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件, `unresolved_branch_alignment` 10件, `unresolved_store_alignment` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00652f0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00652f38"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00652f84"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00652f0c",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00652f24",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00653434"
      ]
    ],
    [
      "unmatched:00652f38",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "006532bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "006532d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00653434"
      ]
    ],
    [
      "006532e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00652f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/00652ee0.md#insn-00652f0c) · [`00652f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/00652ee0.md#insn-00652f24) · [`00652f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/00652ee0.md#insn-00652f38)

~~~diff
- 00652f0c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00652f0c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00652f0c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00652f0c bytes a8831ff8
- 00652f24 ["INT_NOTEQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00652f24 ["CBRANCH", null, ["local:b38:8", "tmp:0:1"]]
- 00652f24 bytes 090b00b5
- 00652f38 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00652f38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00652f38 bytes e91300f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71ea7326bc048c447efb2e16e0bd3454"></a>

### [`00653174`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00653/00653174.md) → [`00653524`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00653/00653524.md) FUN_00653524

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00645010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00645/00645010.md) [`00652ee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/00652ee0.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 2件 [`006453c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00645/006453c0.md) [`00653290`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00653/00653290.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "00653530",
      "incomplete_value": false,
      "site": "00653534",
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
            "const:5b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00653180",
      "incomplete_value": false,
      "site": "00653184",
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
            "const:f8c:8"
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
      "00653530",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00653530",
      "PARAM",
      [
        "storage",
        "002b805b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00653184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00653/00653174.md#insn-00653184) · [`0065317c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00653/00653174.md#insn-0065317c) · [`00653180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00653/00653174.md#insn-00653180)
- 新版 [`00653534`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00653/00653524.md#insn-00653534) · [`0065352c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00653/00653524.md#insn-0065352c) · [`00653530`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00653/00653524.md#insn-00653530)

~~~diff
- 00653184 ["INT_ADD", "register:40f0:8", ["const:653184:8", "const:4:8"]]
- 00653184 ["CALL", null, ["callee:0043bad8:8"]]
+ 00653534 ["INT_ADD", "register:40f0:8", ["const:653534:8", "const:4:8"]]
+ 00653534 ["CALL", null, ["callee:0043bad8:8"]]
- 00653184 bytes 8da1f797
+ 00653534 bytes 69a1f797
- 0065317c ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 0065352c ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 0065317c bytes 20e3ff90
+ 0065352c bytes 20e3ffb0
- 00653180 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 00653180 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00653180 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00653180 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00653530 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 00653530 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00653530 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00653530 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00653180 bytes 00303e91
+ 00653530 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e8dd32e86fac755e7b310cf3b5aa106"></a>

### [`00653188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00653/00653188.md) → [`00653538`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00653/00653538.md) FUN_00653538

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00645010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00645/00645010.md) · 呼出先 3件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`006453c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00645/006453c0.md) · 呼出先 3件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 89.34% / 新版 89.34%

CFGの説明率　旧版 52.63% / 新版 47.62%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 4件, `unresolved_branch_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00653198"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00653198"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0065328c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00653198",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00653208",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00653698"
      ]
    ],
    [
      "unmatched:006532a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00653624"
      ]
    ]
  ],
  "added": [
    [
      "00653548",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "006535b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00653698"
      ]
    ],
    [
      "00653658",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00653624"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00653198`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00653/00653188.md#insn-00653198) · [`00653208`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00653/00653188.md#insn-00653208) · [`00653258`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00653/00653188.md#insn-00653258)
- 新版 [`00653608`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00653/00653538.md#insn-00653608)

~~~diff
- 00653198 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00653198 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00653198 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00653198 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00653198 bytes f44f04a9
- 00653208 ["CBRANCH", null, ["local:b19:8", "register:101:1"]]
- 00653208 bytes 00070054
- 00653258 ["INT_ADD", "register:40f0:8", ["const:653258:8", "const:4:8"]]
- 00653258 ["CALL", null, ["callee:00c58f30:8"]]
+ 00653608 ["INT_ADD", "register:40f0:8", ["const:653608:8", "const:4:8"]]
+ 00653608 ["CALL", null, ["callee:00c58f30:8"]]
- 00653258 bytes 42131894
+ 00653608 bytes 4a161894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e25ff159435b52bd4bb8f7ccc5b1863a"></a>

### [`00653370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00653/00653370.md) → [`00653720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00653/00653720.md) FUN_00653720

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00645010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00645/00645010.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`006453c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00645/006453c0.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 86.96% / 新版 86.96%

CFGの説明率　旧版 11.11% / 新版 11.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 2件, `unresolved_branch_alignment` 5件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006534bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006534c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006534c8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006533dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00653758"
      ]
    ],
    [
      "00653794",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:006533f4"
      ]
    ],
    [
      "unmatched:006533f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006537b8"
      ]
    ]
  ],
  "added": [
    [
      "0065378c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00653758"
      ]
    ],
    [
      "00653794",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "006537a4"
      ]
    ],
    [
      "006537a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006537b8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006533dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00653/00653370.md#insn-006533dc) · [`006533f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00653/00653370.md#insn-006533f0) · [`006533f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00653/00653370.md#insn-006533f8)

~~~diff
- 006533dc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 006533dc ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 006533dc bytes 61feff54
- 006533f0 ["CBRANCH", null, ["local:b9:8", "register:101:1"]]
- 006533f0 bytes c0000054
- 006533f8 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 006533f8 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 006533f8 bytes 80ffffb4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5cb47b53549c91399fd207edd4cf40b2"></a>

### [`006534e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00653/006534e8.md) → [`00653898`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00653/00653898.md) FUN_00653898

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "006538ac",
      "incomplete_value": false,
      "site": "006538b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:8d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006534fc",
      "incomplete_value": false,
      "site": "00653500",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:908:8"
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
      "006538b0",
      "DATA",
      [
        "storage",
        "00c73908",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006538b0",
      "DATA",
      [
        "storage",
        "00c748d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006534f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00653/006534e8.md#insn-006534f4) · [`006534f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00653/006534e8.md#insn-006534f8) · [`006534fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00653/006534e8.md#insn-006534fc)
- 新版 [`006538a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00653/00653898.md#insn-006538a4) · [`006538a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00653/00653898.md#insn-006538a8) · [`006538ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00653/00653898.md#insn-006538ac)

~~~diff
- 006534f4 ["INT_ADD", "register:40f0:8", ["const:6534f4:8", "const:4:8"]]
- 006534f4 ["CALL", null, ["callee:00c58f30:8"]]
+ 006538a4 ["INT_ADD", "register:40f0:8", ["const:6538a4:8", "const:4:8"]]
+ 006538a4 ["CALL", null, ["callee:00c58f30:8"]]
- 006534f4 bytes 9b121894
+ 006538a4 bytes a3151894
- 006534f8 ["COPY", "register:4040:8", ["const:c73000:8"]]
+ 006538a8 ["COPY", "register:4040:8", ["const:c74000:8"]]
- 006534f8 bytes 08310090
+ 006538a8 bytes 083100b0
- 006534fc ["COPY", "tmp:0:8", ["const:908:8"]]
- 006534fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006534fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006534fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006538ac ["COPY", "tmp:0:8", ["const:8d8:8"]]
+ 006538ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006538ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006538ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006534fc bytes 08212491
+ 006538ac bytes 08612391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5df4b26be1610515ad67541b9fec03fa"></a>

### [`0065350c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00653/0065350c.md) → [`006538bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00653/006538bc.md) FUN_006538bc

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006538c0",
      "incomplete_value": false,
      "site": "006538c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:8d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00653510",
      "incomplete_value": false,
      "site": "00653514",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:908:8"
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
      "006538c4",
      "DATA",
      [
        "storage",
        "00c73908",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006538c4",
      "DATA",
      [
        "storage",
        "00c748d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0065350c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00653/0065350c.md#insn-0065350c) · [`00653510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00653/0065350c.md#insn-00653510)
- 新版 [`006538bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00653/006538bc.md#insn-006538bc) · [`006538c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00653/006538bc.md#insn-006538c0)

~~~diff
- 0065350c ["COPY", "register:4040:8", ["const:c73000:8"]]
+ 006538bc ["COPY", "register:4040:8", ["const:c74000:8"]]
- 0065350c bytes 08310090
+ 006538bc bytes 083100b0
- 00653510 ["COPY", "tmp:0:8", ["const:908:8"]]
- 00653510 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00653510 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00653510 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006538c0 ["COPY", "tmp:0:8", ["const:8d8:8"]]
+ 006538c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006538c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006538c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00653510 bytes 08212491
+ 006538c0 bytes 08612391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-727002754d8d34de6b654c0e88a7e91f"></a>

### [`00653558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00653/00653558.md) → [`00653908`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00653/00653908.md) FUN_00653908

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0065357c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0065357c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0065392c"
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
      "unmatched:0065357c",
      "DATA",
      [
        "storage",
        "00c73998",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00653580",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00653584",
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
      "0065392c",
      "DATA",
      [
        "storage",
        "00c74968",
        null,
        "undefined *"
      ]
    ],
    [
      "00653930",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00653934",
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

- 旧版 [`0065356c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00653/00653558.md#insn-0065356c) · [`0065357c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00653/00653558.md#insn-0065357c) · [`00653588`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00653/00653558.md#insn-00653588)
- 新版 [`0065391c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00653/00653908.md#insn-0065391c)

~~~diff
- 0065356c ["INT_ADD", "register:40f0:8", ["const:65356c:8", "const:4:8"]]
- 0065356c ["CALL", null, ["callee:00c58f30:8"]]
+ 0065391c ["INT_ADD", "register:40f0:8", ["const:65391c:8", "const:4:8"]]
+ 0065391c ["CALL", null, ["callee:00c58f30:8"]]
- 0065356c bytes 7d121894
+ 0065391c bytes 85151894
- 0065357c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0065357c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 0065357c ["COPY", "tmp:2:8", ["register:4000:8"]]
- 0065357c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0065357c bytes 082400a9
- 00653588 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00653588 ["RETURN", null, ["register:0:8"]]
- 00653588 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b56ad665907e2a52e09c9040f37329da"></a>

### [`006535a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00653/006535a8.md) → [`00653958`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00653/00653958.md) FUN_00653958

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 1件 [`006535e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00653/006535e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00653990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00653/00653990.md)

変更の種類 cfg_edge_inventory

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-c8458aab861933a9c405d67aee971d00"></a>

### [`006535e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00653/006535e0.md) → [`00653990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00653/00653990.md) FUN_00653990

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`006535a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00653/006535a8.md) · 呼出先 45件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md)
- 新版 呼出元 1件 [`00653958`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00653/00653958.md) · 呼出先 45件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00448254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448254.md) [`0046d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md) [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 54.15% / 新版 54.15%

CFGの説明率　旧版 19.13% / 新版 19.13%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 58件, `call_target` 4件, `unresolved_branch_alignment` 57件, `unresolved_call_alignment` 97件, `unresolved_store_alignment` 46件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00653610"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00653868"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00653874"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00653610",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00653614",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00653a10"
      ]
    ],
    [
      "unmatched:00653618",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008524fc"
      ]
    ]
  ],
  "added": [
    [
      "006539c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "006539c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00653a10"
      ]
    ],
    [
      "006539c8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008524fc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00653610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00653/006535e0.md#insn-00653610) · [`00653824`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00653/006535e0.md#insn-00653824) · [`00653830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00653/006535e0.md#insn-00653830)
- 新版 [`00653bd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00653/00653990.md#insn-00653bd4) · [`00653be0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00653/00653990.md#insn-00653be0)

~~~diff
- 00653610 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00653610 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00653610 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00653610 bytes a8831ff8
- 00653824 ["INT_ADD", "register:40f0:8", ["const:653824:8", "const:4:8"]]
- 00653824 ["CALL", null, ["callee:008524fc:8"]]
+ 00653bd4 ["INT_ADD", "register:40f0:8", ["const:653bd4:8", "const:4:8"]]
+ 00653bd4 ["CALL", null, ["callee:008524fc:8"]]
- 00653824 bytes 4bf70794
+ 00653bd4 bytes 4afa0794
- 00653830 ["INT_ADD", "register:40f0:8", ["const:653830:8", "const:4:8"]]
- 00653830 ["CALL", null, ["callee:00b30a48:8"]]
+ 00653be0 ["INT_ADD", "register:40f0:8", ["const:653be0:8", "const:4:8"]]
+ 00653be0 ["CALL", null, ["callee:00b30a48:8"]]
- 00653830 bytes 89701394
+ 00653be0 bytes 9a731394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80c2fff5aa6d761be459384953a5ca9d"></a>

### [`006550f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/006550f8.md) → [`006554a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00655/006554a8.md) FUN_006554a8

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "006554bc",
      "incomplete_value": false,
      "site": "006554c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:9d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0065510c",
      "incomplete_value": false,
      "site": "00655110",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:a08:8"
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
      "006554c0",
      "DATA",
      [
        "storage",
        "00c73a08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006554c0",
      "DATA",
      [
        "storage",
        "00c749d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00655104`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/006550f8.md#insn-00655104) · [`00655108`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/006550f8.md#insn-00655108) · [`0065510c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/006550f8.md#insn-0065510c)
- 新版 [`006554b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00655/006554a8.md#insn-006554b4) · [`006554b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00655/006554a8.md#insn-006554b8) · [`006554bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00655/006554a8.md#insn-006554bc)

~~~diff
- 00655104 ["INT_ADD", "register:40f0:8", ["const:655104:8", "const:4:8"]]
- 00655104 ["CALL", null, ["callee:00c58f30:8"]]
+ 006554b4 ["INT_ADD", "register:40f0:8", ["const:6554b4:8", "const:4:8"]]
+ 006554b4 ["CALL", null, ["callee:00c58f30:8"]]
- 00655104 bytes 970b1894
+ 006554b4 bytes 9f0e1894
- 00655108 ["COPY", "register:4040:8", ["const:c73000:8"]]
+ 006554b8 ["COPY", "register:4040:8", ["const:c74000:8"]]
- 00655108 bytes e83000d0
+ 006554b8 bytes e83000f0
- 0065510c ["COPY", "tmp:0:8", ["const:a08:8"]]
- 0065510c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0065510c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0065510c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006554bc ["COPY", "tmp:0:8", ["const:9d8:8"]]
+ 006554bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006554bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006554bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0065510c bytes 08212891
+ 006554bc bytes 08612791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-abb8da8a7c3df00cd76a0f87d3f8b397"></a>

### [`0065511c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/0065511c.md) → [`006554cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00655/006554cc.md) FUN_006554cc

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006554d0",
      "incomplete_value": false,
      "site": "006554d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:9d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00655120",
      "incomplete_value": false,
      "site": "00655124",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:a08:8"
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
      "006554d4",
      "DATA",
      [
        "storage",
        "00c73a08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006554d4",
      "DATA",
      [
        "storage",
        "00c749d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0065511c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/0065511c.md#insn-0065511c) · [`00655120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/0065511c.md#insn-00655120)
- 新版 [`006554cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00655/006554cc.md#insn-006554cc) · [`006554d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00655/006554cc.md#insn-006554d0)

~~~diff
- 0065511c ["COPY", "register:4040:8", ["const:c73000:8"]]
+ 006554cc ["COPY", "register:4040:8", ["const:c74000:8"]]
- 0065511c bytes e83000d0
+ 006554cc bytes e83000f0
- 00655120 ["COPY", "tmp:0:8", ["const:a08:8"]]
- 00655120 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00655120 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00655120 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006554d0 ["COPY", "tmp:0:8", ["const:9d8:8"]]
+ 006554d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006554d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006554d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00655120 bytes 08212891
+ 006554d0 bytes 08612791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-679eebf500afcf1e3c0f814af03631f4"></a>

### [`006551c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/006551c0.md) → [`00655570`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00655/00655570.md) FUN_00655570

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "00655584",
      "incomplete_value": false,
      "site": "00655588",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:a58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006551d4",
      "incomplete_value": false,
      "site": "006551d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:a88:8"
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
      "00655588",
      "DATA",
      [
        "storage",
        "00c73a88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00655588",
      "DATA",
      [
        "storage",
        "00c74a58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006551cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/006551c0.md#insn-006551cc) · [`006551d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/006551c0.md#insn-006551d0) · [`006551d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/006551c0.md#insn-006551d4)
- 新版 [`0065557c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00655/00655570.md#insn-0065557c) · [`00655580`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00655/00655570.md#insn-00655580) · [`00655584`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00655/00655570.md#insn-00655584)

~~~diff
- 006551cc ["INT_ADD", "register:40f0:8", ["const:6551cc:8", "const:4:8"]]
- 006551cc ["CALL", null, ["callee:00c58f30:8"]]
+ 0065557c ["INT_ADD", "register:40f0:8", ["const:65557c:8", "const:4:8"]]
+ 0065557c ["CALL", null, ["callee:00c58f30:8"]]
- 006551cc bytes 650b1894
+ 0065557c bytes 6d0e1894
- 006551d0 ["COPY", "register:4040:8", ["const:c73000:8"]]
+ 00655580 ["COPY", "register:4040:8", ["const:c74000:8"]]
- 006551d0 bytes e83000d0
+ 00655580 bytes e83000f0
- 006551d4 ["COPY", "tmp:0:8", ["const:a88:8"]]
- 006551d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006551d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006551d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00655584 ["COPY", "tmp:0:8", ["const:a58:8"]]
+ 00655584 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00655584 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00655584 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006551d4 bytes 08212a91
+ 00655584 bytes 08612991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4215426f7efd7c312d87ed6719d5ba78"></a>

### [`006551e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/006551e4.md) → [`00655594`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00655/00655594.md) FUN_00655594

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00655598",
      "incomplete_value": false,
      "site": "0065559c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:a58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006551e8",
      "incomplete_value": false,
      "site": "006551ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:a88:8"
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
      "0065559c",
      "DATA",
      [
        "storage",
        "00c73a88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0065559c",
      "DATA",
      [
        "storage",
        "00c74a58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006551e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/006551e4.md#insn-006551e4) · [`006551e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/006551e4.md#insn-006551e8)
- 新版 [`00655594`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00655/00655594.md#insn-00655594) · [`00655598`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00655/00655594.md#insn-00655598)

~~~diff
- 006551e4 ["COPY", "register:4040:8", ["const:c73000:8"]]
+ 00655594 ["COPY", "register:4040:8", ["const:c74000:8"]]
- 006551e4 bytes e83000d0
+ 00655594 bytes e83000f0
- 006551e8 ["COPY", "tmp:0:8", ["const:a88:8"]]
- 006551e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006551e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006551e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00655598 ["COPY", "tmp:0:8", ["const:a58:8"]]
+ 00655598 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00655598 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00655598 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006551e8 bytes 08212a91
+ 00655598 bytes 08612991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7789a9c995d0a5d7e9091e94cb921142"></a>

### [`00655288`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/00655288.md) → [`00655638`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00655/00655638.md) FUN_00655638

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "0065564c",
      "incomplete_value": false,
      "site": "00655650",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:ad8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0065529c",
      "incomplete_value": false,
      "site": "006552a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:b08:8"
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
      "00655650",
      "DATA",
      [
        "storage",
        "00c73b08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00655650",
      "DATA",
      [
        "storage",
        "00c74ad8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00655294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/00655288.md#insn-00655294) · [`00655298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/00655288.md#insn-00655298) · [`0065529c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/00655288.md#insn-0065529c)
- 新版 [`00655644`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00655/00655638.md#insn-00655644) · [`00655648`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00655/00655638.md#insn-00655648) · [`0065564c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00655/00655638.md#insn-0065564c)

~~~diff
- 00655294 ["INT_ADD", "register:40f0:8", ["const:655294:8", "const:4:8"]]
- 00655294 ["CALL", null, ["callee:00c58f30:8"]]
+ 00655644 ["INT_ADD", "register:40f0:8", ["const:655644:8", "const:4:8"]]
+ 00655644 ["CALL", null, ["callee:00c58f30:8"]]
- 00655294 bytes 330b1894
+ 00655644 bytes 3b0e1894
- 00655298 ["COPY", "register:4040:8", ["const:c73000:8"]]
+ 00655648 ["COPY", "register:4040:8", ["const:c74000:8"]]
- 00655298 bytes e83000d0
+ 00655648 bytes e83000f0
- 0065529c ["COPY", "tmp:0:8", ["const:b08:8"]]
- 0065529c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0065529c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0065529c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0065564c ["COPY", "tmp:0:8", ["const:ad8:8"]]
+ 0065564c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0065564c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0065564c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0065529c bytes 08212c91
+ 0065564c bytes 08612b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5d30963584017b3fe8a817d61f86bb6"></a>

### [`006552ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/006552ac.md) → [`0065565c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00655/0065565c.md) FUN_0065565c

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00655660",
      "incomplete_value": false,
      "site": "00655664",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:ad8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006552b0",
      "incomplete_value": false,
      "site": "006552b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:b08:8"
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
      "00655664",
      "DATA",
      [
        "storage",
        "00c73b08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00655664",
      "DATA",
      [
        "storage",
        "00c74ad8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006552ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/006552ac.md#insn-006552ac) · [`006552b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/006552ac.md#insn-006552b0)
- 新版 [`0065565c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00655/0065565c.md#insn-0065565c) · [`00655660`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00655/0065565c.md#insn-00655660)

~~~diff
- 006552ac ["COPY", "register:4040:8", ["const:c73000:8"]]
+ 0065565c ["COPY", "register:4040:8", ["const:c74000:8"]]
- 006552ac bytes e83000d0
+ 0065565c bytes e83000f0
- 006552b0 ["COPY", "tmp:0:8", ["const:b08:8"]]
- 006552b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006552b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006552b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00655660 ["COPY", "tmp:0:8", ["const:ad8:8"]]
+ 00655660 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00655660 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00655660 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006552b0 bytes 08212c91
+ 00655660 bytes 08612b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a5b802d603392ed3cfaf39e66a100d6"></a>

### [`00655374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/00655374.md) → [`00655724`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00655/00655724.md) FUN_00655724

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00655728",
      "incomplete_value": false,
      "site": "0065572c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:b58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00655378",
      "incomplete_value": false,
      "site": "0065537c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:b88:8"
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
      "0065572c",
      "DATA",
      [
        "storage",
        "00c73b88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0065572c",
      "DATA",
      [
        "storage",
        "00c74b58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00655374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/00655374.md#insn-00655374) · [`00655378`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/00655374.md#insn-00655378)
- 新版 [`00655724`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00655/00655724.md#insn-00655724) · [`00655728`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00655/00655724.md#insn-00655728)

~~~diff
- 00655374 ["COPY", "register:4040:8", ["const:c73000:8"]]
+ 00655724 ["COPY", "register:4040:8", ["const:c74000:8"]]
- 00655374 bytes e83000d0
+ 00655724 bytes e83000f0
- 00655378 ["COPY", "tmp:0:8", ["const:b88:8"]]
- 00655378 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00655378 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00655378 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00655728 ["COPY", "tmp:0:8", ["const:b58:8"]]
+ 00655728 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00655728 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00655728 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00655378 bytes 08212e91
+ 00655728 bytes 08612d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1540619e682bb069513855b7f749a156"></a>

### [`0065543c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/0065543c.md) → [`006557ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00655/006557ec.md) FUN_006557ec

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006557f0",
      "incomplete_value": false,
      "site": "006557f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:bd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00655440",
      "incomplete_value": false,
      "site": "00655444",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:c08:8"
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
      "006557f4",
      "DATA",
      [
        "storage",
        "00c73c08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006557f4",
      "DATA",
      [
        "storage",
        "00c74bd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0065543c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/0065543c.md#insn-0065543c) · [`00655440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/0065543c.md#insn-00655440)
- 新版 [`006557ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00655/006557ec.md#insn-006557ec) · [`006557f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00655/006557ec.md#insn-006557f0)

~~~diff
- 0065543c ["COPY", "register:4040:8", ["const:c73000:8"]]
+ 006557ec ["COPY", "register:4040:8", ["const:c74000:8"]]
- 0065543c bytes e83000d0
+ 006557ec bytes e83000f0
- 00655440 ["COPY", "tmp:0:8", ["const:c08:8"]]
- 00655440 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00655440 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00655440 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006557f0 ["COPY", "tmp:0:8", ["const:bd8:8"]]
+ 006557f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006557f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006557f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00655440 bytes 08213091
+ 006557f0 bytes 08612f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-587d79d6c1c95b92b560e2735882cee6"></a>

### [`006554e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/006554e0.md) → [`00655890`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00655/00655890.md) FUN_00655890

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "006558b4",
      "incomplete_value": false,
      "site": "006558b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:c58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00655504",
      "incomplete_value": false,
      "site": "00655504",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:c88:8"
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
      "006558b4",
      "DATA",
      [
        "storage",
        "00c73c88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006558b4",
      "DATA",
      [
        "storage",
        "00c74c58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006554f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/006554e0.md#insn-006554f4) · [`006554fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/006554e0.md#insn-006554fc) · [`00655500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/006554e0.md#insn-00655500)
- 新版 [`006558a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00655/00655890.md#insn-006558a4) · [`006558ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00655/00655890.md#insn-006558ac) · [`006558b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00655/00655890.md#insn-006558b0)

~~~diff
- 006554f4 ["INT_ADD", "register:40f0:8", ["const:6554f4:8", "const:4:8"]]
- 006554f4 ["CALL", null, ["callee:00c58f30:8"]]
+ 006558a4 ["INT_ADD", "register:40f0:8", ["const:6558a4:8", "const:4:8"]]
+ 006558a4 ["CALL", null, ["callee:00c58f30:8"]]
- 006554f4 bytes 9b0a1894
+ 006558a4 bytes a30d1894
- 006554fc ["COPY", "register:4040:8", ["const:c73000:8"]]
+ 006558ac ["COPY", "register:4040:8", ["const:c74000:8"]]
- 006554fc bytes e83000d0
+ 006558ac bytes e83000f0
- 00655500 ["COPY", "tmp:0:8", ["const:c88:8"]]
- 00655500 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00655500 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00655500 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006558b0 ["COPY", "tmp:0:8", ["const:c58:8"]]
+ 006558b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006558b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006558b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00655500 bytes 08213291
+ 006558b0 bytes 08613191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35df2875d4b8d6d78b014601ae5181f0"></a>

### [`00655514`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/00655514.md) → [`006558c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00655/006558c4.md) FUN_006558c4

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006558d0",
      "incomplete_value": false,
      "site": "006558d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:c58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00655520",
      "incomplete_value": false,
      "site": "00655520",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:c88:8"
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
      "006558d0",
      "DATA",
      [
        "storage",
        "00c73c88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006558d0",
      "DATA",
      [
        "storage",
        "00c74c58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00655518`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/00655514.md#insn-00655518) · [`0065551c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/00655514.md#insn-0065551c)
- 新版 [`006558c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00655/006558c4.md#insn-006558c8) · [`006558cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00655/006558c4.md#insn-006558cc)

~~~diff
- 00655518 ["COPY", "register:4048:8", ["const:c73000:8"]]
+ 006558c8 ["COPY", "register:4048:8", ["const:c74000:8"]]
- 00655518 bytes e93000d0
+ 006558c8 bytes e93000f0
- 0065551c ["COPY", "tmp:0:8", ["const:c88:8"]]
- 0065551c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0065551c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0065551c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006558cc ["COPY", "tmp:0:8", ["const:c58:8"]]
+ 006558cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006558cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006558cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0065551c bytes 29213291
+ 006558cc bytes 29613191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a4c11a11bf381e656ee6c5b426d95b7"></a>

### [`00655884`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/00655884.md) → [`00655c34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00655/00655c34.md) FUN_00655c34

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 55.56% / 新版 55.56%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0065589c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00655c4c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "0065588c",
      "incomplete_value": false,
      "site": "00655890",
      "value": [
        "leaf",
        "const:10:8"
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
      "unmatched:0065589c",
      "DATA",
      [
        "storage",
        "00c73d18",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:006558a0",
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
      "00655c4c",
      "DATA",
      [
        "storage",
        "00c74ce8",
        null,
        "undefined *"
      ]
    ],
    [
      "00655c50",
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

- 旧版 [`00655890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/00655884.md#insn-00655890) · [`0065589c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/00655884.md#insn-0065589c) · [`006558a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/00655884.md#insn-006558a4)
- 新版 [`00655c40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00655/00655c34.md#insn-00655c40)

~~~diff
- 00655890 ["INT_ADD", "register:40f0:8", ["const:655890:8", "const:4:8"]]
- 00655890 ["CALL", null, ["callee:00c58f30:8"]]
+ 00655c40 ["INT_ADD", "register:40f0:8", ["const:655c40:8", "const:4:8"]]
+ 00655c40 ["CALL", null, ["callee:00c58f30:8"]]
- 00655890 bytes b4091894
+ 00655c40 bytes bc0c1894
- 0065589c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 0065589c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0065589c bytes 080000f9
- 006558a4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 006558a4 ["RETURN", null, ["register:0:8"]]
- 006558a4 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6445752ccfc95ac0ec34a52370327c8"></a>

### [`006558c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/006558c0.md) → [`00655c70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00655/00655c70.md) FUN_00655c70

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 8件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00641f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00641/00641f80.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b6efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6efc.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`00642330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00642/00642330.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`008b7ea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7ea8.md)

変更の種類 branch_condition_or_target, call, call_target, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 95.08% / 新版 95.08%

CFGの説明率　旧版 50.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0065595c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00655d0c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00655d1c",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0065596c",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "unmatched:0065595c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00655d40"
      ]
    ],
    [
      "00655d1c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "00655d28",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "00655d0c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00655d40"
      ]
    ],
    [
      "00655d1c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "00655d28",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0065595c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/006558c0.md#insn-0065595c) · [`0065596c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/006558c0.md#insn-0065596c) · [`00655978`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/006558c0.md#insn-00655978)
- 新版 [`00655d1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00655/00655c70.md#insn-00655d1c) · [`00655d28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00655/00655c70.md#insn-00655d28)

~~~diff
- 0065595c ["CBRANCH", null, ["local:b10:8", "register:101:1"]]
- 0065595c bytes a0010054
- 0065596c ["INT_ADD", "register:40f0:8", ["const:65596c:8", "const:4:8"]]
- 0065596c ["CALL", null, ["ram:47ad34:8"]]
+ 00655d1c ["INT_ADD", "register:40f0:8", ["const:655d1c:8", "const:4:8"]]
+ 00655d1c ["CALL", null, ["ram:47b054:8"]]
- 0065596c bytes f294f897
+ 00655d1c bytes ce94f897
- 00655978 ["INT_ADD", "register:40f0:8", ["const:655978:8", "const:4:8"]]
- 00655978 ["CALL", null, ["ram:47ad34:8"]]
+ 00655d28 ["INT_ADD", "register:40f0:8", ["const:655d28:8", "const:4:8"]]
+ 00655d28 ["CALL", null, ["ram:47b054:8"]]
- 00655978 bytes ef94f897
+ 00655d28 bytes cb94f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84d75fabba87f33e6fb2a26bc8b9e90f"></a>

### [`00655a30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/00655a30.md) → [`00655de0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00655/00655de0.md) FUN_00655de0

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 14件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`005e3154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e3/005e3154.md) [`00655e30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/00655e30.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md) [`005e3504`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005e3/005e3504.md) [`006561e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00656/006561e0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 62.50% / 新版 61.40%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 2件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 5件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00655c78"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00655c80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00655ca0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00655e1c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "00655e38",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "00655e80",
      "DATA",
      [
        "storage",
        "004347c0",
        null,
        "byte[43]"
      ]
    ]
  ],
  "added": [
    [
      "00655e1c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "00655e38",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "00655e80",
      "DATA",
      [
        "storage",
        "004347c0",
        null,
        "byte[35]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00655a6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/00655a30.md#insn-00655a6c) · [`00655a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/00655a30.md#insn-00655a88) · [`00655bec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/00655a30.md#insn-00655bec)
- 新版 [`00655e1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00655/00655de0.md#insn-00655e1c) · [`00655e38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00655/00655de0.md#insn-00655e38) · [`00655f9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00655/00655de0.md#insn-00655f9c)

~~~diff
- 00655a6c ["INT_ADD", "register:40f0:8", ["const:655a6c:8", "const:4:8"]]
- 00655a6c ["CALL", null, ["ram:47ad34:8"]]
+ 00655e1c ["INT_ADD", "register:40f0:8", ["const:655e1c:8", "const:4:8"]]
+ 00655e1c ["CALL", null, ["ram:47b054:8"]]
- 00655a6c bytes b294f897
+ 00655e1c bytes 8e94f897
- 00655a88 ["INT_ADD", "register:40f0:8", ["const:655a88:8", "const:4:8"]]
- 00655a88 ["CALL", null, ["ram:47ad34:8"]]
+ 00655e38 ["INT_ADD", "register:40f0:8", ["const:655e38:8", "const:4:8"]]
+ 00655e38 ["CALL", null, ["ram:47b054:8"]]
- 00655a88 bytes ab94f897
+ 00655e38 bytes 8794f897
- 00655bec ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00655bec ["CBRANCH", null, ["local:b21:8", "tmp:0:1"]]
+ 00655f9c ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00655f9c ["CBRANCH", null, ["local:b25:8", "tmp:0:1"]]
- 00655bec bytes 200100b4
+ 00655f9c bytes 200100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d14418a696a592b1aced20eb8bfe999"></a>

### [`00655dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/00655dfc.md) → [`006561ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00656/006561ac.md) FUN_006561ac

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 55.56% / 新版 55.56%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00655e14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "006561c4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006561b4",
      "incomplete_value": false,
      "site": "006561b8",
      "value": [
        "leaf",
        "const:10:8"
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
      "unmatched:00655e14",
      "DATA",
      [
        "storage",
        "00c73e08",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00655e18",
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
      "006561c4",
      "DATA",
      [
        "storage",
        "00c74dd8",
        null,
        "undefined *"
      ]
    ],
    [
      "006561c8",
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

- 旧版 [`00655e08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/00655dfc.md#insn-00655e08) · [`00655e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/00655dfc.md#insn-00655e14) · [`00655e1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/00655dfc.md#insn-00655e1c)
- 新版 [`006561b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00656/006561ac.md#insn-006561b8)

~~~diff
- 00655e08 ["INT_ADD", "register:40f0:8", ["const:655e08:8", "const:4:8"]]
- 00655e08 ["CALL", null, ["callee:00c58f30:8"]]
+ 006561b8 ["INT_ADD", "register:40f0:8", ["const:6561b8:8", "const:4:8"]]
+ 006561b8 ["CALL", null, ["callee:00c58f30:8"]]
- 00655e08 bytes 56081894
+ 006561b8 bytes 5e0b1894
- 00655e14 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00655e14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00655e14 bytes 080000f9
- 00655e1c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00655e1c ["RETURN", null, ["register:0:8"]]
- 00655e1c bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c7a917c004aad011bb31b02df1610bb"></a>

### [`00655e20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/00655e20.md) → [`006561d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00656/006561d0.md) FUN_006561d0

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006561d4",
      "incomplete_value": false,
      "site": "006561d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:dd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00655e24",
      "incomplete_value": false,
      "site": "00655e28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:e08:8"
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
      "006561d8",
      "DATA",
      [
        "storage",
        "00c73e08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006561d8",
      "DATA",
      [
        "storage",
        "00c74dd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00655e20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/00655e20.md#insn-00655e20) · [`00655e24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/00655e20.md#insn-00655e24)
- 新版 [`006561d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00656/006561d0.md#insn-006561d0) · [`006561d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00656/006561d0.md#insn-006561d4)

~~~diff
- 00655e20 ["COPY", "register:4040:8", ["const:c73000:8"]]
+ 006561d0 ["COPY", "register:4040:8", ["const:c74000:8"]]
- 00655e20 bytes e83000d0
+ 006561d0 bytes e83000d0
- 00655e24 ["COPY", "tmp:0:8", ["const:e08:8"]]
- 00655e24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00655e24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00655e24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006561d4 ["COPY", "tmp:0:8", ["const:dd8:8"]]
+ 006561d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006561d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006561d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00655e24 bytes 08213891
+ 006561d4 bytes 08613791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11dc070599f7280c3f59e76763f3ba6b"></a>

### [`00655ea4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/00655ea4.md) → [`00656254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00656/00656254.md) FUN_00656254

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "00656278",
      "incomplete_value": false,
      "site": "00656278",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:e68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00655ec8",
      "incomplete_value": false,
      "site": "00655ec8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:e98:8"
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
      "00656278",
      "DATA",
      [
        "storage",
        "00c73e98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00656278",
      "DATA",
      [
        "storage",
        "00c74e68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00655eb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/00655ea4.md#insn-00655eb8) · [`00655ec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/00655ea4.md#insn-00655ec0) · [`00655ec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/00655ea4.md#insn-00655ec4)
- 新版 [`00656268`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00656/00656254.md#insn-00656268) · [`00656270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00656/00656254.md#insn-00656270) · [`00656274`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00656/00656254.md#insn-00656274)

~~~diff
- 00655eb8 ["INT_ADD", "register:40f0:8", ["const:655eb8:8", "const:4:8"]]
- 00655eb8 ["CALL", null, ["callee:00c58f30:8"]]
+ 00656268 ["INT_ADD", "register:40f0:8", ["const:656268:8", "const:4:8"]]
+ 00656268 ["CALL", null, ["callee:00c58f30:8"]]
- 00655eb8 bytes 2a081894
+ 00656268 bytes 320b1894
- 00655ec0 ["COPY", "register:4040:8", ["const:c73000:8"]]
+ 00656270 ["COPY", "register:4040:8", ["const:c74000:8"]]
- 00655ec0 bytes e83000d0
+ 00656270 bytes e83000d0
- 00655ec4 ["COPY", "tmp:0:8", ["const:e98:8"]]
- 00655ec4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00655ec4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00655ec4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00656274 ["COPY", "tmp:0:8", ["const:e68:8"]]
+ 00656274 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00656274 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00656274 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00655ec4 bytes 08613a91
+ 00656274 bytes 08a13991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5358edf21294f27830b7c22c2f3418db"></a>

### [`0065658c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00656/0065658c.md) → [`0065693c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00656/0065693c.md) FUN_0065693c

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "00656960",
      "incomplete_value": false,
      "site": "00656960",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:ee8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006565b0",
      "incomplete_value": false,
      "site": "006565b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:f18:8"
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
      "00656960",
      "DATA",
      [
        "storage",
        "00c73f18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00656960",
      "DATA",
      [
        "storage",
        "00c74ee8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006565a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00656/0065658c.md#insn-006565a0) · [`006565a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00656/0065658c.md#insn-006565a8) · [`006565ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00656/0065658c.md#insn-006565ac)
- 新版 [`00656950`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00656/0065693c.md#insn-00656950) · [`00656958`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00656/0065693c.md#insn-00656958) · [`0065695c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00656/0065693c.md#insn-0065695c)

~~~diff
- 006565a0 ["INT_ADD", "register:40f0:8", ["const:6565a0:8", "const:4:8"]]
- 006565a0 ["CALL", null, ["callee:00c58f30:8"]]
+ 00656950 ["INT_ADD", "register:40f0:8", ["const:656950:8", "const:4:8"]]
+ 00656950 ["CALL", null, ["callee:00c58f30:8"]]
- 006565a0 bytes 70061894
+ 00656950 bytes 78091894
- 006565a8 ["COPY", "register:4040:8", ["const:c73000:8"]]
+ 00656958 ["COPY", "register:4040:8", ["const:c74000:8"]]
- 006565a8 bytes e83000b0
+ 00656958 bytes e83000d0
- 006565ac ["COPY", "tmp:0:8", ["const:f18:8"]]
- 006565ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006565ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006565ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0065695c ["COPY", "tmp:0:8", ["const:ee8:8"]]
+ 0065695c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0065695c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0065695c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006565ac bytes 08613c91
+ 0065695c bytes 08a13b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f87d5fc896cbb4c8863fce1305d82a3c"></a>

### [`00656ca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00656/00656ca0.md) → [`00657050`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00657/00657050.md) FUN_00657050

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "00657074",
      "incomplete_value": false,
      "site": "00657074",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:f68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00656cc4",
      "incomplete_value": false,
      "site": "00656cc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:f98:8"
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
      "00657074",
      "DATA",
      [
        "storage",
        "00c73f98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00657074",
      "DATA",
      [
        "storage",
        "00c74f68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00656cb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00656/00656ca0.md#insn-00656cb4) · [`00656cbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00656/00656ca0.md#insn-00656cbc) · [`00656cc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00656/00656ca0.md#insn-00656cc0)
- 新版 [`00657064`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00657/00657050.md#insn-00657064) · [`0065706c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00657/00657050.md#insn-0065706c) · [`00657070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00657/00657050.md#insn-00657070)

~~~diff
- 00656cb4 ["INT_ADD", "register:40f0:8", ["const:656cb4:8", "const:4:8"]]
- 00656cb4 ["CALL", null, ["callee:00c58f30:8"]]
+ 00657064 ["INT_ADD", "register:40f0:8", ["const:657064:8", "const:4:8"]]
+ 00657064 ["CALL", null, ["callee:00c58f30:8"]]
- 00656cb4 bytes ab041894
+ 00657064 bytes b3071894
- 00656cbc ["COPY", "register:4040:8", ["const:c73000:8"]]
+ 0065706c ["COPY", "register:4040:8", ["const:c74000:8"]]
- 00656cbc bytes e83000b0
+ 0065706c bytes e83000b0
- 00656cc0 ["COPY", "tmp:0:8", ["const:f98:8"]]
- 00656cc0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00656cc0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00656cc0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00657070 ["COPY", "tmp:0:8", ["const:f68:8"]]
+ 00657070 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00657070 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00657070 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00656cc0 bytes 08613e91
+ 00657070 bytes 08a13d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-588590533f19c387adf72a1d35eeac68"></a>

### [`00656cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00656/00656cf0.md) → [`006570a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00657/006570a0.md) FUN_006570a0

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b7a68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b7a68.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`008b8a14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b8/008b8a14.md)

変更の種類 branch_condition_or_target, call, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 90.62% / 新版 90.62%

CFGの説明率　旧版 87.50% / 新版 70.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00656d40"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "006570f0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006570c0",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00656d10",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "006570c0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "006570cc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "unmatched:00656d40",
      "DATA",
      [
        "storage",
        "0039b1b4",
        null,
        "dword"
      ]
    ]
  ],
  "added": [
    [
      "006570c0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "006570cc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "006570f0",
      "DATA",
      [
        "storage",
        "0039b1b4",
        null,
        "qword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00656d10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00656/00656cf0.md#insn-00656d10) · [`00656d1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00656/00656cf0.md#insn-00656d1c) · [`00656d40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00656/00656cf0.md#insn-00656d40)
- 新版 [`006570c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00657/006570a0.md#insn-006570c0) · [`006570cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00657/006570a0.md#insn-006570cc)

~~~diff
- 00656d10 ["INT_ADD", "register:40f0:8", ["const:656d10:8", "const:4:8"]]
- 00656d10 ["CALL", null, ["ram:47ad34:8"]]
+ 006570c0 ["INT_ADD", "register:40f0:8", ["const:6570c0:8", "const:4:8"]]
+ 006570c0 ["CALL", null, ["ram:47b054:8"]]
- 00656d10 bytes 0990f897
+ 006570c0 bytes e58ff897
- 00656d1c ["INT_ADD", "register:40f0:8", ["const:656d1c:8", "const:4:8"]]
- 00656d1c ["CALL", null, ["ram:47ad34:8"]]
+ 006570cc ["INT_ADD", "register:40f0:8", ["const:6570cc:8", "const:4:8"]]
+ 006570cc ["CALL", null, ["ram:47b054:8"]]
- 00656d1c bytes 0690f897
+ 006570cc bytes e28ff897
- 00656d40 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00656d40 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00656d40 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00656d40 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
- 00656d40 bytes 096828b8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bccbd23920901aee3bbcac84e5a181ea"></a>

### [`00656d98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00656/00656d98.md) → [`00657148`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00657/00657148.md) FUN_00657148

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0064bd94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064b/0064bd94.md) · 呼出先 4件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00656ed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00656/00656ed0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`0064c144`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064c/0064c144.md) · 呼出先 4件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00657280`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00657/00657280.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 98.36% / 新版 98.36%

CFGの説明率　旧版 52.63% / 新版 55.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00656df0",
      "incomplete_value": true,
      "site": "00656df4",
      "value": [
        "live",
        "register:8:8"
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00656dec",
      "incomplete_value": true,
      "site": "00656df4",
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
              [
                "leaf",
                "const:8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00656dec",
      "incomplete_value": true,
      "site": "00656df4",
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
                "live",
                "register:40b0:8"
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
    "ordinal": 0,
    "slot": 3
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00656df4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00656/00656d98.md#insn-00656df4) · [`00656e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00656/00656d98.md#insn-00656e84)
- 新版 [`006571a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00657/00657148.md#insn-006571a4) · [`00657234`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00657/00657148.md#insn-00657234)

~~~diff
- 00656df4 ["INT_ADD", "register:40f0:8", ["const:656df4:8", "const:4:8"]]
- 00656df4 ["CALL", null, ["callee:0043be80:8"]]
+ 006571a4 ["INT_ADD", "register:40f0:8", ["const:6571a4:8", "const:4:8"]]
+ 006571a4 ["CALL", null, ["callee:0043be80:8"]]
- 00656df4 bytes 5b93f797
+ 006571a4 bytes 3793f797
- 00656e84 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00656e84 ["RETURN", null, ["register:0:8"]]
- 00656e84 bytes c0035fd6
+ 00657234 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00657234 ["RETURN", null, ["register:0:8"]]
+ 00657234 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92fe6e094da92761cf78418bb75bcf31"></a>

### [`00656ed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00656/00656ed0.md) → [`00657280`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00657/00657280.md) FUN_00657280

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00656d98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00656/00656d98.md) [`00656ed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00656/00656ed0.md) · 呼出先 21件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) [`00441d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441d2c.md)
- 新版 呼出元 2件 [`00657148`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00657/00657148.md) [`00657280`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00657/00657280.md) · 呼出先 21件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`004412d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004412d0.md) [`0044204c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/0044204c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 92.19% / 新版 92.19%

CFGの説明率　旧版 57.59% / 新版 57.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 14件, `store_condition` 2件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00656f08"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00656f14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00657384"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00656f08",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "unmatched:00656f14",
      "WRITE",
      [
        "storage",
        "Stack[-0x180]",
        null,
        null
      ]
    ],
    [
      "unmatched:00656f94",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00657b5c"
      ]
    ]
  ],
  "added": [
    [
      "006572b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "006572c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x180]",
        null,
        null
      ]
    ],
    [
      "00657344",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00657b5c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00656f08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00656/00656ed0.md#insn-00656f08) · [`00656f14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00656/00656ed0.md#insn-00656f14) · [`00656f54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00656/00656ed0.md#insn-00656f54)
- 新版 [`00657304`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00657/00657280.md#insn-00657304)

~~~diff
- 00656f08 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00656f08 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffe8:8"]]
- 00656f08 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00656f08 bytes a9831ef8
- 00656f14 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:30:8"]]
- 00656f14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00656f14 bytes e81b00f9
- 00656f54 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00656f54 ["CBRANCH", null, ["local:b22:8", "tmp:0:1"]]
+ 00657304 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00657304 ["CBRANCH", null, ["local:b23:8", "tmp:0:1"]]
- 00656f54 bytes 000900b4
+ 00657304 bytes 000900b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28fe3854e6785ec6843e13c7ab269173"></a>

### [`00657928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00657/00657928.md) → [`00657cd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00657/00657cd8.md) FUN_00657cd8

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00657cf8",
      "incomplete_value": false,
      "site": "00657cfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:fe8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00657948",
      "incomplete_value": false,
      "site": "0065794c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:18:8"
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
      "00657cfc",
      "DATA",
      [
        "storage",
        "00c74018",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00657cfc",
      "DATA",
      [
        "storage",
        "00c74fe8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0065793c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00657/00657928.md#insn-0065793c) · [`00657948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00657/00657928.md#insn-00657948)
- 新版 [`00657cec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00657/00657cd8.md#insn-00657cec) · [`00657cf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00657/00657cd8.md#insn-00657cf8)

~~~diff
- 0065793c ["INT_ADD", "register:40f0:8", ["const:65793c:8", "const:4:8"]]
- 0065793c ["CALL", null, ["callee:00c58f30:8"]]
+ 00657cec ["INT_ADD", "register:40f0:8", ["const:657cec:8", "const:4:8"]]
+ 00657cec ["CALL", null, ["callee:00c58f30:8"]]
- 0065793c bytes 89011894
+ 00657cec bytes 91041894
- 00657948 ["COPY", "tmp:0:8", ["const:18:8"]]
- 00657948 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00657948 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00657948 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00657cf8 ["COPY", "tmp:0:8", ["const:fe8:8"]]
+ 00657cf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00657cf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00657cf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00657948 bytes 08610091
+ 00657cf8 bytes 08a13f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23315871215d0dbd17a9f761ac1f0153"></a>

### [`00657960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00657/00657960.md) → [`00657d10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00657/00657d10.md) FUN_00657d10

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00657d14",
      "incomplete_value": false,
      "site": "00657d18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:fe8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00657964",
      "incomplete_value": false,
      "site": "00657968",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:18:8"
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
      "00657d18",
      "DATA",
      [
        "storage",
        "00c74018",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00657d18",
      "DATA",
      [
        "storage",
        "00c74fe8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00657964`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00657/00657960.md#insn-00657964)
- 新版 [`00657d14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00657/00657d10.md#insn-00657d14)

~~~diff
- 00657964 ["COPY", "tmp:0:8", ["const:18:8"]]
- 00657964 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00657964 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00657964 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00657d14 ["COPY", "tmp:0:8", ["const:fe8:8"]]
+ 00657d14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00657d14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00657d14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00657964 bytes 08610091
+ 00657d14 bytes 08a13f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d34dc90143c4da24f4bd49394fb710a"></a>

### [`00657c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00657/00657c28.md) → [`00657fd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00657/00657fd8.md) FUN_00657fd8

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00657ff8",
      "incomplete_value": false,
      "site": "00657ffc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00657c48",
      "incomplete_value": false,
      "site": "00657c4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:118:8"
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
      "00657ffc",
      "DATA",
      [
        "storage",
        "00c74118",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00657ffc",
      "DATA",
      [
        "storage",
        "00c750e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00657c3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00657/00657c28.md#insn-00657c3c) · [`00657c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00657/00657c28.md#insn-00657c44) · [`00657c48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00657/00657c28.md#insn-00657c48)
- 新版 [`00657fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00657/00657fd8.md#insn-00657fec) · [`00657ff4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00657/00657fd8.md#insn-00657ff4) · [`00657ff8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00657/00657fd8.md#insn-00657ff8)

~~~diff
- 00657c3c ["INT_ADD", "register:40f0:8", ["const:657c3c:8", "const:4:8"]]
- 00657c3c ["CALL", null, ["callee:00c58f30:8"]]
+ 00657fec ["INT_ADD", "register:40f0:8", ["const:657fec:8", "const:4:8"]]
+ 00657fec ["CALL", null, ["callee:00c58f30:8"]]
- 00657c3c bytes c9001894
+ 00657fec bytes d1031894
- 00657c44 ["COPY", "register:4040:8", ["const:c74000:8"]]
+ 00657ff4 ["COPY", "register:4040:8", ["const:c75000:8"]]
- 00657c44 bytes e83000b0
+ 00657ff4 bytes e83000d0
- 00657c48 ["COPY", "tmp:0:8", ["const:118:8"]]
- 00657c48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00657c48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00657c48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00657ff8 ["COPY", "tmp:0:8", ["const:e8:8"]]
+ 00657ff8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00657ff8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00657ff8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00657c48 bytes 08610491
+ 00657ff8 bytes 08a10391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e527b3a31b7fe7bd04d43a77397b8b53"></a>

### [`00657c80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00657/00657c80.md) → [`00658030`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00658/00658030.md) FUN_00658030

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 92.00% / 新版 92.00%

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
      "site": "00658050",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00657ca0",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0065805c",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00657cac",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "00658050",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "0065805c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "00658050",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "0065805c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00657ca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00657/00657c80.md#insn-00657ca0) · [`00657cac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00657/00657c80.md#insn-00657cac)
- 新版 [`00658050`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00658/00658030.md#insn-00658050) · [`0065805c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00658/00658030.md#insn-0065805c)

~~~diff
- 00657ca0 ["INT_ADD", "register:40f0:8", ["const:657ca0:8", "const:4:8"]]
- 00657ca0 ["CALL", null, ["ram:47ad34:8"]]
+ 00658050 ["INT_ADD", "register:40f0:8", ["const:658050:8", "const:4:8"]]
+ 00658050 ["CALL", null, ["ram:47b054:8"]]
- 00657ca0 bytes 258cf897
+ 00658050 bytes 018cf897
- 00657cac ["INT_ADD", "register:40f0:8", ["const:657cac:8", "const:4:8"]]
- 00657cac ["CALL", null, ["ram:47ad34:8"]]
+ 0065805c ["INT_ADD", "register:40f0:8", ["const:65805c:8", "const:4:8"]]
+ 0065805c ["CALL", null, ["ram:47b054:8"]]
- 00657cac bytes 228cf897
+ 0065805c bytes fe8bf897
~~~


<a id="compare-74c54428d43e60f77d2b9802fad7d37a"></a>

### [`00657f04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00657/00657f04.md) → [`006582b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00658/006582b4.md) FUN_006582b4

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 call_argument_candidate, constant, local_def_use, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 55.56% / 新版 55.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006582c8",
      "incomplete_value": false,
      "site": "006582cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:268:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00657f18",
      "incomplete_value": false,
      "site": "00657f1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:298:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00657f0c",
      "incomplete_value": false,
      "site": "00657f10",
      "value": [
        "leaf",
        "const:10:8"
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
      "006582cc",
      "DATA",
      [
        "storage",
        "00c74298",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006582cc",
      "DATA",
      [
        "storage",
        "00c75268",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00657f10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00657/00657f04.md#insn-00657f10) · [`00657f08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00657/00657f04.md#insn-00657f08) · [`00657f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00657/00657f04.md#insn-00657f0c)
- 新版 [`006582c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00658/006582b4.md#insn-006582c0)

~~~diff
- 00657f10 ["INT_ADD", "register:40f0:8", ["const:657f10:8", "const:4:8"]]
- 00657f10 ["CALL", null, ["callee:00c58f30:8"]]
+ 006582c0 ["INT_ADD", "register:40f0:8", ["const:6582c0:8", "const:4:8"]]
+ 006582c0 ["CALL", null, ["callee:00c58f30:8"]]
- 00657f10 bytes 14001894
+ 006582c0 bytes 1c031894
- 00657f08 ["COPY", "register:40e8:8", ["register:8:8"]]
- 00657f08 bytes fd030091
- 00657f0c ["COPY", "register:4000:8", ["const:10:8"]]
- 00657f0c bytes 00028052
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dddc6026d3220c49ad99b927ff7d1783"></a>

### [`00657fcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00657/00657fcc.md) → [`0065837c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00658/0065837c.md) FUN_0065837c

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0064ecf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064e/0064ecf8.md) [`00ad6fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ad6/00ad6fbc.md) · 呼出先 21件 [`0044db90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044db90.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`0046da88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046da88.md) [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`0048ef30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048ef30.md)
- 新版 呼出元 2件 [`0064f0a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0064f/0064f0a8.md) [`00ad7fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ad7/00ad7fb0.md) · 呼出先 21件 [`0044deb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044d/0044deb0.md) [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md) [`0046dda8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046dda8.md) [`0048d058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d058.md) [`0048f250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048f/0048f250.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 83.00% / 新版 83.00%

CFGの説明率　旧版 22.86% / 新版 22.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 1件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00658084"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00658088"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0065808c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006583bc",
      "DATA",
      [
        "storage",
        "0039b1b4",
        null,
        "dword"
      ]
    ],
    [
      "006583d4",
      "DATA",
      [
        "storage",
        "0039b1bc",
        null,
        "qword"
      ]
    ],
    [
      "006583ec",
      "DATA",
      [
        "storage",
        "0039b1bc",
        null,
        "qword"
      ]
    ]
  ],
  "added": [
    [
      "006583bc",
      "DATA",
      [
        "storage",
        "0039b1b4",
        null,
        "qword"
      ]
    ],
    [
      "006583d4",
      "DATA",
      [
        "storage",
        "0039b1bc",
        null,
        "dword"
      ]
    ],
    [
      "006583ec",
      "DATA",
      [
        "storage",
        "0039b1bc",
        null,
        "dword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00658060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00657/00657fcc.md#insn-00658060) · [`00658084`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00657/00657fcc.md#insn-00658084) · [`00658088`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00657/00657fcc.md#insn-00658088)

~~~diff
- 00658060 ["INT_ADD", "register:40f0:8", ["const:658060:8", "const:4:8"]]
- 00658060 ["CALL", null, ["ram:48cd38:8"]]
- 00658060 bytes 36d3f897
- 00658084 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00658084 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:8:8"]]
- 00658084 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00658084 bytes e8230039
- 00658088 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 00658088 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:11:8"]]
- 00658088 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 00658088 bytes ea130178
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-218b5bf80f115cc3ccfa85229ecf068d"></a>

### [`006583e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00658/006583e4.md) → [`00658794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00658/00658794.md) FUN_00658794

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`0065e23c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0065e/0065e23c.md) [`0065ef44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0065e/0065ef44.md) · 呼出先 5件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b6f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6f70.md) [`008b79a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b79a0.md) [`008b7a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b7a20.md) [`00a832d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a83/00a832d0.md)
- 新版 呼出元 2件 [`0065e5ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0065e/0065e5ec.md) [`0065f2f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0065f/0065f2f4.md) · 呼出先 5件 [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`008b7f1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7f1c.md) [`008b894c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b8/008b894c.md) [`008b89cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b8/008b89cc.md) [`00a842c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a84/00a842c4.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 40.00% / 新版 28.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "0065848c",
      "incomplete_value": true,
      "site": "00658494",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4000:8"
          ],
          [
            "live",
            "register:40a8:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00658490",
      "incomplete_value": true,
      "site": "00658494",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:40a0:4"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00658494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00658/006583e4.md#insn-00658494) · [`006583f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00658/006583e4.md#insn-006583f8) · [`00658408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00658/006583e4.md#insn-00658408)
- 新版 [`00658844`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00658/00658794.md#insn-00658844) · [`006587a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00658/00658794.md#insn-006587a8) · [`006587b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00658/00658794.md#insn-006587b8)

~~~diff
- 00658494 ["INT_ADD", "register:40f0:8", ["const:658494:8", "const:4:8"]]
- 00658494 ["CALL", null, ["callee:008b894c:8"]]
+ 00658844 ["INT_ADD", "register:40f0:8", ["const:658844:8", "const:4:8"]]
+ 00658844 ["CALL", null, ["callee:008b894c:8"]]
- 00658494 bytes 437d0994
+ 00658844 bytes 42800994
- 006583f8 ["INT_ADD", "register:40f0:8", ["const:6583f8:8", "const:4:8"]]
- 006583f8 ["CALL", null, ["callee:008524fc:8"]]
+ 006587a8 ["INT_ADD", "register:40f0:8", ["const:6587a8:8", "const:4:8"]]
+ 006587a8 ["CALL", null, ["callee:008524fc:8"]]
- 006583f8 bytes 56e40794
+ 006587a8 bytes 55e70794
- 00658408 ["INT_ADD", "register:40f0:8", ["const:658408:8", "const:4:8"]]
- 00658408 ["CALL", null, ["callee:00a842c4:8"]]
+ 006587b8 ["INT_ADD", "register:40f0:8", ["const:6587b8:8", "const:4:8"]]
+ 006587b8 ["CALL", null, ["callee:00a842c4:8"]]
- 00658408 bytes b2ab1094
+ 006587b8 bytes c3ae1094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-025b7ef6bbe583908a38d1a206bb65b5"></a>

### [`00658c2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00658/00658c2c.md) → [`00658fdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00658/00658fdc.md) FUN_00658fdc

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`006584c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00658/006584c8.md) [`00659edc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00659/00659edc.md) [`0065be6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0065b/0065be6c.md) · 呼出先 9件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`00641ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00641/00641ba0.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`009dfb6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009df/009dfb6c.md)
- 新版 呼出元 3件 [`00658878`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00658/00658878.md) [`0065a28c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0065a/0065a28c.md) [`0065c21c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0065c/0065c21c.md) · 呼出先 9件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`005c1b8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c1/005c1b8c.md) [`00641f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00641/00641f50.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`009e0b18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e0/009e0b18.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 93.14% / 新版 93.14%

CFGの説明率　旧版 37.50% / 新版 32.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00658d78"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00659128"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00658c8c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00658c8c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00659198"
      ]
    ],
    [
      "unmatched:00658cac",
      "DATA",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00658cb4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00641ba0"
      ]
    ]
  ],
  "added": [
    [
      "0065903c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00659198"
      ]
    ],
    [
      "0065905c",
      "DATA",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00659064",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00641f50"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00658c8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00658/00658c2c.md#insn-00658c8c) · [`00658d5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00658/00658c2c.md#insn-00658d5c) · [`00658d78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00658/00658c2c.md#insn-00658d78)

~~~diff
- 00658c8c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00658c8c ["CBRANCH", null, ["local:b23:8", "tmp:0:1"]]
- 00658c8c bytes e10a0054
- 00658d5c ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00658d5c ["CBRANCH", null, ["local:b17:8", "tmp:0:1"]]
- 00658d5c bytes 680000b4
- 00658d78 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00658d78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00658d78 bytes e80b00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73f7cc4293e5532e72deaee7cdbb7e8c"></a>

### [`00658dec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00658/00658dec.md) → [`0065919c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00659/0065919c.md) FUN_0065919c

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00aeef94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aee/00aeef94.md) · 呼出先 38件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`0047e64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e64c.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md)
- 新版 呼出元 1件 [`00aeff88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aef/00aeff88.md) · 呼出先 38件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md) [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`0047e96c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047e/0047e96c.md) [`0047f114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047f/0047f114.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 17.68% / 新版 17.94%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 43件, `call_target` 1件, `store_condition` 5件, `store_destination` 3件, `store_value` 1件, `unresolved_branch_alignment` 32件, `unresolved_call_alignment` 22件, `unresolved_store_alignment` 43件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00658e04"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00658e04"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00658e3c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00658e04",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00658e3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x1c0]",
        null,
        null
      ]
    ],
    [
      "unmatched:00658eb0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00659280"
      ]
    ]
  ],
  "added": [
    [
      "006591b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "006591ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x1c0]",
        null,
        null
      ]
    ],
    [
      "00659260",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00659280"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00658e04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00658/00658dec.md#insn-00658e04) · [`00658e3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00658/00658dec.md#insn-00658e3c) · [`00658e40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00658/00658dec.md#insn-00658e40)

~~~diff
- 00658e04 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00658e04 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00658e04 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:1d0:8"]]
- 00658e04 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00658e04 bytes f44f1da9
- 00658e3c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00658e3c ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00658e3c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00658e3c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00658e3c bytes e02b02a9
- 00658e40 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:10:8"]]
- 00658e40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00658e40 bytes 080800f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7429bb6faa30fb6039409ab91d4d6664"></a>

### [`00659edc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00659/00659edc.md) → [`0065a28c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0065a/0065a28c.md) FUN_0065a28c

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00658dec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00658/00658dec.md) [`0065ec38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0065e/0065ec38.md) · 呼出先 32件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`0047e64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e64c.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`005d8c08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d8/005d8c08.md)
- 新版 呼出元 2件 [`0065919c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00659/0065919c.md) [`0065efe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0065e/0065efe8.md) · 呼出先 32件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md) [`0047e96c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047e/0047e96c.md) [`0047f114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047f/0047f114.md) [`005d8fb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d8/005d8fb8.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 72.58% / 新版 72.58%

CFGの説明率　旧版 43.32% / 新版 43.32%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 18件, `store_condition` 4件, `store_value` 2件, `unresolved_branch_alignment` 16件, `unresolved_call_alignment` 27件, `unresolved_store_alignment` 55件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00659ef0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00659ef0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00659ef4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00659ef0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00659ef4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00659f08",
      "WRITE",
      [
        "storage",
        "Stack[-0x148]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0065a2a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0065a2a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0065a2b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x148]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00659ef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00659/00659edc.md#insn-00659ef0) · [`00659ef4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00659/00659edc.md#insn-00659ef4) · [`00659f08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00659/00659edc.md#insn-00659f08)

~~~diff
- 00659ef0 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00659ef0 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00659ef0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:130:8"]]
- 00659ef0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00659ef0 bytes f65713a9
- 00659ef4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00659ef4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00659ef4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:140:8"]]
- 00659ef4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00659ef4 bytes f44f14a9
- 00659f08 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00659f08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00659f08 bytes e80700f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a24ab42334a50726e2f65a763fe8460"></a>

### [`0065ad80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0065a/0065ad80.md) → [`0065b130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0065b/0065b130.md) FUN_0065b130

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00657980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00657/00657980.md) · 呼出先 38件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`0047e64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e64c.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md)
- 新版 呼出元 1件 [`00657d30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00657/00657d30.md) · 呼出先 38件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md) [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`0047e96c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047e/0047e96c.md) [`0047f114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047f/0047f114.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 80.56% / 新版 80.56%

CFGの説明率　旧版 54.58% / 新版 54.18%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `call_target` 1件, `store_condition` 1件, `store_value` 2件, `unresolved_branch_alignment` 24件, `unresolved_call_alignment` 17件, `unresolved_store_alignment` 30件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0065b390"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0065b394"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0065b494"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0065ae60",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0065b1f8"
      ]
    ],
    [
      "unmatched:0065ae94",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0065bfd4"
      ]
    ],
    [
      "unmatched:0065aeb8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:0065aed4"
      ]
    ]
  ],
  "added": [
    [
      "0065b210",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0065b1f8"
      ]
    ],
    [
      "0065b244",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0065bfd4"
      ]
    ],
    [
      "0065b268",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0065b284"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0065b0e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0065a/0065ad80.md#insn-0065b0e4) · [`0065b284`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0065a/0065ad80.md#insn-0065b284) · [`0065b370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0065a/0065ad80.md#insn-0065b370)
- 新版 [`0065b494`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0065b/0065b130.md#insn-0065b494) · [`0065b634`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0065b/0065b130.md#insn-0065b634) · [`0065b720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0065b/0065b130.md#insn-0065b720)

~~~diff
- 0065b0e4 ["CBRANCH", null, ["local:b73:8", "register:101:1"]]
+ 0065b494 ["CBRANCH", null, ["local:b77:8", "register:101:1"]]
- 0065b0e4 bytes 200d0054
+ 0065b494 bytes 200d0054
- 0065b284 ["BRANCH", null, ["local:b48:8"]]
+ 0065b634 ["BRANCH", null, ["local:b50:8"]]
- 0065b284 bytes 95ffff17
+ 0065b634 bytes 95ffff17
- 0065b370 ["COPY", "register:0:8", ["register:4040:8"]]
- 0065b370 ["INT_ADD", "register:40f0:8", ["const:65b370:8", "const:4:8"]]
- 0065b370 ["CALLIND", null, ["register:0:8"]]
+ 0065b720 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0065b720 ["INT_ADD", "register:40f0:8", ["const:65b720:8", "const:4:8"]]
+ 0065b720 ["CALLIND", null, ["register:0:8"]]
- 0065b370 bytes 00013fd6
+ 0065b720 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c028dddac7dc1186bd1de450fecad3ae"></a>

### [`0065be6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0065b/0065be6c.md) → [`0065c21c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0065c/0065c21c.md) FUN_0065c21c

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0065ad80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0065a/0065ad80.md) [`0065f6b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0065f/0065f6b0.md) · 呼出先 32件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`0047e64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e64c.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`005d8c08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d8/005d8c08.md)
- 新版 呼出元 2件 [`0065b130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0065b/0065b130.md) [`0065fa60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0065f/0065fa60.md) · 呼出先 32件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md) [`0047e96c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047e/0047e96c.md) [`0047f114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047f/0047f114.md) [`005d8fb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d8/005d8fb8.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 72.78% / 新版 72.78%

CFGの説明率　旧版 45.25% / 新版 45.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `call_target` 1件, `store_destination` 3件, `store_value` 3件, `unresolved_branch_alignment` 17件, `unresolved_call_alignment` 28件, `unresolved_store_alignment` 44件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0065c284",
      "incomplete_value": false,
      "site": "0065c284",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca7000:8"
          ],
          [
            "leaf",
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0065bed4",
      "incomplete_value": false,
      "site": "0065bed4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca6000:8"
          ],
          [
            "leaf",
            "const:dd8:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0065c290",
      "incomplete_value": true,
      "site": "0065c290",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4058:8"
          ],
          [
            "leaf",
            "const:d90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0065bee0",
      "incomplete_value": true,
      "site": "0065bee0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4058:8"
          ],
          [
            "leaf",
            "const:dd0:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0065c298",
      "incomplete_value": false,
      "site": "0065c298",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca7000:8"
          ],
          [
            "leaf",
            "const:d94:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0065bee8",
      "incomplete_value": false,
      "site": "0065bee8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca6000:8"
          ],
          [
            "leaf",
            "const:dd4:8"
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0065c284",
      "WRITE",
      [
        "storage",
        "00ca6dd8",
        null,
        "undefined4"
      ]
    ],
    [
      "0065c290",
      "WRITE",
      [
        "storage",
        "00ca6dd0",
        null,
        "undefined1"
      ]
    ],
    [
      "0065c298",
      "WRITE",
      [
        "storage",
        "00ca6dd4",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0065c284",
      "WRITE",
      [
        "storage",
        "00ca7d98",
        null,
        "undefined4"
      ]
    ],
    [
      "0065c290",
      "WRITE",
      [
        "storage",
        "00ca7d90",
        null,
        "undefined1"
      ]
    ],
    [
      "0065c298",
      "WRITE",
      [
        "storage",
        "00ca7d94",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0065bed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0065b/0065be6c.md#insn-0065bed0) · [`0065bed4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0065b/0065be6c.md#insn-0065bed4) · [`0065bee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0065b/0065be6c.md#insn-0065bee0)
- 新版 [`0065c280`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0065c/0065c21c.md#insn-0065c280) · [`0065c284`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0065c/0065c21c.md#insn-0065c284) · [`0065c290`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0065c/0065c21c.md#insn-0065c290)

~~~diff
- 0065bed0 ["COPY", "register:40b0:8", ["const:ca6000:8"]]
+ 0065c280 ["COPY", "register:40b0:8", ["const:ca7000:8"]]
- 0065bed0 bytes 563200f0
+ 0065c280 bytes 563200f0
- 0065bed4 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:dd8:8"]]
- 0065bed4 ["COPY", "tmp:1:4", ["const:0:4"]]
- 0065bed4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:4"]]
+ 0065c284 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:d98:8"]]
+ 0065c284 ["COPY", "tmp:1:4", ["const:0:4"]]
+ 0065c284 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:4"]]
- 0065bed4 bytes 5fd90db9
+ 0065c284 bytes 5f990db9
- 0065bee0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 0065bee0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 0065bee0 ["INT_ADD", "tmp:2:8", ["register:4058:8", "const:dd0:8"]]
- 0065bee0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 0065c290 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 0065c290 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 0065c290 ["INT_ADD", "tmp:2:8", ["register:4058:8", "const:d90:8"]]
+ 0065c290 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 0065bee0 bytes 7f413739
+ 0065c290 bytes 7f413639
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e915a1a12ac1f1e046336db90f6d6c3"></a>

### [`0065cd0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0065c/0065cd0c.md) → [`0065d0bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0065d/0065d0bc.md) FUN_0065d0bc

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00ae1328`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ae1/00ae1328.md) · 呼出先 31件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00467ac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467ac8.md) [`00467ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467ba0.md) [`00467df4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467df4.md)
- 新版 呼出元 1件 [`00ae231c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ae2/00ae231c.md) · 呼出先 31件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00467bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467bc0.md) [`00467de8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467de8.md) [`00467ec0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467ec0.md) [`00468114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00468/00468114.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 87.99% / 新版 87.99%

CFGの説明率　旧版 39.13% / 新版 40.91%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 20件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 17件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0065cd24"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0065cd24"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0065cd28"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0065cd24",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0065cd28",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0065cd3c",
      "WRITE",
      [
        "storage",
        "Stack[-0xb0]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0065d0d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0065d0d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0065d0ec",
      "WRITE",
      [
        "storage",
        "Stack[-0xb0]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0065cd24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0065c/0065cd0c.md#insn-0065cd24) · [`0065cd28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0065c/0065cd0c.md#insn-0065cd28) · [`0065cd3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0065c/0065cd0c.md#insn-0065cd3c)

~~~diff
- 0065cd24 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 0065cd24 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 0065cd24 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:90:8"]]
- 0065cd24 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0065cd24 bytes f65709a9
- 0065cd28 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0065cd28 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0065cd28 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:a0:8"]]
- 0065cd28 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0065cd28 bytes f44f0aa9
- 0065cd3c ["COPY", "tmp:0:8", ["register:8:8"]]
- 0065cd3c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0065cd3c bytes e80300f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-107c15b6f95e0eb28b5a04d69506f505"></a>

### [`0065d670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0065d/0065d670.md) → [`0065da20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0065d/0065da20.md) FUN_0065da20

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00651ae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00651/00651ae4.md) · 呼出先 31件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00467ac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467ac8.md) [`00467ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467ba0.md) [`00467df4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467df4.md)
- 新版 呼出元 1件 [`00651e94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00651/00651e94.md) · 呼出先 31件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00467bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467bc0.md) [`00467de8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467de8.md) [`00467ec0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467ec0.md) [`00468114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00468/00468114.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 93.23% / 新版 93.23%

CFGの説明率　旧版 23.81% / 新版 23.81%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 21件, `store_condition` 1件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 6件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0065d6a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0065d6c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0065d948"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0065d6a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "unmatched:0065d6c8",
      "WRITE",
      [
        "storage",
        "Stack[-0xa8]",
        null,
        null
      ]
    ],
    [
      "0065da7c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:0065d74c"
      ]
    ]
  ],
  "added": [
    [
      "0065da58",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "0065da78",
      "WRITE",
      [
        "storage",
        "Stack[-0xa8]",
        null,
        null
      ]
    ],
    [
      "0065da7c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "0065dafc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0065d6a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0065d/0065d670.md#insn-0065d6a8) · [`0065d6c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0065d/0065d670.md#insn-0065d6c8) · [`0065d6e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0065d/0065d670.md#insn-0065d6e8)

~~~diff
- 0065d6a8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0065d6a8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffe8:8"]]
- 0065d6a8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0065d6a8 bytes a8831ef8
- 0065d6c8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 0065d6c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0065d6c8 bytes e80700f9
- 0065d6e8 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 0065d6e8 ["COPY", "tmp:1:4", ["register:4048:4"]]
- 0065d6e8 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 0065d6e8 ["COPY", "tmp:1:4", ["register:4040:4"]]
- 0065d6e8 bytes 28b1881a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f8f909a77be23769f91128f42ee52f2"></a>

### [`0065dfd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0065d/0065dfd4.md) → [`0065e384`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0065e/0065e384.md) FUN_0065e384

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0065e390",
      "incomplete_value": false,
      "site": "0065e39c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:2e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0065dfe0",
      "incomplete_value": false,
      "site": "0065dfec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:318:8"
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
      "0065e39c",
      "DATA",
      [
        "storage",
        "00c74318",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0065e39c",
      "DATA",
      [
        "storage",
        "00c752e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0065dfdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0065d/0065dfd4.md#insn-0065dfdc) · [`0065dfe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0065d/0065dfd4.md#insn-0065dfe0)
- 新版 [`0065e38c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0065e/0065e384.md#insn-0065e38c) · [`0065e390`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0065e/0065e384.md#insn-0065e390)

~~~diff
- 0065dfdc ["COPY", "register:4050:8", ["const:c74000:8"]]
+ 0065e38c ["COPY", "register:4050:8", ["const:c75000:8"]]
- 0065dfdc bytes aa3000f0
+ 0065e38c bytes aa3000f0
- 0065dfe0 ["COPY", "tmp:0:8", ["const:318:8"]]
- 0065dfe0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0065dfe0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0065dfe0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0065e390 ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 0065e390 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0065e390 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0065e390 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0065dfe0 bytes 4a610c91
+ 0065e390 bytes 4aa10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad5534b3d6b58336431d9ab5fc608ef9"></a>

### [`0065e018`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0065e/0065e018.md) → [`0065e3c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0065e/0065e3c8.md) FUN_0065e3c8

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0065e3e0",
      "incomplete_value": false,
      "site": "0065e3ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:2e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0065e030",
      "incomplete_value": false,
      "site": "0065e03c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:318:8"
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
      "0065e3ec",
      "DATA",
      [
        "storage",
        "00c74318",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0065e3ec",
      "DATA",
      [
        "storage",
        "00c752e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0065e02c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0065e/0065e018.md#insn-0065e02c) · [`0065e030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0065e/0065e018.md#insn-0065e030) · [`0065e060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0065e/0065e018.md#insn-0065e060)
- 新版 [`0065e3dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0065e/0065e3c8.md#insn-0065e3dc) · [`0065e3e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0065e/0065e3c8.md#insn-0065e3e0) · [`0065e410`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0065e/0065e3c8.md#insn-0065e410)

~~~diff
- 0065e02c ["COPY", "register:4040:8", ["const:c74000:8"]]
+ 0065e3dc ["COPY", "register:4040:8", ["const:c75000:8"]]
- 0065e02c bytes a83000d0
+ 0065e3dc bytes a83000f0
- 0065e030 ["COPY", "tmp:0:8", ["const:318:8"]]
- 0065e030 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0065e030 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0065e030 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0065e3e0 ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 0065e3e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0065e3e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0065e3e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0065e030 bytes 08610c91
+ 0065e3e0 bytes 08a10b91
- 0065e060 ["COPY", "register:0:8", ["register:4040:8"]]
- 0065e060 ["INT_ADD", "register:40f0:8", ["const:65e060:8", "const:4:8"]]
- 0065e060 ["CALLIND", null, ["register:0:8"]]
+ 0065e410 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0065e410 ["INT_ADD", "register:40f0:8", ["const:65e410:8", "const:4:8"]]
+ 0065e410 ["CALLIND", null, ["register:0:8"]]
- 0065e060 bytes 00013fd6
+ 0065e410 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16b68fc99cd2cc5724bce00f00aeeec7"></a>

### [`0065e074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0065e/0065e074.md) → [`0065e424`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0065e/0065e424.md) FUN_0065e424

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.55% / 新版 93.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0065e44c",
      "incomplete_value": false,
      "site": "0065e450",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:2e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0065e09c",
      "incomplete_value": false,
      "site": "0065e0a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:318:8"
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
      "0065e450",
      "DATA",
      [
        "storage",
        "00c74318",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0065e450",
      "DATA",
      [
        "storage",
        "00c752e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0065e088`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0065e/0065e074.md#insn-0065e088) · [`0065e098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0065e/0065e074.md#insn-0065e098) · [`0065e09c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0065e/0065e074.md#insn-0065e09c)
- 新版 [`0065e438`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0065e/0065e424.md#insn-0065e438) · [`0065e448`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0065e/0065e424.md#insn-0065e448) · [`0065e44c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0065e/0065e424.md#insn-0065e44c)

~~~diff
- 0065e088 ["INT_ADD", "register:40f0:8", ["const:65e088:8", "const:4:8"]]
- 0065e088 ["CALL", null, ["callee:00c58f30:8"]]
+ 0065e438 ["INT_ADD", "register:40f0:8", ["const:65e438:8", "const:4:8"]]
+ 0065e438 ["CALL", null, ["callee:00c58f30:8"]]
- 0065e088 bytes b6e71794
+ 0065e438 bytes beea1794
- 0065e098 ["COPY", "register:4048:8", ["const:c74000:8"]]
+ 0065e448 ["COPY", "register:4048:8", ["const:c75000:8"]]
- 0065e098 bytes a93000d0
+ 0065e448 bytes a93000f0
- 0065e09c ["COPY", "tmp:0:8", ["const:318:8"]]
- 0065e09c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0065e09c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0065e09c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0065e44c ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 0065e44c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0065e44c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0065e44c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0065e09c bytes 29610c91
+ 0065e44c bytes 29a10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

