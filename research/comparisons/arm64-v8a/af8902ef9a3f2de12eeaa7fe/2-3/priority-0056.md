# v16.0.0 → v16.0.1 · 最優先の変更候補 (56)

[一覧の目次](README.md)

<a id="compare-fe5b8d0507835d7d18074fdb50eb54a1"></a>

### [`009b1d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b1/009b1d08.md) → [`009b1ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b1/009b1ea4.md) FUN_009b1ea4

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 69.44% / 新版 69.44%

CFGの説明率　旧版 15.38% / 新版 10.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b1d24"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009b1ec0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "009b1d28"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009b1d24",
      "DATA",
      [
        "storage",
        "00c88700",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:009b1d28",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b1ef0"
      ]
    ],
    [
      "unmatched:009b1d60",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b1f0c"
      ]
    ]
  ],
  "added": [
    [
      "009b1ec0",
      "DATA",
      [
        "storage",
        "00c88b00",
        null,
        "undefined *"
      ]
    ],
    [
      "009b1ec4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b1ef0"
      ]
    ],
    [
      "009b1efc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b1f0c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b1d24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b1/009b1d08.md#insn-009b1d24) · [`009b1d28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b1/009b1d08.md#insn-009b1d28) · [`009b1d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b1/009b1d08.md#insn-009b1d34)
- 新版 `009b1ed0`（命令位置の公開資料なし）

~~~diff
- 009b1d24 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 009b1d24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 009b1d24 bytes 080000f9
- 009b1d28 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 009b1d28 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 009b1d28 bytes 740100b4
- 009b1d34 ["INT_ADD", "register:40f0:8", ["const:9b1d34:8", "const:4:8"]]
- 009b1d34 ["CALL", null, ["callee:00c53d00:8"]]
+ 009b1ed0 ["INT_ADD", "register:40f0:8", ["const:9b1ed0:8", "const:4:8"]]
+ 009b1ed0 ["CALL", null, ["callee:00c53d00:8"]]
- 009b1d34 bytes eb860a94
+ 009b1ed0 bytes 8c870a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca6f6e923b7476a2e27323ea208f5b32"></a>

### [`009b1d98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b1/009b1d98.md) → [`009b1f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b1/009b1f34.md) FUN_009b1f34

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 82.86% / 新版 82.86%

CFGの説明率　旧版 17.65% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009b1f4c",
      "incomplete_value": false,
      "site": "009b1f50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c88000:8"
          ],
          [
            "leaf",
            "const:b00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b1db0",
      "incomplete_value": false,
      "site": "009b1db4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c88000:8"
          ],
          [
            "leaf",
            "const:700:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "009b1df0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "009b1f8c"
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
      "009b1f50",
      "DATA",
      [
        "storage",
        "00c88700",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:009b1df0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b1f9c"
      ]
    ],
    [
      "unmatched:009b1e10",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "009b1f50",
      "DATA",
      [
        "storage",
        "00c88b00",
        null,
        "undefined *"
      ]
    ],
    [
      "009b1f8c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b1f9c"
      ]
    ],
    [
      "009b1fac",
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

- 旧版 [`009b1df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b1/009b1d98.md#insn-009b1df0) · [`009b1e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b1/009b1d98.md#insn-009b1e10)
- 新版 `009b1f8c`（命令位置の公開資料なし）

~~~diff
- 009b1df0 ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
- 009b1df0 bytes 80000054
- 009b1e10 ["COPY", "register:0:8", ["register:4040:8"]]
- 009b1e10 ["INT_ADD", "register:40f0:8", ["const:9b1e10:8", "const:4:8"]]
- 009b1e10 ["CALLIND", null, ["register:0:8"]]
- 009b1e10 bytes 00013fd6
+ 009b1f8c ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
+ 009b1f8c bytes 80000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75736acb5aeba7059be8144e85890385"></a>

### [`009b1e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b1/009b1e24.md) → [`009b1fc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b1/009b1fc0.md) FUN_009b1fc0

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 56.41% / 新版 56.41%

CFGの説明率　旧版 3.70% / 新版 10.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b1e24"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b1e24"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b1e28"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009b1e24",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:009b1e28",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:009b1e50",
      "DATA",
      [
        "storage",
        "00c88700",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b1fc0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "009b1fc4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "009b1fec",
      "DATA",
      [
        "storage",
        "00c88b00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b1e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b1/009b1e24.md#insn-009b1e24) · [`009b1e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b1/009b1e24.md#insn-009b1e28) · [`009b1e38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b1/009b1e24.md#insn-009b1e38)
- 新版 `009b1fd4`（命令位置の公開資料なし）

~~~diff
- 009b1e24 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 009b1e24 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 009b1e24 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 009b1e24 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 009b1e24 bytes fd7bbea9
- 009b1e28 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 009b1e28 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 009b1e28 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 009b1e28 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009b1e28 bytes f44f01a9
- 009b1e38 ["INT_ADD", "register:40f0:8", ["const:9b1e38:8", "const:4:8"]]
- 009b1e38 ["CALL", null, ["callee:00c57e90:8"]]
+ 009b1fd4 ["INT_ADD", "register:40f0:8", ["const:9b1fd4:8", "const:4:8"]]
+ 009b1fd4 ["CALL", null, ["callee:00c57e90:8"]]
- 009b1e38 bytes 16970a94
+ 009b1fd4 bytes af970a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c58ebf19bd9b06e4e05862b729e8a2da"></a>

### [`009b2074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b2074.md) → [`009b2210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b2/009b2210.md) FUN_009b2210

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`005aa130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa130.md) [`009a9e44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a9/009a9e44.md) [`009ae0d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ae/009ae0d0.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`005aa170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa170.md) [`009a9fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a9/009a9fe0.md) [`009ae26c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ae/009ae26c.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 89.52% / 新版 89.52%

CFGの説明率　旧版 58.06% / 新版 56.25%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "009b214c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "009b219c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "009b22e8"
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
      "009b22c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:009b2150"
      ]
    ],
    [
      "unmatched:009b214c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b2354"
      ]
    ],
    [
      "009b2320",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:009b2190"
      ]
    ]
  ],
  "added": [
    [
      "009b22c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b22ec"
      ]
    ],
    [
      "009b22e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b2354"
      ]
    ],
    [
      "009b2320",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b232c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b214c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b2074.md#insn-009b214c) · [`009b2168`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b2074.md#insn-009b2168) · [`009b217c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b2074.md#insn-009b217c)
- 新版 `009b2304`（命令位置の公開資料なし） · `009b2318`（命令位置の公開資料なし）

~~~diff
- 009b214c ["CBRANCH", null, ["local:b16:8", "register:102:1"]]
- 009b214c bytes 62030054
- 009b2168 ["INT_ADD", "register:40f0:8", ["const:9b2168:8", "const:4:8"]]
- 009b2168 ["CALL", null, ["callee:009a9fe0:8"]]
+ 009b2304 ["INT_ADD", "register:40f0:8", ["const:9b2304:8", "const:4:8"]]
+ 009b2304 ["CALL", null, ["callee:009a9fe0:8"]]
- 009b2168 bytes 37dfff97
+ 009b2304 bytes 37dfff97
- 009b217c ["INT_ADD", "register:40f0:8", ["const:9b217c:8", "const:4:8"]]
- 009b217c ["CALL", null, ["callee:009ae26c:8"]]
+ 009b2318 ["INT_ADD", "register:40f0:8", ["const:9b2318:8", "const:4:8"]]
+ 009b2318 ["CALL", null, ["callee:009ae26c:8"]]
- 009b217c bytes d5efff97
+ 009b2318 bytes d5efff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1b14e1d8d8db40cc465a4d8f5d1e97b"></a>

### [`009b236c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b236c.md) → [`009b2508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b2/009b2508.md) FUN_009b2508

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 86.21% / 新版 86.21%

CFGの説明率　旧版 14.29% / 新版 11.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b2388"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009b2524"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "009b238c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009b2388",
      "DATA",
      [
        "storage",
        "00c88780",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:009b238c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b2550"
      ]
    ]
  ],
  "added": [
    [
      "009b2524",
      "DATA",
      [
        "storage",
        "00c88b80",
        null,
        "undefined *"
      ]
    ],
    [
      "009b2528",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b2550"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b2388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b236c.md#insn-009b2388) · [`009b238c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b236c.md#insn-009b238c)
- 新版 `009b2524`（命令位置の公開資料なし）

~~~diff
- 009b2388 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 009b2388 ["COPY", "tmp:1:8", ["register:4008:8"]]
- 009b2388 ["INT_ADD", "register:4008:8", ["register:4008:8", "const:10:8"]]
- 009b2388 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 009b2388 bytes 290401f8
- 009b238c ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 009b238c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 009b238c bytes 480100b4
+ 009b2524 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 009b2524 ["COPY", "tmp:1:8", ["register:4008:8"]]
+ 009b2524 ["INT_ADD", "register:4008:8", ["register:4008:8", "const:10:8"]]
+ 009b2524 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 009b2524 bytes 290401f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-558f2a5c4057e008ae8cff2e27ce7e56"></a>

### [`009b2508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b2508.md) → [`009b26a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b2/009b26a4.md) FUN_009b26a4

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "009b26b8",
      "incomplete_value": false,
      "site": "009b26bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c88000:8"
          ],
          [
            "leaf",
            "const:c00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b251c",
      "incomplete_value": false,
      "site": "009b2520",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c88000:8"
          ],
          [
            "leaf",
            "const:800:8"
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
      "009b26bc",
      "DATA",
      [
        "storage",
        "00c88800",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b26bc",
      "DATA",
      [
        "storage",
        "00c88c00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b2514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b2508.md#insn-009b2514) · [`009b251c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b2508.md#insn-009b251c)
- 新版 `009b26b0`（命令位置の公開資料なし） · `009b26b8`（命令位置の公開資料なし）

~~~diff
- 009b2514 ["INT_ADD", "register:40f0:8", ["const:9b2514:8", "const:4:8"]]
- 009b2514 ["CALL", null, ["callee:00c57e90:8"]]
+ 009b26b0 ["INT_ADD", "register:40f0:8", ["const:9b26b0:8", "const:4:8"]]
+ 009b26b0 ["CALL", null, ["callee:00c57e90:8"]]
- 009b2514 bytes 5f950a94
+ 009b26b0 bytes f8950a94
- 009b251c ["COPY", "tmp:0:8", ["const:800:8"]]
- 009b251c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009b251c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009b251c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009b26b8 ["COPY", "tmp:0:8", ["const:c00:8"]]
+ 009b26b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009b26b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009b26b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009b251c bytes 08012091
+ 009b26b8 bytes 08013091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2bdd3fc63cec91daf732f2ad45621fa5"></a>

### [`009b252c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b252c.md) → [`009b26c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b2/009b26c8.md) FUN_009b26c8

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009b26cc",
      "incomplete_value": false,
      "site": "009b26d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c88000:8"
          ],
          [
            "leaf",
            "const:c00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b2530",
      "incomplete_value": false,
      "site": "009b2534",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c88000:8"
          ],
          [
            "leaf",
            "const:800:8"
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
      "009b26d0",
      "DATA",
      [
        "storage",
        "00c88800",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b26d0",
      "DATA",
      [
        "storage",
        "00c88c00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b2530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b252c.md#insn-009b2530)
- 新版 `009b26cc`（命令位置の公開資料なし）

~~~diff
- 009b2530 ["COPY", "tmp:0:8", ["const:800:8"]]
- 009b2530 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009b2530 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009b2530 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009b26cc ["COPY", "tmp:0:8", ["const:c00:8"]]
+ 009b26cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009b26cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009b26cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009b2530 bytes 08012091
+ 009b26cc bytes 08013091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7fb2ae890afd3a7103df59537b74ad8d"></a>

### [`009b2648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b2648.md) → [`009b27e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b2/009b27e4.md) FUN_009b27e4

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009b27e8",
      "incomplete_value": false,
      "site": "009b27ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c88000:8"
          ],
          [
            "leaf",
            "const:d00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b264c",
      "incomplete_value": false,
      "site": "009b2650",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c88000:8"
          ],
          [
            "leaf",
            "const:900:8"
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
      "009b27ec",
      "DATA",
      [
        "storage",
        "00c88900",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b27ec",
      "DATA",
      [
        "storage",
        "00c88d00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b264c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b2648.md#insn-009b264c)
- 新版 `009b27e8`（命令位置の公開資料なし）

~~~diff
- 009b264c ["COPY", "tmp:0:8", ["const:900:8"]]
- 009b264c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009b264c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009b264c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009b27e8 ["COPY", "tmp:0:8", ["const:d00:8"]]
+ 009b27e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009b27e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009b27e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009b264c bytes 08012491
+ 009b27e8 bytes 08013491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f765ccb5afb51996c05243290e1adeb"></a>

### [`009b2660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b2660.md) → [`009b27fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b2/009b27fc.md) FUN_009b27fc

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b2660"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b2660"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b2664"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009b2660",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:009b2664",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:009b2684",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "009b27fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "009b2800",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "009b2820",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b2660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b2660.md#insn-009b2660) · [`009b2664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b2660.md#insn-009b2664) · [`009b2684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b2660.md#insn-009b2684)

~~~diff
- 009b2660 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 009b2660 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 009b2660 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 009b2660 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 009b2660 bytes fd7bbea9
- 009b2664 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 009b2664 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 009b2664 bytes f30b00f9
- 009b2684 ["INT_ADD", "register:40f0:8", ["const:9b2684:8", "const:4:8"]]
- 009b2684 ["CALL", null, ["ram:47acb4:8"]]
- 009b2684 bytes 8c21eb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-198ad7e5b846cd607c32d061266c850b"></a>

### [`009b2814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b2814.md) → [`009b29b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b2/009b29b0.md) FUN_009b29b0

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 76.60% / 新版 76.60%

CFGの説明率　旧版 17.39% / 新版 28.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b2814"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b2814"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b2818"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009b2814",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:009b2818",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:009b281c",
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
      "009b29b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "009b29b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "009b29b8",
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

- 旧版 [`009b2814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b2814.md#insn-009b2814) · [`009b2818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b2814.md#insn-009b2818) · [`009b281c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b2814.md#insn-009b281c)

~~~diff
- 009b2814 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 009b2814 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 009b2814 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 009b2814 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 009b2814 bytes fd7bbda9
- 009b2818 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 009b2818 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 009b2818 bytes f50b00f9
- 009b281c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 009b281c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 009b281c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 009b281c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009b281c bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4b7fa3f6e362a02dd3fa21f38efde05"></a>

### [`009b291c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b291c.md) → [`009b2ab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b2/009b2ab8.md) FUN_009b2ab8

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.23% / 新版 94.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009b2ae0",
      "incomplete_value": false,
      "site": "009b2ae0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c88000:8"
          ],
          [
            "leaf",
            "const:d80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b2944",
      "incomplete_value": false,
      "site": "009b2944",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c88000:8"
          ],
          [
            "leaf",
            "const:980:8"
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
      "009b2ae0",
      "DATA",
      [
        "storage",
        "00c88980",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b2ae0",
      "DATA",
      [
        "storage",
        "00c88d80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b293c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b291c.md#insn-009b293c) · [`009b2940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b291c.md#insn-009b2940) · [`009b2960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b291c.md#insn-009b2960)
- 新版 `009b2ad8`（命令位置の公開資料なし） · `009b2afc`（命令位置の公開資料なし）

~~~diff
- 009b293c ["COPY", "tmp:0:8", ["const:980:8"]]
- 009b293c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009b293c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009b293c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009b2ad8 ["COPY", "tmp:0:8", ["const:d80:8"]]
+ 009b2ad8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009b2ad8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009b2ad8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009b293c bytes 08012691
+ 009b2ad8 bytes 08013691
- 009b2940 ["COPY", "register:40a0:8", ["register:4008:8"]]
- 009b2940 bytes f40301aa
- 009b2960 ["COPY", "register:0:8", ["register:4040:8"]]
- 009b2960 ["INT_ADD", "register:40f0:8", ["const:9b2960:8", "const:4:8"]]
- 009b2960 ["CALLIND", null, ["register:0:8"]]
+ 009b2afc ["COPY", "register:0:8", ["register:4040:8"]]
+ 009b2afc ["INT_ADD", "register:40f0:8", ["const:9b2afc:8", "const:4:8"]]
+ 009b2afc ["CALLIND", null, ["register:0:8"]]
- 009b2960 bytes 00013fd6
+ 009b2afc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a30b60a6228cd7416dfce5741f06b013"></a>

### [`009b2c08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b2c08.md) → [`009b2da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b2/009b2da4.md) _INIT_196

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 77.97% / 新版 77.97%

CFGの説明率　旧版 51.16% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b2c38"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b2c4c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b2c50"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009b2c38",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:009b2c44",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "unmatched:009b2c4c",
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
      "009b2dd4",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "009b2de0",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "009b2de8",
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

- 旧版 [`009b2c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b2c08.md#insn-009b2c38) · [`009b2c4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b2c08.md#insn-009b2c4c) · [`009b2c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b2c08.md#insn-009b2c50)

~~~diff
- 009b2c38 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 009b2c38 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 009b2c38 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 009b2c38 bytes a9831ff8
- 009b2c4c ["COPY", "tmp:0:4", ["register:4050:4"]]
- 009b2c4c ["INT_ADD", "tmp:1:8", ["register:8:8", "const:21:8"]]
- 009b2c4c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 009b2c4c bytes ea130278
- 009b2c50 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 009b2c50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 009b2c50 bytes e92b00b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2742a84d931d61b1644075928d1799a1"></a>

### [`009b2f98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b2f98.md) → [`009b3134`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b3/009b3134.md) FUN_009b3134

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005a8de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a8/005a8de8.md) · 呼出先 6件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`005a9f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9f14.md) [`009b35fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b3/009b35fc.md) [`009b5be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5be8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`005a8e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a8/005a8e28.md) · 呼出先 6件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`005a9f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9f54.md) [`009b3798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b3/009b3798.md) [`009b5d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b5/009b5d84.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 80.42% / 新版 80.42%

CFGの説明率　旧版 23.13% / 新版 23.61%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_condition` 2件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 7件, `unresolved_store_alignment` 20件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b2fac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b2fac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b2fb0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009b2fac",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:009b2fb0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:009b2fbc",
      "WRITE",
      [
        "storage",
        "Stack[-0x138]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009b3148",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "009b314c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "009b3158",
      "WRITE",
      [
        "storage",
        "Stack[-0x138]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b2fac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b2f98.md#insn-009b2fac) · [`009b2fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b2f98.md#insn-009b2fb0) · [`009b2fbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b2f98.md#insn-009b2fbc)

~~~diff
- 009b2fac ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 009b2fac ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 009b2fac ["INT_ADD", "tmp:2:8", ["register:8:8", "const:120:8"]]
- 009b2fac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009b2fac bytes f65712a9
- 009b2fb0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 009b2fb0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 009b2fb0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:130:8"]]
- 009b2fb0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009b2fb0 bytes f44f13a9
- 009b2fbc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 009b2fbc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 009b2fbc bytes e80700f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cefc2c48bc993de3f5ea0f77e0d1339d"></a>

### [`009b35fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b3/009b35fc.md) → [`009b3798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b3/009b3798.md) FUN_009b3798

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`005aa76c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa76c.md) [`005ab8d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005ab8d4.md) [`009b2f98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b2f98.md) · 呼出先 7件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`005aa130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa130.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`005aa7ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa7ac.md) [`005ab914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005ab914.md) [`009b3134`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b3/009b3134.md) · 呼出先 7件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`005aa170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa170.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 68.14% / 新版 68.14%

CFGの説明率　旧版 17.46% / 新版 14.47%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 10件, `unresolved_call_alignment` 6件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b3620"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b3628"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b3668"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009b3620",
      "WRITE",
      [
        "storage",
        "Stack[-0x98]",
        null,
        null
      ]
    ],
    [
      "unmatched:009b3628",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:009b3650",
      "READ",
      [
        "storage",
        "002b9fef",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009b37bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x98]",
        null,
        null
      ]
    ],
    [
      "009b37c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "009b37ec",
      "READ",
      [
        "storage",
        "002ba02f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b3620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b3/009b35fc.md#insn-009b3620) · [`009b3628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b3/009b35fc.md#insn-009b3628) · [`009b3668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b3/009b35fc.md#insn-009b3668)

~~~diff
- 009b3620 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 009b3620 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 009b3620 bytes e80700f9
- 009b3628 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 009b3628 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 009b3628 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 009b3628 bytes a8831ff8
- 009b3668 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 009b3668 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 009b3668 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 009b3668 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009b3668 bytes fa2701a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f62f35cf43fbf0f74314f018d074d3e5"></a>

### [`009b3964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b3/009b3964.md) → [`009b3b00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b3/009b3b00.md) FUN_009b3b00

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 4件 [`0084e55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0084e/0084e55c.md) [`009ac8d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ac/009ac8d8.md) [`009aca94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ac/009aca94.md) [`009ad308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ad/009ad308.md) · 呼出先 0件 
- 新版 呼出元 4件 [`0084e59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0084e/0084e59c.md) [`009aca74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ac/009aca74.md) [`009acc30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ac/009acc30.md) [`009ad4a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ad/009ad4a4.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-01a0b175a1b492d1f0ee1a05441e62d7"></a>

### [`009b396c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b3/009b396c.md) → [`009b3b08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b3/009b3b08.md) FUN_009b3b08

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`008492f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00849/008492f4.md) [`0084e55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0084e/0084e55c.md) [`009b0a40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b0/009b0a40.md) · 呼出先 2件 [`00869eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/00869eb4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 4件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00849334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00849/00849334.md) [`0084e59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0084e/0084e59c.md) [`009b0bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b0/009b0bdc.md) · 呼出先 2件 [`00869ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00869/00869ef4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 58.33% / 新版 58.33%

CFGの説明率　旧版 5.56% / 新版 12.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b396c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b396c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b3970"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009b396c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:009b3970",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:009b3980",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b3b5c"
      ]
    ]
  ],
  "added": [
    [
      "009b3b08",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "009b3b0c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "009b3b1c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b3b5c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b396c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b3/009b396c.md#insn-009b396c) · [`009b3970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b3/009b396c.md#insn-009b3970) · [`009b397c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b3/009b396c.md#insn-009b397c)

~~~diff
- 009b396c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 009b396c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 009b396c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 009b396c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 009b396c bytes fd7bbea9
- 009b3970 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 009b3970 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 009b3970 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 009b3970 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009b3970 bytes f44f01a9
- 009b397c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 009b397c ["COPY", "tmp:1:8", ["const:0:8"]]
- 009b397c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 009b397c bytes 1f0000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e157d8bae536181f399a2a45b7f1049"></a>

### [`009b39cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b3/009b39cc.md) → [`009b3b68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b3/009b3b68.md) FUN_009b3b68

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`009adf94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ad/009adf94.md) [`009ae7ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ae/009ae7ec.md) [`009b4504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b4/009b4504.md) · 呼出先 10件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00752240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00752/00752240.md) [`009a95cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a9/009a95cc.md) [`009a95dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a9/009a95dc.md) [`009b3fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b3/009b3fc8.md)
- 新版 呼出元 3件 [`009ae130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ae/009ae130.md) [`009ae988`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ae/009ae988.md) [`009b46a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b4/009b46a0.md) · 呼出先 10件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00752280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00752/00752280.md) [`009a9768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a9/009a9768.md) [`009a9778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a9/009a9778.md) [`009b4164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b4/009b4164.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 86.96% / 新版 86.96%

CFGの説明率　旧版 39.81% / 新版 38.05%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 1件, `store_value` 1件, `unresolved_branch_alignment` 9件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009b3cf0",
      "incomplete_value": false,
      "site": "009b3cfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c88000:8"
          ],
          [
            "leaf",
            "const:e10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b3b54",
      "incomplete_value": false,
      "site": "009b3b60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c88000:8"
          ],
          [
            "leaf",
            "const:a10:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b3c20"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b3c2c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009b3bb4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "009a95cc"
      ]
    ],
    [
      "unmatched:009b3a34",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b3f54"
      ]
    ],
    [
      "009b3be8",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:009b3db8"
      ]
    ]
  ],
  "added": [
    [
      "009b3bb4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "009a9768"
      ]
    ],
    [
      "009b3bd0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b3fa0"
      ]
    ],
    [
      "009b3be8",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "009b3f54"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b3a18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b3/009b39cc.md#insn-009b3a18) · [`009b3a34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b3/009b39cc.md#insn-009b3a34) · [`009b3a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b3/009b39cc.md#insn-009b3a84)
- 新版 `009b3bb4`（命令位置の公開資料なし） · `009b3c20`（命令位置の公開資料なし）

~~~diff
- 009b3a18 ["INT_ADD", "register:40f0:8", ["const:9b3a18:8", "const:4:8"]]
- 009b3a18 ["CALL", null, ["ram:9a95cc:8"]]
+ 009b3bb4 ["INT_ADD", "register:40f0:8", ["const:9b3bb4:8", "const:4:8"]]
+ 009b3bb4 ["CALL", null, ["ram:9a9768:8"]]
- 009b3a18 bytes edd6ff97
+ 009b3bb4 bytes edd6ff97
- 009b3a34 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 009b3a34 ["CBRANCH", null, ["local:b78:8", "tmp:0:1"]]
- 009b3a34 bytes 801e00b4
- 009b3a84 ["COPY", "register:0:8", ["register:4040:8"]]
- 009b3a84 ["INT_ADD", "register:40f0:8", ["const:9b3a84:8", "const:4:8"]]
- 009b3a84 ["CALLIND", null, ["register:0:8"]]
+ 009b3c20 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009b3c20 ["INT_ADD", "register:40f0:8", ["const:9b3c20:8", "const:4:8"]]
+ 009b3c20 ["CALLIND", null, ["register:0:8"]]
- 009b3a84 bytes 00013fd6
+ 009b3c20 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c212a3d7d44e55e8a019fb5cfc4d96f"></a>

### [`009b3fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b3/009b3fc8.md) → [`009b4164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b4/009b4164.md) FUN_009b4164

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00745f74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00745/00745f74.md) [`009b39cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b3/009b39cc.md) · 呼出先 15件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00598af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00598/00598af4.md) [`00598cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00598/00598cb4.md) [`005abfb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ab/005abfb0.md) [`00795de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00795/00795de4.md)
- 新版 呼出元 2件 [`00745fb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00745/00745fb4.md) [`009b3b68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b3/009b3b68.md) · 呼出先 15件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00598b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598b34.md) [`00598cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598cf4.md) [`005abff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ab/005abff0.md) [`00795e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795e24.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 86.99% / 新版 86.99%

CFGの説明率　旧版 37.17% / 新版 36.21%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `store_condition` 2件, `store_value` 1件, `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b4004"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b4020"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b409c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009b4004",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:009b4020",
      "WRITE",
      [
        "storage",
        "Stack[-0x90]",
        null,
        null
      ]
    ],
    [
      "unmatched:009b409c",
      "DATA",
      [
        "storage",
        "00c6d620",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b41a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "009b41bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x90]",
        null,
        null
      ]
    ],
    [
      "009b4238",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b4004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b3/009b3fc8.md#insn-009b4004) · [`009b4008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b3/009b3fc8.md#insn-009b4008) · [`009b4020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b3/009b3fc8.md#insn-009b4020)
- 新版 `009b41a4`（命令位置の公開資料なし）

~~~diff
- 009b4004 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 009b4004 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 009b4004 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 009b4004 bytes a8831ff8
- 009b4008 ["INT_ADD", "register:40f0:8", ["const:9b4008:8", "const:4:8"]]
- 009b4008 ["CALL", null, ["callee:00c57e90:8"]]
+ 009b41a4 ["INT_ADD", "register:40f0:8", ["const:9b41a4:8", "const:4:8"]]
+ 009b41a4 ["CALL", null, ["callee:00c57e90:8"]]
- 009b4008 bytes a28e0a94
+ 009b41a4 bytes 3b8f0a94
- 009b4020 ["INT_ADD", "tmp:0:8", ["register:40e8:8", "const:ffffffffffffffc0:8"]]
- 009b4020 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 009b4020 bytes a0039c3c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54381be8af2de2c225bad8f8bea12ac7"></a>

### [`009b4504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b4/009b4504.md) → [`009b46a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b4/009b46a0.md) FUN_009b46a0

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009ad6e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ad/009ad6e0.md) · 呼出先 15件 [`00752240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00752/00752240.md) [`009a95cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a9/009a95cc.md) [`009a95d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a9/009a95d4.md) [`009aab7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009aa/009aab7c.md) [`009aac04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009aa/009aac04.md)
- 新版 呼出元 1件 [`009ad87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ad/009ad87c.md) · 呼出先 15件 [`00752280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00752/00752280.md) [`009a9768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a9/009a9768.md) [`009a9770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a9/009a9770.md) [`009aad18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009aa/009aad18.md) [`009aada0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009aa/009aada0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 81.55% / 新版 81.55%

CFGの説明率　旧版 24.39% / 新版 23.81%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `call_target` 2件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b456c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b45c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b45c0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009b4538",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "009a95d4"
      ]
    ],
    [
      "unmatched:009b4540",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:009b4554"
      ]
    ],
    [
      "009b46e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "009a95d4"
      ]
    ]
  ],
  "added": [
    [
      "009b46d4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "009a9770"
      ]
    ],
    [
      "009b46dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b46f0"
      ]
    ],
    [
      "009b46e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "009a9770"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b4538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b4/009b4504.md#insn-009b4538) · [`009b4540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b4/009b4504.md#insn-009b4540) · [`009b4548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b4/009b4504.md#insn-009b4548)
- 新版 `009b46e4`（命令位置の公開資料なし）

~~~diff
- 009b4538 ["INT_ADD", "register:40f0:8", ["const:9b4538:8", "const:4:8"]]
- 009b4538 ["CALL", null, ["ram:9a95d4:8"]]
- 009b4538 bytes 27d4ff97
- 009b4540 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 009b4540 bytes a0000054
- 009b4548 ["INT_ADD", "register:40f0:8", ["const:9b4548:8", "const:4:8"]]
- 009b4548 ["CALL", null, ["ram:9a95d4:8"]]
+ 009b46e4 ["INT_ADD", "register:40f0:8", ["const:9b46e4:8", "const:4:8"]]
+ 009b46e4 ["CALL", null, ["ram:9a9770:8"]]
- 009b4548 bytes 23d4ff97
+ 009b46e4 bytes 23d4ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3236f26a0c55ec3eb7eabd8e488f3b09"></a>

### [`009b4764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b4/009b4764.md) → [`009b4900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b4/009b4900.md) FUN_009b4900

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`007459e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00745/007459e4.md) [`00746674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00746/00746674.md) [`009ae0d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ae/009ae0d0.md) [`009b4504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b4/009b4504.md) · 呼出先 15件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00598af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00598/00598af4.md) [`00598cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00598/00598cb4.md) [`005aae48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aae48.md) [`00795de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00795/00795de4.md)
- 新版 呼出元 4件 [`00745a24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00745/00745a24.md) [`007466b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00746/007466b4.md) [`009ae26c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ae/009ae26c.md) [`009b46a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b4/009b46a0.md) · 呼出先 15件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00598b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598b34.md) [`00598cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598cf4.md) [`005aae88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aae88.md) [`00795e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795e24.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 78.93% / 新版 78.93%

CFGの説明率　旧版 30.70% / 新版 31.53%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_condition` 1件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 5件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b4798"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b482c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b4884"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009b4798",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:009b482c",
      "DATA",
      [
        "storage",
        "00c6d620",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:009b4864",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b4a18"
      ]
    ]
  ],
  "added": [
    [
      "009b4934",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "009b49c8",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ],
    [
      "009b4a00",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b4a18"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b4798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b4/009b4764.md#insn-009b4798) · [`009b4818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b4/009b4764.md#insn-009b4818) · [`009b482c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b4/009b4764.md#insn-009b482c)
- 新版 `009b49b4`（命令位置の公開資料なし）

~~~diff
- 009b4798 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 009b4798 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 009b4798 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 009b4798 bytes a8831ff8
- 009b4818 ["INT_ADD", "register:40f0:8", ["const:9b4818:8", "const:4:8"]]
- 009b4818 ["CALL", null, ["callee:00c57eb0:8"]]
+ 009b49b4 ["INT_ADD", "register:40f0:8", ["const:9b49b4:8", "const:4:8"]]
+ 009b49b4 ["CALL", null, ["callee:00c57eb0:8"]]
- 009b4818 bytes a68c0a94
+ 009b49b4 bytes 3f8d0a94
- 009b482c ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 009b482c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 009b482c bytes a80200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c65cfa8cd1e8dd49a2ce7f6839dc521"></a>

### [`009b4c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b4/009b4c90.md) → [`009b4e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b4/009b4e2c.md) FUN_009b4e2c

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009af7ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009af/009af7ec.md) · 呼出先 10件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00752240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00752/00752240.md) [`009a95cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a9/009a95cc.md) [`009aa480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009aa/009aa480.md) [`009b5220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5220.md)
- 新版 呼出元 1件 [`009af988`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009af/009af988.md) · 呼出先 10件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00752280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00752/00752280.md) [`009a9768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a9/009a9768.md) [`009aa61c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009aa/009aa61c.md) [`009b53bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b5/009b53bc.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 84.17% / 新版 84.17%

CFGの説明率　旧版 35.59% / 新版 31.58%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `call_target` 1件, `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 6件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b4cb8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b4d4c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b4db4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009b4cb8",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "009b4e6c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "009a95cc"
      ]
    ],
    [
      "unmatched:009b4cec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:009b5084"
      ]
    ]
  ],
  "added": [
    [
      "009b4e54",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "009b4e6c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "009a9768"
      ]
    ],
    [
      "009b4e88",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b5220"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b4cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b4/009b4c90.md#insn-009b4cb8) · [`009b4cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b4/009b4c90.md#insn-009b4cc4) · [`009b4cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b4/009b4c90.md#insn-009b4cd0)
- 新版 `009b4e60`（命令位置の公開資料なし） · `009b4e6c`（命令位置の公開資料なし）

~~~diff
- 009b4cb8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 009b4cb8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 009b4cb8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 009b4cb8 bytes a8831ff8
- 009b4cc4 ["INT_ADD", "register:40f0:8", ["const:9b4cc4:8", "const:4:8"]]
- 009b4cc4 ["CALL", null, ["callee:009aa61c:8"]]
+ 009b4e60 ["INT_ADD", "register:40f0:8", ["const:9b4e60:8", "const:4:8"]]
+ 009b4e60 ["CALL", null, ["callee:009aa61c:8"]]
- 009b4cc4 bytes efd5ff97
+ 009b4e60 bytes efd5ff97
- 009b4cd0 ["INT_ADD", "register:40f0:8", ["const:9b4cd0:8", "const:4:8"]]
- 009b4cd0 ["CALL", null, ["ram:9a95cc:8"]]
+ 009b4e6c ["INT_ADD", "register:40f0:8", ["const:9b4e6c:8", "const:4:8"]]
+ 009b4e6c ["CALL", null, ["ram:9a9768:8"]]
- 009b4cd0 bytes 3fd2ff97
+ 009b4e6c bytes 3fd2ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17ca815fbf2924eeb22577fa17cbfea2"></a>

### [`009b5220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5220.md) → [`009b53bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b5/009b53bc.md) FUN_009b53bc

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00746cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00746/00746cac.md) [`009b4c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b4/009b4c90.md) · 呼出先 15件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00598af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00598/00598af4.md) [`00598cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00598/00598cb4.md) [`005a9720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9720.md) [`00795de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00795/00795de4.md)
- 新版 呼出元 2件 [`00746cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00746/00746cec.md) [`009b4e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b4/009b4e2c.md) · 呼出先 15件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00598b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598b34.md) [`00598cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598cf4.md) [`005a9760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9760.md) [`00795e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795e24.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 86.36% / 新版 86.36%

CFGの説明率　旧版 47.96% / 新版 46.08%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_condition` 1件, `store_value` 2件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b5254"
    }
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009b5480",
      "incomplete_value": false,
      "site": "009b5484",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:a10:8"
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
      "definition_site": "009b52e4",
      "incomplete_value": false,
      "site": "009b52e8",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:610:8"
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009b5510",
      "incomplete_value": false,
      "site": "009b5510",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:190:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b5374",
      "incomplete_value": false,
      "site": "009b5374",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c88000:8"
          ],
          [
            "leaf",
            "const:d90:8"
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
      "unmatched:009b5254",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:009b52c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b54ac"
      ]
    ],
    [
      "009b5484",
      "DATA",
      [
        "storage",
        "00c6d620",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b53f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "009b5460",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b54ac"
      ]
    ],
    [
      "009b5484",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b5254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5220.md#insn-009b5254) · [`009b5258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5220.md#insn-009b5258) · [`009b52c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5220.md#insn-009b52c4)
- 新版 `009b53f4`（命令位置の公開資料なし）

~~~diff
- 009b5254 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 009b5254 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 009b5254 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 009b5254 bytes a8831ff8
- 009b5258 ["INT_ADD", "register:40f0:8", ["const:9b5258:8", "const:4:8"]]
- 009b5258 ["CALL", null, ["callee:00c57e90:8"]]
+ 009b53f4 ["INT_ADD", "register:40f0:8", ["const:9b53f4:8", "const:4:8"]]
+ 009b53f4 ["CALL", null, ["callee:00c57e90:8"]]
- 009b5258 bytes 0e8a0a94
+ 009b53f4 bytes a78a0a94
- 009b52c4 ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
- 009b52c4 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 009b52c4 bytes 750200b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93502ad8252e669df487915a0cfe0515"></a>

### [`009b58f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b58f4.md) → [`009b5a90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b5/009b5a90.md) FUN_009b5a90

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 82.76% / 新版 82.76%

CFGの説明率　旧版 41.67% / 新版 31.25%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009b5ac4",
      "incomplete_value": false,
      "site": "009b5ac8",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:a10:8"
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
      "definition_site": "009b5928",
      "incomplete_value": false,
      "site": "009b592c",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:610:8"
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "009b5908"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "009b5aa4"
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
      "unmatched:009b5908",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b5af8"
      ]
    ],
    [
      "009b5ac8",
      "DATA",
      [
        "storage",
        "00c6d620",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b5aa4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b5af8"
      ]
    ],
    [
      "009b5ac8",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b5908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b58f4.md#insn-009b5908) · [`009b5938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b58f4.md#insn-009b5938) · [`009b5964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b58f4.md#insn-009b5964)
- 新版 `009b5ad4`（命令位置の公開資料なし）

~~~diff
- 009b5908 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 009b5908 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 009b5908 bytes b30200b4
- 009b5938 ["INT_ADD", "register:40f0:8", ["const:9b5938:8", "const:4:8"]]
- 009b5938 ["CALL", null, ["callee:00c57eb0:8"]]
+ 009b5ad4 ["INT_ADD", "register:40f0:8", ["const:9b5ad4:8", "const:4:8"]]
+ 009b5ad4 ["CALL", null, ["callee:00c57eb0:8"]]
- 009b5938 bytes 5e880a94
+ 009b5ad4 bytes f7880a94
- 009b5964 ["COPY", "register:0:8", ["register:40f0:8"]]
- 009b5964 ["RETURN", null, ["register:0:8"]]
- 009b5964 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af4893faa92acaed276f29e4871019f4"></a>

### [`009b5968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5968.md) → [`009b5b04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b5/009b5b04.md) FUN_009b5b04

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 82.76% / 新版 82.76%

CFGの説明率　旧版 9.09% / 新版 4.55%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b59a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009b5b3c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "009b597c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009b597c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b5b6c"
      ]
    ],
    [
      "unmatched:009b59a0",
      "DATA",
      [
        "storage",
        "00c6d620",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b5b18",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b5b6c"
      ]
    ],
    [
      "009b5b3c",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b597c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5968.md#insn-009b597c) · [`009b59a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5968.md#insn-009b59a0) · [`009b59bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5968.md#insn-009b59bc)
- 新版 `009b5b58`（命令位置の公開資料なし）

~~~diff
- 009b597c ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 009b597c ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 009b597c bytes b30200b4
- 009b59a0 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 009b59a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 009b59a0 bytes 680200f9
- 009b59bc ["INT_ADD", "register:40f0:8", ["const:9b59bc:8", "const:4:8"]]
- 009b59bc ["CALL", null, ["callee:00c57eb0:8"]]
+ 009b5b58 ["INT_ADD", "register:40f0:8", ["const:9b5b58:8", "const:4:8"]]
+ 009b5b58 ["CALL", null, ["callee:00c57eb0:8"]]
- 009b59bc bytes 3d880a94
+ 009b5b58 bytes d6880a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69cf7344d8c03867de8ae617b4c6a6a1"></a>

### [`009b59dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b59dc.md) → [`009b5b78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b5/009b5b78.md) FUN_009b5b78

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`009ac78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ac/009ac78c.md) · 呼出先 2件 [`009a91c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a9/009a91c8.md) [`009a9418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a9/009a9418.md)
- 新版 呼出元 1件 [`009ac928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ac/009ac928.md) · 呼出先 2件 [`009a9364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a9/009a9364.md) [`009a95b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a9/009a95b4.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009b59f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b59dc.md#insn-009b59f0) · [`009b59f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b59dc.md#insn-009b59f8)
- 新版 `009b5b8c`（命令位置の公開資料なし） · `009b5b94`（命令位置の公開資料なし）

~~~diff
- 009b59f0 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 009b59f0 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 009b5b8c ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 009b5b8c ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 009b59f0 bytes 000100b4
+ 009b5b8c bytes 000100b4
- 009b59f8 ["INT_ADD", "register:40f0:8", ["const:9b59f8:8", "const:4:8"]]
- 009b59f8 ["CALL", null, ["callee:009a9364:8"]]
+ 009b5b94 ["INT_ADD", "register:40f0:8", ["const:9b5b94:8", "const:4:8"]]
+ 009b5b94 ["CALL", null, ["callee:009a9364:8"]]
- 009b59f8 bytes f4cdff97
+ 009b5b94 bytes f4cdff97
~~~


<a id="compare-a8e39fb36b81fda6938b9a90024667d4"></a>

### [`009b5a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5a90.md) → [`009b5c2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b5/009b5c2c.md) FUN_009b5c2c

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009ad308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ad/009ad308.md) · 呼出先 3件 [`009a9164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a9/009a9164.md) [`009a9454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a9/009a9454.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`009ad4a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ad/009ad4a4.md) · 呼出先 3件 [`009a9300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a9/009a9300.md) [`009a95f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a9/009a95f0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 96.15% / 新版 96.15%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 9件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "009b5aa8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "009b5c44"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009b5c48",
      "incomplete_value": false,
      "site": "009b5c54",
      "value": [
        "leaf",
        "const:78:8"
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
      "unmatched:009b5aa8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b5c84"
      ]
    ]
  ],
  "added": [
    [
      "009b5c44",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b5c84"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b5aa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5a90.md#insn-009b5aa8) · [`009b5ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5a90.md#insn-009b5ab8)
- 新版 `009b5c54`（命令位置の公開資料なし） · `009b5c44`（命令位置の公開資料なし）

~~~diff
- 009b5aa8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 009b5aa8 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 009b5aa8 bytes 000200b5
- 009b5ab8 ["INT_ADD", "register:40f0:8", ["const:9b5ab8:8", "const:4:8"]]
- 009b5ab8 ["CALL", null, ["callee:00c57e90:8"]]
+ 009b5c54 ["INT_ADD", "register:40f0:8", ["const:9b5c54:8", "const:4:8"]]
+ 009b5c54 ["CALL", null, ["callee:00c57e90:8"]]
- 009b5ab8 bytes f6870a94
+ 009b5c54 bytes 8f880a94
+ 009b5c44 ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 009b5c44 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 009b5c44 bytes 000200b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-662e0f3ca3458ee0a223ce17c1861d58"></a>

### [`009b5be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5be8.md) → [`009b5d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b5/009b5d84.md) FUN_009b5d84

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009b2f98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b2/009b2f98.md) · 呼出先 7件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`005a9ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9ea4.md) [`005a9f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9f14.md) [`005aa144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa144.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`009b3134`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b3/009b3134.md) · 呼出先 7件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`005a9ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9ee4.md) [`005a9f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a9/005a9f54.md) [`005aa184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa184.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 97.83% / 新版 97.83%

CFGの説明率　旧版 65.38% / 新版 58.62%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b5d44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b5d48"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b5da0"
    }
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`009b5d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5be8.md#insn-009b5d44) · [`009b5d48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5be8.md#insn-009b5d48) · [`009b5da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5be8.md#insn-009b5da0)

~~~diff
- 009b5d44 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:68:8"]]
- 009b5d44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 009b5d44 bytes 0a3500f9
- 009b5d48 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:58:8"]]
- 009b5d48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 009b5d48 bytes 0081853c
- 009b5da0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:10:8"]]
- 009b5da0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 009b5da0 bytes 680a00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2b8ef89b190d50491824710664b0543"></a>

### [`009b5e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5e8c.md) → [`009b6028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b6/009b6028.md) FUN_009b6028

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_value, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 64.71% / 新版 64.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009b6034",
      "incomplete_value": false,
      "site": "009b6040",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c88000:8"
          ],
          [
            "leaf",
            "const:e10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009b5ea4",
      "value": [
        "live",
        "register:4050:8"
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "009b603c",
      "incomplete_value": true,
      "site": "009b6044",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
      "definition_site": "009b5ea0",
      "incomplete_value": true,
      "site": "009b5ea8",
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
                "register:4000:8"
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
      "009b6040",
      "DATA",
      [
        "storage",
        "00c88a10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b6040",
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

- 旧版 [`009b5e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5e8c.md#insn-009b5e90) · [`009b5e94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5e8c.md#insn-009b5e94) · [`009b5e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5e8c.md#insn-009b5e98)

~~~diff
- 009b5e90 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:40:8"]]
- 009b5e90 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 009b5e90 bytes 002040f9
- 009b5e94 ["COPY", "register:4050:8", ["const:c88000:8"]]
- 009b5e94 bytes 8a1600f0
- 009b5e98 ["COPY", "tmp:0:8", ["const:a10:8"]]
- 009b5e98 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 009b5e98 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 009b5e98 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 009b5e98 bytes 4a412891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03d6782c86b86d65a0053257b7583455"></a>

### [`009b5f2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5f2c.md) → [`009b60c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b6/009b60c8.md) FUN_009b60c8

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_store_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 33.33% / 新版 27.27%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b5f2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b5f2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b5f30"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009b5f2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:009b5f30",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:009b5f58",
      "DATA",
      [
        "storage",
        "00c88a10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b60c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "009b60cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "009b60f4",
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

- 旧版 [`009b5f2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5f2c.md#insn-009b5f2c) · [`009b5f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5f2c.md#insn-009b5f30) · [`009b5f58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b5/009b5f2c.md#insn-009b5f58)

~~~diff
- 009b5f2c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 009b5f2c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 009b5f2c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 009b5f2c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 009b5f2c bytes fd7bbea9
- 009b5f30 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 009b5f30 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 009b5f30 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 009b5f30 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009b5f30 bytes f44f01a9
- 009b5f58 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 009b5f58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 009b5f58 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b12ba0814b5f9faf639ed89ad223484"></a>

### [`009b60d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b60d4.md) → [`009b6270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b6/009b6270.md) FUN_009b6270

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`005aa130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa130.md) [`009a9e44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a9/009a9e44.md) [`009a9ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a9/009a9ec8.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`005aa170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa170.md) [`009a9fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a9/009a9fe0.md) [`009aa064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009aa/009aa064.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 71.84% / 新版 71.84%

CFGの説明率　旧版 20.00% / 新版 19.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_condition` 1件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b60f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b6124"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b6148"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009b60f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:009b6104",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b62c8"
      ]
    ],
    [
      "unmatched:009b6124",
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
      "009b6294",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "009b62a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b62c8"
      ]
    ],
    [
      "009b62c0",
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

- 旧版 [`009b60f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b60d4.md#insn-009b60f8) · [`009b6104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b60d4.md#insn-009b6104) · [`009b6124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b60d4.md#insn-009b6124)

~~~diff
- 009b60f8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 009b60f8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 009b60f8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 009b60f8 bytes a8831ff8
- 009b6104 ["INT_EQUAL", "tmp:0:1", ["register:40b8:8", "const:0:8"]]
- 009b6104 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 009b6104 bytes 570100b4
- 009b6124 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:30:8"]]
- 009b6124 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 009b6124 bytes e81b00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43ad13cb728edf866023434d78b97b8a"></a>

### [`009b65f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b65f0.md) → [`009b678c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b6/009b678c.md) FUN_009b678c

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "009b67a0",
      "incomplete_value": false,
      "site": "009b67a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c88000:8"
          ],
          [
            "leaf",
            "const:f10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b6604",
      "incomplete_value": false,
      "site": "009b6608",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c88000:8"
          ],
          [
            "leaf",
            "const:b10:8"
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
      "009b67a4",
      "DATA",
      [
        "storage",
        "00c88b10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b67a4",
      "DATA",
      [
        "storage",
        "00c88f10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b65fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b65f0.md#insn-009b65fc) · [`009b6604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b65f0.md#insn-009b6604)
- 新版 `009b6798`（命令位置の公開資料なし） · `009b67a0`（命令位置の公開資料なし）

~~~diff
- 009b65fc ["INT_ADD", "register:40f0:8", ["const:9b65fc:8", "const:4:8"]]
- 009b65fc ["CALL", null, ["callee:00c57e90:8"]]
+ 009b6798 ["INT_ADD", "register:40f0:8", ["const:9b6798:8", "const:4:8"]]
+ 009b6798 ["CALL", null, ["callee:00c57e90:8"]]
- 009b65fc bytes 25850a94
+ 009b6798 bytes be850a94
- 009b6604 ["COPY", "tmp:0:8", ["const:b10:8"]]
- 009b6604 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009b6604 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009b6604 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009b67a0 ["COPY", "tmp:0:8", ["const:f10:8"]]
+ 009b67a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009b67a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009b67a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009b6604 bytes 08412c91
+ 009b67a0 bytes 08413c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be85002e52dad7120999e57a4540a16f"></a>

### [`009b6614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b6614.md) → [`009b67b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b6/009b67b0.md) FUN_009b67b0

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009b67b4",
      "incomplete_value": false,
      "site": "009b67b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c88000:8"
          ],
          [
            "leaf",
            "const:f10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b6618",
      "incomplete_value": false,
      "site": "009b661c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c88000:8"
          ],
          [
            "leaf",
            "const:b10:8"
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
      "009b67b8",
      "DATA",
      [
        "storage",
        "00c88b10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b67b8",
      "DATA",
      [
        "storage",
        "00c88f10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b6618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b6614.md#insn-009b6618)
- 新版 `009b67b4`（命令位置の公開資料なし）

~~~diff
- 009b6618 ["COPY", "tmp:0:8", ["const:b10:8"]]
- 009b6618 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009b6618 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009b6618 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009b67b4 ["COPY", "tmp:0:8", ["const:f10:8"]]
+ 009b67b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009b67b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009b67b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009b6618 bytes 08412c91
+ 009b67b4 bytes 08413c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ab21f4e42f8b2d6b5f7d98536cc941e"></a>

### [`009b665c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b665c.md) → [`009b67f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b6/009b67f8.md) FUN_009b67f8

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, local_def_use, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 76.92% / 新版 76.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009b681c",
      "incomplete_value": false,
      "site": "009b681c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c88000:8"
          ],
          [
            "leaf",
            "const:f90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b6680",
      "incomplete_value": false,
      "site": "009b6680",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c88000:8"
          ],
          [
            "leaf",
            "const:b90:8"
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
      "009b681c",
      "DATA",
      [
        "storage",
        "00c88b90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b681c",
      "DATA",
      [
        "storage",
        "00c88f90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b6664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b665c.md#insn-009b6664) · [`009b6670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b665c.md#insn-009b6670) · [`009b667c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b665c.md#insn-009b667c)
- 新版 `009b680c`（命令位置の公開資料なし） · `009b6818`（命令位置の公開資料なし）

~~~diff
- 009b6664 ["COPY", "register:40e8:8", ["register:8:8"]]
- 009b6664 bytes fd030091
- 009b6670 ["INT_ADD", "register:40f0:8", ["const:9b6670:8", "const:4:8"]]
- 009b6670 ["CALL", null, ["callee:00c57e90:8"]]
+ 009b680c ["INT_ADD", "register:40f0:8", ["const:9b680c:8", "const:4:8"]]
+ 009b680c ["CALL", null, ["callee:00c57e90:8"]]
- 009b6670 bytes 08850a94
+ 009b680c bytes a1850a94
- 009b667c ["COPY", "tmp:0:8", ["const:b90:8"]]
- 009b667c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009b667c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009b667c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009b6818 ["COPY", "tmp:0:8", ["const:f90:8"]]
+ 009b6818 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009b6818 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009b6818 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009b667c bytes 08412e91
+ 009b6818 bytes 08413e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d124b664572e27d9260a75f83697c60"></a>

### [`009b6690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b6690.md) → [`009b682c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b6/009b682c.md) FUN_009b682c

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009b6838",
      "incomplete_value": false,
      "site": "009b6838",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c88000:8"
          ],
          [
            "leaf",
            "const:f90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b669c",
      "incomplete_value": false,
      "site": "009b669c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c88000:8"
          ],
          [
            "leaf",
            "const:b90:8"
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
      "009b6838",
      "DATA",
      [
        "storage",
        "00c88b90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b6838",
      "DATA",
      [
        "storage",
        "00c88f90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b6698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b6690.md#insn-009b6698)
- 新版 `009b6834`（命令位置の公開資料なし）

~~~diff
- 009b6698 ["COPY", "tmp:0:8", ["const:b90:8"]]
- 009b6698 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 009b6698 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 009b6698 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 009b6834 ["COPY", "tmp:0:8", ["const:f90:8"]]
+ 009b6834 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 009b6834 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 009b6834 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 009b6698 bytes 29412e91
+ 009b6834 bytes 29413e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e32578e5601eb20b45e0941258991b5"></a>

### [`009b66ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b66ac.md) → [`009b6848`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b6/009b6848.md) FUN_009b6848

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`005aa130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa130.md) [`009a9e44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a9/009a9e44.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`005aa170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005aa/005aa170.md) [`009a9fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a9/009a9fe0.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 88.46% / 新版 92.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009b6704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b66ac.md#insn-009b6704) · [`009b675c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b66ac.md#insn-009b675c) · [`009b676c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b66ac.md#insn-009b676c)
- 新版 `009b68a0`（命令位置の公開資料なし） · `009b68f8`（命令位置の公開資料なし） · `009b6908`（命令位置の公開資料なし）

~~~diff
- 009b6704 ["INT_ADD", "register:40f0:8", ["const:9b6704:8", "const:4:8"]]
- 009b6704 ["CALL", null, ["callee:0043bb20:8"]]
+ 009b68a0 ["INT_ADD", "register:40f0:8", ["const:9b68a0:8", "const:4:8"]]
+ 009b68a0 ["CALL", null, ["callee:0043bb20:8"]]
- 009b6704 bytes f714ea97
+ 009b68a0 bytes a014ea97
- 009b675c ["INT_ADD", "register:40f0:8", ["const:9b675c:8", "const:4:8"]]
- 009b675c ["CALL", null, ["callee:009a9fe0:8"]]
+ 009b68f8 ["INT_ADD", "register:40f0:8", ["const:9b68f8:8", "const:4:8"]]
+ 009b68f8 ["CALL", null, ["callee:009a9fe0:8"]]
- 009b675c bytes bacdff97
+ 009b68f8 bytes bacdff97
- 009b676c ["INT_ADD", "register:40f0:8", ["const:9b676c:8", "const:4:8"]]
- 009b676c ["CALL", null, ["callee:00c57eb0:8"]]
+ 009b6908 ["INT_ADD", "register:40f0:8", ["const:9b6908:8", "const:4:8"]]
+ 009b6908 ["CALL", null, ["callee:00c57eb0:8"]]
- 009b676c bytes d1840a94
+ 009b6908 bytes 6a850a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9617074b470549f4d2fe748210763651"></a>

### [`009b6824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b6824.md) → [`009b69c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b6/009b69c0.md) FUN_009b69c0

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "009b69d4",
      "incomplete_value": false,
      "site": "009b69d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b6838",
      "incomplete_value": false,
      "site": "009b683c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c88000:8"
          ],
          [
            "leaf",
            "const:c10:8"
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
      "009b69d8",
      "DATA",
      [
        "storage",
        "00c88c10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b69d8",
      "DATA",
      [
        "storage",
        "00c89010",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b6830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b6824.md#insn-009b6830) · [`009b6834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b6824.md#insn-009b6834) · [`009b6838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b6824.md#insn-009b6838)
- 新版 `009b69cc`（命令位置の公開資料なし） · `009b69d0`（命令位置の公開資料なし） · `009b69d4`（命令位置の公開資料なし）

~~~diff
- 009b6830 ["INT_ADD", "register:40f0:8", ["const:9b6830:8", "const:4:8"]]
- 009b6830 ["CALL", null, ["callee:00c57e90:8"]]
+ 009b69cc ["INT_ADD", "register:40f0:8", ["const:9b69cc:8", "const:4:8"]]
+ 009b69cc ["CALL", null, ["callee:00c57e90:8"]]
- 009b6830 bytes 98840a94
+ 009b69cc bytes 31850a94
- 009b6834 ["COPY", "register:4040:8", ["const:c88000:8"]]
+ 009b69d0 ["COPY", "register:4040:8", ["const:c89000:8"]]
- 009b6834 bytes 881600d0
+ 009b69d0 bytes 881600f0
- 009b6838 ["COPY", "tmp:0:8", ["const:c10:8"]]
- 009b6838 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009b6838 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009b6838 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009b69d4 ["COPY", "tmp:0:8", ["const:10:8"]]
+ 009b69d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009b69d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009b69d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009b6838 bytes 08413091
+ 009b69d4 bytes 08410091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5e2aad300a79cfa161bd2bf87ec8270"></a>

### [`009b6848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b6848.md) → [`009b69e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b6/009b69e4.md) FUN_009b69e4

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009b69e8",
      "incomplete_value": false,
      "site": "009b69ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b684c",
      "incomplete_value": false,
      "site": "009b6850",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c88000:8"
          ],
          [
            "leaf",
            "const:c10:8"
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
      "009b69ec",
      "DATA",
      [
        "storage",
        "00c88c10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b69ec",
      "DATA",
      [
        "storage",
        "00c89010",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b6848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b6848.md#insn-009b6848) · [`009b684c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b6848.md#insn-009b684c)
- 新版 `009b69e4`（命令位置の公開資料なし） · `009b69e8`（命令位置の公開資料なし）

~~~diff
- 009b6848 ["COPY", "register:4040:8", ["const:c88000:8"]]
+ 009b69e4 ["COPY", "register:4040:8", ["const:c89000:8"]]
- 009b6848 bytes 881600d0
+ 009b69e4 bytes 881600f0
- 009b684c ["COPY", "tmp:0:8", ["const:c10:8"]]
- 009b684c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009b684c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009b684c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009b69e8 ["COPY", "tmp:0:8", ["const:10:8"]]
+ 009b69e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009b69e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009b69e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009b684c bytes 08413091
+ 009b69e8 bytes 08410091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a4034952a3bdfef03b9fd0bde79a4ed"></a>

### [`009b688c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b688c.md) → [`009b6a28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b6/009b6a28.md) FUN_009b6a28

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "009b6a34",
      "incomplete_value": false,
      "site": "009b6a40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b6898",
      "incomplete_value": false,
      "site": "009b68a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c88000:8"
          ],
          [
            "leaf",
            "const:c90:8"
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
      "009b6a40",
      "DATA",
      [
        "storage",
        "00c88c90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b6a40",
      "DATA",
      [
        "storage",
        "00c89090",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b6894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b688c.md#insn-009b6894) · [`009b6898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b688c.md#insn-009b6898)
- 新版 `009b6a30`（命令位置の公開資料なし） · `009b6a34`（命令位置の公開資料なし）

~~~diff
- 009b6894 ["COPY", "register:4050:8", ["const:c88000:8"]]
+ 009b6a30 ["COPY", "register:4050:8", ["const:c89000:8"]]
- 009b6894 bytes 8a1600d0
+ 009b6a30 bytes 8a1600f0
- 009b6898 ["COPY", "tmp:0:8", ["const:c90:8"]]
- 009b6898 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 009b6898 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 009b6898 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 009b6a34 ["COPY", "tmp:0:8", ["const:90:8"]]
+ 009b6a34 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 009b6a34 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 009b6a34 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 009b6898 bytes 4a413291
+ 009b6a34 bytes 4a410291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ac17e750e9ec51aa0dbde7a9be03e45"></a>

### [`009b68d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b68d0.md) → [`009b6a6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b6/009b6a6c.md) FUN_009b6a6c

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "009b6a84",
      "incomplete_value": false,
      "site": "009b6a90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b68e8",
      "incomplete_value": false,
      "site": "009b68f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c88000:8"
          ],
          [
            "leaf",
            "const:c90:8"
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
      "009b6a90",
      "DATA",
      [
        "storage",
        "00c88c90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b6a90",
      "DATA",
      [
        "storage",
        "00c89090",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b68e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b68d0.md#insn-009b68e4) · [`009b68e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b68d0.md#insn-009b68e8) · [`009b6918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b68d0.md#insn-009b6918)
- 新版 `009b6a80`（命令位置の公開資料なし） · `009b6a84`（命令位置の公開資料なし） · `009b6ab4`（命令位置の公開資料なし）

~~~diff
- 009b68e4 ["COPY", "register:4040:8", ["const:c88000:8"]]
+ 009b6a80 ["COPY", "register:4040:8", ["const:c89000:8"]]
- 009b68e4 bytes 881600d0
+ 009b6a80 bytes 881600f0
- 009b68e8 ["COPY", "tmp:0:8", ["const:c90:8"]]
- 009b68e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009b68e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009b68e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009b6a84 ["COPY", "tmp:0:8", ["const:90:8"]]
+ 009b6a84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009b6a84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009b6a84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009b68e8 bytes 08413291
+ 009b6a84 bytes 08410291
- 009b6918 ["COPY", "register:0:8", ["register:4040:8"]]
- 009b6918 ["INT_ADD", "register:40f0:8", ["const:9b6918:8", "const:4:8"]]
- 009b6918 ["CALLIND", null, ["register:0:8"]]
+ 009b6ab4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009b6ab4 ["INT_ADD", "register:40f0:8", ["const:9b6ab4:8", "const:4:8"]]
+ 009b6ab4 ["CALLIND", null, ["register:0:8"]]
- 009b6918 bytes 00013fd6
+ 009b6ab4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-196ff54c16613724b01892cd0187644f"></a>

### [`009b692c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b692c.md) → [`009b6ac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b6/009b6ac8.md) FUN_009b6ac8

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "009b6af4",
      "incomplete_value": false,
      "site": "009b6af4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b6958",
      "incomplete_value": false,
      "site": "009b6958",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c88000:8"
          ],
          [
            "leaf",
            "const:c90:8"
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
      "009b6af4",
      "DATA",
      [
        "storage",
        "00c88c90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b6af4",
      "DATA",
      [
        "storage",
        "00c89090",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b6940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b692c.md#insn-009b6940) · [`009b694c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b692c.md#insn-009b694c) · [`009b6950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b692c.md#insn-009b6950)
- 新版 `009b6adc`（命令位置の公開資料なし） · `009b6ae8`（命令位置の公開資料なし） · `009b6aec`（命令位置の公開資料なし）

~~~diff
- 009b6940 ["INT_ADD", "register:40f0:8", ["const:9b6940:8", "const:4:8"]]
- 009b6940 ["CALL", null, ["callee:00c57e90:8"]]
+ 009b6adc ["INT_ADD", "register:40f0:8", ["const:9b6adc:8", "const:4:8"]]
+ 009b6adc ["CALL", null, ["callee:00c57e90:8"]]
- 009b6940 bytes 54840a94
+ 009b6adc bytes ed840a94
- 009b694c ["COPY", "register:4040:8", ["const:c88000:8"]]
+ 009b6ae8 ["COPY", "register:4040:8", ["const:c89000:8"]]
- 009b694c bytes 881600d0
+ 009b6ae8 bytes 881600f0
- 009b6950 ["COPY", "tmp:0:8", ["const:c90:8"]]
- 009b6950 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009b6950 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009b6950 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009b6aec ["COPY", "tmp:0:8", ["const:90:8"]]
+ 009b6aec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009b6aec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009b6aec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009b6950 bytes 08413291
+ 009b6aec bytes 08410291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6cd65b280f42505d2be780ad1b247038"></a>

### [`009b69bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b69bc.md) → [`009b6b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b6/009b6b58.md) FUN_009b6b58

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "009b6b78",
      "incomplete_value": false,
      "site": "009b6b78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b69dc",
      "incomplete_value": false,
      "site": "009b69dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c88000:8"
          ],
          [
            "leaf",
            "const:c90:8"
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
      "009b6b78",
      "DATA",
      [
        "storage",
        "00c88c90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b6b78",
      "DATA",
      [
        "storage",
        "00c89090",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b69d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b69bc.md#insn-009b69d4) · [`009b69d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b69bc.md#insn-009b69d8) · [`009b69f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b69bc.md#insn-009b69f8)
- 新版 `009b6b70`（命令位置の公開資料なし） · `009b6b74`（命令位置の公開資料なし） · `009b6b94`（命令位置の公開資料なし）

~~~diff
- 009b69d4 ["COPY", "register:4040:8", ["const:c88000:8"]]
+ 009b6b70 ["COPY", "register:4040:8", ["const:c89000:8"]]
- 009b69d4 bytes 881600d0
+ 009b6b70 bytes 881600f0
- 009b69d8 ["COPY", "tmp:0:8", ["const:c90:8"]]
- 009b69d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009b69d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009b69d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009b6b74 ["COPY", "tmp:0:8", ["const:90:8"]]
+ 009b6b74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009b6b74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009b6b74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009b69d8 bytes 08413291
+ 009b6b74 bytes 08410291
- 009b69f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 009b69f8 ["INT_ADD", "register:40f0:8", ["const:9b69f8:8", "const:4:8"]]
- 009b69f8 ["CALLIND", null, ["register:0:8"]]
+ 009b6b94 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009b6b94 ["INT_ADD", "register:40f0:8", ["const:9b6b94:8", "const:4:8"]]
+ 009b6b94 ["CALLIND", null, ["register:0:8"]]
- 009b69f8 bytes 00013fd6
+ 009b6b94 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8e3716799f8420a34584f9eed7bbe06"></a>

### [`009b6c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b6c38.md) → [`009b6dd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b6/009b6dd4.md) FUN_009b6dd4

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "009b6de0",
      "incomplete_value": false,
      "site": "009b6dec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:110:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b6c44",
      "incomplete_value": false,
      "site": "009b6c50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c88000:8"
          ],
          [
            "leaf",
            "const:d10:8"
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
      "009b6dec",
      "DATA",
      [
        "storage",
        "00c88d10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b6dec",
      "DATA",
      [
        "storage",
        "00c89110",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b6c40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b6c38.md#insn-009b6c40) · [`009b6c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b6c38.md#insn-009b6c44)
- 新版 `009b6ddc`（命令位置の公開資料なし） · `009b6de0`（命令位置の公開資料なし）

~~~diff
- 009b6c40 ["COPY", "register:4050:8", ["const:c88000:8"]]
+ 009b6ddc ["COPY", "register:4050:8", ["const:c89000:8"]]
- 009b6c40 bytes 8a1600d0
+ 009b6ddc bytes 8a1600f0
- 009b6c44 ["COPY", "tmp:0:8", ["const:d10:8"]]
- 009b6c44 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 009b6c44 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 009b6c44 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 009b6de0 ["COPY", "tmp:0:8", ["const:110:8"]]
+ 009b6de0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 009b6de0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 009b6de0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 009b6c44 bytes 4a413491
+ 009b6de0 bytes 4a410491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9cc977f3baa62f781bd9c4270d0a6983"></a>

### [`009b6c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b6c7c.md) → [`009b6e18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b6/009b6e18.md) FUN_009b6e18

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "009b6e30",
      "incomplete_value": false,
      "site": "009b6e3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:110:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b6c94",
      "incomplete_value": false,
      "site": "009b6ca0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c88000:8"
          ],
          [
            "leaf",
            "const:d10:8"
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
      "009b6e3c",
      "DATA",
      [
        "storage",
        "00c88d10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b6e3c",
      "DATA",
      [
        "storage",
        "00c89110",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b6c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b6c7c.md#insn-009b6c90) · [`009b6c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b6c7c.md#insn-009b6c94) · [`009b6cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b6c7c.md#insn-009b6cc4)
- 新版 `009b6e2c`（命令位置の公開資料なし） · `009b6e30`（命令位置の公開資料なし） · `009b6e60`（命令位置の公開資料なし）

~~~diff
- 009b6c90 ["COPY", "register:4040:8", ["const:c88000:8"]]
+ 009b6e2c ["COPY", "register:4040:8", ["const:c89000:8"]]
- 009b6c90 bytes 881600d0
+ 009b6e2c bytes 881600f0
- 009b6c94 ["COPY", "tmp:0:8", ["const:d10:8"]]
- 009b6c94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009b6c94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009b6c94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009b6e30 ["COPY", "tmp:0:8", ["const:110:8"]]
+ 009b6e30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009b6e30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009b6e30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009b6c94 bytes 08413491
+ 009b6e30 bytes 08410491
- 009b6cc4 ["COPY", "register:0:8", ["register:4040:8"]]
- 009b6cc4 ["INT_ADD", "register:40f0:8", ["const:9b6cc4:8", "const:4:8"]]
- 009b6cc4 ["CALLIND", null, ["register:0:8"]]
+ 009b6e60 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009b6e60 ["INT_ADD", "register:40f0:8", ["const:9b6e60:8", "const:4:8"]]
+ 009b6e60 ["CALLIND", null, ["register:0:8"]]
- 009b6cc4 bytes 00013fd6
+ 009b6e60 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-198ed08a97d052db4d0e4d8df9e831e2"></a>

### [`009b6cd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b6cd8.md) → [`009b6e74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b6/009b6e74.md) FUN_009b6e74

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009b6ea0",
      "incomplete_value": false,
      "site": "009b6ea0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:110:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b6d04",
      "incomplete_value": false,
      "site": "009b6d04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c88000:8"
          ],
          [
            "leaf",
            "const:d10:8"
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
      "009b6ea0",
      "DATA",
      [
        "storage",
        "00c88d10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b6ea0",
      "DATA",
      [
        "storage",
        "00c89110",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b6cec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b6cd8.md#insn-009b6cec) · [`009b6cf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b6cd8.md#insn-009b6cf8) · [`009b6cfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b6cd8.md#insn-009b6cfc)
- 新版 `009b6e88`（命令位置の公開資料なし） · `009b6e94`（命令位置の公開資料なし） · `009b6e98`（命令位置の公開資料なし）

~~~diff
- 009b6cec ["INT_ADD", "register:40f0:8", ["const:9b6cec:8", "const:4:8"]]
- 009b6cec ["CALL", null, ["callee:00c57e90:8"]]
+ 009b6e88 ["INT_ADD", "register:40f0:8", ["const:9b6e88:8", "const:4:8"]]
+ 009b6e88 ["CALL", null, ["callee:00c57e90:8"]]
- 009b6cec bytes 69830a94
+ 009b6e88 bytes 02840a94
- 009b6cf8 ["COPY", "register:4040:8", ["const:c88000:8"]]
+ 009b6e94 ["COPY", "register:4040:8", ["const:c89000:8"]]
- 009b6cf8 bytes 881600d0
+ 009b6e94 bytes 881600f0
- 009b6cfc ["COPY", "tmp:0:8", ["const:d10:8"]]
- 009b6cfc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009b6cfc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009b6cfc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009b6e98 ["COPY", "tmp:0:8", ["const:110:8"]]
+ 009b6e98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009b6e98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009b6e98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009b6cfc bytes 08413491
+ 009b6e98 bytes 08410491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0e5a06d91361ed54a9738a8c24260b8"></a>

### [`009b6d60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b6d60.md) → [`009b6efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b6/009b6efc.md) FUN_009b6efc

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009b6f18",
      "incomplete_value": false,
      "site": "009b6f18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:110:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b6d7c",
      "incomplete_value": false,
      "site": "009b6d7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c88000:8"
          ],
          [
            "leaf",
            "const:d10:8"
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
      "009b6f18",
      "DATA",
      [
        "storage",
        "00c88d10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b6f18",
      "DATA",
      [
        "storage",
        "00c89110",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b6d74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b6d60.md#insn-009b6d74) · [`009b6d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b6d60.md#insn-009b6d78) · [`009b6d9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b6d60.md#insn-009b6d9c)
- 新版 `009b6f10`（命令位置の公開資料なし） · `009b6f14`（命令位置の公開資料なし） · `009b6f38`（命令位置の公開資料なし）

~~~diff
- 009b6d74 ["COPY", "register:4048:8", ["const:c88000:8"]]
+ 009b6f10 ["COPY", "register:4048:8", ["const:c89000:8"]]
- 009b6d74 bytes 891600d0
+ 009b6f10 bytes 891600f0
- 009b6d78 ["COPY", "tmp:0:8", ["const:d10:8"]]
- 009b6d78 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 009b6d78 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 009b6d78 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 009b6f14 ["COPY", "tmp:0:8", ["const:110:8"]]
+ 009b6f14 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 009b6f14 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 009b6f14 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 009b6d78 bytes 29413491
+ 009b6f14 bytes 29410491
- 009b6d9c ["COPY", "register:0:8", ["register:4048:8"]]
- 009b6d9c ["INT_ADD", "register:40f0:8", ["const:9b6d9c:8", "const:4:8"]]
- 009b6d9c ["CALLIND", null, ["register:0:8"]]
+ 009b6f38 ["COPY", "register:0:8", ["register:4048:8"]]
+ 009b6f38 ["INT_ADD", "register:40f0:8", ["const:9b6f38:8", "const:4:8"]]
+ 009b6f38 ["CALLIND", null, ["register:0:8"]]
- 009b6d9c bytes 20013fd6
+ 009b6f38 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f4b31cd892814dd4db754edaf6cf80e"></a>

### [`009b6e0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b6e0c.md) → [`009b6fa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b6/009b6fa8.md) FUN_009b6fa8

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`009b4c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b4/009b4c90.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`009b4e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b4/009b4e2c.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 71.43% / 新版 62.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009b6e48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b6/009b6e0c.md#insn-009b6e48)
- 新版 `009b6fe4`（命令位置の公開資料なし）

~~~diff
- 009b6e48 ["COPY", "register:0:8", ["register:4040:8"]]
- 009b6e48 ["INT_ADD", "register:40f0:8", ["const:9b6e48:8", "const:4:8"]]
- 009b6e48 ["CALLIND", null, ["register:0:8"]]
+ 009b6fe4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009b6fe4 ["INT_ADD", "register:40f0:8", ["const:9b6fe4:8", "const:4:8"]]
+ 009b6fe4 ["CALLIND", null, ["register:0:8"]]
- 009b6e48 bytes 00013fd6
+ 009b6fe4 bytes 00013fd6
~~~


<a id="compare-14351fe8ab1714c82859634961267058"></a>

### [`009b7078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7078.md) → [`009b7214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b7/009b7214.md) FUN_009b7214

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "009b7220",
      "incomplete_value": false,
      "site": "009b722c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:190:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b7084",
      "incomplete_value": false,
      "site": "009b7090",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c88000:8"
          ],
          [
            "leaf",
            "const:d90:8"
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
      "009b722c",
      "DATA",
      [
        "storage",
        "00c88d90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b722c",
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

- 旧版 [`009b7080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7078.md#insn-009b7080) · [`009b7084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7078.md#insn-009b7084)
- 新版 `009b721c`（命令位置の公開資料なし） · `009b7220`（命令位置の公開資料なし）

~~~diff
- 009b7080 ["COPY", "register:4050:8", ["const:c88000:8"]]
+ 009b721c ["COPY", "register:4050:8", ["const:c89000:8"]]
- 009b7080 bytes 8a1600b0
+ 009b721c bytes 8a1600d0
- 009b7084 ["COPY", "tmp:0:8", ["const:d90:8"]]
- 009b7084 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 009b7084 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 009b7084 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 009b7220 ["COPY", "tmp:0:8", ["const:190:8"]]
+ 009b7220 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 009b7220 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 009b7220 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 009b7084 bytes 4a413691
+ 009b7220 bytes 4a410691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7de8823f038f41ee791432aa0952dc55"></a>

### [`009b7118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7118.md) → [`009b72b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b7/009b72b4.md) FUN_009b72b4

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009b72e0",
      "incomplete_value": false,
      "site": "009b72e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:190:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b7144",
      "incomplete_value": false,
      "site": "009b7144",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c88000:8"
          ],
          [
            "leaf",
            "const:d90:8"
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
      "009b72e0",
      "DATA",
      [
        "storage",
        "00c88d90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b72e0",
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

- 旧版 [`009b712c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7118.md#insn-009b712c) · [`009b7138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7118.md#insn-009b7138) · [`009b713c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7118.md#insn-009b713c)
- 新版 `009b72c8`（命令位置の公開資料なし） · `009b72d4`（命令位置の公開資料なし） · `009b72d8`（命令位置の公開資料なし）

~~~diff
- 009b712c ["INT_ADD", "register:40f0:8", ["const:9b712c:8", "const:4:8"]]
- 009b712c ["CALL", null, ["callee:00c57e90:8"]]
+ 009b72c8 ["INT_ADD", "register:40f0:8", ["const:9b72c8:8", "const:4:8"]]
+ 009b72c8 ["CALL", null, ["callee:00c57e90:8"]]
- 009b712c bytes 59820a94
+ 009b72c8 bytes f2820a94
- 009b7138 ["COPY", "register:4040:8", ["const:c88000:8"]]
+ 009b72d4 ["COPY", "register:4040:8", ["const:c89000:8"]]
- 009b7138 bytes 881600b0
+ 009b72d4 bytes 881600d0
- 009b713c ["COPY", "tmp:0:8", ["const:d90:8"]]
- 009b713c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009b713c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009b713c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009b72d8 ["COPY", "tmp:0:8", ["const:190:8"]]
+ 009b72d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009b72d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009b72d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009b713c bytes 08413691
+ 009b72d8 bytes 08410691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4275656a846720ab14fe60ae16f483ad"></a>

### [`009b71a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b71a0.md) → [`009b733c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b7/009b733c.md) FUN_009b733c

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 66.67% / 新版 57.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009b7358",
      "incomplete_value": false,
      "site": "009b7358",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:190:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b71bc",
      "incomplete_value": false,
      "site": "009b71bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c88000:8"
          ],
          [
            "leaf",
            "const:d90:8"
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
      "009b7358",
      "DATA",
      [
        "storage",
        "00c88d90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b7358",
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

- 旧版 [`009b71b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b71a0.md#insn-009b71b4) · [`009b71b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b71a0.md#insn-009b71b8) · [`009b71c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b71a0.md#insn-009b71c0)
- 新版 `009b7350`（命令位置の公開資料なし） · `009b7354`（命令位置の公開資料なし） · `009b735c`（命令位置の公開資料なし）

~~~diff
- 009b71b4 ["COPY", "register:4048:8", ["const:c88000:8"]]
+ 009b7350 ["COPY", "register:4048:8", ["const:c89000:8"]]
- 009b71b4 bytes 891600b0
+ 009b7350 bytes 891600d0
- 009b71b8 ["COPY", "tmp:0:8", ["const:d90:8"]]
- 009b71b8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 009b71b8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 009b71b8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 009b7354 ["COPY", "tmp:0:8", ["const:190:8"]]
+ 009b7354 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 009b7354 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 009b7354 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 009b71b8 bytes 29413691
+ 009b7354 bytes 29410691
- 009b71c0 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 009b71c0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 009b735c ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 009b735c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 009b71c0 bytes 480100b4
+ 009b735c bytes 480100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7415d515de41db8c3bdcc23212a77052"></a>

### [`009b7338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7338.md) → [`009b74d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b7/009b74d4.md) FUN_009b74d4

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "009b74e0",
      "incomplete_value": false,
      "site": "009b74ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:210:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b7344",
      "incomplete_value": false,
      "site": "009b7350",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c88000:8"
          ],
          [
            "leaf",
            "const:e10:8"
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
      "009b74ec",
      "DATA",
      [
        "storage",
        "00c88e10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b74ec",
      "DATA",
      [
        "storage",
        "00c89210",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b7340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7338.md#insn-009b7340) · [`009b7344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7338.md#insn-009b7344)
- 新版 `009b74dc`（命令位置の公開資料なし） · `009b74e0`（命令位置の公開資料なし）

~~~diff
- 009b7340 ["COPY", "register:4050:8", ["const:c88000:8"]]
+ 009b74dc ["COPY", "register:4050:8", ["const:c89000:8"]]
- 009b7340 bytes 8a1600b0
+ 009b74dc bytes 8a1600d0
- 009b7344 ["COPY", "tmp:0:8", ["const:e10:8"]]
- 009b7344 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 009b7344 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 009b7344 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 009b74e0 ["COPY", "tmp:0:8", ["const:210:8"]]
+ 009b74e0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 009b74e0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 009b74e0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 009b7344 bytes 4a413891
+ 009b74e0 bytes 4a410891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1833b24045b9bc04ccd5e4bb0b422e7"></a>

### [`009b737c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b737c.md) → [`009b7518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b7/009b7518.md) FUN_009b7518

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "009b7530",
      "incomplete_value": false,
      "site": "009b753c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:210:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b7394",
      "incomplete_value": false,
      "site": "009b73a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c88000:8"
          ],
          [
            "leaf",
            "const:e10:8"
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
      "009b753c",
      "DATA",
      [
        "storage",
        "00c88e10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b753c",
      "DATA",
      [
        "storage",
        "00c89210",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b7390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b737c.md#insn-009b7390) · [`009b7394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b737c.md#insn-009b7394) · [`009b73c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b737c.md#insn-009b73c4)
- 新版 `009b752c`（命令位置の公開資料なし） · `009b7530`（命令位置の公開資料なし） · `009b7560`（命令位置の公開資料なし）

~~~diff
- 009b7390 ["COPY", "register:4040:8", ["const:c88000:8"]]
+ 009b752c ["COPY", "register:4040:8", ["const:c89000:8"]]
- 009b7390 bytes 881600b0
+ 009b752c bytes 881600d0
- 009b7394 ["COPY", "tmp:0:8", ["const:e10:8"]]
- 009b7394 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009b7394 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009b7394 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009b7530 ["COPY", "tmp:0:8", ["const:210:8"]]
+ 009b7530 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009b7530 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009b7530 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009b7394 bytes 08413891
+ 009b7530 bytes 08410891
- 009b73c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 009b73c4 ["INT_ADD", "register:40f0:8", ["const:9b73c4:8", "const:4:8"]]
- 009b73c4 ["CALLIND", null, ["register:0:8"]]
+ 009b7560 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009b7560 ["INT_ADD", "register:40f0:8", ["const:9b7560:8", "const:4:8"]]
+ 009b7560 ["CALLIND", null, ["register:0:8"]]
- 009b73c4 bytes 00013fd6
+ 009b7560 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9bdb9736b3c6585e59475e029817c7e"></a>

### [`009b73d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b73d8.md) → [`009b7574`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b7/009b7574.md) FUN_009b7574

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009b75a0",
      "incomplete_value": false,
      "site": "009b75a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:210:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b7404",
      "incomplete_value": false,
      "site": "009b7404",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c88000:8"
          ],
          [
            "leaf",
            "const:e10:8"
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
      "009b75a0",
      "DATA",
      [
        "storage",
        "00c88e10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b75a0",
      "DATA",
      [
        "storage",
        "00c89210",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b73ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b73d8.md#insn-009b73ec) · [`009b73f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b73d8.md#insn-009b73f8) · [`009b73fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b73d8.md#insn-009b73fc)
- 新版 `009b7588`（命令位置の公開資料なし） · `009b7594`（命令位置の公開資料なし） · `009b7598`（命令位置の公開資料なし）

~~~diff
- 009b73ec ["INT_ADD", "register:40f0:8", ["const:9b73ec:8", "const:4:8"]]
- 009b73ec ["CALL", null, ["callee:00c57e90:8"]]
+ 009b7588 ["INT_ADD", "register:40f0:8", ["const:9b7588:8", "const:4:8"]]
+ 009b7588 ["CALL", null, ["callee:00c57e90:8"]]
- 009b73ec bytes a9810a94
+ 009b7588 bytes 42820a94
- 009b73f8 ["COPY", "register:4040:8", ["const:c88000:8"]]
+ 009b7594 ["COPY", "register:4040:8", ["const:c89000:8"]]
- 009b73f8 bytes 881600b0
+ 009b7594 bytes 881600d0
- 009b73fc ["COPY", "tmp:0:8", ["const:e10:8"]]
- 009b73fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009b73fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009b73fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009b7598 ["COPY", "tmp:0:8", ["const:210:8"]]
+ 009b7598 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009b7598 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009b7598 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009b73fc bytes 08413891
+ 009b7598 bytes 08410891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3b9dd4ca4cedbf0e6c00dc477b10c10"></a>

### [`009b7460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7460.md) → [`009b75fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b7/009b75fc.md) FUN_009b75fc

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009b7618",
      "incomplete_value": false,
      "site": "009b7618",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:210:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b747c",
      "incomplete_value": false,
      "site": "009b747c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c88000:8"
          ],
          [
            "leaf",
            "const:e10:8"
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
      "009b7618",
      "DATA",
      [
        "storage",
        "00c88e10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b7618",
      "DATA",
      [
        "storage",
        "00c89210",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b7474`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7460.md#insn-009b7474) · [`009b7478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7460.md#insn-009b7478) · [`009b749c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7460.md#insn-009b749c)
- 新版 `009b7610`（命令位置の公開資料なし） · `009b7614`（命令位置の公開資料なし） · `009b7638`（命令位置の公開資料なし）

~~~diff
- 009b7474 ["COPY", "register:4048:8", ["const:c88000:8"]]
+ 009b7610 ["COPY", "register:4048:8", ["const:c89000:8"]]
- 009b7474 bytes 891600b0
+ 009b7610 bytes 891600d0
- 009b7478 ["COPY", "tmp:0:8", ["const:e10:8"]]
- 009b7478 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 009b7478 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 009b7478 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 009b7614 ["COPY", "tmp:0:8", ["const:210:8"]]
+ 009b7614 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 009b7614 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 009b7614 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 009b7478 bytes 29413891
+ 009b7614 bytes 29410891
- 009b749c ["COPY", "register:0:8", ["register:4048:8"]]
- 009b749c ["INT_ADD", "register:40f0:8", ["const:9b749c:8", "const:4:8"]]
- 009b749c ["CALLIND", null, ["register:0:8"]]
+ 009b7638 ["COPY", "register:0:8", ["register:4048:8"]]
+ 009b7638 ["INT_ADD", "register:40f0:8", ["const:9b7638:8", "const:4:8"]]
+ 009b7638 ["CALLIND", null, ["register:0:8"]]
- 009b749c bytes 20013fd6
+ 009b7638 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0ed086e29307a803f53c8752eef5961"></a>

### [`009b771c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b771c.md) → [`009b78b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b7/009b78b8.md) FUN_009b78b8

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "009b78c4",
      "incomplete_value": false,
      "site": "009b78d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:290:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b7728",
      "incomplete_value": false,
      "site": "009b7734",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c88000:8"
          ],
          [
            "leaf",
            "const:e90:8"
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
      "009b78d0",
      "DATA",
      [
        "storage",
        "00c88e90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b78d0",
      "DATA",
      [
        "storage",
        "00c89290",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b7724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b771c.md#insn-009b7724) · [`009b7728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b771c.md#insn-009b7728)
- 新版 `009b78c0`（命令位置の公開資料なし） · `009b78c4`（命令位置の公開資料なし）

~~~diff
- 009b7724 ["COPY", "register:4050:8", ["const:c88000:8"]]
+ 009b78c0 ["COPY", "register:4050:8", ["const:c89000:8"]]
- 009b7724 bytes 8a1600b0
+ 009b78c0 bytes 8a1600d0
- 009b7728 ["COPY", "tmp:0:8", ["const:e90:8"]]
- 009b7728 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 009b7728 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 009b7728 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 009b78c4 ["COPY", "tmp:0:8", ["const:290:8"]]
+ 009b78c4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 009b78c4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 009b78c4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 009b7728 bytes 4a413a91
+ 009b78c4 bytes 4a410a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-130088f8fb0f5fedd2300437ac8a7096"></a>

### [`009b7760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7760.md) → [`009b78fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b7/009b78fc.md) FUN_009b78fc

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "009b7914",
      "incomplete_value": false,
      "site": "009b7920",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:290:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b7778",
      "incomplete_value": false,
      "site": "009b7784",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c88000:8"
          ],
          [
            "leaf",
            "const:e90:8"
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
      "009b7920",
      "DATA",
      [
        "storage",
        "00c88e90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b7920",
      "DATA",
      [
        "storage",
        "00c89290",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b7774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7760.md#insn-009b7774) · [`009b7778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7760.md#insn-009b7778) · [`009b77a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7760.md#insn-009b77a8)
- 新版 `009b7910`（命令位置の公開資料なし） · `009b7914`（命令位置の公開資料なし） · `009b7944`（命令位置の公開資料なし）

~~~diff
- 009b7774 ["COPY", "register:4040:8", ["const:c88000:8"]]
+ 009b7910 ["COPY", "register:4040:8", ["const:c89000:8"]]
- 009b7774 bytes 881600b0
+ 009b7910 bytes 881600d0
- 009b7778 ["COPY", "tmp:0:8", ["const:e90:8"]]
- 009b7778 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009b7778 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009b7778 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009b7914 ["COPY", "tmp:0:8", ["const:290:8"]]
+ 009b7914 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009b7914 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009b7914 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009b7778 bytes 08413a91
+ 009b7914 bytes 08410a91
- 009b77a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 009b77a8 ["INT_ADD", "register:40f0:8", ["const:9b77a8:8", "const:4:8"]]
- 009b77a8 ["CALLIND", null, ["register:0:8"]]
+ 009b7944 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009b7944 ["INT_ADD", "register:40f0:8", ["const:9b7944:8", "const:4:8"]]
+ 009b7944 ["CALLIND", null, ["register:0:8"]]
- 009b77a8 bytes 00013fd6
+ 009b7944 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e049c73048605510c458e54ca3a2599"></a>

### [`009b77bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b77bc.md) → [`009b7958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b7/009b7958.md) FUN_009b7958

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_value, unresolved_return_alignment

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 62.50% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009b7984",
      "incomplete_value": false,
      "site": "009b7984",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:290:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b77e8",
      "incomplete_value": false,
      "site": "009b77e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c88000:8"
          ],
          [
            "leaf",
            "const:e90:8"
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
      "site": "009b782c"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "009b79c8"
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
      "009b7984",
      "DATA",
      [
        "storage",
        "00c88e90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b7984",
      "DATA",
      [
        "storage",
        "00c89290",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b782c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b77bc.md#insn-009b782c) · [`009b77d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b77bc.md#insn-009b77d0)
- 新版 `009b79c8`（命令位置の公開資料なし） · `009b796c`（命令位置の公開資料なし）

~~~diff
- 009b782c ["COPY", "register:0:8", ["register:40f0:8"]]
- 009b782c ["RETURN", null, ["register:0:8"]]
- 009b782c bytes c0035fd6
+ 009b79c8 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 009b79c8 ["RETURN", null, ["register:0:8"]]
+ 009b79c8 bytes c0035fd6
- 009b77d0 ["INT_ADD", "register:40f0:8", ["const:9b77d0:8", "const:4:8"]]
- 009b77d0 ["CALL", null, ["callee:00c57e90:8"]]
+ 009b796c ["INT_ADD", "register:40f0:8", ["const:9b796c:8", "const:4:8"]]
+ 009b796c ["CALL", null, ["callee:00c57e90:8"]]
- 009b77d0 bytes b0800a94
+ 009b796c bytes 49810a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17d5c236786e732641d60d90cf2df69f"></a>

### [`009b7844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7844.md) → [`009b79e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b7/009b79e0.md) FUN_009b79e0

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 44.44% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b7860"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009b79fc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "009b7864"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009b7860",
      "DATA",
      [
        "storage",
        "00c88e90",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:009b7864",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b7a28"
      ]
    ]
  ],
  "added": [
    [
      "009b79fc",
      "DATA",
      [
        "storage",
        "00c89290",
        null,
        "undefined *"
      ]
    ],
    [
      "009b7a00",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b7a28"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b7860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7844.md#insn-009b7860) · [`009b7864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7844.md#insn-009b7864)
- 新版 `009b79fc`（命令位置の公開資料なし）

~~~diff
- 009b7860 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 009b7860 ["COPY", "tmp:1:8", ["register:4008:8"]]
- 009b7860 ["INT_ADD", "register:4008:8", ["register:4008:8", "const:10:8"]]
- 009b7860 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 009b7860 bytes 290401f8
- 009b7864 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 009b7864 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 009b7864 bytes 480100b4
+ 009b79fc ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 009b79fc ["COPY", "tmp:1:8", ["register:4008:8"]]
+ 009b79fc ["INT_ADD", "register:4008:8", ["register:4008:8", "const:10:8"]]
+ 009b79fc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 009b79fc bytes 290401f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0fe1684620430b0ad117653c2bae114"></a>

### [`009b7c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7c00.md) → [`009b7d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b7/009b7d9c.md) FUN_009b7d9c

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 2件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "009b7c04"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "009b7da0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "CONDITIONAL_JUMP",
        "009b7c04"
      ],
      [
        "CONDITIONAL_JUMP",
        "009b7da0"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "009b7da0",
      "incomplete_value": true,
      "site": "009b7db0",
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
      "definition_site": "009b7c04",
      "incomplete_value": true,
      "site": "009b7c14",
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
      "unmatched:009b7c04",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b7db0"
      ]
    ]
  ],
  "added": [
    [
      "009b7da0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b7db0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b7c04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7c00.md#insn-009b7c04) · [`009b7c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7c00.md#insn-009b7c00)
- 新版 `009b7da0`（命令位置の公開資料なし）

~~~diff
- 009b7c04 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 009b7c04 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 009b7c04 bytes 800000b4
+ 009b7da0 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 009b7da0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 009b7da0 bytes 800000b4
- 009b7c00 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:30:8"]]
- 009b7c00 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 009b7c00 bytes 001840f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80ed1baebd21c8158c0a80447789f445"></a>

### [`009b7c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7c48.md) → [`009b7de4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b7/009b7de4.md) FUN_009b7de4

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009b3fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b3/009b3fc8.md) · 呼出先 7件 [`00597e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e90.md) [`005b72fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b72fc.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`009b4164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b4/009b4164.md) · 呼出先 7件 [`00597ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ed0.md) [`005b733c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b7/005b733c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment

命令の説明率　旧版 93.51% / 新版 93.51%

CFGの説明率　旧版 73.33% / 新版 78.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 2件, `store_value` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009b7e1c",
      "incomplete_value": false,
      "site": "009b7e24",
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
            "const:5c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b7c80",
      "incomplete_value": false,
      "site": "009b7c88",
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
            "const:1c0:8"
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
      "site": "009b7ce0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "009b7e7c"
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
      "009b7e24",
      "DATA",
      [
        "storage",
        "00c701c0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:009b7ce0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b7eec"
      ]
    ],
    [
      "009b7edc",
      "READ",
      [
        "storage",
        "00c701d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b7e24",
      "DATA",
      [
        "storage",
        "00c705c0",
        null,
        "pointer"
      ]
    ],
    [
      "009b7e7c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b7eec"
      ]
    ],
    [
      "009b7edc",
      "READ",
      [
        "storage",
        "00c705d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b7ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7c48.md#insn-009b7ce0) · [`009b7c78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7c48.md#insn-009b7c78)
- 新版 `009b7e7c`（命令位置の公開資料なし） · `009b7e14`（命令位置の公開資料なし）

~~~diff
- 009b7ce0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 009b7ce0 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 009b7ce0 bytes 81030054
+ 009b7e7c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 009b7e7c ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 009b7e7c bytes 81030054
- 009b7c78 ["INT_ADD", "register:40f0:8", ["const:9b7c78:8", "const:4:8"]]
- 009b7c78 ["CALL", null, ["callee:00c57e90:8"]]
+ 009b7e14 ["INT_ADD", "register:40f0:8", ["const:9b7e14:8", "const:4:8"]]
+ 009b7e14 ["CALL", null, ["callee:00c57e90:8"]]
- 009b7c78 bytes 867f0a94
+ 009b7e14 bytes 1f800a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c0176fbb9ed5112ee0ec26a8978ab71"></a>

### [`009b7dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7dc0.md) → [`009b7f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b7/009b7f5c.md) FUN_009b7f5c

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "009b7f68",
      "incomplete_value": false,
      "site": "009b7f74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:390:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b7dcc",
      "incomplete_value": false,
      "site": "009b7dd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c88000:8"
          ],
          [
            "leaf",
            "const:f90:8"
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
      "009b7f74",
      "DATA",
      [
        "storage",
        "00c88f90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b7f74",
      "DATA",
      [
        "storage",
        "00c89390",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b7dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7dc0.md#insn-009b7dc8) · [`009b7dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7dc0.md#insn-009b7dcc)
- 新版 `009b7f64`（命令位置の公開資料なし） · `009b7f68`（命令位置の公開資料なし）

~~~diff
- 009b7dc8 ["COPY", "register:4050:8", ["const:c88000:8"]]
+ 009b7f64 ["COPY", "register:4050:8", ["const:c89000:8"]]
- 009b7dc8 bytes 8a1600b0
+ 009b7f64 bytes 8a1600d0
- 009b7dcc ["COPY", "tmp:0:8", ["const:f90:8"]]
- 009b7dcc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 009b7dcc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 009b7dcc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 009b7f68 ["COPY", "tmp:0:8", ["const:390:8"]]
+ 009b7f68 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 009b7f68 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 009b7f68 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 009b7dcc bytes 4a413e91
+ 009b7f68 bytes 4a410e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd2a5a58b35bbd3bc87a3c7eb075df81"></a>

### [`009b7e04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7e04.md) → [`009b7fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b7/009b7fa0.md) FUN_009b7fa0

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "009b7fb8",
      "incomplete_value": false,
      "site": "009b7fc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:390:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b7e1c",
      "incomplete_value": false,
      "site": "009b7e28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c88000:8"
          ],
          [
            "leaf",
            "const:f90:8"
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
      "009b7fc4",
      "DATA",
      [
        "storage",
        "00c88f90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b7fc4",
      "DATA",
      [
        "storage",
        "00c89390",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b7e18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7e04.md#insn-009b7e18) · [`009b7e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7e04.md#insn-009b7e1c) · [`009b7e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7e04.md#insn-009b7e4c)
- 新版 `009b7fb4`（命令位置の公開資料なし） · `009b7fb8`（命令位置の公開資料なし） · `009b7fe8`（命令位置の公開資料なし）

~~~diff
- 009b7e18 ["COPY", "register:4040:8", ["const:c88000:8"]]
+ 009b7fb4 ["COPY", "register:4040:8", ["const:c89000:8"]]
- 009b7e18 bytes 881600b0
+ 009b7fb4 bytes 881600d0
- 009b7e1c ["COPY", "tmp:0:8", ["const:f90:8"]]
- 009b7e1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009b7e1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009b7e1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009b7fb8 ["COPY", "tmp:0:8", ["const:390:8"]]
+ 009b7fb8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009b7fb8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009b7fb8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009b7e1c bytes 08413e91
+ 009b7fb8 bytes 08410e91
- 009b7e4c ["COPY", "register:0:8", ["register:4040:8"]]
- 009b7e4c ["INT_ADD", "register:40f0:8", ["const:9b7e4c:8", "const:4:8"]]
- 009b7e4c ["CALLIND", null, ["register:0:8"]]
+ 009b7fe8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009b7fe8 ["INT_ADD", "register:40f0:8", ["const:9b7fe8:8", "const:4:8"]]
+ 009b7fe8 ["CALLIND", null, ["register:0:8"]]
- 009b7e4c bytes 00013fd6
+ 009b7fe8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14a9f5b34ec55be44bb5bbf9d654e408"></a>

### [`009b7e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7e60.md) → [`009b7ffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b7/009b7ffc.md) FUN_009b7ffc

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 86.21% / 新版 86.21%

CFGの説明率　旧版 62.50% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009b8028",
      "incomplete_value": false,
      "site": "009b8028",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:390:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b7e8c",
      "incomplete_value": false,
      "site": "009b7e8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c88000:8"
          ],
          [
            "leaf",
            "const:f90:8"
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
      "site": "009b7ec0"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "009b805c"
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
      "009b8028",
      "DATA",
      [
        "storage",
        "00c88f90",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:009b7ec0",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "009b8028",
      "DATA",
      [
        "storage",
        "00c89390",
        null,
        "undefined *"
      ]
    ],
    [
      "009b805c",
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

- 旧版 [`009b7ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7e60.md#insn-009b7ec0) · [`009b7e74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7e60.md#insn-009b7e74)
- 新版 `009b805c`（命令位置の公開資料なし） · `009b8010`（命令位置の公開資料なし）

~~~diff
- 009b7ec0 ["COPY", "register:0:8", ["register:4040:8"]]
- 009b7ec0 ["INT_ADD", "register:40f0:8", ["const:9b7ec0:8", "const:4:8"]]
- 009b7ec0 ["CALLIND", null, ["register:0:8"]]
- 009b7ec0 bytes 00013fd6
+ 009b805c ["COPY", "register:0:8", ["register:4040:8"]]
+ 009b805c ["INT_ADD", "register:40f0:8", ["const:9b805c:8", "const:4:8"]]
+ 009b805c ["CALLIND", null, ["register:0:8"]]
+ 009b805c bytes 00013fd6
- 009b7e74 ["INT_ADD", "register:40f0:8", ["const:9b7e74:8", "const:4:8"]]
- 009b7e74 ["CALL", null, ["callee:00c57e90:8"]]
+ 009b8010 ["INT_ADD", "register:40f0:8", ["const:9b8010:8", "const:4:8"]]
+ 009b8010 ["CALL", null, ["callee:00c57e90:8"]]
- 009b7e74 bytes 077f0a94
+ 009b8010 bytes a07f0a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-397ea092fb8c514b306a702c84bd6a7f"></a>

### [`009b7ee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7ee8.md) → [`009b8084`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b8/009b8084.md) FUN_009b8084

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment

命令の説明率　旧版 82.76% / 新版 82.76%

CFGの説明率　旧版 50.00% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 2件, `store_value` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009b80a0",
      "incomplete_value": false,
      "site": "009b80a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:390:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b7f04",
      "incomplete_value": false,
      "site": "009b7f04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c88000:8"
          ],
          [
            "leaf",
            "const:f90:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "009b7f14"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "009b80b0"
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
      "009b80a0",
      "DATA",
      [
        "storage",
        "00c88f90",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:009b7f14",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b80dc"
      ]
    ]
  ],
  "added": [
    [
      "009b80a0",
      "DATA",
      [
        "storage",
        "00c89390",
        null,
        "undefined *"
      ]
    ],
    [
      "009b80b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b80dc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b7f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7ee8.md#insn-009b7f14) · [`009b7efc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b7/009b7ee8.md#insn-009b7efc)
- 新版 `009b80b0`（命令位置の公開資料なし） · `009b8098`（命令位置の公開資料なし）

~~~diff
- 009b7f14 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
- 009b7f14 bytes 60010054
+ 009b80b0 ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
+ 009b80b0 bytes 60010054
- 009b7efc ["COPY", "register:4048:8", ["const:c88000:8"]]
+ 009b8098 ["COPY", "register:4048:8", ["const:c89000:8"]]
- 009b7efc bytes 891600b0
+ 009b8098 bytes 891600b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-604341768d50a8e47a798ec570076dc5"></a>

### [`009b8080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b8/009b8080.md) → [`009b821c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b8/009b821c.md) FUN_009b821c

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "009b8228",
      "incomplete_value": false,
      "site": "009b8234",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:410:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b808c",
      "incomplete_value": false,
      "site": "009b8098",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
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
      "009b8234",
      "DATA",
      [
        "storage",
        "00c89010",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b8234",
      "DATA",
      [
        "storage",
        "00c89410",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b808c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b8/009b8080.md#insn-009b808c)
- 新版 `009b8228`（命令位置の公開資料なし）

~~~diff
- 009b808c ["COPY", "tmp:0:8", ["const:10:8"]]
- 009b808c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 009b808c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 009b808c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 009b8228 ["COPY", "tmp:0:8", ["const:410:8"]]
+ 009b8228 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 009b8228 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 009b8228 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 009b808c bytes 4a410091
+ 009b8228 bytes 4a411091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7378b18ecc4f268e683ea01f45e81eae"></a>

### [`009b81a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b8/009b81a8.md) → [`009b8344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b8/009b8344.md) FUN_009b8344

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 66.67% / 新版 57.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b81c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009b8360"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "009b81c8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009b81c4",
      "DATA",
      [
        "storage",
        "00c89010",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:009b81c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b838c"
      ]
    ]
  ],
  "added": [
    [
      "009b8360",
      "DATA",
      [
        "storage",
        "00c89410",
        null,
        "undefined *"
      ]
    ],
    [
      "009b8364",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009b838c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b81c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b8/009b81a8.md#insn-009b81c4) · [`009b81c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b8/009b81a8.md#insn-009b81c8)
- 新版 `009b8360`（命令位置の公開資料なし）

~~~diff
- 009b81c4 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 009b81c4 ["COPY", "tmp:1:8", ["register:4008:8"]]
- 009b81c4 ["INT_ADD", "register:4008:8", ["register:4008:8", "const:10:8"]]
- 009b81c4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 009b81c4 bytes 290401f8
- 009b81c8 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 009b81c8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 009b81c8 bytes 480100b4
+ 009b8360 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 009b8360 ["COPY", "tmp:1:8", ["register:4008:8"]]
+ 009b8360 ["INT_ADD", "register:4008:8", ["register:4008:8", "const:10:8"]]
+ 009b8360 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 009b8360 bytes 290401f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66695c9fc05fd87380d35045a8329a59"></a>

### [`009b8254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b8/009b8254.md) → [`009b83f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b8/009b83f0.md) FUN_009b83f0

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`009b3fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b3/009b3fc8.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`009b4164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b4/009b4164.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 62.50% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009b8290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b8/009b8254.md#insn-009b8290)
- 新版 `009b842c`（命令位置の公開資料なし）

~~~diff
- 009b8290 ["COPY", "register:0:8", ["register:4040:8"]]
- 009b8290 ["INT_ADD", "register:40f0:8", ["const:9b8290:8", "const:4:8"]]
- 009b8290 ["CALLIND", null, ["register:0:8"]]
+ 009b842c ["COPY", "register:0:8", ["register:4040:8"]]
+ 009b842c ["INT_ADD", "register:40f0:8", ["const:9b842c:8", "const:4:8"]]
+ 009b842c ["CALLIND", null, ["register:0:8"]]
- 009b8290 bytes 00013fd6
+ 009b842c bytes 00013fd6
~~~


<a id="compare-cf8ba853ce003465dfcd6a07fdba2790"></a>

### [`009b82ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b8/009b82ec.md) → [`009b8488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b8/009b8488.md) _INIT_197

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 69.49% / 新版 69.49%

CFGの説明率　旧版 75.00% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_store_alignment` 20件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b831c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b8330"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b8334"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009b831c",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:009b8328",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "unmatched:009b8330",
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
      "009b84b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "009b84c4",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "009b84cc",
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

- 旧版 [`009b831c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b8/009b82ec.md#insn-009b831c) · [`009b8330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b8/009b82ec.md#insn-009b8330) · [`009b8334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b8/009b82ec.md#insn-009b8334)

~~~diff
- 009b831c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 009b831c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 009b831c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 009b831c bytes a9831ff8
- 009b8330 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 009b8330 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:21:8"]]
- 009b8330 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 009b8330 bytes ea130278
- 009b8334 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 009b8334 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 009b8334 bytes e92b00b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a62aa6d82b3a96254caa96477d6f15a9"></a>

### [`009b867c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b8/009b867c.md) → [`009b8818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b8/009b8818.md) FUN_009b8818

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) · 呼出先 2件 [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 1件 [`0075eb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075eb80.md) · 呼出先 2件 [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.24% / 新版 95.24%

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
      "site": "009b8830",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009b8694",
      "value": [
        "leaf",
        "ram:46c984:8"
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
      "009b8830",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ]
  ],
  "added": [
    [
      "009b8830",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b8694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b8/009b867c.md#insn-009b8694) · [`009b86bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b8/009b867c.md#insn-009b86bc)
- 新版 `009b8830`（命令位置の公開資料なし） · `009b8858`（命令位置の公開資料なし）

~~~diff
- 009b8694 ["INT_ADD", "register:40f0:8", ["const:9b8694:8", "const:4:8"]]
- 009b8694 ["CALL", null, ["ram:46c984:8"]]
+ 009b8830 ["INT_ADD", "register:40f0:8", ["const:9b8830:8", "const:4:8"]]
+ 009b8830 ["CALL", null, ["ram:46c9c4:8"]]
- 009b8694 bytes bcd0ea97
+ 009b8830 bytes 65d0ea97
- 009b86bc ["INT_ADD", "register:40f0:8", ["const:9b86bc:8", "const:4:8"]]
- 009b86bc ["CALL", null, ["callee:00c53cd0:8"]]
+ 009b8858 ["INT_ADD", "register:40f0:8", ["const:9b8858:8", "const:4:8"]]
+ 009b8858 ["CALL", null, ["callee:00c53cd0:8"]]
- 009b86bc bytes 7d6c0a94
+ 009b8858 bytes 1e6d0a94
~~~


<a id="compare-31dd36d1716649ccb21bdb677ad3d80b"></a>

### [`009b873c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b8/009b873c.md) → [`009b88d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b8/009b88d8.md) FUN_009b88d8

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) · 呼出先 13件 [`00935400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/00935400.md) [`00935ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/00935ca0.md) [`009ad9cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ad/009ad9cc.md) [`009b89b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b8/009b89b4.md) [`009b9050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b9/009b9050.md)
- 新版 呼出元 1件 [`0075eb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075eb80.md) · 呼出先 13件 [`0093559c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00935/0093559c.md) [`00935e3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00935/00935e3c.md) [`009adb68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ad/009adb68.md) [`009b8b50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b8/009b8b50.md) [`009b91ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b9/009b91ec.md)

変更の種類 branch_condition_or_target, call, call_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_value

命令の説明率　旧版 97.66% / 新版 97.66%

CFGの説明率　旧版 81.82% / 新版 79.41%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009b8a38",
      "incomplete_value": false,
      "site": "009b8a38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:490:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b889c",
      "incomplete_value": false,
      "site": "009b889c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:90:8"
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
      "site": "009b89c4",
      "value": [
        "leaf",
        "ram:93559c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009b8828",
      "value": [
        "leaf",
        "ram:935400:8"
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
      "009b89c4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00935400"
      ]
    ],
    [
      "009b8a38",
      "DATA",
      [
        "storage",
        "00c89090",
        null,
        "undefined *"
      ]
    ],
    [
      "009b8a70",
      "READ",
      [
        "storage",
        "00c890b0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "009b89c4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0093559c"
      ]
    ],
    [
      "009b8a38",
      "DATA",
      [
        "storage",
        "00c89490",
        null,
        "undefined *"
      ]
    ],
    [
      "009b8a70",
      "READ",
      [
        "storage",
        "00c894b0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b8828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b8/009b873c.md#insn-009b8828) · [`009b8778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b8/009b873c.md#insn-009b8778) · [`009b8790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b8/009b873c.md#insn-009b8790)
- 新版 `009b89c4`（命令位置の公開資料なし） · `009b8914`（命令位置の公開資料なし） · `009b892c`（命令位置の公開資料なし）

~~~diff
- 009b8828 ["INT_ADD", "register:40f0:8", ["const:9b8828:8", "const:4:8"]]
- 009b8828 ["CALL", null, ["ram:935400:8"]]
+ 009b89c4 ["INT_ADD", "register:40f0:8", ["const:9b89c4:8", "const:4:8"]]
+ 009b89c4 ["CALL", null, ["ram:93559c:8"]]
- 009b8828 bytes f6f2fd97
+ 009b89c4 bytes f6f2fd97
- 009b8778 ["INT_ADD", "register:40f0:8", ["const:9b8778:8", "const:4:8"]]
- 009b8778 ["CALL", null, ["callee:009b8b50:8"]]
+ 009b8914 ["INT_ADD", "register:40f0:8", ["const:9b8914:8", "const:4:8"]]
+ 009b8914 ["CALL", null, ["callee:009b8b50:8"]]
- 009b8778 bytes 8f000094
+ 009b8914 bytes 8f000094
- 009b8790 ["INT_ADD", "register:40f0:8", ["const:9b8790:8", "const:4:8"]]
- 009b8790 ["CALL", null, ["callee:009b91ec:8"]]
+ 009b892c ["INT_ADD", "register:40f0:8", ["const:9b892c:8", "const:4:8"]]
+ 009b892c ["CALL", null, ["callee:009b91ec:8"]]
- 009b8790 bytes 30020094
+ 009b892c bytes 30020094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71a3c675310a2bfe9b89f54228ad6d66"></a>

### [`009b89b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b8/009b89b4.md) → [`009b8b50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b8/009b8b50.md) FUN_009b8b50

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009b873c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b8/009b873c.md) · 呼出先 20件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0047c928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047c928.md) [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047e89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e89c.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md)
- 新版 呼出元 1件 [`009b88d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b8/009b88d8.md) · 呼出先 20件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0047c968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047c968.md) [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047e8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e8dc.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 82.86% / 新版 82.86%

CFGの説明率　旧版 74.60% / 新版 70.68%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `call_target` 1件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 20件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b89b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b89b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b89bc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009b89b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:009b89bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:009b89c0",
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
      "009b8b54",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "009b8b58",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "009b8b5c",
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

- 旧版 [`009b89b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b8/009b89b4.md#insn-009b89b8) · [`009b89bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b8/009b89b4.md#insn-009b89bc) · [`009b89c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b8/009b89b4.md#insn-009b89c0)

~~~diff
- 009b89b8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 009b89b8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 009b89b8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:c0:8"]]
- 009b89b8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009b89b8 bytes fd7b0ca9
- 009b89bc ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 009b89bc ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 009b89bc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:d0:8"]]
- 009b89bc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009b89bc bytes fc6f0da9
- 009b89c0 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 009b89c0 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 009b89c0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:e0:8"]]
- 009b89c0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009b89c0 bytes fa670ea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c311f5543e6a718c10155ed3b703ea6b"></a>

### [`009b9050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b9/009b9050.md) → [`009b91ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b9/009b91ec.md) FUN_009b91ec

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009b873c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b8/009b873c.md) · 呼出先 12件 [`00489f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f0c.md) [`005d8b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8b88.md) [`008b6efc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6efc.md) [`008b6fa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6fa8.md) [`009ba1d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ba/009ba1d8.md)
- 新版 呼出元 1件 [`009b88d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b8/009b88d8.md) · 呼出先 12件 [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md) [`005d8bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8bc8.md) [`008b6f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f40.md) [`008b6fec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6fec.md) [`009ba374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ba/009ba374.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 88.73% / 新版 88.73%

CFGの説明率　旧版 81.82% / 新版 90.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_store_alignment` 16件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b9054"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b9058"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009b9058"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009b9054",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "unmatched:009b9058",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:009b905c",
      "WRITE",
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
      "009b91f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "009b91f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "009b91f8",
      "WRITE",
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

- 旧版 [`009b9054`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b9/009b9050.md#insn-009b9054) · [`009b9058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b9/009b9050.md#insn-009b9058) · [`009b905c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b9/009b9050.md#insn-009b905c)

~~~diff
- 009b9054 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:50:8"]]
- 009b9054 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5100:8"]]
- 009b9054 bytes e82b00fd
- 009b9058 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 009b9058 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 009b9058 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 009b9058 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009b9058 bytes fd7b06a9
- 009b905c ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 009b905c ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 009b905c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 009b905c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009b905c bytes fc6f07a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1751e9a86d35c6be87dc3deb2b7d1e0e"></a>

### [`009b95a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b9/009b95a4.md) → [`009b9740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b9/009b9740.md) FUN_009b9740

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00773854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/00773854.md) · 呼出先 24件 [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`004687c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/004687c4.md) [`00468c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468c28.md) [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md) [`0046961c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/0046961c.md)
- 新版 呼出元 1件 [`00773894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00773/00773894.md) · 呼出先 24件 [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00468804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468804.md) [`00468c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468c68.md) [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`0046965c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/0046965c.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.99% / 新版 98.99%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009b9980",
      "value": [
        "leaf",
        "ram:9a9770:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009b97e4",
      "value": [
        "leaf",
        "ram:9a95d4:8"
      ]
    },
    "ordinal": 19,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009b9998",
      "value": [
        "leaf",
        "ram:9a9770:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009b97fc",
      "value": [
        "leaf",
        "ram:9a95d4:8"
      ]
    },
    "ordinal": 20,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009b9b70",
      "value": [
        "leaf",
        "ram:9a9770:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009b99d4",
      "value": [
        "leaf",
        "ram:9a95d4:8"
      ]
    },
    "ordinal": 36,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009b9980",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "009a95d4"
      ]
    ],
    [
      "009b9998",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "009a95d4"
      ]
    ],
    [
      "009b9b70",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "009a95d4"
      ]
    ]
  ],
  "added": [
    [
      "009b9980",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "009a9770"
      ]
    ],
    [
      "009b9998",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "009a9770"
      ]
    ],
    [
      "009b9b70",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "009a9770"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b97e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b9/009b95a4.md#insn-009b97e4) · [`009b97fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b9/009b95a4.md#insn-009b97fc) · [`009b99d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b9/009b95a4.md#insn-009b99d4)
- 新版 `009b9980`（命令位置の公開資料なし） · `009b9998`（命令位置の公開資料なし） · `009b9b70`（命令位置の公開資料なし）

~~~diff
- 009b97e4 ["INT_ADD", "register:40f0:8", ["const:9b97e4:8", "const:4:8"]]
- 009b97e4 ["CALL", null, ["ram:9a95d4:8"]]
+ 009b9980 ["INT_ADD", "register:40f0:8", ["const:9b9980:8", "const:4:8"]]
+ 009b9980 ["CALL", null, ["ram:9a9770:8"]]
- 009b97e4 bytes 7cbfff97
+ 009b9980 bytes 7cbfff97
- 009b97fc ["INT_ADD", "register:40f0:8", ["const:9b97fc:8", "const:4:8"]]
- 009b97fc ["CALL", null, ["ram:9a95d4:8"]]
+ 009b9998 ["INT_ADD", "register:40f0:8", ["const:9b9998:8", "const:4:8"]]
+ 009b9998 ["CALL", null, ["ram:9a9770:8"]]
- 009b97fc bytes 76bfff97
+ 009b9998 bytes 76bfff97
- 009b99d4 ["INT_ADD", "register:40f0:8", ["const:9b99d4:8", "const:4:8"]]
- 009b99d4 ["CALL", null, ["ram:9a95d4:8"]]
+ 009b9b70 ["INT_ADD", "register:40f0:8", ["const:9b9b70:8", "const:4:8"]]
+ 009b9b70 ["CALL", null, ["ram:9a9770:8"]]
- 009b99d4 bytes 00bfff97
+ 009b9b70 bytes 00bfff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f172f9c5bd785151e08c4e6222ac6deb"></a>

### [`009b9c64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b9/009b9c64.md) → [`009b9e00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b9/009b9e00.md) FUN_009b9e00

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009b95a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b9/009b95a4.md) · 呼出先 6件 [`00468f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f0c.md) [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md) [`0046aecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046aecc.md) [`0046da1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046da1c.md) [`00489f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f0c.md)
- 新版 呼出元 1件 [`009b9740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b9/009b9740.md) · 呼出先 6件 [`00468f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f4c.md) [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`0046af0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046af0c.md) [`0046da5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046da5c.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.20% / 新版 97.20%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009b9e70",
      "incomplete_value": true,
      "site": "009b9ea4",
      "value": [
        "live",
        "register:40b0:8"
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
      "definition_site": "009b9e78",
      "incomplete_value": false,
      "site": "009b9ea4",
      "value": [
        "leaf",
        "const:9:8"
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`009b9d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b9/009b9c64.md#insn-009b9d08) · [`009b9cbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b9/009b9c64.md#insn-009b9cbc) · [`009b9ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b9/009b9c64.md#insn-009b9ce8)
- 新版 `009b9ea4`（命令位置の公開資料なし） · `009b9e58`（命令位置の公開資料なし）

~~~diff
- 009b9d08 ["INT_ADD", "register:40f0:8", ["const:9b9d08:8", "const:4:8"]]
- 009b9d08 ["CALL", null, ["callee:00489f4c:8"]]
+ 009b9ea4 ["INT_ADD", "register:40f0:8", ["const:9b9ea4:8", "const:4:8"]]
+ 009b9ea4 ["CALL", null, ["callee:00489f4c:8"]]
- 009b9d08 bytes 8140eb97
+ 009b9ea4 bytes 2a40eb97
- 009b9cbc ["INT_ADD", "register:40f0:8", ["const:9b9cbc:8", "const:4:8"]]
- 009b9cbc ["CALL", null, ["callee:00468f88:8"]]
+ 009b9e58 ["INT_ADD", "register:40f0:8", ["const:9b9e58:8", "const:4:8"]]
+ 009b9e58 ["CALL", null, ["callee:00468f88:8"]]
- 009b9cbc bytes a3bcea97
+ 009b9e58 bytes 4cbcea97
- 009b9ce8 ["INT_RIGHT", "register:4050:8", ["register:4048:8", "const:3f:8"]]
- 009b9ce8 bytes 2afd7fd3
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd06ef8cc2d8dd32e0daed662d3075d2"></a>

### [`009b9edc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b9/009b9edc.md) → [`009ba078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ba/009ba078.md) FUN_009ba078

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "009ba09c",
      "incomplete_value": false,
      "site": "009ba09c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:490:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b9f00",
      "incomplete_value": false,
      "site": "009b9f00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:90:8"
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
      "009ba09c",
      "DATA",
      [
        "storage",
        "00c89090",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009ba09c",
      "DATA",
      [
        "storage",
        "00c89490",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b9ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b9/009b9edc.md#insn-009b9ef0) · [`009b9efc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b9/009b9edc.md#insn-009b9efc)
- 新版 `009ba08c`（命令位置の公開資料なし） · `009ba098`（命令位置の公開資料なし）

~~~diff
- 009b9ef0 ["INT_ADD", "register:40f0:8", ["const:9b9ef0:8", "const:4:8"]]
- 009b9ef0 ["CALL", null, ["callee:00c57e90:8"]]
+ 009ba08c ["INT_ADD", "register:40f0:8", ["const:9ba08c:8", "const:4:8"]]
+ 009ba08c ["CALL", null, ["callee:00c57e90:8"]]
- 009b9ef0 bytes e8760a94
+ 009ba08c bytes 81770a94
- 009b9efc ["COPY", "tmp:0:8", ["const:90:8"]]
- 009b9efc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009b9efc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009b9efc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009ba098 ["COPY", "tmp:0:8", ["const:490:8"]]
+ 009ba098 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009ba098 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009ba098 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009b9efc bytes 08410291
+ 009ba098 bytes 08411291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e191e5f10c36a3d395c32b22abdc893"></a>

### [`009b9f10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b9/009b9f10.md) → [`009ba0ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ba/009ba0ac.md) FUN_009ba0ac

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009ba0b8",
      "incomplete_value": false,
      "site": "009ba0b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:490:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b9f1c",
      "incomplete_value": false,
      "site": "009b9f1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:90:8"
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
      "009ba0b8",
      "DATA",
      [
        "storage",
        "00c89090",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009ba0b8",
      "DATA",
      [
        "storage",
        "00c89490",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b9f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b9/009b9f10.md#insn-009b9f18)
- 新版 `009ba0b4`（命令位置の公開資料なし）

~~~diff
- 009b9f18 ["COPY", "tmp:0:8", ["const:90:8"]]
- 009b9f18 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 009b9f18 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 009b9f18 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 009ba0b4 ["COPY", "tmp:0:8", ["const:490:8"]]
+ 009ba0b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 009ba0b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 009ba0b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 009b9f18 bytes 29410291
+ 009ba0b4 bytes 29411291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d876aa02e49df1b8b4f4f92c29475af"></a>

### [`009ba028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ba/009ba028.md) → [`009ba1c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ba/009ba1c4.md) FUN_009ba1c4

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`009b89b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009b8/009b89b4.md) [`00a9f828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a9f/00a9f828.md) · 呼出先 7件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0063670c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/0063670c.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 2件 [`009b8b50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009b8/009b8b50.md) [`00a9fa24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a9f/00a9fa24.md) · 呼出先 7件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0063674c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00636/0063674c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 67.82% / 新版 67.82%

CFGの説明率　旧版 39.39% / 新版 37.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009ba028"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009ba028"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009ba02c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009ba028",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:009ba02c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:009ba030",
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
      "009ba1c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "009ba1c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "009ba1cc",
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

- 旧版 [`009ba028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ba/009ba028.md#insn-009ba028) · [`009ba02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ba/009ba028.md#insn-009ba02c) · [`009ba030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ba/009ba028.md#insn-009ba030)

~~~diff
- 009ba028 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 009ba028 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 009ba028 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 009ba028 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 009ba028 bytes fd7bbba9
- 009ba02c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 009ba02c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 009ba02c bytes f90b00f9
- 009ba030 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 009ba030 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 009ba030 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 009ba030 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009ba030 bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6240a6ca0958c8db3cbf367e4777b9a9"></a>

### [`009ba1c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ba/009ba1c0.md) → [`009ba35c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ba/009ba35c.md) FUN_009ba35c

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009ba360",
      "incomplete_value": false,
      "site": "009ba364",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:510:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ba1c4",
      "incomplete_value": false,
      "site": "009ba1c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:110:8"
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
      "009ba364",
      "DATA",
      [
        "storage",
        "00c89110",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009ba364",
      "DATA",
      [
        "storage",
        "00c89510",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009ba1c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ba/009ba1c0.md#insn-009ba1c4)
- 新版 `009ba360`（命令位置の公開資料なし）

~~~diff
- 009ba1c4 ["COPY", "tmp:0:8", ["const:110:8"]]
- 009ba1c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009ba1c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009ba1c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009ba360 ["COPY", "tmp:0:8", ["const:510:8"]]
+ 009ba360 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009ba360 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009ba360 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009ba1c4 bytes 08410491
+ 009ba360 bytes 08411491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-834d23152d90e7634c7fe1f57c8a9ecf"></a>

### [`009ba264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ba/009ba264.md) → [`009ba400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ba/009ba400.md) _INIT_198

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00bc43c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc43c8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00bc47f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc47f0.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 62.04% / 新版 62.04%

CFGの説明率　旧版 37.14% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 30件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009ba294"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009ba2bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009ba2e0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009ba294",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:009ba2a0",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "unmatched:009ba2bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10f]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009ba430",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "009ba43c",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "009ba458",
      "WRITE",
      [
        "storage",
        "Stack[-0x10f]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009ba294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ba/009ba264.md#insn-009ba294) · [`009ba2bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ba/009ba264.md#insn-009ba2bc) · [`009ba2e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ba/009ba264.md#insn-009ba2e0)

~~~diff
- 009ba294 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 009ba294 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 009ba294 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 009ba294 bytes a9831ff8
- 009ba2bc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:11:8"]]
- 009ba2bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 009ba2bc bytes e013813c
- 009ba2e0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:31:8"]]
- 009ba2e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 009ba2e0 bytes e013833c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb3fd3276b250c3761f46f30ad5c2635"></a>

### [`009ba7c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ba/009ba7c0.md) → [`009ba95c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ba/009ba95c.md) FUN_009ba95c

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009bcee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bc/009bcee4.md) · 呼出先 17件 [`0044f8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f8a0.md) [`00454ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00454/00454ce8.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`00764344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764344.md) [`00764ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764ea0.md)
- 新版 呼出元 1件 [`009bd080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009bd/009bd080.md) · 呼出先 17件 [`0044f8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f8e0.md) [`00454d28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00454/00454d28.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00764384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/00764384.md) [`00764ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/00764ee0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 72.73% / 新版 72.73%

CFGの説明率　旧版 32.20% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 7件, `unresolved_store_alignment` 19件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009ba7c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009ba7c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009ba7c8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009ba7c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:009ba7c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:009ba7cc",
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
      "009ba960",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "009ba964",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "009ba968",
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

- 旧版 [`009ba7c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ba/009ba7c0.md#insn-009ba7c4) · [`009ba7c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ba/009ba7c0.md#insn-009ba7c8) · [`009ba7cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ba/009ba7c0.md#insn-009ba7cc)

~~~diff
- 009ba7c4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 009ba7c4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 009ba7c4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:d0:8"]]
- 009ba7c4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009ba7c4 bytes fd7b0da9
- 009ba7c8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:e0:8"]]
- 009ba7c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40e0:8"]]
- 009ba7c8 bytes fc7300f9
- 009ba7cc ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 009ba7cc ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 009ba7cc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:f0:8"]]
- 009ba7cc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009ba7cc bytes f85f0fa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8baf43de17bfe5acb0c9d1e7a8313e9d"></a>

### [`009bab64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ba/009bab64.md) → [`009bad00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ba/009bad00.md) FUN_009bad00

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009bd99c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bd/009bd99c.md) · 呼出先 24件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`0046e4f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e4f8.md) [`0047c928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047c928.md) [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md)
- 新版 呼出元 1件 [`009bdb38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009bd/009bdb38.md) · 呼出先 24件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`0046e538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e538.md) [`0047c968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047c968.md) [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 59.31% / 新版 59.31%

CFGの説明率　旧版 25.57% / 新版 25.41%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 50件, `call_target` 1件, `unresolved_branch_alignment` 36件, `unresolved_call_alignment` 96件, `unresolved_store_alignment` 80件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009babac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009babf0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009babf4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009babac",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "unmatched:009babc4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009baed8"
      ]
    ],
    [
      "unmatched:009babd0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009bb110"
      ]
    ]
  ],
  "added": [
    [
      "009bad48",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "009bad60",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009baed8"
      ]
    ],
    [
      "009bad6c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009bb110"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009babac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ba/009bab64.md#insn-009babac) · [`009babf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ba/009bab64.md#insn-009babf0) · [`009babf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ba/009bab64.md#insn-009babf4)

~~~diff
- 009babac ["COPY", "tmp:0:8", ["register:4040:8"]]
- 009babac ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffe8:8"]]
- 009babac ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 009babac bytes a8831ef8
- 009babf0 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 009babf0 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffb8:8"]]
- 009babf0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 009babf0 bytes a8831b38
- 009babf4 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 009babf4 ["INT_ADD", "tmp:1:8", ["register:40c0:8", "const:b9:8"]]
- 009babf4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 009babf4 bytes 0a930b78
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6047d1414b90dc54c3b645e860700b98"></a>

### [`009bcbbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bc/009bcbbc.md) → [`009bcd58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009bc/009bcd58.md) FUN_009bcd58

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`009bd99c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bd/009bd99c.md) [`009bdae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bd/009bdae4.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 2件 [`009bdb38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009bd/009bdb38.md) [`009bdc80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009bd/009bdc80.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 82.43% / 新版 82.43%

CFGの説明率　旧版 42.31% / 新版 42.31%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "009bcbe4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "009bcc80"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "009bcca4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009bce40",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009bcd9c"
      ]
    ],
    [
      "unmatched:009bcbe0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c53d00"
      ]
    ],
    [
      "unmatched:009bcbe4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009bcd9c"
      ]
    ]
  ],
  "added": [
    [
      "009bcd70",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009bcd9c"
      ]
    ],
    [
      "009bcd7c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c53d00"
      ]
    ],
    [
      "009bcd80",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009bcd9c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009bcbe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bc/009bcbbc.md#insn-009bcbe0) · [`009bcbe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bc/009bcbbc.md#insn-009bcbe4) · [`009bcc80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bc/009bcbbc.md#insn-009bcc80)

~~~diff
- 009bcbe0 ["INT_ADD", "register:40f0:8", ["const:9bcbe0:8", "const:4:8"]]
- 009bcbe0 ["CALL", null, ["callee:00c53d00:8"]]
- 009bcbe0 bytes 405b0a94
- 009bcbe4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 009bcbe4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 009bcbe4 bytes e00000b5
- 009bcc80 ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 009bcc80 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 009bcc80 bytes e00000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c797baf0fff5143ce86b28834a78495b"></a>

### [`009bcce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bc/009bcce4.md) → [`009bce80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009bc/009bce80.md) FUN_009bce80

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009c03f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c0/009c03f0.md) · 呼出先 7件 [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`006c0d94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c0/006c0d94.md) [`006c0ed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c0/006c0ed0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`009bf078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bf/009bf078.md)
- 新版 呼出元 1件 [`009c058c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c0/009c058c.md) · 呼出先 7件 [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`006c0dd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c0/006c0dd4.md) [`006c0f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c0/006c0f10.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`009bf214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009bf/009bf214.md)

変更の種類 branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 95.31% / 新版 95.31%

CFGの説明率　旧版 38.46% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 10件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "009bceac",
      "incomplete_value": true,
      "site": "009bceac",
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
      "definition_site": "009bcd10",
      "incomplete_value": true,
      "site": "009bcd10",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009bceb4",
      "incomplete_value": false,
      "site": "009bcec8",
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
            "const:e58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009bcd18",
      "incomplete_value": false,
      "site": "009bcd2c",
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
            "const:a58:8"
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
    "new": {
      "definition_site": "009bcebc",
      "incomplete_value": false,
      "site": "009bcec8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:680:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009bcd20",
      "incomplete_value": false,
      "site": "009bcd2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:280:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009bcea4",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "009bceb4",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009bcebc",
      "PARAM",
      [
        "storage",
        "00c89280",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "009bcea4",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "009bceb4",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009bcebc",
      "PARAM",
      [
        "storage",
        "00c89680",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009bcd2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bc/009bcce4.md#insn-009bcd2c) · [`009bcd44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bc/009bcce4.md#insn-009bcd44) · [`009bcde0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bc/009bcce4.md#insn-009bcde0)
- 新版 `009bcec8`（命令位置の公開資料なし） · `009bcf7c`（命令位置の公開資料なし）

~~~diff
- 009bcd2c ["INT_ADD", "register:40f0:8", ["const:9bcd2c:8", "const:4:8"]]
- 009bcd2c ["CALL", null, ["callee:00c58610:8"]]
+ 009bcec8 ["INT_ADD", "register:40f0:8", ["const:9bcec8:8", "const:4:8"]]
+ 009bcec8 ["CALL", null, ["callee:00c58610:8"]]
- 009bcd2c bytes 396d0a94
+ 009bcec8 bytes d26d0a94
- 009bcd44 ["INT_ADD", "register:40f0:8", ["const:9bcd44:8", "const:4:8"]]
- 009bcd44 ["CALL", null, ["ram:46c984:8"]]
- 009bcd44 bytes 10bfea97
- 009bcde0 ["INT_ADD", "register:40f0:8", ["const:9bcde0:8", "const:4:8"]]
- 009bcde0 ["CALL", null, ["callee:00c58430:8"]]
+ 009bcf7c ["INT_ADD", "register:40f0:8", ["const:9bcf7c:8", "const:4:8"]]
+ 009bcf7c ["CALL", null, ["callee:00c58430:8"]]
- 009bcde0 bytes 946c0a94
+ 009bcf7c bytes 2d6d0a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96f33ffd8c9e4824c51c6b43ff7a0cde"></a>

### [`009bcee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bc/009bcee4.md) → [`009bd080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009bd/009bd080.md) FUN_009bd080

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009bdee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bd/009bdee0.md) · 呼出先 8件 [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`006c0ef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c0/006c0ef8.md) [`00764344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764344.md) [`00768398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/00768398.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`009be07c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009be/009be07c.md) · 呼出先 8件 [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`006c0f38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c0/006c0f38.md) [`00764384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/00764384.md) [`007683d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00768/007683d8.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 83.49% / 新版 83.49%

CFGの説明率　旧版 33.33% / 新版 32.26%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 8件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009bcf04"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "009bd0a0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "009bcfd0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009bcf04",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:009bcf08",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514f8"
      ]
    ],
    [
      "unmatched:009bcf0c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ]
  ],
  "added": [
    [
      "009bd0a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "009bd0a4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514f8"
      ]
    ],
    [
      "009bd0a8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009bcf04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bc/009bcee4.md#insn-009bcf04) · [`009bcf08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bc/009bcee4.md#insn-009bcf08) · [`009bcf0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bc/009bcee4.md#insn-009bcf0c)

~~~diff
- 009bcf04 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 009bcf04 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 009bcf04 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 009bcf04 bytes a8831ff8
- 009bcf08 ["INT_ADD", "register:40f0:8", ["const:9bcf08:8", "const:4:8"]]
- 009bcf08 ["CALL", null, ["callee:008514f8:8"]]
- 009bcf08 bytes 6c51fa97
- 009bcf0c ["INT_ADD", "register:40f0:8", ["const:9bcf0c:8", "const:4:8"]]
- 009bcf0c ["CALL", null, ["ram:46c984:8"]]
- 009bcf0c bytes 9ebeea97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e62b3be8a544089e4daa36a62e7681b"></a>

### [`009bd0c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bd/009bd0c4.md) → [`009bd260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009bd/009bd260.md) FUN_009bd260

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009be144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009be/009be144.md) · 呼出先 9件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`00467f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467f14.md) [`004687c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/004687c4.md) [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md)
- 新版 呼出元 1件 [`009be2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009be/009be2e0.md) · 呼出先 9件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00467f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467f54.md) [`00468804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468804.md) [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 94.49% / 新版 94.49%

CFGの説明率　旧版 32.35% / 新版 34.38%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 14件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "009bd27c",
      "incomplete_value": true,
      "site": "009bd27c",
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
      "definition_site": "009bd0e0",
      "incomplete_value": true,
      "site": "009bd0e0",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "009bd278"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "009bd280"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009bd278",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "009bd284",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009bd28c",
      "PARAM",
      [
        "storage",
        "00c89280",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "009bd278",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "009bd284",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009bd28c",
      "PARAM",
      [
        "storage",
        "00c89680",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009bd0dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bd/009bd0c4.md#insn-009bd0dc) · [`009bd0fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bd/009bd0c4.md#insn-009bd0fc) · [`009bd12c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bd/009bd0c4.md#insn-009bd12c)
- 新版 `009bd278`（命令位置の公開資料なし） · `009bd298`（命令位置の公開資料なし） · `009bd2c8`（命令位置の公開資料なし）

~~~diff
- 009bd0dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:578:8"]]
- 009bd0dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 009bd278 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:978:8"]]
+ 009bd278 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 009bd0dc bytes 08bd42f9
+ 009bd278 bytes 08bd44f9
- 009bd0fc ["INT_ADD", "register:40f0:8", ["const:9bd0fc:8", "const:4:8"]]
- 009bd0fc ["CALL", null, ["callee:00c58610:8"]]
+ 009bd298 ["INT_ADD", "register:40f0:8", ["const:9bd298:8", "const:4:8"]]
+ 009bd298 ["CALL", null, ["callee:00c58610:8"]]
- 009bd0fc bytes 456c0a94
+ 009bd298 bytes de6c0a94
- 009bd12c ["INT_ADD", "register:40f0:8", ["const:9bd12c:8", "const:4:8"]]
- 009bd12c ["CALL", null, ["callee:00468f88:8"]]
+ 009bd2c8 ["INT_ADD", "register:40f0:8", ["const:9bd2c8:8", "const:4:8"]]
+ 009bd2c8 ["CALL", null, ["callee:00468f88:8"]]
- 009bd12c bytes 87afea97
+ 009bd2c8 bytes 30afea97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aaf477483cd958fa4c767509d589c1f0"></a>

### [`009bd2c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bd/009bd2c0.md) → [`009bd45c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009bd/009bd45c.md) FUN_009bd45c

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0088f45c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088f45c.md) [`00a99ed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a99/00a99ed8.md) · 呼出先 8件 [`006649ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/006649ac.md) [`00689914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00689/00689914.md) [`0071c420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071c/0071c420.md) [`007287a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00728/007287a8.md) [`00737c34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00737/00737c34.md)
- 新版 呼出元 2件 [`0088f49c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f49c.md) [`00a9a0d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a9a/00a9a0d0.md) · 呼出先 8件 [`006649ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/006649ec.md) [`00689954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00689/00689954.md) [`0071c460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071c/0071c460.md) [`007287e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00728/007287e8.md) [`00737c74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00737/00737c74.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 86.11% / 新版 86.11%

CFGの説明率　旧版 62.96% / 新版 64.15%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "009bd48c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "009bd628"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "009bd4ac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009bd4f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009bd73c"
      ]
    ],
    [
      "unmatched:009bd48c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009bd77c"
      ]
    ],
    [
      "unmatched:009bd4ac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071c420"
      ]
    ]
  ],
  "added": [
    [
      "009bd4f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009bd734"
      ]
    ],
    [
      "009bd628",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009bd77c"
      ]
    ],
    [
      "009bd648",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071c460"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009bd48c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bd/009bd2c0.md#insn-009bd48c) · [`009bd4ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bd/009bd2c0.md#insn-009bd4ac) · [`009bd5a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bd/009bd2c0.md#insn-009bd5a4)

~~~diff
- 009bd48c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 009bd48c ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 009bd48c ["CBRANCH", null, ["local:b33:8", "tmp:1:1"]]
- 009bd48c bytes a90a0054
- 009bd4ac ["INT_ADD", "register:40f0:8", ["const:9bd4ac:8", "const:4:8"]]
- 009bd4ac ["CALL", null, ["ram:71c420:8"]]
- 009bd4ac bytes dd7bf597
- 009bd5a4 ["INT_ADD", "register:40f0:8", ["const:9bd5a4:8", "const:4:8"]]
- 009bd5a4 ["CALL", null, ["ram:71c420:8"]]
- 009bd5a4 bytes 9f7bf597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4805c722c75113ab9a7f5bd1394c66c9"></a>

### [`009bd650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bd/009bd650.md) → [`009bd7ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009bd/009bd7ec.md) FUN_009bd7ec

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009bdb9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bd/009bdb9c.md) · 呼出先 15件 [`0044f8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f8a0.md) [`00454804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00454/00454804.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`00764344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764344.md) [`00764ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764ea0.md)
- 新版 呼出元 1件 [`009bdd38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009bd/009bdd38.md) · 呼出先 15件 [`0044f8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f8e0.md) [`00454844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00454/00454844.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00764384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/00764384.md) [`00764ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/00764ee0.md)

変更の種類 branch_condition_or_target, call, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 82.05% / 新版 82.05%

CFGの説明率　旧版 64.44% / 新版 67.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 6件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009bd670"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009bd848",
      "incomplete_value": true,
      "site": "009bd848",
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
                "const:2c0000:8"
              ],
              [
                "leaf",
                "const:2b5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009bd6ac",
      "incomplete_value": true,
      "site": "009bd6ac",
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
                "const:2c0000:8"
              ],
              [
                "leaf",
                "const:275:8"
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
      "definition_site": "009bd84c",
      "incomplete_value": true,
      "site": "009bd84c",
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
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009bd6b0",
      "incomplete_value": true,
      "site": "009bd6b0",
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
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009bd670",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "009bd834",
      "READ",
      [
        "storage",
        "002c0275",
        null,
        "string"
      ]
    ],
    [
      "009bd83c",
      "READ",
      [
        "storage",
        "002c027b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009bd80c",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "009bd834",
      "READ",
      [
        "storage",
        "002c02b5",
        null,
        "string"
      ]
    ],
    [
      "009bd83c",
      "READ",
      [
        "storage",
        "002c02bb",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009bd670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bd/009bd650.md#insn-009bd670) · [`009bd674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bd/009bd650.md#insn-009bd674) · [`009bd72c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bd/009bd650.md#insn-009bd72c)
- 新版 `009bd810`（命令位置の公開資料なし）

~~~diff
- 009bd670 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 009bd670 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 009bd670 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 009bd670 bytes a8831ff8
- 009bd674 ["INT_ADD", "register:40f0:8", ["const:9bd674:8", "const:4:8"]]
- 009bd674 ["CALL", null, ["callee:008514f8:8"]]
+ 009bd810 ["INT_ADD", "register:40f0:8", ["const:9bd810:8", "const:4:8"]]
+ 009bd810 ["CALL", null, ["callee:008514f8:8"]]
- 009bd674 bytes 914ffa97
+ 009bd810 bytes 3a4ffa97
- 009bd72c ["INT_ADD", "register:40f0:8", ["const:9bd72c:8", "const:4:8"]]
- 009bd72c ["CALL", null, ["callee:00c57eb0:8"]]
- 009bd72c bytes e1680a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5a710e8295cc50e51b322e7913284d1"></a>

### [`009bd99c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bd/009bd99c.md) → [`009bdb38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009bd/009bdb38.md) FUN_009bdb38

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`009bdb9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bd/009bdb9c.md) [`009bdee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bd/009bdee0.md) [`009c03f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c0/009c03f0.md) · 呼出先 7件 [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`00498190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498190.md) [`009bab64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ba/009bab64.md) [`009bcbbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bc/009bcbbc.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md)
- 新版 呼出元 3件 [`009bdd38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009bd/009bdd38.md) [`009be07c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009be/009be07c.md) [`009c058c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c0/009c058c.md) · 呼出先 7件 [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`004981d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/004981d0.md) [`009bad00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ba/009bad00.md) [`009bcd58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009bc/009bcd58.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 60.98% / 新版 60.98%

CFGの説明率　旧版 3.03% / 新版 4.35%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009bd9d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009bdab8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009bdabc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009bd9c0",
      "READ",
      [
        "storage",
        "00ca421c",
        null,
        "undefined4"
      ]
    ],
    [
      "009bdb64",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:009bda48"
      ]
    ],
    [
      "unmatched:009bd9d8",
      "WRITE",
      [
        "storage",
        "00ca421c",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "009bdb5c",
      "READ",
      [
        "storage",
        "00ca461c",
        null,
        "undefined4"
      ]
    ],
    [
      "009bdb64",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009bdbe4"
      ]
    ],
    [
      "009bdb74",
      "WRITE",
      [
        "storage",
        "00ca461c",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009bd9d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bd/009bd99c.md#insn-009bd9d8) · [`009bda1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bd/009bd99c.md#insn-009bda1c) · [`009bda38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bd/009bd99c.md#insn-009bda38)

~~~diff
- 009bd9d8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:21c:8"]]
- 009bd9d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 009bd9d8 bytes 891e02b9
- 009bda1c ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 009bda1c ["CBRANCH", null, ["local:b18:8", "tmp:0:1"]]
- 009bda1c bytes 6a010054
- 009bda38 ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 009bda38 ["COPY", "tmp:1:1", ["tmp:0:1"]]
- 009bda38 ["COPY", "tmp:2:1", ["const:0:1"]]
- 009bda38 ["INT_AND", "tmp:3:1", ["tmp:2:1", "const:8:1"]]
- 009bda38 bytes e0a24afa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c6cd856c2e8eb1587fc7491d58c77993"></a>

### [`009bdae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bd/009bdae4.md) → [`009bdc80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009bd/009bdc80.md) FUN_009bdc80

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009be660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009be/009be660.md) · 呼出先 5件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`009bcbbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bc/009bcbbc.md) [`00a83068`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a83/00a83068.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`009be7fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009be/009be7fc.md) · 呼出先 5件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`009bcd58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009bc/009bcd58.md) [`00a83260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a83/00a83260.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 82.61% / 新版 82.61%

CFGの説明率　旧版 8.33% / 新版 7.69%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009bdae4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009bdae4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009bdae8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009bdae4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:009bdae8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:009bdaec",
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
      "009bdc80",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "009bdc84",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "009bdc88",
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

- 旧版 [`009bdae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bd/009bdae4.md#insn-009bdae4) · [`009bdae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bd/009bdae4.md#insn-009bdae8) · [`009bdaec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bd/009bdae4.md#insn-009bdaec)

~~~diff
- 009bdae4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 009bdae4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 009bdae4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 009bdae4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 009bdae4 bytes fd7bbda9
- 009bdae8 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 009bdae8 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 009bdae8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 009bdae8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009bdae8 bytes f65701a9
- 009bdaec ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 009bdaec ["COPY", "tmp:1:8", ["register:4098:8"]]
- 009bdaec ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 009bdaec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009bdaec bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed8d2c5de1119a4f81be1cee06216609"></a>

### [`009bdb9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bd/009bdb9c.md) → [`009bdd38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009bd/009bdd38.md) FUN_009bdd38

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009be268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009be/009be268.md) · 呼出先 18件 [`00442af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/00442af8.md) [`0047e89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e89c.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`0066d09c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066d/0066d09c.md)
- 新版 呼出元 1件 [`009be404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009be/009be404.md) · 呼出先 18件 [`00442b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442b38.md) [`0047e8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e8dc.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`0066d0dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066d/0066d0dc.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 70.18% / 新版 70.18%

CFGの説明率　旧版 34.00% / 新版 36.17%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `call_target` 1件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 5件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009bdc70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009bdc74"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009bdc78"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009bdbd0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009bdd84"
      ]
    ],
    [
      "009bddcc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768398"
      ]
    ],
    [
      "unmatched:009bdc40",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764344"
      ]
    ]
  ],
  "added": [
    [
      "009bdd6c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009bdd84"
      ]
    ],
    [
      "009bddcc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007683d8"
      ]
    ],
    [
      "009bdddc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764384"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009bdbd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bd/009bdb9c.md#insn-009bdbd0) · [`009bdc14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bd/009bdb9c.md#insn-009bdc14) · [`009bdc30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bd/009bdb9c.md#insn-009bdc30)
- 新版 `009bddcc`（命令位置の公開資料なし）

~~~diff
- 009bdbd0 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 009bdbd0 bytes c0000054
- 009bdc14 ["COPY", "register:0:8", ["register:4040:8"]]
- 009bdc14 ["INT_ADD", "register:40f0:8", ["const:9bdc14:8", "const:4:8"]]
- 009bdc14 ["CALLIND", null, ["register:0:8"]]
- 009bdc14 bytes 00013fd6
- 009bdc30 ["INT_ADD", "register:40f0:8", ["const:9bdc30:8", "const:4:8"]]
- 009bdc30 ["CALL", null, ["ram:768398:8"]]
+ 009bddcc ["INT_ADD", "register:40f0:8", ["const:9bddcc:8", "const:4:8"]]
+ 009bddcc ["CALL", null, ["ram:7683d8:8"]]
- 009bdc30 bytes daa9f697
+ 009bddcc bytes 83a9f697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75db0ba520f4e4b030dc4d5b2ca6e2d1"></a>

### [`009bdee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bd/009bdee0.md) → [`009be07c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009be/009be07c.md) FUN_009be07c

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009be66c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009be/009be66c.md) · 呼出先 13件 [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b9660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9660.md) [`008b9814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9814.md) [`008bac84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ba/008bac84.md)
- 新版 呼出元 1件 [`009be808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009be/009be808.md) · 呼出先 13件 [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b96a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b96a4.md) [`008b9858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9858.md) [`008bacc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ba/008bacc8.md)

変更の種類 branch_condition_or_target, call, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.28% / 新版 95.28%

CFGの説明率　旧版 86.49% / 新版 88.89%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009be144",
      "incomplete_value": false,
      "site": "009be14c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:ab8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009bdfa8",
      "incomplete_value": false,
      "site": "009bdfb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:6b8:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009be230",
      "incomplete_value": false,
      "site": "009be230",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:b38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009be094",
      "incomplete_value": false,
      "site": "009be094",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:738:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009be0e8",
      "value": [
        "leaf",
        "ram:48ccf8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009bdf4c",
      "value": [
        "leaf",
        "ram:48ccb8:8"
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
      "009be0e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ],
    [
      "009be14c",
      "DATA",
      [
        "storage",
        "00c896b8",
        null,
        "undefined *"
      ]
    ],
    [
      "009be210",
      "READ",
      [
        "storage",
        "00c896d8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "009be0e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "009be14c",
      "DATA",
      [
        "storage",
        "00c89ab8",
        null,
        "undefined *"
      ]
    ],
    [
      "009be210",
      "READ",
      [
        "storage",
        "00c89ad8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009bdf4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bd/009bdee0.md#insn-009bdf4c) · [`009bdf24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bd/009bdee0.md#insn-009bdf24) · [`009bdf50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bd/009bdee0.md#insn-009bdf50)
- 新版 `009be0e8`（命令位置の公開資料なし） · `009be0c0`（命令位置の公開資料なし） · `009be0ec`（命令位置の公開資料なし）

~~~diff
- 009bdf4c ["INT_ADD", "register:40f0:8", ["const:9bdf4c:8", "const:4:8"]]
- 009bdf4c ["CALL", null, ["ram:48ccb8:8"]]
+ 009be0e8 ["INT_ADD", "register:40f0:8", ["const:9be0e8:8", "const:4:8"]]
+ 009be0e8 ["CALL", null, ["ram:48ccf8:8"]]
- 009bdf4c bytes 5b3beb97
+ 009be0e8 bytes 043beb97
- 009bdf24 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 009bdf24 ["CBRANCH", null, ["local:b26:8", "tmp:0:1"]]
+ 009be0c0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 009be0c0 ["CBRANCH", null, ["local:b25:8", "tmp:0:1"]]
- 009bdf24 bytes e1100054
+ 009be0c0 bytes e1100054
- 009bdf50 ["INT_RIGHT", "tmp:0:4", ["register:40a8:4", "const:0:4"]]
- 009bdf50 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 009bdf50 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 009bdf50 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
+ 009be0ec ["INT_RIGHT", "tmp:0:4", ["register:40a8:4", "const:0:4"]]
+ 009be0ec ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 009be0ec ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 009be0ec ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 009bdf50 bytes 75010036
+ 009be0ec bytes 75010036
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b991e65a30c5349c25f24bd38f08b7e4"></a>

### [`009be144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009be/009be144.md) → [`009be2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009be/009be2e0.md) FUN_009be2e0

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009bec30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009be/009bec30.md) · 呼出先 7件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`004687c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/004687c4.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0048aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048aaf0.md)
- 新版 呼出元 1件 [`009bedcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009be/009bedcc.md) · 呼出先 7件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00468804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468804.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0048ab30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab30.md)

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, constant, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 98.63% / 新版 98.63%

CFGの説明率　旧版 64.29% / 新版 69.23%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "009be208"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009be3b4",
      "incomplete_value": true,
      "site": "009be3bc",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "old": null,
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "009be3a4"
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
      "unmatched:009be208",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ]
  ],
  "added": [
    [
      "009be3a4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009be208`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009be/009be144.md#insn-009be208) · [`009be220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009be/009be144.md#insn-009be220)
- 新版 `009be3bc`（命令位置の公開資料なし） · `009be3a4`（命令位置の公開資料なし）

~~~diff
- 009be208 ["INT_ADD", "register:40f0:8", ["const:9be208:8", "const:4:8"]]
- 009be208 ["CALL", null, ["ram:46c984:8"]]
- 009be208 bytes dfb9ea97
- 009be220 ["INT_ADD", "register:40f0:8", ["const:9be220:8", "const:4:8"]]
- 009be220 ["CALL", null, ["callee:0048ab30:8"]]
+ 009be3bc ["INT_ADD", "register:40f0:8", ["const:9be3bc:8", "const:4:8"]]
+ 009be3bc ["CALL", null, ["callee:0048ab30:8"]]
- 009be220 bytes 3432eb97
+ 009be3bc bytes dd31eb97
+ 009be3a4 ["INT_ADD", "register:40f0:8", ["const:9be3a4:8", "const:4:8"]]
+ 009be3a4 ["CALL", null, ["ram:46c9c4:8"]]
+ 009be3a4 bytes 88b9ea97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e8b5e0d26d834c5a8311153c077c7a1"></a>

### [`009be268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009be/009be268.md) → [`009be404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009be/009be404.md) FUN_009be404

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 17件 [`0043e90c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043e90c.md) [`0043f3f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f3f8.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0065349c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00653/0065349c.md) [`006534a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00653/006534a0.md)
- 新版 呼出元 1件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 17件 [`0043e94c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e94c.md) [`0043f438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f438.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`006534dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00653/006534dc.md) [`006534e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00653/006534e0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 83.55% / 新版 83.55%

CFGの説明率　旧版 43.33% / 新版 43.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 17件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009be2b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009be380"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009be3a4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009be2b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "009be47c",
      "DATA",
      [
        "storage",
        "0039b1b4",
        null,
        "qword"
      ]
    ],
    [
      "unmatched:009be380",
      "DATA",
      [
        "storage",
        "00334170",
        null,
        "fde_table_entry"
      ]
    ]
  ],
  "added": [
    [
      "009be44c",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "009be47c",
      "DATA",
      [
        "storage",
        "0039b1b4",
        null,
        "dword"
      ]
    ],
    [
      "009be51c",
      "DATA",
      [
        "storage",
        "00334170",
        null,
        "fde_table_entry"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009be2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009be/009be268.md#insn-009be2b0) · [`009be380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009be/009be268.md#insn-009be380) · [`009be3a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009be/009be268.md#insn-009be3a4)

~~~diff
- 009be2b0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 009be2b0 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 009be2b0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 009be2b0 bytes a8831ff8
- 009be380 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 009be380 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 009be380 bytes 090100f9
- 009be3a4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:20:8"]]
- 009be3a4 ["COPY", "tmp:1:8", ["const:0:8"]]
- 009be3a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 009be3a4 bytes 1f1100f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51c7f6f8bca58e014d9dfa7218e2ec10"></a>

### [`009be66c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009be/009be66c.md) → [`009be808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009be/009be808.md) FUN_009be808

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 12件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`00859b0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00859/00859b0c.md) [`0085b264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085b264.md)
- 新版 呼出元 1件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 12件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`00859b4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00859/00859b4c.md) [`0085b2a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085b2a4.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 94.31% / 新版 94.31%

CFGの説明率　旧版 55.47% / 新版 56.30%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 2件, `store_condition` 3件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009be66c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009be66c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009be670"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009be66c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:009be670",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:009be674",
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
      "009be808",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "009be80c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "009be810",
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

- 旧版 [`009be66c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009be/009be66c.md#insn-009be66c) · [`009be670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009be/009be66c.md#insn-009be670) · [`009be674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009be/009be66c.md#insn-009be674)

~~~diff
- 009be66c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 009be66c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 009be66c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffa0:8"]]
- 009be66c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 009be66c bytes fd7bbaa9
- 009be670 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 009be670 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d8:8"]]
- 009be670 bytes fb0b00f9
- 009be674 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 009be674 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 009be674 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 009be674 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009be674 bytes fa6702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8098e592b4b93cf973faed117fe68ec7"></a>

### [`009bec30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009be/009bec30.md) → [`009bedcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009be/009bedcc.md) FUN_009bedcc

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00859b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00859/00859b18.md) · 呼出先 14件 [`00467b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467b20.md) [`00468b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468b9c.md) [`00468c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468c20.md) [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md) [`00469bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469bc4.md)
- 新版 呼出元 1件 [`00859b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00859/00859b58.md) · 呼出先 14件 [`00467b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b60.md) [`00468bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468bdc.md) [`00468c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468c60.md) [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`00469c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469c04.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 88.32% / 新版 88.32%

CFGの説明率　旧版 15.15% / 新版 14.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 16件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 5件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009bec44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009bec44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009bec48"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009bec44",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:009bec48",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "009bedf0",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "009bede0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "009bede4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "009bedf0",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009bec44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009be/009bec30.md#insn-009bec44) · [`009bec48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009be/009bec30.md#insn-009bec48) · [`009bec58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009be/009bec30.md#insn-009bec58)
- 新版 `009bedf4`（命令位置の公開資料なし）

~~~diff
- 009bec44 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 009bec44 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 009bec44 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 009bec44 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009bec44 bytes f65704a9
- 009bec48 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 009bec48 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 009bec48 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 009bec48 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009bec48 bytes f44f05a9
- 009bec58 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 009bec58 ["CBRANCH", null, ["local:b23:8", "tmp:0:1"]]
+ 009bedf4 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 009bedf4 ["CBRANCH", null, ["local:b24:8", "tmp:0:1"]]
- 009bec58 bytes 082000b4
+ 009bedf4 bytes 082000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-420bbfb36c09da166ff7a1d525d164cd"></a>

### [`009bf078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bf/009bf078.md) → [`009bf214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009bf/009bf214.md) FUN_009bf214

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009bcce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bc/009bcce4.md) · 呼出先 8件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`004619d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/004619d8.md) [`004619ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/004619ec.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`009bce80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009bc/009bce80.md) · 呼出先 8件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00461a18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461a18.md) [`00461a2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461a2c.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 68.54% / 新版 68.54%

CFGの説明率　旧版 17.44% / 新版 15.79%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_condition` 7件, `unresolved_branch_alignment` 9件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 17件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009bf08c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009bf08c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009bf0ac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009bf08c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:009bf0ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:009bf0d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009bf2ac"
      ]
    ]
  ],
  "added": [
    [
      "009bf228",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "009bf248",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "009bf26c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "009bf2ac"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009bf08c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bf/009bf078.md#insn-009bf08c) · [`009bf0ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bf/009bf078.md#insn-009bf0ac) · [`009bf144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bf/009bf078.md#insn-009bf144)

~~~diff
- 009bf08c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 009bf08c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 009bf08c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 009bf08c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009bf08c bytes f44f08a9
- 009bf0ac ["COPY", "tmp:0:8", ["register:4040:8"]]
- 009bf0ac ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 009bf0ac ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 009bf0ac bytes a8831ff8
- 009bf144 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:8:8"]]
- 009bf144 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 009bf144 bytes c80a00b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce09df053a8bdff763225a95a9c38a10"></a>

### [`009bf4a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bf/009bf4a4.md) → [`009bf640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009bf/009bf640.md) FUN_009bf640

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009bf644",
      "incomplete_value": false,
      "site": "009bf648",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:610:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009bf4a8",
      "incomplete_value": false,
      "site": "009bf4ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:210:8"
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
      "009bf648",
      "DATA",
      [
        "storage",
        "00c89210",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009bf648",
      "DATA",
      [
        "storage",
        "00c89610",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009bf4a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bf/009bf4a4.md#insn-009bf4a8)
- 新版 `009bf644`（命令位置の公開資料なし）

~~~diff
- 009bf4a8 ["COPY", "tmp:0:8", ["const:210:8"]]
- 009bf4a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009bf4a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009bf4a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009bf644 ["COPY", "tmp:0:8", ["const:610:8"]]
+ 009bf644 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009bf644 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009bf644 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009bf4a8 bytes 08410891
+ 009bf644 bytes 08411891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84948589800c7a4d45fcc2807785e5ce"></a>

### [`009bf4ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bf/009bf4ec.md) → [`009bf688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009bf/009bf688.md) FUN_009bf688

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "009bf6ac",
      "incomplete_value": false,
      "site": "009bf6ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:6a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009bf510",
      "incomplete_value": false,
      "site": "009bf510",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:2a8:8"
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
      "009bf6ac",
      "DATA",
      [
        "storage",
        "00c892a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009bf6ac",
      "DATA",
      [
        "storage",
        "00c896a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009bf500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bf/009bf4ec.md#insn-009bf500) · [`009bf50c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bf/009bf4ec.md#insn-009bf50c)
- 新版 `009bf69c`（命令位置の公開資料なし） · `009bf6a8`（命令位置の公開資料なし）

~~~diff
- 009bf500 ["INT_ADD", "register:40f0:8", ["const:9bf500:8", "const:4:8"]]
- 009bf500 ["CALL", null, ["callee:00c57e90:8"]]
+ 009bf69c ["INT_ADD", "register:40f0:8", ["const:9bf69c:8", "const:4:8"]]
+ 009bf69c ["CALL", null, ["callee:00c57e90:8"]]
- 009bf500 bytes 64610a94
+ 009bf69c bytes fd610a94
- 009bf50c ["COPY", "tmp:0:8", ["const:2a8:8"]]
- 009bf50c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009bf50c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009bf50c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009bf6a8 ["COPY", "tmp:0:8", ["const:6a8:8"]]
+ 009bf6a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009bf6a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009bf6a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009bf50c bytes 08a10a91
+ 009bf6a8 bytes 08a11a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a12ed962a5beaee6c7f4d172d1669172"></a>

### [`009bf520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bf/009bf520.md) → [`009bf6bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009bf/009bf6bc.md) FUN_009bf6bc

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009bf6c8",
      "incomplete_value": false,
      "site": "009bf6c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:6a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009bf52c",
      "incomplete_value": false,
      "site": "009bf52c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:2a8:8"
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
      "009bf6c8",
      "DATA",
      [
        "storage",
        "00c892a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009bf6c8",
      "DATA",
      [
        "storage",
        "00c896a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009bf528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bf/009bf520.md#insn-009bf528)
- 新版 `009bf6c4`（命令位置の公開資料なし）

~~~diff
- 009bf528 ["COPY", "tmp:0:8", ["const:2a8:8"]]
- 009bf528 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 009bf528 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 009bf528 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 009bf6c4 ["COPY", "tmp:0:8", ["const:6a8:8"]]
+ 009bf6c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 009bf6c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 009bf6c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 009bf528 bytes 29a10a91
+ 009bf6c4 bytes 29a11a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-789e0ab794085d540cce0bfbb7a9e3a4"></a>

### [`009bf53c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bf/009bf53c.md) → [`009bf6d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009bf/009bf6d8.md) FUN_009bf6d8

採用 · 移動量 `+0x19c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 40件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`00492dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492dc8.md) [`005da544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005da/005da544.md) [`006649ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/006649ac.md)
- 新版 呼出元 0件  · 呼出先 40件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00492e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492e08.md) [`005da584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005da/005da584.md) [`006649ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/006649ec.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 87.54% / 新版 87.54%

CFGの説明率　旧版 63.95% / 新版 64.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 17件, `call_target` 3件, `store_condition` 2件, `store_value` 12件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009bf630"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009bf634"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009bf638"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009bf760",
      "DATA",
      [
        "storage",
        "003c77d8",
        null,
        "byte[15]"
      ]
    ],
    [
      "009bf784",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "009bf79c",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "009bf760",
      "DATA",
      [
        "storage",
        "003c77d8",
        null,
        "uleb128"
      ]
    ],
    [
      "009bf784",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "009bf79c",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009bf5dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bf/009bf53c.md#insn-009bf5dc) · [`009bf630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bf/009bf53c.md#insn-009bf630) · [`009bf634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bf/009bf53c.md#insn-009bf634)
- 新版 `009bf778`（命令位置の公開資料なし）

~~~diff
- 009bf5dc ["INT_ADD", "register:40f0:8", ["const:9bf5dc:8", "const:4:8"]]
- 009bf5dc ["CALL", null, ["callee:008514f8:8"]]
+ 009bf778 ["INT_ADD", "register:40f0:8", ["const:9bf778:8", "const:4:8"]]
+ 009bf778 ["CALL", null, ["callee:008514f8:8"]]
- 009bf5dc bytes b747fa97
+ 009bf778 bytes 6047fa97
- 009bf630 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 009bf630 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffb0:8"]]
- 009bf630 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 009bf630 bytes a8031b38
- 009bf634 ["COPY", "tmp:0:4", ["const:0:4"]]
- 009bf634 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 009bf634 ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffffc6:8"]]
- 009bf634 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 009bf634 bytes bf631c38
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3882ae4fdba0c008c021071bcc9e48d5"></a>

### [`009c01c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c0/009c01c4.md) → [`009c0360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009c0/009c0360.md) FUN_009c0360

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "009c0374",
      "incomplete_value": false,
      "site": "009c0378",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:718:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009c01d8",
      "incomplete_value": false,
      "site": "009c01dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c89000:8"
          ],
          [
            "leaf",
            "const:318:8"
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
      "009c0378",
      "DATA",
      [
        "storage",
        "00c89318",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009c0378",
      "DATA",
      [
        "storage",
        "00c89718",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009c01d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c0/009c01c4.md#insn-009c01d0) · [`009c01d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009c0/009c01c4.md#insn-009c01d8)
- 新版 `009c036c`（命令位置の公開資料なし） · `009c0374`（命令位置の公開資料なし）

~~~diff
- 009c01d0 ["INT_ADD", "register:40f0:8", ["const:9c01d0:8", "const:4:8"]]
- 009c01d0 ["CALL", null, ["callee:00c57e90:8"]]
+ 009c036c ["INT_ADD", "register:40f0:8", ["const:9c036c:8", "const:4:8"]]
+ 009c036c ["CALL", null, ["callee:00c57e90:8"]]
- 009c01d0 bytes 305e0a94
+ 009c036c bytes c95e0a94
- 009c01d8 ["COPY", "tmp:0:8", ["const:318:8"]]
- 009c01d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009c01d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009c01d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009c0374 ["COPY", "tmp:0:8", ["const:718:8"]]
+ 009c0374 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009c0374 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009c0374 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009c01d8 bytes 08610c91
+ 009c0374 bytes 08611c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

