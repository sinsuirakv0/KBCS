# v15.7.4 → v16.0.0 · 最優先の変更候補 (50)

[一覧の目次](README.md)

<a id="compare-81e59d7349fb08ff288d3d2e78752b1c"></a>

### [`009e16a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e16a0.md) → [`00a3e59c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3e59c.md) FUN_00a3e59c

採用 · 移動量 `+0x5cefc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a3e5a8",
      "incomplete_value": false,
      "site": "00a3e5a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:fb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e16ac",
      "incomplete_value": false,
      "site": "009e16ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:998:8"
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
      "00a3e5a8",
      "DATA",
      [
        "storage",
        "00c0b998",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a3e5a8",
      "DATA",
      [
        "storage",
        "00c8afb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e16a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e16a0.md#insn-009e16a4) · [`009e16a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e16a0.md#insn-009e16a8)
- 新版 [`00a3e5a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3e59c.md#insn-00a3e5a0) · [`00a3e5a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3e59c.md#insn-00a3e5a4)

~~~diff
- 009e16a4 ["COPY", "register:4048:8", ["const:c0b000:8"]]
+ 00a3e5a0 ["COPY", "register:4048:8", ["const:c8a000:8"]]
- 009e16a4 bytes 491100d0
+ 00a3e5a0 bytes 69120090
- 009e16a8 ["COPY", "tmp:0:8", ["const:998:8"]]
- 009e16a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 009e16a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 009e16a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a3e5a4 ["COPY", "tmp:0:8", ["const:fb8:8"]]
+ 00a3e5a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a3e5a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a3e5a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 009e16a8 bytes 29612691
+ 00a3e5a4 bytes 29e13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9937b662d5642a96127054ef4aef7957"></a>

### [`009e16bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e16bc.md) → [`00a3e5b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3e5b8.md) FUN_00a3e5b8

採用 · 移動量 `+0x5cefc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00885f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 40.00% / 新版 18.18%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009e16d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009e1704"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a3e5d0"
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
      "unmatched:009e16d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:009e16e0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ]
  ],
  "added": [
    [
      "00a3e5d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a3e5dc",
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

- 旧版 [`009e16d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e16bc.md#insn-009e16d4) · [`009e16e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e16bc.md#insn-009e16e0) · [`009e16ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e16bc.md#insn-009e16ec)
- 新版 [`00a3e5e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3e5b8.md#insn-00a3e5e8)

~~~diff
- 009e16d4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 009e16d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 009e16d4 bytes f30b00f9
- 009e16e0 ["INT_ADD", "register:40f0:8", ["const:9e16e0:8", "const:4:8"]]
- 009e16e0 ["CALL", null, ["ram:457e1c:8"]]
- 009e16e0 bytes cfd9e997
- 009e16ec ["INT_ADD", "register:40f0:8", ["const:9e16ec:8", "const:4:8"]]
- 009e16ec ["CALL", null, ["callee:0047cd94:8"]]
+ 00a3e5e8 ["INT_ADD", "register:40f0:8", ["const:a3e5e8:8", "const:4:8"]]
+ 00a3e5e8 ["CALL", null, ["callee:0047cd94:8"]]
- 009e16ec bytes 04e2e997
+ 00a3e5e8 bytes ebf9e897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa2dff98df78e0af97cfa2b78639f88f"></a>

### [`009e1734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e1734.md) → [`00a3e630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3e630.md) FUN_00a3e630

採用 · 移動量 `+0x5cefc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 25.00% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009e1750"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a3e64c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "009e1740",
      "incomplete_value": true,
      "site": "009e1754",
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
                "register:4000:8"
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
      "unmatched:009e1750",
      "DATA",
      [
        "storage",
        "00c0ba18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a3e64c",
      "DATA",
      [
        "storage",
        "00c8b038",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e1750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e1734.md#insn-009e1750) · [`009e1754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e1734.md#insn-009e1754)
- 新版 [`00a3e650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3e630.md#insn-00a3e650) · [`00a3e64c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3e630.md#insn-00a3e64c)

~~~diff
- 009e1750 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 009e1750 ["COPY", "tmp:1:8", ["register:4000:8"]]
- 009e1750 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:40:8"]]
- 009e1750 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 009e1750 bytes 080404f8
- 009e1754 ["INT_ADD", "register:40f0:8", ["const:9e1754:8", "const:4:8"]]
- 009e1754 ["CALL", null, ["callee:005c175c:8"]]
+ 00a3e650 ["INT_ADD", "register:40f0:8", ["const:a3e650:8", "const:4:8"]]
+ 00a3e650 ["CALL", null, ["callee:005c175c:8"]]
- 009e1754 bytes 76eeee97
+ 00a3e650 bytes 430cee97
+ 00a3e64c ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00a3e64c ["COPY", "tmp:1:8", ["register:4000:8"]]
+ 00a3e64c ["INT_ADD", "register:4000:8", ["register:4000:8", "const:40:8"]]
+ 00a3e64c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 00a3e64c bytes 080404f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-617dd850083753d7189f455d43707d99"></a>

### [`009e1788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e1788.md) → [`00a3e684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3e684.md) FUN_00a3e684

採用 · 移動量 `+0x5cefc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009e17a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a3e6a0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "009e17a4",
      "incomplete_value": true,
      "site": "009e17a8",
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
            "const:40:8"
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
      "unmatched:009e17a4",
      "DATA",
      [
        "storage",
        "00c0ba18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a3e6a0",
      "DATA",
      [
        "storage",
        "00c8b038",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e17a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e1788.md#insn-009e17a4) · [`009e17a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e1788.md#insn-009e17a8)
- 新版 [`00a3e6a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3e684.md#insn-00a3e6a4) · [`00a3e6a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3e684.md#insn-00a3e6a0)

~~~diff
- 009e17a4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 009e17a4 ["COPY", "tmp:1:8", ["register:4000:8"]]
- 009e17a4 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:40:8"]]
- 009e17a4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 009e17a4 bytes 080404f8
- 009e17a8 ["INT_ADD", "register:40f0:8", ["const:9e17a8:8", "const:4:8"]]
- 009e17a8 ["CALL", null, ["callee:005c175c:8"]]
+ 00a3e6a4 ["INT_ADD", "register:40f0:8", ["const:a3e6a4:8", "const:4:8"]]
+ 00a3e6a4 ["CALL", null, ["callee:005c175c:8"]]
- 009e17a8 bytes 61eeee97
+ 00a3e6a4 bytes 2e0cee97
+ 00a3e6a0 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00a3e6a0 ["COPY", "tmp:1:8", ["register:4000:8"]]
+ 00a3e6a0 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:40:8"]]
+ 00a3e6a0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 00a3e6a0 bytes 080404f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a1380378afe9c1ff177e0554ab84eac"></a>

### [`009e17d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e17d8.md) → [`00a3e6d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3e6d4.md) FUN_00a3e6d4

採用 · 移動量 `+0x5cefc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`009e1b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e1b70.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00a3ea6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3ea6c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009e17fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a3e6f8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "009e17e8",
      "incomplete_value": false,
      "site": "009e17ec",
      "value": [
        "leaf",
        "const:58:8"
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
      "unmatched:009e17fc",
      "DATA",
      [
        "storage",
        "00c0ba18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a3e6f8",
      "DATA",
      [
        "storage",
        "00c8b038",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e17ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e17d8.md#insn-009e17ec) · [`009e17fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e17d8.md#insn-009e17fc)
- 新版 [`00a3e6e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3e6d4.md#insn-00a3e6e8) · [`00a3e6f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3e6d4.md#insn-00a3e6f8)

~~~diff
- 009e17ec ["INT_ADD", "register:40f0:8", ["const:9e17ec:8", "const:4:8"]]
- 009e17ec ["CALL", null, ["callee:00c57a90:8"]]
+ 00a3e6e8 ["INT_ADD", "register:40f0:8", ["const:a3e6e8:8", "const:4:8"]]
+ 00a3e6e8 ["CALL", null, ["callee:00c57a90:8"]]
- 009e17ec bytes 15e60794
+ 00a3e6e8 bytes ea640894
- 009e17fc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 009e17fc ["COPY", "tmp:1:8", ["register:4000:8"]]
- 009e17fc ["INT_ADD", "register:4000:8", ["register:4000:8", "const:8:8"]]
- 009e17fc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 009e17fc bytes 088400f8
+ 00a3e6f8 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00a3e6f8 ["COPY", "tmp:1:8", ["register:4000:8"]]
+ 00a3e6f8 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:8:8"]]
+ 00a3e6f8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 00a3e6f8 bytes 088400f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d09d99cccdb88d815ce77d2eaf5ff422"></a>

### [`009e1848`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e1848.md) → [`00a3e744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3e744.md) FUN_00a3e744

採用 · 移動量 `+0x5cefc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 84.21% / 新版 84.21%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009e1848"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009e1848"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009e184c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009e1848",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:009e184c",
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
      "00a3e744",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00a3e748",
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

- 旧版 [`009e1848`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e1848.md#insn-009e1848) · [`009e184c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e1848.md#insn-009e184c) · [`009e1860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e1848.md#insn-009e1860)
- 新版 [`00a3e75c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3e744.md#insn-00a3e75c)

~~~diff
- 009e1848 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 009e1848 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 009e1848 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 009e1848 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 009e1848 bytes fd7bbea9
- 009e184c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 009e184c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 009e184c bytes f30b00f9
- 009e1860 ["INT_ADD", "register:40f0:8", ["const:9e1860:8", "const:4:8"]]
- 009e1860 ["CALL", null, ["callee:005c175c:8"]]
+ 00a3e75c ["INT_ADD", "register:40f0:8", ["const:a3e75c:8", "const:4:8"]]
+ 00a3e75c ["CALL", null, ["callee:005c175c:8"]]
- 009e1860 bytes 33eeee97
+ 00a3e75c bytes 000cee97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d44b622d39c14bb051a235eab4558b5"></a>

### [`009e1894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e1894.md) → [`00a3e790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3e790.md) FUN_00a3e790

採用 · 移動量 `+0x5cefc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009dfd24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009df/009dfd24.md) · 呼出先 2件 [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00a3cc20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3c/00a3cc20.md) · 呼出先 2件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 28.57% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009e1894"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009e1894"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009e1898"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009e1894",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:009e1898",
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
      "00a3e790",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00a3e794",
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

- 旧版 [`009e1894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e1894.md#insn-009e1894) · [`009e1898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e1894.md#insn-009e1898) · [`009e18ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e1894.md#insn-009e18ac)
- 新版 [`00a3e7a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3e790.md#insn-00a3e7a8)

~~~diff
- 009e1894 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 009e1894 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 009e1894 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 009e1894 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 009e1894 bytes fd7bbea9
- 009e1898 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 009e1898 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 009e1898 bytes f30b00f9
- 009e18ac ["INT_ADD", "register:40f0:8", ["const:9e18ac:8", "const:4:8"]]
- 009e18ac ["CALL", null, ["callee:005c175c:8"]]
+ 00a3e7a8 ["INT_ADD", "register:40f0:8", ["const:a3e7a8:8", "const:4:8"]]
+ 00a3e7a8 ["CALL", null, ["callee:005c175c:8"]]
- 009e18ac bytes 20eeee97
+ 00a3e7a8 bytes ed0bee97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-821634ce8ef8010e4976b39bfdbbebba"></a>

### [`009e18dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e18dc.md) → [`00a3e7d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3e7d8.md) FUN_00a3e7d8

採用 · 移動量 `+0x5cefc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 10件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md) [`0066b478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066b/0066b478.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`006917c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00691/006917c0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 87.60% / 新版 87.60%

CFGの説明率　旧版 53.57% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 2件, `store_value` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009e18e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009e18e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009e18e4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009e18e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:009e18e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:009e18e8",
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
      "00a3e7dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00a3e7e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00a3e7e4",
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

- 旧版 [`009e18e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e18dc.md#insn-009e18e0) · [`009e18e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e18dc.md#insn-009e18e4) · [`009e18e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e18dc.md#insn-009e18e8)

~~~diff
- 009e18e0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 009e18e0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 009e18e0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 009e18e0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009e18e0 bytes fd7b08a9
- 009e18e4 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 009e18e4 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 009e18e4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:90:8"]]
- 009e18e4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009e18e4 bytes f85f09a9
- 009e18e8 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 009e18e8 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 009e18e8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:a0:8"]]
- 009e18e8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009e18e8 bytes f6570aa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dbc33d60fecbaa4759f5e75c7eed8c03"></a>

### [`009e1b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e1b70.md) → [`00a3ea6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3ea6c.md) FUN_00a3ea6c

採用 · 移動量 `+0x5cefc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`009e17d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e17d8.md) [`009e182c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e182c.md) · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0066b478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066b/0066b478.md)
- 新版 呼出元 2件 [`00a3e6d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3e6d4.md) [`00a3e728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3e728.md) · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`006917c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00691/006917c0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 67.39% / 新版 67.39%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009e1b98"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009e1bb4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009e1bd8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009e1be8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "006917c0"
      ]
    ]
  ],
  "added": [
    [
      "00a3eae4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "006917c0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e1b98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e1b70.md#insn-009e1b98) · [`009e1bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e1b70.md#insn-009e1bb4) · [`009e1bc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e1b70.md#insn-009e1bc4)
- 新版 [`00a3eac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3ea6c.md#insn-00a3eac0)

~~~diff
- 009e1b98 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 009e1b98 ["COPY", "tmp:1:8", ["register:40a0:8"]]
- 009e1b98 ["INT_ADD", "register:40a0:8", ["register:40a0:8", "const:8:8"]]
- 009e1b98 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 009e1b98 bytes 888600f8
- 009e1bb4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 009e1bb4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 009e1bb4 bytes 8002803d
- 009e1bc4 ["INT_ADD", "register:40f0:8", ["const:9e1bc4:8", "const:4:8"]]
- 009e1bc4 ["CALL", null, ["callee:0043bae0:8"]]
+ 00a3eac0 ["INT_ADD", "register:40f0:8", ["const:a3eac0:8", "const:4:8"]]
+ 00a3eac0 ["CALL", null, ["callee:0043bae0:8"]]
- 009e1bc4 bytes 07dde897
+ 00a3eac0 bytes 08f4e797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-643dd75e1871128ea5f2819ea48c3e61"></a>

### [`009e1c64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e1c64.md) → [`00a3eb60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3eb60.md) FUN_00a3eb60

採用 · 移動量 `+0x5cefc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009e1c7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e1c64.md#insn-009e1c7c)
- 新版 [`00a3eb78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3eb60.md#insn-00a3eb78)

~~~diff
- 009e1c7c ["INT_ADD", "register:40f0:8", ["const:9e1c7c:8", "const:4:8"]]
- 009e1c7c ["CALL", null, ["callee:005c175c:8"]]
+ 00a3eb78 ["INT_ADD", "register:40f0:8", ["const:a3eb78:8", "const:4:8"]]
+ 00a3eb78 ["CALL", null, ["callee:005c175c:8"]]
- 009e1c7c bytes 2cedee97
+ 00a3eb78 bytes f90aee97
~~~


<a id="compare-253d3f1f3746e99b2767d0f3cdb2f650"></a>

### [`009e1ccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e1ccc.md) → [`00a3ebc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3ebc8.md) FUN_00a3ebc8

採用 · 移動量 `+0x5cefc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a3ebe4",
      "incomplete_value": false,
      "site": "00a3ebe4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e1ce8",
      "incomplete_value": false,
      "site": "009e1ce8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:a88:8"
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
      "00a3ebe4",
      "DATA",
      [
        "storage",
        "00c0ba88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a3ebe4",
      "DATA",
      [
        "storage",
        "00c8b0a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e1cdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e1ccc.md#insn-009e1cdc) · [`009e1ce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e1ccc.md#insn-009e1ce0) · [`009e1cec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e1ccc.md#insn-009e1cec)
- 新版 [`00a3ebd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3ebc8.md#insn-00a3ebd8) · [`00a3ebdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3ebc8.md#insn-00a3ebdc) · [`00a3ebe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3ebc8.md#insn-00a3ebe8)

~~~diff
- 009e1cdc ["COPY", "register:4040:8", ["const:c0b000:8"]]
+ 00a3ebd8 ["COPY", "register:4040:8", ["const:c8b000:8"]]
- 009e1cdc bytes 481100d0
+ 00a3ebd8 bytes 681200b0
- 009e1ce0 ["COPY", "tmp:0:8", ["const:a88:8"]]
- 009e1ce0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009e1ce0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009e1ce0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a3ebdc ["COPY", "tmp:0:8", ["const:a8:8"]]
+ 00a3ebdc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a3ebdc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a3ebdc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009e1ce0 bytes 08212a91
+ 00a3ebdc bytes 08a10291
- 009e1cec ["INT_ADD", "register:40f0:8", ["const:9e1cec:8", "const:4:8"]]
- 009e1cec ["CALL", null, ["callee:005c175c:8"]]
+ 00a3ebe8 ["INT_ADD", "register:40f0:8", ["const:a3ebe8:8", "const:4:8"]]
+ 00a3ebe8 ["CALL", null, ["callee:005c175c:8"]]
- 009e1cec bytes 10edee97
+ 00a3ebe8 bytes dd0aee97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36dad979bc5891abbb9a88f105e47b42"></a>

### [`009e1d0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e1d0c.md) → [`00a3ec08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3ec08.md) FUN_00a3ec08

採用 · 移動量 `+0x5cefc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0066b478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066b/0066b478.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`006917c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00691/006917c0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a3ec40",
      "incomplete_value": false,
      "site": "00a3ec40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e1d44",
      "incomplete_value": false,
      "site": "009e1d44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:a88:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a3ec40",
      "DATA",
      [
        "storage",
        "00c0ba88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a3ec40",
      "DATA",
      [
        "storage",
        "00c8b0a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e1d28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e1d0c.md#insn-009e1d28) · [`009e1d30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e1d0c.md#insn-009e1d30) · [`009e1d34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e1d0c.md#insn-009e1d34)
- 新版 [`00a3ec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3ec08.md#insn-00a3ec24) · [`00a3ec2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3ec08.md#insn-00a3ec2c) · [`00a3ec30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3ec08.md#insn-00a3ec30)

~~~diff
- 009e1d28 ["INT_ADD", "register:40f0:8", ["const:9e1d28:8", "const:4:8"]]
- 009e1d28 ["CALL", null, ["callee:00c57a90:8"]]
+ 00a3ec24 ["INT_ADD", "register:40f0:8", ["const:a3ec24:8", "const:4:8"]]
+ 00a3ec24 ["CALL", null, ["callee:00c57a90:8"]]
- 009e1d28 bytes c6e40794
+ 00a3ec24 bytes 9b630894
- 009e1d30 ["COPY", "register:4040:8", ["const:c0b000:8"]]
+ 00a3ec2c ["COPY", "register:4040:8", ["const:c8b000:8"]]
- 009e1d30 bytes 481100d0
+ 00a3ec2c bytes 681200b0
- 009e1d34 ["COPY", "tmp:0:8", ["const:a88:8"]]
- 009e1d34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009e1d34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009e1d34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a3ec30 ["COPY", "tmp:0:8", ["const:a8:8"]]
+ 00a3ec30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a3ec30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a3ec30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009e1d34 bytes 08212a91
+ 00a3ec30 bytes 08a10291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fbc54dfd1bcdd519d50c6f2b1c6bdb07"></a>

### [`009e1dd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e1dd0.md) → [`00a3eccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3eccc.md) FUN_00a3eccc

採用 · 移動量 `+0x5cefc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`0066b478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066b/0066b478.md)
- 新版 呼出元 0件  · 呼出先 1件 [`006917c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00691/006917c0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a3ed04",
      "incomplete_value": false,
      "site": "00a3ed10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e1e08",
      "incomplete_value": false,
      "site": "009e1e14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:a88:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a3ed10",
      "DATA",
      [
        "storage",
        "00c0ba88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a3ed10",
      "DATA",
      [
        "storage",
        "00c8b0a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e1e04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e1dd0.md#insn-009e1e04) · [`009e1e08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e1dd0.md#insn-009e1e08) · [`009e1e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e1dd0.md#insn-009e1e20)
- 新版 [`00a3ed00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3eccc.md#insn-00a3ed00) · [`00a3ed04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3eccc.md#insn-00a3ed04) · [`00a3ed1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3eccc.md#insn-00a3ed1c)

~~~diff
- 009e1e04 ["COPY", "register:4040:8", ["const:c0b000:8"]]
+ 00a3ed00 ["COPY", "register:4040:8", ["const:c8b000:8"]]
- 009e1e04 bytes 481100d0
+ 00a3ed00 bytes 681200b0
- 009e1e08 ["COPY", "tmp:0:8", ["const:a88:8"]]
- 009e1e08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009e1e08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009e1e08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a3ed04 ["COPY", "tmp:0:8", ["const:a8:8"]]
+ 00a3ed04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a3ed04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a3ed04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009e1e08 bytes 08212a91
+ 00a3ed04 bytes 08a10291
- 009e1e20 ["INT_ADD", "register:40f0:8", ["const:9e1e20:8", "const:4:8"]]
- 009e1e20 ["CALL", null, ["callee:006917c0:8"]]
+ 00a3ed1c ["INT_ADD", "register:40f0:8", ["const:a3ed1c:8", "const:4:8"]]
+ 00a3ed1c ["CALL", null, ["callee:006917c0:8"]]
- 009e1e20 bytes 9625f297
+ 00a3ed1c bytes a94af197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b95b51350818ce982e4578d05ee20a0"></a>

### [`009e2100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e2/009e2100.md) → [`00a3effc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3effc.md) FUN_00a3effc

採用 · 移動量 `+0x5cefc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a3f020",
      "incomplete_value": false,
      "site": "00a3f020",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:138:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e2124",
      "incomplete_value": false,
      "site": "009e2124",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:b18:8"
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
      "00a3f020",
      "DATA",
      [
        "storage",
        "00c0bb18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a3f020",
      "DATA",
      [
        "storage",
        "00c8b138",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e2114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e2/009e2100.md#insn-009e2114) · [`009e211c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e2/009e2100.md#insn-009e211c) · [`009e2120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e2/009e2100.md#insn-009e2120)
- 新版 [`00a3f010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3effc.md#insn-00a3f010) · [`00a3f018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3effc.md#insn-00a3f018) · [`00a3f01c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3effc.md#insn-00a3f01c)

~~~diff
- 009e2114 ["INT_ADD", "register:40f0:8", ["const:9e2114:8", "const:4:8"]]
- 009e2114 ["CALL", null, ["callee:00c57a90:8"]]
+ 00a3f010 ["INT_ADD", "register:40f0:8", ["const:a3f010:8", "const:4:8"]]
+ 00a3f010 ["CALL", null, ["callee:00c57a90:8"]]
- 009e2114 bytes cbe30794
+ 00a3f010 bytes a0620894
- 009e211c ["COPY", "register:4040:8", ["const:c0b000:8"]]
+ 00a3f018 ["COPY", "register:4040:8", ["const:c8b000:8"]]
- 009e211c bytes 481100b0
+ 00a3f018 bytes 68120090
- 009e2120 ["COPY", "tmp:0:8", ["const:b18:8"]]
- 009e2120 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009e2120 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009e2120 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a3f01c ["COPY", "tmp:0:8", ["const:138:8"]]
+ 00a3f01c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a3f01c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a3f01c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009e2120 bytes 08612c91
+ 00a3f01c bytes 08e10491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a29cf0f62e634b13281856622a4a365a"></a>

### [`009e2134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e2/009e2134.md) → [`00a3f030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3f/00a3f030.md) FUN_00a3f030

採用 · 移動量 `+0x5cefc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a3f03c",
      "incomplete_value": false,
      "site": "00a3f03c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:138:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e2140",
      "incomplete_value": false,
      "site": "009e2140",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:b18:8"
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
      "00a3f03c",
      "DATA",
      [
        "storage",
        "00c0bb18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a3f03c",
      "DATA",
      [
        "storage",
        "00c8b138",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e2138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e2/009e2134.md#insn-009e2138) · [`009e213c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e2/009e2134.md#insn-009e213c)
- 新版 [`00a3f034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3f/00a3f030.md#insn-00a3f034) · [`00a3f038`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3f/00a3f030.md#insn-00a3f038)

~~~diff
- 009e2138 ["COPY", "register:4048:8", ["const:c0b000:8"]]
+ 00a3f034 ["COPY", "register:4048:8", ["const:c8b000:8"]]
- 009e2138 bytes 491100b0
+ 00a3f034 bytes 69120090
- 009e213c ["COPY", "tmp:0:8", ["const:b18:8"]]
- 009e213c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 009e213c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 009e213c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a3f038 ["COPY", "tmp:0:8", ["const:138:8"]]
+ 00a3f038 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a3f038 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a3f038 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 009e213c bytes 29612c91
+ 00a3f038 bytes 29e10491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc66701fc0f8ed00fd2ae837c92cb73f"></a>

### [`009e2258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e2/009e2258.md) → [`00a3f154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3f/00a3f154.md) FUN_00a3f154

採用 · 移動量 `+0x5cefc` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009e0d64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e0/009e0d64.md) · 呼出先 28件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0044b8ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b8ec.md) [`0044b9cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b9cc.md)
- 新版 呼出元 1件 [`00a3dc60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3d/00a3dc60.md) · 呼出先 28件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0046e784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e784.md) [`0046e864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e864.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 43.22% / 新版 43.22%

CFGの説明率　旧版 13.61% / 新版 13.03%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 17件, `store_condition` 4件, `store_value` 1件, `unresolved_branch_alignment` 101件, `unresolved_call_alignment` 80件, `unresolved_store_alignment` 158件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a3f194",
      "incomplete_value": false,
      "site": "00a3f198",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:1b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e2298",
      "incomplete_value": false,
      "site": "009e229c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:b98:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009e2304"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009e2314"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a3f198",
      "DATA",
      [
        "storage",
        "00c0bb98",
        null,
        "pointer"
      ]
    ],
    [
      "00a3f1d4",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:009e22ec",
      "READ",
      [
        "storage",
        "002a5920",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00a3f198",
      "DATA",
      [
        "storage",
        "00c8b1b8",
        null,
        "pointer"
      ]
    ],
    [
      "00a3f1d4",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ],
    [
      "00a3f1e8",
      "READ",
      [
        "storage",
        "002b634e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e2304`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e2/009e2258.md#insn-009e2304) · [`009e2314`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e2/009e2258.md#insn-009e2314) · [`009e231c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e2/009e2258.md#insn-009e231c)

~~~diff
- 009e2304 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 009e2304 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:41:8"]]
- 009e2304 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 009e2304 bytes e91304f8
- 009e2314 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 009e2314 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffb8:8"]]
- 009e2314 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 009e2314 bytes a8831b38
- 009e231c ["COPY", "tmp:0:4", ["const:0:4"]]
- 009e231c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 009e231c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:4b:8"]]
- 009e231c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 009e231c bytes ff2f0139
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-870f8a24a78f245d05928b8ebdc739a1"></a>

### [`009e3c4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e3/009e3c4c.md) → [`00a40b48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a40/00a40b48.md) FUN_00a40b48

採用 · 移動量 `+0x5cefc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a40b6c",
      "incomplete_value": false,
      "site": "00a40b6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:258:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e3c70",
      "incomplete_value": false,
      "site": "009e3c70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:c38:8"
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
      "00a40b6c",
      "DATA",
      [
        "storage",
        "00c0bc38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a40b6c",
      "DATA",
      [
        "storage",
        "00c8b258",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e3c60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e3/009e3c4c.md#insn-009e3c60) · [`009e3c68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e3/009e3c4c.md#insn-009e3c68) · [`009e3c6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e3/009e3c4c.md#insn-009e3c6c)
- 新版 [`00a40b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a40/00a40b48.md#insn-00a40b5c) · [`00a40b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a40/00a40b48.md#insn-00a40b64) · [`00a40b68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a40/00a40b48.md#insn-00a40b68)

~~~diff
- 009e3c60 ["INT_ADD", "register:40f0:8", ["const:9e3c60:8", "const:4:8"]]
- 009e3c60 ["CALL", null, ["callee:00c57a90:8"]]
+ 00a40b5c ["INT_ADD", "register:40f0:8", ["const:a40b5c:8", "const:4:8"]]
+ 00a40b5c ["CALL", null, ["callee:00c57a90:8"]]
- 009e3c60 bytes f8dc0794
+ 00a40b5c bytes cd5b0894
- 009e3c68 ["COPY", "register:4040:8", ["const:c0b000:8"]]
+ 00a40b64 ["COPY", "register:4040:8", ["const:c8b000:8"]]
- 009e3c68 bytes 48110090
+ 00a40b64 bytes 481200f0
- 009e3c6c ["COPY", "tmp:0:8", ["const:c38:8"]]
- 009e3c6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009e3c6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009e3c6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a40b68 ["COPY", "tmp:0:8", ["const:258:8"]]
+ 00a40b68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a40b68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a40b68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009e3c6c bytes 08e13091
+ 00a40b68 bytes 08610991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8d85a4e4af28b424b7c6d346697eef1"></a>

### [`009e3c9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e3/009e3c9c.md) → [`00a40b98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a40/00a40b98.md) FUN_00a40b98

採用 · 移動量 `+0x5cefc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`009e3e04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e3/009e3e04.md) [`009e3e08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e3/009e3e08.md) [`00a6b404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6b/00a6b404.md) [`00a6ca44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6c/00a6ca44.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00a40d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a40/00a40d00.md) [`00a40d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a40/00a40d04.md) [`00ac9398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac9/00ac9398.md) [`00aca9d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00aca9d8.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a40bd8",
      "incomplete_value": false,
      "site": "00a40bd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:2c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e3cdc",
      "incomplete_value": false,
      "site": "009e3cdc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:ca8:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a40be8",
      "value": [
        "leaf",
        "ram:aca9d8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009e3cec",
      "value": [
        "leaf",
        "ram:a6ca44:8"
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
      "00a40bd8",
      "DATA",
      [
        "storage",
        "00c0bca8",
        null,
        "undefined *"
      ]
    ],
    [
      "00a40be8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a6ca44"
      ]
    ],
    [
      "00a40c10",
      "READ",
      [
        "storage",
        "00c0bcc8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00a40bd8",
      "DATA",
      [
        "storage",
        "00c8b2c8",
        null,
        "undefined *"
      ]
    ],
    [
      "00a40be8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00aca9d8"
      ]
    ],
    [
      "00a40c10",
      "READ",
      [
        "storage",
        "00c8b2e8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e3cec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e3/009e3c9c.md#insn-009e3cec) · [`009e3cb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e3/009e3c9c.md#insn-009e3cb4) · [`009e3ccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e3/009e3c9c.md#insn-009e3ccc)
- 新版 [`00a40be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a40/00a40b98.md#insn-00a40be8) · [`00a40bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a40/00a40b98.md#insn-00a40bb0) · [`00a40bc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a40/00a40b98.md#insn-00a40bc8)

~~~diff
- 009e3cec ["INT_ADD", "register:40f0:8", ["const:9e3cec:8", "const:4:8"]]
- 009e3cec ["CALL", null, ["ram:a6ca44:8"]]
+ 00a40be8 ["INT_ADD", "register:40f0:8", ["const:a40be8:8", "const:4:8"]]
+ 00a40be8 ["CALL", null, ["ram:aca9d8:8"]]
- 009e3cec bytes 56230294
+ 00a40be8 bytes 7c270294
- 009e3cb4 ["COPY", "register:40b0:8", ["const:3cf0:8"]]
+ 00a40bb0 ["COPY", "register:40b0:8", ["const:7d90:8"]]
- 009e3cb4 bytes 169e8752
+ 00a40bb0 bytes 16b28f52
- 009e3ccc ["INT_ADD", "register:40f0:8", ["const:9e3ccc:8", "const:4:8"]]
- 009e3ccc ["CALL", null, ["callee:00ac9398:8"]]
+ 00a40bc8 ["INT_ADD", "register:40f0:8", ["const:a40bc8:8", "const:4:8"]]
+ 00a40bc8 ["CALL", null, ["callee:00ac9398:8"]]
- 009e3ccc bytes ce1d0294
+ 00a40bc8 bytes f4210294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76d1e28e8efa07ff9caae04cc60dbc41"></a>

### [`009e3df0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e3/009e3df0.md) → [`00a40cec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a40/00a40cec.md) FUN_00a40cec

採用 · 移動量 `+0x5cefc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a40cf8",
      "incomplete_value": false,
      "site": "00a40cf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:2c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e3dfc",
      "incomplete_value": false,
      "site": "009e3dfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:ca8:8"
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
      "00a40cf8",
      "DATA",
      [
        "storage",
        "00c0bca8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a40cf8",
      "DATA",
      [
        "storage",
        "00c8b2c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e3df4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e3/009e3df0.md#insn-009e3df4) · [`009e3df8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e3/009e3df0.md#insn-009e3df8)
- 新版 [`00a40cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a40/00a40cec.md#insn-00a40cf0) · [`00a40cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a40/00a40cec.md#insn-00a40cf4)

~~~diff
- 009e3df4 ["COPY", "register:4048:8", ["const:c0b000:8"]]
+ 00a40cf0 ["COPY", "register:4048:8", ["const:c8b000:8"]]
- 009e3df4 bytes 49110090
+ 00a40cf0 bytes 491200f0
- 009e3df8 ["COPY", "tmp:0:8", ["const:ca8:8"]]
- 009e3df8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 009e3df8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 009e3df8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a40cf4 ["COPY", "tmp:0:8", ["const:2c8:8"]]
+ 00a40cf4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a40cf4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a40cf4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 009e3df8 bytes 29a13291
+ 00a40cf4 bytes 29210b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-649f120556fd425454fa04e0b7f7403a"></a>

### [`009e3f00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e3/009e3f00.md) → [`00a40dfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a40/00a40dfc.md) _INIT_214

採用 · 移動量 `+0x5cefc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 80.23% / 新版 80.23%

CFGの説明率　旧版 80.00% / 新版 70.59%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009e3f30"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009e3f58"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009e3f7c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009e3f30",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:009e3f3c",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "unmatched:009e3f58",
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
      "00a40e2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00a40e38",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00a40e54",
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

- 旧版 [`009e3f30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e3/009e3f00.md#insn-009e3f30) · [`009e3f58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e3/009e3f00.md#insn-009e3f58) · [`009e3f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e3/009e3f00.md#insn-009e3f7c)

~~~diff
- 009e3f30 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 009e3f30 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 009e3f30 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 009e3f30 bytes a9831ff8
- 009e3f58 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:11:8"]]
- 009e3f58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 009e3f58 bytes e013813c
- 009e3f7c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:31:8"]]
- 009e3f7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 009e3f7c bytes e013833c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93487c917e0648a64b53705ebfb63fe1"></a>

### [`009e44b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e4/009e44b8.md) → [`00a413b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a41/00a413b4.md) FUN_00a413b4

採用 · 移動量 `+0x5cefc` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00ac9098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9098.md) · 呼出先 20件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md)
- 新版 呼出元 1件 [`00b28b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b28/00b28b2c.md) · 呼出先 20件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`004878dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878dc.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 87.95% / 新版 87.95%

CFGの説明率　旧版 78.57% / 新版 71.60%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 1件, `store_condition` 2件, `store_value` 1件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009e44e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009e44ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009e4504"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009e44e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x260]",
        null,
        null
      ]
    ],
    [
      "unmatched:009e44ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "unmatched:009e44f0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00487de0"
      ]
    ]
  ],
  "added": [
    [
      "00a413e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x260]",
        null,
        null
      ]
    ],
    [
      "00a413e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "00a413ec",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00487de0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e44e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e4/009e44b8.md#insn-009e44e4) · [`009e44ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e4/009e44b8.md#insn-009e44ec) · [`009e4504`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e4/009e44b8.md#insn-009e4504)

~~~diff
- 009e44e4 ["COPY", "tmp:0:8", ["register:8:8"]]
- 009e44e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 009e44e4 bytes e80300f9
- 009e44ec ["COPY", "tmp:0:8", ["register:4040:8"]]
- 009e44ec ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff0:8"]]
- 009e44ec ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 009e44ec bytes a8031ff8
- 009e4504 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:98:8"]]
- 009e4504 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 009e4504 bytes e84f00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df2370807b4d98ef2a6c9354553ace42"></a>

### [`009e4e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e4/009e4e14.md) → [`00a41d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a41/00a41d10.md) FUN_00a41d10

採用 · 移動量 `+0x5cefc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 60.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009e4e28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e4/009e4e14.md#insn-009e4e28) · [`009e4e30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e4/009e4e14.md#insn-009e4e30) · [`009e4e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e4/009e4e14.md#insn-009e4e38)
- 新版 [`00a41d24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a41/00a41d10.md#insn-00a41d24) · [`00a41d2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a41/00a41d10.md#insn-00a41d2c) · [`00a41d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a41/00a41d10.md#insn-00a41d34)

~~~diff
- 009e4e28 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 009e4e28 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 009e4e28 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 009e4e28 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
+ 00a41d24 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
+ 00a41d24 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00a41d24 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00a41d24 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 009e4e28 bytes 68000036
+ 00a41d24 bytes 68000036
- 009e4e30 ["INT_ADD", "register:40f0:8", ["const:9e4e30:8", "const:4:8"]]
- 009e4e30 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00a41d2c ["INT_ADD", "register:40f0:8", ["const:a41d2c:8", "const:4:8"]]
+ 00a41d2c ["CALL", null, ["callee:00c57ab0:8"]]
- 009e4e30 bytes 8cd80794
+ 00a41d2c bytes 61570894
- 009e4e38 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 009e4e38 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00a41d34 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00a41d34 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 009e4e38 bytes a00000b4
+ 00a41d34 bytes a00000b4
~~~


<a id="compare-d904fc199937e771cdcff0aa18fea051"></a>

### [`009e4f3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e4/009e4f3c.md) → [`00a41e38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a41/00a41e38.md) FUN_00a41e38

採用 · 移動量 `+0x5cefc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 19件 [`0059815c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00598/0059815c.md) [`005bc910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bc910.md) [`005d0a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d0/005d0a68.md) [`006a7120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a7/006a7120.md) [`0072f3c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072f/0072f3c8.md) · 呼出先 4件 [`007cf4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cf4b0.md) [`007cf950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cf950.md) [`007cfaa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cfaa0.md) [`007cfcd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cfcd8.md)
- 新版 呼出元 19件 [`005bc78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bc/005bc78c.md) [`005e15e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e15e0.md) [`005f5750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f5/005f5750.md) [`006d0264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d0/006d0264.md) [`0075959c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00759/0075959c.md) · 呼出先 4件 [`00802678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802678.md) [`00802b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802b18.md) [`00802c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802c68.md) [`00802ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802ea0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 62.86% / 新版 62.86%

CFGの説明率　旧版 40.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 4件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a41e48",
      "value": [
        "leaf",
        "ram:802678:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009e4f4c",
      "value": [
        "leaf",
        "ram:7cf4b0:8"
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
      "site": "00a41e54",
      "value": [
        "leaf",
        "ram:802678:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009e4f58",
      "value": [
        "leaf",
        "ram:7cf4b0:8"
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
      "site": "00a41e64",
      "value": [
        "leaf",
        "ram:802678:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009e4f68",
      "value": [
        "leaf",
        "ram:7cf4b0:8"
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
      "00a41e48",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007cf4b0"
      ]
    ],
    [
      "00a41e54",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007cf4b0"
      ]
    ],
    [
      "00a41e64",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007cf4b0"
      ]
    ]
  ],
  "added": [
    [
      "00a41e48",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00802678"
      ]
    ],
    [
      "00a41e54",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00802678"
      ]
    ],
    [
      "00a41e64",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00802678"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e4f4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e4/009e4f3c.md#insn-009e4f4c) · [`009e4f58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e4/009e4f3c.md#insn-009e4f58) · [`009e4f68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e4/009e4f3c.md#insn-009e4f68)
- 新版 [`00a41e48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a41/00a41e38.md#insn-00a41e48) · [`00a41e54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a41/00a41e38.md#insn-00a41e54) · [`00a41e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a41/00a41e38.md#insn-00a41e64)

~~~diff
- 009e4f4c ["INT_ADD", "register:40f0:8", ["const:9e4f4c:8", "const:4:8"]]
- 009e4f4c ["CALL", null, ["ram:7cf4b0:8"]]
+ 00a41e48 ["INT_ADD", "register:40f0:8", ["const:a41e48:8", "const:4:8"]]
+ 00a41e48 ["CALL", null, ["ram:802678:8"]]
- 009e4f4c bytes 59a9f797
+ 00a41e48 bytes 0c02f797
- 009e4f58 ["INT_ADD", "register:40f0:8", ["const:9e4f58:8", "const:4:8"]]
- 009e4f58 ["CALL", null, ["ram:7cf4b0:8"]]
+ 00a41e54 ["INT_ADD", "register:40f0:8", ["const:a41e54:8", "const:4:8"]]
+ 00a41e54 ["CALL", null, ["ram:802678:8"]]
- 009e4f58 bytes 56a9f797
+ 00a41e54 bytes 0902f797
- 009e4f68 ["INT_ADD", "register:40f0:8", ["const:9e4f68:8", "const:4:8"]]
- 009e4f68 ["CALL", null, ["ram:7cf4b0:8"]]
+ 00a41e64 ["INT_ADD", "register:40f0:8", ["const:a41e64:8", "const:4:8"]]
+ 00a41e64 ["CALL", null, ["ram:802678:8"]]
- 009e4f68 bytes 52a9f797
+ 00a41e64 bytes 0502f797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7fe46eea47fb92b24e840cf4f484d894"></a>

### [`009e4fc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e4/009e4fc8.md) → [`00a41ec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a41/00a41ec4.md) FUN_00a41ec4

採用 · 移動量 `+0x5cefc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 16件 [`0059815c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00598/0059815c.md) [`005bc910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bc910.md) [`005d0a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d0/005d0a68.md) [`006a7120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a7/006a7120.md) [`0072f3c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072f/0072f3c8.md) · 呼出先 2件 [`006440f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00644/006440f0.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)
- 新版 呼出元 16件 [`005bc78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bc/005bc78c.md) [`005e15e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e15e0.md) [`005f5750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f5/005f5750.md) [`006d0264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d0/006d0264.md) [`0075959c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00759/0075959c.md) · 呼出先 2件 [`0066a3c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066a/0066a3c8.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, operands_and_dependencies, operation_sequence

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 76.47% / 新版 65.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "009e4fe8",
      "incomplete_value": true,
      "site": "009e5004",
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
            "const:690:8"
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
      "definition_site": "009e5010",
      "incomplete_value": true,
      "site": "009e501c",
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
            "const:690:8"
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
      "definition_site": "009e5014",
      "incomplete_value": true,
      "site": "009e501c",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "INT_ADD",
            "4",
            [
              [
                "live",
                "register:40b0:4"
              ],
              [
                "live",
                "register:40a8:4"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`009e5004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e4/009e4fc8.md#insn-009e5004) · [`009e501c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e4/009e4fc8.md#insn-009e501c) · [`009e5034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e4/009e4fc8.md#insn-009e5034)
- 新版 [`00a41f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a41/00a41ec4.md#insn-00a41f00) · [`00a41f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a41/00a41ec4.md#insn-00a41f18) · [`00a41f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a41/00a41ec4.md#insn-00a41f30)

~~~diff
- 009e5004 ["INT_ADD", "register:40f0:8", ["const:9e5004:8", "const:4:8"]]
- 009e5004 ["CALL", null, ["callee:0066a3c8:8"]]
+ 00a41f00 ["INT_ADD", "register:40f0:8", ["const:a41f00:8", "const:4:8"]]
+ 00a41f00 ["CALL", null, ["callee:0066a3c8:8"]]
- 009e5004 bytes 3b7cf197
+ 00a41f00 bytes 32a1f097
- 009e501c ["INT_ADD", "register:40f0:8", ["const:9e501c:8", "const:4:8"]]
- 009e501c ["CALL", null, ["callee:0066a3c8:8"]]
+ 00a41f18 ["INT_ADD", "register:40f0:8", ["const:a41f18:8", "const:4:8"]]
+ 00a41f18 ["CALL", null, ["callee:0066a3c8:8"]]
- 009e501c bytes 357cf197
+ 00a41f18 bytes 2ca1f097
- 009e5034 ["INT_ADD", "register:40f0:8", ["const:9e5034:8", "const:4:8"]]
- 009e5034 ["CALL", null, ["callee:0066a3c8:8"]]
+ 00a41f30 ["INT_ADD", "register:40f0:8", ["const:a41f30:8", "const:4:8"]]
+ 00a41f30 ["CALL", null, ["callee:0066a3c8:8"]]
- 009e5034 bytes 2f7cf197
+ 00a41f30 bytes 26a1f097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46e86a3b3695b0f9102e0f02c6b40778"></a>

### [`009e50a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e5/009e50a0.md) → [`00a41f9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a41/00a41f9c.md) FUN_00a41f9c

採用 · 移動量 `+0x5cefc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 7件 [`005bc910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bc910.md) [`005d0a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d0/005d0a68.md) [`00a788d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a78/00a788d0.md) [`00a80570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a80/00a80570.md) [`00a823d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a82/00a823d8.md) · 呼出先 14件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0047c518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c518.md) [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md) [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0063e4a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063e4a8.md)
- 新版 呼出元 7件 [`005e15e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e15e0.md) [`005f5750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f5/005f5750.md) [`00ad6d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad6/00ad6d50.md) [`00adee94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ade/00adee94.md) [`00ae0e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ae0/00ae0e64.md) · 呼出先 14件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0049f3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3b0.md) [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`00664780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664780.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 72.43% / 新版 72.43%

CFGの説明率　旧版 42.33% / 新版 30.13%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_condition` 1件, `unresolved_branch_alignment` 16件, `unresolved_call_alignment` 14件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009e5400"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009e540c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009e5410"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a41ffc",
      "DATA",
      [
        "storage",
        "0039781c",
        null,
        "uleb128"
      ]
    ],
    [
      "unmatched:009e515c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0063eaf8"
      ]
    ],
    [
      "unmatched:009e5164",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514b8"
      ]
    ]
  ],
  "added": [
    [
      "00a41ffc",
      "DATA",
      [
        "storage",
        "0039b97c",
        null,
        "dword"
      ]
    ],
    [
      "00a42058",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00664dd0"
      ]
    ],
    [
      "00a42060",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514b8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e5200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e5/009e50a0.md#insn-009e5200) · [`009e527c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e5/009e50a0.md#insn-009e527c) · [`009e5284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e5/009e50a0.md#insn-009e5284)

~~~diff
- 009e5200 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 009e5200 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 009e5200 bytes e8010034
- 009e527c ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 009e527c ["COPY", "tmp:1:8", ["register:4040:8"]]
- 009e527c ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 009e527c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 009e527c bytes 19b1899a
- 009e5284 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 009e5284 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 009e5284 bytes a1000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71f7b7439deddf2d95bf7bcdc7c84150"></a>

### [`009e57fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e5/009e57fc.md) → [`00a426f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a42/00a426f8.md) FUN_00a426f8

採用 · 移動量 `+0x5cefc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`005d0508`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d0/005d0508.md) [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) [`006ee6c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ee/006ee6c8.md) · 呼出先 4件 [`005bc1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bc1dc.md) [`0063e4a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063e4a8.md) [`00a93f4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a93/00a93f4c.md) [`00a9400c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a94/00a9400c.md)
- 新版 呼出元 3件 [`005f51f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f5/005f51f0.md) [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) [`00718734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00718/00718734.md) · 呼出先 4件 [`005e0eac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0eac.md) [`00664780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664780.md) [`00af34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af3/00af34c8.md) [`00af3588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af3/00af3588.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a4272c",
      "value": [
        "leaf",
        "ram:af34c8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009e5830",
      "value": [
        "leaf",
        "ram:a93f4c:8"
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
      "site": "00a42754",
      "value": [
        "leaf",
        "ram:af3588:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009e5858",
      "value": [
        "leaf",
        "ram:a9400c:8"
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
      "site": "00a42758",
      "value": [
        "leaf",
        "ram:664780:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009e585c",
      "value": [
        "leaf",
        "ram:63e4a8:8"
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
      "00a4272c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a93f4c"
      ]
    ],
    [
      "00a42754",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a9400c"
      ]
    ],
    [
      "00a42758",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0063e4a8"
      ]
    ]
  ],
  "added": [
    [
      "00a4272c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00af34c8"
      ]
    ],
    [
      "00a42754",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00af3588"
      ]
    ],
    [
      "00a42758",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00664780"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e5830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e5/009e57fc.md#insn-009e5830) · [`009e5858`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e5/009e57fc.md#insn-009e5858) · [`009e585c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e5/009e57fc.md#insn-009e585c)
- 新版 [`00a4272c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a42/00a426f8.md#insn-00a4272c) · [`00a42754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a42/00a426f8.md#insn-00a42754) · [`00a42758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a42/00a426f8.md#insn-00a42758)

~~~diff
- 009e5830 ["INT_ADD", "register:40f0:8", ["const:9e5830:8", "const:4:8"]]
- 009e5830 ["CALL", null, ["ram:a93f4c:8"]]
+ 00a4272c ["INT_ADD", "register:40f0:8", ["const:a4272c:8", "const:4:8"]]
+ 00a4272c ["CALL", null, ["ram:af34c8:8"]]
- 009e5830 bytes c7b90294
+ 00a4272c bytes 67c30294
- 009e5858 ["INT_ADD", "register:40f0:8", ["const:9e5858:8", "const:4:8"]]
- 009e5858 ["CALL", null, ["ram:a9400c:8"]]
+ 00a42754 ["INT_ADD", "register:40f0:8", ["const:a42754:8", "const:4:8"]]
+ 00a42754 ["CALL", null, ["ram:af3588:8"]]
- 009e5858 bytes edb90294
+ 00a42754 bytes 8dc30294
- 009e585c ["INT_ADD", "register:40f0:8", ["const:9e585c:8", "const:4:8"]]
- 009e585c ["CALL", null, ["ram:63e4a8:8"]]
+ 00a42758 ["INT_ADD", "register:40f0:8", ["const:a42758:8", "const:4:8"]]
+ 00a42758 ["CALL", null, ["ram:664780:8"]]
- 009e585c bytes 1363f197
+ 00a42758 bytes 0a88f097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1f5ea55a8653d247253c830bb90f6e3"></a>

### [`009e5880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e5/009e5880.md) → [`00a4277c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a42/00a4277c.md) FUN_00a4277c

採用 · 移動量 `+0x5cefc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`005d0a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d0/005d0a68.md) [`006ee6c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ee/006ee6c8.md) [`009f4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f4/009f4ab8.md) · 呼出先 8件 [`0047c518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c518.md) [`005bce08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bce08.md) [`005be130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005be/005be130.md) [`005c2720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2720.md) [`0063e4a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063e4a8.md)
- 新版 呼出元 3件 [`005f5750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f5/005f5750.md) [`00718734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00718/00718734.md) [`00a51dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a51/00a51dcc.md) · 呼出先 8件 [`0049f3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3b0.md) [`005e1ad8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e1ad8.md) [`005e2e00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e2/005e2e00.md) [`005e73f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73f0.md) [`00664780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664780.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 85.53% / 新版 85.53%

CFGの説明率　旧版 25.00% / 新版 22.73%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "009e58a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a427a8",
      "incomplete_value": true,
      "site": "00a427b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:778:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e58ac",
      "incomplete_value": true,
      "site": "009e58b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:690:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a427c8",
      "incomplete_value": true,
      "site": "00a427cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:2768:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e58cc",
      "incomplete_value": true,
      "site": "009e58d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:2678:8"
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
      "unmatched:009e58a4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00802b18"
      ]
    ],
    [
      "unmatched:009e591c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0063e4a8"
      ]
    ],
    [
      "unmatched:009e595c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00802b18"
      ]
    ]
  ],
  "added": [
    [
      "00a427a0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00802b18"
      ]
    ],
    [
      "00a42818",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00664780"
      ]
    ],
    [
      "00a42858",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00802b18"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e58a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e5/009e5880.md#insn-009e58a4) · [`009e58b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e5/009e5880.md#insn-009e58b4) · [`009e58d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e5/009e5880.md#insn-009e58d0)
- 新版 [`00a427b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a42/00a4277c.md#insn-00a427b0) · [`00a427cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a42/00a4277c.md#insn-00a427cc)

~~~diff
- 009e58a4 ["INT_ADD", "register:40f0:8", ["const:9e58a4:8", "const:4:8"]]
- 009e58a4 ["CALL", null, ["callee:00802b18:8"]]
- 009e58a4 bytes 2ba8f797
- 009e58b4 ["INT_ADD", "register:40f0:8", ["const:9e58b4:8", "const:4:8"]]
- 009e58b4 ["CALL", null, ["callee:0066a5dc:8"]]
+ 00a427b0 ["INT_ADD", "register:40f0:8", ["const:a427b0:8", "const:4:8"]]
+ 00a427b0 ["CALL", null, ["callee:0066a5dc:8"]]
- 009e58b4 bytes 947af197
+ 00a427b0 bytes 8b9ff097
- 009e58d0 ["INT_ADD", "register:40f0:8", ["const:9e58d0:8", "const:4:8"]]
- 009e58d0 ["CALL", null, ["callee:005e73f0:8"]]
+ 00a427cc ["INT_ADD", "register:40f0:8", ["const:a427cc:8", "const:4:8"]]
+ 00a427cc ["CALL", null, ["callee:005e73f0:8"]]
- 009e58d0 bytes 9473ef97
+ 00a427cc bytes 0993ee97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f534e4c23eb24f7916fc22b7fecc3426"></a>

### [`009e59b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e5/009e59b0.md) → [`00a428ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a42/00a428ac.md) FUN_00a428ac

採用 · 移動量 `+0x5cefc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 7件 [`0059815c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00598/0059815c.md) [`006a7120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a7/006a7120.md) [`0072f3c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072f/0072f3c8.md) [`00730204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00730/00730204.md) [`00a7268c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a72/00a7268c.md) · 呼出先 12件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0047c518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c518.md) [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md) [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0063e4a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063e4a8.md)
- 新版 呼出元 7件 [`005bc78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bc/005bc78c.md) [`006d0264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d0/006d0264.md) [`0075959c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00759/0075959c.md) [`0075a3d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075a/0075a3d8.md) [`00ad075c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad0/00ad075c.md) · 呼出先 12件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0049f3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3b0.md) [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`00664780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664780.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 66.10% / 新版 66.10%

CFGの説明率　旧版 17.59% / 新版 21.08%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `call_target` 1件, `store_condition` 1件, `unresolved_branch_alignment` 25件, `unresolved_call_alignment` 9件, `unresolved_store_alignment` 22件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009e59e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009e5c04"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009e5c04"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:009e59e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:009e59e4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00a41e38"
      ]
    ],
    [
      "unmatched:009e59f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a42930"
      ]
    ]
  ],
  "added": [
    [
      "00a428dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00a428e0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00a41e38"
      ]
    ],
    [
      "00a428f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a42930"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e59e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e5/009e59b0.md#insn-009e59e0) · [`009e5c04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e5/009e59b0.md#insn-009e5c04) · [`009e5c08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e5/009e59b0.md#insn-009e5c08)

~~~diff
- 009e59e0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 009e59e0 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 009e59e0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 009e59e0 bytes a8831ff8
- 009e5c04 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 009e5c04 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 009e5c04 ["COPY", "tmp:2:8", ["register:8:8"]]
- 009e5c04 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 009e5c04 bytes e05f00a9
- 009e5c08 ["COPY", "tmp:0:8", ["const:0:8"]]
- 009e5c08 ["COPY", "tmp:1:8", ["const:0:8"]]
- 009e5c08 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 009e5c08 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 009e5c08 bytes ffff01a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17694777d45204aece806bb814967d9e"></a>

### [`009e955c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e955c.md) → [`00a46458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46458.md) FUN_00a46458

採用 · 移動量 `+0x5cefc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`009e9508`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9508.md) [`009ea458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ea/009ea458.md) · 呼出先 4件 [`00444710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444710.md) [`0044ac14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044ac14.md) [`005a1ae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a1/005a1ae4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 2件 [`00a46404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46404.md) [`00a47354`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a47354.md) · 呼出先 4件 [`004675a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/004675a8.md) [`0046daac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046daac.md) [`005c6114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c6/005c6114.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 84.38% / 新版 84.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a46484",
      "incomplete_value": false,
      "site": "00a464ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:358:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e9588",
      "incomplete_value": false,
      "site": "009e95b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:d38:8"
          ]
        ]
      ]
    },
    "ordinal": 21,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a464c8",
      "incomplete_value": true,
      "site": "00a464dc",
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
      "definition_site": "009e95cc",
      "incomplete_value": true,
      "site": "009e95e0",
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
                "const:440:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 28,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a46518",
      "incomplete_value": false,
      "site": "00a46524",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:3b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e961c",
      "incomplete_value": false,
      "site": "009e9628",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:d90:8"
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
      "00a464ac",
      "DATA",
      [
        "storage",
        "00c0bd38",
        null,
        "undefined *"
      ]
    ],
    [
      "00a464bc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00444710"
      ]
    ],
    [
      "00a464c8",
      "READ",
      [
        "storage",
        "002b1440",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00a464ac",
      "DATA",
      [
        "storage",
        "00c8b358",
        null,
        "undefined *"
      ]
    ],
    [
      "00a464bc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "004675a8"
      ]
    ],
    [
      "00a464c8",
      "READ",
      [
        "storage",
        "002c2a90",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e95c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e955c.md#insn-009e95c0) · [`009e9574`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e955c.md#insn-009e9574) · [`009e9584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e955c.md#insn-009e9584)
- 新版 [`00a464bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46458.md#insn-00a464bc) · [`00a46470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46458.md#insn-00a46470) · [`00a46480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46458.md#insn-00a46480)

~~~diff
- 009e95c0 ["INT_ADD", "register:40f0:8", ["const:9e95c0:8", "const:4:8"]]
- 009e95c0 ["CALL", null, ["ram:444710:8"]]
+ 00a464bc ["INT_ADD", "register:40f0:8", ["const:a464bc:8", "const:4:8"]]
+ 00a464bc ["CALL", null, ["ram:4675a8:8"]]
- 009e95c0 bytes 546ce997
+ 00a464bc bytes 3b84e897
- 009e9574 ["INT_ADD", "register:40f0:8", ["const:9e9574:8", "const:4:8"]]
- 009e9574 ["CALL", null, ["callee:00c57a90:8"]]
+ 00a46470 ["INT_ADD", "register:40f0:8", ["const:a46470:8", "const:4:8"]]
+ 00a46470 ["CALL", null, ["callee:00c57a90:8"]]
- 009e9574 bytes b3c60794
+ 00a46470 bytes 88450894
- 009e9584 ["COPY", "register:4040:8", ["const:c0b000:8"]]
+ 00a46480 ["COPY", "register:4040:8", ["const:c8b000:8"]]
- 009e9584 bytes 081100d0
+ 00a46480 bytes 281200b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32393bb04578786bd46b0766e213a38f"></a>

### [`009e9930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9930.md) → [`00a4682c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a4682c.md) FUN_00a4682c

採用 · 移動量 `+0x5cefc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 5件 [`009e9808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9808.md) [`009e9bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9bd4.md) [`009e9cf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9cf4.md) [`009e9de4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9de4.md) [`009e9ecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9ecc.md) · 呼出先 4件 [`00444710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444710.md) [`0044ac14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044ac14.md) [`005a1ae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a1/005a1ae4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 5件 [`00a46704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46704.md) [`00a46ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46ad0.md) [`00a46bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46bf0.md) [`00a46ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46ce0.md) [`00a46dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46dc8.md) · 呼出先 4件 [`004675a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/004675a8.md) [`0046daac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046daac.md) [`005c6114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c6/005c6114.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a46858",
      "incomplete_value": false,
      "site": "00a4687c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:358:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e995c",
      "incomplete_value": false,
      "site": "009e9980",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:d38:8"
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
      "definition_site": "00a46898",
      "incomplete_value": true,
      "site": "00a468ac",
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
      "definition_site": "009e999c",
      "incomplete_value": true,
      "site": "009e99b0",
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
                "const:440:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 27,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a468e8",
      "incomplete_value": false,
      "site": "00a468f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:3b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e99ec",
      "incomplete_value": false,
      "site": "009e99f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:d90:8"
          ]
        ]
      ]
    },
    "ordinal": 34,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a4687c",
      "DATA",
      [
        "storage",
        "00c0bd38",
        null,
        "undefined *"
      ]
    ],
    [
      "00a4688c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00444710"
      ]
    ],
    [
      "00a46898",
      "READ",
      [
        "storage",
        "002b1440",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00a4687c",
      "DATA",
      [
        "storage",
        "00c8b358",
        null,
        "undefined *"
      ]
    ],
    [
      "00a4688c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "004675a8"
      ]
    ],
    [
      "00a46898",
      "READ",
      [
        "storage",
        "002c2a90",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e9990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9930.md#insn-009e9990) · [`009e9948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9930.md#insn-009e9948) · [`009e9958`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9930.md#insn-009e9958)
- 新版 [`00a4688c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a4682c.md#insn-00a4688c) · [`00a46844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a4682c.md#insn-00a46844) · [`00a46854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a4682c.md#insn-00a46854)

~~~diff
- 009e9990 ["INT_ADD", "register:40f0:8", ["const:9e9990:8", "const:4:8"]]
- 009e9990 ["CALL", null, ["ram:444710:8"]]
+ 00a4688c ["INT_ADD", "register:40f0:8", ["const:a4688c:8", "const:4:8"]]
+ 00a4688c ["CALL", null, ["ram:4675a8:8"]]
- 009e9990 bytes 606be997
+ 00a4688c bytes 4783e897
- 009e9948 ["INT_ADD", "register:40f0:8", ["const:9e9948:8", "const:4:8"]]
- 009e9948 ["CALL", null, ["callee:00c57a90:8"]]
+ 00a46844 ["INT_ADD", "register:40f0:8", ["const:a46844:8", "const:4:8"]]
+ 00a46844 ["CALL", null, ["callee:00c57a90:8"]]
- 009e9948 bytes bec50794
+ 00a46844 bytes 93440894
- 009e9958 ["COPY", "register:4040:8", ["const:c0b000:8"]]
+ 00a46854 ["COPY", "register:4040:8", ["const:c8b000:8"]]
- 009e9958 bytes 081100d0
+ 00a46854 bytes 281200b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17f06d84f81cc2169ee3ca2dbb401da7"></a>

### [`009e9de4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9de4.md) → [`00a46ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46ce0.md) FUN_00a46ce0

採用 · 移動量 `+0x5cefc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`007f6a14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f6/007f6a14.md) · 呼出先 5件 [`009e9930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9930.md) [`009e9b40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9b40.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`0082be28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082b/0082be28.md) · 呼出先 5件 [`00a4682c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a4682c.md) [`00a46a3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46a3c.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 75.00% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "009e9e40",
      "incomplete_value": false,
      "site": "009e9e44",
      "value": [
        "leaf",
        "const:1:8"
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
      "definition_site": "009e9e3c",
      "incomplete_value": true,
      "site": "009e9e44",
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
            "const:8:8"
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

- 旧版 [`009e9e44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9de4.md#insn-009e9e44) · [`009e9e2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9de4.md#insn-009e9e2c) · [`009e9e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9de4.md#insn-009e9e38)
- 新版 [`00a46d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46ce0.md#insn-00a46d40) · [`00a46d28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46ce0.md#insn-00a46d28) · [`00a46d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46ce0.md#insn-00a46d34)

~~~diff
- 009e9e44 ["INT_ADD", "register:40f0:8", ["const:9e9e44:8", "const:4:8"]]
- 009e9e44 ["CALL", null, ["callee:00c538b0:8"]]
+ 00a46d40 ["INT_ADD", "register:40f0:8", ["const:a46d40:8", "const:4:8"]]
+ 00a46d40 ["CALL", null, ["callee:00c538b0:8"]]
- 009e9e44 bytes 07b40794
+ 00a46d40 bytes dc320894
- 009e9e2c ["INT_ADD", "register:40f0:8", ["const:9e9e2c:8", "const:4:8"]]
- 009e9e2c ["CALL", null, ["callee:00a4682c:8"]]
+ 00a46d28 ["INT_ADD", "register:40f0:8", ["const:a46d28:8", "const:4:8"]]
+ 00a46d28 ["CALL", null, ["callee:00a4682c:8"]]
- 009e9e2c bytes c1feff97
+ 00a46d28 bytes c1feff97
- 009e9e38 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 009e9e38 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00a46d34 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
+ 00a46d34 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 009e9e38 bytes 930000b4
+ 00a46d34 bytes 930000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db7bf4054776fd5e029beef925827d05"></a>

### [`009e9ecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9ecc.md) → [`00a46dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46dc8.md) FUN_00a46dc8

採用 · 移動量 `+0x5cefc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`0079942c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00799/0079942c.md) · 呼出先 9件 [`00467074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467074.md) [`00467080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467080.md) [`00467c68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467c68.md) [`00467c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467c70.md) [`009e9930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9930.md)
- 新版 呼出元 1件 [`007ca4e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ca/007ca4e8.md) · 呼出先 9件 [`00489f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f0c.md) [`00489f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f18.md) [`0048ab00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048ab00.md) [`0048ab08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048a/0048ab08.md) [`00a4682c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a4682c.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 85.71% / 新版 80.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009e9f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9ecc.md#insn-009e9f0c) · [`009e9f24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9ecc.md#insn-009e9f24) · [`009e9f3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9ecc.md#insn-009e9f3c)
- 新版 [`00a46e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46dc8.md#insn-00a46e08) · [`00a46e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46dc8.md#insn-00a46e20) · [`00a46e38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46dc8.md#insn-00a46e38)

~~~diff
- 009e9f0c ["INT_ADD", "register:40f0:8", ["const:9e9f0c:8", "const:4:8"]]
- 009e9f0c ["CALL", null, ["callee:00a4682c:8"]]
+ 00a46e08 ["INT_ADD", "register:40f0:8", ["const:a46e08:8", "const:4:8"]]
+ 00a46e08 ["CALL", null, ["callee:00a4682c:8"]]
- 009e9f0c bytes 89feff97
+ 00a46e08 bytes 89feff97
- 009e9f24 ["INT_ADD", "register:40f0:8", ["const:9e9f24:8", "const:4:8"]]
- 009e9f24 ["CALL", null, ["callee:00c538b0:8"]]
+ 00a46e20 ["INT_ADD", "register:40f0:8", ["const:a46e20:8", "const:4:8"]]
+ 00a46e20 ["CALL", null, ["callee:00c538b0:8"]]
- 009e9f24 bytes cfb30794
+ 00a46e20 bytes a4320894
- 009e9f3c ["INT_ADD", "register:40f0:8", ["const:9e9f3c:8", "const:4:8"]]
- 009e9f3c ["CALL", null, ["callee:00c538e0:8"]]
+ 00a46e38 ["INT_ADD", "register:40f0:8", ["const:a46e38:8", "const:4:8"]]
+ 00a46e38 ["CALL", null, ["callee:00c538e0:8"]]
- 009e9f3c bytes d5b30794
+ 00a46e38 bytes aa320894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8dc5853a893e5adde641eedcc518c6d0"></a>

### [`009ea540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ea/009ea540.md) → [`00a4743c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a4743c.md) FUN_00a4743c

採用 · 移動量 `+0x5cefc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`004447a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/004447a4.md) [`00444808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444808.md) [`00444840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444840.md) [`0044494c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/0044494c.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0046763c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/0046763c.md) [`004676a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/004676a0.md) [`004676d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/004676d8.md) [`004677e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/004677e4.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 96.59% / 新版 96.59%

CFGの説明率　旧版 96.15% / 新版 92.59%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009ea708"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a47604"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "009ea6ec",
      "incomplete_value": true,
      "site": "009ea718",
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
            "const:68:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`009ea708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ea/009ea540.md#insn-009ea708) · [`009ea718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ea/009ea540.md#insn-009ea718)
- 新版 [`00a47614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a4743c.md#insn-00a47614) · [`00a47604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a4743c.md#insn-00a47604)

~~~diff
- 009ea708 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:68:8"]]
- 009ea708 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5080:16"]]
- 009ea708 bytes 6482863c
- 009ea718 ["INT_ADD", "register:40f0:8", ["const:9ea718:8", "const:4:8"]]
- 009ea718 ["CALL", null, ["callee:004676a0:8"]]
+ 00a47614 ["INT_ADD", "register:40f0:8", ["const:a47614:8", "const:4:8"]]
+ 00a47614 ["CALL", null, ["callee:004676a0:8"]]
- 009ea718 bytes 3c68e997
+ 00a47614 bytes 2380e897
+ 00a47604 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:68:8"]]
+ 00a47604 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5080:16"]]
+ 00a47604 bytes 6482863c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dacbef3f1b9db72d78f3017384871bae"></a>

### [`009ea800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ea/009ea800.md) → [`00a476fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a476fc.md) FUN_00a476fc

採用 · 移動量 `+0x5cefc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c88.md) [`00446784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446784.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`00467b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467b20.md) [`0046961c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/0046961c.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 89.33% / 新版 89.33%

CFGの説明率　旧版 45.45% / 新版 35.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "009ea854",
      "incomplete_value": true,
      "site": "009ea858",
      "value": [
        "live",
        "register:40a0:8"
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "009ea874",
      "incomplete_value": true,
      "site": "009ea8a4",
      "value": [
        "live",
        "register:40a0:8"
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a47780",
      "incomplete_value": true,
      "site": "00a477a0",
      "value": [
        "TRUNC",
        "4",
        [
          [
            "live",
            "register:5000:4"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ea884",
      "incomplete_value": true,
      "site": "009ea8a4",
      "value": [
        "TRUNC",
        "4",
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
    "ordinal": 4,
    "slot": 4
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`009ea858`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ea/009ea800.md#insn-009ea858) · [`009ea8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ea/009ea800.md#insn-009ea8a4) · [`009ea820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ea/009ea800.md#insn-009ea820)
- 新版 [`00a47754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a476fc.md#insn-00a47754) · [`00a477a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a476fc.md#insn-00a477a0) · [`00a4771c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a476fc.md#insn-00a4771c)

~~~diff
- 009ea858 ["INT_ADD", "register:40f0:8", ["const:9ea858:8", "const:4:8"]]
- 009ea858 ["CALL", null, ["callee:00467aec:8"]]
+ 00a47754 ["INT_ADD", "register:40f0:8", ["const:a47754:8", "const:4:8"]]
+ 00a47754 ["CALL", null, ["callee:00467aec:8"]]
- 009ea858 bytes ff68e997
+ 00a47754 bytes e680e897
- 009ea8a4 ["INT_ADD", "register:40f0:8", ["const:9ea8a4:8", "const:4:8"]]
- 009ea8a4 ["CALL", null, ["callee:0046961c:8"]]
+ 00a477a0 ["INT_ADD", "register:40f0:8", ["const:a477a0:8", "const:4:8"]]
+ 00a477a0 ["CALL", null, ["callee:0046961c:8"]]
- 009ea8a4 bytes b86fe997
+ 00a477a0 bytes 9f87e897
- 009ea820 ["COPY", "register:0:8", ["register:4040:8"]]
- 009ea820 ["INT_ADD", "register:40f0:8", ["const:9ea820:8", "const:4:8"]]
- 009ea820 ["CALLIND", null, ["register:0:8"]]
+ 00a4771c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a4771c ["INT_ADD", "register:40f0:8", ["const:a4771c:8", "const:4:8"]]
+ 00a4771c ["CALLIND", null, ["register:0:8"]]
- 009ea820 bytes 00013fd6
+ 00a4771c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d52561da73f566433673b0dd68f2b04c"></a>

### [`009ea9a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ea/009ea9a8.md) → [`00a478a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a478a4.md) FUN_00a478a4

採用 · 移動量 `+0x5cefc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009e9690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9690.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00a4658c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a4658c.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "00a478b4",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009ea9b8",
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
      "definition_site": "00a478b0",
      "incomplete_value": false,
      "site": "00a478b4",
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
      "definition_site": "009ea9b4",
      "incomplete_value": false,
      "site": "009ea9b8",
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
      "00a478b0",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "00a478b4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "00a478b0",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "00a478b4",
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

- 旧版 [`009ea9b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ea/009ea9a8.md#insn-009ea9b8) · [`009ea9b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ea/009ea9a8.md#insn-009ea9b0) · [`009ea9b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ea/009ea9a8.md#insn-009ea9b4)
- 新版 [`00a478b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a478a4.md#insn-00a478b4) · [`00a478ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a478a4.md#insn-00a478ac) · [`00a478b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a478a4.md#insn-00a478b0)

~~~diff
- 009ea9b8 ["INT_ADD", "register:40f0:8", ["const:9ea9b8:8", "const:4:8"]]
- 009ea9b8 ["CALL", null, ["ram:418c38:8"]]
+ 00a478b4 ["INT_ADD", "register:40f0:8", ["const:a478b4:8", "const:4:8"]]
+ 00a478b4 ["CALL", null, ["ram:43b738:8"]]
- 009ea9b8 bytes a0b8e897
+ 00a478b4 bytes a1cfe797
- 009ea9b0 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 00a478ac ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 009ea9b0 bytes e0c5ffb0
+ 00a478ac bytes 80c3ff90
- 009ea9b4 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 009ea9b4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 009ea9b4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 009ea9b4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00a478b0 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 00a478b0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00a478b0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00a478b0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 009ea9b4 bytes 00740e91
+ 00a478b0 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e8e579b6e29c752389b52bb0315c4bc"></a>

### [`009ea9bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ea/009ea9bc.md) → [`00a478b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a478b8.md) FUN_00a478b8

採用 · 移動量 `+0x5cefc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`005a1ae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a1/005a1ae4.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 4件 [`005c6114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c6/005c6114.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a478dc",
      "incomplete_value": false,
      "site": "00a478e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:3b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ea9e0",
      "incomplete_value": false,
      "site": "009ea9e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:d90:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a47918",
      "incomplete_value": false,
      "site": "00a4791c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:358:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009eaa1c",
      "incomplete_value": false,
      "site": "009eaa20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:d38:8"
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
      "00a478e0",
      "DATA",
      [
        "storage",
        "00c0bd90",
        null,
        "undefined *"
      ]
    ],
    [
      "00a4791c",
      "DATA",
      [
        "storage",
        "00c0bd38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a478e0",
      "DATA",
      [
        "storage",
        "00c8b3b0",
        null,
        "undefined *"
      ]
    ],
    [
      "00a4791c",
      "DATA",
      [
        "storage",
        "00c8b358",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009ea9dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ea/009ea9bc.md#insn-009ea9dc) · [`009ea9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ea/009ea9bc.md#insn-009ea9e0) · [`009ea9f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ea/009ea9bc.md#insn-009ea9f4)
- 新版 [`00a478d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a478b8.md#insn-00a478d8) · [`00a478dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a478b8.md#insn-00a478dc) · [`00a478f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a478b8.md#insn-00a478f0)

~~~diff
- 009ea9dc ["COPY", "register:4040:8", ["const:c0b000:8"]]
+ 00a478d8 ["COPY", "register:4040:8", ["const:c8b000:8"]]
- 009ea9dc bytes 081100b0
+ 00a478d8 bytes 28120090
- 009ea9e0 ["COPY", "tmp:0:8", ["const:d90:8"]]
- 009ea9e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009ea9e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009ea9e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a478dc ["COPY", "tmp:0:8", ["const:3b0:8"]]
+ 00a478dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a478dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a478dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009ea9e0 bytes 08413691
+ 00a478dc bytes 08c10e91
- 009ea9f4 ["INT_ADD", "register:40f0:8", ["const:9ea9f4:8", "const:4:8"]]
- 009ea9f4 ["CALL", null, ["callee:00c538e0:8"]]
+ 00a478f0 ["INT_ADD", "register:40f0:8", ["const:a478f0:8", "const:4:8"]]
+ 00a478f0 ["CALL", null, ["callee:00c538e0:8"]]
- 009ea9f4 bytes 27b10794
+ 00a478f0 bytes fc2f0894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab49a0309fee75713c01df466029642d"></a>

### [`009eaa7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ea/009eaa7c.md) → [`00a47978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a47978.md) _INIT_216

採用 · 移動量 `+0x5cefc` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 81.36% / 新版 81.36%

CFGの説明率　旧版 73.33% / 新版 68.75%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_destination` 3件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a479b4",
      "incomplete_value": true,
      "site": "00a479d0",
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
                "const:ee6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009eaab8",
      "incomplete_value": true,
      "site": "009eaad4",
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
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:377:8"
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
      "definition_site": "00a479d8",
      "incomplete_value": true,
      "site": "00a479f4",
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
                "const:ef9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009eaadc",
      "incomplete_value": true,
      "site": "009eaaf8",
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
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:38a:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "00a479f8",
      "incomplete_value": true,
      "site": "00a47a14",
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
                "const:d82:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009eaafc",
      "incomplete_value": true,
      "site": "009eab18",
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
                "const:2a8000:8"
              ],
              [
                "leaf",
                "const:e0:8"
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
      "00a479b4",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00a479d8",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00a479f8",
      "READ",
      [
        "storage",
        "002a80e0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00a479b4",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00a479d8",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "00a479f8",
      "READ",
      [
        "storage",
        "002b8d82",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009eabdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ea/009eaa7c.md#insn-009eabdc) · [`009eacb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ea/009eaa7c.md#insn-009eacb0) · [`009eacdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ea/009eaa7c.md#insn-009eacdc)
- 新版 [`00a47ad8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a47978.md#insn-00a47ad8) · [`00a47bac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a47978.md#insn-00a47bac) · [`00a47bd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a47978.md#insn-00a47bd8)

~~~diff
- 009eabdc ["INT_ADD", "register:40f0:8", ["const:9eabdc:8", "const:4:8"]]
- 009eabdc ["CALL", null, ["callee:0043b7b8:8"]]
+ 00a47ad8 ["INT_ADD", "register:40f0:8", ["const:a47ad8:8", "const:4:8"]]
+ 00a47ad8 ["CALL", null, ["callee:0043b7b8:8"]]
- 009eabdc bytes 37b8e897
+ 00a47ad8 bytes 38cfe797
- 009eacb0 ["INT_ADD", "register:40f0:8", ["const:9eacb0:8", "const:4:8"]]
- 009eacb0 ["CALL", null, ["callee:00c57a30:8"]]
+ 00a47bac ["INT_ADD", "register:40f0:8", ["const:a47bac:8", "const:4:8"]]
+ 00a47bac ["CALL", null, ["callee:00c57a30:8"]]
- 009eacb0 bytes ccc00794
+ 00a47bac bytes a13f0894
- 009eacdc ["INT_ADD", "register:40f0:8", ["const:9eacdc:8", "const:4:8"]]
- 009eacdc ["CALL", null, ["callee:00c57ab0:8"]]
+ 00a47bd8 ["INT_ADD", "register:40f0:8", ["const:a47bd8:8", "const:4:8"]]
+ 00a47bd8 ["CALL", null, ["callee:00c57ab0:8"]]
- 009eacdc bytes e1c00794
+ 00a47bd8 bytes b63f0894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4665cfd2a75c70dfcc782c40cfca4ab2"></a>

### [`009f46cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f4/009f46cc.md) → [`00a519e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a51/00a519e0.md) FUN_00a519e0

採用 · 移動量 `+0x5d314` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) [`006eb464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006eb/006eb464.md) [`006ecae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ec/006ecae4.md) [`006eccf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ec/006eccf4.md) · 呼出先 12件 [`0044beb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044beb4.md) [`0044bf2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044bf2c.md) [`005bc1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bc1dc.md) [`005bde34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bd/005bde34.md) [`0065c134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065c/0065c134.md)
- 新版 呼出元 4件 [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) [`007154c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00715/007154c0.md) [`00716b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00716/00716b40.md) [`00716d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00716/00716d50.md) · 呼出先 12件 [`0046ed4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ed4c.md) [`0046edc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046edc4.md) [`005e0eac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0eac.md) [`005e2b04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e2/005e2b04.md) [`00682424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00682/00682424.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, constant, control_flow, control_flow_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 86.45% / 新版 86.45%

CFGの説明率　旧版 53.85% / 新版 58.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 11件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 9件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009f4a34"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a51d48"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "009f499c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a51a28",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a94278"
      ]
    ],
    [
      "00a51a38",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a94278"
      ]
    ],
    [
      "00a51a90",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a9481c"
      ]
    ]
  ],
  "added": [
    [
      "00a51a28",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00af37f4"
      ]
    ],
    [
      "00a51a38",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00af37f4"
      ]
    ],
    [
      "00a51a90",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00af3d98"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f4714`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f4/009f46cc.md#insn-009f4714) · [`009f4724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f4/009f46cc.md#insn-009f4724) · [`009f4788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f4/009f46cc.md#insn-009f4788)
- 新版 [`00a51a28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a51/00a519e0.md#insn-00a51a28) · [`00a51a38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a51/00a519e0.md#insn-00a51a38) · [`00a51a9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a51/00a519e0.md#insn-00a51a9c)

~~~diff
- 009f4714 ["INT_ADD", "register:40f0:8", ["const:9f4714:8", "const:4:8"]]
- 009f4714 ["CALL", null, ["ram:a94278:8"]]
+ 00a51a28 ["INT_ADD", "register:40f0:8", ["const:a51a28:8", "const:4:8"]]
+ 00a51a28 ["CALL", null, ["ram:af37f4:8"]]
- 009f4714 bytes d97e0294
+ 00a51a28 bytes 73870294
- 009f4724 ["INT_ADD", "register:40f0:8", ["const:9f4724:8", "const:4:8"]]
- 009f4724 ["CALL", null, ["ram:a94278:8"]]
+ 00a51a38 ["INT_ADD", "register:40f0:8", ["const:a51a38:8", "const:4:8"]]
+ 00a51a38 ["CALL", null, ["ram:af37f4:8"]]
- 009f4724 bytes d57e0294
+ 00a51a38 bytes 6f870294
- 009f4788 ["INT_ADD", "register:40f0:8", ["const:9f4788:8", "const:4:8"]]
- 009f4788 ["CALL", null, ["ram:a94278:8"]]
+ 00a51a9c ["INT_ADD", "register:40f0:8", ["const:a51a9c:8", "const:4:8"]]
+ 00a51a9c ["CALL", null, ["ram:af37f4:8"]]
- 009f4788 bytes bc7e0294
+ 00a51a9c bytes 56870294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-919027fedd5a70f5ebea70480da1db1f"></a>

### [`00a00bac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a00/00a00bac.md) → [`00a5e194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5e/00a5e194.md) FUN_00a5e194

採用 · 移動量 `+0x5d5e8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009f5650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f5/009f5650.md) · 呼出先 1件 [`0044c020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c020.md)
- 新版 呼出元 1件 [`00a52c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a52/00a52c38.md) · 呼出先 1件 [`0046eeb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046eeb8.md)

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 94.29% / 新版 94.29%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a5e21c",
      "incomplete_value": true,
      "site": "00a5e220",
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
            "const:690:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 10,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00a00c80"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a5e270",
      "incomplete_value": true,
      "site": "00a5e274",
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
            "const:b28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a00c88",
      "incomplete_value": true,
      "site": "00a00c8c",
      "value": [
        "live",
        "register:40a0:8"
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
      "unmatched:00a00c80",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0046eeb8"
      ]
    ]
  ],
  "added": [
    [
      "00a5e268",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0046eeb8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a00c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a00/00a00bac.md#insn-00a00c38) · [`00a00c80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a00/00a00bac.md#insn-00a00c80) · [`00a00c8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a00/00a00bac.md#insn-00a00c8c)
- 新版 [`00a5e220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5e/00a5e194.md#insn-00a5e220) · [`00a5e274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5e/00a5e194.md#insn-00a5e274)

~~~diff
- 00a00c38 ["INT_ADD", "register:40f0:8", ["const:a00c38:8", "const:4:8"]]
- 00a00c38 ["CALL", null, ["callee:0046eeb8:8"]]
+ 00a5e220 ["INT_ADD", "register:40f0:8", ["const:a5e220:8", "const:4:8"]]
+ 00a5e220 ["CALL", null, ["callee:0046eeb8:8"]]
- 00a00c38 bytes fa2ce997
+ 00a5e220 bytes 2643e897
- 00a00c80 ["INT_ADD", "register:40f0:8", ["const:a00c80:8", "const:4:8"]]
- 00a00c80 ["CALL", null, ["callee:0046eeb8:8"]]
- 00a00c80 bytes e82ce997
- 00a00c8c ["INT_ADD", "register:40f0:8", ["const:a00c8c:8", "const:4:8"]]
- 00a00c8c ["CALL", null, ["callee:0046eeb8:8"]]
+ 00a5e274 ["INT_ADD", "register:40f0:8", ["const:a5e274:8", "const:4:8"]]
+ 00a5e274 ["CALL", null, ["callee:0046eeb8:8"]]
- 00a00c8c bytes e52ce997
+ 00a5e274 bytes 1143e897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-995deed9756de9e9a81e827007d3c041"></a>

### [`00a00ce4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a00/00a00ce4.md) → [`00a5e2cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5e/00a5e2cc.md) FUN_00a5e2cc

採用 · 移動量 `+0x5d5e8` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009f5650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f5/009f5650.md) · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00756ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00756/00756ba0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00a52c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a52/00a52c38.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00781004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00781/00781004.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 98.33% / 新版 98.33%

CFGの説明率　旧版 55.56% / 新版 62.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a00d2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a5e314"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a5e330",
      "incomplete_value": true,
      "site": "00a5e338",
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
      "unmatched:00a00d2c",
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
      "00a5e314",
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

- 旧版 [`00a00d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a00/00a00ce4.md#insn-00a00d2c) · [`00a00d50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a00/00a00ce4.md#insn-00a00d50)
- 新版 [`00a5e338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5e/00a5e2cc.md#insn-00a5e338) · [`00a5e314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5e/00a5e2cc.md#insn-00a5e314)

~~~diff
- 00a00d2c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00a00d2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a00d2c bytes e80b00f9
- 00a00d50 ["INT_ADD", "register:40f0:8", ["const:a00d50:8", "const:4:8"]]
- 00a00d50 ["CALL", null, ["callee:0043bae0:8"]]
+ 00a5e338 ["INT_ADD", "register:40f0:8", ["const:a5e338:8", "const:4:8"]]
+ 00a5e338 ["CALL", null, ["callee:0043bae0:8"]]
- 00a00d50 bytes a460e897
+ 00a5e338 bytes ea75e797
+ 00a5e314 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
+ 00a5e314 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00a5e314 bytes e80b00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac6ef4190ab00ae50f2ef9ef135700ca"></a>

### [`00a010c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a01/00a010c8.md) → [`00a5e6b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5e/00a5e6b0.md) FUN_00a5e6b0

採用 · 移動量 `+0x5d5e8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 77.78% / 新版 87.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a01100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a01/00a010c8.md#insn-00a01100) · [`00a01114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a01/00a010c8.md#insn-00a01114) · [`00a0111c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a01/00a010c8.md#insn-00a0111c)
- 新版 [`00a5e6e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5e/00a5e6b0.md#insn-00a5e6e8) · [`00a5e6fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5e/00a5e6b0.md#insn-00a5e6fc) · [`00a5e704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5e/00a5e6b0.md#insn-00a5e704)

~~~diff
- 00a01100 ["INT_ADD", "register:40f0:8", ["const:a01100:8", "const:4:8"]]
- 00a01100 ["CALL", null, ["callee:00c538e0:8"]]
+ 00a5e6e8 ["INT_ADD", "register:40f0:8", ["const:a5e6e8:8", "const:4:8"]]
+ 00a5e6e8 ["CALL", null, ["callee:00c538e0:8"]]
- 00a01100 bytes 64570794
+ 00a5e6e8 bytes 7ed40794
- 00a01114 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a01114 ["INT_ADD", "register:40f0:8", ["const:a01114:8", "const:4:8"]]
- 00a01114 ["CALLIND", null, ["register:0:8"]]
+ 00a5e6fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a5e6fc ["INT_ADD", "register:40f0:8", ["const:a5e6fc:8", "const:4:8"]]
+ 00a5e6fc ["CALLIND", null, ["register:0:8"]]
- 00a01114 bytes 00013fd6
+ 00a5e6fc bytes 00013fd6
- 00a0111c ["INT_ADD", "register:40f0:8", ["const:a0111c:8", "const:4:8"]]
- 00a0111c ["CALL", null, ["callee:00c57a80:8"]]
+ 00a5e704 ["INT_ADD", "register:40f0:8", ["const:a5e704:8", "const:4:8"]]
+ 00a5e704 ["CALL", null, ["callee:00c57a80:8"]]
- 00a0111c bytes c5670794
+ 00a5e704 bytes dfe40794
~~~


<a id="compare-7e76d11ea01589809d7d419688464144"></a>

### [`00a01f6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a01/00a01f6c.md) → [`00a5f554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5f/00a5f554.md) FUN_00a5f554

採用 · 移動量 `+0x5d5e8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 3件 [`009eae0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ea/009eae0c.md) [`00a01134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a01/00a01134.md) [`00a01f6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a01/00a01f6c.md) · 呼出先 3件 [`0044b9cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b9cc.md) [`00a01f6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a01/00a01f6c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 3件 [`00a47d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a47d08.md) [`00a5e71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5e/00a5e71c.md) [`00a5f554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5f/00a5f554.md) · 呼出先 3件 [`0046e864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e864.md) [`00a5f554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5f/00a5f554.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 40.00% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00a01f90",
      "incomplete_value": true,
      "site": "00a01f94",
      "value": [
        "live",
        "register:40a0:8"
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
      "definition_site": "00a01f8c",
      "incomplete_value": true,
      "site": "00a01f94",
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
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00a01f98",
      "incomplete_value": true,
      "site": "00a01f9c",
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
            "const:38:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00a01f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a01/00a01f6c.md#insn-00a01f94) · [`00a01f9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a01/00a01f6c.md#insn-00a01f9c) · [`00a01f6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a01/00a01f6c.md#insn-00a01f6c)
- 新版 [`00a5f57c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5f/00a5f554.md#insn-00a5f57c) · [`00a5f584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5f/00a5f554.md#insn-00a5f584) · [`00a5f554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5f/00a5f554.md#insn-00a5f554)

~~~diff
- 00a01f94 ["INT_ADD", "register:40f0:8", ["const:a01f94:8", "const:4:8"]]
- 00a01f94 ["CALL", null, ["local:b0:8"]]
+ 00a5f57c ["INT_ADD", "register:40f0:8", ["const:a5f57c:8", "const:4:8"]]
+ 00a5f57c ["CALL", null, ["local:b0:8"]]
- 00a01f94 bytes f6ffff97
+ 00a5f57c bytes f6ffff97
- 00a01f9c ["INT_ADD", "register:40f0:8", ["const:a01f9c:8", "const:4:8"]]
- 00a01f9c ["CALL", null, ["callee:0046e864:8"]]
+ 00a5f584 ["INT_ADD", "register:40f0:8", ["const:a5f584:8", "const:4:8"]]
+ 00a5f584 ["CALL", null, ["callee:0046e864:8"]]
- 00a01f9c bytes 8c26e997
+ 00a5f584 bytes b83ce897
- 00a01f6c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00a01f6c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00a5f554 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00a5f554 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00a01f6c bytes a10200b4
+ 00a5f554 bytes a10200b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cca3334fa5b6af36d9dcd47be26751f3"></a>

### [`00a01fc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a01/00a01fc4.md) → [`00a5f5ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5f/00a5f5ac.md) FUN_00a5f5ac

採用 · 移動量 `+0x5d5e8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 3件 [`009eae0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ea/009eae0c.md) [`00a01134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a01/00a01134.md) [`00a01fc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a01/00a01fc4.md) · 呼出先 3件 [`0044c104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c104.md) [`00a01fc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a01/00a01fc4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 3件 [`00a47d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a47d08.md) [`00a5e71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5e/00a5e71c.md) [`00a5f5ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5f/00a5f5ac.md) · 呼出先 3件 [`0046ef9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ef9c.md) [`00a5f5ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5f/00a5f5ac.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 16.67% / 新版 6.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00a01fd8",
      "incomplete_value": true,
      "site": "00a01fe0",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00a01fe8",
      "incomplete_value": true,
      "site": "00a01fec",
      "value": [
        "live",
        "register:40a0:8"
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
      "definition_site": "00a01fe4",
      "incomplete_value": true,
      "site": "00a01fec",
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
    "ordinal": 1,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00a01fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a01/00a01fc4.md#insn-00a01fe0) · [`00a01fec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a01/00a01fc4.md#insn-00a01fec) · [`00a01ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a01/00a01fc4.md#insn-00a01ff4)
- 新版 [`00a5f5c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5f/00a5f5ac.md#insn-00a5f5c8) · [`00a5f5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5f/00a5f5ac.md#insn-00a5f5d4) · [`00a5f5dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5f/00a5f5ac.md#insn-00a5f5dc)

~~~diff
- 00a01fe0 ["INT_ADD", "register:40f0:8", ["const:a01fe0:8", "const:4:8"]]
- 00a01fe0 ["CALL", null, ["local:b0:8"]]
+ 00a5f5c8 ["INT_ADD", "register:40f0:8", ["const:a5f5c8:8", "const:4:8"]]
+ 00a5f5c8 ["CALL", null, ["local:b0:8"]]
- 00a01fe0 bytes f9ffff97
+ 00a5f5c8 bytes f9ffff97
- 00a01fec ["INT_ADD", "register:40f0:8", ["const:a01fec:8", "const:4:8"]]
- 00a01fec ["CALL", null, ["local:b0:8"]]
+ 00a5f5d4 ["INT_ADD", "register:40f0:8", ["const:a5f5d4:8", "const:4:8"]]
+ 00a5f5d4 ["CALL", null, ["local:b0:8"]]
- 00a01fec bytes f6ffff97
+ 00a5f5d4 bytes f6ffff97
- 00a01ff4 ["INT_ADD", "register:40f0:8", ["const:a01ff4:8", "const:4:8"]]
- 00a01ff4 ["CALL", null, ["callee:0046ef9c:8"]]
+ 00a5f5dc ["INT_ADD", "register:40f0:8", ["const:a5f5dc:8", "const:4:8"]]
+ 00a5f5dc ["CALL", null, ["callee:0046ef9c:8"]]
- 00a01ff4 bytes 4428e997
+ 00a5f5dc bytes 703ee897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-436c2e3bddc96c6f74eae56cbd9e6df0"></a>

### [`00a0201c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a0201c.md) → [`00a5f604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5f/00a5f604.md) FUN_00a5f604

採用 · 移動量 `+0x5d5e8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00a01134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a01/00a01134.md) [`00a0201c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a0201c.md) · 呼出先 4件 [`00a0201c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a0201c.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`00a5e71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5e/00a5e71c.md) [`00a5f604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5f/00a5f604.md) · 呼出先 4件 [`00a5f604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5f/00a5f604.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 94.29% / 新版 94.29%

CFGの説明率　旧版 58.33% / 新版 46.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00a02068",
      "incomplete_value": true,
      "site": "00a0206c",
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
                "register:4098:8"
              ],
              [
                "leaf",
                "const:30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00a02090"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00a5f678"
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
      "unmatched:00a02090",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00a5f678",
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

- 旧版 [`00a0206c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a0201c.md#insn-00a0206c) · [`00a02090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a0201c.md#insn-00a02090)
- 新版 [`00a5f654`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5f/00a5f604.md#insn-00a5f654) · [`00a5f678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5f/00a5f604.md#insn-00a5f678)

~~~diff
- 00a0206c ["INT_ADD", "register:40f0:8", ["const:a0206c:8", "const:4:8"]]
- 00a0206c ["CALL", null, ["callee:00c57ab0:8"]]
+ 00a5f654 ["INT_ADD", "register:40f0:8", ["const:a5f654:8", "const:4:8"]]
+ 00a5f654 ["CALL", null, ["callee:00c57ab0:8"]]
- 00a0206c bytes fd630794
+ 00a5f654 bytes 17e10794
- 00a02090 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a02090 ["INT_ADD", "register:40f0:8", ["const:a02090:8", "const:4:8"]]
- 00a02090 ["CALLIND", null, ["register:0:8"]]
- 00a02090 bytes 00013fd6
+ 00a5f678 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a5f678 ["INT_ADD", "register:40f0:8", ["const:a5f678:8", "const:4:8"]]
+ 00a5f678 ["CALLIND", null, ["register:0:8"]]
+ 00a5f678 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88e308a0405df81f5cd04a9c40e6d182"></a>

### [`00a020a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a020a8.md) → [`00a5f690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5f/00a5f690.md) FUN_00a5f690

採用 · 移動量 `+0x5d5e8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00a01134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a01/00a01134.md) [`00a020a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a020a8.md) · 呼出先 3件 [`0044c104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c104.md) [`00a020a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a020a8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`00a5e71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5e/00a5e71c.md) [`00a5f690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5f/00a5f690.md) · 呼出先 3件 [`0046ef9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ef9c.md) [`00a5f690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5f/00a5f690.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 33.33% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a5f6ac",
      "incomplete_value": true,
      "site": "00a5f6b0",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "old": {
      "definition_site": "00a020c4",
      "incomplete_value": true,
      "site": "00a020c8",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00a020d8",
      "incomplete_value": true,
      "site": "00a020dc",
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
            "const:28:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00a020c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a020a8.md#insn-00a020c8) · [`00a020dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a020a8.md#insn-00a020dc) · [`00a020a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a020a8.md#insn-00a020a8)
- 新版 [`00a5f6b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5f/00a5f690.md#insn-00a5f6b0) · [`00a5f6c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5f/00a5f690.md#insn-00a5f6c4) · [`00a5f690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5f/00a5f690.md#insn-00a5f690)

~~~diff
- 00a020c8 ["INT_ADD", "register:40f0:8", ["const:a020c8:8", "const:4:8"]]
- 00a020c8 ["CALL", null, ["local:b0:8"]]
+ 00a5f6b0 ["INT_ADD", "register:40f0:8", ["const:a5f6b0:8", "const:4:8"]]
+ 00a5f6b0 ["CALL", null, ["local:b0:8"]]
- 00a020c8 bytes f8ffff97
+ 00a5f6b0 bytes f8ffff97
- 00a020dc ["INT_ADD", "register:40f0:8", ["const:a020dc:8", "const:4:8"]]
- 00a020dc ["CALL", null, ["callee:0046ef9c:8"]]
+ 00a5f6c4 ["INT_ADD", "register:40f0:8", ["const:a5f6c4:8", "const:4:8"]]
+ 00a5f6c4 ["CALL", null, ["callee:0046ef9c:8"]]
- 00a020dc bytes 0a28e997
+ 00a5f6c4 bytes 363ee897
- 00a020a8 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00a020a8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00a5f690 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00a5f690 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00a020a8 bytes 410200b4
+ 00a5f690 bytes 410200b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ce06ad556c12b49defca88e14f9a2ca"></a>

### [`00a020f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a020f4.md) → [`00a5f6dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5f/00a5f6dc.md) FUN_00a5f6dc

採用 · 移動量 `+0x5d5e8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00a01134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a01/00a01134.md) [`00a020f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a020f4.md) · 呼出先 4件 [`00a020f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a020f4.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`00a5e71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5e/00a5e71c.md) [`00a5f6dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5f/00a5f6dc.md) · 呼出先 4件 [`00a5f6dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5f/00a5f6dc.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 28.57% / 新版 22.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00a02108",
      "incomplete_value": true,
      "site": "00a02110",
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
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00a02144"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00a5f72c"
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
      "unmatched:00a02144",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00a5f72c",
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

- 旧版 [`00a02110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a020f4.md#insn-00a02110) · [`00a02144`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a020f4.md#insn-00a02144)
- 新版 [`00a5f6f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5f/00a5f6dc.md#insn-00a5f6f8) · [`00a5f72c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5f/00a5f6dc.md#insn-00a5f72c)

~~~diff
- 00a02110 ["INT_ADD", "register:40f0:8", ["const:a02110:8", "const:4:8"]]
- 00a02110 ["CALL", null, ["local:b0:8"]]
+ 00a5f6f8 ["INT_ADD", "register:40f0:8", ["const:a5f6f8:8", "const:4:8"]]
+ 00a5f6f8 ["CALL", null, ["local:b0:8"]]
- 00a02110 bytes f9ffff97
+ 00a5f6f8 bytes f9ffff97
- 00a02144 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a02144 ["INT_ADD", "register:40f0:8", ["const:a02144:8", "const:4:8"]]
- 00a02144 ["CALLIND", null, ["register:0:8"]]
- 00a02144 bytes 00013fd6
+ 00a5f72c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a5f72c ["INT_ADD", "register:40f0:8", ["const:a5f72c:8", "const:4:8"]]
+ 00a5f72c ["CALLIND", null, ["register:0:8"]]
+ 00a5f72c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b575ee090df55822ea87bcb7c5587d24"></a>

### [`00a02178`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a02178.md) → [`00a5f760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5f/00a5f760.md) _INIT_217

採用 · 移動量 `+0x5d5e8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 78.53% / 新版 78.53%

CFGの説明率　旧版 41.03% / 新版 29.63%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a021a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a021bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a021c0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a021a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a021b4",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00a021bc",
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
      "00a5f790",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00a5f79c",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00a5f7a4",
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

- 旧版 [`00a021a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a02178.md#insn-00a021a8) · [`00a021bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a02178.md#insn-00a021bc) · [`00a021c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a02178.md#insn-00a021c0)

~~~diff
- 00a021a8 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00a021a8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00a021a8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a021a8 bytes a9831ff8
- 00a021bc ["COPY", "tmp:0:4", ["register:4050:4"]]
- 00a021bc ["INT_ADD", "tmp:1:8", ["register:8:8", "const:21:8"]]
- 00a021bc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 00a021bc bytes ea130278
- 00a021c0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 00a021c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00a021c0 bytes e92b00b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-320752b8359ca4b1b84670c28e3cc4f5"></a>

### [`00a02508`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a02508.md) → [`00a5faf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5f/00a5faf0.md) FUN_00a5faf0

採用 · 移動量 `+0x5d5e8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00abf570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00abf/00abf570.md) · 呼出先 13件 [`00464a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a54.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464b8c.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md) [`00465680`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465680.md)
- 新版 呼出元 1件 [`00b1f000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1f/00b1f000.md) · 呼出先 13件 [`004878ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878ec.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00487a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487a24.md) [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md) [`00488518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488518.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 77.36% / 新版 77.36%

CFGの説明率　旧版 24.53% / 新版 15.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `store_condition` 9件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 21件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a02534"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0254c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0257c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a02534",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a02538",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00487de0"
      ]
    ],
    [
      "unmatched:00a0254c",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a5fb1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00a5fb20",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00487de0"
      ]
    ],
    [
      "00a5fb34",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a02534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a02508.md#insn-00a02534) · [`00a0254c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a02508.md#insn-00a0254c) · [`00a0257c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a02508.md#insn-00a0257c)

~~~diff
- 00a02534 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a02534 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00a02534 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a02534 bytes a8831ff8
- 00a0254c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:50:8"]]
- 00a0254c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a0254c bytes e82b00f9
- 00a0257c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00a0257c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00a0257c bytes e00b00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f279110b4cd95d98097d0cb309d7e46"></a>

### [`00a02dd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a02dd4.md) → [`00a603bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a60/00a603bc.md) FUN_00a603bc

採用 · 移動量 `+0x5d5e8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 6件 [`00695904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00695/00695904.md) [`00a30558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a30/00a30558.md) [`00a33554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a33/00a33554.md) [`00a33760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a33/00a33760.md) [`00a3cecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3c/00a3cecc.md) · 呼出先 3件 [`00a028fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a028fc.md) [`00a02ad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a02ad0.md) [`00a02c74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a02c74.md)
- 新版 呼出元 6件 [`006bbc58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bb/006bbc58.md) [`00a8e3bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a8e/00a8e3bc.md) [`00a913b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a91/00a913b0.md) [`00a915bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a91/00a915bc.md) [`00a9adc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a9a/00a9adc0.md) · 呼出先 3件 [`00a5fee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5f/00a5fee4.md) [`00a600b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a60/00a600b8.md) [`00a6025c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a60/00a6025c.md)

変更の種類 branch_condition_or_target, call, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 91.84% / 新版 91.84%

CFGの説明率　旧版 73.68% / 新版 66.67%

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
      "site": "00a6040c",
      "value": [
        "leaf",
        "ram:a5fee4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a02e24",
      "value": [
        "leaf",
        "ram:a028fc:8"
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
      "site": "00a60424",
      "value": [
        "leaf",
        "ram:a6025c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a02e3c",
      "value": [
        "leaf",
        "ram:a02c74:8"
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
      "00a6040c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a028fc"
      ]
    ],
    [
      "00a60424",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a02c74"
      ]
    ]
  ],
  "added": [
    [
      "00a6040c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a5fee4"
      ]
    ],
    [
      "00a60424",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a6025c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a02e24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a02dd4.md#insn-00a02e24) · [`00a02e3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a02dd4.md#insn-00a02e3c) · [`00a02df8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a02dd4.md#insn-00a02df8)
- 新版 [`00a6040c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a60/00a603bc.md#insn-00a6040c) · [`00a60424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a60/00a603bc.md#insn-00a60424) · [`00a603e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a60/00a603bc.md#insn-00a603e0)

~~~diff
- 00a02e24 ["INT_ADD", "register:40f0:8", ["const:a02e24:8", "const:4:8"]]
- 00a02e24 ["CALL", null, ["ram:a028fc:8"]]
+ 00a6040c ["INT_ADD", "register:40f0:8", ["const:a6040c:8", "const:4:8"]]
+ 00a6040c ["CALL", null, ["ram:a5fee4:8"]]
- 00a02e24 bytes b6feff97
+ 00a6040c bytes b6feff97
- 00a02e3c ["INT_ADD", "register:40f0:8", ["const:a02e3c:8", "const:4:8"]]
- 00a02e3c ["CALL", null, ["ram:a02c74:8"]]
+ 00a60424 ["INT_ADD", "register:40f0:8", ["const:a60424:8", "const:4:8"]]
+ 00a60424 ["CALL", null, ["ram:a6025c:8"]]
- 00a02e3c bytes 8effff97
+ 00a60424 bytes 8effff97
- 00a02df8 ["CBRANCH", null, ["local:b11:8", "register:101:1"]]
+ 00a603e0 ["CBRANCH", null, ["local:b13:8", "register:101:1"]]
- 00a02df8 bytes 40040054
+ 00a603e0 bytes 40040054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f42717febf2b8890206780df62a8cf5f"></a>

### [`00a02e98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a02e98.md) → [`00a60480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a60/00a60480.md) FUN_00a60480

採用 · 移動量 `+0x5d5e8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00a02f68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a02f68.md) [`00a044e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a04/00a044e8.md) · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00a04c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a04/00a04c18.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`00a60550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a60/00a60550.md) [`00a61ad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a61/00a61ad4.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00a62204`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a62/00a62204.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 86.54% / 新版 86.54%

CFGの説明率　旧版 23.08% / 新版 12.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a02ee4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a02ee4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a02efc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a02ecc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a60530"
      ]
    ]
  ],
  "added": [
    [
      "00a604b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a60530"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a02ecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a02e98.md#insn-00a02ecc) · [`00a02ee4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a02e98.md#insn-00a02ee4) · [`00a02efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a02e98.md#insn-00a02efc)

~~~diff
- 00a02ecc ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00a02ecc ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00a02ecc ["CBRANCH", null, ["local:b8:8", "tmp:1:1"]]
- 00a02ecc bytes e9030054
- 00a02ee4 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00a02ee4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5020:16"]]
- 00a02ee4 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00a02ee4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5000:16"]]
- 00a02ee4 bytes 610200ad
- 00a02efc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:20:8"]]
- 00a02efc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00a02efc bytes 6002823c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8fca0c4d96f8568e4f810fc76fcce14d"></a>

### [`00a02f68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a02f68.md) → [`00a60550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a60/00a60550.md) FUN_00a60550

採用 · 移動量 `+0x5d5e8` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00996eec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00996/00996eec.md) · 呼出先 35件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`0044b898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b898.md) [`0044b8a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b8a8.md)
- 新版 呼出元 1件 [`009cc9e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009cc/009cc9e0.md) · 呼出先 35件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0046e730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e730.md) [`0046e740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e740.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 63.36% / 新版 63.36%

CFGの説明率　旧版 16.87% / 新版 11.08%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 48件, `store_condition` 11件, `store_value` 1件, `unresolved_branch_alignment` 36件, `unresolved_call_alignment` 32件, `unresolved_store_alignment` 70件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a02f7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a02f7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a02f80"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a02f7c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a02f80",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a02f90",
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
      "00a60564",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00a60568",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a60578",
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

- 旧版 [`00a02f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a02f68.md#insn-00a02f7c) · [`00a02f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a02f68.md#insn-00a02f80) · [`00a02f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a02f68.md#insn-00a02f90)

~~~diff
- 00a02f7c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00a02f7c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00a02f7c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:1c0:8"]]
- 00a02f7c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a02f7c bytes f6571ca9
- 00a02f80 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00a02f80 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00a02f80 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:1d0:8"]]
- 00a02f80 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a02f80 bytes f44f1da9
- 00a02f90 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a02f90 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffe8:8"]]
- 00a02f90 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a02f90 bytes a8831ef8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2175fbe6c7a0d2cc35d83db1fe7befe9"></a>

### [`00a04c04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a04/00a04c04.md) → [`00a621f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a62/00a621f0.md) FUN_00a621f0

採用 · 移動量 `+0x5d5ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a04a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a04/00a04a54.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00a62040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a62/00a62040.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "00a62200",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a04c14",
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
      "definition_site": "00a621fc",
      "incomplete_value": false,
      "site": "00a62200",
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
      "definition_site": "00a04c10",
      "incomplete_value": false,
      "site": "00a04c14",
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
      "00a621fc",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "00a62200",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "00a621fc",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "00a62200",
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

- 旧版 [`00a04c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a04/00a04c04.md#insn-00a04c14) · [`00a04c0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a04/00a04c04.md#insn-00a04c0c) · [`00a04c10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a04/00a04c04.md#insn-00a04c10)
- 新版 [`00a62200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a62/00a621f0.md#insn-00a62200) · [`00a621f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a62/00a621f0.md#insn-00a621f8) · [`00a621fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a62/00a621f0.md#insn-00a621fc)

~~~diff
- 00a04c14 ["INT_ADD", "register:40f0:8", ["const:a04c14:8", "const:4:8"]]
- 00a04c14 ["CALL", null, ["ram:418c38:8"]]
+ 00a62200 ["INT_ADD", "register:40f0:8", ["const:a62200:8", "const:4:8"]]
+ 00a62200 ["CALL", null, ["ram:43b738:8"]]
- 00a04c14 bytes 0950e897
+ 00a62200 bytes 4e65e797
- 00a04c0c ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 00a621f8 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 00a04c0c bytes 00c5fff0
+ 00a621f8 bytes a0c2ffb0
- 00a04c10 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 00a04c10 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00a04c10 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00a04c10 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00a621fc ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 00a621fc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00a621fc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00a621fc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00a04c10 bytes 00740e91
+ 00a621fc bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6f015d056215566b3d46fa874b4b96f"></a>

### [`00a04c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a04/00a04c18.md) → [`00a62204`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a62/00a62204.md) FUN_00a62204

採用 · 移動量 `+0x5d5ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a02e98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a02/00a02e98.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)
- 新版 呼出元 1件 [`00a60480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a60/00a60480.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)

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
      "site": "00a62214",
      "value": [
        "leaf",
        "ram:4428f0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a04c28",
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
      "definition_site": "00a62210",
      "incomplete_value": false,
      "site": "00a62214",
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
      "definition_site": "00a04c24",
      "incomplete_value": false,
      "site": "00a04c28",
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
      "00a62210",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "00a62214",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0041fdf0"
      ]
    ]
  ],
  "added": [
    [
      "00a62210",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "00a62214",
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

- 旧版 [`00a04c28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a04/00a04c18.md#insn-00a04c28) · [`00a04c20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a04/00a04c18.md#insn-00a04c20) · [`00a04c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a04/00a04c18.md#insn-00a04c24)
- 新版 [`00a62214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a62/00a62204.md#insn-00a62214) · [`00a6220c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a62/00a62204.md#insn-00a6220c) · [`00a62210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a62/00a62204.md#insn-00a62210)

~~~diff
- 00a04c28 ["INT_ADD", "register:40f0:8", ["const:a04c28:8", "const:4:8"]]
- 00a04c28 ["CALL", null, ["ram:41fdf0:8"]]
+ 00a62214 ["INT_ADD", "register:40f0:8", ["const:a62214:8", "const:4:8"]]
+ 00a62214 ["CALL", null, ["ram:4428f0:8"]]
- 00a04c28 bytes 726ce897
+ 00a62214 bytes b781e797
- 00a04c20 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 00a6220c ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 00a04c20 bytes 00c5fff0
+ 00a6220c bytes a0c2ffb0
- 00a04c24 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 00a04c24 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00a04c24 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00a04c24 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00a62210 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 00a62210 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00a62210 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00a62210 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00a04c24 bytes 00740e91
+ 00a62210 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ce46937274efd31282a0f6a8b4ba8ba"></a>

### [`00a04c2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a04/00a04c2c.md) → [`00a62218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a62/00a62218.md) FUN_00a62218

採用 · 移動量 `+0x5d5ec` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a03f2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a03/00a03f2c.md) · 呼出先 12件 [`0044b8ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b8ec.md) [`0044c020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c020.md) [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00adccd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adccd8.md)
- 新版 呼出元 1件 [`00a61514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a61/00a61514.md) · 呼出先 12件 [`0046e784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e784.md) [`0046eeb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046eeb8.md) [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`00b3c6b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3c/00b3c6b0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 62.02% / 新版 62.02%

CFGの説明率　旧版 47.83% / 新版 52.38%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 6件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 26件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a04c70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a04d6c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a04d94"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a04c70",
      "DATA",
      [
        "storage",
        "00c0be40",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00a04d38",
      "DATA",
      [
        "storage",
        "0032ff0c",
        null,
        "byte[35]"
      ]
    ],
    [
      "unmatched:00a04d40",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a623b8"
      ]
    ]
  ],
  "added": [
    [
      "00a6225c",
      "DATA",
      [
        "storage",
        "00c8b460",
        null,
        "pointer"
      ]
    ],
    [
      "00a62324",
      "DATA",
      [
        "storage",
        "00333f4c",
        null,
        "fde_table_entry"
      ]
    ],
    [
      "00a6232c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a623b8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a04c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a04/00a04c2c.md#insn-00a04c70) · [`00a04d6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a04/00a04c2c.md#insn-00a04d6c) · [`00a04d94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a04/00a04c2c.md#insn-00a04d94)

~~~diff
- 00a04c70 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00a04c70 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a04c70 bytes 680200f9
- 00a04d6c ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00a04d6c ["INT_ADD", "tmp:1:8", ["register:8:8", "const:18:8"]]
- 00a04d6c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00a04d6c bytes e8630039
- 00a04d94 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:19:8"]]
- 00a04d94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00a04d94 bytes e093813c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e08de71089381cf0a855665ec6e172f"></a>

### [`00a05118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a05/00a05118.md) → [`00a62704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a62/00a62704.md) FUN_00a62704

採用 · 移動量 `+0x5d5ec` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a05234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a05/00a05234.md) · 呼出先 6件 [`0044b9cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b9cc.md) [`0044c104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c104.md) [`0064c428`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064c/0064c428.md) [`0064c828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064c/0064c828.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)
- 新版 呼出元 1件 [`00a62820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a62/00a62820.md) · 呼出先 6件 [`0046e864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e864.md) [`0046ef9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ef9c.md) [`00672708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672708.md) [`00672b08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672b08.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 95.77% / 新版 95.77%

CFGの説明率　旧版 77.78% / 新版 87.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a05134"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a62720"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a62724",
      "incomplete_value": true,
      "site": "00a62728",
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
            "const:510:8"
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
      "unmatched:00a05134",
      "DATA",
      [
        "storage",
        "00c0be40",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00a62720",
      "DATA",
      [
        "storage",
        "00c8b460",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a05134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a05/00a05118.md#insn-00a05134) · [`00a0513c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a05/00a05118.md#insn-00a0513c)
- 新版 [`00a62728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a62/00a62704.md#insn-00a62728) · [`00a62720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a62/00a62704.md#insn-00a62720)

~~~diff
- 00a05134 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00a05134 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a05134 bytes 080000f9
- 00a0513c ["INT_ADD", "register:40f0:8", ["const:a0513c:8", "const:4:8"]]
- 00a0513c ["CALL", null, ["callee:0046e864:8"]]
+ 00a62728 ["INT_ADD", "register:40f0:8", ["const:a62728:8", "const:4:8"]]
+ 00a62728 ["CALL", null, ["callee:0046e864:8"]]
- 00a0513c bytes 241ae997
+ 00a62728 bytes 4f30e897
+ 00a62720 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00a62720 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00a62720 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ff5627cdee756c9cbb5f7ed1f9ac34d"></a>

### [`00a0525c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a05/00a0525c.md) → [`00a62848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a62/00a62848.md) FUN_00a62848

採用 · 移動量 `+0x5d5ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00a6286c",
      "incomplete_value": false,
      "site": "00a6286c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:480:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a05280",
      "incomplete_value": false,
      "site": "00a05280",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:e60:8"
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
      "00a6286c",
      "DATA",
      [
        "storage",
        "00c0be60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a6286c",
      "DATA",
      [
        "storage",
        "00c8b480",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a05270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a05/00a0525c.md#insn-00a05270) · [`00a05278`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a05/00a0525c.md#insn-00a05278) · [`00a0527c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a05/00a0525c.md#insn-00a0527c)
- 新版 [`00a6285c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a62/00a62848.md#insn-00a6285c) · [`00a62864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a62/00a62848.md#insn-00a62864) · [`00a62868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a62/00a62848.md#insn-00a62868)

~~~diff
- 00a05270 ["INT_ADD", "register:40f0:8", ["const:a05270:8", "const:4:8"]]
- 00a05270 ["CALL", null, ["callee:00c57a90:8"]]
+ 00a6285c ["INT_ADD", "register:40f0:8", ["const:a6285c:8", "const:4:8"]]
+ 00a6285c ["CALL", null, ["callee:00c57a90:8"]]
- 00a05270 bytes 74570794
+ 00a6285c bytes 8dd40794
- 00a05278 ["COPY", "register:4040:8", ["const:c0b000:8"]]
+ 00a62864 ["COPY", "register:4040:8", ["const:c8b000:8"]]
- 00a05278 bytes 281000d0
+ 00a62864 bytes 481100b0
- 00a0527c ["COPY", "tmp:0:8", ["const:e60:8"]]
- 00a0527c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a0527c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a0527c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a62868 ["COPY", "tmp:0:8", ["const:480:8"]]
+ 00a62868 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a62868 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a62868 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a0527c bytes 08813991
+ 00a62868 bytes 08011291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d145c1a860a27d1e6c757b205fd835f4"></a>

### [`00a053d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a05/00a053d8.md) → [`00a629c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a62/00a629c4.md) _INIT_218

採用 · 移動量 `+0x5d5ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 68.36% / 新版 68.36%

CFGの説明率　旧版 54.90% / 新版 93.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `unresolved_store_alignment` 29件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a05408"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a05430"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a05454"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a05408",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a05414",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00a05430",
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
      "00a629f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00a62a00",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00a62a1c",
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

- 旧版 [`00a05408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a05/00a053d8.md#insn-00a05408) · [`00a05430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a05/00a053d8.md#insn-00a05430) · [`00a05454`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a05/00a053d8.md#insn-00a05454)

~~~diff
- 00a05408 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00a05408 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00a05408 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a05408 bytes a9831ff8
- 00a05430 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:11:8"]]
- 00a05430 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00a05430 bytes e013813c
- 00a05454 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:31:8"]]
- 00a05454 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00a05454 bytes e013833c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77a71a2b9ea0537127777a51c9be1619"></a>

### [`00a05768`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a05/00a05768.md) → [`00a62d54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a62/00a62d54.md) FUN_00a62d54

採用 · 移動量 `+0x5d5ec` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00ab3444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab3/00ab3444.md) · 呼出先 15件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465780.md)
- 新版 呼出元 1件 [`00b12ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b12/00b12ed4.md) · 呼出先 15件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`004878dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878dc.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md) [`00488618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488618.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 93.72% / 新版 93.72%

CFGの説明率　旧版 87.67% / 新版 90.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 5件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a62d94",
      "incomplete_value": false,
      "site": "00a62da0",
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
            "const:938:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a057a8",
      "incomplete_value": false,
      "site": "00a057b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:d78:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a62db4",
      "incomplete_value": true,
      "site": "00a62dd0",
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
                "const:2b2000:8"
              ],
              [
                "leaf",
                "const:427:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a057c8",
      "incomplete_value": true,
      "site": "00a057e4",
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
                "const:d66:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a63068",
      "incomplete_value": true,
      "site": "00a6306c",
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
      "definition_site": "00a05a7c",
      "incomplete_value": true,
      "site": "00a05a80",
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
      "00a62da0",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "00a62db4",
      "READ",
      [
        "storage",
        "002a1d66",
        null,
        "string"
      ]
    ],
    [
      "00a63058",
      "READ",
      [
        "storage",
        "00c1adc0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00a62da0",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "00a62db4",
      "READ",
      [
        "storage",
        "002b2427",
        null,
        "string"
      ]
    ],
    [
      "00a63058",
      "READ",
      [
        "storage",
        "00c9a7b0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a0579c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a05/00a05768.md#insn-00a0579c) · [`00a057a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a05/00a05768.md#insn-00a057a4) · [`00a057a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a05/00a05768.md#insn-00a057a8)
- 新版 [`00a62d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a62/00a62d54.md#insn-00a62d88) · [`00a62d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a62/00a62d54.md#insn-00a62d90) · [`00a62d94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a62/00a62d54.md#insn-00a62d94)

~~~diff
- 00a0579c ["INT_ADD", "register:40f0:8", ["const:a0579c:8", "const:4:8"]]
- 00a0579c ["CALL", null, ["callee:00487de0:8"]]
+ 00a62d88 ["INT_ADD", "register:40f0:8", ["const:a62d88:8", "const:4:8"]]
+ 00a62d88 ["CALL", null, ["callee:00487de0:8"]]
- 00a0579c bytes eb7de997
+ 00a62d88 bytes 1694e897
- 00a057a4 ["COPY", "register:4040:8", ["const:be7000:8"]]
+ 00a62d90 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 00a057a4 bytes 080f00d0
+ 00a62d90 bytes 081000d0
- 00a057a8 ["COPY", "tmp:0:8", ["const:d78:8"]]
- 00a057a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a057a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a057a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a62d94 ["COPY", "tmp:0:8", ["const:938:8"]]
+ 00a62d94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a62d94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a62d94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a057a8 bytes 08e13591
+ 00a62d94 bytes 08e12491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03364a4d4f35622573e355823edbfe50"></a>

### [`00a06798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a06/00a06798.md) → [`00a63de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a63/00a63de4.md) _INIT_219

採用 · 移動量 `+0x5d64c` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 57.63% / 新版 57.63%

CFGの説明率　旧版 93.33% / 新版 90.32%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_store_alignment` 37件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a067c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a067f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a067fc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a067c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a067d4",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00a067f0",
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
      "00a63e14",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00a63e20",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00a63e3c",
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

- 旧版 [`00a067c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a06/00a06798.md#insn-00a067c8) · [`00a067f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a06/00a06798.md#insn-00a067f0) · [`00a067fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a06/00a06798.md#insn-00a067fc)

~~~diff
- 00a067c8 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00a067c8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00a067c8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a067c8 bytes a9831ff8
- 00a067f0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:11:8"]]
- 00a067f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00a067f0 bytes e013813c
- 00a067fc ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00a067fc ["INT_ADD", "tmp:1:8", ["register:8:8", "const:41:8"]]
- 00a067fc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 00a067fc bytes e9130478
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a721f05a6532af75e35e7782348a5c3"></a>

### [`00a06b28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a06/00a06b28.md) → [`00a64174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a64/00a64174.md) FUN_00a64174

採用 · 移動量 `+0x5d64c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`0099fe4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0099f/0099fe4c.md) · 呼出先 1件 [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md)
- 新版 呼出元 1件 [`009d5b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d5/009d5b5c.md) · 呼出先 1件 [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 50.00% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a06b60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a06/00a06b28.md#insn-00a06b60) · [`00a06b74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a06/00a06b28.md#insn-00a06b74)
- 新版 [`00a641ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a64/00a64174.md#insn-00a641ac) · [`00a641c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a64/00a64174.md#insn-00a641c0)

~~~diff
- 00a06b60 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a06b60 ["INT_ADD", "register:40f0:8", ["const:a06b60:8", "const:4:8"]]
- 00a06b60 ["CALLIND", null, ["register:0:8"]]
+ 00a641ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a641ac ["INT_ADD", "register:40f0:8", ["const:a641ac:8", "const:4:8"]]
+ 00a641ac ["CALLIND", null, ["register:0:8"]]
- 00a06b60 bytes 00013fd6
+ 00a641ac bytes 00013fd6
- 00a06b74 ["INT_ADD", "register:40f0:8", ["const:a06b74:8", "const:4:8"]]
- 00a06b74 ["CALL", null, ["callee:004878fc:8"]]
+ 00a641c0 ["INT_ADD", "register:40f0:8", ["const:a641c0:8", "const:4:8"]]
+ 00a641c0 ["CALL", null, ["callee:004878fc:8"]]
- 00a06b74 bytes bc77e997
+ 00a641c0 bytes cf8de897
~~~


<a id="compare-9b4e94b339071b2e183875e0fe1426e5"></a>

### [`00a06c10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a06/00a06c10.md) → [`00a6425c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a64/00a6425c.md) FUN_00a6425c

採用 · 移動量 `+0x5d64c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `compiler_shape_candidate`

- 旧版 呼出元 1件 [`009bd6c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009bd/009bd6c4.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00a1a5b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a1a/00a1a5b4.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-27957ae503b39d4622e93dd354a1a1c3"></a>

### [`00a06c74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a06/00a06c74.md) → [`00a642c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a64/00a642c0.md) FUN_00a642c0

採用 · 移動量 `+0x5d64c` · 根拠 `leaf_bytes_and_unique_code_order` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `compiler_shape_candidate`

- 旧版 呼出元 2件 [`0099fe4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0099f/0099fe4c.md) [`009bd6c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009bd/009bd6c4.md) · 呼出先 0件 
- 新版 呼出元 2件 [`009d5b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d5/009d5b5c.md) [`00a1a5b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a1a/00a1a5b4.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-7c0cd21fb84b6cb424adec2636c47139"></a>

### [`00a06d28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a06/00a06d28.md) → [`00a64374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a64/00a64374.md) FUN_00a64374

採用 · 移動量 `+0x5d64c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`009c5344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009c5/009c5344.md) · 呼出先 1件 [`0045df50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045df50.md)
- 新版 呼出元 1件 [`00a22234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a22/00a22234.md) · 呼出先 1件 [`00480de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480de8.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a643d0",
      "incomplete_value": true,
      "site": "00a643d8",
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a6440c",
      "incomplete_value": true,
      "site": "00a64414",
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
    "ordinal": 11,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00a06d8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a06/00a06d28.md#insn-00a06d8c) · [`00a06dc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a06/00a06d28.md#insn-00a06dc8) · [`00a06d44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a06/00a06d28.md#insn-00a06d44)
- 新版 [`00a643d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a64/00a64374.md#insn-00a643d8) · [`00a64414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a64/00a64374.md#insn-00a64414) · [`00a64390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a64/00a64374.md#insn-00a64390)

~~~diff
- 00a06d8c ["INT_ADD", "register:40f0:8", ["const:a06d8c:8", "const:4:8"]]
- 00a06d8c ["CALL", null, ["callee:00480de8:8"]]
+ 00a643d8 ["INT_ADD", "register:40f0:8", ["const:a643d8:8", "const:4:8"]]
+ 00a643d8 ["CALL", null, ["callee:00480de8:8"]]
- 00a06d8c bytes 715ce997
+ 00a643d8 bytes 8472e897
- 00a06dc8 ["INT_ADD", "register:40f0:8", ["const:a06dc8:8", "const:4:8"]]
- 00a06dc8 ["CALL", null, ["callee:00480de8:8"]]
+ 00a64414 ["INT_ADD", "register:40f0:8", ["const:a64414:8", "const:4:8"]]
+ 00a64414 ["CALL", null, ["callee:00480de8:8"]]
- 00a06dc8 bytes 625ce997
+ 00a64414 bytes 7572e897
- 00a06d44 ["INT_ADD", "register:40f0:8", ["const:a06d44:8", "const:4:8"]]
- 00a06d44 ["CALL", null, ["callee:00480de8:8"]]
+ 00a64390 ["INT_ADD", "register:40f0:8", ["const:a64390:8", "const:4:8"]]
+ 00a64390 ["CALL", null, ["callee:00480de8:8"]]
- 00a06d44 bytes 835ce997
+ 00a64390 bytes 9672e897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6d12705bb658d52a48a589c391d150f"></a>

### [`00a06e18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a06/00a06e18.md) → [`00a64464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a64/00a64464.md) FUN_00a64464

採用 · 移動量 `+0x5d64c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`009bd6c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009bd/009bd6c4.md) · 呼出先 1件 [`0045d518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d518.md)
- 新版 呼出元 1件 [`00a1a5b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a1a/00a1a5b4.md) · 呼出先 1件 [`004803b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004803b0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 33.33% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a64478",
      "incomplete_value": true,
      "site": "00a64484",
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
      "definition_site": "00a6448c",
      "incomplete_value": true,
      "site": "00a64490",
      "value": [
        "live",
        "register:40a0:8"
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00a06e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a06/00a06e18.md#insn-00a06e38) · [`00a06e44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a06/00a06e18.md#insn-00a06e44) · [`00a06e58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a06/00a06e18.md#insn-00a06e58)
- 新版 [`00a64484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a64/00a64464.md#insn-00a64484) · [`00a64490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a64/00a64464.md#insn-00a64490) · [`00a644a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a64/00a64464.md#insn-00a644a4)

~~~diff
- 00a06e38 ["INT_ADD", "register:40f0:8", ["const:a06e38:8", "const:4:8"]]
- 00a06e38 ["CALL", null, ["callee:004803b0:8"]]
+ 00a64484 ["INT_ADD", "register:40f0:8", ["const:a64484:8", "const:4:8"]]
+ 00a64484 ["CALL", null, ["callee:004803b0:8"]]
- 00a06e38 bytes b859e997
+ 00a64484 bytes cb6fe897
- 00a06e44 ["INT_ADD", "register:40f0:8", ["const:a06e44:8", "const:4:8"]]
- 00a06e44 ["CALL", null, ["callee:004803b0:8"]]
+ 00a64490 ["INT_ADD", "register:40f0:8", ["const:a64490:8", "const:4:8"]]
+ 00a64490 ["CALL", null, ["callee:004803b0:8"]]
- 00a06e44 bytes b559e997
+ 00a64490 bytes c86fe897
- 00a06e58 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00a06e58 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00a644a4 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 00a644a4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00a06e58 bytes 8b000054
+ 00a644a4 bytes 8b000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-729769b5368e69e0b1e53090d4ac37f3"></a>

### [`00a06e80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a06/00a06e80.md) → [`00a644cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a64/00a644cc.md) FUN_00a644cc

採用 · 移動量 `+0x5d64c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`009c5344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009c5/009c5344.md) · 呼出先 1件 [`0045df50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045df50.md)
- 新版 呼出元 1件 [`00a22234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a22/00a22234.md) · 呼出先 1件 [`00480de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480de8.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a644f0",
      "incomplete_value": true,
      "site": "00a644f8",
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

- 旧版 [`00a06eac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a06/00a06e80.md#insn-00a06eac) · [`00a06ea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a06/00a06e80.md#insn-00a06ea0)
- 新版 [`00a644f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a64/00a644cc.md#insn-00a644f8) · [`00a644ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a64/00a644cc.md#insn-00a644ec)

~~~diff
- 00a06eac ["INT_ADD", "register:40f0:8", ["const:a06eac:8", "const:4:8"]]
- 00a06eac ["CALL", null, ["callee:00480de8:8"]]
+ 00a644f8 ["INT_ADD", "register:40f0:8", ["const:a644f8:8", "const:4:8"]]
+ 00a644f8 ["CALL", null, ["callee:00480de8:8"]]
- 00a06eac bytes 295ce997
+ 00a644f8 bytes 3c72e897
- 00a06ea0 ["INT_ADD", "register:40f0:8", ["const:a06ea0:8", "const:4:8"]]
- 00a06ea0 ["CALL", null, ["callee:00480de8:8"]]
+ 00a644ec ["INT_ADD", "register:40f0:8", ["const:a644ec:8", "const:4:8"]]
+ 00a644ec ["CALL", null, ["callee:00480de8:8"]]
- 00a06ea0 bytes 2c5ce997
+ 00a644ec bytes 3f72e897
~~~


<a id="compare-d836508fcb6e29b08169b37596cb3387"></a>

### [`00a06ec4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a06/00a06ec4.md) → [`00a64510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a64/00a64510.md) _INIT_220

採用 · 移動量 `+0x5d64c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 54.80% / 新版 54.80%

CFGの説明率　旧版 51.28% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 17件, `unresolved_store_alignment` 39件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a06ef4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a06f08"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a06f0c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a06ef4",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a06f00",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00a06f08",
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
      "00a64540",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00a6454c",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00a64554",
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

- 旧版 [`00a06ef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a06/00a06ec4.md#insn-00a06ef4) · [`00a06f08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a06/00a06ec4.md#insn-00a06f08) · [`00a06f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a06/00a06ec4.md#insn-00a06f0c)

~~~diff
- 00a06ef4 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00a06ef4 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00a06ef4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a06ef4 bytes a9831ff8
- 00a06f08 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 00a06f08 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:21:8"]]
- 00a06f08 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 00a06f08 bytes ea130278
- 00a06f0c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 00a06f0c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00a06f0c bytes e92b00b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f0896ba2bfe43bcd4f6097ca2a43ffb"></a>

### [`00a07294`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a07/00a07294.md) → [`00a648e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a64/00a648e0.md) FUN_00a648e0

採用 · 移動量 `+0x5d64c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00996eec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00996/00996eec.md) [`009a1cd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a1/009a1cd4.md) [`009eae0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ea/009eae0c.md) · 呼出先 13件 [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464ca8.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md) [`004652a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/004652a0.md)
- 新版 呼出元 3件 [`009cc9e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009cc/009cc9e0.md) [`009d79e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d7/009d79e0.md) [`00a47d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a47d08.md) · 呼出先 13件 [`004878dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878dc.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00487b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487b40.md) [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md) [`00488138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488138.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 94.56% / 新版 94.56%

CFGの説明率　旧版 39.13% / 新版 41.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a072d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a075b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a075b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a072d4",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00a072d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x1a0]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a075a0",
      "READ",
      [
        "storage",
        "00c1adc0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00a64920",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "00a64920",
      "WRITE",
      [
        "storage",
        "Stack[-0x1a0]",
        null,
        null
      ]
    ],
    [
      "00a64bec",
      "READ",
      [
        "storage",
        "00c9a7b0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a072d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a07/00a07294.md#insn-00a072d4) · [`00a07378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a07/00a07294.md#insn-00a07378) · [`00a074bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a07/00a07294.md#insn-00a074bc)
- 新版 [`00a649c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a64/00a648e0.md#insn-00a649c4) · [`00a64b08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a64/00a648e0.md#insn-00a64b08)

~~~diff
- 00a072d4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00a072d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a072d4 bytes e81300f9
- 00a07378 ["INT_ADD", "register:40f0:8", ["const:a07378:8", "const:4:8"]]
- 00a07378 ["CALL", null, ["callee:004878fc:8"]]
+ 00a649c4 ["INT_ADD", "register:40f0:8", ["const:a649c4:8", "const:4:8"]]
+ 00a649c4 ["CALL", null, ["callee:004878fc:8"]]
- 00a07378 bytes bb75e997
+ 00a649c4 bytes ce8be897
- 00a074bc ["INT_ADD", "register:40f0:8", ["const:a074bc:8", "const:4:8"]]
- 00a074bc ["CALL", null, ["callee:00487b40:8"]]
+ 00a64b08 ["INT_ADD", "register:40f0:8", ["const:a64b08:8", "const:4:8"]]
+ 00a64b08 ["CALL", null, ["callee:00487b40:8"]]
- 00a074bc bytes fb75e997
+ 00a64b08 bytes 0e8ce897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6328d131661598a55713876d4159506"></a>

### [`00a076f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a07/00a076f4.md) → [`00a64d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a64/00a64d40.md) FUN_00a64d40

採用 · 移動量 `+0x5d64c` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00abf570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00abf/00abf570.md) · 呼出先 22件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md) [`0046555c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/0046555c.md)
- 新版 呼出元 1件 [`00b1f000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1f/00b1f000.md) · 呼出先 22件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md) [`004883f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/004883f4.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 84.85% / 新版 84.85%

CFGの説明率　旧版 38.92% / 新版 41.94%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `store_condition` 2件, `unresolved_branch_alignment` 8件, `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 28件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a076f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a076f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a076f8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a076f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a076f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a076fc",
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
      "00a64d40",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00a64d44",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00a64d48",
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

- 旧版 [`00a076f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a07/00a076f4.md#insn-00a076f4) · [`00a076f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a07/00a076f4.md#insn-00a076f8) · [`00a076fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a07/00a076f4.md#insn-00a076fc)

~~~diff
- 00a076f4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a076f4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a076f4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffa0:8"]]
- 00a076f4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00a076f4 bytes fd7bbaa9
- 00a076f8 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00a076f8 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00a076f8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00a076f8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a076f8 bytes fc6f01a9
- 00a076fc ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00a076fc ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00a076fc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00a076fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a076fc bytes fa6702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a072936819dddd2acacf722aba7a252"></a>

### [`00a0821c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a08/00a0821c.md) → [`00a65868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a65/00a65868.md) FUN_00a65868

採用 · 移動量 `+0x5d64c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`005d996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d996c.md) [`007ab6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ab/007ab6a0.md) [`007acf88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ac/007acf88.md) · 呼出先 7件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`006928b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00692/006928b0.md) [`00a0801c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a08/00a0801c.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 3件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`007dd760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007dd/007dd760.md) [`007df0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) · 呼出先 7件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`006b8c04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b8c04.md) [`00a65668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a65/00a65668.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 98.47% / 新版 98.47%

CFGの説明率　旧版 86.05% / 新版 80.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a083b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a083e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a083e4"
    }
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00a083b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a08/00a0821c.md#insn-00a083b4) · [`00a083b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a08/00a0821c.md#insn-00a083b8) · [`00a083e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a08/00a0821c.md#insn-00a083e4)
- 新版 [`00a65a04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a65/00a65868.md#insn-00a65a04)

~~~diff
- 00a083b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:10:8"]]
- 00a083b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a083b4 bytes 680a00f9
- 00a083b8 ["INT_ADD", "register:40f0:8", ["const:a083b8:8", "const:4:8"]]
- 00a083b8 ["CALL", null, ["callee:00c57c00:8"]]
+ 00a65a04 ["INT_ADD", "register:40f0:8", ["const:a65a04:8", "const:4:8"]]
+ 00a65a04 ["CALL", null, ["callee:00c57c00:8"]]
- 00a083b8 bytes 7e4b0794
+ 00a65a04 bytes 7fc80794
- 00a083e4 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00a083e4 ["COPY", "tmp:1:8", ["register:4000:8"]]
- 00a083e4 ["INT_ADD", "tmp:2:8", ["register:4098:8", "const:8:8"]]
- 00a083e4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a083e4 bytes 608200a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9ad52705aac0b4aa0c16356c79ea1d6"></a>

### [`00a08428`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a08/00a08428.md) → [`00a65a74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a65/00a65a74.md) FUN_00a65a74

採用 · 移動量 `+0x5d64c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`007acf88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ac/007acf88.md) · 呼出先 3件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00a0801c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a08/00a0801c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`007df0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) · 呼出先 3件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00a65668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a65/00a65668.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, control_flow_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.96% / 新版 98.96%

CFGの説明率　旧版 57.89% / 新版 57.89%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00a08490",
      "incomplete_value": false,
      "site": "00a08498",
      "value": [
        "leaf",
        "const:40:8"
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
      "unmatched:00a08460",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00a65adc"
      ]
    ],
    [
      "00a65aac",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00a65be0"
      ]
    ]
  ],
  "added": [
    [
      "00a65aac",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00a65adc"
      ]
    ],
    [
      "00a65bd8",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00a65be0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a08498`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a08/00a08428.md#insn-00a08498) · [`00a08448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a08/00a08428.md#insn-00a08448) · [`00a08458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a08/00a08428.md#insn-00a08458)
- 新版 [`00a65ae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a65/00a65a74.md#insn-00a65ae4) · [`00a65a94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a65/00a65a74.md#insn-00a65a94) · [`00a65aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a65/00a65a74.md#insn-00a65aa4)

~~~diff
- 00a08498 ["INT_ADD", "register:40f0:8", ["const:a08498:8", "const:4:8"]]
- 00a08498 ["CALL", null, ["callee:00c57a90:8"]]
+ 00a65ae4 ["INT_ADD", "register:40f0:8", ["const:a65ae4:8", "const:4:8"]]
+ 00a65ae4 ["CALL", null, ["callee:00c57a90:8"]]
- 00a08498 bytes ea4a0794
+ 00a65ae4 bytes ebc70794
- 00a08448 ["INT_ADD", "register:40f0:8", ["const:a08448:8", "const:4:8"]]
- 00a08448 ["CALL", null, ["callee:00a65668:8"]]
+ 00a65a94 ["INT_ADD", "register:40f0:8", ["const:a65a94:8", "const:4:8"]]
+ 00a65a94 ["CALL", null, ["callee:00a65668:8"]]
- 00a08448 bytes f5feff97
+ 00a65a94 bytes f5feff97
- 00a08458 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00a08458 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00a65aa4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00a65aa4 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00a08458 bytes c80000b5
+ 00a65aa4 bytes c80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3649b1331b79c1a9b26d3bb7c0524381"></a>

### [`00a09db8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a09/00a09db8.md) → [`00a67a88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a67/00a67a88.md) FUN_00a67a88

採用 · 移動量 `+0x5dcd0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a076f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a07/00a076f4.md) · 呼出先 5件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00837180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/00837180.md) [`00a0a1a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0a/00a0a1a4.md) [`00a0a4cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0a/00a0a4cc.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00a64d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a64/00a64d40.md) · 呼出先 5件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`008690f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00869/008690f8.md) [`00a67e74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a67/00a67e74.md) [`00a6819c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a6819c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 81.36% / 新版 81.36%

CFGの説明率　旧版 46.15% / 新版 47.37%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 6件, `unresolved_branch_alignment` 9件, `unresolved_store_alignment` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a09dcc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a09dcc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a09de8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a09dcc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a09de8",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a09df0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a67cf0"
      ]
    ]
  ],
  "added": [
    [
      "00a67a9c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a67ab8",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00a67ac0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a67cf0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a09dcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a09/00a09db8.md#insn-00a09dcc) · [`00a09de8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a09/00a09db8.md#insn-00a09de8) · [`00a09df0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a09/00a09db8.md#insn-00a09df0)

~~~diff
- 00a09dcc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00a09dcc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00a09dcc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00a09dcc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a09dcc bytes f44f06a9
- 00a09de8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a09de8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00a09de8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a09de8 bytes a8831ff8
- 00a09df0 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00a09df0 ["CBRANCH", null, ["local:b53:8", "tmp:0:1"]]
- 00a09df0 bytes 881100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2bf5a2ea26789a0d188ef7957c986de"></a>

### [`00a0a4cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0a/00a0a4cc.md) → [`00a6819c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a6819c.md) FUN_00a6819c

採用 · 移動量 `+0x5dcd0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a09db8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a09/00a09db8.md) · 呼出先 6件 [`006928b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00692/006928b0.md) [`00a09d6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a09/00a09d6c.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00a67a88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a67/00a67a88.md) · 呼出先 6件 [`006b8c04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b8/006b8c04.md) [`00a67a3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a67/00a67a3c.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 36.36% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a681f4",
      "incomplete_value": true,
      "site": "00a681f8",
      "value": [
        "live",
        "register:40b8:8"
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00a0a528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0a/00a0a4cc.md#insn-00a0a528) · [`00a0a4f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0a/00a0a4cc.md#insn-00a0a4f0) · [`00a0a518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0a/00a0a4cc.md#insn-00a0a518)
- 新版 [`00a681f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a6819c.md#insn-00a681f8) · [`00a681c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a6819c.md#insn-00a681c0) · [`00a681e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a6819c.md#insn-00a681e8)

~~~diff
- 00a0a528 ["INT_ADD", "register:40f0:8", ["const:a0a528:8", "const:4:8"]]
- 00a0a528 ["CALL", null, ["callee:00c57a90:8"]]
+ 00a681f8 ["INT_ADD", "register:40f0:8", ["const:a681f8:8", "const:4:8"]]
+ 00a681f8 ["CALL", null, ["callee:00c57a90:8"]]
- 00a0a528 bytes c6420794
+ 00a681f8 bytes 26be0794
- 00a0a4f0 ["INT_ADD", "register:40f0:8", ["const:a0a4f0:8", "const:4:8"]]
- 00a0a4f0 ["CALL", null, ["callee:00c57a90:8"]]
+ 00a681c0 ["INT_ADD", "register:40f0:8", ["const:a681c0:8", "const:4:8"]]
+ 00a681c0 ["CALL", null, ["callee:00c57a90:8"]]
- 00a0a4f0 bytes d4420794
+ 00a681c0 bytes 34be0794
- 00a0a518 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
+ 00a681e8 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 00a0a518 bytes e0010054
+ 00a681e8 bytes e0010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ee8329c8b0eb9ddda1f6c6286357837"></a>

### [`00a0a5a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0a/00a0a5a0.md) → [`00a68270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a68270.md) FUN_00a68270

採用 · 移動量 `+0x5dcd0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a09968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a09/00a09968.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)
- 新版 呼出元 1件 [`00a67638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a67/00a67638.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)

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
      "site": "00a68280",
      "value": [
        "leaf",
        "ram:4428f0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a0a5b0",
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
      "definition_site": "00a6827c",
      "incomplete_value": false,
      "site": "00a68280",
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
      "definition_site": "00a0a5ac",
      "incomplete_value": false,
      "site": "00a0a5b0",
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
      "00a6827c",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "00a68280",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0041fdf0"
      ]
    ]
  ],
  "added": [
    [
      "00a6827c",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "00a68280",
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

- 旧版 [`00a0a5b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0a/00a0a5a0.md#insn-00a0a5b0) · [`00a0a5a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0a/00a0a5a0.md#insn-00a0a5a8) · [`00a0a5ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0a/00a0a5a0.md#insn-00a0a5ac)
- 新版 [`00a68280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a68270.md#insn-00a68280) · [`00a68278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a68270.md#insn-00a68278) · [`00a6827c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a68270.md#insn-00a6827c)

~~~diff
- 00a0a5b0 ["INT_ADD", "register:40f0:8", ["const:a0a5b0:8", "const:4:8"]]
- 00a0a5b0 ["CALL", null, ["ram:41fdf0:8"]]
+ 00a68280 ["INT_ADD", "register:40f0:8", ["const:a68280:8", "const:4:8"]]
+ 00a68280 ["CALL", null, ["ram:4428f0:8"]]
- 00a0a5b0 bytes 1056e897
+ 00a68280 bytes 9c69e797
- 00a0a5a8 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 00a68278 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 00a0a5a8 bytes e0c4ffb0
+ 00a68278 bytes 60c2fff0
- 00a0a5ac ["COPY", "tmp:0:8", ["const:39d:8"]]
- 00a0a5ac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00a0a5ac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00a0a5ac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00a6827c ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 00a6827c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00a6827c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00a6827c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00a0a5ac bytes 00740e91
+ 00a6827c bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48f5e591605d11457bcb7c39caefc824"></a>

### [`00a0a5b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0a/00a0a5b4.md) → [`00a68284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a68284.md) _INIT_221

採用 · 移動量 `+0x5dcd0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 72.32% / 新版 72.32%

CFGの説明率　旧版 45.95% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_store_alignment` 16件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0a5e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0a60c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0a630"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a0a5e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a0a5f0",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00a0a60c",
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
      "00a682b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00a682c0",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00a682dc",
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

- 旧版 [`00a0a5e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0a/00a0a5b4.md#insn-00a0a5e4) · [`00a0a60c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0a/00a0a5b4.md#insn-00a0a60c) · [`00a0a630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0a/00a0a5b4.md#insn-00a0a630)

~~~diff
- 00a0a5e4 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00a0a5e4 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00a0a5e4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a0a5e4 bytes a9831ff8
- 00a0a60c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:11:8"]]
- 00a0a60c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00a0a60c bytes e013813c
- 00a0a630 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:31:8"]]
- 00a0a630 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00a0a630 bytes e013833c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ede7c95ce65896c70d2c7bcbe81c46d"></a>

### [`00a0a944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0a/00a0a944.md) → [`00a68614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a68614.md) FUN_00a68614

採用 · 移動量 `+0x5dcd0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a0b08c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0b08c.md) · 呼出先 4件 [`0045df50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045df50.md) [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md) [`0066b478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066b/0066b478.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00a68dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a68dc0.md) · 呼出先 4件 [`00480de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480de8.md) [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`006917c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00691/006917c0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 95.74% / 新版 95.74%

CFGの説明率　旧版 58.06% / 新版 64.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0a948"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0a948"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0a94c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a0a948",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a0a94c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a0a9b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a6875c"
      ]
    ]
  ],
  "added": [
    [
      "00a68618",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00a6861c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00a68684",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a6875c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a0a948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0a/00a0a944.md#insn-00a0a948) · [`00a0a94c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0a/00a0a944.md#insn-00a0a94c) · [`00a0a98c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0a/00a0a944.md#insn-00a0a98c)
- 新版 [`00a6865c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a68614.md#insn-00a6865c)

~~~diff
- 00a0a948 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a0a948 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a0a948 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00a0a948 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a0a948 bytes fd7b03a9
- 00a0a94c ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00a0a94c ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00a0a94c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00a0a94c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a0a94c bytes fa6704a9
- 00a0a98c ["INT_ADD", "register:40f0:8", ["const:a0a98c:8", "const:4:8"]]
- 00a0a98c ["CALL", null, ["callee:00480de8:8"]]
+ 00a6865c ["INT_ADD", "register:40f0:8", ["const:a6865c:8", "const:4:8"]]
+ 00a6865c ["CALL", null, ["callee:00480de8:8"]]
- 00a0a98c bytes 714de997
+ 00a6865c bytes e361e897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-027fa412b5b8b83ff4e72968fe70e5b5"></a>

### [`00a0aaec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0a/00a0aaec.md) → [`00a687bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a687bc.md) FUN_00a687bc

採用 · 移動量 `+0x5dcd0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a0b228`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0b228.md) · 呼出先 4件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0045d518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d518.md) [`0059d170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d170.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00a68f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a68f5c.md) · 呼出先 4件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`004803b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004803b0.md) [`005c17a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c17a0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 52.17% / 新版 55.81%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00a0ab84",
      "incomplete_value": true,
      "site": "00a0ab88",
      "value": [
        "live",
        "register:40a0:8"
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a6886c",
      "incomplete_value": true,
      "site": "00a68870",
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
                "register:40e0:8"
              ],
              [
                "leaf",
                "const:30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a68898",
      "incomplete_value": true,
      "site": "00a6889c",
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
                "register:40e8:8"
              ],
              [
                "leaf",
                "const:fffffffffffffff8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 6,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00a0ab88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0a/00a0aaec.md#insn-00a0ab88) · [`00a0aba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0a/00a0aaec.md#insn-00a0aba0) · [`00a0abcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0a/00a0aaec.md#insn-00a0abcc)
- 新版 [`00a68858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a687bc.md#insn-00a68858) · [`00a68870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a687bc.md#insn-00a68870) · [`00a6889c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a687bc.md#insn-00a6889c)

~~~diff
- 00a0ab88 ["INT_ADD", "register:40f0:8", ["const:a0ab88:8", "const:4:8"]]
- 00a0ab88 ["CALL", null, ["callee:004803b0:8"]]
+ 00a68858 ["INT_ADD", "register:40f0:8", ["const:a68858:8", "const:4:8"]]
+ 00a68858 ["CALL", null, ["callee:004803b0:8"]]
- 00a0ab88 bytes 644ae997
+ 00a68858 bytes d65ee897
- 00a0aba0 ["INT_ADD", "register:40f0:8", ["const:a0aba0:8", "const:4:8"]]
- 00a0aba0 ["CALL", null, ["callee:0043bb64:8"]]
+ 00a68870 ["INT_ADD", "register:40f0:8", ["const:a68870:8", "const:4:8"]]
+ 00a68870 ["CALL", null, ["callee:0043bb64:8"]]
- 00a0aba0 bytes 3139e897
+ 00a68870 bytes bd4ce797
- 00a0abcc ["INT_ADD", "register:40f0:8", ["const:a0abcc:8", "const:4:8"]]
- 00a0abcc ["CALL", null, ["callee:004803b0:8"]]
+ 00a6889c ["INT_ADD", "register:40f0:8", ["const:a6889c:8", "const:4:8"]]
+ 00a6889c ["CALL", null, ["callee:004803b0:8"]]
- 00a0abcc bytes 534ae997
+ 00a6889c bytes c55ee897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c3c5cb6eec46bba4429866e543e850a"></a>

### [`00a0b228`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0b228.md) → [`00a68f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a68f5c.md) FUN_00a68f5c

採用 · 移動量 `+0x5dd34` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009c9134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009c9/009c9134.md) · 呼出先 10件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0045d518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d518.md) [`00839a8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839a8c.md) [`00a0aaec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0a/00a0aaec.md) [`00a0d1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0d/00a0d1b0.md)
- 新版 呼出元 1件 [`00a26020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a26/00a26020.md) · 呼出先 10件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`004803b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004803b0.md) [`0086bd78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bd78.md) [`00a687bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a687bc.md) [`00a6ae18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6ae18.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 90.58% / 新版 90.58%

CFGの説明率　旧版 57.14% / 新版 58.54%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0b254"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0b260"
    }
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a68ff8",
      "incomplete_value": false,
      "site": "00a69000",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:500:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a0b2c4",
      "incomplete_value": false,
      "site": "00a0b2cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a0b254",
      "WRITE",
      [
        "storage",
        "Stack[-0x88]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a0b260",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00a69000",
      "DATA",
      [
        "storage",
        "00c0bee0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00a68f88",
      "WRITE",
      [
        "storage",
        "Stack[-0x88]",
        null,
        null
      ]
    ],
    [
      "00a68f94",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00a69000",
      "DATA",
      [
        "storage",
        "00c8b500",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a0b254`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0b228.md#insn-00a0b254) · [`00a0b260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0b228.md#insn-00a0b260) · [`00a0b3a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0b228.md#insn-00a0b3a0)
- 新版 [`00a690d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a68f5c.md#insn-00a690d4)

~~~diff
- 00a0b254 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00a0b254 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a0b254 bytes e80700f9
- 00a0b260 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a0b260 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00a0b260 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a0b260 bytes a8831ff8
- 00a0b3a0 ["INT_ADD", "register:40f0:8", ["const:a0b3a0:8", "const:4:8"]]
- 00a0b3a0 ["CALL", null, ["callee:00c538b0:8"]]
+ 00a690d4 ["INT_ADD", "register:40f0:8", ["const:a690d4:8", "const:4:8"]]
+ 00a690d4 ["CALL", null, ["callee:00c538b0:8"]]
- 00a0b3a0 bytes b02e0794
+ 00a690d4 bytes f7a90794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cbd3bdfb69d188b4a48d2a2688542e96"></a>

### [`00a0b478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0b478.md) → [`00a691ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a691ac.md) FUN_00a691ac

採用 · 移動量 `+0x5dd34` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 20.00% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a691c4",
      "incomplete_value": false,
      "site": "00a691c8",
      "value": [
        "leaf",
        "const:ffffffffffffffff:8"
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
      "definition_site": "00a691c0",
      "incomplete_value": true,
      "site": "00a691c8",
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
            "const:8:8"
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

- 旧版 [`00a0b494`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0b478.md#insn-00a0b494) · [`00a0b488`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0b478.md#insn-00a0b488) · [`00a0b498`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0b478.md#insn-00a0b498)
- 新版 [`00a691c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a691ac.md#insn-00a691c8) · [`00a691bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a691ac.md#insn-00a691bc) · [`00a691cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a691ac.md#insn-00a691cc)

~~~diff
- 00a0b494 ["INT_ADD", "register:40f0:8", ["const:a0b494:8", "const:4:8"]]
- 00a0b494 ["CALL", null, ["callee:00c538e0:8"]]
+ 00a691c8 ["INT_ADD", "register:40f0:8", ["const:a691c8:8", "const:4:8"]]
+ 00a691c8 ["CALL", null, ["callee:00c538e0:8"]]
- 00a0b494 bytes 7f2e0794
+ 00a691c8 bytes c6a90794
- 00a0b488 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 00a0b488 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00a691bc ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
+ 00a691bc ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00a0b488 bytes b30000b4
+ 00a691bc bytes b30000b4
- 00a0b498 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00a0b498 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00a691cc ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00a691cc ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00a0b498 bytes 800000b4
+ 00a691cc bytes 800000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e9fcd8899d20f2ba9d61c076a19f75b"></a>

### [`00a0b4c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0b4c8.md) → [`00a691fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a691fc.md) FUN_00a691fc

採用 · 移動量 `+0x5dd34` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`009d1474`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d1/009d1474.md) · 呼出先 1件 [`0045df50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045df50.md)
- 新版 呼出元 1件 [`00a2e370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2e/00a2e370.md) · 呼出先 1件 [`00480de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480de8.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a0b4e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0b4c8.md#insn-00a0b4e8) · [`00a0b4f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0b4c8.md#insn-00a0b4f4)
- 新版 [`00a6921c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a691fc.md#insn-00a6921c) · [`00a69228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a691fc.md#insn-00a69228)

~~~diff
- 00a0b4e8 ["INT_ADD", "register:40f0:8", ["const:a0b4e8:8", "const:4:8"]]
- 00a0b4e8 ["CALL", null, ["callee:00480de8:8"]]
+ 00a6921c ["INT_ADD", "register:40f0:8", ["const:a6921c:8", "const:4:8"]]
+ 00a6921c ["CALL", null, ["callee:00480de8:8"]]
- 00a0b4e8 bytes 9a4ae997
+ 00a6921c bytes f35ee897
- 00a0b4f4 ["INT_ADD", "register:40f0:8", ["const:a0b4f4:8", "const:4:8"]]
- 00a0b4f4 ["CALL", null, ["callee:00480de8:8"]]
+ 00a69228 ["INT_ADD", "register:40f0:8", ["const:a69228:8", "const:4:8"]]
+ 00a69228 ["CALL", null, ["callee:00480de8:8"]]
- 00a0b4f4 bytes 974ae997
+ 00a69228 bytes f05ee897
~~~


<a id="compare-e868ad4e412ab6719887e10289090fc2"></a>

### [`00a0b550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0b550.md) → [`00a69284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69284.md) FUN_00a69284

採用 · 移動量 `+0x5dd34` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`0081c6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081c/0081c6a0.md) · 呼出先 1件 [`00839a8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00839/00839a8c.md)
- 新版 呼出元 1件 [`0084e55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0084e/0084e55c.md) · 呼出先 1件 [`0086bd78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086b/0086bd78.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a0b568`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0b550.md#insn-00a0b568)
- 新版 [`00a6929c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69284.md#insn-00a6929c)

~~~diff
- 00a0b568 ["INT_ADD", "register:40f0:8", ["const:a0b568:8", "const:4:8"]]
- 00a0b568 ["CALL", null, ["callee:0086bd78:8"]]
+ 00a6929c ["INT_ADD", "register:40f0:8", ["const:a6929c:8", "const:4:8"]]
+ 00a6929c ["CALL", null, ["callee:0086bd78:8"]]
- 00a0b568 bytes 49b9f897
+ 00a6929c bytes b70af897
~~~


<a id="compare-cde1abdd289c10660c7b570990756c48"></a>

### [`00a0b584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0b584.md) → [`00a692b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a692b8.md) FUN_00a692b8

採用 · 移動量 `+0x5dd34` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`0090688c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00906/0090688c.md) · 呼出先 2件 [`00a0d1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0d/00a0d1c0.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`0093b2c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093b/0093b2c4.md) · 呼出先 2件 [`00a6ae28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6ae28.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 78.57% / 新版 84.62%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a69304",
      "incomplete_value": true,
      "site": "00a69308",
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
            "const:4:8"
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

- 旧版 [`00a0b5d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0b584.md#insn-00a0b5d4) · [`00a0b5ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0b584.md#insn-00a0b5ac) · [`00a0b5b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0b584.md#insn-00a0b5b4)
- 新版 [`00a69308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a692b8.md#insn-00a69308) · [`00a692e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a692b8.md#insn-00a692e0) · [`00a692e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a692b8.md#insn-00a692e8)

~~~diff
- 00a0b5d4 ["INT_ADD", "register:40f0:8", ["const:a0b5d4:8", "const:4:8"]]
- 00a0b5d4 ["CALL", null, ["callee:00a6ae28:8"]]
+ 00a69308 ["INT_ADD", "register:40f0:8", ["const:a69308:8", "const:4:8"]]
+ 00a69308 ["CALL", null, ["callee:00a6ae28:8"]]
- 00a0b5d4 bytes fb060094
+ 00a69308 bytes c8060094
- 00a0b5ac ["BRANCH", null, ["local:b8:8"]]
+ 00a692e0 ["BRANCH", null, ["local:b7:8"]]
- 00a0b5ac bytes 0b000014
+ 00a692e0 bytes 0b000014
- 00a0b5b4 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00a0b5b4 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 00a692e8 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00a692e8 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00a0b5b4 bytes 280100b4
+ 00a692e8 bytes 280100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae4d54da94434867da327cfbb1056e64"></a>

### [`00a0b6e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0b6e0.md) → [`00a69414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69414.md) FUN_00a69414

採用 · 移動量 `+0x5dd34` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`006f1e2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f1e2c.md) [`009034dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00903/009034dc.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)
- 新版 呼出元 2件 [`0071be98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071b/0071be98.md) [`00937f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00937/00937f14.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)

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
      "site": "00a69474",
      "value": [
        "leaf",
        "ram:4428f0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a0b740",
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
      "definition_site": "00a69470",
      "incomplete_value": false,
      "site": "00a69474",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a0000:8"
          ],
          [
            "leaf",
            "const:f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a0b73c",
      "incomplete_value": false,
      "site": "00a0b740",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:290000:8"
          ],
          [
            "leaf",
            "const:bae:8"
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
      "00a69470",
      "PARAM",
      [
        "storage",
        "00290bae",
        null,
        "string"
      ]
    ],
    [
      "00a69474",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0041fdf0"
      ]
    ]
  ],
  "added": [
    [
      "00a69470",
      "PARAM",
      [
        "storage",
        "002a00f0",
        null,
        "string"
      ]
    ],
    [
      "00a69474",
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

- 旧版 [`00a0b740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0b6e0.md#insn-00a0b740) · [`00a0b738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0b6e0.md#insn-00a0b738) · [`00a0b73c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0b6e0.md#insn-00a0b73c)
- 新版 [`00a69474`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69414.md#insn-00a69474) · [`00a6946c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69414.md#insn-00a6946c) · [`00a69470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69414.md#insn-00a69470)

~~~diff
- 00a0b740 ["INT_ADD", "register:40f0:8", ["const:a0b740:8", "const:4:8"]]
- 00a0b740 ["CALL", null, ["ram:41fdf0:8"]]
+ 00a69474 ["INT_ADD", "register:40f0:8", ["const:a69474:8", "const:4:8"]]
+ 00a69474 ["CALL", null, ["ram:4428f0:8"]]
- 00a0b740 bytes ac51e897
+ 00a69474 bytes 1f65e797
- 00a0b738 ["COPY", "register:4000:8", ["const:290000:8"]]
+ 00a6946c ["COPY", "register:4000:8", ["const:2a0000:8"]]
- 00a0b738 bytes 20c4ffb0
+ 00a6946c bytes a0c1fff0
- 00a0b73c ["COPY", "tmp:0:8", ["const:bae:8"]]
- 00a0b73c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00a0b73c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00a0b73c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00a69470 ["COPY", "tmp:0:8", ["const:f0:8"]]
+ 00a69470 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00a69470 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00a69470 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00a0b73c bytes 00b82e91
+ 00a69470 bytes 00c00391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0f0c944a2a7044546e54ada5f38553b"></a>

### [`00a0b760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0b760.md) → [`00a69494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69494.md) FUN_00a69494

採用 · 移動量 `+0x5dd34` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a0d0cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0d/00a0d0cc.md) · 呼出先 2件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`00a0b864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0b864.md)
- 新版 呼出元 1件 [`00a6ad34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6ad34.md) · 呼出先 2件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`00a69598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69598.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.83% / 新版 96.83%

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
      "site": "00a69500",
      "value": [
        "leaf",
        "ram:4428f0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a0b7cc",
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
      "definition_site": "00a694fc",
      "incomplete_value": false,
      "site": "00a69500",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a0000:8"
          ],
          [
            "leaf",
            "const:f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a0b7c8",
      "incomplete_value": false,
      "site": "00a0b7cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:290000:8"
          ],
          [
            "leaf",
            "const:bae:8"
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
      "00a694fc",
      "PARAM",
      [
        "storage",
        "00290bae",
        null,
        "string"
      ]
    ],
    [
      "00a69500",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0041fdf0"
      ]
    ]
  ],
  "added": [
    [
      "00a694fc",
      "PARAM",
      [
        "storage",
        "002a00f0",
        null,
        "string"
      ]
    ],
    [
      "00a69500",
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

- 旧版 [`00a0b7cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0b760.md#insn-00a0b7cc) · [`00a0b7c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0b760.md#insn-00a0b7c4) · [`00a0b7c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0b760.md#insn-00a0b7c8)
- 新版 [`00a69500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69494.md#insn-00a69500) · [`00a694f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69494.md#insn-00a694f8) · [`00a694fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69494.md#insn-00a694fc)

~~~diff
- 00a0b7cc ["INT_ADD", "register:40f0:8", ["const:a0b7cc:8", "const:4:8"]]
- 00a0b7cc ["CALL", null, ["ram:41fdf0:8"]]
+ 00a69500 ["INT_ADD", "register:40f0:8", ["const:a69500:8", "const:4:8"]]
+ 00a69500 ["CALL", null, ["ram:4428f0:8"]]
- 00a0b7cc bytes 8951e897
+ 00a69500 bytes fc64e797
- 00a0b7c4 ["COPY", "register:4000:8", ["const:290000:8"]]
+ 00a694f8 ["COPY", "register:4000:8", ["const:2a0000:8"]]
- 00a0b7c4 bytes 20c4ffb0
+ 00a694f8 bytes a0c1fff0
- 00a0b7c8 ["COPY", "tmp:0:8", ["const:bae:8"]]
- 00a0b7c8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00a0b7c8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00a0b7c8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00a694fc ["COPY", "tmp:0:8", ["const:f0:8"]]
+ 00a694fc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00a694fc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00a694fc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00a0b7c8 bytes 00b82e91
+ 00a694fc bytes 00c00391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0076b5df0dfddc193b2b582d747e58e5"></a>

### [`00a0b864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0b864.md) → [`00a69598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69598.md) FUN_00a69598

採用 · 移動量 `+0x5dd34` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`006f3154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f3/006f3154.md) [`00a0b760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0b760.md) · 呼出先 11件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`0044abe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044abe4.md) [`0044abfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044abfc.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`0071d1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071d/0071d1bc.md) [`00a69494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69494.md) · 呼出先 11件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`0046da7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046da7c.md) [`0046da94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046da94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 90.12% / 新版 90.12%

CFGの説明率　旧版 67.53% / 新版 72.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 3件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0b8e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0b988"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a69614"
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
      "unmatched:00a0b8e0",
      "DATA",
      [
        "storage",
        "00c0bee0",
        null,
        "pointer"
      ]
    ],
    [
      "00a69734",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00821cb4"
      ]
    ],
    [
      "00a6974c",
      "DATA",
      [
        "storage",
        "0032ff0c",
        null,
        "byte[35]"
      ]
    ]
  ],
  "added": [
    [
      "00a69614",
      "DATA",
      [
        "storage",
        "00c8b500",
        null,
        "pointer"
      ]
    ],
    [
      "00a69734",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00853c30"
      ]
    ],
    [
      "00a6974c",
      "DATA",
      [
        "storage",
        "00333f4c",
        null,
        "fde_table_entry"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a0b8e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0b864.md#insn-00a0b8e0) · [`00a0b988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0b864.md#insn-00a0b988) · [`00a0ba00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0b864.md#insn-00a0ba00)
- 新版 [`00a69734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69598.md#insn-00a69734)

~~~diff
- 00a0b8e0 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00a0b8e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a0b8e0 bytes 080000f9
- 00a0b988 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:10:8"]]
- 00a0b988 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00a0b988 bytes a90a00f9
- 00a0ba00 ["INT_ADD", "register:40f0:8", ["const:a0ba00:8", "const:4:8"]]
- 00a0ba00 ["CALL", null, ["ram:821cb4:8"]]
+ 00a69734 ["INT_ADD", "register:40f0:8", ["const:a69734:8", "const:4:8"]]
+ 00a69734 ["CALL", null, ["ram:853c30:8"]]
- 00a0ba00 bytes ad58f897
+ 00a69734 bytes 3fa9f797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05939429f32390175bff8201a15d48b8"></a>

### [`00a0bc1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0bc1c.md) → [`00a69950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69950.md) FUN_00a69950

採用 · 移動量 `+0x5dd34` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a0d0cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0d/00a0d0cc.md) · 呼出先 7件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`00a0ae20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0a/00a0ae20.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`00a6ad34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6ad34.md) · 呼出先 7件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`00a68af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a68af0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 80.36% / 新版 84.91%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a699d4",
      "incomplete_value": false,
      "site": "00a699d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:500:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a0bca0",
      "incomplete_value": false,
      "site": "00a0bca4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0bd4c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a69a80"
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
      "00a699d8",
      "DATA",
      [
        "storage",
        "00c0bee0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00a0bd48",
      "READ",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a0be00",
      "PARAM",
      [
        "storage",
        "00290bae",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00a699d8",
      "DATA",
      [
        "storage",
        "00c8b500",
        null,
        "pointer"
      ]
    ],
    [
      "00a69a7c",
      "READ",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "00a69b34",
      "PARAM",
      [
        "storage",
        "002a00f0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a0bd4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0bc1c.md#insn-00a0bd4c) · [`00a0bd84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0bc1c.md#insn-00a0bd84) · [`00a0be04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0bc1c.md#insn-00a0be04)

~~~diff
- 00a0bd4c ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:10:8"]]
- 00a0bd4c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00a0bd4c bytes e90a00f9
- 00a0bd84 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a0bd84 ["INT_ADD", "register:40f0:8", ["const:a0bd84:8", "const:4:8"]]
- 00a0bd84 ["CALLIND", null, ["register:0:8"]]
- 00a0bd84 bytes 00013fd6
- 00a0be04 ["INT_ADD", "register:40f0:8", ["const:a0be04:8", "const:4:8"]]
- 00a0be04 ["CALL", null, ["ram:41fdf0:8"]]
- 00a0be04 bytes fb4fe897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6a2ccfa8c974db07a1bf96b0309fec2"></a>

### [`00a0bea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0bea4.md) → [`00a69bd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69bd8.md) FUN_00a69bd8

採用 · 移動量 `+0x5dd34` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a0be80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0be80.md) · 呼出先 19件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md)
- 新版 呼出元 1件 [`00a69bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69bb4.md) · 呼出先 19件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 85.40% / 新版 85.40%

CFGの説明率　旧版 68.04% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0beb4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0beb4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0beb8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a0beb4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a0beb8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a0bed4",
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
      "00a69be8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00a69bec",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a69c08",
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

- 旧版 [`00a0beb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0bea4.md#insn-00a0beb4) · [`00a0beb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0bea4.md#insn-00a0beb8) · [`00a0bed4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0bea4.md#insn-00a0bed4)

~~~diff
- 00a0beb4 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00a0beb4 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00a0beb4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00a0beb4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a0beb4 bytes f65704a9
- 00a0beb8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00a0beb8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00a0beb8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00a0beb8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a0beb8 bytes f44f05a9
- 00a0bed4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a0bed4 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff0:8"]]
- 00a0bed4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a0bed4 bytes a8031ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ab83916fc7c7fa47a753352f5d02567"></a>

### [`00a0c374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0c/00a0c374.md) → [`00a6a0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6a0a8.md) FUN_00a6a0a8

採用 · 移動量 `+0x5dd34` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a0be80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0be80.md) · 呼出先 18件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md) [`0046555c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/0046555c.md) [`00470c48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/00470c48.md)
- 新版 呼出元 1件 [`00a69bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a69bb4.md) · 呼出先 18件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md) [`004883f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/004883f4.md) [`00493ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493ae0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 90.95% / 新版 90.95%

CFGの説明率　旧版 67.61% / 新版 69.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_condition` 1件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0c3b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0c618"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0c61c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a0c3b4",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00a0c3b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x1c8]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a0c3bc",
      "PARAM",
      [
        "storage",
        "0109eca0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00a6a0e8",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "00a6a0e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x1c8]",
        null,
        null
      ]
    ],
    [
      "00a6a0f0",
      "PARAM",
      [
        "storage",
        "01123b10",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a0c3b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0c/00a0c374.md#insn-00a0c3b4) · [`00a0c3cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0c/00a0c374.md#insn-00a0c3cc) · [`00a0c44c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0c/00a0c374.md#insn-00a0c44c)
- 新版 [`00a6a100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6a0a8.md#insn-00a6a100) · [`00a6a180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6a0a8.md#insn-00a6a180)

~~~diff
- 00a0c3b4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:38:8"]]
- 00a0c3b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a0c3b4 bytes e81f00f9
- 00a0c3cc ["INT_ADD", "register:40f0:8", ["const:a0c3cc:8", "const:4:8"]]
- 00a0c3cc ["CALL", null, ["callee:00b10cc4:8"]]
+ 00a6a100 ["INT_ADD", "register:40f0:8", ["const:a6a100:8", "const:4:8"]]
+ 00a6a100 ["CALL", null, ["callee:00b10cc4:8"]]
- 00a0c3cc bytes 9a930294
+ 00a6a100 bytes f19a0294
- 00a0c44c ["INT_ADD", "register:40f0:8", ["const:a0c44c:8", "const:4:8"]]
- 00a0c44c ["CALL", null, ["callee:0044104c:8"]]
+ 00a6a180 ["INT_ADD", "register:40f0:8", ["const:a6a180:8", "const:4:8"]]
+ 00a6a180 ["CALL", null, ["callee:0044104c:8"]]
- 00a0c44c bytes 4048e897
+ 00a6a180 bytes b35be797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38950eec8a645185bfa32967db83357c"></a>

### [`00a0c7ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0c/00a0c7ac.md) → [`00a6a4e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6a4e0.md) FUN_00a6a4e0

採用 · 移動量 `+0x5dd34` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`0073465c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00734/0073465c.md) [`0073496c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00734/0073496c.md) · 呼出先 1件 [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md)
- 新版 呼出元 2件 [`0075e830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075e830.md) [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) · 呼出先 1件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a0c7c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0c/00a0c7ac.md#insn-00a0c7c4)
- 新版 [`00a6a4f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6a4e0.md#insn-00a6a4f8)

~~~diff
- 00a0c7c4 ["INT_ADD", "register:40f0:8", ["const:a0c7c4:8", "const:4:8"]]
- 00a0c7c4 ["CALL", null, ["callee:005c175c:8"]]
+ 00a6a4f8 ["INT_ADD", "register:40f0:8", ["const:a6a4f8:8", "const:4:8"]]
+ 00a6a4f8 ["CALL", null, ["callee:005c175c:8"]]
- 00a0c7c4 bytes 5a42ee97
+ 00a6a4f8 bytes 995ced97
~~~


<a id="compare-11a8d4feb32a9e68e5c39edbff392e15"></a>

### [`00a0cb24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0c/00a0cb24.md) → [`00a6a858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6a858.md) FUN_00a6a858

採用 · 移動量 `+0x5dd34` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009034dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00903/009034dc.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)
- 新版 呼出元 1件 [`00937f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00937/00937f14.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.55% / 新版 93.55%

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
      "site": "00a6a8b8",
      "value": [
        "leaf",
        "ram:4428f0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a0cb84",
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
      "definition_site": "00a6a8b4",
      "incomplete_value": false,
      "site": "00a6a8b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a0000:8"
          ],
          [
            "leaf",
            "const:f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a0cb80",
      "incomplete_value": false,
      "site": "00a0cb84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:290000:8"
          ],
          [
            "leaf",
            "const:bae:8"
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
      "00a6a8b4",
      "PARAM",
      [
        "storage",
        "00290bae",
        null,
        "string"
      ]
    ],
    [
      "00a6a8b8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0041fdf0"
      ]
    ]
  ],
  "added": [
    [
      "00a6a8b4",
      "PARAM",
      [
        "storage",
        "002a00f0",
        null,
        "string"
      ]
    ],
    [
      "00a6a8b8",
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

- 旧版 [`00a0cb84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0c/00a0cb24.md#insn-00a0cb84) · [`00a0cb7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0c/00a0cb24.md#insn-00a0cb7c) · [`00a0cb80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0c/00a0cb24.md#insn-00a0cb80)
- 新版 [`00a6a8b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6a858.md#insn-00a6a8b8) · [`00a6a8b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6a858.md#insn-00a6a8b0) · [`00a6a8b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6a858.md#insn-00a6a8b4)

~~~diff
- 00a0cb84 ["INT_ADD", "register:40f0:8", ["const:a0cb84:8", "const:4:8"]]
- 00a0cb84 ["CALL", null, ["ram:41fdf0:8"]]
+ 00a6a8b8 ["INT_ADD", "register:40f0:8", ["const:a6a8b8:8", "const:4:8"]]
+ 00a6a8b8 ["CALL", null, ["ram:4428f0:8"]]
- 00a0cb84 bytes 9b4ce897
+ 00a6a8b8 bytes 0e60e797
- 00a0cb7c ["COPY", "register:4000:8", ["const:290000:8"]]
+ 00a6a8b0 ["COPY", "register:4000:8", ["const:2a0000:8"]]
- 00a0cb7c bytes 20c4ff90
+ 00a6a8b0 bytes a0c1ffd0
- 00a0cb80 ["COPY", "tmp:0:8", ["const:bae:8"]]
- 00a0cb80 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00a0cb80 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00a0cb80 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00a6a8b4 ["COPY", "tmp:0:8", ["const:f0:8"]]
+ 00a6a8b4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00a6a8b4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00a6a8b4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00a0cb80 bytes 00b82e91
+ 00a6a8b4 bytes 00c00391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa6c1e7026c8ddeacaddaad8cc749e38"></a>

### [`00a0d030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0d/00a0d030.md) → [`00a6ac98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6ac98.md) FUN_00a6ac98

採用 · 移動量 `+0x5dc68` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`006eccf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ec/006eccf4.md) [`009f4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f4/009f4ab8.md) · 呼出先 3件 [`00a0ce38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0c/00a0ce38.md) [`00a0e0cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0e/00a0e0cc.md) [`00a0e450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0e/00a0e450.md)
- 新版 呼出元 2件 [`00716d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00716/00716d50.md) [`00a51dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a51/00a51dcc.md) · 呼出先 3件 [`00a6aaa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6aaa4.md) [`00a6bee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6b/00a6bee4.md) [`00a6c290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6c/00a6c290.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 96.88% / 新版 96.88%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00a0d044",
      "incomplete_value": true,
      "site": "00a0d05c",
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
                "register:4000:8"
              ],
              [
                "leaf",
                "const:70:8"
              ]
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
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0d080"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00a6ace8"
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
      "unmatched:00a0d080",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a0ce38"
      ]
    ]
  ],
  "added": [
    [
      "00a6ace8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a6aaa4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a0d05c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0d/00a0d030.md#insn-00a0d05c) · [`00a0d080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0d/00a0d030.md#insn-00a0d080)
- 新版 [`00a6acc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6ac98.md#insn-00a6acc4) · [`00a6ace8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6ac98.md#insn-00a6ace8)

~~~diff
- 00a0d05c ["INT_ADD", "register:40f0:8", ["const:a0d05c:8", "const:4:8"]]
- 00a0d05c ["CALL", null, ["callee:00a6c290:8"]]
+ 00a6acc4 ["INT_ADD", "register:40f0:8", ["const:a6acc4:8", "const:4:8"]]
+ 00a6acc4 ["CALL", null, ["callee:00a6c290:8"]]
- 00a0d05c bytes fd040094
+ 00a6acc4 bytes 73050094
- 00a0d080 ["INT_ADD", "register:40f0:8", ["const:a0d080:8", "const:4:8"]]
- 00a0d080 ["CALL", null, ["ram:a0ce38:8"]]
- 00a0d080 bytes 6effff97
+ 00a6ace8 ["INT_ADD", "register:40f0:8", ["const:a6ace8:8", "const:4:8"]]
+ 00a6ace8 ["CALL", null, ["ram:a6aaa4:8"]]
+ 00a6ace8 bytes 6fffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f06d713a47b2e5c863fa8fe9e52bb1a"></a>

### [`00a0d1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0d/00a0d1b0.md) → [`00a6ae18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6ae18.md) FUN_00a6ae18

採用 · 移動量 `+0x5dc68` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 1件 [`00a0b228`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0b228.md) · 呼出先 1件 [`0059d170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d170.md)
- 新版 呼出元 1件 [`00a68f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a68f5c.md) · 呼出先 1件 [`005c17a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c17a0.md)

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a0d1b8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "005c17a0"
      ]
    ]
  ],
  "added": [
    [
      "00a6ae20",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "005c17a0"
      ]
    ]
  ]
}
~~~


<a id="compare-5b841748c04937278ced46e795ba539b"></a>

### [`00a0d1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0d/00a0d1c0.md) → [`00a6ae28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6ae28.md) FUN_00a6ae28

採用 · 移動量 `+0x5dc68` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a0b584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0b/00a0b584.md) · 呼出先 4件 [`00471738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471738.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00a692b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a69/00a692b8.md) · 呼出先 4件 [`004945d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004945d0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 79.37% / 新版 79.37%

CFGの説明率　旧版 14.29% / 新版 20.69%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_condition` 1件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0d26c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a6aed4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0d1f4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a0d214",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a6ae88"
      ]
    ],
    [
      "unmatched:00a0d230",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a6ae90"
      ]
    ],
    [
      "00a6ae9c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00a0d250"
      ]
    ]
  ],
  "added": [
    [
      "00a6ae7c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a6ae88"
      ]
    ],
    [
      "00a6ae98",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a6ae90"
      ]
    ],
    [
      "00a6ae9c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00a6aeb8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a0d1f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0d/00a0d1c0.md#insn-00a0d1f4) · [`00a0d214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0d/00a0d1c0.md#insn-00a0d214) · [`00a0d230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0d/00a0d1c0.md#insn-00a0d230)

~~~diff
- 00a0d1f4 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00a0d1f4 ["COPY", "tmp:1:8", ["register:4058:8"]]
- 00a0d1f4 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00a0d1f4 ["COPY", "tmp:1:8", ["register:4060:8"]]
- 00a0d1f4 bytes 6bb18c9a
- 00a0d214 ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00a0d214 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 00a0d214 bytes 6a000054
- 00a0d230 ["INT_NOTEQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
- 00a0d230 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 00a0d230 bytes caffffb5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afdab63eac9682fbd94c9a983716de5f"></a>

### [`00a0d2bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0d/00a0d2bc.md) → [`00a6af24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6af24.md) _INIT_222

採用 · 移動量 `+0x5dc68` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00b5565c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b5565c.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00bc43c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc43c8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 69.42% / 新版 69.42%

CFGの説明率　旧版 18.75% / 新版 27.27%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 17件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0d2ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0d314"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0d338"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a0d2ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a0d2f8",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00a0d314",
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
      "00a6af54",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00a6af60",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00a6af7c",
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

- 旧版 [`00a0d2ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0d/00a0d2bc.md#insn-00a0d2ec) · [`00a0d314`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0d/00a0d2bc.md#insn-00a0d314) · [`00a0d338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0d/00a0d2bc.md#insn-00a0d338)

~~~diff
- 00a0d2ec ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00a0d2ec ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00a0d2ec ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a0d2ec bytes a9831ff8
- 00a0d314 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:21:8"]]
- 00a0d314 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00a0d314 bytes e013823c
- 00a0d338 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:41:8"]]
- 00a0d338 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00a0d338 bytes e013843c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1cbcf0531de68a57d0baa59eddf11d9e"></a>

### [`00a0d8b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0d/00a0d8b8.md) → [`00a6b520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6b/00a6b520.md) FUN_00a6b520

採用 · 移動量 `+0x5dc68` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a0ce38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0c/00a0ce38.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00a6aaa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6aaa4.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 84.00% / 新版 87.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a0d8c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0d/00a0d8b8.md#insn-00a0d8c4) · [`00a0d8dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0d/00a0d8b8.md#insn-00a0d8dc) · [`00a0d8f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0d/00a0d8b8.md#insn-00a0d8f0)
- 新版 [`00a6b52c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6b/00a6b520.md#insn-00a6b52c) · [`00a6b544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6b/00a6b520.md#insn-00a6b544) · [`00a6b558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6b/00a6b520.md#insn-00a6b558)

~~~diff
- 00a0d8c4 ["CBRANCH", null, ["local:b11:8", "register:101:1"]]
+ 00a6b52c ["CBRANCH", null, ["local:b10:8", "register:101:1"]]
- 00a0d8c4 bytes 00030054
+ 00a6b52c bytes 00030054
- 00a0d8dc ["CBRANCH", null, ["local:b11:8", "register:101:1"]]
+ 00a6b544 ["CBRANCH", null, ["local:b10:8", "register:101:1"]]
- 00a0d8dc bytes 40020054
+ 00a6b544 bytes 40020054
- 00a0d8f0 ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00a0d8f0 ["CBRANCH", null, ["local:b15:8", "tmp:0:1"]]
+ 00a6b558 ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 00a6b558 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 00a0d8f0 bytes 0a030054
+ 00a6b558 bytes 0a030054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4f2141aea5767b93d368e6e62ee28b7"></a>

### [`00a0e080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0e/00a0e080.md) → [`00a6be98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6b/00a6be98.md) FUN_00a6be98

採用 · 移動量 `+0x5de18` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.47% / 新版 89.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a6beb8",
      "incomplete_value": false,
      "site": "00a6bec0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:550:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a0e0a0",
      "incomplete_value": false,
      "site": "00a0e0a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:f30:8"
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
      "00a6bec0",
      "DATA",
      [
        "storage",
        "00c0bf30",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00a6bec0",
      "DATA",
      [
        "storage",
        "00c8b550",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a0e09c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0e/00a0e080.md#insn-00a0e09c) · [`00a0e0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0e/00a0e080.md#insn-00a0e0a0) · [`00a0e0ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0e/00a0e080.md#insn-00a0e0ac)
- 新版 [`00a6beb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6b/00a6be98.md#insn-00a6beb4) · [`00a6beb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6b/00a6be98.md#insn-00a6beb8) · [`00a6bec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6b/00a6be98.md#insn-00a6bec4)

~~~diff
- 00a0e09c ["COPY", "register:4040:8", ["const:c0b000:8"]]
+ 00a6beb4 ["COPY", "register:4040:8", ["const:c8b000:8"]]
- 00a0e09c bytes e80f00b0
+ 00a6beb4 bytes 08110090
- 00a0e0a0 ["COPY", "tmp:0:8", ["const:f30:8"]]
- 00a0e0a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a0e0a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a0e0a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a6beb8 ["COPY", "tmp:0:8", ["const:550:8"]]
+ 00a6beb8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a6beb8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a6beb8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a0e0a0 bytes 08c13c91
+ 00a6beb8 bytes 08411591
- 00a0e0ac ["INT_ADD", "register:40f0:8", ["const:a0e0ac:8", "const:4:8"]]
- 00a0e0ac ["CALL", null, ["callee:005c175c:8"]]
+ 00a6bec4 ["INT_ADD", "register:40f0:8", ["const:a6bec4:8", "const:4:8"]]
+ 00a6bec4 ["CALL", null, ["callee:005c175c:8"]]
- 00a0e0ac bytes 203cee97
+ 00a6bec4 bytes 2656ed97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43d07b07030b584ab7d54b8ecb18b0cb"></a>

### [`00a0e128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0e/00a0e128.md) → [`00a6bf40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6b/00a6bf40.md) FUN_00a6bf40

採用 · 移動量 `+0x5de18` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 1件 [`00a0cba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0c/00a0cba0.md) · 呼出先 1件 [`0051d884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d884.md)
- 新版 呼出元 1件 [`00a6a8d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6a8d4.md) · 呼出先 1件 [`0054071c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/0054071c.md)

変更の種類 cfg_edge_inventory

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a0e14c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0054071c"
      ]
    ]
  ],
  "added": [
    [
      "00a6bf64",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0054071c"
      ]
    ]
  ]
}
~~~


<a id="compare-f8b5a729c4b651bda628deede9abaa80"></a>

### [`00a0e150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0e/00a0e150.md) → [`00a6bf68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6b/00a6bf68.md) FUN_00a6bf68

採用 · 移動量 `+0x5de18` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a0cba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0c/00a0cba0.md) · 呼出先 3件 [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00a6a8d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6a/00a6a8d4.md) · 呼出先 3件 [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 60.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a0e178`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0e/00a0e150.md#insn-00a0e178) · [`00a0e180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0e/00a0e150.md#insn-00a0e180) · [`00a0e198`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0e/00a0e150.md#insn-00a0e198)
- 新版 [`00a6bf90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6b/00a6bf68.md#insn-00a6bf90) · [`00a6bf98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6b/00a6bf68.md#insn-00a6bf98) · [`00a6bfb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6b/00a6bf68.md#insn-00a6bfb0)

~~~diff
- 00a0e178 ["INT_RIGHT", "tmp:0:8", ["register:40a8:8", "const:3f:4"]]
- 00a0e178 ["INT_AND", "tmp:1:8", ["tmp:0:8", "const:1:8"]]
- 00a0e178 ["INT_EQUAL", "tmp:2:1", ["tmp:1:8", "const:0:8"]]
- 00a0e178 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00a6bf90 ["INT_RIGHT", "tmp:0:8", ["register:40a8:8", "const:3f:4"]]
+ 00a6bf90 ["INT_AND", "tmp:1:8", ["tmp:0:8", "const:1:8"]]
+ 00a6bf90 ["INT_EQUAL", "tmp:2:1", ["tmp:1:8", "const:0:8"]]
+ 00a6bf90 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00a0e178 bytes d501f8b7
+ 00a6bf90 bytes d501f8b7
- 00a0e180 ["INT_ADD", "register:40f0:8", ["const:a0e180:8", "const:4:8"]]
- 00a0e180 ["CALL", null, ["callee:00c57a90:8"]]
+ 00a6bf98 ["INT_ADD", "register:40f0:8", ["const:a6bf98:8", "const:4:8"]]
+ 00a6bf98 ["CALL", null, ["callee:00c57a90:8"]]
- 00a0e180 bytes b0330794
+ 00a6bf98 bytes beae0794
- 00a0e198 ["INT_ADD", "register:40f0:8", ["const:a0e198:8", "const:4:8"]]
- 00a0e198 ["CALL", null, ["callee:00c57c00:8"]]
+ 00a6bfb0 ["INT_ADD", "register:40f0:8", ["const:a6bfb0:8", "const:4:8"]]
+ 00a6bfb0 ["CALL", null, ["callee:00c57c00:8"]]
- 00a0e198 bytes 06340794
+ 00a6bfb0 bytes 14af0794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98a725433571d314090cb55b5cb9c17d"></a>

### [`00a0e53c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0e/00a0e53c.md) → [`00a6c37c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6c/00a6c37c.md) FUN_00a6c37c

採用 · 移動量 `+0x5de40` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a6c398",
      "incomplete_value": false,
      "site": "00a6c3a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:550:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a0e558",
      "incomplete_value": false,
      "site": "00a0e560",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:f30:8"
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
      "00a6c3a0",
      "DATA",
      [
        "storage",
        "00c0bf30",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00a6c3a0",
      "DATA",
      [
        "storage",
        "00c8b550",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a0e554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0e/00a0e53c.md#insn-00a0e554) · [`00a0e558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0e/00a0e53c.md#insn-00a0e558) · [`00a0e564`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0e/00a0e53c.md#insn-00a0e564)
- 新版 [`00a6c394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6c/00a6c37c.md#insn-00a6c394) · [`00a6c398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6c/00a6c37c.md#insn-00a6c398) · [`00a6c3a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6c/00a6c37c.md#insn-00a6c3a4)

~~~diff
- 00a0e554 ["COPY", "register:4040:8", ["const:c0b000:8"]]
+ 00a6c394 ["COPY", "register:4040:8", ["const:c8b000:8"]]
- 00a0e554 bytes e80f00b0
+ 00a6c394 bytes e81000f0
- 00a0e558 ["COPY", "tmp:0:8", ["const:f30:8"]]
- 00a0e558 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a0e558 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a0e558 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a6c398 ["COPY", "tmp:0:8", ["const:550:8"]]
+ 00a6c398 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a6c398 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a6c398 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a0e558 bytes 08c13c91
+ 00a6c398 bytes 08411591
- 00a0e564 ["INT_ADD", "register:40f0:8", ["const:a0e564:8", "const:4:8"]]
- 00a0e564 ["CALL", null, ["callee:005c175c:8"]]
+ 00a6c3a4 ["INT_ADD", "register:40f0:8", ["const:a6c3a4:8", "const:4:8"]]
+ 00a6c3a4 ["CALL", null, ["callee:005c175c:8"]]
- 00a0e564 bytes f23aee97
+ 00a6c3a4 bytes ee54ed97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84eae8eb6af2932da5f2884e3bc4bcc9"></a>

### [`00a0eadc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0e/00a0eadc.md) → [`00a6c954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6c/00a6c954.md) _INIT_224

採用 · 移動量 `+0x5de78` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.23% / 新版 67.23%

CFGの説明率　旧版 37.84% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 23件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0eae0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0eae0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0eae4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a0eae0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a0eae4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a0eae8",
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
      "00a6c958",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00a6c95c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00a6c960",
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

- 旧版 [`00a0eae0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0e/00a0eadc.md#insn-00a0eae0) · [`00a0eae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0e/00a0eadc.md#insn-00a0eae4) · [`00a0eae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0e/00a0eadc.md#insn-00a0eae8)

~~~diff
- 00a0eae0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a0eae0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a0eae0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:f0:8"]]
- 00a0eae0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a0eae0 bytes fd7b0fa9
- 00a0eae4 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00a0eae4 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00a0eae4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:100:8"]]
- 00a0eae4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a0eae4 bytes fc5710a9
- 00a0eae8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00a0eae8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00a0eae8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:110:8"]]
- 00a0eae8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a0eae8 bytes f44f11a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ee46582385122ee1a55f619a1c32788"></a>

### [`00a0ee6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0e/00a0ee6c.md) → [`00a6cce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6c/00a6cce4.md) FUN_00a6cce4

採用 · 移動量 `+0x5de78` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a0fc64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0f/00a0fc64.md) · 呼出先 13件 [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`00657e7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00657/00657e7c.md)
- 新版 呼出元 1件 [`00a6dadc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a6d/00a6dadc.md) · 呼出先 13件 [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`0067e15c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067e/0067e15c.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 43.16% / 新版 43.16%

CFGの説明率　旧版 22.83% / 新版 26.48%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 15件, `unresolved_branch_alignment` 36件, `unresolved_call_alignment` 49件, `unresolved_store_alignment` 118件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0ee70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0ee70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a0ee74"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a0ee70",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a0ee74",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a0ee78",
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
      "00a6cce8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00a6ccec",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00a6ccf0",
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

- 旧版 [`00a0ee70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0e/00a0ee6c.md#insn-00a0ee70) · [`00a0ee74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0e/00a0ee6c.md#insn-00a0ee74) · [`00a0ee78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a0e/00a0ee6c.md#insn-00a0ee78)

~~~diff
- 00a0ee70 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a0ee70 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a0ee70 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:c0:8"]]
- 00a0ee70 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a0ee70 bytes fd7b0ca9
- 00a0ee74 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00a0ee74 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00a0ee74 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:d0:8"]]
- 00a0ee74 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a0ee74 bytes fc670da9
- 00a0ee78 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00a0ee78 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00a0ee78 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:e0:8"]]
- 00a0ee78 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a0ee78 bytes f85f0ea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

