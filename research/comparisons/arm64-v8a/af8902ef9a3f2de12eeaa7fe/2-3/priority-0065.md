# v16.0.0 → v16.0.1 · 最優先の変更候補 (65)

[一覧の目次](README.md)

<a id="compare-db9b531213981898906016458ec12615"></a>

### [`00aed9b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed9b8.md) → [`00aedde0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aed/00aedde0.md) FUN_00aedde0

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 36件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md)
- 新版 呼出元 0件  · 呼出先 36件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 38.51% / 新版 37.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 28件, `store_condition` 2件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 9件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 20件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aed9bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aed9bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aed9c0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aed9bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aed9c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aed9c4",
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
      "00aedde4",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00aedde8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00aeddec",
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

- 旧版 [`00aed9bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed9b8.md#insn-00aed9bc) · [`00aed9c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed9b8.md#insn-00aed9c0) · [`00aed9c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed9b8.md#insn-00aed9c4)

~~~diff
- 00aed9bc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aed9bc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aed9bc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:b0:8"]]
- 00aed9bc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aed9bc bytes fd7b0ba9
- 00aed9c0 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00aed9c0 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00aed9c0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:c0:8"]]
- 00aed9c0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aed9c0 bytes fc6f0ca9
- 00aed9c4 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00aed9c4 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00aed9c4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:d0:8"]]
- 00aed9c4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aed9c4 bytes fa670da9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc59bd46de3fddab24960d04ce46a435"></a>

### [`00aee3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aee3f0.md) → [`00aee818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aee/00aee818.md) FUN_00aee818

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00aee83c",
      "incomplete_value": false,
      "site": "00aee83c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8d000:8"
          ],
          [
            "leaf",
            "const:cd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aee414",
      "incomplete_value": false,
      "site": "00aee414",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8d000:8"
          ],
          [
            "leaf",
            "const:8d8:8"
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
      "00aee83c",
      "DATA",
      [
        "storage",
        "00c8d8d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00aee83c",
      "DATA",
      [
        "storage",
        "00c8dcd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aee404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aee3f0.md#insn-00aee404) · [`00aee410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aee3f0.md#insn-00aee410)
- 新版 `00aee82c`（命令位置の公開資料なし） · `00aee838`（命令位置の公開資料なし）

~~~diff
- 00aee404 ["INT_ADD", "register:40f0:8", ["const:aee404:8", "const:4:8"]]
- 00aee404 ["CALL", null, ["callee:00c57e90:8"]]
+ 00aee82c ["INT_ADD", "register:40f0:8", ["const:aee82c:8", "const:4:8"]]
+ 00aee82c ["CALL", null, ["callee:00c57e90:8"]]
- 00aee404 bytes a3a50594
+ 00aee82c bytes 99a50594
- 00aee410 ["COPY", "tmp:0:8", ["const:8d8:8"]]
- 00aee410 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aee410 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aee410 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aee838 ["COPY", "tmp:0:8", ["const:cd8:8"]]
+ 00aee838 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aee838 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aee838 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aee410 bytes 08612391
+ 00aee838 bytes 08613391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c737b229878d29640b692b39a378bdf7"></a>

### [`00aee440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aee440.md) → [`00aee868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aee/00aee868.md) FUN_00aee868

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 8件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`004920e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/004920e0.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`00492120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492120.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 67.11% / 新版 67.11%

CFGの説明率　旧版 40.91% / 新版 23.68%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aee444"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aee444"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aee448"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aee444",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aee448",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aee458",
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
      "00aee86c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00aee870",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00aee880",
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

- 旧版 [`00aee444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aee440.md#insn-00aee444) · [`00aee448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aee440.md#insn-00aee448) · [`00aee458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aee440.md#insn-00aee458)

~~~diff
- 00aee444 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aee444 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aee444 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00aee444 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aee444 bytes fd7b04a9
- 00aee448 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00aee448 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00aee448 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00aee448 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aee448 bytes f44f05a9
- 00aee458 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00aee458 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00aee458 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00aee458 bytes a8831ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2bbd27452485cfdb1c14d32b2d16344"></a>

### [`00aee5d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aee5d8.md) → [`00aeea00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aee/00aeea00.md) FUN_00aeea00

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aee5fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aee5fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00aeea24"
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
      "unmatched:00aee5fc",
      "DATA",
      [
        "storage",
        "00c8d958",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00aee600",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aee604",
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
      "00aeea24",
      "DATA",
      [
        "storage",
        "00c8dd58",
        null,
        "undefined *"
      ]
    ],
    [
      "00aeea28",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00aeea2c",
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

- 旧版 [`00aee5ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aee5d8.md#insn-00aee5ec) · [`00aee5fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aee5d8.md#insn-00aee5fc) · [`00aee608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aee5d8.md#insn-00aee608)
- 新版 `00aeea14`（命令位置の公開資料なし）

~~~diff
- 00aee5ec ["INT_ADD", "register:40f0:8", ["const:aee5ec:8", "const:4:8"]]
- 00aee5ec ["CALL", null, ["callee:00c57e90:8"]]
+ 00aeea14 ["INT_ADD", "register:40f0:8", ["const:aeea14:8", "const:4:8"]]
+ 00aeea14 ["CALL", null, ["callee:00c57e90:8"]]
- 00aee5ec bytes 29a50594
+ 00aeea14 bytes 1fa50594
- 00aee5fc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00aee5fc ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00aee5fc ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00aee5fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aee5fc bytes 082400a9
- 00aee608 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00aee608 ["RETURN", null, ["register:0:8"]]
- 00aee608 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe4fbd4d609d4ca4a31d540a4f0667cd"></a>

### [`00aee60c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aee60c.md) → [`00aeea34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aee/00aeea34.md) FUN_00aeea34

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00aeea40",
      "incomplete_value": false,
      "site": "00aeea40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8d000:8"
          ],
          [
            "leaf",
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aee618",
      "incomplete_value": false,
      "site": "00aee618",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8d000:8"
          ],
          [
            "leaf",
            "const:958:8"
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
      "00aeea40",
      "DATA",
      [
        "storage",
        "00c8d958",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00aeea40",
      "DATA",
      [
        "storage",
        "00c8dd58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aee614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aee60c.md#insn-00aee614)
- 新版 `00aeea3c`（命令位置の公開資料なし）

~~~diff
- 00aee614 ["COPY", "tmp:0:8", ["const:958:8"]]
- 00aee614 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00aee614 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00aee614 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00aeea3c ["COPY", "tmp:0:8", ["const:d58:8"]]
+ 00aeea3c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00aeea3c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00aeea3c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00aee614 bytes 29612591
+ 00aeea3c bytes 29613591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9b4d93ebd68630658615d811a7dd3b3"></a>

### [`00aee628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aee628.md) → [`00aeea50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aee/00aeea50.md) FUN_00aeea50

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md) [`008b980c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b980c.md) [`008bb4cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008bb/008bb4cc.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`008b9850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9850.md) [`008bb510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008bb/008bb510.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 93.55% / 新版 93.55%

CFGの説明率　旧版 75.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00aeea6c",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00aee644",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00aee660"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00aee684",
      "incomplete_value": true,
      "site": "00aee688",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "live",
            "register:40a0:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aeea6c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "unmatched:00aee660",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00aeea6c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00aeea88",
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

- 旧版 [`00aee644`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aee628.md#insn-00aee644) · [`00aee660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aee628.md#insn-00aee660) · [`00aee688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aee628.md#insn-00aee688)
- 新版 `00aeea6c`（命令位置の公開資料なし） · `00aeeab0`（命令位置の公開資料なし）

~~~diff
- 00aee644 ["INT_ADD", "register:40f0:8", ["const:aee644:8", "const:4:8"]]
- 00aee644 ["CALL", null, ["ram:47acb4:8"]]
+ 00aeea6c ["INT_ADD", "register:40f0:8", ["const:aeea6c:8", "const:4:8"]]
+ 00aeea6c ["CALL", null, ["ram:47acf4:8"]]
- 00aee644 bytes 9c31e697
+ 00aeea6c bytes a230e697
- 00aee660 ["INT_ADD", "register:40f0:8", ["const:aee660:8", "const:4:8"]]
- 00aee660 ["CALL", null, ["ram:47acb4:8"]]
- 00aee660 bytes 9531e697
- 00aee688 ["INT_ADD", "register:40f0:8", ["const:aee688:8", "const:4:8"]]
- 00aee688 ["CALL", null, ["callee:008bb510:8"]]
+ 00aeeab0 ["INT_ADD", "register:40f0:8", ["const:aeeab0:8", "const:4:8"]]
+ 00aeeab0 ["CALL", null, ["callee:008bb510:8"]]
- 00aee688 bytes 9133f797
+ 00aeeab0 bytes 9832f797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a414bb6023002d3707f28ef24129c8bc"></a>

### [`00aee6f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aee6f4.md) → [`00aeeb1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aee/00aeeb1c.md) FUN_00aeeb1c

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00aeeb20",
      "incomplete_value": false,
      "site": "00aeeb24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8d000:8"
          ],
          [
            "leaf",
            "const:dd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aee6f8",
      "incomplete_value": false,
      "site": "00aee6fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8d000:8"
          ],
          [
            "leaf",
            "const:9d8:8"
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
      "00aeeb24",
      "DATA",
      [
        "storage",
        "00c8d9d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00aeeb24",
      "DATA",
      [
        "storage",
        "00c8ddd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aee6f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aee6f4.md#insn-00aee6f8)
- 新版 `00aeeb20`（命令位置の公開資料なし）

~~~diff
- 00aee6f8 ["COPY", "tmp:0:8", ["const:9d8:8"]]
- 00aee6f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aee6f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aee6f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aeeb20 ["COPY", "tmp:0:8", ["const:dd8:8"]]
+ 00aeeb20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aeeb20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aeeb20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aee6f8 bytes 08612791
+ 00aeeb20 bytes 08613791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27d31ed10622f811805c54ce9ed47e0f"></a>

### [`00aee70c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aee70c.md) → [`00aeeb34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aee/00aeeb34.md) FUN_00aeeb34

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_condition` 3件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aee714"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00aeeb3c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00aee728"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aee714",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aeeb70"
      ]
    ],
    [
      "unmatched:00aee728",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00aeeb3c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aeeb70"
      ]
    ],
    [
      "00aeeb50",
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

- 旧版 [`00aee714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aee70c.md#insn-00aee714) · [`00aee728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aee70c.md#insn-00aee728) · [`00aee734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aee70c.md#insn-00aee734)
- 新版 `00aeeb5c`（命令位置の公開資料なし）

~~~diff
- 00aee714 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00aee714 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00aee714 bytes a1010054
- 00aee728 ["INT_ADD", "register:40f0:8", ["const:aee728:8", "const:4:8"]]
- 00aee728 ["CALL", null, ["ram:47acb4:8"]]
- 00aee728 bytes 6331e697
- 00aee734 ["INT_ADD", "register:40f0:8", ["const:aee734:8", "const:4:8"]]
- 00aee734 ["CALL", null, ["callee:0047cdd4:8"]]
+ 00aeeb5c ["INT_ADD", "register:40f0:8", ["const:aeeb5c:8", "const:4:8"]]
+ 00aeeb5c ["CALL", null, ["callee:0047cdd4:8"]]
- 00aee734 bytes 9839e697
+ 00aeeb5c bytes 9e38e697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e2bab5726c3088771e563b0b13bada9"></a>

### [`00aee7ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aee7ac.md) → [`00aeebd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aee/00aeebd4.md) FUN_00aeebd4

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00aeebe0",
      "incomplete_value": false,
      "site": "00aeebe0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8d000:8"
          ],
          [
            "leaf",
            "const:e68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aee7b8",
      "incomplete_value": false,
      "site": "00aee7b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8d000:8"
          ],
          [
            "leaf",
            "const:a68:8"
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
      "00aeebe0",
      "DATA",
      [
        "storage",
        "00c8da68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00aeebe0",
      "DATA",
      [
        "storage",
        "00c8de68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aee7b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aee7ac.md#insn-00aee7b4)
- 新版 `00aeebdc`（命令位置の公開資料なし）

~~~diff
- 00aee7b4 ["COPY", "tmp:0:8", ["const:a68:8"]]
- 00aee7b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00aee7b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00aee7b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00aeebdc ["COPY", "tmp:0:8", ["const:e68:8"]]
+ 00aeebdc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00aeebdc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00aeebdc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00aee7b4 bytes 29a12991
+ 00aeebdc bytes 29a13991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c924bc9336dcf930202867b45be920c"></a>

### [`00aee7c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aee7c8.md) → [`00aeebf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aee/00aeebf0.md) FUN_00aeebf0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 12件 [`00467b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467b20.md) [`00469bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469bc4.md) [`0046daac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046daac.md) [`00489f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f0c.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00467b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b60.md) [`00469c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469c04.md) [`0046daec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046daec.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 46.43% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_store_alignment` 13件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aee7cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aee7cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aee7d0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aee7cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aee7d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aee7d4",
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
      "00aeebf4",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00aeebf8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00aeebfc",
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

- 旧版 [`00aee7cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aee7c8.md#insn-00aee7cc) · [`00aee7d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aee7c8.md#insn-00aee7d0) · [`00aee7d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aee7c8.md#insn-00aee7d4)

~~~diff
- 00aee7cc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aee7cc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aee7cc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00aee7cc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aee7cc bytes fd7b02a9
- 00aee7d0 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00aee7d0 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00aee7d0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00aee7d0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aee7d0 bytes fc6f03a9
- 00aee7d4 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00aee7d4 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00aee7d4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00aee7d4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aee7d4 bytes fa6704a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44ce93e192d81b7a13ed942683e704e4"></a>

### [`00aeea78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aeea78.md) → [`00aeeea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aee/00aeeea0.md) FUN_00aeeea0

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "00aeeec0",
      "incomplete_value": false,
      "site": "00aeeec4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8d000:8"
          ],
          [
            "leaf",
            "const:ef8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeea98",
      "incomplete_value": false,
      "site": "00aeea9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8d000:8"
          ],
          [
            "leaf",
            "const:af8:8"
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
      "00aeeec4",
      "DATA",
      [
        "storage",
        "00c8daf8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00aeeec4",
      "DATA",
      [
        "storage",
        "00c8def8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeea8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aeea78.md#insn-00aeea8c) · [`00aeea98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aeea78.md#insn-00aeea98)
- 新版 `00aeeeb4`（命令位置の公開資料なし） · `00aeeec0`（命令位置の公開資料なし）

~~~diff
- 00aeea8c ["INT_ADD", "register:40f0:8", ["const:aeea8c:8", "const:4:8"]]
- 00aeea8c ["CALL", null, ["callee:00c57e90:8"]]
+ 00aeeeb4 ["INT_ADD", "register:40f0:8", ["const:aeeeb4:8", "const:4:8"]]
+ 00aeeeb4 ["CALL", null, ["callee:00c57e90:8"]]
- 00aeea8c bytes 01a40594
+ 00aeeeb4 bytes f7a30594
- 00aeea98 ["COPY", "tmp:0:8", ["const:af8:8"]]
- 00aeea98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aeea98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aeea98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aeeec0 ["COPY", "tmp:0:8", ["const:ef8:8"]]
+ 00aeeec0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aeeec0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aeeec0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aeea98 bytes 08e12b91
+ 00aeeec0 bytes 08e13b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1143d6370ce8db1ba79bd202a27bdcb"></a>

### [`00aeead0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aeead0.md) → [`00aeeef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aee/00aeeef8.md) FUN_00aeeef8

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`00658d6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00658/00658d6c.md) [`00aeec90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aeec90.md) [`00aeec94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aeec94.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`00658dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00658/00658dac.md) [`00aef0b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aef/00aef0b8.md) [`00aef0bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aef/00aef0bc.md)

変更の種類 branch_condition_or_target, call, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 87.10% / 新版 87.10%

CFGの説明率　旧版 86.36% / 新版 82.61%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件, `store_value` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeead4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeead4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeeae8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aeead4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aeeae8",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "00aeef2c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00aeeefc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00aeef10",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "00aeef2c",
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

- 旧版 [`00aeead4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aeead0.md#insn-00aeead4) · [`00aeeae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aeead0.md#insn-00aeeae8) · [`00aeeb04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aeead0.md#insn-00aeeb04)
- 新版 `00aeef2c`（命令位置の公開資料なし）

~~~diff
- 00aeead4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aeead4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aeead4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00aeead4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aeead4 bytes fd7b04a9
- 00aeeae8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00aeeae8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00aeeae8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00aeeae8 bytes a8831ff8
- 00aeeb04 ["INT_ADD", "register:40f0:8", ["const:aeeb04:8", "const:4:8"]]
- 00aeeb04 ["CALL", null, ["ram:47acb4:8"]]
+ 00aeef2c ["INT_ADD", "register:40f0:8", ["const:aeef2c:8", "const:4:8"]]
+ 00aeef2c ["CALL", null, ["ram:47acf4:8"]]
- 00aeeb04 bytes 6c30e697
+ 00aeef2c bytes 722fe697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca8845b7815236ee3ee5dd2e507a1d4e"></a>

### [`00aeeccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aeeccc.md) → [`00aef0f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aef/00aef0f4.md) FUN_00aef0f4

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "00aef114",
      "incomplete_value": false,
      "site": "00aef118",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8d000:8"
          ],
          [
            "leaf",
            "const:ff8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeecec",
      "incomplete_value": false,
      "site": "00aeecf0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8d000:8"
          ],
          [
            "leaf",
            "const:bf8:8"
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
      "00aef118",
      "DATA",
      [
        "storage",
        "00c8dbf8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00aef118",
      "DATA",
      [
        "storage",
        "00c8dff8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeece0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aeeccc.md#insn-00aeece0) · [`00aeecec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aeeccc.md#insn-00aeecec)
- 新版 `00aef108`（命令位置の公開資料なし） · `00aef114`（命令位置の公開資料なし）

~~~diff
- 00aeece0 ["INT_ADD", "register:40f0:8", ["const:aeece0:8", "const:4:8"]]
- 00aeece0 ["CALL", null, ["callee:00c57e90:8"]]
+ 00aef108 ["INT_ADD", "register:40f0:8", ["const:aef108:8", "const:4:8"]]
+ 00aef108 ["CALL", null, ["callee:00c57e90:8"]]
- 00aeece0 bytes 6ca30594
+ 00aef108 bytes 62a30594
- 00aeecec ["COPY", "tmp:0:8", ["const:bf8:8"]]
- 00aeecec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aeecec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aeecec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aef114 ["COPY", "tmp:0:8", ["const:ff8:8"]]
+ 00aef114 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aef114 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aef114 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aeecec bytes 08e12f91
+ 00aef114 bytes 08e13f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b97f44016d66b966161c63ba1fa7f00"></a>

### [`00aeed24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aeed24.md) → [`00aef14c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aef/00aef14c.md) FUN_00aef14c

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 33件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`00489f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f0c.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`005d8b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8b88.md)
- 新版 呼出元 0件  · 呼出先 33件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`005d8bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8bc8.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 86.55% / 新版 86.55%

CFGの説明率　旧版 31.03% / 新版 27.55%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 15件, `call_target` 1件, `store_condition` 1件, `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 16件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeed4c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeee14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeee34"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aeed4c",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aeed64",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00aeed88"
      ]
    ],
    [
      "00aef194",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00aef174",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "00aef18c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aef1b0"
      ]
    ],
    [
      "00aef194",
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

- 旧版 [`00aeed4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aeed24.md#insn-00aeed4c) · [`00aeed6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aeed24.md#insn-00aeed6c) · [`00aeedf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aeed24.md#insn-00aeedf0)
- 新版 `00aef194`（命令位置の公開資料なし） · `00aef218`（命令位置の公開資料なし）

~~~diff
- 00aeed4c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00aeed4c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff0:8"]]
- 00aeed4c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00aeed4c bytes a8031ff8
- 00aeed6c ["INT_ADD", "register:40f0:8", ["const:aeed6c:8", "const:4:8"]]
- 00aeed6c ["CALL", null, ["ram:47acb4:8"]]
+ 00aef194 ["INT_ADD", "register:40f0:8", ["const:aef194:8", "const:4:8"]]
+ 00aef194 ["CALL", null, ["ram:47acf4:8"]]
- 00aeed6c bytes d22fe697
+ 00aef194 bytes d82ee697
- 00aeedf0 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 00aeedf0 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00aeedf0 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00aeedf0 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
+ 00aef218 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
+ 00aef218 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00aef218 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00aef218 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 00aeedf0 bytes a0240036
+ 00aef218 bytes a0240036
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0880e83042df06252c7904f02bed1072"></a>

### [`00aef4a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aef4a4.md) → [`00aef8cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aef/00aef8cc.md) FUN_00aef8cc

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b6ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6ed4.md) [`008b7984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7984.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b6f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f18.md) [`008b79c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b79c8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 branch_condition_or_target, call, call_count, call_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 92.98% / 新版 92.98%

CFGの説明率　旧版 57.14% / 新版 52.17%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aef4d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00aef8f8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00aef914",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00aef4ec",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "unmatched:00aef4d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aef9a4"
      ]
    ],
    [
      "00aef914",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "unmatched:00aef52c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00aef8f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aef9a4"
      ]
    ],
    [
      "00aef914",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00aef954",
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

- 旧版 [`00aef4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aef4a4.md#insn-00aef4d0) · [`00aef4ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aef4a4.md#insn-00aef4ec) · [`00aef52c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aef4a4.md#insn-00aef52c)
- 新版 `00aef914`（命令位置の公開資料なし）

~~~diff
- 00aef4d0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00aef4d0 ["CBRANCH", null, ["local:b15:8", "tmp:0:1"]]
- 00aef4d0 bytes 61050054
- 00aef4ec ["INT_ADD", "register:40f0:8", ["const:aef4ec:8", "const:4:8"]]
- 00aef4ec ["CALL", null, ["ram:47acb4:8"]]
+ 00aef914 ["INT_ADD", "register:40f0:8", ["const:aef914:8", "const:4:8"]]
+ 00aef914 ["CALL", null, ["ram:47acf4:8"]]
- 00aef4ec bytes f22de697
+ 00aef914 bytes f82ce697
- 00aef52c ["INT_ADD", "register:40f0:8", ["const:aef52c:8", "const:4:8"]]
- 00aef52c ["CALL", null, ["ram:47acb4:8"]]
- 00aef52c bytes e22de697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd8df3aa886c8b3c174e1b9b8c397023"></a>

### [`00aef5b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aef5b4.md) → [`00aef9dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aef/00aef9dc.md) FUN_00aef9dc

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 69.23% / 新版 69.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aef5b8"
    }
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00aefa00",
      "incomplete_value": false,
      "site": "00aefa00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aef5d8",
      "incomplete_value": false,
      "site": "00aef5d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8d000:8"
          ],
          [
            "leaf",
            "const:ce8:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00aef9e0"
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
      "unmatched:00aef5b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00aefa00",
      "DATA",
      [
        "storage",
        "00c8dce8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00aef9e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00aefa00",
      "DATA",
      [
        "storage",
        "00c8e0e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aef5b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aef5b4.md#insn-00aef5b8) · [`00aef5bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aef5b4.md#insn-00aef5bc)
- 新版 `00aef9e0`（命令位置の公開資料なし）

~~~diff
- 00aef5b8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00aef5b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00aef5b8 bytes f30b00f9
+ 00aef9e0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
+ 00aef9e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
+ 00aef9e0 bytes f30b00f9
- 00aef5bc ["COPY", "register:40e8:8", ["register:8:8"]]
- 00aef5bc bytes fd030091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa92ce043e338a1e1699185aecc592b1"></a>

### [`00aef5e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aef5e8.md) → [`00aefa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aef/00aefa10.md) FUN_00aefa10

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00aefa1c",
      "incomplete_value": false,
      "site": "00aefa1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aef5f4",
      "incomplete_value": false,
      "site": "00aef5f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8d000:8"
          ],
          [
            "leaf",
            "const:ce8:8"
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
      "00aefa1c",
      "DATA",
      [
        "storage",
        "00c8dce8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00aefa1c",
      "DATA",
      [
        "storage",
        "00c8e0e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aef5ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aef5e8.md#insn-00aef5ec) · [`00aef5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aef5e8.md#insn-00aef5f0)
- 新版 `00aefa14`（命令位置の公開資料なし） · `00aefa18`（命令位置の公開資料なし）

~~~diff
- 00aef5ec ["COPY", "register:4048:8", ["const:c8d000:8"]]
+ 00aefa14 ["COPY", "register:4048:8", ["const:c8e000:8"]]
- 00aef5ec bytes e90c00d0
+ 00aefa14 bytes e90c00f0
- 00aef5f0 ["COPY", "tmp:0:8", ["const:ce8:8"]]
- 00aef5f0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00aef5f0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00aef5f0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00aefa18 ["COPY", "tmp:0:8", ["const:e8:8"]]
+ 00aefa18 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00aefa18 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00aefa18 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00aef5f0 bytes 29a13391
+ 00aefa18 bytes 29a10391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0987f238778de178134b0a17c78805e0"></a>

### [`00aef604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aef604.md) → [`00aefa2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aef/00aefa2c.md) FUN_00aefa2c

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`008b6a18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6a18.md) [`008b6ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6ecc.md) [`008b7984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7984.md)
- 新版 呼出元 0件  · 呼出先 3件 [`008b6a5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6a5c.md) [`008b6f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f10.md) [`008b79c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b79c8.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aefa40",
      "incomplete_value": true,
      "site": "00aefa44",
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
            "const:2f38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aef618",
      "incomplete_value": true,
      "site": "00aef61c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "live",
            "register:4048:8"
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
      "definition_site": "00aefa3c",
      "incomplete_value": false,
      "site": "00aefa44",
      "value": [
        "leaf",
        "const:326:8"
      ]
    },
    "old": null,
    "ordinal": 0,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00aef61c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aef604.md#insn-00aef61c) · [`00aef618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aef604.md#insn-00aef618) · [`00aef624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aef604.md#insn-00aef624)
- 新版 `00aefa44`（命令位置の公開資料なし） · `00aefa4c`（命令位置の公開資料なし）

~~~diff
- 00aef61c ["INT_ADD", "register:40f0:8", ["const:aef61c:8", "const:4:8"]]
- 00aef61c ["CALL", null, ["callee:008b79c8:8"]]
+ 00aefa44 ["INT_ADD", "register:40f0:8", ["const:aefa44:8", "const:4:8"]]
+ 00aefa44 ["CALL", null, ["callee:008b79c8:8"]]
- 00aef61c bytes da20f797
+ 00aefa44 bytes e11ff797
- 00aef618 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00aef618 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aef618 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aef618 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aef618 bytes 0001098b
- 00aef624 ["INT_ADD", "register:40f0:8", ["const:aef624:8", "const:4:8"]]
- 00aef624 ["CALL", null, ["callee:008b6f10:8"]]
+ 00aefa4c ["INT_ADD", "register:40f0:8", ["const:aefa4c:8", "const:4:8"]]
+ 00aefa4c ["CALL", null, ["callee:008b6f10:8"]]
- 00aef624 bytes 2a1ef797
+ 00aefa4c bytes 311df797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c06212ae1cb68d677cd5682bd74d35a4"></a>

### [`00aef6b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aef6b0.md) → [`00aefad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aef/00aefad8.md) FUN_00aefad8

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 10件 [`00467b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467b20.md) [`00469bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469bc4.md) [`00489f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f0c.md) [`008b6d58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6d58.md) [`008b7984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7984.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00467b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b60.md) [`00469c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469c04.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md) [`008b6d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6d9c.md) [`008b79c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b79c8.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 87.76% / 新版 87.76%

CFGの説明率　旧版 20.00% / 新版 13.89%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 26件, `unresolved_branch_alignment` 3件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00aefb28",
      "incomplete_value": true,
      "site": "00aefb28",
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
      "definition_site": "00aef700",
      "incomplete_value": true,
      "site": "00aef700",
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aef7a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aef7a8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aefb24",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00aef708",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "unmatched:00aef710",
      "PARAM",
      [
        "storage",
        "00c8d550",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00aefb24",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "00aefb30",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00aefb38",
      "PARAM",
      [
        "storage",
        "00c8d950",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aef700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aef6b0.md#insn-00aef700) · [`00aef718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aef6b0.md#insn-00aef718) · [`00aef74c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aef6b0.md#insn-00aef74c)
- 新版 `00aefb28`（命令位置の公開資料なし） · `00aefb40`（命令位置の公開資料なし） · `00aefb74`（命令位置の公開資料なし）

~~~diff
- 00aef700 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00aef700 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00aefb28 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00aefb28 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00aef700 bytes 200100b4
+ 00aefb28 bytes 200100b4
- 00aef718 ["INT_ADD", "register:40f0:8", ["const:aef718:8", "const:4:8"]]
- 00aef718 ["CALL", null, ["callee:00c58610:8"]]
+ 00aefb40 ["INT_ADD", "register:40f0:8", ["const:aefb40:8", "const:4:8"]]
+ 00aefb40 ["CALL", null, ["callee:00c58610:8"]]
- 00aef718 bytes bea20594
+ 00aefb40 bytes b4a20594
- 00aef74c ["INT_ADD", "register:40f0:8", ["const:aef74c:8", "const:4:8"]]
- 00aef74c ["CALL", null, ["callee:00467b60:8"]]
+ 00aefb74 ["INT_ADD", "register:40f0:8", ["const:aefb74:8", "const:4:8"]]
+ 00aefb74 ["CALL", null, ["callee:00467b60:8"]]
- 00aef74c bytes f5e0e597
+ 00aefb74 bytes fbdfe597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d184043c6f2eb5fc77dcd453f0e3be13"></a>

### [`00aef9ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aef9ec.md) → [`00aefe14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aef/00aefe14.md) FUN_00aefe14

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "00aefe34",
      "incomplete_value": false,
      "site": "00aefe38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:1e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aefa0c",
      "incomplete_value": false,
      "site": "00aefa10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8d000:8"
          ],
          [
            "leaf",
            "const:de8:8"
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
      "00aefe38",
      "DATA",
      [
        "storage",
        "00c8dde8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00aefe38",
      "DATA",
      [
        "storage",
        "00c8e1e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aefa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aef9ec.md#insn-00aefa00) · [`00aefa08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aef9ec.md#insn-00aefa08) · [`00aefa0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aef9ec.md#insn-00aefa0c)
- 新版 `00aefe28`（命令位置の公開資料なし） · `00aefe30`（命令位置の公開資料なし） · `00aefe34`（命令位置の公開資料なし）

~~~diff
- 00aefa00 ["INT_ADD", "register:40f0:8", ["const:aefa00:8", "const:4:8"]]
- 00aefa00 ["CALL", null, ["callee:00c57e90:8"]]
+ 00aefe28 ["INT_ADD", "register:40f0:8", ["const:aefe28:8", "const:4:8"]]
+ 00aefe28 ["CALL", null, ["callee:00c57e90:8"]]
- 00aefa00 bytes 24a00594
+ 00aefe28 bytes 1aa00594
- 00aefa08 ["COPY", "register:4040:8", ["const:c8d000:8"]]
+ 00aefe30 ["COPY", "register:4040:8", ["const:c8e000:8"]]
- 00aefa08 bytes e80c00d0
+ 00aefe30 bytes e80c00f0
- 00aefa0c ["COPY", "tmp:0:8", ["const:de8:8"]]
- 00aefa0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aefa0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aefa0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aefe34 ["COPY", "tmp:0:8", ["const:1e8:8"]]
+ 00aefe34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aefe34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aefe34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aefa0c bytes 08a13791
+ 00aefe34 bytes 08a10791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aebd96c6fe94c2388d2e693c8362ac70"></a>

### [`00aefa44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aefa44.md) → [`00aefe6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aef/00aefe6c.md) FUN_00aefe6c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 8件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b6e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e60.md) [`008b975c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b975c.md) [`00a466f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a466f8.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b6ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6ea4.md) [`008b97a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b97a0.md) [`00a468f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a468f0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 96.55% / 新版 96.55%

CFGの説明率　旧版 50.00% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00aefe8c",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00aefa64",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00aefa8c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aefec8",
      "incomplete_value": true,
      "site": "00aefed4",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "old": null,
    "ordinal": 3,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aefe8c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "unmatched:00aefa8c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00aefe8c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00aefeb4",
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

- 旧版 [`00aefa64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aefa44.md#insn-00aefa64) · [`00aefa8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aefa44.md#insn-00aefa8c) · [`00aefaac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aefa44.md#insn-00aefaac)
- 新版 `00aefe8c`（命令位置の公開資料なし） · `00aefed4`（命令位置の公開資料なし）

~~~diff
- 00aefa64 ["INT_ADD", "register:40f0:8", ["const:aefa64:8", "const:4:8"]]
- 00aefa64 ["CALL", null, ["ram:47acb4:8"]]
+ 00aefe8c ["INT_ADD", "register:40f0:8", ["const:aefe8c:8", "const:4:8"]]
+ 00aefe8c ["CALL", null, ["ram:47acf4:8"]]
- 00aefa64 bytes 942ce697
+ 00aefe8c bytes 9a2be697
- 00aefa8c ["INT_ADD", "register:40f0:8", ["const:aefa8c:8", "const:4:8"]]
- 00aefa8c ["CALL", null, ["ram:47acb4:8"]]
- 00aefa8c bytes 8a2ce697
- 00aefaac ["INT_ADD", "register:40f0:8", ["const:aefaac:8", "const:4:8"]]
- 00aefaac ["CALL", null, ["callee:008b6ea4:8"]]
+ 00aefed4 ["INT_ADD", "register:40f0:8", ["const:aefed4:8", "const:4:8"]]
+ 00aefed4 ["CALL", null, ["callee:008b6ea4:8"]]
- 00aefaac bytes ed1cf797
+ 00aefed4 bytes f41bf797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6915e6ffe7492f8369a565a82b91541"></a>

### [`00aefbb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aefbb0.md) → [`00aeffd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aef/00aeffd8.md) FUN_00aeffd8

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b6f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6f0c.md) [`00b0b218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0b/00b0b218.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b6f50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f50.md) [`00b0b640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0b/00b0b640.md)

変更の種類 branch_condition_or_target, call, call_count, call_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 91.11% / 新版 91.11%

CFGの説明率　旧版 14.29% / 新版 30.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aefbd4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aefc04"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00aefffc"
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
      "unmatched:00aefbd4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00aefbe8"
      ]
    ],
    [
      "00af0004",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "unmatched:00aefbe8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00aefffc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af0010"
      ]
    ],
    [
      "00af0004",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00af0010",
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

- 旧版 [`00aefbd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aefbb0.md#insn-00aefbd4) · [`00aefbdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aefbb0.md#insn-00aefbdc) · [`00aefbe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aefbb0.md#insn-00aefbe8)
- 新版 `00af0004`（命令位置の公開資料なし）

~~~diff
- 00aefbd4 ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
- 00aefbd4 bytes a0000054
- 00aefbdc ["INT_ADD", "register:40f0:8", ["const:aefbdc:8", "const:4:8"]]
- 00aefbdc ["CALL", null, ["ram:47acb4:8"]]
+ 00af0004 ["INT_ADD", "register:40f0:8", ["const:af0004:8", "const:4:8"]]
+ 00af0004 ["CALL", null, ["ram:47acf4:8"]]
- 00aefbdc bytes 362ce697
+ 00af0004 bytes 3c2be697
- 00aefbe8 ["INT_ADD", "register:40f0:8", ["const:aefbe8:8", "const:4:8"]]
- 00aefbe8 ["CALL", null, ["ram:47acb4:8"]]
- 00aefbe8 bytes 332ce697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2acc1f05dd3fd4af766c5a060c3815bf"></a>

### [`00aefc90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aefc90.md) → [`00af00b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af0/00af00b8.md) FUN_00af00b8

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aefcb4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aefcb4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00af00dc"
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
      "unmatched:00aefcb4",
      "DATA",
      [
        "storage",
        "00c8def8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00aefcb8",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aefcbc",
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
      "00af00dc",
      "DATA",
      [
        "storage",
        "00c8e2f8",
        null,
        "undefined *"
      ]
    ],
    [
      "00af00e0",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00af00e4",
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

- 旧版 [`00aefca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aefc90.md#insn-00aefca4) · [`00aefcb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aefc90.md#insn-00aefcb4) · [`00aefcc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aefc90.md#insn-00aefcc0)
- 新版 `00af00cc`（命令位置の公開資料なし）

~~~diff
- 00aefca4 ["INT_ADD", "register:40f0:8", ["const:aefca4:8", "const:4:8"]]
- 00aefca4 ["CALL", null, ["callee:00c57e90:8"]]
+ 00af00cc ["INT_ADD", "register:40f0:8", ["const:af00cc:8", "const:4:8"]]
+ 00af00cc ["CALL", null, ["callee:00c57e90:8"]]
- 00aefca4 bytes 7b9f0594
+ 00af00cc bytes 719f0594
- 00aefcb4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00aefcb4 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00aefcb4 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00aefcb4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aefcb4 bytes 082400a9
- 00aefcc0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00aefcc0 ["RETURN", null, ["register:0:8"]]
- 00aefcc0 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c29b43462d5526d757d3f865a3f4b810"></a>

### [`00aefce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aefce0.md) → [`00af0108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af0/00af0108.md) FUN_00af0108

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 19件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`005bc78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bc/005bc78c.md) [`007441c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00744/007441c8.md)
- 新版 呼出元 0件  · 呼出先 19件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`005bc7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bc/005bc7cc.md) [`00744208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00744/00744208.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 79.02% / 新版 79.02%

CFGの説明率　旧版 23.33% / 新版 19.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 1件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aefec0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aefef8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeff8c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00af0148",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00aefd44"
      ]
    ],
    [
      "00af0150",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "unmatched:00aefd44",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00af0148",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af016c"
      ]
    ],
    [
      "00af0150",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00af016c",
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

- 旧版 [`00aefd28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aefce0.md#insn-00aefd28) · [`00aefd44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aefce0.md#insn-00aefd44) · [`00aefe58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aefce0.md#insn-00aefe58)
- 新版 `00af0150`（命令位置の公開資料なし） · `00af0280`（命令位置の公開資料なし）

~~~diff
- 00aefd28 ["INT_ADD", "register:40f0:8", ["const:aefd28:8", "const:4:8"]]
- 00aefd28 ["CALL", null, ["ram:47acb4:8"]]
+ 00af0150 ["INT_ADD", "register:40f0:8", ["const:af0150:8", "const:4:8"]]
+ 00af0150 ["CALL", null, ["ram:47acf4:8"]]
- 00aefd28 bytes e32be697
+ 00af0150 bytes e92ae697
- 00aefd44 ["INT_ADD", "register:40f0:8", ["const:aefd44:8", "const:4:8"]]
- 00aefd44 ["CALL", null, ["ram:47acb4:8"]]
- 00aefd44 bytes dc2be697
- 00aefe58 ["INT_ADD", "register:40f0:8", ["const:aefe58:8", "const:4:8"]]
- 00aefe58 ["CALL", null, ["callee:00744208:8"]]
+ 00af0280 ["INT_ADD", "register:40f0:8", ["const:af0280:8", "const:4:8"]]
+ 00af0280 ["CALL", null, ["callee:00744208:8"]]
- 00aefe58 bytes dc50f197
+ 00af0280 bytes e24ff197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e89fa1903fb1b5f2992e5f8c940ab13"></a>

### [`00af0198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af0198.md) → [`00af05c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af0/00af05c0.md) FUN_00af05c0

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "site": "00af01b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00af05d8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00af01a0",
      "incomplete_value": false,
      "site": "00af01a4",
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
      "unmatched:00af01b0",
      "DATA",
      [
        "storage",
        "00c8df68",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00af01b4",
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
      "00af05d8",
      "DATA",
      [
        "storage",
        "00c8e368",
        null,
        "undefined *"
      ]
    ],
    [
      "00af05dc",
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

- 旧版 [`00af01a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af0198.md#insn-00af01a4) · [`00af01b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af0198.md#insn-00af01b0) · [`00af01b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af0198.md#insn-00af01b8)
- 新版 `00af05cc`（命令位置の公開資料なし）

~~~diff
- 00af01a4 ["INT_ADD", "register:40f0:8", ["const:af01a4:8", "const:4:8"]]
- 00af01a4 ["CALL", null, ["callee:00c57e90:8"]]
+ 00af05cc ["INT_ADD", "register:40f0:8", ["const:af05cc:8", "const:4:8"]]
+ 00af05cc ["CALL", null, ["callee:00c57e90:8"]]
- 00af01a4 bytes 3b9e0594
+ 00af05cc bytes 319e0594
- 00af01b0 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00af01b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00af01b0 bytes 080000f9
- 00af01b8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00af01b8 ["RETURN", null, ["register:0:8"]]
- 00af01b8 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d4246945fb1d1e8dc8e7969999e5c51"></a>

### [`00af0298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af0298.md) → [`00af06c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af0/00af06c0.md) FUN_00af06c0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`005bc78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bc/005bc78c.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md) [`00aeb76c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aeb/00aeb76c.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`005bc7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bc/005bc7cc.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`00aebb94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aeb/00aebb94.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 85.29% / 新版 85.29%

CFGの説明率　旧版 26.67% / 新版 44.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af0298"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af0298"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af029c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af0298",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af029c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af02c4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00af06c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af06c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00af06ec",
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

- 旧版 [`00af0298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af0298.md#insn-00af0298) · [`00af029c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af0298.md#insn-00af029c) · [`00af02c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af0298.md#insn-00af02c4)

~~~diff
- 00af0298 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af0298 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af0298 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00af0298 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af0298 bytes fd7bbea9
- 00af029c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00af029c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00af029c bytes f30b00f9
- 00af02c4 ["INT_ADD", "register:40f0:8", ["const:af02c4:8", "const:4:8"]]
- 00af02c4 ["CALL", null, ["ram:47acb4:8"]]
- 00af02c4 bytes 7c2ae697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cdc96678878e7e914e8cc6ac38d99dc5"></a>

### [`00af034c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af034c.md) → [`00af0774`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af0/00af0774.md) FUN_00af0774

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00af0788",
      "incomplete_value": false,
      "site": "00af078c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:478:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af0360",
      "incomplete_value": false,
      "site": "00af0364",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:78:8"
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
      "00af078c",
      "DATA",
      [
        "storage",
        "00c8e078",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00af078c",
      "DATA",
      [
        "storage",
        "00c8e478",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af0358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af034c.md#insn-00af0358) · [`00af0360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af034c.md#insn-00af0360)
- 新版 `00af0780`（命令位置の公開資料なし） · `00af0788`（命令位置の公開資料なし）

~~~diff
- 00af0358 ["INT_ADD", "register:40f0:8", ["const:af0358:8", "const:4:8"]]
- 00af0358 ["CALL", null, ["callee:00c57e90:8"]]
+ 00af0780 ["INT_ADD", "register:40f0:8", ["const:af0780:8", "const:4:8"]]
+ 00af0780 ["CALL", null, ["callee:00c57e90:8"]]
- 00af0358 bytes ce9d0594
+ 00af0780 bytes c49d0594
- 00af0360 ["COPY", "tmp:0:8", ["const:78:8"]]
- 00af0360 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00af0360 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00af0360 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00af0788 ["COPY", "tmp:0:8", ["const:478:8"]]
+ 00af0788 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00af0788 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00af0788 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00af0360 bytes 08e10191
+ 00af0788 bytes 08e11191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0f0b959979c591f67a2466a79321ee4"></a>

### [`00af0450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af0450.md) → [`00af0878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af0/00af0878.md) FUN_00af0878

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 15件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md) [`008b9588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9588.md)
- 新版 呼出元 0件  · 呼出先 15件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`008b95cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b95cc.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 82.50% / 新版 82.50%

CFGの説明率　旧版 74.36% / 新版 72.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af04d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af04dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af04e0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af0478",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af08e4"
      ]
    ],
    [
      "00af08b0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "unmatched:00af04d0",
      "READ",
      [
        "storage",
        "002adfef",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00af08a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af08e4"
      ]
    ],
    [
      "00af08b0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00af08f8",
      "READ",
      [
        "storage",
        "002ae02f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af0478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af0450.md#insn-00af0478) · [`00af0488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af0450.md#insn-00af0488) · [`00af04d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af0450.md#insn-00af04d8)
- 新版 `00af08b0`（命令位置の公開資料なし）

~~~diff
- 00af0478 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00af0478 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00af0478 bytes 21020054
- 00af0488 ["INT_ADD", "register:40f0:8", ["const:af0488:8", "const:4:8"]]
- 00af0488 ["CALL", null, ["ram:47acb4:8"]]
+ 00af08b0 ["INT_ADD", "register:40f0:8", ["const:af08b0:8", "const:4:8"]]
+ 00af08b0 ["CALL", null, ["ram:47acf4:8"]]
- 00af0488 bytes 0b2ae697
+ 00af08b0 bytes 1129e697
- 00af04d8 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00af04d8 ["COPY", "tmp:1:8", ["register:8:8"]]
- 00af04d8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00af04d8 bytes e8030039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3475b2035e00aaef51db86d03778928f"></a>

### [`00af075c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af075c.md) → [`00af0b84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af0/00af0b84.md) FUN_00af0b84

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00af0ba8",
      "incomplete_value": false,
      "site": "00af0ba8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:568:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af0780",
      "incomplete_value": false,
      "site": "00af0780",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:168:8"
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
      "00af0ba8",
      "DATA",
      [
        "storage",
        "00c8e168",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00af0ba8",
      "DATA",
      [
        "storage",
        "00c8e568",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af0770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af075c.md#insn-00af0770) · [`00af077c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af075c.md#insn-00af077c)
- 新版 `00af0b98`（命令位置の公開資料なし） · `00af0ba4`（命令位置の公開資料なし）

~~~diff
- 00af0770 ["INT_ADD", "register:40f0:8", ["const:af0770:8", "const:4:8"]]
- 00af0770 ["CALL", null, ["callee:00c57e90:8"]]
+ 00af0b98 ["INT_ADD", "register:40f0:8", ["const:af0b98:8", "const:4:8"]]
+ 00af0b98 ["CALL", null, ["callee:00c57e90:8"]]
- 00af0770 bytes c89c0594
+ 00af0b98 bytes be9c0594
- 00af077c ["COPY", "tmp:0:8", ["const:168:8"]]
- 00af077c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00af077c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00af077c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00af0ba4 ["COPY", "tmp:0:8", ["const:568:8"]]
+ 00af0ba4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00af0ba4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00af0ba4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00af077c bytes 08a10591
+ 00af0ba4 bytes 08a11591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3802a25ee57703859ebb9a6f459cd1e"></a>

### [`00af07ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af07ac.md) → [`00af0bd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af0/00af0bd4.md) FUN_00af0bd4

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md) [`00a1a508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a1a/00a1a508.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`00a1a6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a6a4.md)

変更の種類 branch_condition_or_target, call, call_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 96.15% / 新版 96.15%

CFGの説明率　旧版 83.33% / 新版 71.43%

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
      "site": "00af0bfc",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00af07d4",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "00af0bfc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00af0bfc",
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

- 旧版 [`00af07d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af07ac.md#insn-00af07d4) · [`00af07e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af07ac.md#insn-00af07e0) · [`00af07f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af07ac.md#insn-00af07f8)
- 新版 `00af0bfc`（命令位置の公開資料なし） · `00af0c08`（命令位置の公開資料なし） · `00af0c20`（命令位置の公開資料なし）

~~~diff
- 00af07d4 ["INT_ADD", "register:40f0:8", ["const:af07d4:8", "const:4:8"]]
- 00af07d4 ["CALL", null, ["ram:47acb4:8"]]
+ 00af0bfc ["INT_ADD", "register:40f0:8", ["const:af0bfc:8", "const:4:8"]]
+ 00af0bfc ["CALL", null, ["ram:47acf4:8"]]
- 00af07d4 bytes 3829e697
+ 00af0bfc bytes 3e28e697
- 00af07e0 ["INT_ADD", "register:40f0:8", ["const:af07e0:8", "const:4:8"]]
- 00af07e0 ["CALL", null, ["callee:0047cdd4:8"]]
+ 00af0c08 ["INT_ADD", "register:40f0:8", ["const:af0c08:8", "const:4:8"]]
+ 00af0c08 ["CALL", null, ["callee:0047cdd4:8"]]
- 00af07e0 bytes 6d31e697
+ 00af0c08 bytes 7330e697
- 00af07f8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00af07f8 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00af0c20 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00af0c20 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00af07f8 bytes c1000054
+ 00af0c20 bytes c1000054
~~~


<a id="compare-719d8897a6a4fe6a564da80cc7fe890b"></a>

### [`00af0874`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af0874.md) → [`00af0c9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af0/00af0c9c.md) FUN_00af0c9c

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00af0ca8",
      "incomplete_value": false,
      "site": "00af0ca8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:5e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af0880",
      "incomplete_value": false,
      "site": "00af0880",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:1e8:8"
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
      "00af0ca8",
      "DATA",
      [
        "storage",
        "00c8e1e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00af0ca8",
      "DATA",
      [
        "storage",
        "00c8e5e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af087c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af0874.md#insn-00af087c)
- 新版 `00af0ca4`（命令位置の公開資料なし）

~~~diff
- 00af087c ["COPY", "tmp:0:8", ["const:1e8:8"]]
- 00af087c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00af087c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00af087c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00af0ca4 ["COPY", "tmp:0:8", ["const:5e8:8"]]
+ 00af0ca4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00af0ca4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00af0ca4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00af087c bytes 29a10791
+ 00af0ca4 bytes 29a11791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b70f17806e36234f8961153f1c4850b"></a>

### [`00af0890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af0890.md) → [`00af0cb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af0/00af0cb8.md) FUN_00af0cb8

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af089c",
      "DATA",
      [
        "storage",
        "00336f60",
        null,
        "fde_table_entry"
      ]
    ],
    [
      "unmatched:00af08a4",
      "DATA",
      [
        "storage",
        "00336f60",
        null,
        "fde_table_entry"
      ]
    ]
  ],
  "added": [
    [
      "00af0cc4",
      "DATA",
      [
        "storage",
        "00336f60",
        null,
        "fde_table_entry"
      ]
    ],
    [
      "00af0ccc",
      "DATA",
      [
        "storage",
        "00336f60",
        null,
        "fde_table_entry"
      ]
    ]
  ]
}
~~~


<a id="compare-7782c0c2741fe3cfc2901109c25a2089"></a>

### [`00af08d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af08d8.md) → [`00af0d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af0/00af0d00.md) FUN_00af0d00

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00af0d24",
      "incomplete_value": false,
      "site": "00af0d24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:668:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af08fc",
      "incomplete_value": false,
      "site": "00af08fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:268:8"
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
      "00af0d24",
      "DATA",
      [
        "storage",
        "00c8e268",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00af0d24",
      "DATA",
      [
        "storage",
        "00c8e668",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af08ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af08d8.md#insn-00af08ec) · [`00af08f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af08d8.md#insn-00af08f8)
- 新版 `00af0d14`（命令位置の公開資料なし） · `00af0d20`（命令位置の公開資料なし）

~~~diff
- 00af08ec ["INT_ADD", "register:40f0:8", ["const:af08ec:8", "const:4:8"]]
- 00af08ec ["CALL", null, ["callee:00c57e90:8"]]
+ 00af0d14 ["INT_ADD", "register:40f0:8", ["const:af0d14:8", "const:4:8"]]
+ 00af0d14 ["CALL", null, ["callee:00c57e90:8"]]
- 00af08ec bytes 699c0594
+ 00af0d14 bytes 5f9c0594
- 00af08f8 ["COPY", "tmp:0:8", ["const:268:8"]]
- 00af08f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00af08f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00af08f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00af0d20 ["COPY", "tmp:0:8", ["const:668:8"]]
+ 00af0d20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00af0d20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00af0d20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00af08f8 bytes 08a10991
+ 00af0d20 bytes 08a11991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-198343308f5ff4dbd25a8c0bf1974c6d"></a>

### [`00af090c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af090c.md) → [`00af0d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af0/00af0d34.md) FUN_00af0d34

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00af0d40",
      "incomplete_value": false,
      "site": "00af0d40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:668:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af0918",
      "incomplete_value": false,
      "site": "00af0918",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:268:8"
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
      "00af0d40",
      "DATA",
      [
        "storage",
        "00c8e268",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00af0d40",
      "DATA",
      [
        "storage",
        "00c8e668",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af0914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af090c.md#insn-00af0914)
- 新版 `00af0d3c`（命令位置の公開資料なし）

~~~diff
- 00af0914 ["COPY", "tmp:0:8", ["const:268:8"]]
- 00af0914 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00af0914 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00af0914 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00af0d3c ["COPY", "tmp:0:8", ["const:668:8"]]
+ 00af0d3c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00af0d3c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00af0d3c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00af0914 bytes 29a10991
+ 00af0d3c bytes 29a11991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8a0d3aec7f2b335973deb5b7fb54025"></a>

### [`00af0928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af0928.md) → [`00af0d50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af0/00af0d50.md) FUN_00af0d50

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00468c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468c20.md) [`00469bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469bc4.md) [`0046d934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d934.md) [`00aea2fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aea/00aea2fc.md) [`00c58210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58210.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00468c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468c60.md) [`00469c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469c04.md) [`0046d974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d974.md) [`00aea724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aea/00aea724.md) [`00c58610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58610.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 82.46% / 新版 82.46%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af0960"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00af0d88"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af0d90",
      "incomplete_value": false,
      "site": "00af0da0",
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
      "definition_site": "00af0968",
      "incomplete_value": false,
      "site": "00af0978",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af094c",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00af0960",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af0dac"
      ]
    ],
    [
      "unmatched:00af0968",
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
      "00af0d74",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "00af0d88",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af0dac"
      ]
    ],
    [
      "00af0d90",
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

- 旧版 [`00af0960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af0928.md#insn-00af0960) · [`00af0978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af0928.md#insn-00af0978)
- 新版 `00af0da0`（命令位置の公開資料なし） · `00af0d88`（命令位置の公開資料なし）

~~~diff
- 00af0960 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00af0960 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00af0960 bytes 200100b4
- 00af0978 ["INT_ADD", "register:40f0:8", ["const:af0978:8", "const:4:8"]]
- 00af0978 ["CALL", null, ["callee:00c58610:8"]]
+ 00af0da0 ["INT_ADD", "register:40f0:8", ["const:af0da0:8", "const:4:8"]]
+ 00af0da0 ["CALL", null, ["callee:00c58610:8"]]
- 00af0978 bytes 269e0594
+ 00af0da0 bytes 1c9e0594
+ 00af0d88 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00af0d88 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00af0d88 bytes 200100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de54a8433fe5af7c911658e39b2b958c"></a>

### [`00af0a38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af0a38.md) → [`00af0e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af0/00af0e60.md) FUN_00af0e60

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00af0e84",
      "incomplete_value": false,
      "site": "00af0e84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:6f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af0a5c",
      "incomplete_value": false,
      "site": "00af0a5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:2f8:8"
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
      "00af0e84",
      "DATA",
      [
        "storage",
        "00c8e2f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00af0e84",
      "DATA",
      [
        "storage",
        "00c8e6f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af0a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af0a38.md#insn-00af0a4c) · [`00af0a58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af0a38.md#insn-00af0a58)
- 新版 `00af0e74`（命令位置の公開資料なし） · `00af0e80`（命令位置の公開資料なし）

~~~diff
- 00af0a4c ["INT_ADD", "register:40f0:8", ["const:af0a4c:8", "const:4:8"]]
- 00af0a4c ["CALL", null, ["callee:00c57e90:8"]]
+ 00af0e74 ["INT_ADD", "register:40f0:8", ["const:af0e74:8", "const:4:8"]]
+ 00af0e74 ["CALL", null, ["callee:00c57e90:8"]]
- 00af0a4c bytes 119c0594
+ 00af0e74 bytes 079c0594
- 00af0a58 ["COPY", "tmp:0:8", ["const:2f8:8"]]
- 00af0a58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00af0a58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00af0a58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00af0e80 ["COPY", "tmp:0:8", ["const:6f8:8"]]
+ 00af0e80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00af0e80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00af0e80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00af0a58 bytes 08e10b91
+ 00af0e80 bytes 08e11b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2124e43677fede03bb3446bdec4be5eb"></a>

### [`00af0a88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af0a88.md) → [`00af0eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af0/00af0eb0.md) FUN_00af0eb0

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af0a94",
      "DATA",
      [
        "storage",
        "00336f60",
        null,
        "fde_table_entry"
      ]
    ],
    [
      "unmatched:00af0a9c",
      "DATA",
      [
        "storage",
        "00336f60",
        null,
        "fde_table_entry"
      ]
    ]
  ],
  "added": [
    [
      "00af0ebc",
      "DATA",
      [
        "storage",
        "00336f60",
        null,
        "fde_table_entry"
      ]
    ],
    [
      "00af0ec4",
      "DATA",
      [
        "storage",
        "00336f60",
        null,
        "fde_table_entry"
      ]
    ]
  ]
}
~~~


<a id="compare-3c160714a692ab40171b374ba0d6559c"></a>

### [`00af0b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af0b20.md) → [`00af0f48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af0/00af0f48.md) FUN_00af0f48

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 8件 [`0046bb28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046bb28.md) [`0046d934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d934.md) [`0046d96c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d96c.md) [`008b6d58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6d58.md) [`008b6e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e14.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0046bb68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046bb68.md) [`0046d974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d974.md) [`0046d9ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d9ac.md) [`008b6d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6d9c.md) [`008b6e58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6e58.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 66.28% / 新版 66.28%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af0b24"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af0b28"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af0b28"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af0b24",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af0b28",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af0b2c",
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
      "00af0f4c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00af0f50",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00af0f54",
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

- 旧版 [`00af0b24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af0b20.md#insn-00af0b24) · [`00af0b28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af0b20.md#insn-00af0b28) · [`00af0b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af0b20.md#insn-00af0b2c)

~~~diff
- 00af0b24 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00af0b24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5140:8"]]
- 00af0b24 bytes ea1300fd
- 00af0b28 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:30:8"]]
- 00af0b28 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5120:8"]]
- 00af0b28 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:8:8"]]
- 00af0b28 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5100:8"]]
- 00af0b28 bytes e923036d
- 00af0b2c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af0b2c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af0b2c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00af0b2c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af0b2c bytes fd7b04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84720d9aa416a4f68e8a6cf06aae2da6"></a>

### [`00af0f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af0f48.md) → [`00af1370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af1/00af1370.md) FUN_00af1370

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 11件 [`0046bb28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046bb28.md) [`0046d934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d934.md) [`0046d96c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d96c.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b6d58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6d58.md)
- 新版 呼出元 0件  · 呼出先 11件 [`0046bb68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046bb68.md) [`0046d974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d974.md) [`0046d9ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d9ac.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b6d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6d9c.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 86.60% / 新版 86.60%

CFGの説明率　旧版 10.00% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 5件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af1094"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af1098"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af109c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00af139c",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00af0f84",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "unmatched:00af0f8c",
      "PARAM",
      [
        "storage",
        "00c8d550",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00af139c",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "00af13ac",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00af13b4",
      "PARAM",
      [
        "storage",
        "00c8d950",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af0f7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af0f48.md#insn-00af0f7c) · [`00af0f94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af0f48.md#insn-00af0f94) · [`00af0fb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af0f48.md#insn-00af0fb4)
- 新版 `00af13a4`（命令位置の公開資料なし） · `00af13bc`（命令位置の公開資料なし） · `00af13dc`（命令位置の公開資料なし）

~~~diff
- 00af0f7c ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00af0f7c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00af13a4 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00af13a4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00af0f7c bytes 200100b4
+ 00af13a4 bytes 200100b4
- 00af0f94 ["INT_ADD", "register:40f0:8", ["const:af0f94:8", "const:4:8"]]
- 00af0f94 ["CALL", null, ["callee:00c58610:8"]]
+ 00af13bc ["INT_ADD", "register:40f0:8", ["const:af13bc:8", "const:4:8"]]
+ 00af13bc ["CALL", null, ["callee:00c58610:8"]]
- 00af0f94 bytes 9f9c0594
+ 00af13bc bytes 959c0594
- 00af0fb4 ["INT_ADD", "register:40f0:8", ["const:af0fb4:8", "const:4:8"]]
- 00af0fb4 ["CALL", null, ["callee:008b79c8:8"]]
+ 00af13dc ["INT_ADD", "register:40f0:8", ["const:af13dc:8", "const:4:8"]]
+ 00af13dc ["CALL", null, ["callee:008b79c8:8"]]
- 00af0fb4 bytes 741af797
+ 00af13dc bytes 7b19f797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99105d4a48b0e6a8c5042f04f01bdf7d"></a>

### [`00af10f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af10f8.md) → [`00af1520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af1/00af1520.md) FUN_00af1520

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00af1534",
      "incomplete_value": false,
      "site": "00af1538",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:9f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af110c",
      "incomplete_value": false,
      "site": "00af1110",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:5f8:8"
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
      "00af1538",
      "DATA",
      [
        "storage",
        "00c8e5f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00af1538",
      "DATA",
      [
        "storage",
        "00c8e9f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af1104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af10f8.md#insn-00af1104) · [`00af110c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af10f8.md#insn-00af110c)
- 新版 `00af152c`（命令位置の公開資料なし） · `00af1534`（命令位置の公開資料なし）

~~~diff
- 00af1104 ["INT_ADD", "register:40f0:8", ["const:af1104:8", "const:4:8"]]
- 00af1104 ["CALL", null, ["callee:00c57e90:8"]]
+ 00af152c ["INT_ADD", "register:40f0:8", ["const:af152c:8", "const:4:8"]]
+ 00af152c ["CALL", null, ["callee:00c57e90:8"]]
- 00af1104 bytes 639a0594
+ 00af152c bytes 599a0594
- 00af110c ["COPY", "tmp:0:8", ["const:5f8:8"]]
- 00af110c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00af110c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00af110c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00af1534 ["COPY", "tmp:0:8", ["const:9f8:8"]]
+ 00af1534 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00af1534 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00af1534 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00af110c bytes 08e11791
+ 00af1534 bytes 08e12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7edf617caa823325ad21b830a735cb1"></a>

### [`00af1134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af1134.md) → [`00af155c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af1/00af155c.md) FUN_00af155c

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 50.00% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00af1150"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00af1154",
      "incomplete_value": false,
      "site": "00af115c",
      "value": [
        "leaf",
        "const:b:8"
      ]
    },
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00af1158",
      "incomplete_value": false,
      "site": "00af115c",
      "value": [
        "leaf",
        "const:0:8"
      ]
    },
    "ordinal": 1,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af1150",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00af1578",
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

- 旧版 [`00af1150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af1134.md#insn-00af1150) · [`00af115c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af1134.md#insn-00af115c)
- 新版 `00af1584`（命令位置の公開資料なし） · `00af1578`（命令位置の公開資料なし）

~~~diff
- 00af1150 ["INT_ADD", "register:40f0:8", ["const:af1150:8", "const:4:8"]]
- 00af1150 ["CALL", null, ["ram:47acb4:8"]]
- 00af1150 bytes d926e697
- 00af115c ["INT_ADD", "register:40f0:8", ["const:af115c:8", "const:4:8"]]
- 00af115c ["CALL", null, ["callee:0047cdd4:8"]]
+ 00af1584 ["INT_ADD", "register:40f0:8", ["const:af1584:8", "const:4:8"]]
+ 00af1584 ["CALL", null, ["callee:0047cdd4:8"]]
- 00af115c bytes 0e2fe697
+ 00af1584 bytes 142ee697
+ 00af1578 ["INT_ADD", "register:40f0:8", ["const:af1578:8", "const:4:8"]]
+ 00af1578 ["CALL", null, ["ram:47acf4:8"]]
+ 00af1578 bytes df25e697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba5256dc95ff3cc539ee968118841e11"></a>

### [`00af11a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af11a0.md) → [`00af15c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af1/00af15c8.md) FUN_00af15c8

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00af15dc",
      "incomplete_value": false,
      "site": "00af15e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:a78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af11b4",
      "incomplete_value": false,
      "site": "00af11b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:678:8"
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
      "00af15e0",
      "DATA",
      [
        "storage",
        "00c8e678",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00af15e0",
      "DATA",
      [
        "storage",
        "00c8ea78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af11ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af11a0.md#insn-00af11ac) · [`00af11b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af11a0.md#insn-00af11b4)
- 新版 `00af15d4`（命令位置の公開資料なし） · `00af15dc`（命令位置の公開資料なし）

~~~diff
- 00af11ac ["INT_ADD", "register:40f0:8", ["const:af11ac:8", "const:4:8"]]
- 00af11ac ["CALL", null, ["callee:00c57e90:8"]]
+ 00af15d4 ["INT_ADD", "register:40f0:8", ["const:af15d4:8", "const:4:8"]]
+ 00af15d4 ["CALL", null, ["callee:00c57e90:8"]]
- 00af11ac bytes 399a0594
+ 00af15d4 bytes 2f9a0594
- 00af11b4 ["COPY", "tmp:0:8", ["const:678:8"]]
- 00af11b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00af11b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00af11b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00af15dc ["COPY", "tmp:0:8", ["const:a78:8"]]
+ 00af15dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00af15dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00af15dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00af11b4 bytes 08e11991
+ 00af15dc bytes 08e12991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b635d6a4097a9830f59ea5ac5a97664b"></a>

### [`00af11dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af11dc.md) → [`00af1604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af1/00af1604.md) FUN_00af1604

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.75% / 新版 93.75%

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
      "site": "00af1620",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00af11f8",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "00af1620",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00af1620",
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

- 旧版 [`00af11f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af11dc.md#insn-00af11f8) · [`00af1204`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af11dc.md#insn-00af1204)
- 新版 `00af1620`（命令位置の公開資料なし） · `00af162c`（命令位置の公開資料なし）

~~~diff
- 00af11f8 ["INT_ADD", "register:40f0:8", ["const:af11f8:8", "const:4:8"]]
- 00af11f8 ["CALL", null, ["ram:47acb4:8"]]
+ 00af1620 ["INT_ADD", "register:40f0:8", ["const:af1620:8", "const:4:8"]]
+ 00af1620 ["CALL", null, ["ram:47acf4:8"]]
- 00af11f8 bytes af26e697
+ 00af1620 bytes b525e697
- 00af1204 ["INT_ADD", "register:40f0:8", ["const:af1204:8", "const:4:8"]]
- 00af1204 ["CALL", null, ["callee:0047cdd4:8"]]
+ 00af162c ["INT_ADD", "register:40f0:8", ["const:af162c:8", "const:4:8"]]
+ 00af162c ["CALL", null, ["callee:0047cdd4:8"]]
- 00af1204 bytes e42ee697
+ 00af162c bytes ea2de697
~~~


<a id="compare-189e6663f3f73a8a22d62b6b9ccc2039"></a>

### [`00af1248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af1248.md) → [`00af1670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af1/00af1670.md) FUN_00af1670

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00af1684",
      "incomplete_value": false,
      "site": "00af1688",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:af8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af125c",
      "incomplete_value": false,
      "site": "00af1260",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:6f8:8"
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
      "00af1688",
      "DATA",
      [
        "storage",
        "00c8e6f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00af1688",
      "DATA",
      [
        "storage",
        "00c8eaf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af1254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af1248.md#insn-00af1254) · [`00af125c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af1248.md#insn-00af125c)
- 新版 `00af167c`（命令位置の公開資料なし） · `00af1684`（命令位置の公開資料なし）

~~~diff
- 00af1254 ["INT_ADD", "register:40f0:8", ["const:af1254:8", "const:4:8"]]
- 00af1254 ["CALL", null, ["callee:00c57e90:8"]]
+ 00af167c ["INT_ADD", "register:40f0:8", ["const:af167c:8", "const:4:8"]]
+ 00af167c ["CALL", null, ["callee:00c57e90:8"]]
- 00af1254 bytes 0f9a0594
+ 00af167c bytes 059a0594
- 00af125c ["COPY", "tmp:0:8", ["const:6f8:8"]]
- 00af125c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00af125c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00af125c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00af1684 ["COPY", "tmp:0:8", ["const:af8:8"]]
+ 00af1684 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00af1684 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00af1684 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00af125c bytes 08e11b91
+ 00af1684 bytes 08e12b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b04a570393024e224552178d652492d"></a>

### [`00af1284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af1284.md) → [`00af16ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af1/00af16ac.md) FUN_00af16ac

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md) [`00ad0210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad0/00ad0210.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`00ad040c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ad0/00ad040c.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.67% / 新版 96.67%

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
      "site": "00af16d4",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00af12ac",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "site": "00af174c",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00af1324",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "00af16d4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00af174c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00af16d4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00af174c",
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

- 旧版 [`00af12ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af1284.md#insn-00af12ac) · [`00af1324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af1284.md#insn-00af1324) · [`00af12b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af1284.md#insn-00af12b8)
- 新版 `00af16d4`（命令位置の公開資料なし） · `00af174c`（命令位置の公開資料なし） · `00af16e0`（命令位置の公開資料なし）

~~~diff
- 00af12ac ["INT_ADD", "register:40f0:8", ["const:af12ac:8", "const:4:8"]]
- 00af12ac ["CALL", null, ["ram:47acb4:8"]]
+ 00af16d4 ["INT_ADD", "register:40f0:8", ["const:af16d4:8", "const:4:8"]]
+ 00af16d4 ["CALL", null, ["ram:47acf4:8"]]
- 00af12ac bytes 8226e697
+ 00af16d4 bytes 8825e697
- 00af1324 ["INT_ADD", "register:40f0:8", ["const:af1324:8", "const:4:8"]]
- 00af1324 ["CALL", null, ["ram:47acb4:8"]]
+ 00af174c ["INT_ADD", "register:40f0:8", ["const:af174c:8", "const:4:8"]]
+ 00af174c ["CALL", null, ["ram:47acf4:8"]]
- 00af1324 bytes 6426e697
+ 00af174c bytes 6a25e697
- 00af12b8 ["INT_ADD", "register:40f0:8", ["const:af12b8:8", "const:4:8"]]
- 00af12b8 ["CALL", null, ["callee:0047cdd4:8"]]
+ 00af16e0 ["INT_ADD", "register:40f0:8", ["const:af16e0:8", "const:4:8"]]
+ 00af16e0 ["CALL", null, ["callee:0047cdd4:8"]]
- 00af12b8 bytes b72ee697
+ 00af16e0 bytes bd2de697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0a977d967bc54c02f2a79ca652fae55"></a>

### [`00af13a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af13a0.md) → [`00af17c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af1/00af17c8.md) FUN_00af17c8

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00af17dc",
      "incomplete_value": false,
      "site": "00af17e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:b78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af13b4",
      "incomplete_value": false,
      "site": "00af13b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:778:8"
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
      "00af17e0",
      "DATA",
      [
        "storage",
        "00c8e778",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00af17e0",
      "DATA",
      [
        "storage",
        "00c8eb78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af13ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af13a0.md#insn-00af13ac) · [`00af13b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af13a0.md#insn-00af13b4)
- 新版 `00af17d4`（命令位置の公開資料なし） · `00af17dc`（命令位置の公開資料なし）

~~~diff
- 00af13ac ["INT_ADD", "register:40f0:8", ["const:af13ac:8", "const:4:8"]]
- 00af13ac ["CALL", null, ["callee:00c57e90:8"]]
+ 00af17d4 ["INT_ADD", "register:40f0:8", ["const:af17d4:8", "const:4:8"]]
+ 00af17d4 ["CALL", null, ["callee:00c57e90:8"]]
- 00af13ac bytes b9990594
+ 00af17d4 bytes af990594
- 00af13b4 ["COPY", "tmp:0:8", ["const:778:8"]]
- 00af13b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00af13b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00af13b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00af17dc ["COPY", "tmp:0:8", ["const:b78:8"]]
+ 00af17dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00af17dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00af17dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00af13b4 bytes 08e11d91
+ 00af17dc bytes 08e12d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c928a1d3c85f467f9c9c771d446044d"></a>

### [`00af13dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af13dc.md) → [`00af1804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af1/00af1804.md) FUN_00af1804

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 branch_condition_or_target, call, call_count, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 60.00% / 新版 69.23%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af13dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af13dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af13e0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af13dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af13e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af1404",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00af1804",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af1808",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00af182c",
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

- 旧版 [`00af13dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af13dc.md#insn-00af13dc) · [`00af13e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af13dc.md#insn-00af13e0) · [`00af1404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af13dc.md#insn-00af1404)

~~~diff
- 00af13dc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af13dc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af13dc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00af13dc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af13dc bytes fd7bbea9
- 00af13e0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00af13e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00af13e0 bytes f30b00f9
- 00af1404 ["INT_ADD", "register:40f0:8", ["const:af1404:8", "const:4:8"]]
- 00af1404 ["CALL", null, ["ram:47acb4:8"]]
- 00af1404 bytes 2c26e697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3bd6fda151a0487e77390c1173e7f7d"></a>

### [`00af14bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af14bc.md) → [`00af18e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af1/00af18e4.md) FUN_00af18e4

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "00af1904",
      "incomplete_value": false,
      "site": "00af1908",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:bf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af14dc",
      "incomplete_value": false,
      "site": "00af14e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:7f8:8"
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
      "00af1908",
      "DATA",
      [
        "storage",
        "00c8e7f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00af1908",
      "DATA",
      [
        "storage",
        "00c8ebf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af14d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af14bc.md#insn-00af14d0) · [`00af14dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af14bc.md#insn-00af14dc)
- 新版 `00af18f8`（命令位置の公開資料なし） · `00af1904`（命令位置の公開資料なし）

~~~diff
- 00af14d0 ["INT_ADD", "register:40f0:8", ["const:af14d0:8", "const:4:8"]]
- 00af14d0 ["CALL", null, ["callee:00c57e90:8"]]
+ 00af18f8 ["INT_ADD", "register:40f0:8", ["const:af18f8:8", "const:4:8"]]
+ 00af18f8 ["CALL", null, ["callee:00c57e90:8"]]
- 00af14d0 bytes 70990594
+ 00af18f8 bytes 66990594
- 00af14dc ["COPY", "tmp:0:8", ["const:7f8:8"]]
- 00af14dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00af14dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00af14dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00af1904 ["COPY", "tmp:0:8", ["const:bf8:8"]]
+ 00af1904 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00af1904 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00af1904 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00af14dc bytes 08e11f91
+ 00af1904 bytes 08e12f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8cf6f65613d99fab7b244d6f9dec046"></a>

### [`00af1514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af1514.md) → [`00af193c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af1/00af193c.md) FUN_00af193c

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 19件 [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`00467b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467b20.md) [`00467f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467f14.md) [`004687c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/004687c4.md) [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md)
- 新版 呼出元 0件  · 呼出先 19件 [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00467b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b60.md) [`00467f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467f54.md) [`00468804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468804.md) [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 82.02% / 新版 82.02%

CFGの説明率　旧版 12.90% / 新版 8.16%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 24件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 8件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af1554"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00af197c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af1664"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af1554",
      "WRITE",
      [
        "storage",
        "Stack[-0xc8]",
        null,
        null
      ]
    ],
    [
      "00af19b4",
      "DATA",
      [
        "storage",
        "00436258",
        null,
        "byte[63]"
      ]
    ],
    [
      "unmatched:00af1664",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af1c64"
      ]
    ]
  ],
  "added": [
    [
      "00af197c",
      "WRITE",
      [
        "storage",
        "Stack[-0xc8]",
        null,
        null
      ]
    ],
    [
      "00af19b4",
      "DATA",
      [
        "storage",
        "00436258",
        null,
        "qword"
      ]
    ],
    [
      "00af1a8c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af1c64"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af1554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af1514.md#insn-00af1554) · [`00af155c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af1514.md#insn-00af155c) · [`00af15c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af1514.md#insn-00af15c8)
- 新版 `00af1984`（命令位置の公開資料なし） · `00af19f0`（命令位置の公開資料なし）

~~~diff
- 00af1554 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:38:8"]]
- 00af1554 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00af1554 bytes e01f00f9
- 00af155c ["INT_ADD", "register:40f0:8", ["const:af155c:8", "const:4:8"]]
- 00af155c ["CALL", null, ["callee:008b9290:8"]]
+ 00af1984 ["INT_ADD", "register:40f0:8", ["const:af1984:8", "const:4:8"]]
+ 00af1984 ["CALL", null, ["callee:008b9290:8"]]
- 00af155c bytes 3c1ff797
+ 00af1984 bytes 431ef797
- 00af15c8 ["INT_ADD", "register:40f0:8", ["const:af15c8:8", "const:4:8"]]
- 00af15c8 ["CALL", null, ["callee:0046965c:8"]]
+ 00af19f0 ["INT_ADD", "register:40f0:8", ["const:af19f0:8", "const:4:8"]]
+ 00af19f0 ["CALL", null, ["callee:0046965c:8"]]
- 00af15c8 bytes 15e0e597
+ 00af19f0 bytes 1bdfe597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-223ac60f0bdd8be0f81825d9c8932d14"></a>

### [`00af1b0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af1b0c.md) → [`00af1f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af1/00af1f34.md) FUN_00af1f34

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.75% / 新版 93.75%

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
      "site": "00af1f50",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00af1b28",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af1f54",
      "incomplete_value": false,
      "site": "00af1f5c",
      "value": [
        "leaf",
        "const:b:8"
      ]
    },
    "old": null,
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
      "00af1f50",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00af1f50",
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

- 旧版 [`00af1b28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af1b0c.md#insn-00af1b28) · [`00af1b34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af1b0c.md#insn-00af1b34)
- 新版 `00af1f50`（命令位置の公開資料なし） · `00af1f5c`（命令位置の公開資料なし）

~~~diff
- 00af1b28 ["INT_ADD", "register:40f0:8", ["const:af1b28:8", "const:4:8"]]
- 00af1b28 ["CALL", null, ["ram:47acb4:8"]]
+ 00af1f50 ["INT_ADD", "register:40f0:8", ["const:af1f50:8", "const:4:8"]]
+ 00af1f50 ["CALL", null, ["ram:47acf4:8"]]
- 00af1b28 bytes 6324e697
+ 00af1f50 bytes 6923e697
- 00af1b34 ["INT_ADD", "register:40f0:8", ["const:af1b34:8", "const:4:8"]]
- 00af1b34 ["CALL", null, ["callee:0047cdd4:8"]]
+ 00af1f5c ["INT_ADD", "register:40f0:8", ["const:af1f5c:8", "const:4:8"]]
+ 00af1f5c ["CALL", null, ["callee:0047cdd4:8"]]
- 00af1b34 bytes 982ce697
+ 00af1f5c bytes 9e2be697
~~~


<a id="compare-7e666903ee877758a87ebde0d751def3"></a>

### [`00af1b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af1b78.md) → [`00af1fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af1/00af1fa0.md) FUN_00af1fa0

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00af1fb4",
      "incomplete_value": false,
      "site": "00af1fb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:cf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af1b8c",
      "incomplete_value": false,
      "site": "00af1b90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:8f8:8"
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
      "00af1fb8",
      "DATA",
      [
        "storage",
        "00c8e8f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00af1fb8",
      "DATA",
      [
        "storage",
        "00c8ecf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af1b84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af1b78.md#insn-00af1b84) · [`00af1b8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af1b78.md#insn-00af1b8c)
- 新版 `00af1fac`（命令位置の公開資料なし） · `00af1fb4`（命令位置の公開資料なし）

~~~diff
- 00af1b84 ["INT_ADD", "register:40f0:8", ["const:af1b84:8", "const:4:8"]]
- 00af1b84 ["CALL", null, ["callee:00c57e90:8"]]
+ 00af1fac ["INT_ADD", "register:40f0:8", ["const:af1fac:8", "const:4:8"]]
+ 00af1fac ["CALL", null, ["callee:00c57e90:8"]]
- 00af1b84 bytes c3970594
+ 00af1fac bytes b9970594
- 00af1b8c ["COPY", "tmp:0:8", ["const:8f8:8"]]
- 00af1b8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00af1b8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00af1b8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00af1fb4 ["COPY", "tmp:0:8", ["const:cf8:8"]]
+ 00af1fb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00af1fb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00af1fb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00af1b8c bytes 08e12391
+ 00af1fb4 bytes 08e13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74f20207e38b028a00dfbf82f3bd0457"></a>

### [`00af1bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af1bb4.md) → [`00af1fdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af1/00af1fdc.md) FUN_00af1fdc

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 33.33% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00af1bd0"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af1ffc",
      "incomplete_value": false,
      "site": "00af2004",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af2000",
      "incomplete_value": false,
      "site": "00af2004",
      "value": [
        "leaf",
        "const:0:8"
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af1bd0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00af1ff8",
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

- 旧版 [`00af1bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af1bb4.md#insn-00af1bd0) · [`00af1bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af1bb4.md#insn-00af1bdc)
- 新版 `00af2004`（命令位置の公開資料なし） · `00af1ff8`（命令位置の公開資料なし）

~~~diff
- 00af1bd0 ["INT_ADD", "register:40f0:8", ["const:af1bd0:8", "const:4:8"]]
- 00af1bd0 ["CALL", null, ["ram:47acb4:8"]]
- 00af1bd0 bytes 3924e697
- 00af1bdc ["INT_ADD", "register:40f0:8", ["const:af1bdc:8", "const:4:8"]]
- 00af1bdc ["CALL", null, ["callee:0047cdd4:8"]]
+ 00af2004 ["INT_ADD", "register:40f0:8", ["const:af2004:8", "const:4:8"]]
+ 00af2004 ["CALL", null, ["callee:0047cdd4:8"]]
- 00af1bdc bytes 6e2ce697
+ 00af2004 bytes 742be697
+ 00af1ff8 ["INT_ADD", "register:40f0:8", ["const:af1ff8:8", "const:4:8"]]
+ 00af1ff8 ["CALL", null, ["ram:47acf4:8"]]
+ 00af1ff8 bytes 3f23e697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb060100e5dd1de0b03e0b1eb18915f1"></a>

### [`00af1c5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af1c5c.md) → [`00af2084`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af2/00af2084.md) FUN_00af2084

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 branch_condition_or_target, call, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 25.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_condition` 3件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af1c64"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00af208c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00af20a0",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00af1c78",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "unmatched:00af1c64",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af20c0"
      ]
    ],
    [
      "00af20a0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00af208c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af20c0"
      ]
    ],
    [
      "00af20a0",
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

- 旧版 [`00af1c64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af1c5c.md#insn-00af1c64) · [`00af1c78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af1c5c.md#insn-00af1c78)
- 新版 `00af20a0`（命令位置の公開資料なし） · `00af208c`（命令位置の公開資料なし）

~~~diff
- 00af1c64 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00af1c64 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00af1c64 bytes a1010054
- 00af1c78 ["INT_ADD", "register:40f0:8", ["const:af1c78:8", "const:4:8"]]
- 00af1c78 ["CALL", null, ["ram:47acb4:8"]]
+ 00af20a0 ["INT_ADD", "register:40f0:8", ["const:af20a0:8", "const:4:8"]]
+ 00af20a0 ["CALL", null, ["ram:47acf4:8"]]
- 00af1c78 bytes 0f24e697
+ 00af20a0 bytes 1523e697
+ 00af208c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00af208c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00af208c bytes a1010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81bff77287afa6b7cc3dcdf18aa45668"></a>

### [`00af1cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af1cc4.md) → [`00af20ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af2/00af20ec.md) _INIT_248

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 72.32% / 新版 72.32%

CFGの説明率　旧版 30.56% / 新版 28.95%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_store_alignment` 16件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af1cf4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af1d08"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af1d0c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af1cf4",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af1d00",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00af1d08",
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
      "00af211c",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00af2128",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00af2130",
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

- 旧版 [`00af1cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af1cc4.md#insn-00af1cf4) · [`00af1d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af1cc4.md#insn-00af1d08) · [`00af1d0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af1cc4.md#insn-00af1d0c)

~~~diff
- 00af1cf4 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00af1cf4 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00af1cf4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00af1cf4 bytes a9831ff8
- 00af1d08 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 00af1d08 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:21:8"]]
- 00af1d08 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 00af1d08 bytes ea130278
- 00af1d0c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 00af1d0c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00af1d0c bytes e92b00b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26e64566a559d267d1b5b2311c45b8de"></a>

### [`00af2054`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af2/00af2054.md) → [`00af247c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af2/00af247c.md) _INIT_249

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 63.84% / 新版 63.84%

CFGの説明率　旧版 52.27% / 新版 67.65%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 16件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 31件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af2084"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af20ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af20d0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af2084",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af2090",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00af20ac",
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
      "00af24ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00af24b8",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00af24d4",
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

- 旧版 [`00af2084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af2/00af2054.md#insn-00af2084) · [`00af20ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af2/00af2054.md#insn-00af20ac) · [`00af20d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af2/00af2054.md#insn-00af20d0)

~~~diff
- 00af2084 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00af2084 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00af2084 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00af2084 bytes a9831ff8
- 00af20ac ["INT_ADD", "tmp:0:8", ["register:8:8", "const:11:8"]]
- 00af20ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00af20ac bytes e013813c
- 00af20d0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:31:8"]]
- 00af20d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00af20d0 bytes e013833c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6b49636c381188f3a062b330e521168"></a>

### [`00af2e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af2/00af2e60.md) → [`00af3288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af3/00af3288.md) FUN_00af3288

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a47d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a47d08.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a47f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47f00.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af2e74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af2/00af2e60.md#insn-00af2e74)
- 新版 `00af329c`（命令位置の公開資料なし）

~~~diff
- 00af2e74 ["INT_ADD", "register:40f0:8", ["const:af2e74:8", "const:4:8"]]
- 00af2e74 ["CALL", null, ["callee:008514f8:8"]]
+ 00af329c ["INT_ADD", "register:40f0:8", ["const:af329c:8", "const:4:8"]]
+ 00af329c ["CALL", null, ["callee:008514f8:8"]]
- 00af2e74 bytes 9179f597
+ 00af329c bytes 9778f597
~~~


<a id="compare-aefe4d0dd2cf8d0babd894d791b91ab9"></a>

### [`00af2ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af2/00af2ed4.md) → [`00af32fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af3/00af32fc.md) FUN_00af32fc

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a47d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a47d08.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a47f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47f00.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af2ee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af2/00af2ed4.md#insn-00af2ee8)
- 新版 `00af3310`（命令位置の公開資料なし）

~~~diff
- 00af2ee8 ["INT_ADD", "register:40f0:8", ["const:af2ee8:8", "const:4:8"]]
- 00af2ee8 ["CALL", null, ["callee:008514f8:8"]]
+ 00af3310 ["INT_ADD", "register:40f0:8", ["const:af3310:8", "const:4:8"]]
+ 00af3310 ["CALL", null, ["callee:008514f8:8"]]
- 00af2ee8 bytes 7479f597
+ 00af3310 bytes 7a78f597
~~~


<a id="compare-3e9a519e4e6127418c18ad546519f8ad"></a>

### [`00af2f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af2/00af2f0c.md) → [`00af3334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af3/00af3334.md) FUN_00af3334

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00707ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00707ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707ee0.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af2f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af2/00af2f0c.md#insn-00af2f1c)
- 新版 `00af3344`（命令位置の公開資料なし）

~~~diff
- 00af2f1c ["INT_ADD", "register:40f0:8", ["const:af2f1c:8", "const:4:8"]]
- 00af2f1c ["CALL", null, ["callee:008514f8:8"]]
+ 00af3344 ["INT_ADD", "register:40f0:8", ["const:af3344:8", "const:4:8"]]
+ 00af3344 ["CALL", null, ["callee:008514f8:8"]]
- 00af2f1c bytes 6779f597
+ 00af3344 bytes 6d78f597
~~~


<a id="compare-086b31865b9504ea096f1184d75ec878"></a>

### [`00af2f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af2/00af2f48.md) → [`00af3370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af3/00af3370.md) FUN_00af3370

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a47d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a47d08.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a47f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47f00.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af2f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af2/00af2f48.md#insn-00af2f5c)
- 新版 `00af3384`（命令位置の公開資料なし）

~~~diff
- 00af2f5c ["INT_ADD", "register:40f0:8", ["const:af2f5c:8", "const:4:8"]]
- 00af2f5c ["CALL", null, ["callee:008514f8:8"]]
+ 00af3384 ["INT_ADD", "register:40f0:8", ["const:af3384:8", "const:4:8"]]
+ 00af3384 ["CALL", null, ["callee:008514f8:8"]]
- 00af2f5c bytes 5779f597
+ 00af3384 bytes 5d78f597
~~~


<a id="compare-67544b1b30a4c28fc3f9188a90563c0b"></a>

### [`00af3104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af3/00af3104.md) → [`00af352c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af3/00af352c.md) FUN_00af352c

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 1件 [`005fb8fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fb/005fb8fc.md) · 呼出先 1件 [`00af8d2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af8/00af8d2c.md)
- 新版 呼出元 1件 [`005fb93c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fb/005fb93c.md) · 呼出先 1件 [`00af9154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af9154.md)

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af3108",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00af9154"
      ]
    ]
  ],
  "added": [
    [
      "00af3530",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00af9154"
      ]
    ]
  ]
}
~~~


<a id="compare-45db4b8ae9ccdd46ea7224d10afffbd1"></a>

### [`00af3138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af3/00af3138.md) → [`00af3560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af3/00af3560.md) _INIT_250

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 54.80% / 新版 54.80%

CFGの説明率　旧版 84.85% / 新版 93.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_store_alignment` 39件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af3168"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af317c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af3180"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af3168",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af3174",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00af317c",
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
      "00af3590",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00af359c",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00af35a4",
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

- 旧版 [`00af3168`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af3/00af3138.md#insn-00af3168) · [`00af317c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af3/00af3138.md#insn-00af317c) · [`00af3180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af3/00af3138.md#insn-00af3180)

~~~diff
- 00af3168 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00af3168 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00af3168 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00af3168 bytes a9831ff8
- 00af317c ["COPY", "tmp:0:4", ["register:4050:4"]]
- 00af317c ["INT_ADD", "tmp:1:8", ["register:8:8", "const:21:8"]]
- 00af317c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 00af317c bytes ea130278
- 00af3180 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 00af3180 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00af3180 bytes e92b00b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0634d6c115b7ea630945e88e8b53d82"></a>

### [`00af3634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af3/00af3634.md) → [`00af3a5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af3/00af3a5c.md) FUN_00af3a5c

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 7件 [`005f3a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f3/005f3a30.md) [`005fb8fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fb/005fb8fc.md) [`00713318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00713/00713318.md) [`0071421c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00714/0071421c.md) [`00714ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00714/00714ba8.md) · 呼出先 3件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 7件 [`005f3a70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f3/005f3a70.md) [`005fb93c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fb/005fb93c.md) [`00713358`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00713/00713358.md) [`0071425c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00714/0071425c.md) [`00714be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00714/00714be8.md) · 呼出先 3件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 97.32% / 新版 97.32%

CFGの説明率　旧版 42.86% / 新版 56.25%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af37dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00af3c04"
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
      "00af3b68",
      "DATA",
      [
        "storage",
        "002bfb40",
        null,
        null
      ]
    ],
    [
      "00af3b68",
      "DATA",
      [
        "storage",
        "002bfb48",
        null,
        null
      ]
    ],
    [
      "00af3b9c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00af37e0"
      ]
    ]
  ],
  "added": [
    [
      "00af3b68",
      "DATA",
      [
        "storage",
        "002bfb40",
        null,
        "string"
      ]
    ],
    [
      "00af3b68",
      "DATA",
      [
        "storage",
        "002bfb48",
        null,
        "string"
      ]
    ],
    [
      "00af3b9c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00af3c08"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af37dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af3/00af3634.md#insn-00af37dc) · [`00af3654`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af3/00af3634.md#insn-00af3654)
- 新版 `00af3c04`（命令位置の公開資料なし） · `00af3a7c`（命令位置の公開資料なし）

~~~diff
- 00af37dc ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00af37dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00af37dc bytes 6002803d
+ 00af3c04 ["COPY", "tmp:0:8", ["register:4098:8"]]
+ 00af3c04 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
+ 00af3c04 bytes 6002803d
- 00af3654 ["INT_ADD", "register:40f0:8", ["const:af3654:8", "const:4:8"]]
- 00af3654 ["CALL", null, ["callee:008514f8:8"]]
+ 00af3a7c ["INT_ADD", "register:40f0:8", ["const:af3a7c:8", "const:4:8"]]
+ 00af3a7c ["CALL", null, ["callee:008514f8:8"]]
- 00af3654 bytes 9977f597
+ 00af3a7c bytes 9f76f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50bdff70582d3e423a04126c44682672"></a>

### [`00af3834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af3/00af3834.md) → [`00af3c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af3/00af3c5c.md) FUN_00af3c5c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 9件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`006bbc58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bb/006bbc58.md) [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) [`007154c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00715/007154c0.md) [`00716a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00716/00716a50.md) · 呼出先 5件 [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 9件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`006bbc98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006bb/006bbc98.md) [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) [`00715500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00715/00715500.md) [`00716a90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00716/00716a90.md) · 呼出先 5件 [`0046d7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7b0.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, call, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 47.83% / 新版 61.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af3834"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af3834"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af3838"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af3834",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af3838",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af383c",
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
      "00af3c5c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00af3c60",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af3c64",
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

- 旧版 [`00af3834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af3/00af3834.md#insn-00af3834) · [`00af3838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af3/00af3834.md#insn-00af3838) · [`00af383c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af3/00af3834.md#insn-00af383c)

~~~diff
- 00af3834 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af3834 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af3834 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00af3834 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af3834 bytes fd7bbda9
- 00af3838 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00af3838 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00af3838 bytes f50b00f9
- 00af383c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af383c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af383c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00af383c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af383c bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b67db067d29f21627929caddb1f1a603"></a>

### [`00af3e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af3/00af3e2c.md) → [`00af4254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af4/00af4254.md) FUN_00af4254

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 5件 [`005fdc18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fd/005fdc18.md) [`00716b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00716/00716b40.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00a51dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a51/00a51dcc.md) [`00af2468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af2/00af2468.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 5件 [`005fdc58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fd/005fdc58.md) [`00716b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00716/00716b80.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00a51fc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a51/00a51fc4.md) [`00af2890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af2/00af2890.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af3e48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af3/00af3e2c.md#insn-00af3e48)
- 新版 `00af4270`（命令位置の公開資料なし）

~~~diff
- 00af3e48 ["INT_ADD", "register:40f0:8", ["const:af3e48:8", "const:4:8"]]
- 00af3e48 ["CALL", null, ["callee:008514f8:8"]]
+ 00af4270 ["INT_ADD", "register:40f0:8", ["const:af4270:8", "const:4:8"]]
+ 00af4270 ["CALL", null, ["callee:008514f8:8"]]
- 00af3e48 bytes 9c75f597
+ 00af4270 bytes a274f597
~~~


<a id="compare-55c83ff1cc6eefab903575b2c80773a3"></a>

### [`00af3e78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af3/00af3e78.md) → [`00af42a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af4/00af42a0.md) FUN_00af42a0

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`007154c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00715/007154c0.md) [`00716d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00716/00716d50.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 2件 [`00715500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00715/00715500.md) [`00716d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00716/00716d90.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af3e94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af3/00af3e78.md#insn-00af3e94)
- 新版 `00af42bc`（命令位置の公開資料なし）

~~~diff
- 00af3e94 ["INT_ADD", "register:40f0:8", ["const:af3e94:8", "const:4:8"]]
- 00af3e94 ["CALL", null, ["callee:008514f8:8"]]
+ 00af42bc ["INT_ADD", "register:40f0:8", ["const:af42bc:8", "const:4:8"]]
+ 00af42bc ["CALL", null, ["callee:008514f8:8"]]
- 00af3e94 bytes 8975f597
+ 00af42bc bytes 8f74f597
~~~


<a id="compare-d0abc833c242c4562182c6a35920911b"></a>

### [`00af3ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af3/00af3ecc.md) → [`00af42f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af4/00af42f4.md) FUN_00af42f4

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00af4220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af4/00af4220.md) [`00af42cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af4/00af42cc.md) · 呼出先 12件 [`0046e6ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e6ec.md) [`0046e76c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e76c.md) [`0046e774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e774.md) [`0046e77c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e77c.md) [`004700ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/004700ec.md)
- 新版 呼出元 2件 [`00af4648`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af4/00af4648.md) [`00af46f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af4/00af46f4.md) · 呼出先 12件 [`0046e72c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e72c.md) [`0046e7ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e7ac.md) [`0046e7b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e7b4.md) [`0046e7bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e7bc.md) [`0047012c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/0047012c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 96.22% / 新版 96.22%

CFGの説明率　旧版 62.50% / 新版 83.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 3件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00af4374",
      "value": [
        "leaf",
        "ram:46e7ac:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00af3f4c",
      "value": [
        "leaf",
        "ram:46e76c:8"
      ]
    },
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00af43a8",
      "value": [
        "leaf",
        "ram:46e7b4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00af3f80",
      "value": [
        "leaf",
        "ram:46e774:8"
      ]
    },
    "ordinal": 9,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00af43c8",
      "value": [
        "leaf",
        "ram:46e7bc:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00af3fa0",
      "value": [
        "leaf",
        "ram:46e77c:8"
      ]
    },
    "ordinal": 12,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00af4374",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046e76c"
      ]
    ],
    [
      "00af43a8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046e774"
      ]
    ],
    [
      "00af43c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046e77c"
      ]
    ]
  ],
  "added": [
    [
      "00af4374",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046e7ac"
      ]
    ],
    [
      "00af43a8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046e7b4"
      ]
    ],
    [
      "00af43c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046e7bc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af3f4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af3/00af3ecc.md#insn-00af3f4c) · [`00af3f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af3/00af3ecc.md#insn-00af3f80) · [`00af3fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af3/00af3ecc.md#insn-00af3fa0)
- 新版 `00af4374`（命令位置の公開資料なし） · `00af43a8`（命令位置の公開資料なし） · `00af43c8`（命令位置の公開資料なし）

~~~diff
- 00af3f4c ["INT_ADD", "register:40f0:8", ["const:af3f4c:8", "const:4:8"]]
- 00af3f4c ["CALL", null, ["ram:46e76c:8"]]
+ 00af4374 ["INT_ADD", "register:40f0:8", ["const:af4374:8", "const:4:8"]]
+ 00af4374 ["CALL", null, ["ram:46e7ac:8"]]
- 00af3f4c bytes 08eae597
+ 00af4374 bytes 0ee9e597
- 00af3f80 ["INT_ADD", "register:40f0:8", ["const:af3f80:8", "const:4:8"]]
- 00af3f80 ["CALL", null, ["ram:46e774:8"]]
+ 00af43a8 ["INT_ADD", "register:40f0:8", ["const:af43a8:8", "const:4:8"]]
+ 00af43a8 ["CALL", null, ["ram:46e7b4:8"]]
- 00af3f80 bytes fde9e597
+ 00af43a8 bytes 03e9e597
- 00af3fa0 ["INT_ADD", "register:40f0:8", ["const:af3fa0:8", "const:4:8"]]
- 00af3fa0 ["CALL", null, ["ram:46e77c:8"]]
+ 00af43c8 ["INT_ADD", "register:40f0:8", ["const:af43c8:8", "const:4:8"]]
+ 00af43c8 ["CALL", null, ["ram:46e7bc:8"]]
- 00af3fa0 bytes f7e9e597
+ 00af43c8 bytes fde8e597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0559112edd771afc815d443f25f563d"></a>

### [`00af41b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af4/00af41b0.md) → [`00af45d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af4/00af45d8.md) FUN_00af45d8

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`005e0960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0960.md) [`0061037c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00610/0061037c.md) [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) [`00707ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 2件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 5件 [`005e09a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e09a0.md) [`006103bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00610/006103bc.md) [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) [`00707ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707ee0.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af45fc",
      "incomplete_value": true,
      "site": "00af4600",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "live",
            "register:4048:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af41d4",
      "incomplete_value": true,
      "site": "00af41d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              [
                "live",
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2768:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00af421c"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00af4644"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00af41d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af4/00af41b0.md#insn-00af41d8) · [`00af421c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af4/00af41b0.md#insn-00af421c)
- 新版 `00af4600`（命令位置の公開資料なし） · `00af4644`（命令位置の公開資料なし）

~~~diff
- 00af41d8 ["INT_ADD", "register:40f0:8", ["const:af41d8:8", "const:4:8"]]
- 00af41d8 ["CALL", null, ["callee:005e7420:8"]]
+ 00af4600 ["INT_ADD", "register:40f0:8", ["const:af4600:8", "const:4:8"]]
+ 00af4600 ["CALL", null, ["callee:005e7420:8"]]
- 00af41d8 bytes 82cceb97
+ 00af4600 bytes 88cbeb97
- 00af421c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00af421c ["RETURN", null, ["register:0:8"]]
- 00af421c bytes c0035fd6
+ 00af4644 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00af4644 ["RETURN", null, ["register:0:8"]]
+ 00af4644 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-181262ec18f27af7e77c8708d13fbf69"></a>

### [`00af43f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af4/00af43f4.md) → [`00af481c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af4/00af481c.md) FUN_00af481c

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00af247c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af2/00af247c.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 2件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00af28a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af2/00af28a4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af4410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af4/00af43f4.md#insn-00af4410)
- 新版 `00af4838`（命令位置の公開資料なし）

~~~diff
- 00af4410 ["INT_ADD", "register:40f0:8", ["const:af4410:8", "const:4:8"]]
- 00af4410 ["CALL", null, ["callee:008514f8:8"]]
+ 00af4838 ["INT_ADD", "register:40f0:8", ["const:af4838:8", "const:4:8"]]
+ 00af4838 ["CALL", null, ["callee:008514f8:8"]]
- 00af4410 bytes 2a74f597
+ 00af4838 bytes 3073f597
~~~


<a id="compare-b2a7f5619c94517e8a1419b1c1d0d9ef"></a>

### [`00af4480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af4/00af4480.md) → [`00af48a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af4/00af48a8.md) FUN_00af48a8

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 2件 [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af449c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af4/00af4480.md#insn-00af449c)
- 新版 `00af48c4`（命令位置の公開資料なし）

~~~diff
- 00af449c ["INT_ADD", "register:40f0:8", ["const:af449c:8", "const:4:8"]]
- 00af449c ["CALL", null, ["callee:008514f8:8"]]
+ 00af48c4 ["INT_ADD", "register:40f0:8", ["const:af48c4:8", "const:4:8"]]
+ 00af48c4 ["CALL", null, ["callee:008514f8:8"]]
- 00af449c bytes 0774f597
+ 00af48c4 bytes 0d73f597
~~~


<a id="compare-f3abb0b6f2351eae74544f53f7cd3479"></a>

### [`00af48f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af4/00af48f8.md) → [`00af4d20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af4/00af4d20.md) FUN_00af4d20

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00a51dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a51/00a51dcc.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 2件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00a51fc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a51/00a51fc4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af4914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af4/00af48f8.md#insn-00af4914)
- 新版 `00af4d3c`（命令位置の公開資料なし）

~~~diff
- 00af4914 ["INT_ADD", "register:40f0:8", ["const:af4914:8", "const:4:8"]]
- 00af4914 ["CALL", null, ["callee:008514f8:8"]]
+ 00af4d3c ["INT_ADD", "register:40f0:8", ["const:af4d3c:8", "const:4:8"]]
+ 00af4d3c ["CALL", null, ["callee:008514f8:8"]]
- 00af4914 bytes e972f597
+ 00af4d3c bytes ef71f597
~~~


<a id="compare-e20ce2959d53f6b3cd00400c6c4ae746"></a>

### [`00af4a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af4/00af4a24.md) → [`00af4e4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af4/00af4e4c.md) FUN_00af4e4c

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af4a40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af4/00af4a24.md#insn-00af4a40)
- 新版 `00af4e68`（命令位置の公開資料なし）

~~~diff
- 00af4a40 ["INT_ADD", "register:40f0:8", ["const:af4a40:8", "const:4:8"]]
- 00af4a40 ["CALL", null, ["callee:008514f8:8"]]
+ 00af4e68 ["INT_ADD", "register:40f0:8", ["const:af4e68:8", "const:4:8"]]
+ 00af4e68 ["CALL", null, ["callee:008514f8:8"]]
- 00af4a40 bytes 9e72f597
+ 00af4e68 bytes a471f597
~~~


<a id="compare-99134efd3d6c525bb9baa5a7128624d5"></a>

### [`00af4b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af4/00af4b90.md) → [`00af4fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af4/00af4fb8.md) FUN_00af4fb8

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00a519e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a51/00a519e0.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 2件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00a51bd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a51/00a51bd8.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af4ba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af4/00af4b90.md#insn-00af4ba4)
- 新版 `00af4fcc`（命令位置の公開資料なし）

~~~diff
- 00af4ba4 ["INT_ADD", "register:40f0:8", ["const:af4ba4:8", "const:4:8"]]
- 00af4ba4 ["CALL", null, ["callee:008514f8:8"]]
+ 00af4fcc ["INT_ADD", "register:40f0:8", ["const:af4fcc:8", "const:4:8"]]
+ 00af4fcc ["CALL", null, ["callee:008514f8:8"]]
- 00af4ba4 bytes 4572f597
+ 00af4fcc bytes 4b71f597
~~~


<a id="compare-45733c6f5735e88f05c0d7e82a60c6ac"></a>

### [`00af4c6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af4/00af4c6c.md) → [`00af5094`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af5/00af5094.md) FUN_00af5094

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af4c88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af4/00af4c6c.md#insn-00af4c88)
- 新版 `00af50b0`（命令位置の公開資料なし）

~~~diff
- 00af4c88 ["INT_ADD", "register:40f0:8", ["const:af4c88:8", "const:4:8"]]
- 00af4c88 ["CALL", null, ["callee:008514f8:8"]]
+ 00af50b0 ["INT_ADD", "register:40f0:8", ["const:af50b0:8", "const:4:8"]]
+ 00af50b0 ["CALL", null, ["callee:008514f8:8"]]
- 00af4c88 bytes 0c72f597
+ 00af50b0 bytes 1271f597
~~~


<a id="compare-3473ecffbc86ec5f771e8f34d79ce14b"></a>

### [`00af4cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af4/00af4cb8.md) → [`00af50e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af5/00af50e0.md) FUN_00af50e0

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`0070ea1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070ea1c.md) [`00716d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00716/00716d50.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 2件 [`0070ea5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070ea5c.md) [`00716d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00716/00716d90.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": null,
    "old": {
      "definition_site": "00af4ce8",
      "incomplete_value": true,
      "site": "00af4cf4",
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
    "ordinal": 0,
    "slot": 0
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00af4ccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af4/00af4cb8.md#insn-00af4ccc)
- 新版 `00af50f4`（命令位置の公開資料なし）

~~~diff
- 00af4ccc ["INT_ADD", "register:40f0:8", ["const:af4ccc:8", "const:4:8"]]
- 00af4ccc ["CALL", null, ["callee:008514f8:8"]]
+ 00af50f4 ["INT_ADD", "register:40f0:8", ["const:af50f4:8", "const:4:8"]]
+ 00af50f4 ["CALL", null, ["callee:008514f8:8"]]
- 00af4ccc bytes fb71f597
+ 00af50f4 bytes 0171f597
~~~


<a id="compare-af5d71def38277970245eb2767e7c0c5"></a>

### [`00af5028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af5028.md) → [`00af5450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af5/00af5450.md) FUN_00af5450

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0070ea1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070ea1c.md) [`007119b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00711/007119b0.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 2件 [`0070ea5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070ea5c.md) [`007119f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00711/007119f0.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, return_value_candidate

命令の説明率　旧版 65.22% / 新版 65.22%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00af5498",
      "incomplete_value": true,
      "site": "00af54a8",
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
    "old": {
      "definition_site": "00af5070",
      "incomplete_value": true,
      "site": "00af5080",
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
      "unmatched:00af5060",
      "DATA",
      [
        "storage",
        "0030a328",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00af5488",
      "DATA",
      [
        "storage",
        "0030a368",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af5044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af5028.md#insn-00af5044) · [`00af5054`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af5028.md#insn-00af5054) · [`00af5058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af5028.md#insn-00af5058)
- 新版 `00af546c`（命令位置の公開資料なし）

~~~diff
- 00af5044 ["INT_ADD", "register:40f0:8", ["const:af5044:8", "const:4:8"]]
- 00af5044 ["CALL", null, ["callee:008514f8:8"]]
+ 00af546c ["INT_ADD", "register:40f0:8", ["const:af546c:8", "const:4:8"]]
+ 00af546c ["CALL", null, ["callee:008514f8:8"]]
- 00af5044 bytes 1d71f597
+ 00af546c bytes 2370f597
- 00af5054 ["INT_SEXT", "tmp:0:8", ["register:40a0:4"]]
- 00af5054 ["INT_SEXT", "tmp:1:8", ["register:4048:4"]]
- 00af5054 ["INT_MULT", "tmp:2:8", ["tmp:0:8", "tmp:1:8"]]
- 00af5054 ["INT_ADD", "register:4040:8", ["register:4040:8", "tmp:2:8"]]
- 00af5054 bytes 8822299b
- 00af5058 ["COPY", "register:4048:8", ["const:30a000:8"]]
- 00af5058 bytes a9c0ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b55847a80e13f64f4a68ace29f9c37e5"></a>

### [`00af5190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af5190.md) → [`00af55b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af5/00af55b8.md) FUN_00af55b8

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, return_value_candidate

命令の説明率　旧版 73.91% / 新版 73.91%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00af5600",
      "incomplete_value": true,
      "site": "00af5610",
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
      "unmatched:00af51c8",
      "DATA",
      [
        "storage",
        "0030a334",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00af55f0",
      "DATA",
      [
        "storage",
        "0030a374",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af51ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af5190.md#insn-00af51ac) · [`00af51c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af5190.md#insn-00af51c4) · [`00af51c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af5190.md#insn-00af51c8)
- 新版 `00af55d4`（命令位置の公開資料なし）

~~~diff
- 00af51ac ["INT_ADD", "register:40f0:8", ["const:af51ac:8", "const:4:8"]]
- 00af51ac ["CALL", null, ["callee:008514f8:8"]]
+ 00af55d4 ["INT_ADD", "register:40f0:8", ["const:af55d4:8", "const:4:8"]]
+ 00af55d4 ["CALL", null, ["callee:008514f8:8"]]
- 00af51ac bytes c370f597
+ 00af55d4 bytes c96ff597
- 00af51c4 ["COPY", "tmp:0:8", ["const:334:8"]]
- 00af51c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00af51c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00af51c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00af51c4 bytes 29d10c91
- 00af51c8 ["INT_SEXT", "tmp:0:8", ["register:4098:4"]]
- 00af51c8 ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 00af51c8 ["INT_LEFT", "tmp:1:8", ["tmp:1:8", "const:2:8"]]
- 00af51c8 ["INT_ADD", "tmp:2:8", ["register:4048:8", "tmp:1:8"]]
- 00af51c8 bytes 29d9b3b8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc3c388c8236b391606bb89c53ec04fe"></a>

### [`00af5278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af5278.md) → [`00af56a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af5/00af56a0.md) FUN_00af56a0

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a51dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a51/00a51dcc.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a51fc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a51/00a51fc4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af528c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af5278.md#insn-00af528c)
- 新版 `00af56b4`（命令位置の公開資料なし）

~~~diff
- 00af528c ["INT_ADD", "register:40f0:8", ["const:af528c:8", "const:4:8"]]
- 00af528c ["CALL", null, ["callee:008514f8:8"]]
+ 00af56b4 ["INT_ADD", "register:40f0:8", ["const:af56b4:8", "const:4:8"]]
+ 00af56b4 ["CALL", null, ["callee:008514f8:8"]]
- 00af528c bytes 8b70f597
+ 00af56b4 bytes 916ff597
~~~


<a id="compare-3f36326fe078676a7a1191aea5120a74"></a>

### [`00af5390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af5390.md) → [`00af57b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af5/00af57b8.md) FUN_00af57b8

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00af27c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af2/00af27c4.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 2件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00af2bec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af2/00af2bec.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af53ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af5390.md#insn-00af53ac)
- 新版 `00af57d4`（命令位置の公開資料なし）

~~~diff
- 00af53ac ["INT_ADD", "register:40f0:8", ["const:af53ac:8", "const:4:8"]]
- 00af53ac ["CALL", null, ["callee:008514f8:8"]]
+ 00af57d4 ["INT_ADD", "register:40f0:8", ["const:af57d4:8", "const:4:8"]]
+ 00af57d4 ["CALL", null, ["callee:008514f8:8"]]
- 00af53ac bytes 4370f597
+ 00af57d4 bytes 496ff597
~~~


<a id="compare-db9f80a26d34a065f542c02c895db536"></a>

### [`00af53dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af53dc.md) → [`00af5804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af5/00af5804.md) FUN_00af5804

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af5850",
      "incomplete_value": true,
      "site": "00af5850",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              "INT_LEFT"
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_ZEXT",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af5428",
      "incomplete_value": true,
      "site": "00af5428",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              "INT_LEFT"
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_ZEXT",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00af5840",
      "DATA",
      [
        "storage",
        "0030a334",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00af5840",
      "DATA",
      [
        "storage",
        "0030a374",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af53fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af53dc.md#insn-00af53fc) · [`00af5414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af53dc.md#insn-00af5414)
- 新版 `00af5824`（命令位置の公開資料なし） · `00af583c`（命令位置の公開資料なし）

~~~diff
- 00af53fc ["INT_ADD", "register:40f0:8", ["const:af53fc:8", "const:4:8"]]
- 00af53fc ["CALL", null, ["callee:008514f8:8"]]
+ 00af5824 ["INT_ADD", "register:40f0:8", ["const:af5824:8", "const:4:8"]]
+ 00af5824 ["CALL", null, ["callee:008514f8:8"]]
- 00af53fc bytes 2f70f597
+ 00af5824 bytes 356ff597
- 00af5414 ["COPY", "tmp:0:8", ["const:334:8"]]
- 00af5414 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00af5414 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00af5414 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00af583c ["COPY", "tmp:0:8", ["const:374:8"]]
+ 00af583c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00af583c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00af583c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00af5414 bytes 29d10c91
+ 00af583c bytes 29d10d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d831e94031b6b6dceef1b8d203f17311"></a>

### [`00af54c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af54c8.md) → [`00af58f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af5/00af58f0.md) FUN_00af58f0

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00713318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00713/00713318.md) [`00713ce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00713/00713ce4.md) [`0071421c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00714/0071421c.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 3件 [`00713358`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00713/00713358.md) [`00713d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00713/00713d24.md) [`0071425c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00714/0071425c.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, return_value_candidate

命令の説明率　旧版 76.00% / 新版 76.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00af5940",
      "incomplete_value": true,
      "site": "00af5950",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "BOOL_NEGATE",
            "1",
            [
              "INT_EQUAL"
            ]
          ]
        ]
      ]
    },
    "old": null,
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
      "unmatched:00af5500",
      "DATA",
      [
        "storage",
        "0030a340",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00af5928",
      "DATA",
      [
        "storage",
        "0030a380",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af54e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af54c8.md#insn-00af54e4) · [`00af54fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af54c8.md#insn-00af54fc) · [`00af5500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af54c8.md#insn-00af5500)
- 新版 `00af590c`（命令位置の公開資料なし）

~~~diff
- 00af54e4 ["INT_ADD", "register:40f0:8", ["const:af54e4:8", "const:4:8"]]
- 00af54e4 ["CALL", null, ["callee:008514f8:8"]]
+ 00af590c ["INT_ADD", "register:40f0:8", ["const:af590c:8", "const:4:8"]]
+ 00af590c ["CALL", null, ["callee:008514f8:8"]]
- 00af54e4 bytes f56ff597
+ 00af590c bytes fb6ef597
- 00af54fc ["COPY", "tmp:0:8", ["const:340:8"]]
- 00af54fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00af54fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00af54fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00af54fc bytes 29010d91
- 00af5500 ["INT_SEXT", "tmp:0:8", ["register:4098:4"]]
- 00af5500 ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 00af5500 ["INT_LEFT", "tmp:1:8", ["tmp:1:8", "const:2:8"]]
- 00af5500 ["INT_ADD", "tmp:2:8", ["register:4048:8", "tmp:1:8"]]
- 00af5500 bytes 29d9b3b8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2375622fb87185d2e2063592957cb01"></a>

### [`00af552c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af552c.md) → [`00af5954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af5/00af5954.md) FUN_00af5954

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af59a0",
      "incomplete_value": true,
      "site": "00af59a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              "INT_LEFT"
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_ZEXT",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af5578",
      "incomplete_value": true,
      "site": "00af5578",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              "INT_LEFT"
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_ZEXT",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00af5990",
      "DATA",
      [
        "storage",
        "0030a340",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00af5990",
      "DATA",
      [
        "storage",
        "0030a380",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af554c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af552c.md#insn-00af554c) · [`00af5564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af552c.md#insn-00af5564)
- 新版 `00af5974`（命令位置の公開資料なし） · `00af598c`（命令位置の公開資料なし）

~~~diff
- 00af554c ["INT_ADD", "register:40f0:8", ["const:af554c:8", "const:4:8"]]
- 00af554c ["CALL", null, ["callee:008514f8:8"]]
+ 00af5974 ["INT_ADD", "register:40f0:8", ["const:af5974:8", "const:4:8"]]
+ 00af5974 ["CALL", null, ["callee:008514f8:8"]]
- 00af554c bytes db6ff597
+ 00af5974 bytes e16ef597
- 00af5564 ["COPY", "tmp:0:8", ["const:340:8"]]
- 00af5564 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00af5564 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00af5564 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00af598c ["COPY", "tmp:0:8", ["const:380:8"]]
+ 00af598c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00af598c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00af598c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00af5564 bytes 29010d91
+ 00af598c bytes 29010e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b94de9f7683e84795bb69338b9de80e2"></a>

### [`00af55cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af55cc.md) → [`00af59f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af5/00af59f4.md) FUN_00af59f4

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 3件 [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) [`007154c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00715/007154c0.md) [`00716d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00716/00716d50.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 3件 [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) [`00715500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00715/00715500.md) [`00716d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00716/00716d90.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af55e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af55cc.md#insn-00af55e8)
- 新版 `00af5a10`（命令位置の公開資料なし）

~~~diff
- 00af55e8 ["INT_ADD", "register:40f0:8", ["const:af55e8:8", "const:4:8"]]
- 00af55e8 ["CALL", null, ["callee:008514f8:8"]]
+ 00af5a10 ["INT_ADD", "register:40f0:8", ["const:af5a10:8", "const:4:8"]]
+ 00af5a10 ["CALL", null, ["callee:008514f8:8"]]
- 00af55e8 bytes b46ff597
+ 00af5a10 bytes ba6ef597
~~~


<a id="compare-df073a85ae794332e12322d6947c3005"></a>

### [`00af566c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af566c.md) → [`00af5a94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af5/00af5a94.md) FUN_00af5a94

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`0070ea1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070ea1c.md) [`00710298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00710/00710298.md) [`007119b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00711/007119b0.md) · 呼出先 17件 [`0046da7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046da7c.md) [`005e0eac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0eac.md) [`005e1af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e1af0.md) [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 3件 [`0070ea5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070ea5c.md) [`007102d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00710/007102d8.md) [`007119f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00711/007119f0.md) · 呼出先 17件 [`0046dabc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046dabc.md) [`005e0eec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e0eec.md) [`005e1b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e1/005e1b30.md) [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.64% / 新版 97.64%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af5b8c",
      "incomplete_value": true,
      "site": "00af5ba4",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:4098:4"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 9,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af5b90",
      "incomplete_value": true,
      "site": "00af5ba4",
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
    "old": null,
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af5b98",
      "incomplete_value": true,
      "site": "00af5ba4",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:40a8:4"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 9,
    "slot": 3
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00af577c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af566c.md#insn-00af577c) · [`00af57b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af566c.md#insn-00af57b0) · [`00af5820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af566c.md#insn-00af5820)
- 新版 `00af5ba4`（命令位置の公開資料なし） · `00af5bd8`（命令位置の公開資料なし） · `00af5c48`（命令位置の公開資料なし）

~~~diff
- 00af577c ["INT_ADD", "register:40f0:8", ["const:af577c:8", "const:4:8"]]
- 00af577c ["CALL", null, ["callee:00b03224:8"]]
+ 00af5ba4 ["INT_ADD", "register:40f0:8", ["const:af5ba4:8", "const:4:8"]]
+ 00af5ba4 ["CALL", null, ["callee:00b03224:8"]]
- 00af577c bytes a0350094
+ 00af5ba4 bytes a0350094
- 00af57b0 ["INT_ADD", "register:40f0:8", ["const:af57b0:8", "const:4:8"]]
- 00af57b0 ["CALL", null, ["callee:00aff2cc:8"]]
+ 00af5bd8 ["INT_ADD", "register:40f0:8", ["const:af5bd8:8", "const:4:8"]]
+ 00af5bd8 ["CALL", null, ["callee:00aff2cc:8"]]
- 00af57b0 bytes bd250094
+ 00af5bd8 bytes bd250094
- 00af5820 ["INT_ADD", "register:40f0:8", ["const:af5820:8", "const:4:8"]]
- 00af5820 ["CALL", null, ["callee:00b03154:8"]]
+ 00af5c48 ["INT_ADD", "register:40f0:8", ["const:af5c48:8", "const:4:8"]]
+ 00af5c48 ["CALL", null, ["callee:00b03154:8"]]
- 00af5820 bytes 43350094
+ 00af5c48 bytes 43350094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-115944133d1ddd6d8e60b14e57ead501"></a>

### [`00af5868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af5868.md) → [`00af5c90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af5/00af5c90.md) FUN_00af5c90

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`005fb8fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fb/005fb8fc.md) [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) [`0070ea1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070ea1c.md) [`007119b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00711/007119b0.md) · 呼出先 4件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00af6708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6708.md) [`00af6778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6778.md)
- 新版 呼出元 4件 [`005fb93c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fb/005fb93c.md) [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) [`0070ea5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070ea5c.md) [`007119f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00711/007119f0.md) · 呼出先 4件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00af6b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6b30.md) [`00af6ba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6ba0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 55.42% / 新版 55.42%

CFGの説明率　旧版 13.45% / 新版 11.76%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 26件, `unresolved_call_alignment` 38件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af590c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af598c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af59b0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af5908",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "005e7420"
      ]
    ],
    [
      "unmatched:00af590c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af5d9c"
      ]
    ],
    [
      "unmatched:00af5910",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514f8"
      ]
    ]
  ],
  "added": [
    [
      "00af5d30",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "005e7420"
      ]
    ],
    [
      "00af5d34",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af5d9c"
      ]
    ],
    [
      "00af5d38",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514f8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af590c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af5868.md#insn-00af590c) · [`00af598c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af5868.md#insn-00af598c) · [`00af59b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af5868.md#insn-00af59b0)

~~~diff
- 00af590c ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 00af590c ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00af590c ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00af590c ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 00af590c bytes 40030036
- 00af598c ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 00af598c ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00af598c ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00af598c ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 00af598c bytes 80030036
- 00af59b0 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 00af59b0 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 00af59b0 bytes 68020034
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-475845948b3fa4f7eb3b5267011d3c9a"></a>

### [`00af5f88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af5f88.md) → [`00af63b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af63b0.md) FUN_00af63b0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00710090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00710/00710090.md) · 呼出先 2件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`007100d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00710/007100d0.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

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
      "site": "00af5f88"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5f88"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5f8c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af5f88",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af5f8c",
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
      "00af63b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af63b4",
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

- 旧版 [`00af5f88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af5f88.md#insn-00af5f88) · [`00af5f8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af5f88.md#insn-00af5f8c) · [`00af5fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af5f88.md#insn-00af5fb0)
- 新版 `00af63d8`（命令位置の公開資料なし）

~~~diff
- 00af5f88 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af5f88 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af5f88 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00af5f88 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af5f88 bytes fd7bbea9
- 00af5f8c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af5f8c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af5f8c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00af5f8c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af5f8c bytes f44f01a9
- 00af5fb0 ["INT_ADD", "register:40f0:8", ["const:af5fb0:8", "const:4:8"]]
- 00af5fb0 ["CALL", null, ["callee:005e7420:8"]]
+ 00af63d8 ["INT_ADD", "register:40f0:8", ["const:af63d8:8", "const:4:8"]]
+ 00af63d8 ["CALL", null, ["callee:005e7420:8"]]
- 00af5fb0 bytes 0cc5eb97
+ 00af63d8 bytes 12c4eb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c1fd1cb86d0117c626393534036589f"></a>

### [`00af5ff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af5ff8.md) → [`00af6420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6420.md) FUN_00af6420

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`0070ea1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070ea1c.md) [`00710090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00710/00710090.md) [`007119b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00711/007119b0.md) [`00716d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00716/00716d50.md) · 呼出先 2件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 4件 [`0070ea5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070ea5c.md) [`007100d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00710/007100d0.md) [`007119f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00711/007119f0.md) [`00716d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00716/00716d90.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 9.09% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5ff8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5ff8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5ffc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af5ff8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af5ffc",
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
      "00af6420",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af6424",
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

- 旧版 [`00af5ff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af5ff8.md#insn-00af5ff8) · [`00af5ffc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af5ff8.md#insn-00af5ffc) · [`00af6020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af5ff8.md#insn-00af6020)
- 新版 `00af6448`（命令位置の公開資料なし）

~~~diff
- 00af5ff8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af5ff8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af5ff8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00af5ff8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af5ff8 bytes fd7bbea9
- 00af5ffc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af5ffc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af5ffc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00af5ffc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af5ffc bytes f44f01a9
- 00af6020 ["INT_ADD", "register:40f0:8", ["const:af6020:8", "const:4:8"]]
- 00af6020 ["CALL", null, ["callee:005e7420:8"]]
+ 00af6448 ["INT_ADD", "register:40f0:8", ["const:af6448:8", "const:4:8"]]
+ 00af6448 ["CALL", null, ["callee:005e7420:8"]]
- 00af6020 bytes f0c4eb97
+ 00af6448 bytes f6c3eb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aef366a2e9fdab397647189814b8fb89"></a>

### [`00af60d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af60d8.md) → [`00af6500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6500.md) FUN_00af6500

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`0070ea1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070ea1c.md) [`00710090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00710/00710090.md) [`007119b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00711/007119b0.md) [`00716d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00716/00716d50.md) · 呼出先 2件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 4件 [`0070ea5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070ea5c.md) [`007100d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00710/007100d0.md) [`007119f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00711/007119f0.md) [`00716d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00716/00716d90.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 14.29% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af60d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af60d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af60dc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af60d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af60dc",
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
      "00af6500",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af6504",
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

- 旧版 [`00af60d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af60d8.md#insn-00af60d8) · [`00af60dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af60d8.md#insn-00af60dc) · [`00af6100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af60d8.md#insn-00af6100)
- 新版 `00af6528`（命令位置の公開資料なし）

~~~diff
- 00af60d8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af60d8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af60d8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00af60d8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af60d8 bytes fd7bbea9
- 00af60dc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af60dc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af60dc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00af60dc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af60dc bytes f44f01a9
- 00af6100 ["INT_ADD", "register:40f0:8", ["const:af6100:8", "const:4:8"]]
- 00af6100 ["CALL", null, ["callee:005e7420:8"]]
+ 00af6528 ["INT_ADD", "register:40f0:8", ["const:af6528:8", "const:4:8"]]
+ 00af6528 ["CALL", null, ["callee:005e7420:8"]]
- 00af6100 bytes b8c4eb97
+ 00af6528 bytes bec3eb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4bfea4f9aeda446df0aedfc9728c19f3"></a>

### [`00af6148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6148.md) → [`00af6570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6570.md) FUN_00af6570

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00710090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00710/00710090.md) · 呼出先 2件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`007100d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00710/007100d0.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.43% / 新版 96.43%

CFGの説明率　旧版 50.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af6594",
      "incomplete_value": true,
      "site": "00af6598",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              [
                "live",
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "live",
            "register:4048:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af616c",
      "incomplete_value": true,
      "site": "00af6170",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              [
                "live",
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2768:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00af6170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6148.md#insn-00af6170) · [`00af615c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6148.md#insn-00af615c) · [`00af616c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6148.md#insn-00af616c)
- 新版 `00af6598`（命令位置の公開資料なし） · `00af6584`（命令位置の公開資料なし）

~~~diff
- 00af6170 ["INT_ADD", "register:40f0:8", ["const:af6170:8", "const:4:8"]]
- 00af6170 ["CALL", null, ["callee:005e7420:8"]]
+ 00af6598 ["INT_ADD", "register:40f0:8", ["const:af6598:8", "const:4:8"]]
+ 00af6598 ["CALL", null, ["callee:005e7420:8"]]
- 00af6170 bytes 9cc4eb97
+ 00af6598 bytes a2c3eb97
- 00af615c ["INT_ADD", "register:40f0:8", ["const:af615c:8", "const:4:8"]]
- 00af615c ["CALL", null, ["callee:008514f8:8"]]
+ 00af6584 ["INT_ADD", "register:40f0:8", ["const:af6584:8", "const:4:8"]]
+ 00af6584 ["CALL", null, ["callee:008514f8:8"]]
- 00af615c bytes d76cf597
+ 00af6584 bytes dd6bf597
- 00af616c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00af616c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00af616c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00af616c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00af616c bytes 0001098b
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d4cbe4cceced73e2e112ae667cec186"></a>

### [`00af6298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6298.md) → [`00af66c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af66c0.md) FUN_00af66c0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 6件 [`005f3a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f3/005f3a30.md) [`005fb8fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fb/005fb8fc.md) [`0070ea1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070ea1c.md) [`00710090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00710/00710090.md) [`007119b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00711/007119b0.md) · 呼出先 2件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 6件 [`005f3a70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f3/005f3a70.md) [`005fb93c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fb/005fb93c.md) [`0070ea5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070ea5c.md) [`007100d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00710/007100d0.md) [`007119f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00711/007119f0.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00af672c",
      "incomplete_value": true,
      "site": "00af673c",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "BOOL_NEGATE",
            "1",
            [
              "INT_EQUAL"
            ]
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 0,
    "slot": 0
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00af62b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6298.md#insn-00af62b0) · [`00af62c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6298.md#insn-00af62c4) · [`00af62cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6298.md#insn-00af62cc)
- 新版 `00af66d8`（命令位置の公開資料なし） · `00af66ec`（命令位置の公開資料なし） · `00af66f4`（命令位置の公開資料なし）

~~~diff
- 00af62b0 ["INT_ADD", "register:40f0:8", ["const:af62b0:8", "const:4:8"]]
- 00af62b0 ["CALL", null, ["callee:008514f8:8"]]
+ 00af66d8 ["INT_ADD", "register:40f0:8", ["const:af66d8:8", "const:4:8"]]
+ 00af66d8 ["CALL", null, ["callee:008514f8:8"]]
- 00af62b0 bytes 826cf597
+ 00af66d8 bytes 886bf597
- 00af62c4 ["INT_ADD", "register:40f0:8", ["const:af62c4:8", "const:4:8"]]
- 00af62c4 ["CALL", null, ["callee:005e7420:8"]]
+ 00af66ec ["INT_ADD", "register:40f0:8", ["const:af66ec:8", "const:4:8"]]
+ 00af66ec ["CALL", null, ["callee:005e7420:8"]]
- 00af62c4 bytes 47c4eb97
+ 00af66ec bytes 4dc3eb97
- 00af62cc ["INT_ADD", "register:40f0:8", ["const:af62cc:8", "const:4:8"]]
- 00af62cc ["CALL", null, ["callee:008514f8:8"]]
+ 00af66f4 ["INT_ADD", "register:40f0:8", ["const:af66f4:8", "const:4:8"]]
+ 00af66f4 ["CALL", null, ["callee:008514f8:8"]]
- 00af62cc bytes 7b6cf597
+ 00af66f4 bytes 816bf597
~~~


<a id="compare-6269377def9a2e6129de2c50ec4178a0"></a>

### [`00af6318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6318.md) → [`00af6740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6740.md) FUN_00af6740

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`0070ea1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070ea1c.md) [`007119b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00711/007119b0.md) · 呼出先 2件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 2件 [`0070ea5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070ea5c.md) [`007119f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00711/007119f0.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 16.67% / 新版 14.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00af633c",
      "incomplete_value": true,
      "site": "00af6340",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              [
                "live",
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2768:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00af6340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6318.md#insn-00af6340) · [`00af632c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6318.md#insn-00af632c) · [`00af6344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6318.md#insn-00af6344)
- 新版 `00af6768`（命令位置の公開資料なし） · `00af6754`（命令位置の公開資料なし） · `00af676c`（命令位置の公開資料なし）

~~~diff
- 00af6340 ["INT_ADD", "register:40f0:8", ["const:af6340:8", "const:4:8"]]
- 00af6340 ["CALL", null, ["callee:005e7420:8"]]
+ 00af6768 ["INT_ADD", "register:40f0:8", ["const:af6768:8", "const:4:8"]]
+ 00af6768 ["CALL", null, ["callee:005e7420:8"]]
- 00af6340 bytes 28c4eb97
+ 00af6768 bytes 2ec3eb97
- 00af632c ["INT_ADD", "register:40f0:8", ["const:af632c:8", "const:4:8"]]
- 00af632c ["CALL", null, ["callee:008514f8:8"]]
+ 00af6754 ["INT_ADD", "register:40f0:8", ["const:af6754:8", "const:4:8"]]
+ 00af6754 ["CALL", null, ["callee:008514f8:8"]]
- 00af632c bytes 636cf597
+ 00af6754 bytes 696bf597
- 00af6344 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 00af6344 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00af6344 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00af6344 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00af676c ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
+ 00af676c ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00af676c ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00af676c ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00af6344 bytes a0010037
+ 00af676c bytes a0010037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-483f0514aefb7d7fff205c955d1bc4d5"></a>

### [`00af6468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6468.md) → [`00af6890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6890.md) FUN_00af6890

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00710090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00710/00710090.md) · 呼出先 2件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`007100d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00710/007100d0.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 40.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af68b4",
      "incomplete_value": true,
      "site": "00af68b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              [
                "live",
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2768:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00af6490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6468.md#insn-00af6490) · [`00af647c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6468.md#insn-00af647c) · [`00af6494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6468.md#insn-00af6494)
- 新版 `00af68b8`（命令位置の公開資料なし） · `00af68a4`（命令位置の公開資料なし） · `00af68bc`（命令位置の公開資料なし）

~~~diff
- 00af6490 ["INT_ADD", "register:40f0:8", ["const:af6490:8", "const:4:8"]]
- 00af6490 ["CALL", null, ["callee:005e7420:8"]]
+ 00af68b8 ["INT_ADD", "register:40f0:8", ["const:af68b8:8", "const:4:8"]]
+ 00af68b8 ["CALL", null, ["callee:005e7420:8"]]
- 00af6490 bytes d4c3eb97
+ 00af68b8 bytes dac2eb97
- 00af647c ["INT_ADD", "register:40f0:8", ["const:af647c:8", "const:4:8"]]
- 00af647c ["CALL", null, ["callee:008514f8:8"]]
+ 00af68a4 ["INT_ADD", "register:40f0:8", ["const:af68a4:8", "const:4:8"]]
+ 00af68a4 ["CALL", null, ["callee:008514f8:8"]]
- 00af647c bytes 0f6cf597
+ 00af68a4 bytes 156bf597
- 00af6494 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 00af6494 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00af6494 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00af6494 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00af68bc ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
+ 00af68bc ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00af68bc ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00af68bc ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00af6494 bytes 60000037
+ 00af68bc bytes 60000037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27a044a8027c2b48143b0b55e48cddb8"></a>

### [`00af65b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af65b8.md) → [`00af69e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af69e0.md) FUN_00af69e0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 7件 [`005fb400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fb/005fb400.md) [`005fb8fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fb/005fb8fc.md) [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) [`0070ea1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070ea1c.md) [`00710090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00710/00710090.md) · 呼出先 2件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 7件 [`005fb440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fb/005fb440.md) [`005fb93c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fb/005fb93c.md) [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) [`0070ea5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070ea5c.md) [`007100d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00710/007100d0.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 28.57% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af65b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af65b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af65bc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af65b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af65bc",
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
      "00af69e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af69e4",
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

- 旧版 [`00af65b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af65b8.md#insn-00af65b8) · [`00af65bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af65b8.md#insn-00af65bc) · [`00af65e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af65b8.md#insn-00af65e0)
- 新版 `00af6a08`（命令位置の公開資料なし）

~~~diff
- 00af65b8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af65b8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af65b8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00af65b8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af65b8 bytes fd7bbea9
- 00af65bc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af65bc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af65bc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00af65bc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af65bc bytes f44f01a9
- 00af65e0 ["INT_ADD", "register:40f0:8", ["const:af65e0:8", "const:4:8"]]
- 00af65e0 ["CALL", null, ["callee:005e7420:8"]]
+ 00af6a08 ["INT_ADD", "register:40f0:8", ["const:af6a08:8", "const:4:8"]]
+ 00af6a08 ["CALL", null, ["callee:005e7420:8"]]
- 00af65e0 bytes 80c3eb97
+ 00af6a08 bytes 86c2eb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2ddfccaf4b07b879fd9c89d8044cbbe"></a>

### [`00af6698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6698.md) → [`00af6ac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6ac0.md) FUN_00af6ac0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0070ea1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070ea1c.md) [`007119b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00711/007119b0.md) · 呼出先 2件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 2件 [`0070ea5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070ea5c.md) [`007119f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00711/007119f0.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 7.14% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af6698"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af6698"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af669c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af6698",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af669c",
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
      "00af6ac0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af6ac4",
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

- 旧版 [`00af6698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6698.md#insn-00af6698) · [`00af669c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6698.md#insn-00af669c) · [`00af66c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6698.md#insn-00af66c0)
- 新版 `00af6ae8`（命令位置の公開資料なし）

~~~diff
- 00af6698 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af6698 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af6698 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00af6698 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af6698 bytes fd7bbea9
- 00af669c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af669c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af669c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00af669c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af669c bytes f44f01a9
- 00af66c0 ["INT_ADD", "register:40f0:8", ["const:af66c0:8", "const:4:8"]]
- 00af66c0 ["CALL", null, ["callee:005e7420:8"]]
+ 00af6ae8 ["INT_ADD", "register:40f0:8", ["const:af6ae8:8", "const:4:8"]]
+ 00af6ae8 ["CALL", null, ["callee:005e7420:8"]]
- 00af66c0 bytes 48c3eb97
+ 00af6ae8 bytes 4ec2eb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8add00c1a1ae98517d29736f443669e0"></a>

### [`00af6a18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6a18.md) → [`00af6e40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6e40.md) FUN_00af6e40

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af6a34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6a18.md#insn-00af6a34)
- 新版 `00af6e5c`（命令位置の公開資料なし）

~~~diff
- 00af6a34 ["INT_ADD", "register:40f0:8", ["const:af6a34:8", "const:4:8"]]
- 00af6a34 ["CALL", null, ["callee:008514f8:8"]]
+ 00af6e5c ["INT_ADD", "register:40f0:8", ["const:af6e5c:8", "const:4:8"]]
+ 00af6e5c ["CALL", null, ["callee:008514f8:8"]]
- 00af6a34 bytes a16af597
+ 00af6e5c bytes a769f597
~~~


<a id="compare-ac1a41ce05d685d13769771b315a8a0f"></a>

### [`00af6a64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6a64.md) → [`00af6e8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6e8c.md) FUN_00af6e8c

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af6a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6a64.md#insn-00af6a80)
- 新版 `00af6ea8`（命令位置の公開資料なし）

~~~diff
- 00af6a80 ["INT_ADD", "register:40f0:8", ["const:af6a80:8", "const:4:8"]]
- 00af6a80 ["CALL", null, ["callee:008514f8:8"]]
+ 00af6ea8 ["INT_ADD", "register:40f0:8", ["const:af6ea8:8", "const:4:8"]]
+ 00af6ea8 ["CALL", null, ["callee:008514f8:8"]]
- 00af6a80 bytes 8e6af597
+ 00af6ea8 bytes 9469f597
~~~


<a id="compare-c7b016fd67133457ed513016fa3bd024"></a>

### [`00af6d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6d34.md) → [`00af715c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af715c.md) FUN_00af715c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`0070ea1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070ea1c.md) [`007119b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00711/007119b0.md) · 呼出先 2件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 2件 [`0070ea5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070ea5c.md) [`007119f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00711/007119f0.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 40.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af6d48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6d34.md#insn-00af6d48) · [`00af6d5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6d34.md#insn-00af6d5c) · [`00af6d60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6d34.md#insn-00af6d60)
- 新版 `00af7170`（命令位置の公開資料なし） · `00af7184`（命令位置の公開資料なし） · `00af7188`（命令位置の公開資料なし）

~~~diff
- 00af6d48 ["INT_ADD", "register:40f0:8", ["const:af6d48:8", "const:4:8"]]
- 00af6d48 ["CALL", null, ["callee:008514f8:8"]]
+ 00af7170 ["INT_ADD", "register:40f0:8", ["const:af7170:8", "const:4:8"]]
+ 00af7170 ["CALL", null, ["callee:008514f8:8"]]
- 00af6d48 bytes dc69f597
+ 00af7170 bytes e268f597
- 00af6d5c ["INT_ADD", "register:40f0:8", ["const:af6d5c:8", "const:4:8"]]
- 00af6d5c ["CALL", null, ["callee:005e7420:8"]]
+ 00af7184 ["INT_ADD", "register:40f0:8", ["const:af7184:8", "const:4:8"]]
+ 00af7184 ["CALL", null, ["callee:005e7420:8"]]
- 00af6d5c bytes a1c1eb97
+ 00af7184 bytes a7c0eb97
- 00af6d60 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 00af6d60 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00af6d60 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00af6d60 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00af7188 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
+ 00af7188 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00af7188 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00af7188 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00af6d60 bytes a0010037
+ 00af7188 bytes a0010037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3dff26092d6a2c97c3ea1f134140ab8c"></a>

### [`00af6da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6da4.md) → [`00af71cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af71cc.md) FUN_00af71cc

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af6dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6da4.md#insn-00af6dc0)
- 新版 `00af71e8`（命令位置の公開資料なし）

~~~diff
- 00af6dc0 ["INT_ADD", "register:40f0:8", ["const:af6dc0:8", "const:4:8"]]
- 00af6dc0 ["CALL", null, ["callee:008514f8:8"]]
+ 00af71e8 ["INT_ADD", "register:40f0:8", ["const:af71e8:8", "const:4:8"]]
+ 00af71e8 ["CALL", null, ["callee:008514f8:8"]]
- 00af6dc0 bytes be69f597
+ 00af71e8 bytes c468f597
~~~


<a id="compare-861244d8510156d42040bdf5f72d3a04"></a>

### [`00af6df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6df0.md) → [`00af7218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7218.md) FUN_00af7218

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 3件 [`0070ea1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070ea1c.md) [`00710298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00710/00710298.md) [`007119b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00711/007119b0.md) · 呼出先 2件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 3件 [`0070ea5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070ea5c.md) [`007102d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00710/007102d8.md) [`007119f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00711/007119f0.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 40.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af6e04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6df0.md#insn-00af6e04) · [`00af6e18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6df0.md#insn-00af6e18) · [`00af6e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6df0.md#insn-00af6e1c)
- 新版 `00af722c`（命令位置の公開資料なし） · `00af7240`（命令位置の公開資料なし） · `00af7244`（命令位置の公開資料なし）

~~~diff
- 00af6e04 ["INT_ADD", "register:40f0:8", ["const:af6e04:8", "const:4:8"]]
- 00af6e04 ["CALL", null, ["callee:008514f8:8"]]
+ 00af722c ["INT_ADD", "register:40f0:8", ["const:af722c:8", "const:4:8"]]
+ 00af722c ["CALL", null, ["callee:008514f8:8"]]
- 00af6e04 bytes ad69f597
+ 00af722c bytes b368f597
- 00af6e18 ["INT_ADD", "register:40f0:8", ["const:af6e18:8", "const:4:8"]]
- 00af6e18 ["CALL", null, ["callee:005e7420:8"]]
+ 00af7240 ["INT_ADD", "register:40f0:8", ["const:af7240:8", "const:4:8"]]
+ 00af7240 ["CALL", null, ["callee:005e7420:8"]]
- 00af6e18 bytes 72c1eb97
+ 00af7240 bytes 78c0eb97
- 00af6e1c ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 00af6e1c ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00af6e1c ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00af6e1c ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00af7244 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
+ 00af7244 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00af7244 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00af7244 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00af6e1c bytes a0010037
+ 00af7244 bytes a0010037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7acf184901032ebdf927560eb14f9757"></a>

### [`00af6eac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6eac.md) → [`00af72d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af72d4.md) FUN_00af72d4

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`0070ea1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070ea1c.md) [`007119b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00711/007119b0.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 2件 [`0070ea5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070ea5c.md) [`007119f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00711/007119f0.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af6ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6eac.md#insn-00af6ec0)
- 新版 `00af72e8`（命令位置の公開資料なし）

~~~diff
- 00af6ec0 ["INT_ADD", "register:40f0:8", ["const:af6ec0:8", "const:4:8"]]
- 00af6ec0 ["CALL", null, ["callee:008514f8:8"]]
+ 00af72e8 ["INT_ADD", "register:40f0:8", ["const:af72e8:8", "const:4:8"]]
+ 00af72e8 ["CALL", null, ["callee:008514f8:8"]]
- 00af6ec0 bytes 7e69f597
+ 00af72e8 bytes 8468f597
~~~


<a id="compare-2742cbd0786b3c0b4564a3e3a396760e"></a>

### [`00af7060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af7/00af7060.md) → [`00af7488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af7/00af7488.md) FUN_00af7488

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00af707c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af7/00af7060.md#insn-00af707c)
- 新版 `00af74a4`（命令位置の公開資料なし）

~~~diff
- 00af707c ["INT_ADD", "register:40f0:8", ["const:af707c:8", "const:4:8"]]
- 00af707c ["CALL", null, ["callee:008514f8:8"]]
+ 00af74a4 ["INT_ADD", "register:40f0:8", ["const:af74a4:8", "const:4:8"]]
+ 00af74a4 ["CALL", null, ["callee:008514f8:8"]]
- 00af707c bytes 0f69f597
+ 00af74a4 bytes 1568f597
~~~


