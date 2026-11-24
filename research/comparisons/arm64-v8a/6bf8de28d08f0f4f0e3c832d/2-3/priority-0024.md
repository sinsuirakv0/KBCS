# v16.0.2 → v16.0.3 · 最優先の変更候補 (24)

[一覧の目次](README.md)

<a id="compare-9bf4848eabe250b37705956c964040eb"></a>

### [`005c2a90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c2/005c2a90.md) → [`005c2e40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c2/005c2e40.md) FUN_005c2e40

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`005bc80c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bc/005bc80c.md) [`005c2a90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c2/005c2a90.md) · 呼出先 2件 [`005c2a90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c2/005c2a90.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 2件 [`005bcbbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005bc/005bcbbc.md) [`005c2e40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c2/005c2e40.md) · 呼出先 2件 [`005c2e40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c2/005c2e40.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 58.82% / 新版 58.82%

CFGの説明率　旧版 25.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c2a94"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c2a94"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c2a98"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005c2a94",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:005c2a98",
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
      "005c2e44",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005c2e48",
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

- 旧版 [`005c2a94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c2/005c2a90.md#insn-005c2a94) · [`005c2a98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c2/005c2a90.md#insn-005c2a98) · [`005c2ab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c2/005c2a90.md#insn-005c2ab0)
- 新版 [`005c2e60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c2/005c2e40.md#insn-005c2e60)

~~~diff
- 005c2a94 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005c2a94 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005c2a94 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 005c2a94 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005c2a94 bytes fd7bbea9
- 005c2a98 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 005c2a98 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 005c2a98 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 005c2a98 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005c2a98 bytes f44f01a9
- 005c2ab0 ["INT_ADD", "register:40f0:8", ["const:5c2ab0:8", "const:4:8"]]
- 005c2ab0 ["CALL", null, ["local:b0:8"]]
+ 005c2e60 ["INT_ADD", "register:40f0:8", ["const:5c2e60:8", "const:4:8"]]
+ 005c2e60 ["CALL", null, ["local:b0:8"]]
- 005c2ab0 bytes f8ffff97
+ 005c2e60 bytes f8ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-882c436b1c597d66a965c24dce705728"></a>

### [`005c2ad4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c2/005c2ad4.md) → [`005c2e84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c2/005c2e84.md) FUN_005c2e84

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`005bc80c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005bc/005bc80c.md) [`005c2ad4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c2/005c2ad4.md) · 呼出先 7件 [`005c2ad4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c2/005c2ad4.md) [`005c3778`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c3/005c3778.md) [`005c3938`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c3/005c3938.md) [`005c3b04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c3/005c3b04.md) [`005c3d5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c3/005c3d5c.md)
- 新版 呼出元 2件 [`005bcbbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005bc/005bcbbc.md) [`005c2e84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c2/005c2e84.md) · 呼出先 7件 [`005c2e84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c2/005c2e84.md) [`005c3b28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c3/005c3b28.md) [`005c3ce8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c3/005c3ce8.md) [`005c3eb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c3/005c3eb4.md) [`005c410c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c4/005c410c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 68.36% / 新版 68.36%

CFGの説明率　旧版 23.18% / 新版 22.97%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 29件, `store_condition` 5件, `unresolved_branch_alignment` 13件, `unresolved_call_alignment` 42件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c2ae4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c2ae4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c2b14"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005c2ae4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:005c2b14",
      "WRITE",
      [
        "storage",
        "Stack[-0x88]",
        null,
        null
      ]
    ],
    [
      "unmatched:005c2b18",
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
      "005c2e94",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "005c2ec4",
      "WRITE",
      [
        "storage",
        "Stack[-0x88]",
        null,
        null
      ]
    ],
    [
      "005c2ec8",
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

- 旧版 [`005c2ae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c2/005c2ad4.md#insn-005c2ae4) · [`005c2b14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c2/005c2ad4.md#insn-005c2b14) · [`005c2b18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c2/005c2ad4.md#insn-005c2b18)

~~~diff
- 005c2ae4 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 005c2ae4 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 005c2ae4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 005c2ae4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005c2ae4 bytes f85f06a9
- 005c2b14 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 005c2b14 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 005c2b14 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:8:8"]]
- 005c2b14 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005c2b14 bytes e8a700a9
- 005c2b18 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 005c2b18 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff0:8"]]
- 005c2b18 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 005c2b18 bytes b5031ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-777c6bea05723419ea0cbfc7e8c6c11d"></a>

### [`005c3778`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c3/005c3778.md) → [`005c3b28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c3/005c3b28.md) FUN_005c3b28

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`005c2ad4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c2/005c2ad4.md) [`005c3b04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c3/005c3b04.md) · 呼出先 3件 [`005c3d5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c3/005c3d5c.md) [`00664e50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00664/00664e50.md) [`00b000f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b00/00b000f0.md)
- 新版 呼出元 2件 [`005c2e84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c2/005c2e84.md) [`005c3eb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c3/005c3eb4.md) · 呼出先 3件 [`005c410c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c4/005c410c.md) [`00665200`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00665/00665200.md) [`00b010e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b01/00b010e4.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 97.32% / 新版 97.32%

CFGの説明率　旧版 66.67% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 2件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005c38b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "005c3c60"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "005c38b0"
      ],
      [
        "FALL_THROUGH",
        "005c3c60"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "005c3c60",
      "incomplete_value": true,
      "site": "005c3c6c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "live",
            "register:100:1"
          ],
          [
            "live",
            "register:103:1"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005c38b0",
      "incomplete_value": true,
      "site": "005c38bc",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SLESS",
            "1",
            [
              "INT_SUB",
              [
                "leaf",
                "const:0:4"
              ]
            ]
          ],
          [
            "INT_SBORROW",
            "1",
            [
              [
                "live",
                "register:40b8:4"
              ],
              [
                "live",
                "register:4000:4"
              ]
            ]
          ]
        ]
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
      "unmatched:005c38b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005c3cd0"
      ]
    ]
  ],
  "added": [
    [
      "005c3c60",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005c3cd0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005c38b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c3/005c3778.md#insn-005c38b0) · [`005c37ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c3/005c3778.md#insn-005c37ac)
- 新版 [`005c3c60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c3/005c3b28.md#insn-005c3c60) · [`005c3b5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c3/005c3b28.md#insn-005c3b5c)

~~~diff
- 005c38b0 ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 005c38b0 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 005c38b0 bytes 8a030054
+ 005c3c60 ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 005c3c60 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 005c3c60 bytes 8a030054
- 005c37ac ["INT_ADD", "register:40f0:8", ["const:5c37ac:8", "const:4:8"]]
- 005c37ac ["CALL", null, ["callee:005c410c:8"]]
+ 005c3b5c ["INT_ADD", "register:40f0:8", ["const:5c3b5c:8", "const:4:8"]]
+ 005c3b5c ["CALL", null, ["callee:005c410c:8"]]
- 005c37ac bytes 6c010094
+ 005c3b5c bytes 6c010094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a6c95f14bf0b878314ea54f95001c14"></a>

### [`005c3938`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c3/005c3938.md) → [`005c3ce8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c3/005c3ce8.md) FUN_005c3ce8

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`005c2ad4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c2/005c2ad4.md) [`005c3b04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c3/005c3b04.md) [`005c3d5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c3/005c3d5c.md) · 呼出先 2件 [`00664e50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00664/00664e50.md) [`00b000f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b00/00b000f0.md)
- 新版 呼出元 3件 [`005c2e84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c2/005c2e84.md) [`005c3eb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c3/005c3eb4.md) [`005c410c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c4/005c410c.md) · 呼出先 2件 [`00665200`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00665/00665200.md) [`00b010e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b01/00b010e4.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 83.48% / 新版 83.48%

CFGの説明率　旧版 21.05% / 新版 22.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c3938"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c3938"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c393c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005c3938",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:005c393c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:005c3940",
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
      "005c3ce8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "005c3cec",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "005c3cf0",
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

- 旧版 [`005c3938`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c3/005c3938.md#insn-005c3938) · [`005c393c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c3/005c3938.md#insn-005c393c) · [`005c3940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c3/005c3938.md#insn-005c3940)

~~~diff
- 005c3938 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005c3938 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005c3938 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 005c3938 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005c3938 bytes fd7bbba9
- 005c393c ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 005c393c ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 005c393c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 005c393c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005c393c bytes fa6701a9
- 005c3940 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 005c3940 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 005c3940 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 005c3940 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005c3940 bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b6486d8fe50f474e6dd3b3ec5fdb4c8"></a>

### [`005c3b04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c3/005c3b04.md) → [`005c3eb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c3/005c3eb4.md) FUN_005c3eb4

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005c2ad4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c2/005c2ad4.md) · 呼出先 5件 [`005c3778`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c3/005c3778.md) [`005c3938`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c3/005c3938.md) [`005c3d5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c3/005c3d5c.md) [`00664e50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00664/00664e50.md) [`00b000f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b00/00b000f0.md)
- 新版 呼出元 1件 [`005c2e84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c2/005c2e84.md) · 呼出先 5件 [`005c3b28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c3/005c3b28.md) [`005c3ce8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c3/005c3ce8.md) [`005c410c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c4/005c410c.md) [`00665200`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00665/00665200.md) [`00b010e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b01/00b010e4.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 90.67% / 新版 90.67%

CFGの説明率　旧版 41.46% / 新版 42.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c3cb4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005c4064"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005c3c9c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005c3b68",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00b010e4"
      ]
    ],
    [
      "unmatched:005c3b74",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00665200"
      ]
    ],
    [
      "unmatched:005c3c9c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005c3fec"
      ]
    ]
  ],
  "added": [
    [
      "005c3f18",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00b010e4"
      ]
    ],
    [
      "005c3f24",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00665200"
      ]
    ],
    [
      "005c404c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005c3fec"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005c3b68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c3/005c3b04.md#insn-005c3b68) · [`005c3b74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c3/005c3b04.md#insn-005c3b74) · [`005c3b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c3/005c3b04.md#insn-005c3b88)
- 新版 [`005c3f38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c3/005c3eb4.md#insn-005c3f38)

~~~diff
- 005c3b68 ["INT_ADD", "register:40f0:8", ["const:5c3b68:8", "const:4:8"]]
- 005c3b68 ["CALL", null, ["callee:00b010e4:8"]]
- 005c3b68 bytes 62f11494
- 005c3b74 ["INT_ADD", "register:40f0:8", ["const:5c3b74:8", "const:4:8"]]
- 005c3b74 ["CALL", null, ["callee:00665200:8"]]
- 005c3b74 bytes b7840294
- 005c3b88 ["INT_ADD", "register:40f0:8", ["const:5c3b88:8", "const:4:8"]]
- 005c3b88 ["CALL", null, ["callee:00b010e4:8"]]
+ 005c3f38 ["INT_ADD", "register:40f0:8", ["const:5c3f38:8", "const:4:8"]]
+ 005c3f38 ["CALL", null, ["callee:00b010e4:8"]]
- 005c3b88 bytes 5af11494
+ 005c3f38 bytes 6bf41494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-793a03f707dd4946ed2f3ecb7d109553"></a>

### [`005c3d5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c3/005c3d5c.md) → [`005c410c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c4/005c410c.md) FUN_005c410c

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`005c2ad4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c2/005c2ad4.md) [`005c3778`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c3/005c3778.md) [`005c3b04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c3/005c3b04.md) · 呼出先 3件 [`005c3938`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c3/005c3938.md) [`00664e50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00664/00664e50.md) [`00b000f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b00/00b000f0.md)
- 新版 呼出元 3件 [`005c2e84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c2/005c2e84.md) [`005c3b28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c3/005c3b28.md) [`005c3eb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c3/005c3eb4.md) · 呼出先 3件 [`005c3ce8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c3/005c3ce8.md) [`00665200`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00665/00665200.md) [`00b010e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b01/00b010e4.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.45% / 新版 95.45%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005c4158",
      "incomplete_value": true,
      "site": "005c4160",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:40c0:4"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005c4154",
      "incomplete_value": true,
      "site": "005c4160",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:4000:4"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005c4150",
      "incomplete_value": true,
      "site": "005c4160",
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
                "register:40a8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 2,
    "slot": 3
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`005c3db0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c3/005c3d5c.md#insn-005c3db0) · [`005c3dbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c3/005c3d5c.md#insn-005c3dbc) · [`005c3e88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c3/005c3d5c.md#insn-005c3e88)
- 新版 [`005c4160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c4/005c410c.md#insn-005c4160) · [`005c416c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c4/005c410c.md#insn-005c416c) · [`005c4238`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c4/005c410c.md#insn-005c4238)

~~~diff
- 005c3db0 ["INT_ADD", "register:40f0:8", ["const:5c3db0:8", "const:4:8"]]
- 005c3db0 ["CALL", null, ["callee:00b010e4:8"]]
+ 005c4160 ["INT_ADD", "register:40f0:8", ["const:5c4160:8", "const:4:8"]]
+ 005c4160 ["CALL", null, ["callee:00b010e4:8"]]
- 005c3db0 bytes d0f01494
+ 005c4160 bytes e1f31494
- 005c3dbc ["INT_ADD", "register:40f0:8", ["const:5c3dbc:8", "const:4:8"]]
- 005c3dbc ["CALL", null, ["callee:00665200:8"]]
+ 005c416c ["INT_ADD", "register:40f0:8", ["const:5c416c:8", "const:4:8"]]
+ 005c416c ["CALL", null, ["callee:00665200:8"]]
- 005c3dbc bytes 25840294
+ 005c416c bytes 25840294
- 005c3e88 ["INT_ADD", "register:40f0:8", ["const:5c3e88:8", "const:4:8"]]
- 005c3e88 ["CALL", null, ["callee:00b010e4:8"]]
+ 005c4238 ["INT_ADD", "register:40f0:8", ["const:5c4238:8", "const:4:8"]]
+ 005c4238 ["CALL", null, ["callee:00b010e4:8"]]
- 005c3e88 bytes 9af01494
+ 005c4238 bytes abf31494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91d216996580bc6a4ff5a347414ac019"></a>

### [`005c3f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c3/005c3f0c.md) → [`005c42bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c4/005c42bc.md) _INIT_64

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 74.01% / 新版 74.01%

CFGの説明率　旧版 21.43% / 新版 20.45%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c3f10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c3f10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c3f14"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005c3f10",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:005c3f14",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:005c3f18",
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
      "005c42c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "005c42c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005c42c8",
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

- 旧版 [`005c3f10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c3/005c3f0c.md#insn-005c3f10) · [`005c3f14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c3/005c3f0c.md#insn-005c3f14) · [`005c3f18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c3/005c3f0c.md#insn-005c3f18)

~~~diff
- 005c3f10 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005c3f10 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005c3f10 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:f0:8"]]
- 005c3f10 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005c3f10 bytes fd7b0fa9
- 005c3f14 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 005c3f14 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 005c3f14 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:100:8"]]
- 005c3f14 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005c3f14 bytes fc5710a9
- 005c3f18 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 005c3f18 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 005c3f18 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:110:8"]]
- 005c3f18 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005c3f18 bytes f44f11a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a8a359b2e60492b34a1d2651950f894"></a>

### [`005c429c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c4/005c429c.md) → [`005c464c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c4/005c464c.md) FUN_005c464c

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005c8f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c8/005c8f3c.md) · 呼出先 16件 [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0047e64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e64c.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`005c45e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c4/005c45e0.md) [`00687668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00687/00687668.md)
- 新版 呼出元 1件 [`005c92ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c9/005c92ec.md) · 呼出先 16件 [`00448254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448254.md) [`0047e96c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047e/0047e96c.md) [`0047f114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047f/0047f114.md) [`005c4990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c4/005c4990.md) [`00687a18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00687/00687a18.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 71.95% / 新版 71.95%

CFGの説明率　旧版 22.22% / 新版 22.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c42cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c42d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c42d8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005c42cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:005c42e0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005c46a0"
      ]
    ],
    [
      "unmatched:005c4344",
      "READ",
      [
        "storage",
        "00ca5038",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "005c467c",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "005c4690",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005c46a0"
      ]
    ],
    [
      "005c46f4",
      "READ",
      [
        "storage",
        "00ca5ff8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005c42cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c4/005c429c.md#insn-005c42cc) · [`005c42d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c4/005c429c.md#insn-005c42d0) · [`005c42d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c4/005c429c.md#insn-005c42d8)

~~~diff
- 005c42cc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 005c42cc ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 005c42cc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 005c42cc bytes a8831ff8
- 005c42d0 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 005c42d0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 005c42d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 005c42d0 bytes 1f0000f9
- 005c42d8 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 005c42d8 ["INT_ADD", "register:40a0:8", ["register:40a0:8", "const:8:8"]]
- 005c42d8 ["STORE", null, ["const:1b1:8", "register:40a0:8", "tmp:0:8"]]
- 005c42d8 bytes 898e00f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84085d2b5d8625ddb2267fabe1269648"></a>

### [`005c45e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c4/005c45e0.md) → [`005c4990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c4/005c4990.md) FUN_005c4990

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`005c429c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c4/005c429c.md) [`005c69b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c6/005c69b8.md) · 呼出先 12件 [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`00684ff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00684/00684ff0.md) [`006853b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00685/006853b4.md) [`006855c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00685/006855c8.md) [`00687668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00687/00687668.md)
- 新版 呼出元 2件 [`005c464c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c4/005c464c.md) [`005c6d68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c6/005c6d68.md) · 呼出先 12件 [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md) [`006853a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00685/006853a0.md) [`00685764`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00685/00685764.md) [`00685978`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00685/00685978.md) [`00687a18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00687/00687a18.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 79.46% / 新版 79.46%

CFGの説明率　旧版 27.78% / 新版 28.85%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `unresolved_branch_alignment` 5件, `unresolved_store_alignment` 17件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c45e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c45e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c45e8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005c45e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:005c45e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:005c45ec",
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
      "005c4994",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "005c4998",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "005c499c",
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

- 旧版 [`005c45e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c4/005c45e0.md#insn-005c45e4) · [`005c45e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c4/005c45e0.md#insn-005c45e8) · [`005c45ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c4/005c45e0.md#insn-005c45ec)

~~~diff
- 005c45e4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005c45e4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005c45e4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 005c45e4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005c45e4 bytes fd7b06a9
- 005c45e8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:70:8"]]
- 005c45e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 005c45e8 bytes f93b00f9
- 005c45ec ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 005c45ec ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 005c45ec ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 005c45ec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005c45ec bytes f85f08a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b64e926a91ae8ec4ee188152e949d5f7"></a>

### [`005c4998`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c4/005c4998.md) → [`005c4d48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c4/005c4d48.md) FUN_005c4d48

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005c7d40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c7/005c7d40.md) · 呼出先 30件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00467ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467ba0.md) [`00469d0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00469/00469d0c.md) [`0046a290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046a/0046a290.md)
- 新版 呼出元 1件 [`005c80f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c8/005c80f0.md) · 呼出先 30件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00467bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467bc0.md) [`00467ec0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467ec0.md) [`0046a02c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046a/0046a02c.md) [`0046a5b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046a/0046a5b0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 71.27% / 新版 71.27%

CFGの説明率　旧版 20.42% / 新版 19.87%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 102件, `store_condition` 4件, `unresolved_branch_alignment` 20件, `unresolved_call_alignment` 42件, `unresolved_store_alignment` 35件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c499c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c499c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c49a0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005c499c",
      "WRITE",
      [
        "storage",
        "Stack[-0xa0]",
        null,
        null
      ]
    ],
    [
      "unmatched:005c49a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x90]",
        null,
        null
      ]
    ],
    [
      "unmatched:005c49a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x80]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005c4d4c",
      "WRITE",
      [
        "storage",
        "Stack[-0xa0]",
        null,
        null
      ]
    ],
    [
      "005c4d50",
      "WRITE",
      [
        "storage",
        "Stack[-0x90]",
        null,
        null
      ]
    ],
    [
      "005c4d54",
      "WRITE",
      [
        "storage",
        "Stack[-0x80]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005c499c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c4/005c4998.md#insn-005c499c) · [`005c49a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c4/005c4998.md#insn-005c49a0) · [`005c49a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c4/005c4998.md#insn-005c49a4)

~~~diff
- 005c499c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:50:8"]]
- 005c499c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:51e0:8"]]
- 005c499c ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:8:8"]]
- 005c499c ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:51c0:8"]]
- 005c499c bytes ef3b056d
- 005c49a0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:60:8"]]
- 005c49a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:51a0:8"]]
- 005c49a0 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:8:8"]]
- 005c49a0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5180:8"]]
- 005c49a0 bytes ed33066d
- 005c49a4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:70:8"]]
- 005c49a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5160:8"]]
- 005c49a4 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:8:8"]]
- 005c49a4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5140:8"]]
- 005c49a4 bytes eb2b076d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc1acaad08d330f32519e636ee13e83f"></a>

### [`005c5f90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c5/005c5f90.md) → [`005c6340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c6/005c6340.md) FUN_005c6340

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`005c4998`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c4/005c4998.md) [`005c69b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c6/005c69b8.md) [`005c8f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c8/005c8f3c.md) · 呼出先 4件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00664c0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00664/00664c0c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)
- 新版 呼出元 3件 [`005c4d48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c4/005c4d48.md) [`005c6d68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c6/005c6d68.md) [`005c92ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c9/005c92ec.md) · 呼出先 4件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00664fbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00664/00664fbc.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c59130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59130.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.67% / 新版 97.67%

CFGの説明率　旧版 75.00% / 新版 72.41%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005c5fb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c5/005c5f90.md#insn-005c5fb4) · [`005c5fcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c5/005c5f90.md#insn-005c5fcc) · [`005c6038`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c5/005c5f90.md#insn-005c6038)
- 新版 [`005c6364`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c6/005c6340.md#insn-005c6364) · [`005c637c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c6/005c6340.md#insn-005c637c) · [`005c63e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c6/005c6340.md#insn-005c63e8)

~~~diff
- 005c5fb4 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 005c5fb4 ["CBRANCH", null, ["local:b34:8", "tmp:0:1"]]
+ 005c6364 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 005c6364 ["CBRANCH", null, ["local:b36:8", "tmp:0:1"]]
- 005c5fb4 bytes c80d00b4
+ 005c6364 bytes c80d00b4
- 005c5fcc ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 005c5fcc ["CBRANCH", null, ["local:b34:8", "tmp:0:1"]]
+ 005c637c ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 005c637c ["CBRANCH", null, ["local:b36:8", "tmp:0:1"]]
- 005c5fcc bytes 080d00b4
+ 005c637c bytes 080d00b4
- 005c6038 ["INT_ADD", "register:40f0:8", ["const:5c6038:8", "const:4:8"]]
- 005c6038 ["CALL", null, ["callee:00c58f30:8"]]
+ 005c63e8 ["INT_ADD", "register:40f0:8", ["const:5c63e8:8", "const:4:8"]]
+ 005c63e8 ["CALL", null, ["callee:00c58f30:8"]]
- 005c6038 bytes ca471a94
+ 005c63e8 bytes d24a1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51dfa12d37d5f88649bc32de2f58ba56"></a>

### [`005c6194`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c6/005c6194.md) → [`005c6544`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c6/005c6544.md) FUN_005c6544

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 8件 [`005fe6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe6ac.md) [`00606b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00606/00606b24.md) [`006103fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00610/006103fc.md) [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) [`00a466a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a466a4.md) · 呼出先 2件 [`005d8c08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d8/005d8c08.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 8件 [`005fea5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005fe/005fea5c.md) [`00606ed4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00606/00606ed4.md) [`006107ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00610/006107ac.md) [`007cdea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007cd/007cdea8.md) [`00a47698`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a47/00a47698.md) · 呼出先 2件 [`005d8fb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d8/005d8fb8.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 63.16% / 新版 63.16%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c6194"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c6194"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c6198"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005c6194",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:005c6198",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:005c61b4",
      "READ",
      [
        "storage",
        "00c9b438",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005c6544",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005c6548",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005c6564",
      "READ",
      [
        "storage",
        "00c9c408",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005c6194`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c6/005c6194.md#insn-005c6194) · [`005c6198`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c6/005c6194.md#insn-005c6198) · [`005c61bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c6/005c6194.md#insn-005c61bc)

~~~diff
- 005c6194 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005c6194 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005c6194 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 005c6194 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005c6194 bytes fd7bbea9
- 005c6198 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 005c6198 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 005c6198 bytes f30b00f9
- 005c61bc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 005c61bc ["COPY", "tmp:1:8", ["register:4000:8"]]
- 005c61bc ["INT_ADD", "register:4000:8", ["register:4000:8", "const:50:8"]]
- 005c61bc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 005c61bc bytes 080405f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e06c8e5c9f4af49081e24d5e56ea1d73"></a>

### [`005c61e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c6/005c61e0.md) → [`005c6590`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c6/005c6590.md) FUN_005c6590

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`005fe6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe6ac.md) [`00606b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00606/00606b24.md) [`006103fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00610/006103fc.md) [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) · 呼出先 4件 [`005d8c08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d8/005d8c08.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 4件 [`005fea5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005fe/005fea5c.md) [`00606ed4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00606/00606ed4.md) [`006107ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00610/006107ac.md) [`007cdea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007cd/007cdea8.md) · 呼出先 4件 [`005d8fb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d8/005d8fb8.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 82.86% / 新版 82.86%

CFGの説明率　旧版 50.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005c65b4",
      "incomplete_value": false,
      "site": "005c65b8",
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
                "const:c8c000:8"
              ],
              [
                "leaf",
                "const:840:8"
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
      "definition_site": "005c6204",
      "incomplete_value": false,
      "site": "005c6208",
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
                "const:c8b000:8"
              ],
              [
                "leaf",
                "const:870:8"
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c6248"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005c65f8"
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
      "005c65b8",
      "DATA",
      [
        "storage",
        "00c8b880",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:005c6240",
      "READ",
      [
        "storage",
        "00c9b438",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:005c6248",
      "DATA",
      [
        "storage",
        "00c8b828",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005c65b8",
      "DATA",
      [
        "storage",
        "00c8c850",
        null,
        "undefined *"
      ]
    ],
    [
      "005c65f0",
      "READ",
      [
        "storage",
        "00c9c408",
        null,
        "pointer"
      ]
    ],
    [
      "005c65f8",
      "DATA",
      [
        "storage",
        "00c8c7f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005c6248`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c6/005c61e0.md#insn-005c6248) · [`005c61f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c6/005c61e0.md#insn-005c61f4)
- 新版 [`005c65f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c6/005c6590.md#insn-005c65f8) · [`005c65a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c6/005c6590.md#insn-005c65a4)

~~~diff
- 005c6248 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 005c6248 ["COPY", "tmp:1:8", ["register:4000:8"]]
- 005c6248 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:50:8"]]
- 005c6248 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 005c6248 bytes 080405f8
+ 005c65f8 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 005c65f8 ["COPY", "tmp:1:8", ["register:4000:8"]]
+ 005c65f8 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:50:8"]]
+ 005c65f8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 005c65f8 bytes 080405f8
- 005c61f4 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 005c61f4 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 005c65a4 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
+ 005c65a4 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 005c61f4 bytes 730300b4
+ 005c65a4 bytes 730300b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-720429d3469db95e52c1feac7c3f4104"></a>

### [`005c626c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c6/005c626c.md) → [`005c661c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c6/005c661c.md) FUN_005c661c

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`005c69b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c6/005c69b8.md) [`00700b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/00700b50.md) [`00adf288`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00adf/00adf288.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 3件 [`005c6d68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c6/005c6d68.md) [`00700f00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00700/00700f00.md) [`00ae027c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ae0/00ae027c.md) · 呼出先 2件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 92.45% / 新版 92.45%

CFGの説明率　旧版 31.58% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c62e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c62ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005c6694"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`005c62e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c6/005c626c.md#insn-005c62e4) · [`005c62ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c6/005c626c.md#insn-005c62ec) · [`005c6318`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c6/005c626c.md#insn-005c6318)
- 新版 [`005c66c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c6/005c661c.md#insn-005c66c8)

~~~diff
- 005c62e4 ["COPY", "tmp:0:8", ["const:0:8"]]
- 005c62e4 ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 005c62e4 ["INT_ADD", "register:4040:8", ["register:4040:8", "const:30:8"]]
- 005c62e4 ["STORE", null, ["const:1b1:8", "register:4040:8", "tmp:1:8"]]
- 005c62e4 bytes 1f0d03f8
- 005c62ec ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:28:8"]]
- 005c62ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 005c62ec bytes 081400f9
- 005c6318 ["INT_ADD", "register:40f0:8", ["const:5c6318:8", "const:4:8"]]
- 005c6318 ["CALL", null, ["callee:0043bf04:8"]]
+ 005c66c8 ["INT_ADD", "register:40f0:8", ["const:5c66c8:8", "const:4:8"]]
+ 005c66c8 ["CALL", null, ["callee:0043bf04:8"]]
- 005c6318 bytes 33d6f997
+ 005c66c8 bytes 0fd6f997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32ca9bcdec6b6f7feb933fd105d89679"></a>

### [`005c6340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c6/005c6340.md) → [`005c66f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c6/005c66f0.md) FUN_005c66f0

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0098546c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00985/0098546c.md) · 呼出先 23件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`0048795c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048795c.md) [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md)
- 新版 呼出元 1件 [`00986418`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00986/00986418.md) · 呼出先 23件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`00487c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c7c.md) [`00487c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c9c.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 79.69% / 新版 79.69%

CFGの説明率　旧版 41.84% / 新版 41.26%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `store_destination` 1件, `store_value` 3件, `unresolved_branch_alignment` 8件, `unresolved_call_alignment` 7件, `unresolved_store_alignment` 26件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c6358"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c6358"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c636c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005c6358",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:005c636c",
      "WRITE",
      [
        "storage",
        "Stack[-0x1f0]",
        null,
        null
      ]
    ],
    [
      "unmatched:005c6378",
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
      "005c6708",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005c671c",
      "WRITE",
      [
        "storage",
        "Stack[-0x1f0]",
        null,
        null
      ]
    ],
    [
      "005c6728",
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

- 旧版 [`005c6358`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c6/005c6340.md#insn-005c6358) · [`005c636c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c6/005c6340.md#insn-005c636c) · [`005c6378`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c6/005c6340.md#insn-005c6378)

~~~diff
- 005c6358 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 005c6358 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 005c6358 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:1e0:8"]]
- 005c6358 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005c6358 bytes f44f1ea9
- 005c636c ["COPY", "tmp:0:8", ["register:8:8"]]
- 005c636c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 005c636c bytes e80300f9
- 005c6378 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 005c6378 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff0:8"]]
- 005c6378 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 005c6378 bytes a8031ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bab0d876ac77bae8782e842b4029945c"></a>

### [`005c69b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c6/005c69b8.md) → [`005c6d68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c6/005c6d68.md) FUN_005c6d68

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0098dc5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0098d/0098dc5c.md) · 呼出先 37件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0044d960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044d960.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`0046da94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046da94.md) [`0046db14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046db14.md)
- 新版 呼出元 1件 [`0098ec08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0098e/0098ec08.md) · 呼出先 37件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0044dc80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044d/0044dc80.md) [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md) [`0046ddb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046ddb4.md) [`0046de34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046de34.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 87.66% / 新版 87.66%

CFGの説明率　旧版 17.43% / 新版 17.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 30件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 18件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c6a98"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c6a9c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c6aa0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005c6dd0",
      "DATA",
      [
        "storage",
        "0039b1b4",
        null,
        "dword"
      ]
    ],
    [
      "005c6de8",
      "DATA",
      [
        "storage",
        "0039b1bc",
        null,
        "qword"
      ]
    ],
    [
      "005c6e00",
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
      "005c6dd0",
      "DATA",
      [
        "storage",
        "0039b1b4",
        null,
        "qword"
      ]
    ],
    [
      "005c6de8",
      "DATA",
      [
        "storage",
        "0039b1bc",
        null,
        "dword"
      ]
    ],
    [
      "005c6e00",
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

- 旧版 [`005c6a74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c6/005c69b8.md#insn-005c6a74) · [`005c6a98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c6/005c69b8.md#insn-005c6a98) · [`005c6a9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c6/005c69b8.md#insn-005c6a9c)

~~~diff
- 005c6a74 ["INT_ADD", "register:40f0:8", ["const:5c6a74:8", "const:4:8"]]
- 005c6a74 ["CALL", null, ["ram:48cd38:8"]]
- 005c6a74 bytes b118fb97
- 005c6a98 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 005c6a98 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:8:8"]]
- 005c6a98 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 005c6a98 bytes e8230039
- 005c6a9c ["COPY", "tmp:0:4", ["register:4050:4"]]
- 005c6a9c ["INT_ADD", "tmp:1:8", ["register:8:8", "const:11:8"]]
- 005c6a9c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 005c6a9c bytes ea130178
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1864a9f6f4e83ac57a9fbcba82bd3ced"></a>

### [`005c7260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c7/005c7260.md) → [`005c7610`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c7/005c7610.md) FUN_005c7610

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005c69b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c6/005c69b8.md) · 呼出先 12件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00859ba4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00859/00859ba4.md) [`0085b2fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085b/0085b2fc.md)
- 新版 呼出元 1件 [`005c6d68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c6/005c6d68.md) · 呼出先 12件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`0085ab50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0085a/0085ab50.md) [`0085c2a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0085c/0085c2a8.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 90.24% / 新版 90.24%

CFGの説明率　旧版 29.03% / 新版 28.12%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_condition` 1件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c7260"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c7260"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c7264"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005c7260",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:005c7264",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:005c7278",
      "READ",
      [
        "storage",
        "002c4198",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "005c7610",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005c7614",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005c7628",
      "READ",
      [
        "storage",
        "002c41e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005c7260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c7/005c7260.md#insn-005c7260) · [`005c7264`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c7/005c7260.md#insn-005c7264) · [`005c72ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c7/005c7260.md#insn-005c72ac)

~~~diff
- 005c7260 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005c7260 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005c7260 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 005c7260 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005c7260 bytes fd7bbea9
- 005c7264 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 005c7264 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 005c7264 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 005c7264 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005c7264 bytes f44f01a9
- 005c72ac ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:320:8"]]
- 005c72ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4060:4"]]
- 005c72ac bytes 0c2003b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1326be8d9b732729833191d28c45f089"></a>

### [`005c7638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c7/005c7638.md) → [`005c79e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c7/005c79e8.md) FUN_005c79e8

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`005c69b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c6/005c69b8.md) [`00606b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00606/00606b24.md) [`0060a8e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0060a/0060a8e0.md) [`00b3d6b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3d/00b3d6b4.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 4件 [`005c6d68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c6/005c6d68.md) [`00606ed4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00606/00606ed4.md) [`0060ac90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0060a/0060ac90.md) [`00b3e6a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3e/00b3e6a8.md) · 呼出先 2件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 83.67% / 新版 83.67%

CFGの説明率　旧版 8.70% / 新版 8.70%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 1件, `unresolved_branch_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c7638"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c7638"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c763c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005c7638",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:005c763c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:005c7640",
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
      "005c79e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "005c79ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "005c79f0",
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

- 旧版 [`005c7638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c7/005c7638.md#insn-005c7638) · [`005c763c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c7/005c7638.md#insn-005c763c) · [`005c7640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c7/005c7638.md#insn-005c7640)

~~~diff
- 005c7638 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005c7638 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005c7638 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 005c7638 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005c7638 bytes fd7bbca9
- 005c763c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 005c763c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 005c763c bytes f70b00f9
- 005c7640 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 005c7640 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 005c7640 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 005c7640 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005c7640 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d7db1b508d5a8c939f1a8c4a911a482"></a>

### [`005c76fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c7/005c76fc.md) → [`005c7aac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c7/005c7aac.md) FUN_005c7aac

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`005c69b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c6/005c69b8.md) [`005c8604`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c8/005c8604.md) [`005c8800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c8/005c8800.md) [`005c8f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c8/005c8f3c.md) · 呼出先 4件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)
- 新版 呼出元 4件 [`005c6d68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c6/005c6d68.md) [`005c89b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c8/005c89b4.md) [`005c8bb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c8/005c8bb0.md) [`005c92ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c9/005c92ec.md) · 呼出先 4件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c59130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59130.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 74.81% / 新版 74.81%

CFGの説明率　旧版 49.09% / 新版 49.39%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 14件, `unresolved_call_alignment` 9件, `unresolved_store_alignment` 29件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c76fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c76fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c7700"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005c76fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:005c7700",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:005c7704",
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
      "005c7aac",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "005c7ab0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "005c7ab4",
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

- 旧版 [`005c76fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c7/005c76fc.md#insn-005c76fc) · [`005c7700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c7/005c76fc.md#insn-005c7700) · [`005c7704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c7/005c76fc.md#insn-005c7704)

~~~diff
- 005c76fc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005c76fc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005c76fc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffa0:8"]]
- 005c76fc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005c76fc bytes fd7bbaa9
- 005c7700 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 005c7700 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 005c7700 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 005c7700 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005c7700 bytes fc6f01a9
- 005c7704 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 005c7704 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 005c7704 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 005c7704 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005c7704 bytes fa6702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17e9bef789d15ff67b88457411eb11eb"></a>

### [`005c7d40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c7/005c7d40.md) → [`005c80f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c8/005c80f0.md) FUN_005c80f0

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00997090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00997/00997090.md) · 呼出先 29件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00467b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467b6c.md) [`00467df4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467df4.md) [`00467f5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467f5c.md)
- 新版 呼出元 1件 [`0099803c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00998/0099803c.md) · 呼出先 29件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00467bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467bc0.md) [`00467e8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467e8c.md) [`00468114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00468/00468114.md) [`0046827c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00468/0046827c.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 88.75% / 新版 88.75%

CFGの説明率　旧版 8.42% / 新版 8.42%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 41件, `unresolved_branch_alignment` 9件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c7d74"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c7f18"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c7f1c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005c7d74",
      "WRITE",
      [
        "storage",
        "Stack[-0xa0]",
        null,
        null
      ]
    ],
    [
      "unmatched:005c7ee8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005c847c"
      ]
    ],
    [
      "005c82ac",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:005c7f10"
      ]
    ]
  ],
  "added": [
    [
      "005c8124",
      "WRITE",
      [
        "storage",
        "Stack[-0xa0]",
        null,
        null
      ]
    ],
    [
      "005c8298",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005c847c"
      ]
    ],
    [
      "005c82ac",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "005c82c0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005c7d74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c7/005c7d40.md#insn-005c7d74) · [`005c7dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c7/005c7d40.md#insn-005c7dfc) · [`005c7ee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c7/005c7d40.md#insn-005c7ee8)
- 新版 [`005c81ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c8/005c80f0.md#insn-005c81ac)

~~~diff
- 005c7d74 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 005c7d74 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffc0:8"]]
- 005c7d74 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 005c7d74 bytes a8031cf8
- 005c7dfc ["INT_ADD", "register:40f0:8", ["const:5c7dfc:8", "const:4:8"]]
- 005c7dfc ["CALL", null, ["callee:004682b4:8"]]
+ 005c81ac ["INT_ADD", "register:40f0:8", ["const:5c81ac:8", "const:4:8"]]
+ 005c81ac ["CALL", null, ["callee:004682b4:8"]]
- 005c7dfc bytes 6680fa97
+ 005c81ac bytes 4280fa97
- 005c7ee8 ["CBRANCH", null, ["local:b43:8", "register:101:1"]]
- 005c7ee8 bytes 200f0054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38294540dcd55d473d6e73ef83eff760"></a>

### [`005c8534`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c8/005c8534.md) → [`005c88e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c8/005c88e4.md) FUN_005c88e4

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 98.08% / 新版 98.08%

CFGの説明率　旧版 40.00% / 新版 36.36%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005c8588"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "005c8938"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "005c8590",
      "incomplete_value": false,
      "site": "005c8594",
      "value": [
        "leaf",
        "const:ffffffffffffffff:8"
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
      "unmatched:005c8588",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005c894c"
      ]
    ]
  ],
  "added": [
    [
      "005c8938",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005c894c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005c8588`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c8/005c8534.md#insn-005c8588) · [`005c8594`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c8/005c8534.md#insn-005c8594)
- 新版 [`005c8944`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c8/005c88e4.md#insn-005c8944) · [`005c8938`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c8/005c88e4.md#insn-005c8938)

~~~diff
- 005c8588 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 005c8588 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 005c8588 bytes b40000b4
- 005c8594 ["INT_ADD", "register:40f0:8", ["const:5c8594:8", "const:4:8"]]
- 005c8594 ["CALL", null, ["callee:00c54d90:8"]]
+ 005c8944 ["INT_ADD", "register:40f0:8", ["const:5c8944:8", "const:4:8"]]
+ 005c8944 ["CALL", null, ["callee:00c54d90:8"]]
- 005c8594 bytes 032e1a94
+ 005c8944 bytes 13311a94
+ 005c8938 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
+ 005c8938 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
+ 005c8938 bytes b40000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e648d96c16b892ea0611766ddb00df9"></a>

### [`005c8604`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c8/005c8604.md) → [`005c89b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c8/005c89b4.md) FUN_005c89b4

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005d8fc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d8/005d8fc4.md) · 呼出先 6件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`005c76fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c7/005c76fc.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00b07288`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b07/00b07288.md) [`00b3bf30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3bf30.md)
- 新版 呼出元 1件 [`005d9374`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d9/005d9374.md) · 呼出先 6件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`005c7aac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c7/005c7aac.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`00b0827c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b08/00b0827c.md) [`00b3cf24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b3c/00b3cf24.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 86.61% / 新版 86.61%

CFGの説明率　旧版 17.78% / 新版 17.39%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 5件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c8604"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c8604"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c8608"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005c8604",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:005c8608",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:005c860c",
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
      "005c89b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "005c89b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "005c89bc",
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

- 旧版 [`005c8604`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c8/005c8604.md#insn-005c8604) · [`005c8608`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c8/005c8604.md#insn-005c8608) · [`005c860c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c8/005c8604.md#insn-005c860c)

~~~diff
- 005c8604 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005c8604 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005c8604 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 005c8604 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005c8604 bytes fd7bbba9
- 005c8608 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 005c8608 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 005c8608 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 005c8608 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005c8608 bytes fa6701a9
- 005c860c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 005c860c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 005c860c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 005c860c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005c860c bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4bc04f66c391f305585d12b6472620d"></a>

### [`005c8800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c8/005c8800.md) → [`005c8bb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c8/005c8bb0.md) FUN_005c8bb0

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005d9f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d9/005d9f8c.md) · 呼出先 13件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`005c76fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c7/005c76fc.md) [`0071c4b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071c/0071c4b8.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b6efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6efc.md)
- 新版 呼出元 1件 [`005da33c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005da/005da33c.md) · 呼出先 13件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`005c7aac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c7/005c7aac.md) [`0071c868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0071c/0071c868.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`008b7ea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7ea8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 29.81% / 新版 29.81%

CFGの説明率　旧版 3.07% / 新版 2.99%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_branch_alignment` 45件, `unresolved_call_alignment` 17件, `unresolved_store_alignment` 79件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c8800"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c8800"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c8804"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005c8800",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:005c8804",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:005c8808",
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
      "005c8bb0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "005c8bb4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "005c8bb8",
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

- 旧版 [`005c8800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c8/005c8800.md#insn-005c8800) · [`005c8804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c8/005c8800.md#insn-005c8804) · [`005c8808`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c8/005c8800.md#insn-005c8808)

~~~diff
- 005c8800 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005c8800 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005c8800 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 005c8800 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005c8800 bytes fd7bbba9
- 005c8804 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 005c8804 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 005c8804 bytes f90b00f9
- 005c8808 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 005c8808 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 005c8808 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 005c8808 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005c8808 bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8e87c277154546765561d7c8c91a2f2"></a>

### [`005c8f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c8/005c8f3c.md) → [`005c92ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c9/005c92ec.md) FUN_005c92ec

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0098546c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00985/0098546c.md) [`0098dc5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0098d/0098dc5c.md) · 呼出先 70件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md)
- 新版 呼出元 2件 [`00986418`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00986/00986418.md) [`0098ec08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0098e/0098ec08.md) · 呼出先 70件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`004412d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004412d0.md) [`00448254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448254.md) [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 60.53% / 新版 60.53%

CFGの説明率　旧版 13.34% / 新版 13.31%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 71件, `store_condition` 17件, `store_value` 2件, `unresolved_branch_alignment` 132件, `unresolved_call_alignment` 156件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 206件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c8f3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c8f3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c8f40"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005c8f3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:005c8f40",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:005c8f44",
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
      "005c92ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "005c92f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "005c92f4",
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

- 旧版 [`005c8f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c8/005c8f3c.md#insn-005c8f3c) · [`005c8f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c8/005c8f3c.md#insn-005c8f40) · [`005c8f44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c8/005c8f3c.md#insn-005c8f44)

~~~diff
- 005c8f3c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005c8f3c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005c8f3c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffa0:8"]]
- 005c8f3c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005c8f3c bytes fd7bbaa9
- 005c8f40 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 005c8f40 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 005c8f40 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 005c8f40 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005c8f40 bytes fc6f01a9
- 005c8f44 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 005c8f44 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 005c8f44 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 005c8f44 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005c8f44 bytes fa6702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41808654fbf9b66f504aef47fcd39f9d"></a>

### [`005cc1f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cc/005cc1f4.md) → [`005cc5a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cc/005cc5a4.md) FUN_005cc5a4

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005c8f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c8/005c8f3c.md) · 呼出先 12件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0047e64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e64c.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)
- 新版 呼出元 1件 [`005c92ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c9/005c92ec.md) · 呼出先 12件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00448254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448254.md) [`0047e96c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047e/0047e96c.md) [`0047f114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047f/0047f114.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 71.68% / 新版 71.68%

CFGの説明率　旧版 65.91% / 新版 69.05%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 26件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005cc1f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005cc1f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005cc1fc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005cc1f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:005cc1fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:005cc200",
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
      "005cc5a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "005cc5ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "005cc5b0",
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

- 旧版 [`005cc1f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cc/005cc1f4.md#insn-005cc1f8) · [`005cc1fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cc/005cc1f4.md#insn-005cc1fc) · [`005cc200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cc/005cc1f4.md#insn-005cc200)

~~~diff
- 005cc1f8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005cc1f8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005cc1f8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 005cc1f8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005cc1f8 bytes fd7b07a9
- 005cc1fc ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 005cc1fc ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 005cc1fc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 005cc1fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005cc1fc bytes fc6f08a9
- 005cc200 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 005cc200 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 005cc200 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:90:8"]]
- 005cc200 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005cc200 bytes fa6709a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4fa6f4c6a7262c61b0d0d57eaf5acf4c"></a>

### [`005cc554`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cc/005cc554.md) → [`005cc904`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cc/005cc904.md) FUN_005cc904

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`005fe6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe6ac.md) [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) · 呼出先 4件 [`005d8c08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d8/005d8c08.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 2件 [`005fea5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005fe/005fea5c.md) [`007cdea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007cd/007cdea8.md) · 呼出先 4件 [`005d8fb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d8/005d8fb8.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005cc57c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005cc5bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005cc92c"
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
      "unmatched:005cc568",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005cc984"
      ]
    ],
    [
      "unmatched:005cc57c",
      "DATA",
      [
        "storage",
        "00c8b880",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:005cc5b4",
      "READ",
      [
        "storage",
        "00c9b438",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005cc918",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005cc984"
      ]
    ],
    [
      "005cc92c",
      "DATA",
      [
        "storage",
        "00c8c850",
        null,
        "undefined *"
      ]
    ],
    [
      "005cc964",
      "READ",
      [
        "storage",
        "00c9c408",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005cc568`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cc/005cc554.md#insn-005cc568) · [`005cc57c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cc/005cc554.md#insn-005cc57c) · [`005cc5a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cc/005cc554.md#insn-005cc5a0)

~~~diff
- 005cc568 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 005cc568 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 005cc568 bytes 730300b4
- 005cc57c ["COPY", "tmp:0:8", ["register:4098:8"]]
- 005cc57c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 005cc57c bytes 680200f9
- 005cc5a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 005cc5a0 ["INT_ADD", "register:40f0:8", ["const:5cc5a0:8", "const:4:8"]]
- 005cc5a0 ["CALLIND", null, ["register:0:8"]]
- 005cc5a0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81e8215d146350eeca10e81931726b23"></a>

### [`005cc5e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cc/005cc5e0.md) → [`005cc990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cc/005cc990.md) FUN_005cc990

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`005db178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005db/005db178.md) [`005dc220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005dc/005dc220.md) · 呼出先 5件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b6f68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6f68.md) [`008b7a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b7a20.md) [`008c2984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c2/008c2984.md) [`008c3330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008c3/008c3330.md)
- 新版 呼出元 2件 [`005db528`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005db/005db528.md) [`005dc5d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005dc/005dc5d0.md) · 呼出先 5件 [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`008b7f14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7f14.md) [`008b89cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b8/008b89cc.md) [`008c3930`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c3/008c3930.md) [`008c42dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008c4/008c42dc.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005cc9a8",
      "incomplete_value": false,
      "site": "005cc9b4",
      "value": [
        "leaf",
        "const:1:8"
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005cc9dc",
      "incomplete_value": true,
      "site": "005cc9e4",
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
            "register:40a0:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005cc9f4",
      "incomplete_value": true,
      "site": "005cc9fc",
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
            "register:40a0:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 10,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`005cc604`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cc/005cc5e0.md#insn-005cc604) · [`005cc634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cc/005cc5e0.md#insn-005cc634) · [`005cc64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cc/005cc5e0.md#insn-005cc64c)
- 新版 [`005cc9b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cc/005cc990.md#insn-005cc9b4) · [`005cc9e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cc/005cc990.md#insn-005cc9e4) · [`005cc9fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cc/005cc990.md#insn-005cc9fc)

~~~diff
- 005cc604 ["INT_ADD", "register:40f0:8", ["const:5cc604:8", "const:4:8"]]
- 005cc604 ["CALL", null, ["callee:008b89cc:8"]]
+ 005cc9b4 ["INT_ADD", "register:40f0:8", ["const:5cc9b4:8", "const:4:8"]]
+ 005cc9b4 ["CALL", null, ["callee:008b89cc:8"]]
- 005cc604 bytes 07ad0b94
+ 005cc9b4 bytes 06b00b94
- 005cc634 ["INT_ADD", "register:40f0:8", ["const:5cc634:8", "const:4:8"]]
- 005cc634 ["CALL", null, ["callee:008b89cc:8"]]
+ 005cc9e4 ["INT_ADD", "register:40f0:8", ["const:5cc9e4:8", "const:4:8"]]
+ 005cc9e4 ["CALL", null, ["callee:008b89cc:8"]]
- 005cc634 bytes fbac0b94
+ 005cc9e4 bytes faaf0b94
- 005cc64c ["INT_ADD", "register:40f0:8", ["const:5cc64c:8", "const:4:8"]]
- 005cc64c ["CALL", null, ["callee:008b89cc:8"]]
+ 005cc9fc ["INT_ADD", "register:40f0:8", ["const:5cc9fc:8", "const:4:8"]]
+ 005cc9fc ["CALL", null, ["callee:008b89cc:8"]]
- 005cc64c bytes f5ac0b94
+ 005cc9fc bytes f4af0b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30e9c70bbd391671f8f9f657f5e57741"></a>

### [`005cc724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cc/005cc724.md) → [`005ccad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cc/005ccad4.md) FUN_005ccad4

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005cc9e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cc/005cc9e0.md) · 呼出先 9件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00664c0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00664/00664c0c.md) [`00664e80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00664/00664e80.md) [`0068778c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00687/0068778c.md) [`00687dd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00687/00687dd0.md)
- 新版 呼出元 1件 [`005ccd90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cc/005ccd90.md) · 呼出先 9件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00664fbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00664/00664fbc.md) [`00665230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00665/00665230.md) [`00687b3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00687/00687b3c.md) [`00688180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00688/00688180.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 70.86% / 新版 70.86%

CFGの説明率　旧版 21.52% / 新版 21.79%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 12件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005cc88c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005cc8a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005cc8a0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005cc770",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005ccb8c"
      ]
    ],
    [
      "unmatched:005cc7a0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c594f0"
      ]
    ],
    [
      "unmatched:005cc7b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005ccb8c"
      ]
    ]
  ],
  "added": [
    [
      "005ccb20",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005ccb8c"
      ]
    ],
    [
      "005ccb50",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c594f0"
      ]
    ],
    [
      "005ccb64",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005ccb8c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005cc770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cc/005cc724.md#insn-005cc770) · [`005cc7ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cc/005cc724.md#insn-005cc7ac) · [`005cc7b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cc/005cc724.md#insn-005cc7b4)

~~~diff
- 005cc770 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 005cc770 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 005cc770 bytes 680300b4
- 005cc7ac ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 005cc7ac ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 005cc7ac ["COPY", "tmp:0:8", ["register:4000:8"]]
- 005cc7ac ["COPY", "register:4048:8", ["tmp:0:8"]]
- 005cc7ac bytes a902809a
- 005cc7b4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 005cc7b4 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 005cc7b4 bytes 41010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1cd77e39e8fe546be88611847d01f77d"></a>

### [`005cc9e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cc/005cc9e0.md) → [`005ccd90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cc/005ccd90.md) FUN_005ccd90

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 6件 [`006a7064`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a7/006a7064.md) [`00922e1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00922/00922e1c.md) [`009617f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00961/009617f4.md) [`00962f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00962/00962f70.md) [`0098dc5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0098d/0098dc5c.md) · 呼出先 8件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`005cc724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cc/005cc724.md) [`005ccb48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cc/005ccb48.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 6件 [`006a7414`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006a7/006a7414.md) [`00923dc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00923/00923dc8.md) [`009627a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00962/009627a0.md) [`00963f1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00963/00963f1c.md) [`0098ec08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0098e/0098ec08.md) · 呼出先 8件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`005ccad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cc/005ccad4.md) [`005ccef8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cc/005ccef8.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 27.59% / 新版 28.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_condition` 1件, `unresolved_branch_alignment` 4件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005cc9e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005cc9e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005cc9e8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005cc9e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:005cc9e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:005cca28",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005ccde4"
      ]
    ]
  ],
  "added": [
    [
      "005ccd94",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "005ccd98",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "005ccdd8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005ccde4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005cc9e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cc/005cc9e0.md#insn-005cc9e4) · [`005cc9e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cc/005cc9e0.md#insn-005cc9e8) · [`005cca28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cc/005cc9e0.md#insn-005cca28)

~~~diff
- 005cc9e4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005cc9e4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005cc9e4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 005cc9e4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005cc9e4 bytes fd7b01a9
- 005cc9e8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 005cc9e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d8:8"]]
- 005cc9e8 bytes fb1300f9
- 005cca28 ["CBRANCH", null, ["local:b4:8", "register:102:1"]]
- 005cca28 bytes 62000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d2d7b60fbea602128b8e25d7942f72f"></a>

### [`005ccb48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cc/005ccb48.md) → [`005ccef8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cc/005ccef8.md) FUN_005ccef8

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005cc9e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cc/005cc9e0.md) · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`005dc340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005dc/005dc340.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 1件 [`005ccd90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cc/005ccd90.md) · 呼出先 6件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`005dc6f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005dc/005dc6f0.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 88.43% / 新版 88.43%

CFGの説明率　旧版 54.05% / 新版 48.78%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 4件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ccb58"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ccb58"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ccb5c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005ccb58",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:005ccb5c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:005ccb78",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005ccf54"
      ]
    ]
  ],
  "added": [
    [
      "005ccf08",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005ccf0c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005ccf28",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005ccf54"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ccb58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cc/005ccb48.md#insn-005ccb58) · [`005ccb5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cc/005ccb48.md#insn-005ccb5c) · [`005ccb78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cc/005ccb48.md#insn-005ccb78)

~~~diff
- 005ccb58 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 005ccb58 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 005ccb58 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 005ccb58 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005ccb58 bytes f65704a9
- 005ccb5c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 005ccb5c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 005ccb5c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 005ccb5c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005ccb5c bytes f44f05a9
- 005ccb78 ["CBRANCH", null, ["local:b4:8", "register:102:1"]]
- 005ccb78 bytes 62010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-621e6465414b00fa681931c6618a5d8e"></a>

### [`005ccd44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cc/005ccd44.md) → [`005cd0f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cd/005cd0f4.md) FUN_005cd0f4

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 7件 [`00678920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00678/00678920.md) [`006ac970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ac/006ac970.md) [`006bbcf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bb/006bbcf0.md) [`00914e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00914/00914e84.md) [`0092491c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00924/0092491c.md) · 呼出先 16件 [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md)
- 新版 呼出元 7件 [`00678cd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00678/00678cd0.md) [`006acd20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006ac/006acd20.md) [`006bc0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006bc/006bc0a0.md) [`00915e30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00915/00915e30.md) [`009258c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00925/009258c8.md) · 呼出先 16件 [`00448254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00448/00448254.md) [`0046d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md) [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 84.39% / 新版 84.39%

CFGの説明率　旧版 78.00% / 新版 76.47%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ccdc8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ccdd0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ccdd4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005ccd78",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005cd2fc"
      ]
    ],
    [
      "unmatched:005ccd98",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "unmatched:005ccdbc",
      "READ",
      [
        "storage",
        "002ba42b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005cd128",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005cd2fc"
      ]
    ],
    [
      "005cd148",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "005cd16c",
      "READ",
      [
        "storage",
        "002ba509",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ccd78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cc/005ccd44.md#insn-005ccd78) · [`005ccd98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cc/005ccd44.md#insn-005ccd98) · [`005ccdc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cc/005ccd44.md#insn-005ccdc8)

~~~diff
- 005ccd78 ["CBRANCH", null, ["local:b20:8", "register:101:1"]]
- 005ccd78 bytes a00e0054
- 005ccd98 ["INT_ADD", "register:40f0:8", ["const:5ccd98:8", "const:4:8"]]
- 005ccd98 ["CALL", null, ["ram:47ad34:8"]]
- 005ccd98 bytes e7b7fa97
- 005ccdc8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:50:8"]]
- 005ccdc8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 005ccdc8 bytes e02b00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a5517dc1372aa2a5571c0946a117e77"></a>

### [`005cd130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cd130.md) → [`005cd4e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cd/005cd4e0.md) FUN_005cd4e0

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 53件 [`005ccd44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cc/005ccd44.md) [`005db4c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005db/005db4c8.md) [`00606b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00606/00606b24.md) [`0060a8e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0060a/0060a8e0.md) [`0060e104`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0060e/0060e104.md) · 呼出先 14件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00493e08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493e08.md) [`005cd6a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cd6a0.md) [`005d5ca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d5/005d5ca0.md)
- 新版 呼出元 53件 [`005cd0f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cd/005cd0f4.md) [`005db878`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005db/005db878.md) [`00606ed4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00606/00606ed4.md) [`0060ac90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0060a/0060ac90.md) [`0060e4b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0060e/0060e4b4.md) · 呼出先 14件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00494128`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494128.md) [`005cda50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cd/005cda50.md) [`005d6050`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d6/005d6050.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 75.43% / 新版 75.43%

CFGの説明率　旧版 20.55% / 新版 21.13%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_branch_alignment` 14件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005cd150"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005cd15c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005cd178"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005cd150",
      "WRITE",
      [
        "storage",
        "Stack[-0x198]",
        null,
        null
      ]
    ],
    [
      "unmatched:005cd15c",
      "WRITE",
      [
        "storage",
        "Stack[-0x1b0]",
        null,
        null
      ]
    ],
    [
      "unmatched:005cd168",
      "PARAM",
      [
        "storage",
        "002a7a17",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005cd500",
      "WRITE",
      [
        "storage",
        "Stack[-0x198]",
        null,
        null
      ]
    ],
    [
      "005cd50c",
      "WRITE",
      [
        "storage",
        "Stack[-0x1b0]",
        null,
        null
      ]
    ],
    [
      "005cd518",
      "PARAM",
      [
        "storage",
        "002a7b6f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005cd150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cd130.md#insn-005cd150) · [`005cd15c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cd130.md#insn-005cd15c) · [`005cd178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cd130.md#insn-005cd178)

~~~diff
- 005cd150 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 005cd150 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:8"]]
- 005cd150 bytes e10f00f9
- 005cd15c ["COPY", "tmp:0:8", ["register:8:8"]]
- 005cd15c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 005cd15c bytes e80300f9
- 005cd178 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 005cd178 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff0:8"]]
- 005cd178 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 005cd178 bytes a8031ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10a2d74db293e7facf3386feb2e1d16d"></a>

### [`005cd6a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cd6a0.md) → [`005cda50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cd/005cda50.md) FUN_005cda50

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`005cd130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cd130.md) [`0088c8c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c8c8.md) · 呼出先 8件 [`005cd7a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cd7a8.md) [`005cd7f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cd7f8.md) [`005cdb3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cdb3c.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md)
- 新版 呼出元 2件 [`005cd4e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cd/005cd4e0.md) [`0088d874`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088d/0088d874.md) · 呼出先 8件 [`005cdb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cd/005cdb58.md) [`005cdba8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cd/005cdba8.md) [`005cdeec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cd/005cdeec.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 84.44% / 新版 84.44%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005cd6a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005cd6a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005cd6a4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005cd6a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:005cd6a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:005cd6a8",
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
      "005cda50",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "005cda54",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005cda58",
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

- 旧版 [`005cd6a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cd6a0.md#insn-005cd6a0) · [`005cd6a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cd6a0.md#insn-005cd6a4) · [`005cd6a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cd6a0.md#insn-005cd6a8)

~~~diff
- 005cd6a0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005cd6a0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005cd6a0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 005cd6a0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005cd6a0 bytes fd7bbda9
- 005cd6a4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 005cd6a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 005cd6a4 bytes f50b00f9
- 005cd6a8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 005cd6a8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 005cd6a8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 005cd6a8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005cd6a8 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e6f8ef004f57513fb81cc8a3704d91b"></a>

### [`005cd758`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cd758.md) → [`005cdb08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cd/005cdb08.md) FUN_005cdb08

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005ce640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005ce640.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md)
- 新版 呼出元 1件 [`005ce9f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ce/005ce9f0.md) · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c59330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59330.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "005cd774",
      "incomplete_value": false,
      "site": "005cd778",
      "value": [
        "leaf",
        "const:ffffffffffffffff:8"
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
      "definition_site": "005cd770",
      "incomplete_value": true,
      "site": "005cd778",
      "value": [
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
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "005cd78c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005cd78c",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "005cdb3c",
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

- 旧版 [`005cd778`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cd758.md#insn-005cd778) · [`005cd78c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cd758.md#insn-005cd78c)
- 新版 [`005cdb28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cd/005cdb08.md#insn-005cdb28) · [`005cdb3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cd/005cdb08.md#insn-005cdb3c)

~~~diff
- 005cd778 ["INT_ADD", "register:40f0:8", ["const:5cd778:8", "const:4:8"]]
- 005cd778 ["CALL", null, ["callee:00c54d90:8"]]
+ 005cdb28 ["INT_ADD", "register:40f0:8", ["const:5cdb28:8", "const:4:8"]]
+ 005cdb28 ["CALL", null, ["callee:00c54d90:8"]]
- 005cd778 bytes 8a191a94
+ 005cdb28 bytes 9a1c1a94
- 005cd78c ["COPY", "register:0:8", ["register:4040:8"]]
- 005cd78c ["INT_ADD", "register:40f0:8", ["const:5cd78c:8", "const:4:8"]]
- 005cd78c ["CALLIND", null, ["register:0:8"]]
- 005cd78c bytes 00013fd6
+ 005cdb3c ["COPY", "register:0:8", ["register:4040:8"]]
+ 005cdb3c ["INT_ADD", "register:40f0:8", ["const:5cdb3c:8", "const:4:8"]]
+ 005cdb3c ["CALLIND", null, ["register:0:8"]]
+ 005cdb3c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a82c2814eda578f6006a1ce61dc6fe0"></a>

### [`005cd7a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cd7a8.md) → [`005cdb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cd/005cdb58.md) FUN_005cdb58

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`005cd6a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cd6a0.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 1件 [`005cda50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cd/005cda50.md) · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 20.00% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005cd7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cd7a8.md#insn-005cd7b8) · [`005cd7c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cd7a8.md#insn-005cd7c4) · [`005cd7c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cd7a8.md#insn-005cd7c8)
- 新版 [`005cdb68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cd/005cdb58.md#insn-005cdb68) · [`005cdb74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cd/005cdb58.md#insn-005cdb74) · [`005cdb78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cd/005cdb58.md#insn-005cdb78)

~~~diff
- 005cd7b8 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 005cd7b8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 005cdb68 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
+ 005cdb68 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 005cd7b8 bytes b30000b4
+ 005cdb68 bytes b30000b4
- 005cd7c4 ["INT_ADD", "register:40f0:8", ["const:5cd7c4:8", "const:4:8"]]
- 005cd7c4 ["CALL", null, ["callee:00c54d90:8"]]
+ 005cdb74 ["INT_ADD", "register:40f0:8", ["const:5cdb74:8", "const:4:8"]]
+ 005cdb74 ["CALL", null, ["callee:00c54d90:8"]]
- 005cd7c4 bytes 77191a94
+ 005cdb74 bytes 871c1a94
- 005cd7c8 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 005cd7c8 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 005cdb78 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 005cdb78 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 005cd7c8 bytes 800000b4
+ 005cdb78 bytes 800000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb51ae821f95c7c8cdd150e21e93a1b7"></a>

### [`005cd7f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cd7f8.md) → [`005cdba8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cd/005cdba8.md) FUN_005cdba8

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`005cd6a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cd6a0.md) [`005ce640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005ce640.md) · 呼出先 11件 [`005cdd40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cdd40.md) [`005cdecc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cdecc.md) [`005ce040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005ce040.md) [`005ce1f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005ce1f4.md) [`005ce3a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005ce3a8.md)
- 新版 呼出元 2件 [`005cda50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cd/005cda50.md) [`005ce9f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ce/005ce9f0.md) · 呼出先 11件 [`005ce0f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ce/005ce0f0.md) [`005ce27c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ce/005ce27c.md) [`005ce3f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ce/005ce3f0.md) [`005ce5a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ce/005ce5a4.md) [`005ce758`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ce/005ce758.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, store_value, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 82.21% / 新版 82.21%

CFGの説明率　旧版 24.00% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `return_value_candidate` 1件, `store_value` 1件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 11件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005cd808"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005cd808"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005cd80c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005cd808",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:005cd80c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:005cd830",
      "READ",
      [
        "storage",
        "00c9b450",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005cdbb8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005cdbbc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005cdbe0",
      "READ",
      [
        "storage",
        "00c9c420",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005cd808`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cd7f8.md#insn-005cd808) · [`005cd80c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cd7f8.md#insn-005cd80c) · [`005cd838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cd7f8.md#insn-005cd838)

~~~diff
- 005cd808 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 005cd808 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 005cd808 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 005cd808 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005cd808 bytes f65704a9
- 005cd80c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 005cd80c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 005cd80c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 005cd80c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005cd80c bytes f44f05a9
- 005cd838 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 005cd838 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c0:8"]]
- 005cd838 bytes 180000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-feb6cde9bc3c76ba9722e6f9f1d413d3"></a>

### [`005cdb3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cdb3c.md) → [`005cdeec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cd/005cdeec.md) FUN_005cdeec

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005cd6a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cd6a0.md) · 呼出先 4件 [`00c37324`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37324.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c5a880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a880.md)
- 新版 呼出元 1件 [`005cda50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cd/005cda50.md) · 呼出先 4件 [`00c38318`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38318.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md) [`00c5b850`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b850.md)

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, constant, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 78.57% / 新版 78.57%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "005cdb54",
      "incomplete_value": false,
      "site": "005cdb58",
      "value": [
        "leaf",
        "const:11:8"
      ]
    },
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "005cdb70"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "005cdf20"
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
      "unmatched:005cdb68",
      "READ",
      [
        "storage",
        "00c9b480",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:005cdb68",
      "PARAM",
      [
        "storage",
        "00c96688",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "unmatched:005cdb6c",
      "READ",
      [
        "storage",
        "00c9b488",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005cdf18",
      "READ",
      [
        "storage",
        "00c9c450",
        null,
        "pointer"
      ]
    ],
    [
      "005cdf18",
      "PARAM",
      [
        "storage",
        "00c97658",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005cdf1c",
      "READ",
      [
        "storage",
        "00c9c458",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005cdb58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cdb3c.md#insn-005cdb58) · [`005cdb70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cdb3c.md#insn-005cdb70)
- 新版 [`005cdf08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cd/005cdeec.md#insn-005cdf08) · [`005cdf20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cd/005cdeec.md#insn-005cdf20)

~~~diff
- 005cdb58 ["INT_ADD", "register:40f0:8", ["const:5cdb58:8", "const:4:8"]]
- 005cdb58 ["CALL", null, ["callee:00c5b850:8"]]
+ 005cdf08 ["INT_ADD", "register:40f0:8", ["const:5cdf08:8", "const:4:8"]]
+ 005cdf08 ["CALL", null, ["callee:00c5b850:8"]]
- 005cdb58 bytes 4a331a94
+ 005cdf08 bytes 52361a94
- 005cdb70 ["INT_ADD", "register:40f0:8", ["const:5cdb70:8", "const:4:8"]]
- 005cdb70 ["CALL", null, ["callee:00c58fb0:8"]]
- 005cdb70 bytes 1c291a94
+ 005cdf20 ["INT_ADD", "register:40f0:8", ["const:5cdf20:8", "const:4:8"]]
+ 005cdf20 ["CALL", null, ["callee:00c58fb0:8"]]
+ 005cdf20 bytes 242c1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6198c320d471e69381ee2b1befc7a0d"></a>

### [`005cdb88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cdb88.md) → [`005cdf38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cd/005cdf38.md) FUN_005cdf38

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005ce9a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005ce9a4.md) · 呼出先 2件 [`005ce5ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005ce5ac.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`005ced54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ce/005ced54.md) · 呼出先 2件 [`005ce95c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ce/005ce95c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 76.36% / 新版 76.36%

CFGの説明率　旧版 10.00% / 新版 10.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `return_value_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 20件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005cdb88"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005cdb88"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005cdb8c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005cdb88",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:005cdb8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:005cdb90",
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
      "005cdf38",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "005cdf3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "005cdf40",
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

- 旧版 [`005cdb88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cdb88.md#insn-005cdb88) · [`005cdb8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cdb88.md#insn-005cdb8c) · [`005cdb90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cdb88.md#insn-005cdb90)

~~~diff
- 005cdb88 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005cdb88 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005cdb88 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffa0:8"]]
- 005cdb88 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005cdb88 bytes fd7bbaa9
- 005cdb8c ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 005cdb8c ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 005cdb8c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 005cdb8c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005cdb8c bytes fc6f01a9
- 005cdb90 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 005cdb90 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 005cdb90 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 005cdb90 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005cdb90 bytes fa6702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f394cde3958248b4c2f590f8d9f62bf"></a>

### [`005cdd40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cdd40.md) → [`005ce0f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ce/005ce0f0.md) FUN_005ce0f0

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`005cd7f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cd7f8.md) [`005ce040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005ce040.md) · 呼出先 4件 [`005d51f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d5/005d51f0.md) [`005d523c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d5/005d523c.md) [`005d5448`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d5/005d5448.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 2件 [`005cdba8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cd/005cdba8.md) [`005ce3f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ce/005ce3f0.md) · 呼出先 4件 [`005d55a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d5/005d55a0.md) [`005d55ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d5/005d55ec.md) [`005d57f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d5/005d57f8.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 76.77% / 新版 76.77%

CFGの説明率　旧版 18.75% / 新版 21.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 12件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005cdd40"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005cdd40"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005cdd44"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005cdd40",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:005cdd44",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:005cdd48",
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
      "005ce0f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "005ce0f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "005ce0f8",
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

- 旧版 [`005cdd40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cdd40.md#insn-005cdd40) · [`005cdd44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cdd40.md#insn-005cdd44) · [`005cdd48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cdd40.md#insn-005cdd48)

~~~diff
- 005cdd40 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005cdd40 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005cdd40 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 005cdd40 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005cdd40 bytes fd7bbca9
- 005cdd44 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 005cdd44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 005cdd44 bytes f70b00f9
- 005cdd48 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 005cdd48 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 005cdd48 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 005cdd48 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005cdd48 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7955ccc68ac49f297697aa06d5956744"></a>

### [`005cdecc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cdecc.md) → [`005ce27c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ce/005ce27c.md) FUN_005ce27c

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`005cd7f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cd7f8.md) [`005ce1f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005ce1f4.md) [`005d58ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d5/005d58ac.md) · 呼出先 3件 [`005d51f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d5/005d51f0.md) [`005d58ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d5/005d58ac.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 3件 [`005cdba8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cd/005cdba8.md) [`005ce5a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ce/005ce5a4.md) [`005d5c5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d5/005d5c5c.md) · 呼出先 3件 [`005d55a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d5/005d55a0.md) [`005d5c5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d5/005d5c5c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 83.87% / 新版 83.87%

CFGの説明率　旧版 18.75% / 新版 19.35%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005cdfb8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005cdfb8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005cdfd8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005cdf3c",
      "READ",
      [
        "storage",
        "00c9b468",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:005cdf40",
      "READ",
      [
        "storage",
        "00c9b458",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:005cdf44",
      "READ",
      [
        "storage",
        "00c9b470",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005ce2cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005ce2b4"
      ]
    ],
    [
      "005ce2ec",
      "READ",
      [
        "storage",
        "00c9c438",
        null,
        "pointer"
      ]
    ],
    [
      "005ce2f0",
      "READ",
      [
        "storage",
        "00c9c428",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005cdf90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cdecc.md#insn-005cdf90) · [`005cdf98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cdecc.md#insn-005cdf98) · [`005cdfa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cdecc.md#insn-005cdfa8)
- 新版 [`005ce2c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ce/005ce27c.md#insn-005ce2c4) · [`005ce358`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ce/005ce27c.md#insn-005ce358)

~~~diff
- 005cdf90 ["INT_ADD", "register:40f0:8", ["const:5cdf90:8", "const:4:8"]]
- 005cdf90 ["CALL", null, ["callee:005d5c5c:8"]]
+ 005ce2c4 ["INT_ADD", "register:40f0:8", ["const:5ce2c4:8", "const:4:8"]]
+ 005ce2c4 ["CALL", null, ["callee:005d5c5c:8"]]
- 005cdf90 bytes 471e0094
+ 005ce2c4 bytes 661e0094
- 005cdf98 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 005cdf98 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 005cdf98 bytes 41ffff54
- 005cdfa8 ["INT_ADD", "register:40f0:8", ["const:5cdfa8:8", "const:4:8"]]
- 005cdfa8 ["CALL", null, ["callee:00c58f30:8"]]
+ 005ce358 ["INT_ADD", "register:40f0:8", ["const:5ce358:8", "const:4:8"]]
+ 005ce358 ["CALL", null, ["callee:00c58f30:8"]]
- 005cdfa8 bytes ee271a94
+ 005ce358 bytes f62a1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bdd3667938e830b8eaf03c53a3219047"></a>

### [`005ce040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005ce040.md) → [`005ce3f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ce/005ce3f0.md) FUN_005ce3f0

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005cd7f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cd7f8.md) · 呼出先 3件 [`005cdd40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cdd40.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580a0.md)
- 新版 呼出元 1件 [`005cdba8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cd/005cdba8.md) · 呼出先 3件 [`005ce0f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ce/005ce0f0.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c59070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59070.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 87.16% / 新版 87.16%

CFGの説明率　旧版 8.70% / 新版 8.70%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ce0bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ce110"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ce110"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005ce088",
      "READ",
      [
        "storage",
        "00c9b458",
        null,
        "pointer"
      ]
    ],
    [
      "005ce468",
      "DATA",
      [
        "storage",
        "00c70c10",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "unmatched:005ce0ec",
      "READ",
      [
        "storage",
        "00c9b468",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005ce438",
      "READ",
      [
        "storage",
        "00c9c428",
        null,
        "pointer"
      ]
    ],
    [
      "005ce468",
      "DATA",
      [
        "storage",
        "00c71be0",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005ce49c",
      "READ",
      [
        "storage",
        "00c9c438",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ce078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005ce040.md#insn-005ce078) · [`005ce0bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005ce040.md#insn-005ce0bc) · [`005ce110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005ce040.md#insn-005ce110)
- 新版 [`005ce428`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ce/005ce3f0.md#insn-005ce428)

~~~diff
- 005ce078 ["INT_ADD", "register:40f0:8", ["const:5ce078:8", "const:4:8"]]
- 005ce078 ["CALL", null, ["callee:00c59070:8"]]
+ 005ce428 ["INT_ADD", "register:40f0:8", ["const:5ce428:8", "const:4:8"]]
+ 005ce428 ["CALL", null, ["callee:00c59070:8"]]
- 005ce078 bytes 0a281a94
+ 005ce428 bytes 122b1a94
- 005ce0bc ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8:8"]]
- 005ce0bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 005ce0bc bytes 080400f9
- 005ce110 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 005ce110 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 005ce110 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 005ce110 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005ce110 bytes 1a2000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-187edb960100c9584c8c18e8a74b591b"></a>

### [`005ce1f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005ce1f4.md) → [`005ce5a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ce/005ce5a4.md) FUN_005ce5a4

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005cd7f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cd7f8.md) · 呼出先 3件 [`005cdecc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cdecc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580a0.md)
- 新版 呼出元 1件 [`005cdba8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cd/005cdba8.md) · 呼出先 3件 [`005ce27c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ce/005ce27c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c59070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59070.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 81.65% / 新版 81.65%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `return_value_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 16件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ce1f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ce1f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ce1f8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005ce1f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:005ce1f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:005ce1fc",
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
      "005ce5a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "005ce5a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "005ce5ac",
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

- 旧版 [`005ce1f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005ce1f4.md#insn-005ce1f4) · [`005ce1f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005ce1f4.md#insn-005ce1f8) · [`005ce1fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005ce1f4.md#insn-005ce1fc)

~~~diff
- 005ce1f4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005ce1f4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005ce1f4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffa0:8"]]
- 005ce1f4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005ce1f4 bytes fd7bbaa9
- 005ce1f8 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 005ce1f8 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 005ce1f8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 005ce1f8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005ce1f8 bytes fc6f01a9
- 005ce1fc ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 005ce1fc ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 005ce1fc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 005ce1fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005ce1fc bytes fa6702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48fed1740b4b57d7c68e8dc7d6b9c06a"></a>

### [`005ce3a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005ce3a8.md) → [`005ce758`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ce/005ce758.md) FUN_005ce758

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005cd7f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cd7f8.md) · 呼出先 4件 [`00c37324`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37324.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c5a880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a880.md)
- 新版 呼出元 1件 [`005cdba8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cd/005cdba8.md) · 呼出先 4件 [`00c38318`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38318.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md) [`00c5b850`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b850.md)

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 78.57% / 新版 78.57%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "005ce3b4",
      "incomplete_value": false,
      "site": "005ce3b8",
      "value": [
        "leaf",
        "const:18:8"
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
      "site": "005ce3dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "005ce78c"
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
      "unmatched:005ce3d4",
      "READ",
      [
        "storage",
        "00c9b480",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:005ce3d4",
      "PARAM",
      [
        "storage",
        "00c96688",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "unmatched:005ce3d8",
      "READ",
      [
        "storage",
        "00c9b488",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005ce784",
      "READ",
      [
        "storage",
        "00c9c450",
        null,
        "pointer"
      ]
    ],
    [
      "005ce784",
      "PARAM",
      [
        "storage",
        "00c97658",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005ce788",
      "READ",
      [
        "storage",
        "00c9c458",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ce3b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005ce3a8.md#insn-005ce3b8) · [`005ce3dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005ce3a8.md#insn-005ce3dc)
- 新版 [`005ce768`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ce/005ce758.md#insn-005ce768) · [`005ce78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ce/005ce758.md#insn-005ce78c)

~~~diff
- 005ce3b8 ["INT_ADD", "register:40f0:8", ["const:5ce3b8:8", "const:4:8"]]
- 005ce3b8 ["CALL", null, ["callee:00c58f90:8"]]
+ 005ce768 ["INT_ADD", "register:40f0:8", ["const:5ce768:8", "const:4:8"]]
+ 005ce768 ["CALL", null, ["callee:00c58f90:8"]]
- 005ce3b8 bytes 02271a94
+ 005ce768 bytes 0a2a1a94
- 005ce3dc ["INT_ADD", "register:40f0:8", ["const:5ce3dc:8", "const:4:8"]]
- 005ce3dc ["CALL", null, ["callee:00c58fb0:8"]]
- 005ce3dc bytes 01271a94
+ 005ce78c ["INT_ADD", "register:40f0:8", ["const:5ce78c:8", "const:4:8"]]
+ 005ce78c ["CALL", null, ["callee:00c58fb0:8"]]
+ 005ce78c bytes 092a1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69241d123aaec03d95a45ebee203e093"></a>

### [`005ce40c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005ce40c.md) → [`005ce7bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ce/005ce7bc.md) FUN_005ce7bc

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f40.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005ce41c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005ce40c.md#insn-005ce41c)
- 新版 [`005ce7cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ce/005ce7bc.md#insn-005ce7cc)

~~~diff
- 005ce41c ["INT_ADD", "register:40f0:8", ["const:5ce41c:8", "const:4:8"]]
- 005ce41c ["CALL", null, ["callee:00c58f40:8"]]
+ 005ce7cc ["INT_ADD", "register:40f0:8", ["const:5ce7cc:8", "const:4:8"]]
+ 005ce7cc ["CALL", null, ["callee:00c58f40:8"]]
- 005ce41c bytes d5261a94
+ 005ce7cc bytes dd291a94
~~~


<a id="compare-e76633e931830d34cc93432085201dcc"></a>

### [`005ce4c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005ce4c4.md) → [`005ce874`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ce/005ce874.md) FUN_005ce874

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 33.33% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005ce880",
      "incomplete_value": true,
      "site": "005ce884",
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
      "definition_site": "005ce4d0",
      "incomplete_value": true,
      "site": "005ce4d4",
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
      "site": "005ce4f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "005ce8a8"
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
      "005ce878",
      "READ",
      [
        "storage",
        "00c9b478",
        null,
        "pointer"
      ]
    ],
    [
      "005ce884",
      "DATA",
      [
        "storage",
        "00c70c88",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "unmatched:005ce4f8",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "005ce878",
      "READ",
      [
        "storage",
        "00c9c448",
        null,
        "pointer"
      ]
    ],
    [
      "005ce884",
      "DATA",
      [
        "storage",
        "00c71c58",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005ce8a8",
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

- 旧版 [`005ce4f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005ce4c4.md#insn-005ce4f8) · [`005ce4c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005ce4c4.md#insn-005ce4c4)
- 新版 [`005ce8a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ce/005ce874.md#insn-005ce8a8) · [`005ce874`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ce/005ce874.md#insn-005ce874)

~~~diff
- 005ce4f8 ["COPY", "register:0:8", ["register:4048:8"]]
- 005ce4f8 ["INT_ADD", "register:40f0:8", ["const:5ce4f8:8", "const:4:8"]]
- 005ce4f8 ["CALLIND", null, ["register:0:8"]]
- 005ce4f8 bytes 20013fd6
+ 005ce8a8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005ce8a8 ["INT_ADD", "register:40f0:8", ["const:5ce8a8:8", "const:4:8"]]
+ 005ce8a8 ["CALLIND", null, ["register:0:8"]]
+ 005ce8a8 bytes 20013fd6
- 005ce4c4 ["COPY", "register:4048:8", ["const:c9b000:8"]]
+ 005ce874 ["COPY", "register:4048:8", ["const:c9c000:8"]]
- 005ce4c4 bytes 693600b0
+ 005ce874 bytes 693600d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cfc11eee6d53415fe7b3b8c69d01166c"></a>

### [`005ce50c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005ce50c.md) → [`005ce8bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ce/005ce8bc.md) FUN_005ce8bc

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005cd7f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cd7f8.md) · 呼出先 3件 [`005ce640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005ce640.md) [`005ce9a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005ce9a4.md) [`005cec5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005cec5c.md)
- 新版 呼出元 1件 [`005cdba8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cd/005cdba8.md) · 呼出先 3件 [`005ce9f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ce/005ce9f0.md) [`005ced54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ce/005ced54.md) [`005cf00c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cf/005cf00c.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005ce554"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "005ce904"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005ce8e8",
      "incomplete_value": true,
      "site": "005ce8f8",
      "value": [
        "live",
        "register:40a0:8"
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
      "unmatched:005ce554",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005ce944"
      ]
    ]
  ],
  "added": [
    [
      "005ce904",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005ce944"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ce548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005ce50c.md#insn-005ce548) · [`005ce554`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005ce50c.md#insn-005ce554) · [`005ce588`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005ce50c.md#insn-005ce588)
- 新版 [`005ce8f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ce/005ce8bc.md#insn-005ce8f8) · [`005ce938`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ce/005ce8bc.md#insn-005ce938)

~~~diff
- 005ce548 ["INT_ADD", "register:40f0:8", ["const:5ce548:8", "const:4:8"]]
- 005ce548 ["CALL", null, ["callee:005cf00c:8"]]
+ 005ce8f8 ["INT_ADD", "register:40f0:8", ["const:5ce8f8:8", "const:4:8"]]
+ 005ce8f8 ["CALL", null, ["callee:005cf00c:8"]]
- 005ce548 bytes c5010094
+ 005ce8f8 bytes c5010094
- 005ce554 ["CBRANCH", null, ["local:b9:8", "register:101:1"]]
- 005ce554 bytes 00020054
- 005ce588 ["INT_ADD", "register:40f0:8", ["const:5ce588:8", "const:4:8"]]
- 005ce588 ["CALL", null, ["callee:005ced54:8"]]
+ 005ce938 ["INT_ADD", "register:40f0:8", ["const:5ce938:8", "const:4:8"]]
+ 005ce938 ["CALL", null, ["callee:005ced54:8"]]
- 005ce588 bytes 07010094
+ 005ce938 bytes 07010094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ac54765fa87cb97f9d1463627d390e6"></a>

### [`005ce640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005ce640.md) → [`005ce9f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ce/005ce9f0.md) FUN_005ce9f0

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`005ce50c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005ce50c.md) [`005ce5ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005ce5ac.md) · 呼出先 8件 [`005cd758`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cd758.md) [`005cd7f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cd7f8.md) [`005cefbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005cefbc.md) [`005cf028`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cf028.md) [`005cf0dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cf0dc.md)
- 新版 呼出元 2件 [`005ce8bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ce/005ce8bc.md) [`005ce95c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ce/005ce95c.md) · 呼出先 8件 [`005cdb08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cd/005cdb08.md) [`005cdba8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cd/005cdba8.md) [`005cf36c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cf/005cf36c.md) [`005cf3d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cf/005cf3d8.md) [`005cf48c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cf/005cf48c.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 63.90% / 新版 63.90%

CFGの説明率　旧版 12.50% / 新版 12.31%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 9件, `unresolved_store_alignment` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ce664"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ce6dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ce71c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005ce664",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:005ce6d0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "005cf36c"
      ]
    ],
    [
      "unmatched:005ce6dc",
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
      "005cea14",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "005cea80",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "005cf36c"
      ]
    ],
    [
      "005cea8c",
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

- 旧版 [`005ce664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005ce640.md#insn-005ce664) · [`005ce6dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005ce640.md#insn-005ce6dc) · [`005ce71c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005ce640.md#insn-005ce71c)

~~~diff
- 005ce664 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 005ce664 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 005ce664 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 005ce664 bytes a8831ff8
- 005ce6dc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 005ce6dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 005ce6dc bytes e82300b9
- 005ce71c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:1c:8"]]
- 005ce71c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 005ce71c bytes 881e00b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a23ebb4c3c0df3245035205bc973cc8"></a>

### [`005ce9a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005ce9a4.md) → [`005ced54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ce/005ced54.md) FUN_005ced54

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`005ce50c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005ce50c.md) [`005ce5ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005ce5ac.md) · 呼出先 10件 [`005cdb88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cdb88.md) [`005cf0dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cf0dc.md) [`005d0690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d0/005d0690.md) [`005d07e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d0/005d07e4.md) [`005d0830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d0/005d0830.md)
- 新版 呼出元 2件 [`005ce8bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ce/005ce8bc.md) [`005ce95c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ce/005ce95c.md) · 呼出先 10件 [`005cdf38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cd/005cdf38.md) [`005cf48c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cf/005cf48c.md) [`005d0a40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d0a40.md) [`005d0b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d0b94.md) [`005d0be0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d0be0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 91.38% / 新版 91.38%

CFGの説明率　旧版 68.25% / 新版 70.49%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_value` 1件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005cea00"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005cea04"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005cea0c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005ce9bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005cedd0"
      ]
    ],
    [
      "unmatched:005ce9f4",
      "READ",
      [
        "storage",
        "00c9b4b0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:005cea0c",
      "DATA",
      [
        "storage",
        "00c70dd8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "005ced6c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005cedd0"
      ]
    ],
    [
      "005ceda4",
      "READ",
      [
        "storage",
        "00c9c480",
        null,
        "pointer"
      ]
    ],
    [
      "005cedbc",
      "DATA",
      [
        "storage",
        "00c71da8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ce9bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005ce9a4.md#insn-005ce9bc) · [`005cea00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005ce9a4.md#insn-005cea00) · [`005cea04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005ce9a4.md#insn-005cea04)

~~~diff
- 005ce9bc ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
- 005ce9bc bytes 20030054
- 005cea00 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8:8"]]
- 005cea00 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 005cea00 bytes 0a0400f9
- 005cea04 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:8:8"]]
- 005cea04 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 005cea04 bytes 000500f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc0d3c4c6716d26e7b71c463860c1b17"></a>

### [`005cefbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005cefbc.md) → [`005cf36c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cf/005cf36c.md) FUN_005cf36c

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005ce640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005ce640.md) · 呼出先 2件 [`00c58350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58350.md) [`00c5a870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a870.md)
- 新版 呼出元 1件 [`005ce9f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ce/005ce9f0.md) · 呼出先 2件 [`00c59320`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59320.md) [`00c5b840`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b840.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005cf388",
      "incomplete_value": true,
      "site": "005cf38c",
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
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:cd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005cefd8",
      "incomplete_value": true,
      "site": "005cefdc",
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
                "const:c9a000:8"
              ],
              [
                "leaf",
                "const:d00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005cf39c",
      "incomplete_value": true,
      "site": "005cf3a0",
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
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:418:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005cefec",
      "incomplete_value": true,
      "site": "005ceff0",
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
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:448:8"
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
      "005cf388",
      "READ",
      [
        "storage",
        "00c9ad00",
        null,
        "pointer"
      ]
    ],
    [
      "005cf388",
      "PARAM",
      [
        "storage",
        "01127f18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "005cf39c",
      "READ",
      [
        "storage",
        "00c9b448",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005cf388",
      "READ",
      [
        "storage",
        "00c9bcd0",
        null,
        "pointer"
      ]
    ],
    [
      "005cf388",
      "PARAM",
      [
        "storage",
        "01128ed8",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "005cf39c",
      "READ",
      [
        "storage",
        "00c9c418",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005cefdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005cefbc.md#insn-005cefdc) · [`005ceff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005cefbc.md#insn-005ceff0) · [`005cefcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005cefbc.md#insn-005cefcc)
- 新版 [`005cf38c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cf/005cf36c.md#insn-005cf38c) · [`005cf3a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cf/005cf36c.md#insn-005cf3a0) · [`005cf37c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cf/005cf36c.md#insn-005cf37c)

~~~diff
- 005cefdc ["INT_ADD", "register:40f0:8", ["const:5cefdc:8", "const:4:8"]]
- 005cefdc ["CALL", null, ["callee:00c59320:8"]]
+ 005cf38c ["INT_ADD", "register:40f0:8", ["const:5cf38c:8", "const:4:8"]]
+ 005cf38c ["CALL", null, ["callee:00c59320:8"]]
- 005cefdc bytes dd241a94
+ 005cf38c bytes e5271a94
- 005ceff0 ["INT_ADD", "register:40f0:8", ["const:5ceff0:8", "const:4:8"]]
- 005ceff0 ["CALL", null, ["callee:00c59320:8"]]
+ 005cf3a0 ["INT_ADD", "register:40f0:8", ["const:5cf3a0:8", "const:4:8"]]
+ 005cf3a0 ["CALL", null, ["callee:00c59320:8"]]
- 005ceff0 bytes d8241a94
+ 005cf3a0 bytes e0271a94
- 005cefcc ["INT_ADD", "register:40f0:8", ["const:5cefcc:8", "const:4:8"]]
- 005cefcc ["CALL", null, ["callee:00c5b840:8"]]
+ 005cf37c ["INT_ADD", "register:40f0:8", ["const:5cf37c:8", "const:4:8"]]
+ 005cf37c ["CALL", null, ["callee:00c5b840:8"]]
- 005cefcc bytes 292e1a94
+ 005cf37c bytes 31311a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8923595146c3dac019b5b88a79bfcda8"></a>

### [`005cf028`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cf028.md) → [`005cf3d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cf/005cf3d8.md) FUN_005cf3d8

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005ce640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005ce640.md) · 呼出先 3件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c5a8a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a8a0.md)
- 新版 呼出元 1件 [`005ce9f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ce/005ce9f0.md) · 呼出先 3件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c5b870`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b870.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.11% / 新版 91.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005cf420",
      "incomplete_value": true,
      "site": "005cf420",
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
      "definition_site": "005cf070",
      "incomplete_value": true,
      "site": "005cf070",
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
    "ordinal": 7,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005cf410",
      "READ",
      [
        "storage",
        "00c9b4c8",
        null,
        "pointer"
      ]
    ],
    [
      "005cf420",
      "DATA",
      [
        "storage",
        "00c70d90",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "005cf410",
      "READ",
      [
        "storage",
        "00c9c498",
        null,
        "pointer"
      ]
    ],
    [
      "005cf420",
      "DATA",
      [
        "storage",
        "00c71d60",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005cf050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cf028.md#insn-005cf050) · [`005cf058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cf028.md#insn-005cf058) · [`005cf060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cf028.md#insn-005cf060)
- 新版 [`005cf400`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cf/005cf3d8.md#insn-005cf400) · [`005cf408`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cf/005cf3d8.md#insn-005cf408) · [`005cf410`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cf/005cf3d8.md#insn-005cf410)

~~~diff
- 005cf050 ["INT_ADD", "register:40f0:8", ["const:5cf050:8", "const:4:8"]]
- 005cf050 ["CALL", null, ["callee:00c58f30:8"]]
+ 005cf400 ["INT_ADD", "register:40f0:8", ["const:5cf400:8", "const:4:8"]]
+ 005cf400 ["CALL", null, ["callee:00c58f30:8"]]
- 005cf050 bytes c4231a94
+ 005cf400 bytes cc261a94
- 005cf058 ["COPY", "register:4048:8", ["const:c9b000:8"]]
+ 005cf408 ["COPY", "register:4048:8", ["const:c9c000:8"]]
- 005cf058 bytes 69360090
+ 005cf408 bytes 693600b0
- 005cf060 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:4c8:8"]]
- 005cf060 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005cf410 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:498:8"]]
+ 005cf410 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005cf060 bytes 296542f9
+ 005cf410 bytes 294d42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e580daa66145551a68b4bb57c57c9e88"></a>

### [`005cf0dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cf0dc.md) → [`005cf48c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cf/005cf48c.md) FUN_005cf48c

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`005ce640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005ce640.md) [`005ce9a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005ce9a4.md) [`005d523c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d5/005d523c.md) [`005d58ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d5/005d58ac.md) · 呼出先 4件 [`00c37324`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37324.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c5a880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a880.md)
- 新版 呼出元 4件 [`005ce9f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ce/005ce9f0.md) [`005ced54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ce/005ced54.md) [`005d55ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d5/005d55ec.md) [`005d5c5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d5/005d5c5c.md) · 呼出先 4件 [`00c38318`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38318.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md) [`00c5b850`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b850.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005cf4b8",
      "incomplete_value": true,
      "site": "005cf4c0",
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
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:450:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005cf108",
      "incomplete_value": true,
      "site": "005cf110",
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
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:480:8"
              ]
            ]
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
    "new": {
      "definition_site": "005cf4bc",
      "incomplete_value": true,
      "site": "005cf4c0",
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
                "const:c9c000:8"
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
      "definition_site": "005cf10c",
      "incomplete_value": true,
      "site": "005cf110",
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
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:488:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005cf4b8",
      "READ",
      [
        "storage",
        "00c9b480",
        null,
        "pointer"
      ]
    ],
    [
      "005cf4b8",
      "PARAM",
      [
        "storage",
        "00c96688",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005cf4bc",
      "READ",
      [
        "storage",
        "00c9b488",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005cf4b8",
      "READ",
      [
        "storage",
        "00c9c450",
        null,
        "pointer"
      ]
    ],
    [
      "005cf4b8",
      "PARAM",
      [
        "storage",
        "00c97658",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005cf4bc",
      "READ",
      [
        "storage",
        "00c9c458",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005cf110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cf0dc.md#insn-005cf110) · [`005cf0ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cf0dc.md#insn-005cf0ec) · [`005cf0f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cf0dc.md#insn-005cf0f8)
- 新版 [`005cf4c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cf/005cf48c.md#insn-005cf4c0) · [`005cf49c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cf/005cf48c.md#insn-005cf49c) · [`005cf4a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cf/005cf48c.md#insn-005cf4a8)

~~~diff
- 005cf110 ["INT_ADD", "register:40f0:8", ["const:5cf110:8", "const:4:8"]]
- 005cf110 ["CALL", null, ["callee:00c58fb0:8"]]
+ 005cf4c0 ["INT_ADD", "register:40f0:8", ["const:5cf4c0:8", "const:4:8"]]
+ 005cf4c0 ["CALL", null, ["callee:00c58fb0:8"]]
- 005cf110 bytes b4231a94
+ 005cf4c0 bytes bc261a94
- 005cf0ec ["INT_ADD", "register:40f0:8", ["const:5cf0ec:8", "const:4:8"]]
- 005cf0ec ["CALL", null, ["callee:00c58f90:8"]]
+ 005cf49c ["INT_ADD", "register:40f0:8", ["const:5cf49c:8", "const:4:8"]]
+ 005cf49c ["CALL", null, ["callee:00c58f90:8"]]
- 005cf0ec bytes b5231a94
+ 005cf49c bytes bd261a94
- 005cf0f8 ["INT_ADD", "register:40f0:8", ["const:5cf0f8:8", "const:4:8"]]
- 005cf0f8 ["CALL", null, ["callee:00c5b850:8"]]
+ 005cf4a8 ["INT_ADD", "register:40f0:8", ["const:5cf4a8:8", "const:4:8"]]
+ 005cf4a8 ["CALL", null, ["callee:00c5b850:8"]]
- 005cf0f8 bytes e22d1a94
+ 005cf4a8 bytes ea301a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e838795dab86628055853c8c0d1cca14"></a>

### [`005cf268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cf268.md) → [`005cf618`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cf/005cf618.md) FUN_005cf618

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59330.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.96% / 新版 86.96%

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
      "definition_site": "005cf634",
      "incomplete_value": true,
      "site": "005cf634",
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
      "definition_site": "005cf284",
      "incomplete_value": true,
      "site": "005cf284",
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
      "definition_site": "005cf648",
      "incomplete_value": true,
      "site": "005cf64c",
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
      "definition_site": "005cf298",
      "incomplete_value": true,
      "site": "005cf29c",
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
      "005cf62c",
      "READ",
      [
        "storage",
        "00c9b4a8",
        null,
        "pointer"
      ]
    ],
    [
      "005cf634",
      "DATA",
      [
        "storage",
        "00c70d48",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005cf640",
      "READ",
      [
        "storage",
        "00c9b478",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005cf62c",
      "READ",
      [
        "storage",
        "00c9c478",
        null,
        "pointer"
      ]
    ],
    [
      "005cf634",
      "DATA",
      [
        "storage",
        "00c71d18",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005cf640",
      "READ",
      [
        "storage",
        "00c9c448",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005cf274`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cf268.md#insn-005cf274) · [`005cf27c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cf268.md#insn-005cf27c) · [`005cf288`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cf268.md#insn-005cf288)
- 新版 [`005cf624`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cf/005cf618.md#insn-005cf624) · [`005cf62c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cf/005cf618.md#insn-005cf62c) · [`005cf638`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cf/005cf618.md#insn-005cf638)

~~~diff
- 005cf274 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 005cf624 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 005cf274 bytes 68360090
+ 005cf624 bytes 683600b0
- 005cf27c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4a8:8"]]
- 005cf27c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005cf62c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:478:8"]]
+ 005cf62c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005cf27c bytes 085542f9
+ 005cf62c bytes 083d42f9
- 005cf288 ["INT_ADD", "register:40f0:8", ["const:5cf288:8", "const:4:8"]]
- 005cf288 ["CALL", null, ["callee:00c59330:8"]]
+ 005cf638 ["INT_ADD", "register:40f0:8", ["const:5cf638:8", "const:4:8"]]
+ 005cf638 ["CALL", null, ["callee:00c59330:8"]]
- 005cf288 bytes 36241a94
+ 005cf638 bytes 3e271a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-730b6ba844b970311d591a4b55af842b"></a>

### [`005cf2c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cf2c4.md) → [`005cf674`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cf/005cf674.md) FUN_005cf674

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59330.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.36% / 新版 86.36%

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
      "definition_site": "005cf690",
      "incomplete_value": true,
      "site": "005cf690",
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
      "definition_site": "005cf2e0",
      "incomplete_value": true,
      "site": "005cf2e0",
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
      "definition_site": "005cf6a4",
      "incomplete_value": true,
      "site": "005cf6a8",
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
      "definition_site": "005cf2f4",
      "incomplete_value": true,
      "site": "005cf2f8",
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
      "005cf688",
      "READ",
      [
        "storage",
        "00c9b4a8",
        null,
        "pointer"
      ]
    ],
    [
      "005cf690",
      "DATA",
      [
        "storage",
        "00c70d48",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005cf69c",
      "READ",
      [
        "storage",
        "00c9b478",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005cf688",
      "READ",
      [
        "storage",
        "00c9c478",
        null,
        "pointer"
      ]
    ],
    [
      "005cf690",
      "DATA",
      [
        "storage",
        "00c71d18",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005cf69c",
      "READ",
      [
        "storage",
        "00c9c448",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005cf2d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cf2c4.md#insn-005cf2d0) · [`005cf2d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cf2c4.md#insn-005cf2d8) · [`005cf2e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cf2c4.md#insn-005cf2e4)
- 新版 [`005cf680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cf/005cf674.md#insn-005cf680) · [`005cf688`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cf/005cf674.md#insn-005cf688) · [`005cf694`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cf/005cf674.md#insn-005cf694)

~~~diff
- 005cf2d0 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 005cf680 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 005cf2d0 bytes 68360090
+ 005cf680 bytes 683600b0
- 005cf2d8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4a8:8"]]
- 005cf2d8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005cf688 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:478:8"]]
+ 005cf688 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005cf2d8 bytes 085542f9
+ 005cf688 bytes 083d42f9
- 005cf2e4 ["INT_ADD", "register:40f0:8", ["const:5cf2e4:8", "const:4:8"]]
- 005cf2e4 ["CALL", null, ["callee:00c59330:8"]]
+ 005cf694 ["INT_ADD", "register:40f0:8", ["const:5cf694:8", "const:4:8"]]
+ 005cf694 ["CALL", null, ["callee:00c59330:8"]]
- 005cf2e4 bytes 1f241a94
+ 005cf694 bytes 27271a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b7951b43e5e27c6fbdad3d5e21f4e51"></a>

### [`005cf42c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cf42c.md) → [`005cf7dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cf/005cf7dc.md) FUN_005cf7dc

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c59330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59330.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

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
      "definition_site": "005cf7f8",
      "incomplete_value": true,
      "site": "005cf7fc",
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
      "definition_site": "005cf448",
      "incomplete_value": true,
      "site": "005cf44c",
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
    "kind": "store_value",
    "new": {
      "definition_site": "005cf840",
      "incomplete_value": true,
      "site": "005cf844",
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
      "definition_site": "005cf490",
      "incomplete_value": true,
      "site": "005cf494",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005cf7f0",
      "READ",
      [
        "storage",
        "00c9b4c8",
        null,
        "pointer"
      ]
    ],
    [
      "005cf7fc",
      "DATA",
      [
        "storage",
        "00c70d90",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005cf838",
      "READ",
      [
        "storage",
        "00c9b478",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005cf7f0",
      "READ",
      [
        "storage",
        "00c9c498",
        null,
        "pointer"
      ]
    ],
    [
      "005cf7fc",
      "DATA",
      [
        "storage",
        "00c71d60",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005cf838",
      "READ",
      [
        "storage",
        "00c9c448",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005cf438`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cf42c.md#insn-005cf438) · [`005cf440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cf42c.md#insn-005cf440) · [`005cf45c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cf42c.md#insn-005cf45c)
- 新版 [`005cf7e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cf/005cf7dc.md#insn-005cf7e8) · [`005cf7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cf/005cf7dc.md#insn-005cf7f0) · [`005cf80c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cf/005cf7dc.md#insn-005cf80c)

~~~diff
- 005cf438 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 005cf7e8 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 005cf438 bytes 68360090
+ 005cf7e8 bytes 683600b0
- 005cf440 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4c8:8"]]
- 005cf440 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005cf7f0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:498:8"]]
+ 005cf7f0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005cf440 bytes 086542f9
+ 005cf7f0 bytes 084d42f9
- 005cf45c ["INT_ADD", "register:40f0:8", ["const:5cf45c:8", "const:4:8"]]
- 005cf45c ["CALL", null, ["callee:00c54d90:8"]]
+ 005cf80c ["INT_ADD", "register:40f0:8", ["const:5cf80c:8", "const:4:8"]]
+ 005cf80c ["CALL", null, ["callee:00c54d90:8"]]
- 005cf45c bytes 51121a94
+ 005cf80c bytes 61151a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afd51458ffafcd70b8e6a046eb7cb988"></a>

### [`005cf4bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cf4bc.md) → [`005cf86c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cf/005cf86c.md) FUN_005cf86c

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59330.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

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
      "definition_site": "005cf888",
      "incomplete_value": true,
      "site": "005cf88c",
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
      "definition_site": "005cf4d8",
      "incomplete_value": true,
      "site": "005cf4dc",
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
    "kind": "store_value",
    "new": {
      "definition_site": "005cf8d0",
      "incomplete_value": true,
      "site": "005cf8d4",
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
      "definition_site": "005cf520",
      "incomplete_value": true,
      "site": "005cf524",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005cf880",
      "READ",
      [
        "storage",
        "00c9b4c8",
        null,
        "pointer"
      ]
    ],
    [
      "005cf88c",
      "DATA",
      [
        "storage",
        "00c70d90",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005cf8c8",
      "READ",
      [
        "storage",
        "00c9b478",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005cf880",
      "READ",
      [
        "storage",
        "00c9c498",
        null,
        "pointer"
      ]
    ],
    [
      "005cf88c",
      "DATA",
      [
        "storage",
        "00c71d60",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005cf8c8",
      "READ",
      [
        "storage",
        "00c9c448",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005cf4c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cf4bc.md#insn-005cf4c8) · [`005cf4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cf4bc.md#insn-005cf4d0) · [`005cf4ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cf4bc.md#insn-005cf4ec)
- 新版 [`005cf878`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cf/005cf86c.md#insn-005cf878) · [`005cf880`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cf/005cf86c.md#insn-005cf880) · [`005cf89c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cf/005cf86c.md#insn-005cf89c)

~~~diff
- 005cf4c8 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 005cf878 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 005cf4c8 bytes 68360090
+ 005cf878 bytes 683600b0
- 005cf4d0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4c8:8"]]
- 005cf4d0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005cf880 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:498:8"]]
+ 005cf880 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005cf4d0 bytes 086542f9
+ 005cf880 bytes 084d42f9
- 005cf4ec ["INT_ADD", "register:40f0:8", ["const:5cf4ec:8", "const:4:8"]]
- 005cf4ec ["CALL", null, ["callee:00c54d90:8"]]
+ 005cf89c ["INT_ADD", "register:40f0:8", ["const:5cf89c:8", "const:4:8"]]
+ 005cf89c ["CALL", null, ["callee:00c54d90:8"]]
- 005cf4ec bytes 2d121a94
+ 005cf89c bytes 3d151a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4635d85bfe04e6472a0f6f04d34c123"></a>

### [`005cf700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cf700.md) → [`005cfab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cf/005cfab0.md) FUN_005cfab0

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`005cf548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cf548.md) [`005d5ca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d5/005d5ca0.md) · 呼出先 10件 [`005cfd94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cfd94.md) [`005cfde0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cfde0.md) [`005cff58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cff58.md) [`005cffa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cffa4.md) [`005d002c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d0/005d002c.md)
- 新版 呼出元 2件 [`005cf8f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cf/005cf8f8.md) [`005d6050`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d6/005d6050.md) · 呼出先 10件 [`005d0144`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d0144.md) [`005d0190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d0190.md) [`005d0308`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d0308.md) [`005d0354`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d0354.md) [`005d03dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d03dc.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 85.20% / 新版 85.20%

CFGの説明率　旧版 58.56% / 新版 59.63%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `store_condition` 1件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005cf7c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005cf7cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005cf7cc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005cf7e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005cfbb4"
      ]
    ],
    [
      "unmatched:005cf880",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005cfdbc"
      ]
    ],
    [
      "unmatched:005cf8d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005cfc24"
      ]
    ]
  ],
  "added": [
    [
      "005cfb98",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005cfbb4"
      ]
    ],
    [
      "005cfc30",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005cfdbc"
      ]
    ],
    [
      "005cfc84",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005cfc24"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005cf7c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cf700.md#insn-005cf7c4) · [`005cf7cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cf700.md#insn-005cf7cc) · [`005cf7d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cf700.md#insn-005cf7d0)

~~~diff
- 005cf7c4 ["COPY", "tmp:0:4", ["const:0:4"]]
- 005cf7c4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 005cf7c4 ["INT_ADD", "tmp:2:8", ["register:40e0:8", "const:ffffffffffffffa0:8"]]
- 005cf7c4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:4"]]
- 005cf7c4 bytes 9f031ab8
- 005cf7cc ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 005cf7cc ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 005cf7cc ["INT_ADD", "tmp:2:8", ["register:40e0:8", "const:ffffffffffffffa8:8"]]
- 005cf7cc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005cf7cc bytes 95d73aa9
- 005cf7d0 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 005cf7d0 ["INT_ADD", "tmp:1:8", ["register:40e0:8", "const:ffffffffffffffb8:8"]]
- 005cf7d0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 005cf7d0 bytes 96831bf8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c74b03c721ac76a6525e3fb7b11da40e"></a>

### [`005cfd3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cfd3c.md) → [`005d00ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d00ec.md) FUN_005d00ec

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`005cfb74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cfb74.md) [`005cfde0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cfde0.md) [`005d03c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d0/005d03c4.md) [`005d80cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d8/005d80cc.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 4件 [`005cff24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cf/005cff24.md) [`005d0190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d0190.md) [`005d0774`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d0774.md) [`005d847c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d8/005d847c.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "005d00f8",
      "incomplete_value": false,
      "site": "005d00fc",
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
      "definition_site": "005cfd48",
      "incomplete_value": false,
      "site": "005cfd4c",
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
      "005d00f8",
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
      "005d00f8",
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

- 旧版 [`005cfd4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cfd3c.md#insn-005cfd4c) · [`005cfd44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cfd3c.md#insn-005cfd44) · [`005cfd48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cfd3c.md#insn-005cfd48)
- 新版 [`005d00fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d00ec.md#insn-005d00fc) · [`005d00f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d00ec.md#insn-005d00f4) · [`005d00f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d00ec.md#insn-005d00f8)

~~~diff
- 005cfd4c ["INT_ADD", "register:40f0:8", ["const:5cfd4c:8", "const:4:8"]]
- 005cfd4c ["CALL", null, ["callee:0043bad8:8"]]
+ 005d00fc ["INT_ADD", "register:40f0:8", ["const:5d00fc:8", "const:4:8"]]
+ 005d00fc ["CALL", null, ["callee:0043bad8:8"]]
- 005cfd4c bytes 9baef997
+ 005d00fc bytes 77aef997
- 005cfd44 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 005d00f4 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 005cfd44 bytes 40e7ff90
+ 005d00f4 bytes 40e7ff90
- 005cfd48 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 005cfd48 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005cfd48 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005cfd48 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005d00f8 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 005d00f8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005d00f8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005d00f8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005cfd48 bytes 00303e91
+ 005d00f8 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4dc87977dc3736c19f8581dc78e85ae3"></a>

### [`005cfd94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cfd94.md) → [`005d0144`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d0144.md) FUN_005d0144

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`005cf700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cf700.md) [`005d6150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d6/005d6150.md) [`005d6a30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d6/005d6a30.md) · 呼出先 4件 [`00c37324`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37324.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c5a880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a880.md)
- 新版 呼出元 3件 [`005cfab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cf/005cfab0.md) [`005d6500`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d6/005d6500.md) [`005d6de0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d6/005d6de0.md) · 呼出先 4件 [`00c38318`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38318.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md) [`00c5b850`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b850.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005d0170",
      "incomplete_value": true,
      "site": "005d0178",
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
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:450:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005cfdc0",
      "incomplete_value": true,
      "site": "005cfdc8",
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
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:480:8"
              ]
            ]
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
    "new": {
      "definition_site": "005d0174",
      "incomplete_value": true,
      "site": "005d0178",
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
                "const:c9c000:8"
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
      "definition_site": "005cfdc4",
      "incomplete_value": true,
      "site": "005cfdc8",
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
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:488:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005d0170",
      "READ",
      [
        "storage",
        "00c9b480",
        null,
        "pointer"
      ]
    ],
    [
      "005d0170",
      "PARAM",
      [
        "storage",
        "00c96688",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005d0174",
      "READ",
      [
        "storage",
        "00c9b488",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d0170",
      "READ",
      [
        "storage",
        "00c9c450",
        null,
        "pointer"
      ]
    ],
    [
      "005d0170",
      "PARAM",
      [
        "storage",
        "00c97658",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005d0174",
      "READ",
      [
        "storage",
        "00c9c458",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005cfdc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cfd94.md#insn-005cfdc8) · [`005cfda4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cfd94.md#insn-005cfda4) · [`005cfdb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cfd94.md#insn-005cfdb0)
- 新版 [`005d0178`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d0144.md#insn-005d0178) · [`005d0154`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d0144.md#insn-005d0154) · [`005d0160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d0144.md#insn-005d0160)

~~~diff
- 005cfdc8 ["INT_ADD", "register:40f0:8", ["const:5cfdc8:8", "const:4:8"]]
- 005cfdc8 ["CALL", null, ["callee:00c58fb0:8"]]
+ 005d0178 ["INT_ADD", "register:40f0:8", ["const:5d0178:8", "const:4:8"]]
+ 005d0178 ["CALL", null, ["callee:00c58fb0:8"]]
- 005cfdc8 bytes 86201a94
+ 005d0178 bytes 8e231a94
- 005cfda4 ["INT_ADD", "register:40f0:8", ["const:5cfda4:8", "const:4:8"]]
- 005cfda4 ["CALL", null, ["callee:00c58f90:8"]]
+ 005d0154 ["INT_ADD", "register:40f0:8", ["const:5d0154:8", "const:4:8"]]
+ 005d0154 ["CALL", null, ["callee:00c58f90:8"]]
- 005cfda4 bytes 87201a94
+ 005d0154 bytes 8f231a94
- 005cfdb0 ["INT_ADD", "register:40f0:8", ["const:5cfdb0:8", "const:4:8"]]
- 005cfdb0 ["CALL", null, ["callee:00c5b850:8"]]
+ 005d0160 ["INT_ADD", "register:40f0:8", ["const:5d0160:8", "const:4:8"]]
+ 005d0160 ["CALL", null, ["callee:00c5b850:8"]]
- 005cfdb0 bytes b42a1a94
+ 005d0160 bytes bc2d1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be9c3a42055cb2975a863f75664442fd"></a>

### [`005cff58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cff58.md) → [`005d0308`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d0308.md) FUN_005d0308

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`005cf700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cf700.md) [`005d6150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d6/005d6150.md) [`005d6a30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d6/005d6a30.md) · 呼出先 4件 [`00c37324`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37324.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c5a880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a880.md)
- 新版 呼出元 3件 [`005cfab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cf/005cfab0.md) [`005d6500`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d6/005d6500.md) [`005d6de0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d6/005d6de0.md) · 呼出先 4件 [`00c38318`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38318.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md) [`00c5b850`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b850.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005d0334",
      "incomplete_value": true,
      "site": "005d033c",
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
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:450:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005cff84",
      "incomplete_value": true,
      "site": "005cff8c",
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
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:480:8"
              ]
            ]
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
    "new": {
      "definition_site": "005d0338",
      "incomplete_value": true,
      "site": "005d033c",
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
                "const:c9c000:8"
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
      "definition_site": "005cff88",
      "incomplete_value": true,
      "site": "005cff8c",
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
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:488:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005d0334",
      "READ",
      [
        "storage",
        "00c9b480",
        null,
        "pointer"
      ]
    ],
    [
      "005d0334",
      "PARAM",
      [
        "storage",
        "00c96688",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005d0338",
      "READ",
      [
        "storage",
        "00c9b488",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d0334",
      "READ",
      [
        "storage",
        "00c9c450",
        null,
        "pointer"
      ]
    ],
    [
      "005d0334",
      "PARAM",
      [
        "storage",
        "00c97658",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005d0338",
      "READ",
      [
        "storage",
        "00c9c458",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005cff8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cff58.md#insn-005cff8c) · [`005cff68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cff58.md#insn-005cff68) · [`005cff74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cff58.md#insn-005cff74)
- 新版 [`005d033c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d0308.md#insn-005d033c) · [`005d0318`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d0308.md#insn-005d0318) · [`005d0324`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d0308.md#insn-005d0324)

~~~diff
- 005cff8c ["INT_ADD", "register:40f0:8", ["const:5cff8c:8", "const:4:8"]]
- 005cff8c ["CALL", null, ["callee:00c58fb0:8"]]
+ 005d033c ["INT_ADD", "register:40f0:8", ["const:5d033c:8", "const:4:8"]]
+ 005d033c ["CALL", null, ["callee:00c58fb0:8"]]
- 005cff8c bytes 15201a94
+ 005d033c bytes 1d231a94
- 005cff68 ["INT_ADD", "register:40f0:8", ["const:5cff68:8", "const:4:8"]]
- 005cff68 ["CALL", null, ["callee:00c58f90:8"]]
+ 005d0318 ["INT_ADD", "register:40f0:8", ["const:5d0318:8", "const:4:8"]]
+ 005d0318 ["CALL", null, ["callee:00c58f90:8"]]
- 005cff68 bytes 16201a94
+ 005d0318 bytes 1e231a94
- 005cff74 ["INT_ADD", "register:40f0:8", ["const:5cff74:8", "const:4:8"]]
- 005cff74 ["CALL", null, ["callee:00c5b850:8"]]
+ 005d0324 ["INT_ADD", "register:40f0:8", ["const:5d0324:8", "const:4:8"]]
+ 005d0324 ["CALL", null, ["callee:00c5b850:8"]]
- 005cff74 bytes 432a1a94
+ 005d0324 bytes 4b2d1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ca9f31c75041f9e25b08fd544d5b20c"></a>

### [`005d03b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d0/005d03b0.md) → [`005d0760`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d0760.md) FUN_005d0760

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005d002c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d0/005d002c.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 1件 [`005d03dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d03dc.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "005d076c",
      "incomplete_value": false,
      "site": "005d0770",
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
      "definition_site": "005d03bc",
      "incomplete_value": false,
      "site": "005d03c0",
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
      "005d076c",
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
      "005d076c",
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

- 旧版 [`005d03c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d0/005d03b0.md#insn-005d03c0) · [`005d03b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d0/005d03b0.md#insn-005d03b8) · [`005d03bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d0/005d03b0.md#insn-005d03bc)
- 新版 [`005d0770`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d0760.md#insn-005d0770) · [`005d0768`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d0760.md#insn-005d0768) · [`005d076c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d0760.md#insn-005d076c)

~~~diff
- 005d03c0 ["INT_ADD", "register:40f0:8", ["const:5d03c0:8", "const:4:8"]]
- 005d03c0 ["CALL", null, ["callee:0043bad8:8"]]
+ 005d0770 ["INT_ADD", "register:40f0:8", ["const:5d0770:8", "const:4:8"]]
+ 005d0770 ["CALL", null, ["callee:0043bad8:8"]]
- 005d03c0 bytes feacf997
+ 005d0770 bytes daacf997
- 005d03b8 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 005d0768 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 005d03b8 bytes 20e7fff0
+ 005d0768 bytes 40e7ff90
- 005d03bc ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 005d03bc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005d03bc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005d03bc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005d076c ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 005d076c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005d076c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005d076c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005d03bc bytes 00303e91
+ 005d076c bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19fc6eb321606452ae8546d6165ed0bd"></a>

### [`005d067c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d0/005d067c.md) → [`005d0a2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d0a2c.md) FUN_005d0a2c

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`005cfde0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cfde0.md) [`005d0550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d0/005d0550.md) [`005d82b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d8/005d82b8.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 3件 [`005d0190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d0190.md) [`005d0900`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d0900.md) [`005d8668`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d8/005d8668.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "005d0a38",
      "incomplete_value": false,
      "site": "005d0a3c",
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
      "definition_site": "005d0688",
      "incomplete_value": false,
      "site": "005d068c",
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
      "005d0a38",
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
      "005d0a38",
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

- 旧版 [`005d068c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d0/005d067c.md#insn-005d068c) · [`005d0684`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d0/005d067c.md#insn-005d0684) · [`005d0688`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d0/005d067c.md#insn-005d0688)
- 新版 [`005d0a3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d0a2c.md#insn-005d0a3c) · [`005d0a34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d0a2c.md#insn-005d0a34) · [`005d0a38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d0a2c.md#insn-005d0a38)

~~~diff
- 005d068c ["INT_ADD", "register:40f0:8", ["const:5d068c:8", "const:4:8"]]
- 005d068c ["CALL", null, ["callee:0043bad8:8"]]
+ 005d0a3c ["INT_ADD", "register:40f0:8", ["const:5d0a3c:8", "const:4:8"]]
+ 005d0a3c ["CALL", null, ["callee:0043bad8:8"]]
- 005d068c bytes 4bacf997
+ 005d0a3c bytes 27acf997
- 005d0684 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 005d0a34 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 005d0684 bytes 20e7fff0
+ 005d0a34 bytes 40e7ff90
- 005d0688 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 005d0688 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005d0688 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005d0688 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005d0a38 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 005d0a38 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005d0a38 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005d0a38 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005d0688 bytes 00303e91
+ 005d0a38 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd03a9fdb49076290f89964aa5f23a93"></a>

### [`005d07e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d0/005d07e4.md) → [`005d0b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d0b94.md) FUN_005d0b94

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005ce9a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005ce9a4.md) · 呼出先 4件 [`00c37324`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37324.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c5a880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a880.md)
- 新版 呼出元 1件 [`005ced54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ce/005ced54.md) · 呼出先 4件 [`00c38318`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38318.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md) [`00c5b850`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b850.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005d0bc0",
      "incomplete_value": true,
      "site": "005d0bc8",
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
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:450:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d0810",
      "incomplete_value": true,
      "site": "005d0818",
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
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:480:8"
              ]
            ]
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
    "new": {
      "definition_site": "005d0bc4",
      "incomplete_value": true,
      "site": "005d0bc8",
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
                "const:c9c000:8"
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
      "definition_site": "005d0814",
      "incomplete_value": true,
      "site": "005d0818",
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
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:488:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005d0bc0",
      "READ",
      [
        "storage",
        "00c9b480",
        null,
        "pointer"
      ]
    ],
    [
      "005d0bc0",
      "PARAM",
      [
        "storage",
        "00c96688",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005d0bc4",
      "READ",
      [
        "storage",
        "00c9b488",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d0bc0",
      "READ",
      [
        "storage",
        "00c9c450",
        null,
        "pointer"
      ]
    ],
    [
      "005d0bc0",
      "PARAM",
      [
        "storage",
        "00c97658",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005d0bc4",
      "READ",
      [
        "storage",
        "00c9c458",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d0818`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d0/005d07e4.md#insn-005d0818) · [`005d07f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d0/005d07e4.md#insn-005d07f4) · [`005d0800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d0/005d07e4.md#insn-005d0800)
- 新版 [`005d0bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d0b94.md#insn-005d0bc8) · [`005d0ba4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d0b94.md#insn-005d0ba4) · [`005d0bb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d0b94.md#insn-005d0bb0)

~~~diff
- 005d0818 ["INT_ADD", "register:40f0:8", ["const:5d0818:8", "const:4:8"]]
- 005d0818 ["CALL", null, ["callee:00c58fb0:8"]]
+ 005d0bc8 ["INT_ADD", "register:40f0:8", ["const:5d0bc8:8", "const:4:8"]]
+ 005d0bc8 ["CALL", null, ["callee:00c58fb0:8"]]
- 005d0818 bytes f21d1a94
+ 005d0bc8 bytes fa201a94
- 005d07f4 ["INT_ADD", "register:40f0:8", ["const:5d07f4:8", "const:4:8"]]
- 005d07f4 ["CALL", null, ["callee:00c58f90:8"]]
+ 005d0ba4 ["INT_ADD", "register:40f0:8", ["const:5d0ba4:8", "const:4:8"]]
+ 005d0ba4 ["CALL", null, ["callee:00c58f90:8"]]
- 005d07f4 bytes f31d1a94
+ 005d0ba4 bytes fb201a94
- 005d0800 ["INT_ADD", "register:40f0:8", ["const:5d0800:8", "const:4:8"]]
- 005d0800 ["CALL", null, ["callee:00c5b850:8"]]
+ 005d0bb0 ["INT_ADD", "register:40f0:8", ["const:5d0bb0:8", "const:4:8"]]
+ 005d0bb0 ["CALL", null, ["callee:00c5b850:8"]]
- 005d0800 bytes 20281a94
+ 005d0bb0 bytes 282b1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-efad1fa998f6c34196d462d41accacaf"></a>

### [`005d08e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d0/005d08e0.md) → [`005d0c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d0c90.md) FUN_005d0c90

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`005ce9a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005ce9a4.md) [`005d0bf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d0/005d0bf8.md) [`005d34bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d3/005d34bc.md) [`005d35e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d3/005d35e0.md) · 呼出先 4件 [`00c37324`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37324.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c5a880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a880.md)
- 新版 呼出元 4件 [`005ced54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ce/005ced54.md) [`005d0fa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d0fa8.md) [`005d386c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d3/005d386c.md) [`005d3990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d3/005d3990.md) · 呼出先 4件 [`00c38318`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38318.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md) [`00c5b850`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b850.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005d0cbc",
      "incomplete_value": true,
      "site": "005d0cc4",
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
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:450:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d090c",
      "incomplete_value": true,
      "site": "005d0914",
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
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:480:8"
              ]
            ]
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
    "new": {
      "definition_site": "005d0cc0",
      "incomplete_value": true,
      "site": "005d0cc4",
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
                "const:c9c000:8"
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
      "definition_site": "005d0910",
      "incomplete_value": true,
      "site": "005d0914",
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
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:488:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005d0cbc",
      "READ",
      [
        "storage",
        "00c9b480",
        null,
        "pointer"
      ]
    ],
    [
      "005d0cbc",
      "PARAM",
      [
        "storage",
        "00c96688",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005d0cc0",
      "READ",
      [
        "storage",
        "00c9b488",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d0cbc",
      "READ",
      [
        "storage",
        "00c9c450",
        null,
        "pointer"
      ]
    ],
    [
      "005d0cbc",
      "PARAM",
      [
        "storage",
        "00c97658",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005d0cc0",
      "READ",
      [
        "storage",
        "00c9c458",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d0914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d0/005d08e0.md#insn-005d0914) · [`005d08f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d0/005d08e0.md#insn-005d08f0) · [`005d08fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d0/005d08e0.md#insn-005d08fc)
- 新版 [`005d0cc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d0c90.md#insn-005d0cc4) · [`005d0ca0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d0c90.md#insn-005d0ca0) · [`005d0cac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d0c90.md#insn-005d0cac)

~~~diff
- 005d0914 ["INT_ADD", "register:40f0:8", ["const:5d0914:8", "const:4:8"]]
- 005d0914 ["CALL", null, ["callee:00c58fb0:8"]]
+ 005d0cc4 ["INT_ADD", "register:40f0:8", ["const:5d0cc4:8", "const:4:8"]]
+ 005d0cc4 ["CALL", null, ["callee:00c58fb0:8"]]
- 005d0914 bytes b31d1a94
+ 005d0cc4 bytes bb201a94
- 005d08f0 ["INT_ADD", "register:40f0:8", ["const:5d08f0:8", "const:4:8"]]
- 005d08f0 ["CALL", null, ["callee:00c58f90:8"]]
+ 005d0ca0 ["INT_ADD", "register:40f0:8", ["const:5d0ca0:8", "const:4:8"]]
+ 005d0ca0 ["CALL", null, ["callee:00c58f90:8"]]
- 005d08f0 bytes b41d1a94
+ 005d0ca0 bytes bc201a94
- 005d08fc ["INT_ADD", "register:40f0:8", ["const:5d08fc:8", "const:4:8"]]
- 005d08fc ["CALL", null, ["callee:00c5b850:8"]]
+ 005d0cac ["INT_ADD", "register:40f0:8", ["const:5d0cac:8", "const:4:8"]]
+ 005d0cac ["CALL", null, ["callee:00c5b850:8"]]
- 005d08fc bytes e1271a94
+ 005d0cac bytes e92a1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0cf4b565e6b9f6c2ba818197f988894c"></a>

### [`005d0bf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d0/005d0bf8.md) → [`005d0fa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d0fa8.md) FUN_005d0fa8

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`005ce9a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005ce9a4.md) [`005d34bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d3/005d34bc.md) · 呼出先 3件 [`005d08e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d0/005d08e0.md) [`005d0ef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d0/005d0ef8.md) [`00c5a8b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a8b0.md)
- 新版 呼出元 2件 [`005ced54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ce/005ced54.md) [`005d386c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d3/005d386c.md) · 呼出先 3件 [`005d0c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d0c90.md) [`005d12a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d1/005d12a8.md) [`00c5b880`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b880.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.40% / 新版 97.40%

CFGの説明率　旧版 82.46% / 新版 81.03%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005d0d24"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005d0d78"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005d0db4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005d0d24",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d12a4"
      ]
    ],
    [
      "unmatched:005d0d78",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d114c"
      ]
    ],
    [
      "unmatched:005d0db4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d12a4"
      ]
    ]
  ],
  "added": [
    [
      "005d10d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d12a4"
      ]
    ],
    [
      "005d1128",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d114c"
      ]
    ],
    [
      "005d1164",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d12a4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d0d24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d0/005d0bf8.md#insn-005d0d24) · [`005d0d78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d0/005d0bf8.md#insn-005d0d78) · [`005d0db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d0/005d0bf8.md#insn-005d0db4)

~~~diff
- 005d0d24 ["CBRANCH", null, ["local:b72:8", "register:101:1"]]
- 005d0d24 bytes 800e0054
- 005d0d78 ["CBRANCH", null, ["local:b38:8", "register:101:1"]]
- 005d0d78 bytes 20010054
- 005d0db4 ["CBRANCH", null, ["local:b72:8", "register:101:1"]]
- 005d0db4 bytes 000a0054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e570a6bb66024b7734119890ba54563c"></a>

### [`005d0ef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d0/005d0ef8.md) → [`005d12a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d1/005d12a8.md) FUN_005d12a8

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 7件 [`005d0830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d0/005d0830.md) [`005d092c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d0/005d092c.md) [`005d0bf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d0/005d0bf8.md) [`005d35e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d3/005d35e0.md) [`005d5688`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d5/005d5688.md) · 呼出先 2件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c5a8a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a8a0.md)
- 新版 呼出元 7件 [`005d0be0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d0be0.md) [`005d0cdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d0cdc.md) [`005d0fa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d0fa8.md) [`005d3990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d3/005d3990.md) [`005d5a38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d5/005d5a38.md) · 呼出先 2件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c5b870`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b870.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 64.06% / 新版 64.06%

CFGの説明率　旧版 16.67% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005d0f3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005d0f3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005d0f40"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005d12c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:005d0f48"
      ]
    ],
    [
      "005d12dc",
      "READ",
      [
        "storage",
        "00c9b4d0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:005d0f3c",
      "DATA",
      [
        "storage",
        "00c70eb0",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "005d12c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d12f8"
      ]
    ],
    [
      "005d12dc",
      "READ",
      [
        "storage",
        "00c9c4a0",
        null,
        "pointer"
      ]
    ],
    [
      "005d12ec",
      "DATA",
      [
        "storage",
        "00c71e80",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d0f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d0/005d0ef8.md#insn-005d0f20) · [`005d0f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d0/005d0ef8.md#insn-005d0f3c) · [`005d0f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d0/005d0ef8.md#insn-005d0f40)
- 新版 [`005d12d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d1/005d12a8.md#insn-005d12d0)

~~~diff
- 005d0f20 ["INT_ADD", "register:40f0:8", ["const:5d0f20:8", "const:4:8"]]
- 005d0f20 ["CALL", null, ["callee:00c58f30:8"]]
+ 005d12d0 ["INT_ADD", "register:40f0:8", ["const:5d12d0:8", "const:4:8"]]
+ 005d12d0 ["CALL", null, ["callee:00c58f30:8"]]
- 005d0f20 bytes 101c1a94
+ 005d12d0 bytes 181f1a94
- 005d0f3c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 005d0f3c ["COPY", "tmp:1:8", ["register:4050:8"]]
- 005d0f3c ["COPY", "tmp:2:8", ["register:4000:8"]]
- 005d0f3c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005d0f3c bytes 092800a9
- 005d0f40 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:8:8"]]
- 005d0f40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 005d0f40 bytes 000500f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-015200b0b9e90dffd1378e03e2df64c3"></a>

### [`005d1038`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d1038.md) → [`005d13e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d1/005d13e8.md) FUN_005d13e8

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`005d092c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d0/005d092c.md) [`005d1724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d1724.md) [`005d523c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d5/005d523c.md) [`005d584c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d5/005d584c.md) · 呼出先 4件 [`00c37324`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37324.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c5a880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a880.md)
- 新版 呼出元 4件 [`005d0cdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d0cdc.md) [`005d1ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d1/005d1ad4.md) [`005d55ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d5/005d55ec.md) [`005d5bfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d5/005d5bfc.md) · 呼出先 4件 [`00c38318`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38318.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md) [`00c5b850`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b850.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005d1414",
      "incomplete_value": true,
      "site": "005d141c",
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
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:450:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d1064",
      "incomplete_value": true,
      "site": "005d106c",
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
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:480:8"
              ]
            ]
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
    "new": {
      "definition_site": "005d1418",
      "incomplete_value": true,
      "site": "005d141c",
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
                "const:c9c000:8"
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
      "definition_site": "005d1068",
      "incomplete_value": true,
      "site": "005d106c",
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
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:488:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005d1414",
      "READ",
      [
        "storage",
        "00c9b480",
        null,
        "pointer"
      ]
    ],
    [
      "005d1414",
      "PARAM",
      [
        "storage",
        "00c96688",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005d1418",
      "READ",
      [
        "storage",
        "00c9b488",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d1414",
      "READ",
      [
        "storage",
        "00c9c450",
        null,
        "pointer"
      ]
    ],
    [
      "005d1414",
      "PARAM",
      [
        "storage",
        "00c97658",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005d1418",
      "READ",
      [
        "storage",
        "00c9c458",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d106c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d1038.md#insn-005d106c) · [`005d1048`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d1038.md#insn-005d1048) · [`005d1054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d1038.md#insn-005d1054)
- 新版 [`005d141c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d1/005d13e8.md#insn-005d141c) · [`005d13f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d1/005d13e8.md#insn-005d13f8) · [`005d1404`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d1/005d13e8.md#insn-005d1404)

~~~diff
- 005d106c ["INT_ADD", "register:40f0:8", ["const:5d106c:8", "const:4:8"]]
- 005d106c ["CALL", null, ["callee:00c58fb0:8"]]
+ 005d141c ["INT_ADD", "register:40f0:8", ["const:5d141c:8", "const:4:8"]]
+ 005d141c ["CALL", null, ["callee:00c58fb0:8"]]
- 005d106c bytes dd1b1a94
+ 005d141c bytes e51e1a94
- 005d1048 ["INT_ADD", "register:40f0:8", ["const:5d1048:8", "const:4:8"]]
- 005d1048 ["CALL", null, ["callee:00c58f90:8"]]
+ 005d13f8 ["INT_ADD", "register:40f0:8", ["const:5d13f8:8", "const:4:8"]]
+ 005d13f8 ["CALL", null, ["callee:00c58f90:8"]]
- 005d1048 bytes de1b1a94
+ 005d13f8 bytes e61e1a94
- 005d1054 ["INT_ADD", "register:40f0:8", ["const:5d1054:8", "const:4:8"]]
- 005d1054 ["CALL", null, ["callee:00c5b850:8"]]
+ 005d1404 ["INT_ADD", "register:40f0:8", ["const:5d1404:8", "const:4:8"]]
+ 005d1404 ["CALL", null, ["callee:00c5b850:8"]]
- 005d1054 bytes 0b261a94
+ 005d1404 bytes 13291a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3c61e0f60ab49e5eb013903a2e67640"></a>

### [`005d1084`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d1084.md) → [`005d1434`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d1/005d1434.md) FUN_005d1434

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`005d092c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d0/005d092c.md) [`005d523c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d5/005d523c.md) [`005d584c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d5/005d584c.md) · 呼出先 2件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c5a8a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a8a0.md)
- 新版 呼出元 3件 [`005d0cdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d0cdc.md) [`005d55ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d5/005d55ec.md) [`005d5bfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d5/005d5bfc.md) · 呼出先 2件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c5b870`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b870.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 70.00% / 新版 70.00%

CFGの説明率　旧版 20.00% / 新版 18.18%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 8件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005d1084"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005d1084"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005d1088"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005d1084",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:005d1088",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:005d108c",
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
      "005d1434",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "005d1438",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005d143c",
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

- 旧版 [`005d1084`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d1084.md#insn-005d1084) · [`005d1088`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d1084.md#insn-005d1088) · [`005d108c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d1084.md#insn-005d108c)

~~~diff
- 005d1084 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005d1084 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005d1084 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 005d1084 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005d1084 bytes fd7bbda9
- 005d1088 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 005d1088 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 005d1088 bytes f50b00f9
- 005d108c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 005d108c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 005d108c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 005d108c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005d108c bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd3e24fb59bfc29e6515d4b54f1cab4e"></a>

### [`005d114c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d114c.md) → [`005d14fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d1/005d14fc.md) FUN_005d14fc

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59330.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.96% / 新版 86.96%

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
      "definition_site": "005d1518",
      "incomplete_value": true,
      "site": "005d1518",
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
      "definition_site": "005d1168",
      "incomplete_value": true,
      "site": "005d1168",
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
      "definition_site": "005d152c",
      "incomplete_value": true,
      "site": "005d1530",
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
      "definition_site": "005d117c",
      "incomplete_value": true,
      "site": "005d1180",
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
      "005d1510",
      "READ",
      [
        "storage",
        "00c9b4d8",
        null,
        "pointer"
      ]
    ],
    [
      "005d1518",
      "DATA",
      [
        "storage",
        "00c70e20",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d1524",
      "READ",
      [
        "storage",
        "00c9b478",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d1510",
      "READ",
      [
        "storage",
        "00c9c4a8",
        null,
        "pointer"
      ]
    ],
    [
      "005d1518",
      "DATA",
      [
        "storage",
        "00c71df0",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d1524",
      "READ",
      [
        "storage",
        "00c9c448",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d1158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d114c.md#insn-005d1158) · [`005d1160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d114c.md#insn-005d1160) · [`005d116c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d114c.md#insn-005d116c)
- 新版 [`005d1508`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d1/005d14fc.md#insn-005d1508) · [`005d1510`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d1/005d14fc.md#insn-005d1510) · [`005d151c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d1/005d14fc.md#insn-005d151c)

~~~diff
- 005d1158 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 005d1508 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 005d1158 bytes 483600d0
+ 005d1508 bytes 483600f0
- 005d1160 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4d8:8"]]
- 005d1160 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005d1510 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4a8:8"]]
+ 005d1510 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005d1160 bytes 086d42f9
+ 005d1510 bytes 085542f9
- 005d116c ["INT_ADD", "register:40f0:8", ["const:5d116c:8", "const:4:8"]]
- 005d116c ["CALL", null, ["callee:00c59330:8"]]
+ 005d151c ["INT_ADD", "register:40f0:8", ["const:5d151c:8", "const:4:8"]]
+ 005d151c ["CALL", null, ["callee:00c59330:8"]]
- 005d116c bytes 7d1c1a94
+ 005d151c bytes 851f1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24f54e3ba8aa215c401f08d9b1afc240"></a>

### [`005d11a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d11a8.md) → [`005d1558`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d1/005d1558.md) FUN_005d1558

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59330.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 86.36% / 新版 86.36%

CFGの説明率　旧版 20.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005d11c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005d1588",
      "incomplete_value": true,
      "site": "005d158c",
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
      "definition_site": "005d11d8",
      "incomplete_value": true,
      "site": "005d11dc",
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
    "kind": "store_position_unpaired",
    "new": {
      "site": "005d1574"
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
      "unmatched:005d11bc",
      "READ",
      [
        "storage",
        "00c9b4d8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:005d11c4",
      "DATA",
      [
        "storage",
        "00c70e20",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d1580",
      "READ",
      [
        "storage",
        "00c9b478",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d156c",
      "READ",
      [
        "storage",
        "00c9c4a8",
        null,
        "pointer"
      ]
    ],
    [
      "005d1574",
      "DATA",
      [
        "storage",
        "00c71df0",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d1580",
      "READ",
      [
        "storage",
        "00c9c448",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d11c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d11a8.md#insn-005d11c4) · [`005d11c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d11a8.md#insn-005d11c8)
- 新版 [`005d1578`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d1/005d1558.md#insn-005d1578) · [`005d1574`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d1/005d1558.md#insn-005d1574)

~~~diff
- 005d11c4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 005d11c4 ["COPY", "tmp:1:8", ["register:4000:8"]]
- 005d11c4 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:10:8"]]
- 005d11c4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 005d11c4 bytes 080401f8
- 005d11c8 ["INT_ADD", "register:40f0:8", ["const:5d11c8:8", "const:4:8"]]
- 005d11c8 ["CALL", null, ["callee:00c59330:8"]]
+ 005d1578 ["INT_ADD", "register:40f0:8", ["const:5d1578:8", "const:4:8"]]
+ 005d1578 ["CALL", null, ["callee:00c59330:8"]]
- 005d11c8 bytes 661c1a94
+ 005d1578 bytes 6e1f1a94
+ 005d1574 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 005d1574 ["COPY", "tmp:1:8", ["register:4000:8"]]
+ 005d1574 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:10:8"]]
+ 005d1574 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 005d1574 bytes 080401f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d458e483d7217d795190ddd62c96975"></a>

### [`005d12d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d12d4.md) → [`005d1684`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d1/005d1684.md) FUN_005d1684

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59330.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.36% / 新版 86.36%

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
      "definition_site": "005d16a0",
      "incomplete_value": true,
      "site": "005d16a0",
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
      "definition_site": "005d12f0",
      "incomplete_value": true,
      "site": "005d12f0",
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
      "definition_site": "005d16b4",
      "incomplete_value": true,
      "site": "005d16b8",
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
      "definition_site": "005d1304",
      "incomplete_value": true,
      "site": "005d1308",
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
      "005d1698",
      "READ",
      [
        "storage",
        "00c9b4e0",
        null,
        "pointer"
      ]
    ],
    [
      "005d16a0",
      "DATA",
      [
        "storage",
        "00c70e68",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d16ac",
      "READ",
      [
        "storage",
        "00c9b478",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d1698",
      "READ",
      [
        "storage",
        "00c9c4b0",
        null,
        "pointer"
      ]
    ],
    [
      "005d16a0",
      "DATA",
      [
        "storage",
        "00c71e38",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d16ac",
      "READ",
      [
        "storage",
        "00c9c448",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d12e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d12d4.md#insn-005d12e0) · [`005d12e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d12d4.md#insn-005d12e8) · [`005d12f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d12d4.md#insn-005d12f4)
- 新版 [`005d1690`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d1/005d1684.md#insn-005d1690) · [`005d1698`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d1/005d1684.md#insn-005d1698) · [`005d16a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d1/005d1684.md#insn-005d16a4)

~~~diff
- 005d12e0 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 005d1690 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 005d12e0 bytes 483600d0
+ 005d1690 bytes 483600f0
- 005d12e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4e0:8"]]
- 005d12e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005d1698 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4b0:8"]]
+ 005d1698 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005d12e8 bytes 087142f9
+ 005d1698 bytes 085942f9
- 005d12f4 ["INT_ADD", "register:40f0:8", ["const:5d12f4:8", "const:4:8"]]
- 005d12f4 ["CALL", null, ["callee:00c59330:8"]]
+ 005d16a4 ["INT_ADD", "register:40f0:8", ["const:5d16a4:8", "const:4:8"]]
+ 005d16a4 ["CALL", null, ["callee:00c59330:8"]]
- 005d12f4 bytes 1b1c1a94
+ 005d16a4 bytes 231f1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7e784e95b1fdaaf9f1d6662fd929734"></a>

### [`005d132c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d132c.md) → [`005d16dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d1/005d16dc.md) FUN_005d16dc

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 20.00% / 新版 25.00%

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
      "site": "005d1344"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "005d16f4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "005d1344"
      ],
      [
        "FALL_THROUGH",
        "005d16f4"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "005d16f4",
      "incomplete_value": true,
      "site": "005d1704",
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
    "old": {
      "definition_site": "005d1344",
      "incomplete_value": true,
      "site": "005d1354",
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
      "unmatched:005d1344",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d1714"
      ]
    ]
  ],
  "added": [
    [
      "005d16f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d1714"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d1344`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d132c.md#insn-005d1344) · [`005d1334`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d132c.md#insn-005d1334)
- 新版 [`005d16f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d1/005d16dc.md#insn-005d16f4) · [`005d16e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d1/005d16dc.md#insn-005d16e4)

~~~diff
- 005d1344 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 005d1344 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 005d1344 bytes 01010054
+ 005d16f4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 005d16f4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 005d16f4 bytes 01010054
- 005d1334 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
+ 005d16e4 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 005d1334 bytes 80010054
+ 005d16e4 bytes 80010054
~~~


<a id="compare-e25c9f6f2680fdc3b8bdc4b79e64c223"></a>

### [`005d13bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d13bc.md) → [`005d176c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d1/005d176c.md) FUN_005d176c

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 25.00% / 新版 16.67%

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
      "site": "005d13d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "005d1784"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "005d13d4"
      ],
      [
        "FALL_THROUGH",
        "005d1784"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "005d1784",
      "incomplete_value": true,
      "site": "005d1794",
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
      "definition_site": "005d13d4",
      "incomplete_value": true,
      "site": "005d13e4",
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
      "unmatched:005d13d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d17a4"
      ]
    ]
  ],
  "added": [
    [
      "005d1784",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d17a4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d13d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d13bc.md#insn-005d13d4) · [`005d13c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d13bc.md#insn-005d13c4)
- 新版 [`005d1784`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d1/005d176c.md#insn-005d1784) · [`005d1774`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d1/005d176c.md#insn-005d1774)

~~~diff
- 005d13d4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 005d13d4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 005d13d4 bytes 01010054
+ 005d1784 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 005d1784 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 005d1784 bytes 01010054
- 005d13c4 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
+ 005d1774 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
- 005d13c4 bytes 80010054
+ 005d1774 bytes 80010054
~~~


<a id="compare-863e57a7cf360b67d03eec27bc1a0d98"></a>

### [`005d1404`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d1404.md) → [`005d17b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d1/005d17b4.md) FUN_005d17b4

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59330.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_value, unresolved_return_alignment

命令の説明率　旧版 82.61% / 新版 82.61%

CFGの説明率　旧版 33.33% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_return_alignment` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005d17d0",
      "incomplete_value": true,
      "site": "005d17d0",
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
      "definition_site": "005d1420",
      "incomplete_value": true,
      "site": "005d1420",
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
      "definition_site": "005d17e4",
      "incomplete_value": true,
      "site": "005d17e8",
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
      "definition_site": "005d1434",
      "incomplete_value": true,
      "site": "005d1438",
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
      "site": "005d145c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005d17c8",
      "READ",
      [
        "storage",
        "00c9b4f0",
        null,
        "pointer"
      ]
    ],
    [
      "005d17d0",
      "DATA",
      [
        "storage",
        "00c70ef8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d17dc",
      "READ",
      [
        "storage",
        "00c9b478",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d17c8",
      "READ",
      [
        "storage",
        "00c9c4c0",
        null,
        "pointer"
      ]
    ],
    [
      "005d17d0",
      "DATA",
      [
        "storage",
        "00c71ec8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d17dc",
      "READ",
      [
        "storage",
        "00c9c448",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d145c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d1404.md#insn-005d145c) · [`005d1410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d1404.md#insn-005d1410)
- 新版 [`005d180c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d1/005d17b4.md#insn-005d180c) · [`005d17c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d1/005d17b4.md#insn-005d17c0)

~~~diff
- 005d145c ["COPY", "register:0:8", ["register:40f0:8"]]
- 005d145c ["RETURN", null, ["register:0:8"]]
- 005d145c bytes c0035fd6
+ 005d180c ["COPY", "register:0:8", ["register:40f0:8"]]
+ 005d180c ["RETURN", null, ["register:0:8"]]
+ 005d180c bytes c0035fd6
- 005d1410 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 005d17c0 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 005d1410 bytes 483600d0
+ 005d17c0 bytes 483600f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9ebda45bcc927620e923cef2dc8aebb"></a>

### [`005d1460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d1460.md) → [`005d1810`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d1/005d1810.md) FUN_005d1810

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59330.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 25.00% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005d1460"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005d1460"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005d1464"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005d1460",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:005d1464",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:005d1474",
      "READ",
      [
        "storage",
        "00c9b4f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d1810",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005d1814",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005d1824",
      "READ",
      [
        "storage",
        "00c9c4c0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d1460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d1460.md#insn-005d1460) · [`005d1464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d1460.md#insn-005d1464) · [`005d147c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d1460.md#insn-005d147c)

~~~diff
- 005d1460 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005d1460 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005d1460 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 005d1460 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005d1460 bytes fd7bbea9
- 005d1464 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 005d1464 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 005d1464 bytes f30b00f9
- 005d147c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 005d147c ["COPY", "tmp:1:8", ["register:4000:8"]]
- 005d147c ["INT_ADD", "register:4000:8", ["register:4000:8", "const:10:8"]]
- 005d147c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 005d147c bytes 080401f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5140f5b75c1feaaf3d9f157180a827fe"></a>

### [`005d15a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d15a0.md) → [`005d1950`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d1/005d1950.md) FUN_005d1950

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59330.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.96% / 新版 86.96%

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
      "definition_site": "005d196c",
      "incomplete_value": true,
      "site": "005d196c",
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
      "definition_site": "005d15bc",
      "incomplete_value": true,
      "site": "005d15bc",
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
      "definition_site": "005d1980",
      "incomplete_value": true,
      "site": "005d1984",
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
      "definition_site": "005d15d0",
      "incomplete_value": true,
      "site": "005d15d4",
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
      "005d1964",
      "READ",
      [
        "storage",
        "00c9b4f8",
        null,
        "pointer"
      ]
    ],
    [
      "005d196c",
      "DATA",
      [
        "storage",
        "00c70f40",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d1978",
      "READ",
      [
        "storage",
        "00c9b478",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d1964",
      "READ",
      [
        "storage",
        "00c9c4c8",
        null,
        "pointer"
      ]
    ],
    [
      "005d196c",
      "DATA",
      [
        "storage",
        "00c71f10",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d1978",
      "READ",
      [
        "storage",
        "00c9c448",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d15ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d15a0.md#insn-005d15ac) · [`005d15b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d15a0.md#insn-005d15b4) · [`005d15c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d15a0.md#insn-005d15c0)
- 新版 [`005d195c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d1/005d1950.md#insn-005d195c) · [`005d1964`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d1/005d1950.md#insn-005d1964) · [`005d1970`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d1/005d1950.md#insn-005d1970)

~~~diff
- 005d15ac ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 005d195c ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 005d15ac bytes 483600d0
+ 005d195c bytes 483600f0
- 005d15b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4f8:8"]]
- 005d15b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005d1964 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4c8:8"]]
+ 005d1964 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005d15b4 bytes 087d42f9
+ 005d1964 bytes 086542f9
- 005d15c0 ["INT_ADD", "register:40f0:8", ["const:5d15c0:8", "const:4:8"]]
- 005d15c0 ["CALL", null, ["callee:00c59330:8"]]
+ 005d1970 ["INT_ADD", "register:40f0:8", ["const:5d1970:8", "const:4:8"]]
+ 005d1970 ["CALL", null, ["callee:00c59330:8"]]
- 005d15c0 bytes 681b1a94
+ 005d1970 bytes 701e1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bcf4e2cb446d751b581d1bb5eff30ed9"></a>

### [`005d15fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d15fc.md) → [`005d19ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d1/005d19ac.md) FUN_005d19ac

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59330.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 86.36% / 新版 86.36%

CFGの説明率　旧版 33.33% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005d1618"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005d19dc",
      "incomplete_value": true,
      "site": "005d19e0",
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
      "definition_site": "005d162c",
      "incomplete_value": true,
      "site": "005d1630",
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
    "kind": "store_position_unpaired",
    "new": {
      "site": "005d19c8"
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
      "unmatched:005d1610",
      "READ",
      [
        "storage",
        "00c9b4f8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:005d1618",
      "DATA",
      [
        "storage",
        "00c70f40",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d19d4",
      "READ",
      [
        "storage",
        "00c9b478",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d19c0",
      "READ",
      [
        "storage",
        "00c9c4c8",
        null,
        "pointer"
      ]
    ],
    [
      "005d19c8",
      "DATA",
      [
        "storage",
        "00c71f10",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d19d4",
      "READ",
      [
        "storage",
        "00c9c448",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d1618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d15fc.md#insn-005d1618) · [`005d161c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d15fc.md#insn-005d161c)
- 新版 [`005d19cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d1/005d19ac.md#insn-005d19cc) · [`005d19c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d1/005d19ac.md#insn-005d19c8)

~~~diff
- 005d1618 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 005d1618 ["COPY", "tmp:1:8", ["register:4000:8"]]
- 005d1618 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:10:8"]]
- 005d1618 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 005d1618 bytes 080401f8
- 005d161c ["INT_ADD", "register:40f0:8", ["const:5d161c:8", "const:4:8"]]
- 005d161c ["CALL", null, ["callee:00c59330:8"]]
+ 005d19cc ["INT_ADD", "register:40f0:8", ["const:5d19cc:8", "const:4:8"]]
+ 005d19cc ["CALL", null, ["callee:00c59330:8"]]
- 005d161c bytes 511b1a94
+ 005d19cc bytes 591e1a94
+ 005d19c8 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 005d19c8 ["COPY", "tmp:1:8", ["register:4000:8"]]
+ 005d19c8 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:10:8"]]
+ 005d19c8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 005d19c8 bytes 080401f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58a2fc5ce74c23e4e839ccbd887fbc47"></a>

### [`005d16dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d16dc.md) → [`005d1a8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d1/005d1a8c.md) FUN_005d1a8c

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 61.11% / 新版 61.11%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 3件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005d16ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005d1a9c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005d16f0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005d16e0",
      "READ",
      [
        "storage",
        "00c9b478",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:005d16ec",
      "DATA",
      [
        "storage",
        "00c70c88",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "unmatched:005d16f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d1ad0"
      ]
    ]
  ],
  "added": [
    [
      "005d1a90",
      "READ",
      [
        "storage",
        "00c9c448",
        null,
        "pointer"
      ]
    ],
    [
      "005d1a9c",
      "DATA",
      [
        "storage",
        "00c71c58",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d1aa0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d1ad0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d16ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d16dc.md#insn-005d16ec) · [`005d16f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d16dc.md#insn-005d16f0) · [`005d1710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d16dc.md#insn-005d1710)

~~~diff
- 005d16ec ["COPY", "tmp:0:8", ["register:4000:8"]]
- 005d16ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 005d16ec bytes 090000f9
- 005d16f0 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 005d16f0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 005d16f0 bytes 880100b4
- 005d1710 ["COPY", "register:0:8", ["register:4048:8"]]
- 005d1710 ["INT_ADD", "register:40f0:8", ["const:5d1710:8", "const:4:8"]]
- 005d1710 ["CALLIND", null, ["register:0:8"]]
- 005d1710 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10c75751fc47e5b75ffa7cbec01feb50"></a>

### [`005d17e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d17e4.md) → [`005d1b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d1/005d1b94.md) FUN_005d1b94

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`005d0690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d0/005d0690.md) [`005d09f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d0/005d09f4.md) [`005d2c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d2/005d2c44.md) [`005d3114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d3/005d3114.md) [`005d34bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d3/005d34bc.md) · 呼出先 4件 [`004499f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00449/004499f8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 5件 [`005d0a40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d0a40.md) [`005d0da4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d0da4.md) [`005d2ff4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d2/005d2ff4.md) [`005d34c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d3/005d34c4.md) [`005d386c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d3/005d386c.md) · 呼出先 4件 [`00449d18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00449/00449d18.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 73.56% / 新版 73.56%

CFGの説明率　旧版 14.81% / 新版 12.90%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 1件, `unresolved_branch_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005d1834"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005d184c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005d1860"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005d1bcc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:005d1840"
      ]
    ],
    [
      "unmatched:005d1834",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d1c3c"
      ]
    ],
    [
      "unmatched:005d184c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d1ce8"
      ]
    ]
  ],
  "added": [
    [
      "005d1bcc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d1bf0"
      ]
    ],
    [
      "005d1be4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d1c3c"
      ]
    ],
    [
      "005d1bfc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d1ce8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d1834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d17e4.md#insn-005d1834) · [`005d184c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d17e4.md#insn-005d184c) · [`005d1860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d17e4.md#insn-005d1860)

~~~diff
- 005d1834 ["CBRANCH", null, ["local:b9:8", "register:102:1"]]
- 005d1834 bytes c2020054
- 005d184c ["CBRANCH", null, ["local:b20:8", "register:100:1"]]
- 005d184c bytes 64070054
- 005d1860 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 005d1860 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 005d1860 ["COPY", "tmp:2:8", ["register:4050:8"]]
- 005d1860 ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 005d1860 bytes 4981899a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b16c0b7e85610d4c8ad14b5c3941058"></a>

### [`005d1940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d1940.md) → [`005d1cf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d1/005d1cf0.md) FUN_005d1cf0

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`005d0690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d0/005d0690.md) [`005d09f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d0/005d09f4.md) · 呼出先 5件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md) [`00c5a8a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a8a0.md) [`00c5a8c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a8c0.md)
- 新版 呼出元 2件 [`005d0a40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d0a40.md) [`005d0da4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d0da4.md) · 呼出先 5件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59330.md) [`00c5b870`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b870.md) [`00c5b890`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b890.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 77.33% / 新版 77.33%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005d1954"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005d1954"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005d1988"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005d1954",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:005d196c",
      "READ",
      [
        "storage",
        "00c9b500",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:005d1988",
      "DATA",
      [
        "storage",
        "00c70fd0",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "005d1d04",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005d1d1c",
      "READ",
      [
        "storage",
        "00c9c4d0",
        null,
        "pointer"
      ]
    ],
    [
      "005d1d38",
      "DATA",
      [
        "storage",
        "00c71fa0",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d1954`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d1940.md#insn-005d1954) · [`005d1988`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d1940.md#insn-005d1988) · [`005d19a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d1940.md#insn-005d19a4)

~~~diff
- 005d1954 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 005d1954 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 005d1954 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 005d1954 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005d1954 bytes f44f07a9
- 005d1988 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 005d1988 ["COPY", "tmp:1:8", ["register:4010:8"]]
- 005d1988 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 005d1988 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:10:8"]]
- 005d1988 bytes 080881a8
- 005d19a4 ["INT_ADD", "register:40a8:8", ["register:40a8:8", "const:58:8"]]
- 005d19a4 ["STORE", null, ["const:1b1:8", "register:40a8:8", "register:5000:16"]]
- 005d19a4 bytes a08e853c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5ced3358ce2926957f0a2cb5a17cc67"></a>

### [`005d1afc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d1afc.md) → [`005d1eac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d1/005d1eac.md) FUN_005d1eac

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 68.57% / 新版 68.57%

CFGの説明率　旧版 35.29% / 新版 35.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005d1afc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005d1afc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005d1b00"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005d1afc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:005d1b00",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:005d1b04",
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
      "005d1eac",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "005d1eb0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005d1eb4",
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

- 旧版 [`005d1afc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d1afc.md#insn-005d1afc) · [`005d1b00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d1afc.md#insn-005d1b00) · [`005d1b04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d1afc.md#insn-005d1b04)

~~~diff
- 005d1afc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005d1afc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005d1afc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 005d1afc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005d1afc bytes fd7bbda9
- 005d1b00 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 005d1b00 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 005d1b00 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 005d1b00 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005d1b00 bytes f65701a9
- 005d1b04 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 005d1b04 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 005d1b04 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 005d1b04 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005d1b04 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a286b2087dd07ee2ecb3bf4da4ba6cfb"></a>

### [`005d1b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d1b88.md) → [`005d1f38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d1/005d1f38.md) FUN_005d1f38

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005d1ccc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d1ccc.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md)
- 新版 呼出元 1件 [`005d207c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d2/005d207c.md) · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59330.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 87.65% / 新版 87.65%

CFGの説明率　旧版 55.81% / 新版 57.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005d1bac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005d2048",
      "incomplete_value": true,
      "site": "005d204c",
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
      "definition_site": "005d1c98",
      "incomplete_value": true,
      "site": "005d1c9c",
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
    "kind": "store_position_unpaired",
    "new": {
      "site": "005d1f5c"
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
      "unmatched:005d1ba0",
      "READ",
      [
        "storage",
        "00c9b500",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:005d1bac",
      "DATA",
      [
        "storage",
        "00c70fd0",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "unmatched:005d1bfc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d1fb8"
      ]
    ]
  ],
  "added": [
    [
      "005d1f50",
      "READ",
      [
        "storage",
        "00c9c4d0",
        null,
        "pointer"
      ]
    ],
    [
      "005d1f5c",
      "DATA",
      [
        "storage",
        "00c71fa0",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d1fac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d1fb8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d1bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d1b88.md#insn-005d1bac) · [`005d1bfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d1b88.md#insn-005d1bfc)
- 新版 [`005d1f5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d1/005d1f38.md#insn-005d1f5c)

~~~diff
- 005d1bac ["COPY", "tmp:0:8", ["register:4000:8"]]
- 005d1bac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 005d1bac bytes 080000f9
- 005d1bfc ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 005d1bfc ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 005d1bfc bytes 600000b4
+ 005d1f5c ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 005d1f5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 005d1f5c bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd73343d29b03979c18c4718f3a6895a"></a>

### [`005d1cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d1cf0.md) → [`005d20a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d2/005d20a0.md) FUN_005d20a0

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`005d2650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d2/005d2650.md) [`005d27c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d2/005d27c0.md) [`005d2a24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d2/005d2a24.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`005d2a00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d2/005d2a00.md) [`005d2b70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d2/005d2b70.md) [`005d2dd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d2/005d2dd4.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 97.79% / 新版 97.79%

CFGの説明率　旧版 87.95% / 新版 88.34%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005d1d20"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005d20d0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005d1db8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005d1d20",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:005d1dd4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d2418"
      ]
    ],
    [
      "unmatched:005d1e5c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d222c"
      ]
    ]
  ],
  "added": [
    [
      "005d20d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "005d2184",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d2418"
      ]
    ],
    [
      "005d220c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d222c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d1d20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d1cf0.md#insn-005d1d20) · [`005d1d68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d1cf0.md#insn-005d1d68) · [`005d1da4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d1cf0.md#insn-005d1da4)
- 新版 [`005d2154`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d2/005d20a0.md#insn-005d2154)

~~~diff
- 005d1d20 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 005d1d20 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 005d1d20 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 005d1d20 bytes a8831ff8
- 005d1d68 ["COPY", "register:0:8", ["register:4040:8"]]
- 005d1d68 ["INT_ADD", "register:40f0:8", ["const:5d1d68:8", "const:4:8"]]
- 005d1d68 ["CALLIND", null, ["register:0:8"]]
- 005d1d68 bytes 00013fd6
- 005d1da4 ["INT_ADD", "register:40f0:8", ["const:5d1da4:8", "const:4:8"]]
- 005d1da4 ["CALL", null, ["callee:005d2b70:8"]]
+ 005d2154 ["INT_ADD", "register:40f0:8", ["const:5d2154:8", "const:4:8"]]
+ 005d2154 ["CALL", null, ["callee:005d2b70:8"]]
- 005d1da4 bytes 87020094
+ 005d2154 bytes 87020094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bea42185bfa3b6fd2f1d233a57d9e181"></a>

### [`005d2bf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d2/005d2bf8.md) → [`005d2fa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d2/005d2fa8.md) FUN_005d2fa8

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`005d0690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d0/005d0690.md) [`005d2c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d2/005d2c44.md) [`005d3114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d3/005d3114.md) [`005d33a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d3/005d33a0.md) · 呼出先 4件 [`00c37324`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37324.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c5a880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a880.md)
- 新版 呼出元 4件 [`005d0a40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d0a40.md) [`005d2ff4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d2/005d2ff4.md) [`005d34c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d3/005d34c4.md) [`005d3750`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d3/005d3750.md) · 呼出先 4件 [`00c38318`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38318.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md) [`00c5b850`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b850.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005d2fd4",
      "incomplete_value": true,
      "site": "005d2fdc",
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
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:450:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d2c24",
      "incomplete_value": true,
      "site": "005d2c2c",
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
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:480:8"
              ]
            ]
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
    "new": {
      "definition_site": "005d2fd8",
      "incomplete_value": true,
      "site": "005d2fdc",
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
                "const:c9c000:8"
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
      "definition_site": "005d2c28",
      "incomplete_value": true,
      "site": "005d2c2c",
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
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:488:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005d2fd4",
      "READ",
      [
        "storage",
        "00c9b480",
        null,
        "pointer"
      ]
    ],
    [
      "005d2fd4",
      "PARAM",
      [
        "storage",
        "00c96688",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005d2fd8",
      "READ",
      [
        "storage",
        "00c9b488",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d2fd4",
      "READ",
      [
        "storage",
        "00c9c450",
        null,
        "pointer"
      ]
    ],
    [
      "005d2fd4",
      "PARAM",
      [
        "storage",
        "00c97658",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005d2fd8",
      "READ",
      [
        "storage",
        "00c9c458",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d2c2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d2/005d2bf8.md#insn-005d2c2c) · [`005d2c08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d2/005d2bf8.md#insn-005d2c08) · [`005d2c14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d2/005d2bf8.md#insn-005d2c14)
- 新版 [`005d2fdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d2/005d2fa8.md#insn-005d2fdc) · [`005d2fb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d2/005d2fa8.md#insn-005d2fb8) · [`005d2fc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d2/005d2fa8.md#insn-005d2fc4)

~~~diff
- 005d2c2c ["INT_ADD", "register:40f0:8", ["const:5d2c2c:8", "const:4:8"]]
- 005d2c2c ["CALL", null, ["callee:00c58fb0:8"]]
+ 005d2fdc ["INT_ADD", "register:40f0:8", ["const:5d2fdc:8", "const:4:8"]]
+ 005d2fdc ["CALL", null, ["callee:00c58fb0:8"]]
- 005d2c2c bytes ed141a94
+ 005d2fdc bytes f5171a94
- 005d2c08 ["INT_ADD", "register:40f0:8", ["const:5d2c08:8", "const:4:8"]]
- 005d2c08 ["CALL", null, ["callee:00c58f90:8"]]
+ 005d2fb8 ["INT_ADD", "register:40f0:8", ["const:5d2fb8:8", "const:4:8"]]
+ 005d2fb8 ["CALL", null, ["callee:00c58f90:8"]]
- 005d2c08 bytes ee141a94
+ 005d2fb8 bytes f6171a94
- 005d2c14 ["INT_ADD", "register:40f0:8", ["const:5d2c14:8", "const:4:8"]]
- 005d2c14 ["CALL", null, ["callee:00c5b850:8"]]
+ 005d2fc4 ["INT_ADD", "register:40f0:8", ["const:5d2fc4:8", "const:4:8"]]
+ 005d2fc4 ["CALL", null, ["callee:00c5b850:8"]]
- 005d2c14 bytes 1b1f1a94
+ 005d2fc4 bytes 23221a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9599d9e429e5e3693c759b5b3468524e"></a>

### [`005d3ea4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d3/005d3ea4.md) → [`005d4254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d4/005d4254.md) FUN_005d4254

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005d3114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d3/005d3114.md) [`005d33a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d3/005d33a0.md) · 呼出先 4件 [`00c37324`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37324.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c5a880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a880.md)
- 新版 呼出元 2件 [`005d34c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d3/005d34c4.md) [`005d3750`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d3/005d3750.md) · 呼出先 4件 [`00c38318`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38318.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md) [`00c5b850`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b850.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005d4280",
      "incomplete_value": true,
      "site": "005d4288",
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
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:450:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d3ed0",
      "incomplete_value": true,
      "site": "005d3ed8",
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
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:480:8"
              ]
            ]
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
    "new": {
      "definition_site": "005d4284",
      "incomplete_value": true,
      "site": "005d4288",
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
                "const:c9c000:8"
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
      "definition_site": "005d3ed4",
      "incomplete_value": true,
      "site": "005d3ed8",
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
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:488:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005d4280",
      "READ",
      [
        "storage",
        "00c9b480",
        null,
        "pointer"
      ]
    ],
    [
      "005d4280",
      "PARAM",
      [
        "storage",
        "00c96688",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005d4284",
      "READ",
      [
        "storage",
        "00c9b488",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d4280",
      "READ",
      [
        "storage",
        "00c9c450",
        null,
        "pointer"
      ]
    ],
    [
      "005d4280",
      "PARAM",
      [
        "storage",
        "00c97658",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005d4284",
      "READ",
      [
        "storage",
        "00c9c458",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d3ed8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d3/005d3ea4.md#insn-005d3ed8) · [`005d3eb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d3/005d3ea4.md#insn-005d3eb4) · [`005d3ec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d3/005d3ea4.md#insn-005d3ec0)
- 新版 [`005d4288`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d4/005d4254.md#insn-005d4288) · [`005d4264`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d4/005d4254.md#insn-005d4264) · [`005d4270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d4/005d4254.md#insn-005d4270)

~~~diff
- 005d3ed8 ["INT_ADD", "register:40f0:8", ["const:5d3ed8:8", "const:4:8"]]
- 005d3ed8 ["CALL", null, ["callee:00c58fb0:8"]]
+ 005d4288 ["INT_ADD", "register:40f0:8", ["const:5d4288:8", "const:4:8"]]
+ 005d4288 ["CALL", null, ["callee:00c58fb0:8"]]
- 005d3ed8 bytes 42101a94
+ 005d4288 bytes 4a131a94
- 005d3eb4 ["INT_ADD", "register:40f0:8", ["const:5d3eb4:8", "const:4:8"]]
- 005d3eb4 ["CALL", null, ["callee:00c58f90:8"]]
+ 005d4264 ["INT_ADD", "register:40f0:8", ["const:5d4264:8", "const:4:8"]]
+ 005d4264 ["CALL", null, ["callee:00c58f90:8"]]
- 005d3eb4 bytes 43101a94
+ 005d4264 bytes 4b131a94
- 005d3ec0 ["INT_ADD", "register:40f0:8", ["const:5d3ec0:8", "const:4:8"]]
- 005d3ec0 ["CALL", null, ["callee:00c5b850:8"]]
+ 005d4270 ["INT_ADD", "register:40f0:8", ["const:5d4270:8", "const:4:8"]]
+ 005d4270 ["CALL", null, ["callee:00c5b850:8"]]
- 005d3ec0 bytes 701a1a94
+ 005d4270 bytes 781d1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5950c1f16b158390361694a85fa63f2c"></a>

### [`005d437c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d4/005d437c.md) → [`005d472c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d4/005d472c.md) FUN_005d472c

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005d2c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d2/005d2c44.md) · 呼出先 4件 [`00c37324`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37324.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c5a880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a880.md)
- 新版 呼出元 1件 [`005d2ff4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d2/005d2ff4.md) · 呼出先 4件 [`00c38318`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38318.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md) [`00c5b850`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b850.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005d4758",
      "incomplete_value": true,
      "site": "005d4760",
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
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:450:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d43a8",
      "incomplete_value": true,
      "site": "005d43b0",
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
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:480:8"
              ]
            ]
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
    "new": {
      "definition_site": "005d475c",
      "incomplete_value": true,
      "site": "005d4760",
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
                "const:c9c000:8"
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
      "definition_site": "005d43ac",
      "incomplete_value": true,
      "site": "005d43b0",
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
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:488:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005d4758",
      "READ",
      [
        "storage",
        "00c9b480",
        null,
        "pointer"
      ]
    ],
    [
      "005d4758",
      "PARAM",
      [
        "storage",
        "00c96688",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005d475c",
      "READ",
      [
        "storage",
        "00c9b488",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d4758",
      "READ",
      [
        "storage",
        "00c9c450",
        null,
        "pointer"
      ]
    ],
    [
      "005d4758",
      "PARAM",
      [
        "storage",
        "00c97658",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005d475c",
      "READ",
      [
        "storage",
        "00c9c458",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d43b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d4/005d437c.md#insn-005d43b0) · [`005d438c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d4/005d437c.md#insn-005d438c) · [`005d4398`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d4/005d437c.md#insn-005d4398)
- 新版 [`005d4760`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d4/005d472c.md#insn-005d4760) · [`005d473c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d4/005d472c.md#insn-005d473c) · [`005d4748`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d4/005d472c.md#insn-005d4748)

~~~diff
- 005d43b0 ["INT_ADD", "register:40f0:8", ["const:5d43b0:8", "const:4:8"]]
- 005d43b0 ["CALL", null, ["callee:00c58fb0:8"]]
+ 005d4760 ["INT_ADD", "register:40f0:8", ["const:5d4760:8", "const:4:8"]]
+ 005d4760 ["CALL", null, ["callee:00c58fb0:8"]]
- 005d43b0 bytes 0c0f1a94
+ 005d4760 bytes 14121a94
- 005d438c ["INT_ADD", "register:40f0:8", ["const:5d438c:8", "const:4:8"]]
- 005d438c ["CALL", null, ["callee:00c58f90:8"]]
+ 005d473c ["INT_ADD", "register:40f0:8", ["const:5d473c:8", "const:4:8"]]
+ 005d473c ["CALL", null, ["callee:00c58f90:8"]]
- 005d438c bytes 0d0f1a94
+ 005d473c bytes 15121a94
- 005d4398 ["INT_ADD", "register:40f0:8", ["const:5d4398:8", "const:4:8"]]
- 005d4398 ["CALL", null, ["callee:00c5b850:8"]]
+ 005d4748 ["INT_ADD", "register:40f0:8", ["const:5d4748:8", "const:4:8"]]
+ 005d4748 ["CALL", null, ["callee:00c5b850:8"]]
- 005d4398 bytes 3a191a94
+ 005d4748 bytes 421c1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b660b901a1928603e1f18e6ef8a06f7d"></a>

### [`005d487c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d4/005d487c.md) → [`005d4c2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d4/005d4c2c.md) FUN_005d4c2c

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005d37c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d3/005d37c8.md) · 呼出先 4件 [`00c37324`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37324.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c5a880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a880.md)
- 新版 呼出元 1件 [`005d3b78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d3/005d3b78.md) · 呼出先 4件 [`00c38318`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38318.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md) [`00c5b850`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b850.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005d4c58",
      "incomplete_value": true,
      "site": "005d4c60",
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
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:450:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d48a8",
      "incomplete_value": true,
      "site": "005d48b0",
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
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:480:8"
              ]
            ]
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
    "new": {
      "definition_site": "005d4c5c",
      "incomplete_value": true,
      "site": "005d4c60",
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
                "const:c9c000:8"
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
      "definition_site": "005d48ac",
      "incomplete_value": true,
      "site": "005d48b0",
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
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:488:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005d4c58",
      "READ",
      [
        "storage",
        "00c9b480",
        null,
        "pointer"
      ]
    ],
    [
      "005d4c58",
      "PARAM",
      [
        "storage",
        "00c96688",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005d4c5c",
      "READ",
      [
        "storage",
        "00c9b488",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d4c58",
      "READ",
      [
        "storage",
        "00c9c450",
        null,
        "pointer"
      ]
    ],
    [
      "005d4c58",
      "PARAM",
      [
        "storage",
        "00c97658",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005d4c5c",
      "READ",
      [
        "storage",
        "00c9c458",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d48b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d4/005d487c.md#insn-005d48b0) · [`005d488c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d4/005d487c.md#insn-005d488c) · [`005d4898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d4/005d487c.md#insn-005d4898)
- 新版 [`005d4c60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d4/005d4c2c.md#insn-005d4c60) · [`005d4c3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d4/005d4c2c.md#insn-005d4c3c) · [`005d4c48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d4/005d4c2c.md#insn-005d4c48)

~~~diff
- 005d48b0 ["INT_ADD", "register:40f0:8", ["const:5d48b0:8", "const:4:8"]]
- 005d48b0 ["CALL", null, ["callee:00c58fb0:8"]]
+ 005d4c60 ["INT_ADD", "register:40f0:8", ["const:5d4c60:8", "const:4:8"]]
+ 005d4c60 ["CALL", null, ["callee:00c58fb0:8"]]
- 005d48b0 bytes cc0d1a94
+ 005d4c60 bytes d4101a94
- 005d488c ["INT_ADD", "register:40f0:8", ["const:5d488c:8", "const:4:8"]]
- 005d488c ["CALL", null, ["callee:00c58f90:8"]]
+ 005d4c3c ["INT_ADD", "register:40f0:8", ["const:5d4c3c:8", "const:4:8"]]
+ 005d4c3c ["CALL", null, ["callee:00c58f90:8"]]
- 005d488c bytes cd0d1a94
+ 005d4c3c bytes d5101a94
- 005d4898 ["INT_ADD", "register:40f0:8", ["const:5d4898:8", "const:4:8"]]
- 005d4898 ["CALL", null, ["callee:00c5b850:8"]]
+ 005d4c48 ["INT_ADD", "register:40f0:8", ["const:5d4c48:8", "const:4:8"]]
+ 005d4c48 ["CALL", null, ["callee:00c5b850:8"]]
- 005d4898 bytes fa171a94
+ 005d4c48 bytes 021b1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6f05b51bd0aa3033e08096b1481c722"></a>

### [`005d4a68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d4/005d4a68.md) → [`005d4e18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d4/005d4e18.md) FUN_005d4e18

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005d48c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d4/005d48c8.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 1件 [`005d4c78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d4/005d4c78.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "005d4e24",
      "incomplete_value": false,
      "site": "005d4e28",
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
      "definition_site": "005d4a74",
      "incomplete_value": false,
      "site": "005d4a78",
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
      "005d4e24",
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
      "005d4e24",
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

- 旧版 [`005d4a78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d4/005d4a68.md#insn-005d4a78) · [`005d4a70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d4/005d4a68.md#insn-005d4a70) · [`005d4a74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d4/005d4a68.md#insn-005d4a74)
- 新版 [`005d4e28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d4/005d4e18.md#insn-005d4e28) · [`005d4e20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d4/005d4e18.md#insn-005d4e20) · [`005d4e24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d4/005d4e18.md#insn-005d4e24)

~~~diff
- 005d4a78 ["INT_ADD", "register:40f0:8", ["const:5d4a78:8", "const:4:8"]]
- 005d4a78 ["CALL", null, ["callee:0043bad8:8"]]
+ 005d4e28 ["INT_ADD", "register:40f0:8", ["const:5d4e28:8", "const:4:8"]]
+ 005d4e28 ["CALL", null, ["callee:0043bad8:8"]]
- 005d4a78 bytes 509bf997
+ 005d4e28 bytes 2c9bf997
- 005d4a70 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 005d4e20 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 005d4a70 bytes 00e7fff0
+ 005d4e20 bytes 20e7ff90
- 005d4a74 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 005d4a74 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005d4a74 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005d4a74 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005d4e24 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 005d4e24 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005d4e24 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005d4e24 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005d4a74 bytes 00303e91
+ 005d4e24 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a79bd63cb7ffc79ed3c71d574c2943a9"></a>

### [`005d4a7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d4/005d4a7c.md) → [`005d4e2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d4/005d4e2c.md) FUN_005d4e2c

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005d3c98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d3/005d3c98.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 1件 [`005d4048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d4/005d4048.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "005d4e38",
      "incomplete_value": false,
      "site": "005d4e3c",
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
      "definition_site": "005d4a88",
      "incomplete_value": false,
      "site": "005d4a8c",
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
      "005d4e38",
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
      "005d4e38",
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

- 旧版 [`005d4a8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d4/005d4a7c.md#insn-005d4a8c) · [`005d4a84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d4/005d4a7c.md#insn-005d4a84) · [`005d4a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d4/005d4a7c.md#insn-005d4a88)
- 新版 [`005d4e3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d4/005d4e2c.md#insn-005d4e3c) · [`005d4e34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d4/005d4e2c.md#insn-005d4e34) · [`005d4e38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d4/005d4e2c.md#insn-005d4e38)

~~~diff
- 005d4a8c ["INT_ADD", "register:40f0:8", ["const:5d4a8c:8", "const:4:8"]]
- 005d4a8c ["CALL", null, ["callee:0043bad8:8"]]
+ 005d4e3c ["INT_ADD", "register:40f0:8", ["const:5d4e3c:8", "const:4:8"]]
+ 005d4e3c ["CALL", null, ["callee:0043bad8:8"]]
- 005d4a8c bytes 4b9bf997
+ 005d4e3c bytes 279bf997
- 005d4a84 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 005d4e34 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 005d4a84 bytes 00e7fff0
+ 005d4e34 bytes 20e7ff90
- 005d4a88 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 005d4a88 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005d4a88 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005d4a88 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005d4e38 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 005d4e38 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005d4e38 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005d4e38 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005d4a88 bytes 00303e91
+ 005d4e38 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e8d4312bda5c10d441ca35081b2d742"></a>

### [`005d4b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d4/005d4b88.md) → [`005d4f38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d4/005d4f38.md) FUN_005d4f38

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005cec5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005cec5c.md) [`005d5448`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d5/005d5448.md) · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 2件 [`005cf00c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cf/005cf00c.md) [`005d57f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d5/005d57f8.md) · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "005d4f90",
      "incomplete_value": true,
      "site": "005d4f90",
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
      "definition_site": "005d4be0",
      "incomplete_value": true,
      "site": "005d4be0",
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
      "definition_site": "005d4fc4",
      "incomplete_value": true,
      "site": "005d4fc4",
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
      "definition_site": "005d4c14",
      "incomplete_value": true,
      "site": "005d4c14",
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
      "definition_site": "005d4ff4",
      "incomplete_value": true,
      "site": "005d4ffc",
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
      "definition_site": "005d4c44",
      "incomplete_value": true,
      "site": "005d4c4c",
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
      "005d4f84",
      "READ",
      [
        "storage",
        "00c9b458",
        null,
        "pointer"
      ]
    ],
    [
      "005d4f90",
      "DATA",
      [
        "storage",
        "00c70c10",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d4fac",
      "READ",
      [
        "storage",
        "00c9b508",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d4f84",
      "READ",
      [
        "storage",
        "00c9c428",
        null,
        "pointer"
      ]
    ],
    [
      "005d4f90",
      "DATA",
      [
        "storage",
        "00c71be0",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d4fac",
      "READ",
      [
        "storage",
        "00c9c4d8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d4bc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d4/005d4b88.md#insn-005d4bc4) · [`005d4bcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d4/005d4b88.md#insn-005d4bcc) · [`005d4bd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d4/005d4b88.md#insn-005d4bd4)
- 新版 [`005d4f74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d4/005d4f38.md#insn-005d4f74) · [`005d4f7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d4/005d4f38.md#insn-005d4f7c) · [`005d4f84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d4/005d4f38.md#insn-005d4f84)

~~~diff
- 005d4bc4 ["INT_ADD", "register:40f0:8", ["const:5d4bc4:8", "const:4:8"]]
- 005d4bc4 ["CALL", null, ["callee:00c58f30:8"]]
+ 005d4f74 ["INT_ADD", "register:40f0:8", ["const:5d4f74:8", "const:4:8"]]
+ 005d4f74 ["CALL", null, ["callee:00c58f30:8"]]
- 005d4bc4 bytes e70c1a94
+ 005d4f74 bytes ef0f1a94
- 005d4bcc ["COPY", "register:4048:8", ["const:c9b000:8"]]
+ 005d4f7c ["COPY", "register:4048:8", ["const:c9c000:8"]]
- 005d4bcc bytes 293600f0
+ 005d4f7c bytes 49360090
- 005d4bd4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:458:8"]]
- 005d4bd4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005d4f84 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:428:8"]]
+ 005d4f84 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005d4bd4 bytes 292d42f9
+ 005d4f84 bytes 291542f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00227b5f592447884da57fb4a59aa167"></a>

### [`005d4cc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d4/005d4cc8.md) → [`005d5078`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d5/005d5078.md) FUN_005d5078

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005cec5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005cec5c.md) [`005d5448`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d5/005d5448.md) · 呼出先 4件 [`00c37324`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37324.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c5a880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a880.md)
- 新版 呼出元 2件 [`005cf00c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cf/005cf00c.md) [`005d57f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d5/005d57f8.md) · 呼出先 4件 [`00c38318`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38318.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md) [`00c5b850`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b850.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005d50a4",
      "incomplete_value": true,
      "site": "005d50ac",
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
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:450:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d4cf4",
      "incomplete_value": true,
      "site": "005d4cfc",
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
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:480:8"
              ]
            ]
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
    "new": {
      "definition_site": "005d50a8",
      "incomplete_value": true,
      "site": "005d50ac",
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
                "const:c9c000:8"
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
      "definition_site": "005d4cf8",
      "incomplete_value": true,
      "site": "005d4cfc",
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
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:488:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005d50a4",
      "READ",
      [
        "storage",
        "00c9b480",
        null,
        "pointer"
      ]
    ],
    [
      "005d50a4",
      "PARAM",
      [
        "storage",
        "00c96688",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005d50a8",
      "READ",
      [
        "storage",
        "00c9b488",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d50a4",
      "READ",
      [
        "storage",
        "00c9c450",
        null,
        "pointer"
      ]
    ],
    [
      "005d50a4",
      "PARAM",
      [
        "storage",
        "00c97658",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005d50a8",
      "READ",
      [
        "storage",
        "00c9c458",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d4cfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d4/005d4cc8.md#insn-005d4cfc) · [`005d4cd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d4/005d4cc8.md#insn-005d4cd8) · [`005d4ce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d4/005d4cc8.md#insn-005d4ce4)
- 新版 [`005d50ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d5/005d5078.md#insn-005d50ac) · [`005d5088`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d5/005d5078.md#insn-005d5088) · [`005d5094`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d5/005d5078.md#insn-005d5094)

~~~diff
- 005d4cfc ["INT_ADD", "register:40f0:8", ["const:5d4cfc:8", "const:4:8"]]
- 005d4cfc ["CALL", null, ["callee:00c58fb0:8"]]
+ 005d50ac ["INT_ADD", "register:40f0:8", ["const:5d50ac:8", "const:4:8"]]
+ 005d50ac ["CALL", null, ["callee:00c58fb0:8"]]
- 005d4cfc bytes b90c1a94
+ 005d50ac bytes c10f1a94
- 005d4cd8 ["INT_ADD", "register:40f0:8", ["const:5d4cd8:8", "const:4:8"]]
- 005d4cd8 ["CALL", null, ["callee:00c58f90:8"]]
+ 005d5088 ["INT_ADD", "register:40f0:8", ["const:5d5088:8", "const:4:8"]]
+ 005d5088 ["CALL", null, ["callee:00c58f90:8"]]
- 005d4cd8 bytes ba0c1a94
+ 005d5088 bytes c20f1a94
- 005d4ce4 ["INT_ADD", "register:40f0:8", ["const:5d4ce4:8", "const:4:8"]]
- 005d4ce4 ["CALL", null, ["callee:00c5b850:8"]]
+ 005d5094 ["INT_ADD", "register:40f0:8", ["const:5d5094:8", "const:4:8"]]
+ 005d5094 ["CALL", null, ["callee:00c5b850:8"]]
- 005d4ce4 bytes e7161a94
+ 005d5094 bytes ef191a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0293baf36ef728a31a438ea021fe4341"></a>

### [`005d4d14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d4/005d4d14.md) → [`005d50c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d5/005d50c4.md) FUN_005d50c4

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005cec5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ce/005cec5c.md) [`005d5448`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d5/005d5448.md) · 呼出先 4件 [`00c37324`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37324.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c5a880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a880.md)
- 新版 呼出元 2件 [`005cf00c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cf/005cf00c.md) [`005d57f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d5/005d57f8.md) · 呼出先 4件 [`00c38318`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38318.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md) [`00c5b850`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b850.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005d50f0",
      "incomplete_value": true,
      "site": "005d50f8",
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
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:450:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d4d40",
      "incomplete_value": true,
      "site": "005d4d48",
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
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:480:8"
              ]
            ]
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
    "new": {
      "definition_site": "005d50f4",
      "incomplete_value": true,
      "site": "005d50f8",
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
                "const:c9c000:8"
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
      "definition_site": "005d4d44",
      "incomplete_value": true,
      "site": "005d4d48",
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
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:488:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005d50f0",
      "READ",
      [
        "storage",
        "00c9b480",
        null,
        "pointer"
      ]
    ],
    [
      "005d50f0",
      "PARAM",
      [
        "storage",
        "00c96688",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005d50f4",
      "READ",
      [
        "storage",
        "00c9b488",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d50f0",
      "READ",
      [
        "storage",
        "00c9c450",
        null,
        "pointer"
      ]
    ],
    [
      "005d50f0",
      "PARAM",
      [
        "storage",
        "00c97658",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005d50f4",
      "READ",
      [
        "storage",
        "00c9c458",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d4d48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d4/005d4d14.md#insn-005d4d48) · [`005d4d24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d4/005d4d14.md#insn-005d4d24) · [`005d4d30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d4/005d4d14.md#insn-005d4d30)
- 新版 [`005d50f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d5/005d50c4.md#insn-005d50f8) · [`005d50d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d5/005d50c4.md#insn-005d50d4) · [`005d50e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d5/005d50c4.md#insn-005d50e0)

~~~diff
- 005d4d48 ["INT_ADD", "register:40f0:8", ["const:5d4d48:8", "const:4:8"]]
- 005d4d48 ["CALL", null, ["callee:00c58fb0:8"]]
+ 005d50f8 ["INT_ADD", "register:40f0:8", ["const:5d50f8:8", "const:4:8"]]
+ 005d50f8 ["CALL", null, ["callee:00c58fb0:8"]]
- 005d4d48 bytes a60c1a94
+ 005d50f8 bytes ae0f1a94
- 005d4d24 ["INT_ADD", "register:40f0:8", ["const:5d4d24:8", "const:4:8"]]
- 005d4d24 ["CALL", null, ["callee:00c58f90:8"]]
+ 005d50d4 ["INT_ADD", "register:40f0:8", ["const:5d50d4:8", "const:4:8"]]
+ 005d50d4 ["CALL", null, ["callee:00c58f90:8"]]
- 005d4d24 bytes a70c1a94
+ 005d50d4 bytes af0f1a94
- 005d4d30 ["INT_ADD", "register:40f0:8", ["const:5d4d30:8", "const:4:8"]]
- 005d4d30 ["CALL", null, ["callee:00c5b850:8"]]
+ 005d50e0 ["INT_ADD", "register:40f0:8", ["const:5d50e0:8", "const:4:8"]]
+ 005d50e0 ["CALL", null, ["callee:00c5b850:8"]]
- 005d4d30 bytes d4161a94
+ 005d50e0 bytes dc191a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4cfceb02257a85b4c4da8ebd83e25ca"></a>

### [`005d4d60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d4/005d4d60.md) → [`005d5110`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d5/005d5110.md) FUN_005d5110

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

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
      "definition_site": "005d512c",
      "incomplete_value": true,
      "site": "005d5130",
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
      "definition_site": "005d4d7c",
      "incomplete_value": true,
      "site": "005d4d80",
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
      "definition_site": "005d5150",
      "incomplete_value": true,
      "site": "005d5154",
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
      "definition_site": "005d4da0",
      "incomplete_value": true,
      "site": "005d4da4",
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
      "005d5124",
      "READ",
      [
        "storage",
        "00c9b518",
        null,
        "pointer"
      ]
    ],
    [
      "005d5130",
      "DATA",
      [
        "storage",
        "00c71108",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d5148",
      "READ",
      [
        "storage",
        "00c9b478",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d5124",
      "READ",
      [
        "storage",
        "00c9c4e8",
        null,
        "pointer"
      ]
    ],
    [
      "005d5130",
      "DATA",
      [
        "storage",
        "00c720d8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d5148",
      "READ",
      [
        "storage",
        "00c9c448",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d4d6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d4/005d4d60.md#insn-005d4d6c) · [`005d4d74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d4/005d4d60.md#insn-005d4d74) · [`005d4d90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d4/005d4d60.md#insn-005d4d90)
- 新版 [`005d511c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d5/005d5110.md#insn-005d511c) · [`005d5124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d5/005d5110.md#insn-005d5124) · [`005d5140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d5/005d5110.md#insn-005d5140)

~~~diff
- 005d4d6c ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 005d511c ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 005d4d6c bytes 283600f0
+ 005d511c bytes 283600f0
- 005d4d74 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:518:8"]]
- 005d4d74 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005d5124 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4e8:8"]]
+ 005d5124 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005d4d74 bytes 088d42f9
+ 005d5124 bytes 087542f9
- 005d4d90 ["COPY", "register:0:8", ["register:4040:8"]]
- 005d4d90 ["INT_ADD", "register:40f0:8", ["const:5d4d90:8", "const:4:8"]]
- 005d4d90 ["CALLIND", null, ["register:0:8"]]
+ 005d5140 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005d5140 ["INT_ADD", "register:40f0:8", ["const:5d5140:8", "const:4:8"]]
+ 005d5140 ["CALLIND", null, ["register:0:8"]]
- 005d4d90 bytes 00013fd6
+ 005d5140 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f174662960c59114069ed51b6e9e0cca"></a>

### [`005d5050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d5/005d5050.md) → [`005d5400`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d5/005d5400.md) FUN_005d5400

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

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
      "definition_site": "005d541c",
      "incomplete_value": true,
      "site": "005d5420",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005d5440",
      "incomplete_value": true,
      "site": "005d5444",
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
      "005d5414",
      "READ",
      [
        "storage",
        "00c9b518",
        null,
        "pointer"
      ]
    ],
    [
      "005d5420",
      "DATA",
      [
        "storage",
        "00c71108",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d5438",
      "READ",
      [
        "storage",
        "00c9b478",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d5414",
      "READ",
      [
        "storage",
        "00c9c4e8",
        null,
        "pointer"
      ]
    ],
    [
      "005d5420",
      "DATA",
      [
        "storage",
        "00c720d8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d5438",
      "READ",
      [
        "storage",
        "00c9c448",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d505c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d5/005d5050.md#insn-005d505c) · [`005d5064`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d5/005d5050.md#insn-005d5064) · [`005d5080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d5/005d5050.md#insn-005d5080)
- 新版 [`005d540c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d5/005d5400.md#insn-005d540c) · [`005d5414`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d5/005d5400.md#insn-005d5414) · [`005d5430`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d5/005d5400.md#insn-005d5430)

~~~diff
- 005d505c ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 005d540c ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 005d505c bytes 283600d0
+ 005d540c bytes 283600f0
- 005d5064 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:518:8"]]
- 005d5064 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005d5414 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4e8:8"]]
+ 005d5414 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005d5064 bytes 088d42f9
+ 005d5414 bytes 087542f9
- 005d5080 ["COPY", "register:0:8", ["register:4040:8"]]
- 005d5080 ["INT_ADD", "register:40f0:8", ["const:5d5080:8", "const:4:8"]]
- 005d5080 ["CALLIND", null, ["register:0:8"]]
+ 005d5430 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005d5430 ["INT_ADD", "register:40f0:8", ["const:5d5430:8", "const:4:8"]]
+ 005d5430 ["CALLIND", null, ["register:0:8"]]
- 005d5080 bytes 00013fd6
+ 005d5430 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7786826f3be2fc48856e281bb9c5a68"></a>

### [`005d50d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d5/005d50d0.md) → [`005d5480`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d5/005d5480.md) FUN_005d5480

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "005d549c",
      "incomplete_value": true,
      "site": "005d54a0",
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
      "definition_site": "005d50ec",
      "incomplete_value": true,
      "site": "005d50f0",
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
      "definition_site": "005d54c0",
      "incomplete_value": true,
      "site": "005d54c4",
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
      "definition_site": "005d5110",
      "incomplete_value": true,
      "site": "005d5114",
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
      "005d5494",
      "READ",
      [
        "storage",
        "00c9b518",
        null,
        "pointer"
      ]
    ],
    [
      "005d54a0",
      "DATA",
      [
        "storage",
        "00c71108",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d54b8",
      "READ",
      [
        "storage",
        "00c9b478",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d5494",
      "READ",
      [
        "storage",
        "00c9c4e8",
        null,
        "pointer"
      ]
    ],
    [
      "005d54a0",
      "DATA",
      [
        "storage",
        "00c720d8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d54b8",
      "READ",
      [
        "storage",
        "00c9c448",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d50dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d5/005d50d0.md#insn-005d50dc) · [`005d50e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d5/005d50d0.md#insn-005d50e4) · [`005d5100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d5/005d50d0.md#insn-005d5100)
- 新版 [`005d548c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d5/005d5480.md#insn-005d548c) · [`005d5494`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d5/005d5480.md#insn-005d5494) · [`005d54b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d5/005d5480.md#insn-005d54b0)

~~~diff
- 005d50dc ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 005d548c ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 005d50dc bytes 283600d0
+ 005d548c bytes 283600f0
- 005d50e4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:518:8"]]
- 005d50e4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005d5494 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4e8:8"]]
+ 005d5494 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005d50e4 bytes 088d42f9
+ 005d5494 bytes 087542f9
- 005d5100 ["COPY", "register:0:8", ["register:4040:8"]]
- 005d5100 ["INT_ADD", "register:40f0:8", ["const:5d5100:8", "const:4:8"]]
- 005d5100 ["CALLIND", null, ["register:0:8"]]
+ 005d54b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005d54b0 ["INT_ADD", "register:40f0:8", ["const:5d54b0:8", "const:4:8"]]
+ 005d54b0 ["CALLIND", null, ["register:0:8"]]
- 005d5100 bytes 00013fd6
+ 005d54b0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25a10eedefef4452ee668f500efb973f"></a>

### [`005d513c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d5/005d513c.md) → [`005d54ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d5/005d54ec.md) FUN_005d54ec

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

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
      "definition_site": "005d5508",
      "incomplete_value": true,
      "site": "005d550c",
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
      "definition_site": "005d5158",
      "incomplete_value": true,
      "site": "005d515c",
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
      "definition_site": "005d552c",
      "incomplete_value": true,
      "site": "005d5530",
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
      "definition_site": "005d517c",
      "incomplete_value": true,
      "site": "005d5180",
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
      "005d5500",
      "READ",
      [
        "storage",
        "00c9b518",
        null,
        "pointer"
      ]
    ],
    [
      "005d550c",
      "DATA",
      [
        "storage",
        "00c71108",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d5524",
      "READ",
      [
        "storage",
        "00c9b478",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d5500",
      "READ",
      [
        "storage",
        "00c9c4e8",
        null,
        "pointer"
      ]
    ],
    [
      "005d550c",
      "DATA",
      [
        "storage",
        "00c720d8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d5524",
      "READ",
      [
        "storage",
        "00c9c448",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d5148`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d5/005d513c.md#insn-005d5148) · [`005d5150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d5/005d513c.md#insn-005d5150) · [`005d516c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d5/005d513c.md#insn-005d516c)
- 新版 [`005d54f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d5/005d54ec.md#insn-005d54f8) · [`005d5500`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d5/005d54ec.md#insn-005d5500) · [`005d551c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d5/005d54ec.md#insn-005d551c)

~~~diff
- 005d5148 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 005d54f8 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 005d5148 bytes 283600d0
+ 005d54f8 bytes 283600f0
- 005d5150 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:518:8"]]
- 005d5150 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005d5500 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4e8:8"]]
+ 005d5500 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005d5150 bytes 088d42f9
+ 005d5500 bytes 087542f9
- 005d516c ["COPY", "register:0:8", ["register:4040:8"]]
- 005d516c ["INT_ADD", "register:40f0:8", ["const:5d516c:8", "const:4:8"]]
- 005d516c ["CALLIND", null, ["register:0:8"]]
+ 005d551c ["COPY", "register:0:8", ["register:4040:8"]]
+ 005d551c ["INT_ADD", "register:40f0:8", ["const:5d551c:8", "const:4:8"]]
+ 005d551c ["CALLIND", null, ["register:0:8"]]
- 005d516c bytes 00013fd6
+ 005d551c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc625241c30b871a85444c4941717e35"></a>

### [`005d51f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d5/005d51f0.md) → [`005d55a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d5/005d55a0.md) FUN_005d55a0

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005cdd40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cdd40.md) [`005cdecc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cdecc.md) · 呼出先 4件 [`00c37324`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37324.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c5a880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a880.md)
- 新版 呼出元 2件 [`005ce0f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ce/005ce0f0.md) [`005ce27c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ce/005ce27c.md) · 呼出先 4件 [`00c38318`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c38/00c38318.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md) [`00c5b850`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b850.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005d55cc",
      "incomplete_value": true,
      "site": "005d55d4",
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
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:450:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d521c",
      "incomplete_value": true,
      "site": "005d5224",
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
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:480:8"
              ]
            ]
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
    "new": {
      "definition_site": "005d55d0",
      "incomplete_value": true,
      "site": "005d55d4",
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
                "const:c9c000:8"
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
      "definition_site": "005d5220",
      "incomplete_value": true,
      "site": "005d5224",
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
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:488:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005d55cc",
      "READ",
      [
        "storage",
        "00c9b480",
        null,
        "pointer"
      ]
    ],
    [
      "005d55cc",
      "PARAM",
      [
        "storage",
        "00c96688",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005d55d0",
      "READ",
      [
        "storage",
        "00c9b488",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d55cc",
      "READ",
      [
        "storage",
        "00c9c450",
        null,
        "pointer"
      ]
    ],
    [
      "005d55cc",
      "PARAM",
      [
        "storage",
        "00c97658",
        "_ZTINSt6__ndk111regex_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005d55d0",
      "READ",
      [
        "storage",
        "00c9c458",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d5224`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d5/005d51f0.md#insn-005d5224) · [`005d5200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d5/005d51f0.md#insn-005d5200) · [`005d520c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d5/005d51f0.md#insn-005d520c)
- 新版 [`005d55d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d5/005d55a0.md#insn-005d55d4) · [`005d55b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d5/005d55a0.md#insn-005d55b0) · [`005d55bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d5/005d55a0.md#insn-005d55bc)

~~~diff
- 005d5224 ["INT_ADD", "register:40f0:8", ["const:5d5224:8", "const:4:8"]]
- 005d5224 ["CALL", null, ["callee:00c58fb0:8"]]
+ 005d55d4 ["INT_ADD", "register:40f0:8", ["const:5d55d4:8", "const:4:8"]]
+ 005d55d4 ["CALL", null, ["callee:00c58fb0:8"]]
- 005d5224 bytes 6f0b1a94
+ 005d55d4 bytes 770e1a94
- 005d5200 ["INT_ADD", "register:40f0:8", ["const:5d5200:8", "const:4:8"]]
- 005d5200 ["CALL", null, ["callee:00c58f90:8"]]
+ 005d55b0 ["INT_ADD", "register:40f0:8", ["const:5d55b0:8", "const:4:8"]]
+ 005d55b0 ["CALL", null, ["callee:00c58f90:8"]]
- 005d5200 bytes 700b1a94
+ 005d55b0 bytes 780e1a94
- 005d520c ["INT_ADD", "register:40f0:8", ["const:5d520c:8", "const:4:8"]]
- 005d520c ["CALL", null, ["callee:00c5b850:8"]]
+ 005d55bc ["INT_ADD", "register:40f0:8", ["const:5d55bc:8", "const:4:8"]]
+ 005d55bc ["CALL", null, ["callee:00c5b850:8"]]
- 005d520c bytes 9d151a94
+ 005d55bc bytes a5181a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0511d7b3ac4e3f178d2c611d55b42eb0"></a>

### [`005d523c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d5/005d523c.md) → [`005d55ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d5/005d55ec.md) FUN_005d55ec

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005cdd40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cdd40.md) [`005d523c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d5/005d523c.md) · 呼出先 7件 [`005cf0dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cf0dc.md) [`005d1038`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d1038.md) [`005d1084`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d1/005d1084.md) [`005d523c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d5/005d523c.md) [`005d5448`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d5/005d5448.md)
- 新版 呼出元 2件 [`005ce0f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ce/005ce0f0.md) [`005d55ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d5/005d55ec.md) · 呼出先 7件 [`005cf48c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005cf/005cf48c.md) [`005d13e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d1/005d13e8.md) [`005d1434`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d1/005d1434.md) [`005d55ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d5/005d55ec.md) [`005d57f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d5/005d57f8.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.42% / 新版 95.42%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005d567c",
      "incomplete_value": true,
      "site": "005d5694",
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
      "definition_site": "005d52cc",
      "incomplete_value": true,
      "site": "005d52e4",
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
      "definition_site": "005d57d0",
      "incomplete_value": true,
      "site": "005d57e0",
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
      "definition_site": "005d5420",
      "incomplete_value": true,
      "site": "005d5430",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005d566c",
      "READ",
      [
        "storage",
        "00c9b4b8",
        null,
        "pointer"
      ]
    ],
    [
      "005d5694",
      "DATA",
      [
        "storage",
        "00c71018",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d57c0",
      "READ",
      [
        "storage",
        "00c9b4c0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005d566c",
      "READ",
      [
        "storage",
        "00c9c488",
        null,
        "pointer"
      ]
    ],
    [
      "005d5694",
      "DATA",
      [
        "storage",
        "00c71fe8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d57c0",
      "READ",
      [
        "storage",
        "00c9c490",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d525c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d5/005d523c.md#insn-005d525c) · [`005d52ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d5/005d523c.md#insn-005d52ac) · [`005d52b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d5/005d523c.md#insn-005d52b4)
- 新版 [`005d560c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d5/005d55ec.md#insn-005d560c) · [`005d565c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d5/005d55ec.md#insn-005d565c) · [`005d5664`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d5/005d55ec.md#insn-005d5664)

~~~diff
- 005d525c ["INT_ADD", "register:40f0:8", ["const:5d525c:8", "const:4:8"]]
- 005d525c ["CALL", null, ["callee:005d5a38:8"]]
+ 005d560c ["INT_ADD", "register:40f0:8", ["const:5d560c:8", "const:4:8"]]
+ 005d560c ["CALL", null, ["callee:005d5a38:8"]]
- 005d525c bytes 0b010094
+ 005d560c bytes 0b010094
- 005d52ac ["INT_ADD", "register:40f0:8", ["const:5d52ac:8", "const:4:8"]]
- 005d52ac ["CALL", null, ["callee:00c58f30:8"]]
+ 005d565c ["INT_ADD", "register:40f0:8", ["const:5d565c:8", "const:4:8"]]
+ 005d565c ["CALL", null, ["callee:00c58f30:8"]]
- 005d52ac bytes 2d0b1a94
+ 005d565c bytes 350e1a94
- 005d52b4 ["COPY", "register:4050:8", ["const:c9b000:8"]]
+ 005d5664 ["COPY", "register:4050:8", ["const:c9c000:8"]]
- 005d52b4 bytes 2a3600d0
+ 005d5664 bytes 2a3600f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9cf2f131db4e9d9a81df7346e8586a31"></a>

### [`005d5798`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d5/005d5798.md) → [`005d5b48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d5/005d5b48.md) FUN_005d5b48

採用 · 移動量 `+0x3b0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "005d5b58",
      "incomplete_value": true,
      "site": "005d5b5c",
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
      "definition_site": "005d57a8",
      "incomplete_value": true,
      "site": "005d57ac",
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
      "005d5b50",
      "READ",
      [
        "storage",
        "00c9b478",
        null,
        "pointer"
      ]
    ],
    [
      "005d5b5c",
      "DATA",
      [
        "storage",
        "00c70c88",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "005d5b50",
      "READ",
      [
        "storage",
        "00c9c448",
        null,
        "pointer"
      ]
    ],
    [
      "005d5b5c",
      "DATA",
      [
        "storage",
        "00c71c58",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d5798`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d5/005d5798.md#insn-005d5798) · [`005d57a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d5/005d5798.md#insn-005d57a0)
- 新版 [`005d5b48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d5/005d5b48.md#insn-005d5b48) · [`005d5b50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d5/005d5b48.md#insn-005d5b50)

~~~diff
- 005d5798 ["COPY", "register:4048:8", ["const:c9b000:8"]]
+ 005d5b48 ["COPY", "register:4048:8", ["const:c9c000:8"]]
- 005d5798 bytes 293600d0
+ 005d5b48 bytes 293600f0
- 005d57a0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:478:8"]]
- 005d57a0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005d5b50 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:448:8"]]
+ 005d5b50 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005d57a0 bytes 293d42f9
+ 005d5b50 bytes 292542f9
~~~


<a id="compare-e2d17eebc3d1af9c62e301c32c871727"></a>

### [`005d6150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d6/005d6150.md) → [`005d6500`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d6/005d6500.md) FUN_005d6500

採用 · 移動量 `+0x3b0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005d5ca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d5/005d5ca0.md) · 呼出先 10件 [`005cfd94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cfd94.md) [`005cfde0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cfde0.md) [`005cff58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cff58.md) [`005d0550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d0/005d0550.md) [`005d7180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d7/005d7180.md)
- 新版 呼出元 1件 [`005d6050`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d6/005d6050.md) · 呼出先 10件 [`005d0144`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d0144.md) [`005d0190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d0190.md) [`005d0308`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d0308.md) [`005d0900`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d0900.md) [`005d7530`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d7/005d7530.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.64% / 新版 99.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005d66f0",
      "incomplete_value": true,
      "site": "005d6700",
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
                "const:480:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005d6340",
      "incomplete_value": true,
      "site": "005d6350",
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
                "const:430:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 51,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005d66f0",
      "READ",
      [
        "storage",
        "002c2430",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005d66f0",
      "READ",
      [
        "storage",
        "002c2480",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d61c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d6/005d6150.md#insn-005d61c8) · [`005d62c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d6/005d6150.md#insn-005d62c8) · [`005d6340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d6/005d6150.md#insn-005d6340)
- 新版 [`005d6578`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d6/005d6500.md#insn-005d6578) · [`005d6678`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d6/005d6500.md#insn-005d6678) · [`005d66f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d6/005d6500.md#insn-005d66f0)

~~~diff
- 005d61c8 ["INT_ADD", "register:40f0:8", ["const:5d61c8:8", "const:4:8"]]
- 005d61c8 ["CALL", null, ["callee:005d75ac:8"]]
+ 005d6578 ["INT_ADD", "register:40f0:8", ["const:5d6578:8", "const:4:8"]]
+ 005d6578 ["CALL", null, ["callee:005d75ac:8"]]
- 005d61c8 bytes 0d040094
+ 005d6578 bytes 0d040094
- 005d62c8 ["INT_ADD", "register:40f0:8", ["const:5d62c8:8", "const:4:8"]]
- 005d62c8 ["CALL", null, ["callee:005d0900:8"]]
+ 005d6678 ["INT_ADD", "register:40f0:8", ["const:5d6678:8", "const:4:8"]]
+ 005d6678 ["CALL", null, ["callee:005d0900:8"]]
- 005d62c8 bytes a2e8ff97
+ 005d6678 bytes a2e8ff97
- 005d6340 ["INT_ADD", "tmp:0:8", ["register:4060:8", "const:430:8"]]
- 005d6340 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
- 005d6340 ["COPY", "register:5010:8", ["const:0:8"]]
- 005d6340 ["COPY", "register:5018:8", ["const:0:8"]]
+ 005d66f0 ["INT_ADD", "tmp:0:8", ["register:4060:8", "const:480:8"]]
+ 005d66f0 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
+ 005d66f0 ["COPY", "register:5010:8", ["const:0:8"]]
+ 005d66f0 ["COPY", "register:5018:8", ["const:0:8"]]
- 005d6340 bytes 800dc13d
+ 005d66f0 bytes 8021c13d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64a5e1d46a71c69e4d9be24dcb71810b"></a>

### [`005d80cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d8/005d80cc.md) → [`005d847c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d8/005d847c.md) FUN_005d847c

採用 · 移動量 `+0x3b0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005d6a30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d6/005d6a30.md) · 呼出先 4件 [`005cfd3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cf/005cfd3c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 1件 [`005d6de0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d6/005d6de0.md) · 呼出先 4件 [`005d00ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d0/005d00ec.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 83.74% / 新版 83.74%

CFGの説明率　旧版 55.00% / 新版 61.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_condition` 1件, `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005d8250"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005d8254"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005d8600"
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
      "unmatched:005d8258",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d85e8"
      ]
    ]
  ],
  "added": [
    [
      "005d8608",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d85e8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d8160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d8/005d80cc.md#insn-005d8160) · [`005d8168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d8/005d80cc.md#insn-005d8168) · [`005d81cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d8/005d80cc.md#insn-005d81cc)
- 新版 [`005d857c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d8/005d847c.md#insn-005d857c)

~~~diff
- 005d8160 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 005d8160 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 005d8160 ["COPY", "tmp:2:8", ["register:4050:8"]]
- 005d8160 ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 005d8160 bytes 4a81839a
- 005d8168 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 005d8168 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 005d8168 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 005d8168 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 005d8168 bytes 4831899a
- 005d81cc ["INT_ADD", "register:40f0:8", ["const:5d81cc:8", "const:4:8"]]
- 005d81cc ["CALL", null, ["callee:00c590a0:8"]]
+ 005d857c ["INT_ADD", "register:40f0:8", ["const:5d857c:8", "const:4:8"]]
+ 005d857c ["CALL", null, ["callee:00c590a0:8"]]
- 005d81cc bytes c1ff1994
+ 005d857c bytes c9021a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

