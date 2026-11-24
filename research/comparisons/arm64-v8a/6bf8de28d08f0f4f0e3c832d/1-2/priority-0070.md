# v16.0.1 → v16.0.2 · 最優先の変更候補 (70)

[一覧の目次](README.md)

<a id="compare-abde041634109eeee0e8ef1b189e227e"></a>

### [`00b3f9bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3f/00b3f9bc.md) → [`00b3fa58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3f/00b3fa58.md) FUN_00b3fa58

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00b3fa64",
      "incomplete_value": false,
      "site": "00b3fa64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8f000:8"
          ],
          [
            "leaf",
            "const:638:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b3f9c8",
      "incomplete_value": false,
      "site": "00b3f9c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8f000:8"
          ],
          [
            "leaf",
            "const:568:8"
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
      "00b3fa64",
      "DATA",
      [
        "storage",
        "00c8f568",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b3fa64",
      "DATA",
      [
        "storage",
        "00c8f638",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b3f9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3f/00b3f9bc.md#insn-00b3f9c4)
- 新版 [`00b3fa60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3f/00b3fa58.md#insn-00b3fa60)

~~~diff
- 00b3f9c4 ["COPY", "tmp:0:8", ["const:568:8"]]
- 00b3f9c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00b3f9c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00b3f9c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00b3fa60 ["COPY", "tmp:0:8", ["const:638:8"]]
+ 00b3fa60 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00b3fa60 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00b3fa60 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00b3f9c4 bytes 29a11591
+ 00b3fa60 bytes 29e11891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-506f981b7b92bb669d2a7d9a5f5a6936"></a>

### [`00b3f9d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3f/00b3f9d8.md) → [`00b3fa74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3f/00b3fa74.md) FUN_00b3fa74

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00468804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468804.md) [`0048ab30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ab30.md) [`008b9298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9298.md) [`00c58610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58610.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00467b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467b6c.md) [`00468844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468844.md) [`0048ab70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048ab70.md) [`008b92f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b92f0.md) [`00c586e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c586e0.md)

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 69.64% / 新版 69.64%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3f9d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3f9d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3f9dc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b3f9d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b3f9dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b3f9e0",
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
      "00b3fa74",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b3fa78",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b3fa7c",
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

- 旧版 [`00b3f9d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3f/00b3f9d8.md#insn-00b3f9d8) · [`00b3f9dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3f/00b3f9d8.md#insn-00b3f9dc) · [`00b3f9e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3f/00b3f9d8.md#insn-00b3f9e0)

~~~diff
- 00b3f9d8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b3f9d8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b3f9d8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 00b3f9d8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b3f9d8 bytes fd7bbba9
- 00b3f9dc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00b3f9dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 00b3f9dc bytes f90b00f9
- 00b3f9e0 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b3f9e0 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b3f9e0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b3f9e0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b3f9e0 bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7d38e19eff4f0790d0261bd86e37d5e"></a>

### [`00b3fae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3f/00b3fae0.md) → [`00b3fb7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3f/00b3fb7c.md) _INIT_276

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 79.10% / 新版 79.10%

CFGの説明率　旧版 57.14% / 新版 55.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3fb10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3fb24"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3fb28"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b3fb10",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b3fb1c",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b3fb24",
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
      "00b3fbac",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00b3fbb8",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "00b3fbc0",
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

- 旧版 [`00b3fb10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3f/00b3fae0.md#insn-00b3fb10) · [`00b3fb24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3f/00b3fae0.md#insn-00b3fb24) · [`00b3fb28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3f/00b3fae0.md#insn-00b3fb28)

~~~diff
- 00b3fb10 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b3fb10 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00b3fb10 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b3fb10 bytes a9831ff8
- 00b3fb24 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 00b3fb24 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:21:8"]]
- 00b3fb24 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 00b3fb24 bytes ea130278
- 00b3fb28 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 00b3fb28 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00b3fb28 bytes e92b00b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-965e673793a683bae774e6a52003fb04"></a>

### [`00b3ff28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3f/00b3ff28.md) → [`00b3ffc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3f/00b3ffc4.md) _ZN8firebase9analytics8internal10FutureData7DestroyEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5acd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5acd0.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ac50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac50.md)
- 新版 呼出元 1件 [`00c5ada0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ada0.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ad20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad20.md)

変更の種類 branch_value, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 25.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `branch_value` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b3ffdc",
      "incomplete_value": true,
      "site": "00b3ffdc",
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
      "definition_site": "00b3ff40",
      "incomplete_value": true,
      "site": "00b3ff40",
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
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3ff60"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b3fffc"
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
      "00b3ffd4",
      "READ",
      [
        "storage",
        "00c9b6a0",
        null,
        "pointer"
      ]
    ],
    [
      "00b3ffd8",
      "READ",
      [
        "storage",
        "01125328",
        "_ZN8firebase9analytics8internal10FutureData14s_future_data_E",
        "undefined8"
      ]
    ],
    [
      "00b3fff4",
      "WRITE",
      [
        "storage",
        "01125328",
        "_ZN8firebase9analytics8internal10FutureData14s_future_data_E",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b3ffd4",
      "READ",
      [
        "storage",
        "00c9b770",
        null,
        "pointer"
      ]
    ],
    [
      "00b3ffd8",
      "READ",
      [
        "storage",
        "01125428",
        "_ZN8firebase9analytics8internal10FutureData14s_future_data_E",
        "undefined8"
      ]
    ],
    [
      "00b3fff4",
      "WRITE",
      [
        "storage",
        "01125428",
        "_ZN8firebase9analytics8internal10FutureData14s_future_data_E",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b3ff60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3f/00b3ff28.md#insn-00b3ff60) · [`00b3ff38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3f/00b3ff28.md#insn-00b3ff38)
- 新版 [`00b3fffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3f/00b3ffc4.md#insn-00b3fffc) · [`00b3ffd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3f/00b3ffc4.md#insn-00b3ffd4)

~~~diff
- 00b3ff60 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b3ff60 ["RETURN", null, ["register:0:8"]]
- 00b3ff60 bytes c0035fd6
+ 00b3fffc ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b3fffc ["RETURN", null, ["register:0:8"]]
+ 00b3fffc bytes c0035fd6
- 00b3ff38 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6a0:8"]]
- 00b3ff38 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b3ffd4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:770:8"]]
+ 00b3ffd4 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00b3ff38 bytes 945243f9
+ 00b3ffd4 bytes 94ba43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2aa072cec17bd8f04e3483cc4ce77ce"></a>

### [`00b3ff64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3f/00b3ff64.md) → [`00b40000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40000.md) _ZN8firebase9analytics8internal10FutureData3GetEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5acb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5acb0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5ad80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad80.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b40008",
      "incomplete_value": true,
      "site": "00b4000c",
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
      "definition_site": "00b3ff6c",
      "incomplete_value": true,
      "site": "00b3ff70",
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
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b40004",
      "READ",
      [
        "storage",
        "00c9b6a0",
        null,
        "pointer"
      ]
    ],
    [
      "00b40008",
      "READ",
      [
        "storage",
        "01125328",
        "_ZN8firebase9analytics8internal10FutureData14s_future_data_E",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b40004",
      "READ",
      [
        "storage",
        "00c9b770",
        null,
        "pointer"
      ]
    ],
    [
      "00b40008",
      "READ",
      [
        "storage",
        "01125428",
        "_ZN8firebase9analytics8internal10FutureData14s_future_data_E",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b3ff68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3f/00b3ff64.md#insn-00b3ff68)
- 新版 [`00b40004`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40000.md#insn-00b40004)

~~~diff
- 00b3ff68 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:6a0:8"]]
- 00b3ff68 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b40004 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:770:8"]]
+ 00b40004 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b3ff68 bytes 085143f9
+ 00b40004 bytes 08b943f9
~~~


<a id="compare-cb09340e65c3ef4467149de6ce528e87"></a>

### [`00b3ff74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3f/00b3ff74.md) → [`00b40010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40010.md) _ZN8firebase9analytics8internal36RegisterTerminateOnDefaultAppDestroyEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5acf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5acf0.md) · 呼出先 5件 [`00b40380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40380.md) [`00c5abd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abd0.md) [`00c5abf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abf0.md) [`00c5ac00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac00.md) [`00c5ac60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac60.md)
- 新版 呼出元 1件 [`00c5adc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5adc0.md) · 呼出先 5件 [`00b4041c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b4041c.md) [`00c5aca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aca0.md) [`00c5acc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5acc0.md) [`00c5acd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5acd0.md) [`00c5ad30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 89.47% / 新版 89.47%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b40024",
      "incomplete_value": true,
      "site": "00b40028",
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
      "definition_site": "00b3ff88",
      "incomplete_value": true,
      "site": "00b3ff8c",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b3ff84",
      "READ",
      [
        "storage",
        "00c9b6a8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b3ff88",
      "READ",
      [
        "storage",
        "00ca4630",
        "_ZN8firebase9analytics8internal20kAnalyticsModuleNameE",
        "pointer"
      ]
    ],
    [
      "unmatched:00b3ff88",
      "PARAM",
      [
        "storage",
        "002a835d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b40020",
      "READ",
      [
        "storage",
        "00c9b778",
        null,
        "pointer"
      ]
    ],
    [
      "00b40024",
      "READ",
      [
        "storage",
        "00ca4700",
        "_ZN8firebase9analytics8internal20kAnalyticsModuleNameE",
        "pointer"
      ]
    ],
    [
      "00b40024",
      "PARAM",
      [
        "storage",
        "002a8301",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b3ff8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3f/00b3ff74.md#insn-00b3ff8c) · [`00b3ff84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3f/00b3ff74.md#insn-00b3ff84) · [`00b3ff88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3f/00b3ff74.md#insn-00b3ff88)
- 新版 [`00b40028`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40010.md#insn-00b40028)

~~~diff
- 00b3ff8c ["INT_ADD", "register:40f0:8", ["const:b3ff8c:8", "const:4:8"]]
- 00b3ff8c ["CALL", null, ["callee:00c5aca0:8"]]
+ 00b40028 ["INT_ADD", "register:40f0:8", ["const:b40028:8", "const:4:8"]]
+ 00b40028 ["CALL", null, ["callee:00c5aca0:8"]]
- 00b3ff8c bytes 116b0494
+ 00b40028 bytes 1e6b0494
- 00b3ff84 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a8:8"]]
- 00b3ff84 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
- 00b3ff84 bytes 735643f9
- 00b3ff88 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b3ff88 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00b3ff88 bytes 600240f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b45e39c60de4116c771fb6e97e45fdd"></a>

### [`00b3ffc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3f/00b3ffc0.md) → [`00b4005c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b4005c.md) _ZN8firebase9analytics8internal38UnregisterTerminateOnDefaultAppDestroyEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 1件 [`00c5ad00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad00.md) · 呼出先 5件 [`00c5abd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abd0.md) [`00c5abf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abf0.md) [`00c5ac10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac10.md) [`00c5ac60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac60.md) [`00c5ace0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ace0.md)
- 新版 呼出元 1件 [`00c5add0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5add0.md) · 呼出先 5件 [`00c5aca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aca0.md) [`00c5acc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5acc0.md) [`00c5ace0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ace0.md) [`00c5ad30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad30.md) [`00c5adb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5adb0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 16.67% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b40070",
      "incomplete_value": true,
      "site": "00b40074",
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
      "definition_site": "00b3ffd4",
      "incomplete_value": true,
      "site": "00b3ffd8",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4006c",
      "READ",
      [
        "storage",
        "00c9b6a8",
        null,
        "pointer"
      ]
    ],
    [
      "00b40070",
      "READ",
      [
        "storage",
        "00ca4630",
        "_ZN8firebase9analytics8internal20kAnalyticsModuleNameE",
        "pointer"
      ]
    ],
    [
      "00b40070",
      "PARAM",
      [
        "storage",
        "002a835d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4006c",
      "READ",
      [
        "storage",
        "00c9b778",
        null,
        "pointer"
      ]
    ],
    [
      "00b40070",
      "READ",
      [
        "storage",
        "00ca4700",
        "_ZN8firebase9analytics8internal20kAnalyticsModuleNameE",
        "pointer"
      ]
    ],
    [
      "00b40070",
      "PARAM",
      [
        "storage",
        "002a8301",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b3ffd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3f/00b3ffc0.md#insn-00b3ffd8) · [`00b3ffd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3f/00b3ffc0.md#insn-00b3ffd0) · [`00b3ffdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3f/00b3ffc0.md#insn-00b3ffdc)
- 新版 [`00b40074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b4005c.md#insn-00b40074) · [`00b4006c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b4005c.md#insn-00b4006c) · [`00b40078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b4005c.md#insn-00b40078)

~~~diff
- 00b3ffd8 ["INT_ADD", "register:40f0:8", ["const:b3ffd8:8", "const:4:8"]]
- 00b3ffd8 ["CALL", null, ["callee:00c5aca0:8"]]
+ 00b40074 ["INT_ADD", "register:40f0:8", ["const:b40074:8", "const:4:8"]]
+ 00b40074 ["CALL", null, ["callee:00c5aca0:8"]]
- 00b3ffd8 bytes fe6a0494
+ 00b40074 bytes 0b6b0494
- 00b3ffd0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a8:8"]]
- 00b3ffd0 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4006c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:778:8"]]
+ 00b4006c ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
- 00b3ffd0 bytes 735643f9
+ 00b4006c bytes 73be43f9
- 00b3ffdc ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 00b3ffdc ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b3ffdc ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b3ffdc ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00b40078 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
+ 00b40078 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00b40078 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00b40078 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b3ffdc bytes 20010037
+ 00b40078 bytes 20010037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b92bc48b4f028ff267c132c11f0f4060"></a>

### [`00b4000c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b4000c.md) → [`00b400a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b400a8.md) _ZN8firebase26ReferenceCountedFutureImplC2Em

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5ac40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac40.md) · 呼出先 3件 [`00c5ac20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac20.md) [`00c5ac80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac80.md) [`00c5ad40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad40.md)
- 新版 呼出元 1件 [`00c5ad10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad10.md) · 呼出先 3件 [`00c5acf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5acf0.md) [`00c5ad50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad50.md) [`00c5ae10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae10.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.22% / 新版 97.22%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b400d4",
      "incomplete_value": true,
      "site": "00b400d4",
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
      "definition_site": "00b40038",
      "incomplete_value": true,
      "site": "00b40038",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b40110",
      "incomplete_value": true,
      "site": "00b40114",
      "value": [
        "live",
        "register:40b0:8"
      ]
    },
    "old": {
      "definition_site": "00b40074",
      "incomplete_value": true,
      "site": "00b40078",
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
      "00b400c0",
      "READ",
      [
        "storage",
        "00c9b6b0",
        null,
        "pointer"
      ]
    ],
    [
      "00b400d4",
      "DATA",
      [
        "storage",
        "00c903c0",
        null,
        "undefined1[120]"
      ]
    ]
  ],
  "added": [
    [
      "00b400c0",
      "READ",
      [
        "storage",
        "00c9b780",
        null,
        "pointer"
      ]
    ],
    [
      "00b400d4",
      "DATA",
      [
        "storage",
        "00c90490",
        null,
        "undefined1[120]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b40078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b4000c.md#insn-00b40078) · [`00b40024`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b4000c.md#insn-00b40024) · [`00b40044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b4000c.md#insn-00b40044)
- 新版 [`00b40114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b400a8.md#insn-00b40114) · [`00b400c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b400a8.md#insn-00b400c0) · [`00b400e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b400a8.md#insn-00b400e0)

~~~diff
- 00b40078 ["INT_ADD", "register:40f0:8", ["const:b40078:8", "const:4:8"]]
- 00b40078 ["CALL", null, ["callee:00c5acf0:8"]]
+ 00b40114 ["INT_ADD", "register:40f0:8", ["const:b40114:8", "const:4:8"]]
+ 00b40114 ["CALL", null, ["callee:00c5acf0:8"]]
- 00b40078 bytes ea6a0494
+ 00b40114 bytes f76a0494
- 00b40024 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:6b0:8"]]
- 00b40024 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b400c0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:780:8"]]
+ 00b400c0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b40024 bytes 085943f9
+ 00b400c0 bytes 08c143f9
- 00b40044 ["INT_ADD", "register:40f0:8", ["const:b40044:8", "const:4:8"]]
- 00b40044 ["CALL", null, ["callee:00c5ad50:8"]]
+ 00b400e0 ["INT_ADD", "register:40f0:8", ["const:b400e0:8", "const:4:8"]]
+ 00b400e0 ["CALL", null, ["callee:00c5ad50:8"]]
- 00b40044 bytes 0f6b0494
+ 00b400e0 bytes 1c6b0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf4f8fde169bf1a5406c04b9787a9110"></a>

### [`00b400f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b400f0.md) → [`00b4018c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b4018c.md) _ZNSt6__ndk16vectorIN8firebase10FutureBaseENS_9allocatorIS2_EEEC2Em

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00c5ad40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad40.md) · 呼出先 4件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c5abe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abe0.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad10.md)
- 新版 呼出元 1件 [`00c5ae10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae10.md) · 呼出先 4件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c5acb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5acb0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ade0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ade0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 55.56% / 新版 55.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b401bc",
      "incomplete_value": true,
      "site": "00b401c0",
      "value": [
        "INT_LEFT",
        "8",
        [
          [
            "live",
            "register:4008:8"
          ],
          [
            "leaf",
            "const:6:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b40188",
      "incomplete_value": true,
      "site": "00b4018c",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "ordinal": 3,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b40124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b400f0.md#insn-00b40124) · [`00b4018c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b400f0.md#insn-00b4018c) · [`00b4010c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b400f0.md#insn-00b4010c)
- 新版 [`00b401c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b4018c.md#insn-00b401c0) · [`00b40228`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b4018c.md#insn-00b40228) · [`00b401a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b4018c.md#insn-00b401a8)

~~~diff
- 00b40124 ["INT_ADD", "register:40f0:8", ["const:b40124:8", "const:4:8"]]
- 00b40124 ["CALL", null, ["callee:00c57f60:8"]]
+ 00b401c0 ["INT_ADD", "register:40f0:8", ["const:b401c0:8", "const:4:8"]]
+ 00b401c0 ["CALL", null, ["callee:00c57f60:8"]]
- 00b40124 bytes 5b5f0494
+ 00b401c0 bytes 685f0494
- 00b4018c ["INT_ADD", "register:40f0:8", ["const:b4018c:8", "const:4:8"]]
- 00b4018c ["CALL", null, ["callee:00c5ade0:8"]]
+ 00b40228 ["INT_ADD", "register:40f0:8", ["const:b40228:8", "const:4:8"]]
+ 00b40228 ["CALL", null, ["callee:00c5ade0:8"]]
- 00b4018c bytes e16a0494
+ 00b40228 bytes ee6a0494
- 00b4010c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b4010c ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00b401a8 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b401a8 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b4010c bytes 410300b4
+ 00b401a8 bytes 410300b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-959d92b369848778effaedf36f67c830"></a>

### [`00b402ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b402ac.md) → [`00b40348`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40348.md) _ZNKSt6__ndk120__vector_base_commonILb1EE20__throw_length_errorEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5ad10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad10.md) · 呼出先 1件 [`00b402c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b402c0.md)
- 新版 呼出元 1件 [`00c5ade0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ade0.md) · 呼出先 1件 [`00b4035c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b4035c.md)

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
      "definition_site": "00b40354",
      "incomplete_value": false,
      "site": "00b40358",
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
    "old": {
      "definition_site": "00b402b8",
      "incomplete_value": false,
      "site": "00b402bc",
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
            "const:f4c:8"
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
      "00b40354",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b40354",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b402bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b402ac.md#insn-00b402bc) · [`00b402b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b402ac.md#insn-00b402b8)
- 新版 [`00b40358`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40348.md#insn-00b40358) · [`00b40354`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40348.md#insn-00b40354)

~~~diff
- 00b402bc ["INT_ADD", "register:40f0:8", ["const:b402bc:8", "const:4:8"]]
- 00b402bc ["CALL", null, ["callee:00b4035c:8"]]
+ 00b40358 ["INT_ADD", "register:40f0:8", ["const:b40358:8", "const:4:8"]]
+ 00b40358 ["CALL", null, ["callee:00b4035c:8"]]
- 00b402bc bytes 01000094
+ 00b40358 bytes 01000094
- 00b402b8 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00b402b8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b402b8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b402b8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b40354 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 00b40354 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b40354 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b40354 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b402b8 bytes 00303d91
+ 00b40354 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf7f47b4e7ef480569b2f7577fcccaab"></a>

### [`00b40340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40340.md) → [`00b403dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b403dc.md) _ZNSt6__ndk16__treeINS_12__value_typeImPN8firebase17FutureBackingDataEEENS_19__map_value_compareImS5_NS_4lessImEELb1EEENS_9allocatorIS5_EEE7

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00c5ad30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad30.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ad30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad30.md)
- 新版 呼出元 1件 [`00c5ae00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae00.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ae00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae00.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 25.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b40340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40340.md#insn-00b40340) · [`00b4035c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40340.md#insn-00b4035c) · [`00b40368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40340.md#insn-00b40368)
- 新版 [`00b403dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b403dc.md#insn-00b403dc) · [`00b403f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b403dc.md#insn-00b403f8) · [`00b40404`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b403dc.md#insn-00b40404)

~~~diff
- 00b40340 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b40340 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b403dc ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b403dc ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b40340 bytes e10100b4
+ 00b403dc bytes e10100b4
- 00b4035c ["INT_ADD", "register:40f0:8", ["const:b4035c:8", "const:4:8"]]
- 00b4035c ["CALL", null, ["callee:00c5ae00:8"]]
+ 00b403f8 ["INT_ADD", "register:40f0:8", ["const:b403f8:8", "const:4:8"]]
+ 00b403f8 ["CALL", null, ["callee:00c5ae00:8"]]
- 00b4035c bytes 756a0494
+ 00b403f8 bytes 826a0494
- 00b40368 ["INT_ADD", "register:40f0:8", ["const:b40368:8", "const:4:8"]]
- 00b40368 ["CALL", null, ["callee:00c5ae00:8"]]
+ 00b40404 ["INT_ADD", "register:40f0:8", ["const:b40404:8", "const:4:8"]]
+ 00b40404 ["CALL", null, ["callee:00c5ae00:8"]]
- 00b40368 bytes 726a0494
+ 00b40404 bytes 7f6a0494
~~~


<a id="compare-3aebdade286dc2723e4ca9906d0171c7"></a>

### [`00b40380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40380.md) → [`00b4041c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b4041c.md) FUN_00b4041c

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b3ff74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3f/00b3ff74.md) · 呼出先 3件 [`00c5a940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a940.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5ace0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ace0.md)
- 新版 呼出元 1件 [`00b40010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40010.md) · 呼出先 3件 [`00c5aa10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aa10.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5adb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5adb0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 63.64% / 新版 63.64%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b40380"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b40380"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4041c"
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
      "unmatched:00b40380",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4038c",
      "PARAM",
      [
        "storage",
        "002a4ccf",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4041c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b40428",
      "PARAM",
      [
        "storage",
        "002a4c73",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b40380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40380.md#insn-00b40380) · [`00b40390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40380.md#insn-00b40390)
- 新版 [`00b4042c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b4041c.md#insn-00b4042c) · [`00b4041c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b4041c.md#insn-00b4041c)

~~~diff
- 00b40380 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b40380 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b40380 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 00b40380 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b40380 bytes fd7bbfa9
- 00b40390 ["INT_ADD", "register:40f0:8", ["const:b40390:8", "const:4:8"]]
- 00b40390 ["CALL", null, ["callee:00c5ad70:8"]]
+ 00b4042c ["INT_ADD", "register:40f0:8", ["const:b4042c:8", "const:4:8"]]
+ 00b4042c ["CALL", null, ["callee:00c5ad70:8"]]
- 00b40390 bytes 446a0494
+ 00b4042c bytes 516a0494
+ 00b4041c ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00b4041c ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00b4041c ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 00b4041c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00b4041c bytes fd7bbfa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9c45f717a0654df54ea8fccbd974886"></a>

### [`00b403dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b403dc.md) → [`00b40478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40478.md) _ZN8firebase9analytics9analytics19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b40408"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b404a4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4048c",
      "incomplete_value": true,
      "site": "00b4048c",
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
      "definition_site": "00b403f0",
      "incomplete_value": true,
      "site": "00b403f0",
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
      "00b40488",
      "READ",
      [
        "storage",
        "01125330",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4048c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b4040c"
      ]
    ],
    [
      "unmatched:00b403fc",
      "PARAM",
      [
        "storage",
        "002a70af",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b40488",
      "READ",
      [
        "storage",
        "01125430",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4048c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b404a8"
      ]
    ],
    [
      "00b40498",
      "PARAM",
      [
        "storage",
        "002a7053",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b40400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b403dc.md#insn-00b40400) · [`00b40408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b403dc.md#insn-00b40408) · [`00b40418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b403dc.md#insn-00b40418)

~~~diff
- 00b40400 ["INT_ADD", "register:40f0:8", ["const:b40400:8", "const:4:8"]]
- 00b40400 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b40400 bytes c46a0494
- 00b40408 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:330:8"]]
- 00b40408 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b40408 bytes 609a01f9
- 00b40418 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b40418 ["RETURN", null, ["register:0:8"]]
- 00b40418 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17ecf6189fd30e84b5735eed2d7a6ac7"></a>

### [`00b4041c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b4041c.md) → [`00b404b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b404b8.md) _ZN8firebase9analytics9analytics19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

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
      "site": "00b4041c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b40420"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b40420"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4041c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b40420",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b404c8",
      "READ",
      [
        "storage",
        "01125330",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b404b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b404bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b404c8",
      "READ",
      [
        "storage",
        "01125430",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4041c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b4041c.md#insn-00b4041c) · [`00b40420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b4041c.md#insn-00b40420) · [`00b40430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b4041c.md#insn-00b40430)
- 新版 [`00b404cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b404b8.md#insn-00b404cc)

~~~diff
- 00b4041c ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b4041c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b4041c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b4041c bytes f30f1ef8
- 00b40420 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b40420 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b40420 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b40420 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b40420 bytes fd7b01a9
- 00b40430 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b40430 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b404cc ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b404cc ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b40430 bytes e80000b5
+ 00b404cc bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38d98c3992909ec91141d292719fdf57"></a>

### [`00b404a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b404a0.md) → [`00b4053c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b4053c.md) _ZN8firebase9analytics9analytics10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 76.47% / 新版 76.47%

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
      "site": "00b404d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4056c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b404b4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4054c",
      "READ",
      [
        "storage",
        "01125330",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b404b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b40570"
      ]
    ],
    [
      "unmatched:00b404bc",
      "PARAM",
      [
        "storage",
        "002a70af",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4054c",
      "READ",
      [
        "storage",
        "01125430",
        null,
        "undefined8"
      ]
    ],
    [
      "00b40550",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b40570"
      ]
    ],
    [
      "00b40558",
      "PARAM",
      [
        "storage",
        "002a7053",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b404b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b404a0.md#insn-00b404b4) · [`00b404c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b404a0.md#insn-00b404c8) · [`00b404d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b404a0.md#insn-00b404d0)
- 新版 [`00b40564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b4053c.md#insn-00b40564)

~~~diff
- 00b404b4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b404b4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b404b4 bytes 080100b5
- 00b404c8 ["INT_ADD", "register:40f0:8", ["const:b404c8:8", "const:4:8"]]
- 00b404c8 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b40564 ["INT_ADD", "register:40f0:8", ["const:b40564:8", "const:4:8"]]
+ 00b40564 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b404c8 bytes 926a0494
+ 00b40564 bytes 9f6a0494
- 00b404d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:330:8"]]
- 00b404d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b404d0 bytes 609a01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4994abf7ea360aaa92871821e3ca6a33"></a>

### [`00b404f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b404f0.md) → [`00b4058c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b4058c.md) _ZN8firebase9analytics9analytics15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b405e4",
      "incomplete_value": true,
      "site": "00b405e4",
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
            "const:438:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b40548",
      "incomplete_value": true,
      "site": "00b40548",
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
            "const:338:8"
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
      "definition_site": "00b405c0",
      "incomplete_value": true,
      "site": "00b405cc",
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
                "const:430:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b40524",
      "incomplete_value": true,
      "site": "00b40530",
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
                "const:330:8"
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
      "00b405a0",
      "READ",
      [
        "storage",
        "01125338",
        null,
        "undefined1"
      ]
    ],
    [
      "00b405c0",
      "READ",
      [
        "storage",
        "01125330",
        null,
        "undefined8"
      ]
    ],
    [
      "00b405e4",
      "WRITE",
      [
        "storage",
        "01125338",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b405a0",
      "READ",
      [
        "storage",
        "01125438",
        null,
        "undefined1"
      ]
    ],
    [
      "00b405c0",
      "READ",
      [
        "storage",
        "01125430",
        null,
        "undefined8"
      ]
    ],
    [
      "00b405e4",
      "WRITE",
      [
        "storage",
        "01125438",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b40530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b404f0.md#insn-00b40530) · [`00b40548`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b404f0.md#insn-00b40548) · [`00b40504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b404f0.md#insn-00b40504)
- 新版 [`00b405cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b4058c.md#insn-00b405cc) · [`00b405e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b4058c.md#insn-00b405e4) · [`00b405a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b4058c.md#insn-00b405a0)

~~~diff
- 00b40530 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b40530 ["INT_ADD", "register:40f0:8", ["const:b40530:8", "const:4:8"]]
- 00b40530 ["CALLIND", null, ["register:0:8"]]
+ 00b405cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b405cc ["INT_ADD", "register:40f0:8", ["const:b405cc:8", "const:4:8"]]
+ 00b405cc ["CALLIND", null, ["register:0:8"]]
- 00b40530 bytes 00013fd6
+ 00b405cc bytes 00013fd6
- 00b40548 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b40548 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:338:8"]]
- 00b40548 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b405e4 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b405e4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:438:8"]]
+ 00b405e4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b40548 bytes a0e20c39
+ 00b405e4 bytes a0e21039
- 00b40504 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:338:8"]]
- 00b40504 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b40504 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b405a0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:438:8"]]
+ 00b405a0 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b405a0 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b40504 bytes a8e24c39
+ 00b405a0 bytes a8e25039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e727ea5ef68112923ab02157d0a6b10"></a>

### [`00b4055c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b4055c.md) → [`00b405f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b405f8.md) _ZN8firebase9analytics9analytics12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 14.29% / 新版 14.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b40598"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b405b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b40634"
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
      "00b4060c",
      "READ",
      [
        "storage",
        "01125330",
        null,
        "undefined8"
      ]
    ],
    [
      "00b40610",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b405bc"
      ]
    ],
    [
      "00b40618",
      "READ",
      [
        "storage",
        "01125338",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4060c",
      "READ",
      [
        "storage",
        "01125430",
        null,
        "undefined8"
      ]
    ],
    [
      "00b40610",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b40658"
      ]
    ],
    [
      "00b40618",
      "READ",
      [
        "storage",
        "01125438",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b40574`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b4055c.md#insn-00b40574) · [`00b40594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b4055c.md#insn-00b40594) · [`00b40598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b4055c.md#insn-00b40598)
- 新版 [`00b40610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b405f8.md#insn-00b40610)

~~~diff
- 00b40574 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b40574 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b40610 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b40610 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b40574 bytes 410200b4
+ 00b40610 bytes 410200b4
- 00b40594 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b40594 ["INT_ADD", "register:40f0:8", ["const:b40594:8", "const:4:8"]]
- 00b40594 ["CALLIND", null, ["register:0:8"]]
- 00b40594 bytes 00013fd6
- 00b40598 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b40598 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b40598 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:338:8"]]
- 00b40598 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b40598 bytes bfe20c39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd48454472b01012177811dca2fe8139"></a>

### [`00b405cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b405cc.md) → [`00b40668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40668.md) _ZN8firebase9analytics9analytics14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00b4060c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b406a8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b405e8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b405e0",
      "READ",
      [
        "storage",
        "01125330",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b405e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b406ac"
      ]
    ],
    [
      "unmatched:00b405f0",
      "PARAM",
      [
        "storage",
        "002a70af",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4067c",
      "READ",
      [
        "storage",
        "01125430",
        null,
        "undefined8"
      ]
    ],
    [
      "00b40684",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b406ac"
      ]
    ],
    [
      "00b4068c",
      "PARAM",
      [
        "storage",
        "002a7053",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b405e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b405cc.md#insn-00b405e8) · [`00b40604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b405cc.md#insn-00b40604) · [`00b4060c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b405cc.md#insn-00b4060c)
- 新版 [`00b406a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40668.md#insn-00b406a0)

~~~diff
- 00b405e8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b405e8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b405e8 bytes 410100b5
- 00b40604 ["INT_ADD", "register:40f0:8", ["const:b40604:8", "const:4:8"]]
- 00b40604 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b406a0 ["INT_ADD", "register:40f0:8", ["const:b406a0:8", "const:4:8"]]
+ 00b406a0 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b40604 bytes 436a0494
+ 00b406a0 bytes 506a0494
- 00b4060c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:330:8"]]
- 00b4060c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4060c bytes 809a01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c19927b94d70cf77e758f7e62d6dff37"></a>

### [`00b4063c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b4063c.md) → [`00b406d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b406d8.md) _ZN8firebase9analytics9analytics11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
      "definition_site": "00b406f4",
      "incomplete_value": false,
      "site": "00b406f8",
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
            "const:30b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b40658",
      "incomplete_value": false,
      "site": "00b4065c",
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
            "const:367:8"
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
      "definition_site": "00b40704",
      "incomplete_value": true,
      "site": "00b40710",
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
      "definition_site": "00b40668",
      "incomplete_value": true,
      "site": "00b40674",
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
      "00b406f4",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b40704",
      "DATA",
      [
        "storage",
        "01125340",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b406f4",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b40704",
      "DATA",
      [
        "storage",
        "01125440",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4065c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b4063c.md#insn-00b4065c) · [`00b40658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b4063c.md#insn-00b40658) · [`00b40664`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b4063c.md#insn-00b40664)
- 新版 [`00b406f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b406d8.md#insn-00b406f8) · [`00b406f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b406d8.md#insn-00b406f4) · [`00b40700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b406d8.md#insn-00b40700)

~~~diff
- 00b4065c ["INT_ADD", "register:40f0:8", ["const:b4065c:8", "const:4:8"]]
- 00b4065c ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b406f8 ["INT_ADD", "register:40f0:8", ["const:b406f8:8", "const:4:8"]]
+ 00b406f8 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b4065c bytes 696a0494
+ 00b406f8 bytes 766a0494
- 00b40658 ["COPY", "tmp:0:8", ["const:367:8"]]
- 00b40658 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b40658 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b40658 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b406f4 ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00b406f4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b406f4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b406f4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b40658 bytes 009c0d91
+ 00b406f4 bytes 002c0c91
- 00b40664 ["COPY", "tmp:0:8", ["const:340:8"]]
- 00b40664 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b40664 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b40664 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b40700 ["COPY", "tmp:0:8", ["const:440:8"]]
+ 00b40700 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b40700 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b40700 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b40664 bytes 08010d91
+ 00b40700 bytes 08011191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a2becffe3c02ba3dc0f610208b5503e"></a>

### [`00b40678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40678.md) → [`00b40714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40714.md) _ZN8firebase9analytics9analytics13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b40754",
      "incomplete_value": true,
      "site": "00b40754",
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
            "const:430:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b406b8",
      "incomplete_value": true,
      "site": "00b406b8",
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
            "const:330:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b40730",
      "incomplete_value": true,
      "site": "00b40730",
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
      "definition_site": "00b40694",
      "incomplete_value": true,
      "site": "00b40694",
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
      "definition_site": "00b40738",
      "incomplete_value": false,
      "site": "00b4074c",
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
            "const:53:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4069c",
      "incomplete_value": false,
      "site": "00b406b0",
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
            "const:af:8"
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
      "00b40728",
      "READ",
      [
        "storage",
        "01125330",
        null,
        "undefined8"
      ]
    ],
    [
      "00b40738",
      "PARAM",
      [
        "storage",
        "002a70af",
        null,
        "string"
      ]
    ],
    [
      "00b40754",
      "WRITE",
      [
        "storage",
        "01125330",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b40728",
      "READ",
      [
        "storage",
        "01125430",
        null,
        "undefined8"
      ]
    ],
    [
      "00b40738",
      "PARAM",
      [
        "storage",
        "002a7053",
        null,
        "string"
      ]
    ],
    [
      "00b40754",
      "WRITE",
      [
        "storage",
        "01125430",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b406b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40678.md#insn-00b406b0) · [`00b406b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40678.md#insn-00b406b8) · [`00b4068c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40678.md#insn-00b4068c)
- 新版 [`00b4074c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40714.md#insn-00b4074c) · [`00b40754`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40714.md#insn-00b40754) · [`00b40728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40714.md#insn-00b40728)

~~~diff
- 00b406b0 ["INT_ADD", "register:40f0:8", ["const:b406b0:8", "const:4:8"]]
- 00b406b0 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4074c ["INT_ADD", "register:40f0:8", ["const:b4074c:8", "const:4:8"]]
+ 00b4074c ["CALL", null, ["callee:00c5afe0:8"]]
- 00b406b0 bytes 186a0494
+ 00b4074c bytes 256a0494
- 00b406b8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:330:8"]]
- 00b406b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b40754 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:430:8"]]
+ 00b40754 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b406b8 bytes 809a01f9
+ 00b40754 bytes 801a02f9
- 00b4068c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:330:8"]]
- 00b4068c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b40728 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:430:8"]]
+ 00b40728 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4068c bytes 819a41f9
+ 00b40728 bytes 811a42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9dd7fa430290794ac4988a1ed108a571"></a>

### [`00b406e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b406e8.md) → [`00b40784`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40784.md) _ZN8firebase9analytics9analytics10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
      "definition_site": "00b407a0",
      "incomplete_value": false,
      "site": "00b407a4",
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
            "const:54d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b40704",
      "incomplete_value": false,
      "site": "00b40708",
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
            "const:51e:8"
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
      "definition_site": "00b407b0",
      "incomplete_value": true,
      "site": "00b407bc",
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
      "definition_site": "00b40714",
      "incomplete_value": true,
      "site": "00b40720",
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
      "00b407a0",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b407b0",
      "DATA",
      [
        "storage",
        "01125398",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b407a0",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b407b0",
      "DATA",
      [
        "storage",
        "01125498",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b40708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b406e8.md#insn-00b40708) · [`00b40704`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b406e8.md#insn-00b40704) · [`00b40710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b406e8.md#insn-00b40710)
- 新版 [`00b407a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40784.md#insn-00b407a4) · [`00b407a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40784.md#insn-00b407a0) · [`00b407ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40784.md#insn-00b407ac)

~~~diff
- 00b40708 ["INT_ADD", "register:40f0:8", ["const:b40708:8", "const:4:8"]]
- 00b40708 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b407a4 ["INT_ADD", "register:40f0:8", ["const:b407a4:8", "const:4:8"]]
+ 00b407a4 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b40708 bytes 3e6a0494
+ 00b407a4 bytes 4b6a0494
- 00b40704 ["COPY", "tmp:0:8", ["const:51e:8"]]
- 00b40704 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b40704 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b40704 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b407a0 ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00b407a0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b407a0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b407a0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b40704 bytes 00781491
+ 00b407a0 bytes 00341591
- 00b40710 ["COPY", "tmp:0:8", ["const:398:8"]]
- 00b40710 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b40710 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b40710 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b407ac ["COPY", "tmp:0:8", ["const:498:8"]]
+ 00b407ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b407ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b407ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b40710 bytes 08610e91
+ 00b407ac bytes 08611291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2cdbd54e545dab848f00646b7f0a75ad"></a>

### [`00b40724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40724.md) → [`00b407c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b407c0.md) _ZN8firebase9analytics22analytics_consent_type19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9a

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00b407ec",
      "incomplete_value": true,
      "site": "00b407ec",
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
            "const:4a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b40750",
      "incomplete_value": true,
      "site": "00b40750",
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
            "const:3a0:8"
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
      "definition_site": "00b407d4",
      "incomplete_value": true,
      "site": "00b407d4",
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
      "definition_site": "00b40738",
      "incomplete_value": true,
      "site": "00b40738",
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
      "definition_site": "00b407e0",
      "incomplete_value": false,
      "site": "00b407e4",
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
            "const:57b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b40744",
      "incomplete_value": false,
      "site": "00b40748",
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
            "const:54a:8"
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
      "00b407d0",
      "READ",
      [
        "storage",
        "011253a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b407e0",
      "PARAM",
      [
        "storage",
        "002b254a",
        null,
        "string"
      ]
    ],
    [
      "00b407ec",
      "WRITE",
      [
        "storage",
        "011253a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b407d0",
      "READ",
      [
        "storage",
        "011254a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b407e0",
      "PARAM",
      [
        "storage",
        "002b257b",
        null,
        "string"
      ]
    ],
    [
      "00b407ec",
      "WRITE",
      [
        "storage",
        "011254a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b40748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40724.md#insn-00b40748) · [`00b40750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40724.md#insn-00b40750) · [`00b40734`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40724.md#insn-00b40734)
- 新版 [`00b407e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b407c0.md#insn-00b407e4) · [`00b407ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b407c0.md#insn-00b407ec) · [`00b407d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b407c0.md#insn-00b407d0)

~~~diff
- 00b40748 ["INT_ADD", "register:40f0:8", ["const:b40748:8", "const:4:8"]]
- 00b40748 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b407e4 ["INT_ADD", "register:40f0:8", ["const:b407e4:8", "const:4:8"]]
+ 00b407e4 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b40748 bytes f2690494
+ 00b407e4 bytes ff690494
- 00b40750 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3a0:8"]]
- 00b40750 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b407ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a0:8"]]
+ 00b407ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b40750 bytes 60d201f9
+ 00b407ec bytes 605202f9
- 00b40734 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3a0:8"]]
- 00b40734 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b407d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a0:8"]]
+ 00b407d0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b40734 bytes 68d241f9
+ 00b407d0 bytes 685242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9d895a24e4fa455f9d4f4f40994c68c"></a>

### [`00b40764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40764.md) → [`00b40800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40800.md) _ZN8firebase9analytics22analytics_consent_type19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9a

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00b4082c",
      "incomplete_value": true,
      "site": "00b4082c",
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
            "const:4a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b40790",
      "incomplete_value": true,
      "site": "00b40790",
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
            "const:3a0:8"
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
      "definition_site": "00b40814",
      "incomplete_value": true,
      "site": "00b40814",
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
      "definition_site": "00b40778",
      "incomplete_value": true,
      "site": "00b40778",
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
      "definition_site": "00b4081c",
      "incomplete_value": false,
      "site": "00b40824",
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
            "const:57b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b40780",
      "incomplete_value": false,
      "site": "00b40788",
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
            "const:54a:8"
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
      "00b40810",
      "READ",
      [
        "storage",
        "011253a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4081c",
      "PARAM",
      [
        "storage",
        "002b254a",
        null,
        "string"
      ]
    ],
    [
      "00b4082c",
      "WRITE",
      [
        "storage",
        "011253a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b40810",
      "READ",
      [
        "storage",
        "011254a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4081c",
      "PARAM",
      [
        "storage",
        "002b257b",
        null,
        "string"
      ]
    ],
    [
      "00b4082c",
      "WRITE",
      [
        "storage",
        "011254a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b40788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40764.md#insn-00b40788) · [`00b40790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40764.md#insn-00b40790) · [`00b40774`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40764.md#insn-00b40774)
- 新版 [`00b40824`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40800.md#insn-00b40824) · [`00b4082c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40800.md#insn-00b4082c) · [`00b40810`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40800.md#insn-00b40810)

~~~diff
- 00b40788 ["INT_ADD", "register:40f0:8", ["const:b40788:8", "const:4:8"]]
- 00b40788 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b40824 ["INT_ADD", "register:40f0:8", ["const:b40824:8", "const:4:8"]]
+ 00b40824 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b40788 bytes e2690494
+ 00b40824 bytes ef690494
- 00b40790 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3a0:8"]]
- 00b40790 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4082c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a0:8"]]
+ 00b4082c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b40790 bytes 60d201f9
+ 00b4082c bytes 605202f9
- 00b40774 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3a0:8"]]
- 00b40774 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b40810 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a0:8"]]
+ 00b40810 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b40774 bytes 68d241f9
+ 00b40810 bytes 685242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85e4adf69cb53e83d27c548bf036eda4"></a>

### [`00b407a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b407a4.md) → [`00b40840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40840.md) _ZN8firebase9analytics22analytics_consent_type10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00b40870",
      "incomplete_value": true,
      "site": "00b40870",
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
            "const:4a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b407d4",
      "incomplete_value": true,
      "site": "00b407d4",
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
            "const:3a0:8"
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
      "definition_site": "00b40854",
      "incomplete_value": true,
      "site": "00b40854",
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
      "definition_site": "00b407b8",
      "incomplete_value": true,
      "site": "00b407b8",
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
      "definition_site": "00b40860",
      "incomplete_value": false,
      "site": "00b40868",
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
            "const:57b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b407c4",
      "incomplete_value": false,
      "site": "00b407cc",
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
            "const:54a:8"
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
      "00b40850",
      "READ",
      [
        "storage",
        "011253a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b40860",
      "PARAM",
      [
        "storage",
        "002b254a",
        null,
        "string"
      ]
    ],
    [
      "00b40870",
      "WRITE",
      [
        "storage",
        "011253a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b40850",
      "READ",
      [
        "storage",
        "011254a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b40860",
      "PARAM",
      [
        "storage",
        "002b257b",
        null,
        "string"
      ]
    ],
    [
      "00b40870",
      "WRITE",
      [
        "storage",
        "011254a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b407cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b407a4.md#insn-00b407cc) · [`00b407d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b407a4.md#insn-00b407d4) · [`00b407b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b407a4.md#insn-00b407b4)
- 新版 [`00b40868`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40840.md#insn-00b40868) · [`00b40870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40840.md#insn-00b40870) · [`00b40850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40840.md#insn-00b40850)

~~~diff
- 00b407cc ["INT_ADD", "register:40f0:8", ["const:b407cc:8", "const:4:8"]]
- 00b407cc ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b40868 ["INT_ADD", "register:40f0:8", ["const:b40868:8", "const:4:8"]]
+ 00b40868 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b407cc bytes d1690494
+ 00b40868 bytes de690494
- 00b407d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3a0:8"]]
- 00b407d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b40870 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a0:8"]]
+ 00b40870 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b407d4 bytes 60d201f9
+ 00b40870 bytes 605202f9
- 00b407b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3a0:8"]]
- 00b407b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b40850 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a0:8"]]
+ 00b40850 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b407b4 bytes 68d241f9
+ 00b40850 bytes 685242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04e686350d284f262f0635c00f731cc3"></a>

### [`00b407e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b407e8.md) → [`00b40884`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40884.md) _ZN8firebase9analytics22analytics_consent_type10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00b408b4",
      "incomplete_value": true,
      "site": "00b408b4",
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
            "const:4a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b40818",
      "incomplete_value": true,
      "site": "00b40818",
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
            "const:3a0:8"
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
      "definition_site": "00b40898",
      "incomplete_value": true,
      "site": "00b40898",
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
      "definition_site": "00b407fc",
      "incomplete_value": true,
      "site": "00b407fc",
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
      "definition_site": "00b408a0",
      "incomplete_value": false,
      "site": "00b408ac",
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
            "const:57b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b40804",
      "incomplete_value": false,
      "site": "00b40810",
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
            "const:54a:8"
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
      "00b40894",
      "READ",
      [
        "storage",
        "011253a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b408a0",
      "PARAM",
      [
        "storage",
        "002b254a",
        null,
        "string"
      ]
    ],
    [
      "00b408b4",
      "WRITE",
      [
        "storage",
        "011253a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b40894",
      "READ",
      [
        "storage",
        "011254a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b408a0",
      "PARAM",
      [
        "storage",
        "002b257b",
        null,
        "string"
      ]
    ],
    [
      "00b408b4",
      "WRITE",
      [
        "storage",
        "011254a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b40810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b407e8.md#insn-00b40810) · [`00b40818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b407e8.md#insn-00b40818) · [`00b407f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b407e8.md#insn-00b407f8)
- 新版 [`00b408ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40884.md#insn-00b408ac) · [`00b408b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40884.md#insn-00b408b4) · [`00b40894`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40884.md#insn-00b40894)

~~~diff
- 00b40810 ["INT_ADD", "register:40f0:8", ["const:b40810:8", "const:4:8"]]
- 00b40810 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b408ac ["INT_ADD", "register:40f0:8", ["const:b408ac:8", "const:4:8"]]
+ 00b408ac ["CALL", null, ["callee:00c5afe0:8"]]
- 00b40810 bytes c0690494
+ 00b408ac bytes cd690494
- 00b40818 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3a0:8"]]
- 00b40818 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b408b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a0:8"]]
+ 00b408b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b40818 bytes 60d201f9
+ 00b408b4 bytes 605202f9
- 00b407f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3a0:8"]]
- 00b407f8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b40894 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a0:8"]]
+ 00b40894 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b407f8 bytes 68d241f9
+ 00b40894 bytes 685242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f39321d3a96f0989bd0731a530d2052"></a>

### [`00b40838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40838.md) → [`00b408d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b408d4.md) _ZN8firebase9analytics22analytics_consent_type15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4092c",
      "incomplete_value": true,
      "site": "00b4092c",
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
            "const:4a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b40890",
      "incomplete_value": true,
      "site": "00b40890",
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
            "const:3a8:8"
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
      "definition_site": "00b40908",
      "incomplete_value": true,
      "site": "00b40914",
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
                "const:4a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4086c",
      "incomplete_value": true,
      "site": "00b40878",
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
                "const:3a0:8"
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
      "00b408e8",
      "READ",
      [
        "storage",
        "011253a8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b40908",
      "READ",
      [
        "storage",
        "011253a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4092c",
      "WRITE",
      [
        "storage",
        "011253a8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b408e8",
      "READ",
      [
        "storage",
        "011254a8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b40908",
      "READ",
      [
        "storage",
        "011254a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4092c",
      "WRITE",
      [
        "storage",
        "011254a8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b40878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40838.md#insn-00b40878) · [`00b40890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40838.md#insn-00b40890) · [`00b4084c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40838.md#insn-00b4084c)
- 新版 [`00b40914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b408d4.md#insn-00b40914) · [`00b4092c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b408d4.md#insn-00b4092c) · [`00b408e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b408d4.md#insn-00b408e8)

~~~diff
- 00b40878 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b40878 ["INT_ADD", "register:40f0:8", ["const:b40878:8", "const:4:8"]]
- 00b40878 ["CALLIND", null, ["register:0:8"]]
+ 00b40914 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b40914 ["INT_ADD", "register:40f0:8", ["const:b40914:8", "const:4:8"]]
+ 00b40914 ["CALLIND", null, ["register:0:8"]]
- 00b40878 bytes 00013fd6
+ 00b40914 bytes 00013fd6
- 00b40890 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b40890 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:3a8:8"]]
- 00b40890 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4092c ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4092c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:4a8:8"]]
+ 00b4092c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b40890 bytes a0a20e39
+ 00b4092c bytes a0a21239
- 00b4084c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:3a8:8"]]
- 00b4084c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b4084c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b408e8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:4a8:8"]]
+ 00b408e8 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b408e8 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b4084c bytes a8a24e39
+ 00b408e8 bytes a8a25239
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e68d3794ffc36e84f534217a175367ef"></a>

### [`00b408a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b408a4.md) → [`00b40940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40940.md) _ZN8firebase9analytics22analytics_consent_type12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 35.71% / 新版 35.71%

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
      "site": "00b408a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b408a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b408a8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b408a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b408a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b408ac",
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
      "00b40940",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b40944",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b40948",
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

- 旧版 [`00b408a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b408a4.md#insn-00b408a4) · [`00b408a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b408a4.md#insn-00b408a8) · [`00b408ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b408a4.md#insn-00b408ac)

~~~diff
- 00b408a4 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b408a4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b408a4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b408a4 bytes f50f1df8
- 00b408a8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b408a8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b408a8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b408a8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b408a8 bytes f44f01a9
- 00b408ac ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b408ac ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b408ac ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b408ac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b408ac bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c380e30221d5e15a4965eda11845152d"></a>

### [`00b40a6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40a6c.md) → [`00b40b08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40b08.md) _ZN8firebase9analytics24analytics_consent_status19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_condition_or_target, call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 56.25% / 新版 56.25%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b40a98"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b40b34"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b40a80"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b40b18",
      "READ",
      [
        "storage",
        "011253d8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b40a80",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b40b38"
      ]
    ],
    [
      "unmatched:00b40a8c",
      "PARAM",
      [
        "storage",
        "002a3a35",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b40b18",
      "READ",
      [
        "storage",
        "011254d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b40b1c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b40b38"
      ]
    ],
    [
      "00b40b28",
      "PARAM",
      [
        "storage",
        "002a39e8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b40a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40a6c.md#insn-00b40a80) · [`00b40a90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40a6c.md#insn-00b40a90) · [`00b40a98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40a6c.md#insn-00b40a98)

~~~diff
- 00b40a80 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b40a80 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00b40a80 bytes e80000b5
- 00b40a90 ["INT_ADD", "register:40f0:8", ["const:b40a90:8", "const:4:8"]]
- 00b40a90 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b40a90 bytes 20690494
- 00b40a98 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3d8:8"]]
- 00b40a98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b40a98 bytes 60ee01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0a03d202be1e83673219d7abd74a716"></a>

### [`00b40aec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40aec.md) → [`00b40b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40b88.md) _ZN8firebase9analytics24analytics_consent_status10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "site": "00b40aec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b40af0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b40af0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b40aec",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b40af0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b40b98",
      "READ",
      [
        "storage",
        "011253d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b40b88",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b40b8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b40b98",
      "READ",
      [
        "storage",
        "011254d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b40aec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40aec.md#insn-00b40aec) · [`00b40af0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40aec.md#insn-00b40af0) · [`00b40b00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40aec.md#insn-00b40b00)
- 新版 [`00b40b9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40b88.md#insn-00b40b9c)

~~~diff
- 00b40aec ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b40aec ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b40aec ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b40aec bytes f30f1ef8
- 00b40af0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b40af0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b40af0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b40af0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b40af0 bytes fd7b01a9
- 00b40b00 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b40b00 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b40b9c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b40b9c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b40b00 bytes 080100b5
+ 00b40b9c bytes 080100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-140c84d007588ca9b22854ce4fea7cf2"></a>

### [`00b40b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40b30.md) → [`00b40bcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40bcc.md) _ZN8firebase9analytics24analytics_consent_status10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00b40bfc",
      "incomplete_value": true,
      "site": "00b40bfc",
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
            "const:4d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b40b60",
      "incomplete_value": true,
      "site": "00b40b60",
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
            "const:3d8:8"
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
      "definition_site": "00b40be0",
      "incomplete_value": true,
      "site": "00b40be0",
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
      "definition_site": "00b40b44",
      "incomplete_value": true,
      "site": "00b40b44",
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
      "definition_site": "00b40be8",
      "incomplete_value": false,
      "site": "00b40bf4",
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
            "const:9e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b40b4c",
      "incomplete_value": false,
      "site": "00b40b58",
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
            "const:a35:8"
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
      "00b40bdc",
      "READ",
      [
        "storage",
        "011253d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b40be8",
      "PARAM",
      [
        "storage",
        "002a3a35",
        null,
        "string"
      ]
    ],
    [
      "00b40bfc",
      "WRITE",
      [
        "storage",
        "011253d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b40bdc",
      "READ",
      [
        "storage",
        "011254d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b40be8",
      "PARAM",
      [
        "storage",
        "002a39e8",
        null,
        "string"
      ]
    ],
    [
      "00b40bfc",
      "WRITE",
      [
        "storage",
        "011254d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b40b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40b30.md#insn-00b40b58) · [`00b40b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40b30.md#insn-00b40b60) · [`00b40b40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40b30.md#insn-00b40b40)
- 新版 [`00b40bf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40bcc.md#insn-00b40bf4) · [`00b40bfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40bcc.md#insn-00b40bfc) · [`00b40bdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40bcc.md#insn-00b40bdc)

~~~diff
- 00b40b58 ["INT_ADD", "register:40f0:8", ["const:b40b58:8", "const:4:8"]]
- 00b40b58 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b40bf4 ["INT_ADD", "register:40f0:8", ["const:b40bf4:8", "const:4:8"]]
+ 00b40bf4 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b40b58 bytes ee680494
+ 00b40bf4 bytes fb680494
- 00b40b60 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3d8:8"]]
- 00b40b60 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b40bfc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4d8:8"]]
+ 00b40bfc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b40b60 bytes 60ee01f9
+ 00b40bfc bytes 606e02f9
- 00b40b40 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3d8:8"]]
- 00b40b40 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b40bdc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4d8:8"]]
+ 00b40bdc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b40b40 bytes 68ee41f9
+ 00b40bdc bytes 686e42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10901e5014dc340680d2230d6f1e77e7"></a>

### [`00b40b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40b80.md) → [`00b40c1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40c1c.md) _ZN8firebase9analytics24analytics_consent_status15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b40c74",
      "incomplete_value": true,
      "site": "00b40c74",
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
            "const:4e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b40bd8",
      "incomplete_value": true,
      "site": "00b40bd8",
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
            "const:3e0:8"
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
      "definition_site": "00b40c50",
      "incomplete_value": true,
      "site": "00b40c5c",
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
                "const:4d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b40bb4",
      "incomplete_value": true,
      "site": "00b40bc0",
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
                "const:3d8:8"
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
      "00b40c30",
      "READ",
      [
        "storage",
        "011253e0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b40c50",
      "READ",
      [
        "storage",
        "011253d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b40c74",
      "WRITE",
      [
        "storage",
        "011253e0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b40c30",
      "READ",
      [
        "storage",
        "011254e0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b40c50",
      "READ",
      [
        "storage",
        "011254d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b40c74",
      "WRITE",
      [
        "storage",
        "011254e0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b40bc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40b80.md#insn-00b40bc0) · [`00b40bd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40b80.md#insn-00b40bd8) · [`00b40b94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40b80.md#insn-00b40b94)
- 新版 [`00b40c5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40c1c.md#insn-00b40c5c) · [`00b40c74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40c1c.md#insn-00b40c74) · [`00b40c30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40c1c.md#insn-00b40c30)

~~~diff
- 00b40bc0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b40bc0 ["INT_ADD", "register:40f0:8", ["const:b40bc0:8", "const:4:8"]]
- 00b40bc0 ["CALLIND", null, ["register:0:8"]]
+ 00b40c5c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b40c5c ["INT_ADD", "register:40f0:8", ["const:b40c5c:8", "const:4:8"]]
+ 00b40c5c ["CALLIND", null, ["register:0:8"]]
- 00b40bc0 bytes 00013fd6
+ 00b40c5c bytes 00013fd6
- 00b40bd8 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b40bd8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:3e0:8"]]
- 00b40bd8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b40c74 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b40c74 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:4e0:8"]]
+ 00b40c74 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b40bd8 bytes a0820f39
+ 00b40c74 bytes a0821339
- 00b40b94 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:3e0:8"]]
- 00b40b94 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b40b94 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b40c30 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:4e0:8"]]
+ 00b40c30 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b40c30 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b40b94 bytes a8824f39
+ 00b40c30 bytes a8825339
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e25fca93416ec09c84cea502ad35fc09"></a>

### [`00b40bec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40bec.md) → [`00b40c88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40c88.md) _ZN8firebase9analytics24analytics_consent_status12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b40cc4",
      "incomplete_value": true,
      "site": "00b40cc4",
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
            "const:4e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b40c28",
      "incomplete_value": true,
      "site": "00b40c28",
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
            "const:3e0:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b40ce4",
      "incomplete_value": true,
      "site": "00b40ce4",
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
            "const:4d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b40c48",
      "incomplete_value": true,
      "site": "00b40c48",
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
            "const:3d8:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b40ca0",
      "incomplete_value": true,
      "site": "00b40ca0",
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
      "definition_site": "00b40c04",
      "incomplete_value": true,
      "site": "00b40c04",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b40c9c",
      "READ",
      [
        "storage",
        "011253d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b40ca8",
      "READ",
      [
        "storage",
        "011253e0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b40cc4",
      "WRITE",
      [
        "storage",
        "011253e0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b40c9c",
      "READ",
      [
        "storage",
        "011254d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b40ca8",
      "READ",
      [
        "storage",
        "011254e0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b40cc4",
      "WRITE",
      [
        "storage",
        "011254e0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b40c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40bec.md#insn-00b40c28) · [`00b40c44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40bec.md#insn-00b40c44) · [`00b40c48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40bec.md#insn-00b40c48)
- 新版 [`00b40cc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40c88.md#insn-00b40cc4) · [`00b40ce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40c88.md#insn-00b40ce0) · [`00b40ce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40c88.md#insn-00b40ce4)

~~~diff
- 00b40c28 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b40c28 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b40c28 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:3e0:8"]]
- 00b40c28 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b40cc4 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b40cc4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b40cc4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:4e0:8"]]
+ 00b40cc4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b40c28 bytes bf820f39
+ 00b40cc4 bytes bf821339
- 00b40c44 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b40c44 ["INT_ADD", "register:40f0:8", ["const:b40c44:8", "const:4:8"]]
- 00b40c44 ["CALLIND", null, ["register:0:8"]]
+ 00b40ce0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b40ce0 ["INT_ADD", "register:40f0:8", ["const:b40ce0:8", "const:4:8"]]
+ 00b40ce0 ["CALLIND", null, ["register:0:8"]]
- 00b40c44 bytes 00013fd6
+ 00b40ce0 bytes 00013fd6
- 00b40c48 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3d8:8"]]
- 00b40c48 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b40c48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b40ce4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4d8:8"]]
+ 00b40ce4 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b40ce4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b40c48 bytes 9fee01f9
+ 00b40ce4 bytes 9f6e02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ccdb37db87d63459540b2c23d141a073"></a>

### [`00b40c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40c5c.md) → [`00b40cf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40cf8.md) _ZN8firebase9analytics24analytics_consent_status14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b40d38",
      "incomplete_value": true,
      "site": "00b40d38",
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
            "const:4d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b40c9c",
      "incomplete_value": true,
      "site": "00b40c9c",
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
            "const:3d8:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b40d14",
      "incomplete_value": true,
      "site": "00b40d14",
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
      "definition_site": "00b40c78",
      "incomplete_value": true,
      "site": "00b40c78",
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
      "definition_site": "00b40d1c",
      "incomplete_value": false,
      "site": "00b40d30",
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
            "const:9e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b40c80",
      "incomplete_value": false,
      "site": "00b40c94",
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
            "const:a35:8"
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
      "00b40d0c",
      "READ",
      [
        "storage",
        "011253d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b40d1c",
      "PARAM",
      [
        "storage",
        "002a3a35",
        null,
        "string"
      ]
    ],
    [
      "00b40d38",
      "WRITE",
      [
        "storage",
        "011253d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b40d0c",
      "READ",
      [
        "storage",
        "011254d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b40d1c",
      "PARAM",
      [
        "storage",
        "002a39e8",
        null,
        "string"
      ]
    ],
    [
      "00b40d38",
      "WRITE",
      [
        "storage",
        "011254d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b40c94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40c5c.md#insn-00b40c94) · [`00b40c9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40c5c.md#insn-00b40c9c) · [`00b40c70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40c5c.md#insn-00b40c70)
- 新版 [`00b40d30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40cf8.md#insn-00b40d30) · [`00b40d38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40cf8.md#insn-00b40d38) · [`00b40d0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40cf8.md#insn-00b40d0c)

~~~diff
- 00b40c94 ["INT_ADD", "register:40f0:8", ["const:b40c94:8", "const:4:8"]]
- 00b40c94 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b40d30 ["INT_ADD", "register:40f0:8", ["const:b40d30:8", "const:4:8"]]
+ 00b40d30 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b40c94 bytes 9f680494
+ 00b40d30 bytes ac680494
- 00b40c9c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3d8:8"]]
- 00b40c9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b40d38 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4d8:8"]]
+ 00b40d38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b40c9c bytes 80ee01f9
+ 00b40d38 bytes 806e02f9
- 00b40c70 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3d8:8"]]
- 00b40c70 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b40d0c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4d8:8"]]
+ 00b40d0c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b40c70 bytes 81ee41f9
+ 00b40d0c bytes 816e42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59c4ebb1eb0846955cbba4772cfb1c45"></a>

### [`00b40ccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40ccc.md) → [`00b40d68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40d68.md) _ZN8firebase9analytics24analytics_consent_status11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
      "definition_site": "00b40d84",
      "incomplete_value": false,
      "site": "00b40d88",
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
            "const:30b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b40ce8",
      "incomplete_value": false,
      "site": "00b40cec",
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
            "const:367:8"
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
      "definition_site": "00b40d94",
      "incomplete_value": true,
      "site": "00b40da0",
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
      "definition_site": "00b40cf8",
      "incomplete_value": true,
      "site": "00b40d04",
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
      "00b40d84",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b40d94",
      "DATA",
      [
        "storage",
        "011253e8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b40d84",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b40d94",
      "DATA",
      [
        "storage",
        "011254e8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b40cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40ccc.md#insn-00b40cec) · [`00b40ce8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40ccc.md#insn-00b40ce8) · [`00b40cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40ccc.md#insn-00b40cf4)
- 新版 [`00b40d88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40d68.md#insn-00b40d88) · [`00b40d84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40d68.md#insn-00b40d84) · [`00b40d90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40d68.md#insn-00b40d90)

~~~diff
- 00b40cec ["INT_ADD", "register:40f0:8", ["const:b40cec:8", "const:4:8"]]
- 00b40cec ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b40d88 ["INT_ADD", "register:40f0:8", ["const:b40d88:8", "const:4:8"]]
+ 00b40d88 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b40cec bytes c5680494
+ 00b40d88 bytes d2680494
- 00b40ce8 ["COPY", "tmp:0:8", ["const:367:8"]]
- 00b40ce8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b40ce8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b40ce8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b40d84 ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00b40d84 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b40d84 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b40d84 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b40ce8 bytes 009c0d91
+ 00b40d84 bytes 002c0c91
- 00b40cf4 ["COPY", "tmp:0:8", ["const:3e8:8"]]
- 00b40cf4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b40cf4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b40cf4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b40d90 ["COPY", "tmp:0:8", ["const:4e8:8"]]
+ 00b40d90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b40d90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b40d90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b40cf4 bytes 08a10f91
+ 00b40d90 bytes 08a11391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-deb39d565822841c4155c0b207dcfce4"></a>

### [`00b40d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40d08.md) → [`00b40da4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40da4.md) _ZN8firebase9analytics24analytics_consent_status13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "site": "00b40d48"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b40de4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b40d24"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b40d1c",
      "READ",
      [
        "storage",
        "011253d8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b40d24",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b40de8"
      ]
    ],
    [
      "unmatched:00b40d2c",
      "PARAM",
      [
        "storage",
        "002a3a35",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b40db8",
      "READ",
      [
        "storage",
        "011254d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b40dc0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b40de8"
      ]
    ],
    [
      "00b40dc8",
      "PARAM",
      [
        "storage",
        "002a39e8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b40d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40d08.md#insn-00b40d24) · [`00b40d40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40d08.md#insn-00b40d40) · [`00b40d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40d08.md#insn-00b40d48)
- 新版 [`00b40ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40da4.md#insn-00b40ddc)

~~~diff
- 00b40d24 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b40d24 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b40d24 bytes 410100b5
- 00b40d40 ["INT_ADD", "register:40f0:8", ["const:b40d40:8", "const:4:8"]]
- 00b40d40 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b40ddc ["INT_ADD", "register:40f0:8", ["const:b40ddc:8", "const:4:8"]]
+ 00b40ddc ["CALL", null, ["callee:00c5afe0:8"]]
- 00b40d40 bytes 74680494
+ 00b40ddc bytes 81680494
- 00b40d48 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3d8:8"]]
- 00b40d48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b40d48 bytes 80ee01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ed7b6772b205c4cd526237cf14af0e3"></a>

### [`00b40d78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40d78.md) → [`00b40e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40e14.md) _ZN8firebase9analytics24analytics_consent_status10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
      "definition_site": "00b40e30",
      "incomplete_value": false,
      "site": "00b40e34",
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
            "const:54d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b40d94",
      "incomplete_value": false,
      "site": "00b40d98",
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
            "const:51e:8"
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
      "definition_site": "00b40e40",
      "incomplete_value": true,
      "site": "00b40e4c",
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
      "definition_site": "00b40da4",
      "incomplete_value": true,
      "site": "00b40db0",
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
      "00b40e30",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b40e40",
      "DATA",
      [
        "storage",
        "011253f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b40e30",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b40e40",
      "DATA",
      [
        "storage",
        "011254f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b40d98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40d78.md#insn-00b40d98) · [`00b40d94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40d78.md#insn-00b40d94) · [`00b40da0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40d78.md#insn-00b40da0)
- 新版 [`00b40e34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40e14.md#insn-00b40e34) · [`00b40e30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40e14.md#insn-00b40e30) · [`00b40e3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40e14.md#insn-00b40e3c)

~~~diff
- 00b40d98 ["INT_ADD", "register:40f0:8", ["const:b40d98:8", "const:4:8"]]
- 00b40d98 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b40e34 ["INT_ADD", "register:40f0:8", ["const:b40e34:8", "const:4:8"]]
+ 00b40e34 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b40d98 bytes 9a680494
+ 00b40e34 bytes a7680494
- 00b40d94 ["COPY", "tmp:0:8", ["const:51e:8"]]
- 00b40d94 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b40d94 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b40d94 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b40e30 ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00b40e30 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b40e30 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b40e30 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b40d94 bytes 00781491
+ 00b40e30 bytes 00341591
- 00b40da0 ["COPY", "tmp:0:8", ["const:3f0:8"]]
- 00b40da0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b40da0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b40da0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b40e3c ["COPY", "tmp:0:8", ["const:4f0:8"]]
+ 00b40e3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b40e3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b40e3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b40da0 bytes 08c10f91
+ 00b40e3c bytes 08c11391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6f9cf864ff9b6defb617a31a68cfcbf"></a>

### [`00b40db4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40db4.md) → [`00b40e50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b40e50.md) _ZN8firebase9analytics10InitializeERKNS_3AppE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5a960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a960.md) · 呼出先 13件 [`00c5aba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aba0.md) [`00c5acc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5acc0.md) [`00c5acf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5acf0.md) [`00c5ade0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ade0.md) [`00c5aea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aea0.md)
- 新版 呼出元 1件 [`00c5aa30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aa30.md) · 呼出先 13件 [`00c5ac70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ac70.md) [`00c5ad90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad90.md) [`00c5adc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5adc0.md) [`00c5aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aeb0.md) [`00c5af70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af70.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 46.56% / 新版 46.56%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 16件, `unresolved_branch_alignment` 8件, `unresolved_call_alignment` 10件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 9件

アドレスに依存する影響 `branch_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b40e70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b40ec8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b40f20"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b40e6c",
      "READ",
      [
        "storage",
        "01125400",
        null,
        "undefined8"
      ]
    ],
    [
      "00b40e78",
      "READ",
      [
        "storage",
        "00c9b6a8",
        null,
        "pointer"
      ]
    ],
    [
      "00b40e88",
      "READ",
      [
        "storage",
        "00ca4630",
        "_ZN8firebase9analytics8internal20kAnalyticsModuleNameE",
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b40e6c",
      "READ",
      [
        "storage",
        "01125500",
        null,
        "undefined8"
      ]
    ],
    [
      "00b40e78",
      "READ",
      [
        "storage",
        "00c9b778",
        null,
        "pointer"
      ]
    ],
    [
      "00b40e88",
      "READ",
      [
        "storage",
        "00ca4700",
        "_ZN8firebase9analytics8internal20kAnalyticsModuleNameE",
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b40e4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40db4.md#insn-00b40e4c) · [`00b40e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40db4.md#insn-00b40e70) · [`00b40ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40db4.md#insn-00b40ea4)

~~~diff
- 00b40e4c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b40e4c ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00b40e4c bytes 410100b5
- 00b40e70 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:330:8"]]
- 00b40e70 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b40e70 bytes a09a01f9
- 00b40ea4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b40ea4 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
- 00b40ea4 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2f4e1bcd6ac694167e09d0b857930ab"></a>

### [`00b410a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b41/00b410a8.md) → [`00b41144`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b41144.md) _ZN7_JNIEnv22CallStaticObjectMethodEP7_jclassP10_jmethodIDz

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5aba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aba0.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00c5ac70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ac70.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 82.05% / 新版 82.05%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b41100"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b41100"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b41118"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b41100",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4110c",
      "READ",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b41118",
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
      "00b4119c",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00b411a8",
      "READ",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00b411b4",
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

- 旧版 [`00b41100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b41/00b410a8.md#insn-00b41100) · [`00b41118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b41/00b410a8.md#insn-00b41118) · [`00b4111c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b41/00b410a8.md#insn-00b4111c)
- 新版 [`00b411b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b41144.md#insn-00b411b8)

~~~diff
- 00b41100 ["COPY", "tmp:0:8", ["register:4060:8"]]
- 00b41100 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00b41100 ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffffc8:8"]]
- 00b41100 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b41100 bytes acab3ca9
- 00b41118 ["INT_ADD", "tmp:0:8", ["register:40e8:8", "const:ffffffffffffffa0:8"]]
- 00b41118 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5020:16"]]
- 00b41118 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00b41118 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5000:16"]]
- 00b41118 bytes a1033dad
- 00b4111c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4111c ["INT_ADD", "register:40f0:8", ["const:b4111c:8", "const:4:8"]]
- 00b4111c ["CALLIND", null, ["register:0:8"]]
+ 00b411b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b411b8 ["INT_ADD", "register:40f0:8", ["const:b411b8:8", "const:4:8"]]
+ 00b411b8 ["CALLIND", null, ["register:0:8"]]
- 00b4111c bytes 00013fd6
+ 00b411b8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c6051448732b49efee1e0036e06b164"></a>

### [`00b41158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b41/00b41158.md) → [`00b411f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b411f4.md) _ZN8firebase9analytics9TerminateEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5a940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a940.md) · 呼出先 7件 [`00c5acd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5acd0.md) [`00c5ad00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad00.md) [`00c5ade0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ade0.md) [`00c5af00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af00.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 1件 [`00c5aa10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aa10.md) · 呼出先 7件 [`00c5ada0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ada0.md) [`00c5add0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5add0.md) [`00c5aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aeb0.md) [`00c5afd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afd0.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 40.43% / 新版 40.43%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 8件, `unresolved_store_alignment` 8件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b41194"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b411b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b411dc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b41208",
      "READ",
      [
        "storage",
        "01125400",
        null,
        "undefined8"
      ]
    ],
    [
      "00b41218",
      "READ",
      [
        "storage",
        "00c9b6a8",
        null,
        "pointer"
      ]
    ],
    [
      "00b41220",
      "READ",
      [
        "storage",
        "00ca4630",
        "_ZN8firebase9analytics8internal20kAnalyticsModuleNameE",
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b41208",
      "READ",
      [
        "storage",
        "01125500",
        null,
        "undefined8"
      ]
    ],
    [
      "00b41218",
      "READ",
      [
        "storage",
        "00c9b778",
        null,
        "pointer"
      ]
    ],
    [
      "00b41220",
      "READ",
      [
        "storage",
        "00ca4700",
        "_ZN8firebase9analytics8internal20kAnalyticsModuleNameE",
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4116c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b41/00b41158.md#insn-00b4116c) · [`00b41170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b41/00b41158.md#insn-00b41170) · [`00b41188`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b41/00b41158.md#insn-00b41188)
- 新版 [`00b41208`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b411f4.md#insn-00b41208) · [`00b4120c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b411f4.md#insn-00b4120c) · [`00b41224`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b411f4.md#insn-00b41224)

~~~diff
- 00b4116c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:400:8"]]
- 00b4116c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b41208 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:500:8"]]
+ 00b41208 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4116c bytes 800242f9
+ 00b41208 bytes 808242f9
- 00b41170 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00b41170 ["CBRANCH", null, ["local:b15:8", "tmp:0:1"]]
+ 00b4120c ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00b4120c ["CBRANCH", null, ["local:b16:8", "tmp:0:1"]]
- 00b41170 bytes e00900b4
+ 00b4120c bytes e00900b4
- 00b41188 ["INT_ADD", "register:40f0:8", ["const:b41188:8", "const:4:8"]]
- 00b41188 ["CALL", null, ["callee:00c5afd0:8"]]
+ 00b41224 ["INT_ADD", "register:40f0:8", ["const:b41224:8", "const:4:8"]]
+ 00b41224 ["CALL", null, ["callee:00c5afd0:8"]]
- 00b41188 bytes 5e670494
+ 00b41224 bytes 6b670494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-213aee6d00861e6a40b29ed42336baf7"></a>

### [`00b412d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b41/00b412d0.md) → [`00b4136c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b4136c.md) _ZN8firebase9analytics29SetAnalyticsCollectionEnabledEb

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b41380",
      "incomplete_value": true,
      "site": "00b41380",
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
      "definition_site": "00b412e4",
      "incomplete_value": true,
      "site": "00b412e4",
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
      "definition_site": "00b41398",
      "incomplete_value": true,
      "site": "00b413a8",
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
                "const:508:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b412fc",
      "incomplete_value": true,
      "site": "00b4130c",
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
                "const:408:8"
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
      "definition_site": "00b4139c",
      "incomplete_value": true,
      "site": "00b413a8",
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
                "const:440:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b41300",
      "incomplete_value": true,
      "site": "00b4130c",
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
                "const:340:8"
              ]
            ]
          ]
        ]
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
      "00b4137c",
      "READ",
      [
        "storage",
        "01125400",
        null,
        "undefined8"
      ]
    ],
    [
      "00b41398",
      "READ",
      [
        "storage",
        "01125408",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4139c",
      "READ",
      [
        "storage",
        "01125340",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4137c",
      "READ",
      [
        "storage",
        "01125500",
        null,
        "undefined8"
      ]
    ],
    [
      "00b41398",
      "READ",
      [
        "storage",
        "01125508",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4139c",
      "READ",
      [
        "storage",
        "01125440",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4130c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b41/00b412d0.md#insn-00b4130c) · [`00b412e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b41/00b412d0.md#insn-00b412e0) · [`00b412f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b41/00b412d0.md#insn-00b412f0)
- 新版 [`00b413a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b4136c.md#insn-00b413a8) · [`00b4137c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b4136c.md#insn-00b4137c) · [`00b4138c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b4136c.md#insn-00b4138c)

~~~diff
- 00b4130c ["INT_ADD", "register:40f0:8", ["const:b4130c:8", "const:4:8"]]
- 00b4130c ["CALL", null, ["callee:00574d2c:8"]]
+ 00b413a8 ["INT_ADD", "register:40f0:8", ["const:b413a8:8", "const:4:8"]]
+ 00b413a8 ["CALL", null, ["callee:00574d2c:8"]]
- 00b4130c bytes 78cee897
+ 00b413a8 bytes 61cee897
- 00b412e0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:400:8"]]
- 00b412e0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4137c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:500:8"]]
+ 00b4137c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b412e0 bytes 080142f9
+ 00b4137c bytes 088142f9
- 00b412f0 ["INT_ADD", "register:40f0:8", ["const:b412f0:8", "const:4:8"]]
- 00b412f0 ["CALL", null, ["callee:00c5b150:8"]]
+ 00b4138c ["INT_ADD", "register:40f0:8", ["const:b4138c:8", "const:4:8"]]
+ 00b4138c ["CALL", null, ["callee:00c5b150:8"]]
- 00b412f0 bytes 64670494
+ 00b4138c bytes 71670494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1e8ae74f004893ac722ba13a2a995ee"></a>

### [`00b41334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b41/00b41334.md) → [`00b413d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b413d0.md) _ZN8firebase9analytics10SetConsentERKNSt6__ndk13mapINS0_11ConsentTypeENS0_13ConsentStatusENS1_4lessIS3_EENS1_9allocatorINS1_4pairIKS3_S4_EEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 12件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5aee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aee0.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00589734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589734.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5afb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afb0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 58.62% / 新版 58.62%

CFGの説明率　旧版 7.35% / 新版 7.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `unresolved_branch_alignment` 8件, `unresolved_call_alignment` 13件, `unresolved_store_alignment` 12件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b41334"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b41334"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b41338"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b41334",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b41338",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4133c",
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
      "00b413d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b413d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b413d8",
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

- 旧版 [`00b41334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b41/00b41334.md#insn-00b41334) · [`00b41338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b41/00b41334.md#insn-00b41338) · [`00b4133c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b41/00b41334.md#insn-00b4133c)

~~~diff
- 00b41334 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b41334 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00b41334 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffa0:8"]]
- 00b41334 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b41334 bytes fc6fbaa9
- 00b41338 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b41338 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b41338 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b41338 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b41338 bytes fa6701a9
- 00b4133c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b4133c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b4133c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b4133c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4133c bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d70a2b067a96e9d08c4212b6a208a747"></a>

### [`00b41778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b41/00b41778.md) → [`00b41814`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b41814.md) _ZN8firebase9analytics11AddToBundleEP7_JNIEnvP8_jobjectPKcd

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af90.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b060.md)

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b417a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b417c0",
      "incomplete_value": true,
      "site": "00b417c8",
      "value": [
        "live",
        "register:40a8:8"
      ]
    },
    "ordinal": 2,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b41840"
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
      "unmatched:00b417e8",
      "READ",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b417ec",
      "READ",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b417a4",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b41884",
      "READ",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b41888",
      "READ",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "00b41840",
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

- 旧版 [`00b417a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b41/00b41778.md#insn-00b417a4) · [`00b417c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b41/00b41778.md#insn-00b417c8)
- 新版 [`00b41864`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b41814.md#insn-00b41864) · [`00b41840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b41814.md#insn-00b41840)

~~~diff
- 00b417a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b417a4 ["INT_ADD", "register:40f0:8", ["const:b417a4:8", "const:4:8"]]
- 00b417a4 ["CALLIND", null, ["register:0:8"]]
- 00b417a4 bytes 00013fd6
- 00b417c8 ["INT_ADD", "register:40f0:8", ["const:b417c8:8", "const:4:8"]]
- 00b417c8 ["CALL", null, ["callee:00574d2c:8"]]
+ 00b41864 ["INT_ADD", "register:40f0:8", ["const:b41864:8", "const:4:8"]]
+ 00b41864 ["CALL", null, ["callee:00574d2c:8"]]
- 00b417c8 bytes 49cde897
+ 00b41864 bytes 32cde897
+ 00b41840 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b41840 ["INT_ADD", "register:40f0:8", ["const:b41840:8", "const:4:8"]]
+ 00b41840 ["CALLIND", null, ["register:0:8"]]
+ 00b41840 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2bc49870da8a94dd1088aac67d8d2266"></a>

### [`00b417f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b41/00b417f8.md) → [`00b41894`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b41894.md) _ZN8firebase9analytics11AddToBundleEP7_JNIEnvP8_jobjectPKcl

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af90.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b060.md)

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 70.00% / 新版 70.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b417f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b417f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b417fc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b417f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b417fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b41800",
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
      "00b41894",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b41898",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b4189c",
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

- 旧版 [`00b417f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b41/00b417f8.md#insn-00b417f8) · [`00b417fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b41/00b417f8.md#insn-00b417fc) · [`00b41800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b41/00b417f8.md#insn-00b41800)

~~~diff
- 00b417f8 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b417f8 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b417f8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b417f8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b417f8 bytes f657bda9
- 00b417fc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b417fc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b417fc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b417fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b417fc bytes f44f01a9
- 00b41800 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b41800 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b41800 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b41800 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b41800 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f35b267b29bc5e165816b01ceabcf97a"></a>

### [`00b41c20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b41/00b41c20.md) → [`00b41cbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b41cbc.md) _ZN8firebase9analytics18AddVariantToBundleEP7_JNIEnvP8_jobjectPKcRKNS_7VariantE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b020.md) · 呼出先 7件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00c5ab00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ab00.md) [`00c5ab20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ab20.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af90.md)
- 新版 呼出元 1件 [`00c5b0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0f0.md) · 呼出先 7件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00c5abd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5abd0.md) [`00c5abf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5abf0.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b060.md)

変更の種類 call, call_argument_candidate, call_count, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 84.31% / 新版 84.31%

CFGの説明率　旧版 30.19% / 新版 30.19%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `unresolved_call_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b41d08"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b41d14"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b41d1c",
      "incomplete_value": true,
      "site": "00b41d2c",
      "value": [
        "live",
        "register:4098:8"
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
      "00b41cf0",
      "DATA",
      [
        "storage",
        "0030b599",
        "switchD_00b41c6c::switchdataD_0030b599",
        "byte"
      ]
    ],
    [
      "unmatched:00b41d14",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b060"
      ]
    ],
    [
      "unmatched:00b41da4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5abd0"
      ]
    ]
  ],
  "added": [
    [
      "00b41cf0",
      "DATA",
      [
        "storage",
        "0030b5d9",
        "switchD_00b41d08::switchdataD_0030b5d9",
        "byte"
      ]
    ],
    [
      "00b41db0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b060"
      ]
    ],
    [
      "00b41e64",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b060"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b41cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b41/00b41c20.md#insn-00b41cbc) · [`00b41d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b41/00b41c20.md#insn-00b41d08) · [`00b41d14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b41/00b41c20.md#insn-00b41d14)
- 新版 [`00b41d58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b41cbc.md#insn-00b41d58)

~~~diff
- 00b41cbc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b41cbc ["INT_ADD", "register:40f0:8", ["const:b41cbc:8", "const:4:8"]]
- 00b41cbc ["CALLIND", null, ["register:0:8"]]
+ 00b41d58 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b41d58 ["INT_ADD", "register:40f0:8", ["const:b41d58:8", "const:4:8"]]
+ 00b41d58 ["CALLIND", null, ["register:0:8"]]
- 00b41cbc bytes 00013fd6
+ 00b41d58 bytes 00013fd6
- 00b41d08 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b41d08 ["INT_ADD", "register:40f0:8", ["const:b41d08:8", "const:4:8"]]
- 00b41d08 ["CALLIND", null, ["register:0:8"]]
- 00b41d08 bytes 00013fd6
- 00b41d14 ["INT_ADD", "register:40f0:8", ["const:b41d14:8", "const:4:8"]]
- 00b41d14 ["CALL", null, ["callee:00c5b060:8"]]
- 00b41d14 bytes 9f640494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f10bb55663dd7c8c96065d0afb6138de"></a>

### [`00b41f50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b41/00b41f50.md) → [`00b41fec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b41fec.md) _ZN8firebase9analytics8LogEventEPKcS2_S2_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af90.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00589734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589734.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b060.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.88% / 新版 95.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b42008",
      "incomplete_value": true,
      "site": "00b42008",
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
      "definition_site": "00b41f6c",
      "incomplete_value": true,
      "site": "00b41f6c",
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
      "definition_site": "00b420e4",
      "incomplete_value": true,
      "site": "00b420fc",
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
                "const:508:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b42048",
      "incomplete_value": true,
      "site": "00b42060",
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
                "const:408:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b420e8",
      "incomplete_value": true,
      "site": "00b420fc",
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
                "const:450:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4204c",
      "incomplete_value": true,
      "site": "00b42060",
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
                "const:350:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b42004",
      "READ",
      [
        "storage",
        "01125400",
        null,
        "undefined8"
      ]
    ],
    [
      "00b420e4",
      "READ",
      [
        "storage",
        "01125408",
        null,
        "undefined8"
      ]
    ],
    [
      "00b420e8",
      "READ",
      [
        "storage",
        "01125350",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b42004",
      "READ",
      [
        "storage",
        "01125500",
        null,
        "undefined8"
      ]
    ],
    [
      "00b420e4",
      "READ",
      [
        "storage",
        "01125508",
        null,
        "undefined8"
      ]
    ],
    [
      "00b420e8",
      "READ",
      [
        "storage",
        "01125450",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b41fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b41/00b41f50.md#insn-00b41fe0) · [`00b42060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b41/00b41f50.md#insn-00b42060) · [`00b4207c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b41/00b41f50.md#insn-00b4207c)
- 新版 [`00b4207c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b41fec.md#insn-00b4207c) · [`00b420fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b41fec.md#insn-00b420fc) · [`00b42118`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b41/00b41fec.md#insn-00b42118)

~~~diff
- 00b41fe0 ["INT_ADD", "register:40f0:8", ["const:b41fe0:8", "const:4:8"]]
- 00b41fe0 ["CALL", null, ["callee:00c5b060:8"]]
+ 00b4207c ["INT_ADD", "register:40f0:8", ["const:b4207c:8", "const:4:8"]]
+ 00b4207c ["CALL", null, ["callee:00c5b060:8"]]
- 00b41fe0 bytes ec630494
+ 00b4207c bytes f9630494
- 00b42060 ["INT_ADD", "register:40f0:8", ["const:b42060:8", "const:4:8"]]
- 00b42060 ["CALL", null, ["callee:00574d2c:8"]]
+ 00b420fc ["INT_ADD", "register:40f0:8", ["const:b420fc:8", "const:4:8"]]
+ 00b420fc ["CALL", null, ["callee:00574d2c:8"]]
- 00b42060 bytes 23cbe897
+ 00b420fc bytes 0ccbe897
- 00b4207c ["INT_ADD", "register:40f0:8", ["const:b4207c:8", "const:4:8"]]
- 00b4207c ["CALL", null, ["callee:00c5ad70:8"]]
+ 00b42118 ["INT_ADD", "register:40f0:8", ["const:b42118:8", "const:4:8"]]
+ 00b42118 ["CALL", null, ["callee:00c5ad70:8"]]
- 00b4207c bytes 09630494
+ 00b42118 bytes 16630494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-315bd4e42ede2df365faa7806583540e"></a>

### [`00b420d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b420d4.md) → [`00b42170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42170.md) _ZN8firebase9analytics8LogEventEPKcS2_d

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 8件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af90.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00589734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589734.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b060.md)

変更の種類 branch_value, call, call_argument_candidate, call_count, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 90.70% / 新版 90.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_call_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4218c",
      "incomplete_value": true,
      "site": "00b4218c",
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
      "definition_site": "00b420f0",
      "incomplete_value": true,
      "site": "00b420f0",
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
    "new": null,
    "old": {
      "definition_site": "00b42148",
      "incomplete_value": false,
      "site": "00b4214c",
      "value": [
        "leaf",
        "const:4:8"
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b42194"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b42188",
      "READ",
      [
        "storage",
        "01125400",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4223c",
      "READ",
      [
        "storage",
        "01125408",
        null,
        "undefined8"
      ]
    ],
    [
      "00b42240",
      "READ",
      [
        "storage",
        "01125350",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b42188",
      "READ",
      [
        "storage",
        "01125500",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4223c",
      "READ",
      [
        "storage",
        "01125508",
        null,
        "undefined8"
      ]
    ],
    [
      "00b42240",
      "READ",
      [
        "storage",
        "01125450",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4214c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b420d4.md#insn-00b4214c) · [`00b42194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b420d4.md#insn-00b42194) · [`00b421b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b420d4.md#insn-00b421b8)
- 新版 [`00b421e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42170.md#insn-00b421e8) · [`00b42254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42170.md#insn-00b42254)

~~~diff
- 00b4214c ["INT_ADD", "register:40f0:8", ["const:b4214c:8", "const:4:8"]]
- 00b4214c ["CALL", null, ["callee:00c5b060:8"]]
+ 00b421e8 ["INT_ADD", "register:40f0:8", ["const:b421e8:8", "const:4:8"]]
+ 00b421e8 ["CALL", null, ["callee:00c5b060:8"]]
- 00b4214c bytes 91630494
+ 00b421e8 bytes 9e630494
- 00b42194 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b42194 ["INT_ADD", "register:40f0:8", ["const:b42194:8", "const:4:8"]]
- 00b42194 ["CALLIND", null, ["register:0:8"]]
- 00b42194 bytes 00013fd6
- 00b421b8 ["INT_ADD", "register:40f0:8", ["const:b421b8:8", "const:4:8"]]
- 00b421b8 ["CALL", null, ["callee:00574d2c:8"]]
+ 00b42254 ["INT_ADD", "register:40f0:8", ["const:b42254:8", "const:4:8"]]
+ 00b42254 ["CALL", null, ["callee:00574d2c:8"]]
- 00b421b8 bytes cdcae897
+ 00b42254 bytes b6cae897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1075f1798578f88eae3c1c4a53db245d"></a>

### [`00b4222c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b4222c.md) → [`00b422c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b422c8.md) _ZN8firebase9analytics8LogEventEPKcS2_l

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5b060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b060.md) · 呼出先 8件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af90.md)
- 新版 呼出元 1件 [`00c5b130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b130.md) · 呼出先 8件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00589734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589734.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b060.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b422e4",
      "incomplete_value": true,
      "site": "00b422e4",
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
      "definition_site": "00b42248",
      "incomplete_value": true,
      "site": "00b42248",
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
      "definition_site": "00b42394",
      "incomplete_value": true,
      "site": "00b423ac",
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
                "const:508:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b422f8",
      "incomplete_value": true,
      "site": "00b42310",
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
                "const:408:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b42398",
      "incomplete_value": true,
      "site": "00b423ac",
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
                "const:450:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b422fc",
      "incomplete_value": true,
      "site": "00b42310",
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
                "const:350:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b422e0",
      "READ",
      [
        "storage",
        "01125400",
        null,
        "undefined8"
      ]
    ],
    [
      "00b42394",
      "READ",
      [
        "storage",
        "01125408",
        null,
        "undefined8"
      ]
    ],
    [
      "00b42398",
      "READ",
      [
        "storage",
        "01125350",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b422e0",
      "READ",
      [
        "storage",
        "01125500",
        null,
        "undefined8"
      ]
    ],
    [
      "00b42394",
      "READ",
      [
        "storage",
        "01125508",
        null,
        "undefined8"
      ]
    ],
    [
      "00b42398",
      "READ",
      [
        "storage",
        "01125450",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b42310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b4222c.md#insn-00b42310) · [`00b4232c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b4222c.md#insn-00b4232c) · [`00b42244`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b4222c.md#insn-00b42244)
- 新版 [`00b423ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b422c8.md#insn-00b423ac) · [`00b423c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b422c8.md#insn-00b423c8) · [`00b422e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b422c8.md#insn-00b422e0)

~~~diff
- 00b42310 ["INT_ADD", "register:40f0:8", ["const:b42310:8", "const:4:8"]]
- 00b42310 ["CALL", null, ["callee:00574d2c:8"]]
+ 00b423ac ["INT_ADD", "register:40f0:8", ["const:b423ac:8", "const:4:8"]]
+ 00b423ac ["CALL", null, ["callee:00574d2c:8"]]
- 00b42310 bytes 77cae897
+ 00b423ac bytes 60cae897
- 00b4232c ["INT_ADD", "register:40f0:8", ["const:b4232c:8", "const:4:8"]]
- 00b4232c ["CALL", null, ["callee:00c5ad70:8"]]
+ 00b423c8 ["INT_ADD", "register:40f0:8", ["const:b423c8:8", "const:4:8"]]
+ 00b423c8 ["CALL", null, ["callee:00c5ad70:8"]]
- 00b4232c bytes 5d620494
+ 00b423c8 bytes 6a620494
- 00b42244 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:400:8"]]
- 00b42244 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b422e0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:500:8"]]
+ 00b422e0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b42244 bytes 080142f9
+ 00b422e0 bytes 088142f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63f6bb4e43a6e651fb7aeacc690a9ece"></a>

### [`00b42398`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b42398.md) → [`00b42434`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42434.md) _ZN8firebase9analytics8LogEventEPKcPKNS0_9ParameterEm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5a990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a990.md) · 呼出先 10件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af90.md)
- 新版 呼出元 1件 [`00c5aa60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aa60.md) · 呼出先 10件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00589734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589734.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b060.md)

変更の種類 branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 92.47% / 新版 92.47%

CFGの説明率　旧版 92.31% / 新版 85.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b42454",
      "incomplete_value": true,
      "site": "00b42454",
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
      "definition_site": "00b423b8",
      "incomplete_value": true,
      "site": "00b423b8",
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
      "definition_site": "00b42514",
      "incomplete_value": true,
      "site": "00b4252c",
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
                "const:508:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b42478",
      "incomplete_value": true,
      "site": "00b42490",
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
                "const:408:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b42518",
      "incomplete_value": true,
      "site": "00b4252c",
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
                "const:450:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4247c",
      "incomplete_value": true,
      "site": "00b42490",
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
                "const:350:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b42450",
      "READ",
      [
        "storage",
        "01125400",
        null,
        "undefined8"
      ]
    ],
    [
      "00b424e8",
      "PARAM",
      [
        "storage",
        "002be540",
        null,
        "string"
      ]
    ],
    [
      "00b42514",
      "READ",
      [
        "storage",
        "01125408",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b42450",
      "READ",
      [
        "storage",
        "01125500",
        null,
        "undefined8"
      ]
    ],
    [
      "00b424e8",
      "PARAM",
      [
        "storage",
        "002be4ec",
        null,
        "string"
      ]
    ],
    [
      "00b42514",
      "READ",
      [
        "storage",
        "01125508",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b42454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b42398.md#insn-00b42454) · [`00b42490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b42398.md#insn-00b42490) · [`00b424ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b42398.md#insn-00b424ac)
- 新版 [`00b424f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42434.md#insn-00b424f0) · [`00b4252c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42434.md#insn-00b4252c) · [`00b42548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42434.md#insn-00b42548)

~~~diff
- 00b42454 ["INT_ADD", "register:40f0:8", ["const:b42454:8", "const:4:8"]]
- 00b42454 ["CALL", null, ["callee:00c5ad70:8"]]
+ 00b424f0 ["INT_ADD", "register:40f0:8", ["const:b424f0:8", "const:4:8"]]
+ 00b424f0 ["CALL", null, ["callee:00c5ad70:8"]]
- 00b42454 bytes 13620494
+ 00b424f0 bytes 20620494
- 00b42490 ["INT_ADD", "register:40f0:8", ["const:b42490:8", "const:4:8"]]
- 00b42490 ["CALL", null, ["callee:00574d2c:8"]]
+ 00b4252c ["INT_ADD", "register:40f0:8", ["const:b4252c:8", "const:4:8"]]
+ 00b4252c ["CALL", null, ["callee:00574d2c:8"]]
- 00b42490 bytes 17cae897
+ 00b4252c bytes 00cae897
- 00b424ac ["INT_ADD", "register:40f0:8", ["const:b424ac:8", "const:4:8"]]
- 00b424ac ["CALL", null, ["callee:00c5ad70:8"]]
+ 00b42548 ["INT_ADD", "register:40f0:8", ["const:b42548:8", "const:4:8"]]
+ 00b42548 ["CALL", null, ["callee:00c5ad70:8"]]
- 00b424ac bytes fd610494
+ 00b42548 bytes 0a620494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb8c263e1f8b817052b92275c2db89d3"></a>

### [`00b4250c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b4250c.md) → [`00b425a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b425a8.md) _ZN8firebase9analytics19LogAppleTransactionEPKc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 9件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5abe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abe0.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5acb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5acb0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md) [`00c5acb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5acb0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ad80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 96.72% / 新版 96.72%

CFGの説明率　旧版 55.56% / 新版 55.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b42618",
      "incomplete_value": false,
      "site": "00b4262c",
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
            "const:38e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4257c",
      "incomplete_value": false,
      "site": "00b42590",
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
            "const:3ea:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b425f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b42694"
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
      "unmatched:00b4257c",
      "PARAM",
      [
        "storage",
        "002a63ea",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b42618",
      "PARAM",
      [
        "storage",
        "002a638e",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b42590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b4250c.md#insn-00b42590) · [`00b425f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b4250c.md#insn-00b425f8)
- 新版 [`00b4262c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b425a8.md#insn-00b4262c) · [`00b42694`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b425a8.md#insn-00b42694)

~~~diff
- 00b42590 ["INT_ADD", "register:40f0:8", ["const:b42590:8", "const:4:8"]]
- 00b42590 ["CALL", null, ["callee:00c5ae70:8"]]
+ 00b4262c ["INT_ADD", "register:40f0:8", ["const:b4262c:8", "const:4:8"]]
+ 00b4262c ["CALL", null, ["callee:00c5ae70:8"]]
- 00b42590 bytes 04620494
+ 00b4262c bytes 11620494
- 00b425f8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b425f8 ["RETURN", null, ["register:0:8"]]
- 00b425f8 bytes c0035fd6
+ 00b42694 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b42694 ["RETURN", null, ["register:0:8"]]
+ 00b42694 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b0178310550f2bb6448a3b63e6f2264"></a>

### [`00b42644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b42644.md) → [`00b426e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b426e0.md) _ZN8firebase6FutureIvEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`00c5add0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5add0.md) · 呼出先 3件 [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5adf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5adf0.md) [`00c5ae00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae00.md)
- 新版 呼出元 1件 [`00c5aea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aea0.md) · 呼出先 3件 [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5aec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aec0.md) [`00c5aed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aed0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 33.33% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b42690",
      "incomplete_value": true,
      "site": "00b42694",
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

- 旧版 [`00b42694`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b42644.md#insn-00b42694) · [`00b42664`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b42644.md#insn-00b42664) · [`00b42678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b42644.md#insn-00b42678)
- 新版 [`00b42730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b426e0.md#insn-00b42730) · [`00b42700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b426e0.md#insn-00b42700) · [`00b42714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b426e0.md#insn-00b42714)

~~~diff
- 00b42694 ["INT_ADD", "register:40f0:8", ["const:b42694:8", "const:4:8"]]
- 00b42694 ["CALL", null, ["callee:00c5aec0:8"]]
+ 00b42730 ["INT_ADD", "register:40f0:8", ["const:b42730:8", "const:4:8"]]
+ 00b42730 ["CALL", null, ["callee:00c5aec0:8"]]
- 00b42694 bytes d7610494
+ 00b42730 bytes e4610494
- 00b42664 ["INT_ADD", "register:40f0:8", ["const:b42664:8", "const:4:8"]]
- 00b42664 ["CALL", null, ["callee:00c5ad40:8"]]
+ 00b42700 ["INT_ADD", "register:40f0:8", ["const:b42700:8", "const:4:8"]]
+ 00b42700 ["CALL", null, ["callee:00c5ad40:8"]]
- 00b42664 bytes 83610494
+ 00b42700 bytes 90610494
- 00b42678 ["INT_ADD", "register:40f0:8", ["const:b42678:8", "const:4:8"]]
- 00b42678 ["CALL", null, ["callee:00c5aed0:8"]]
+ 00b42714 ["INT_ADD", "register:40f0:8", ["const:b42714:8", "const:4:8"]]
+ 00b42714 ["CALL", null, ["callee:00c5aed0:8"]]
- 00b42678 bytes e2610494
+ 00b42714 bytes ef610494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15e66ca04f476b1693de7f89f8c34406"></a>

### [`00b426e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b426e4.md) → [`00b42780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42780.md) _ZN8firebase9analytics29LogAppleTransactionLastResultEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5abe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abe0.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5acb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5acb0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5acb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5acb0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ad80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.44% / 新版 97.44%

CFGの説明率　旧版 57.14% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b427ac",
      "incomplete_value": true,
      "site": "00b427b0",
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
    "old": {
      "definition_site": "00b42710",
      "incomplete_value": true,
      "site": "00b42714",
      "value": [
        "live",
        "register:40a8:8"
      ]
    },
    "ordinal": 2,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b42714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b426e4.md#insn-00b42714) · [`00b426f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b426e4.md#insn-00b426f8) · [`00b426fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b426e4.md#insn-00b426fc)
- 新版 [`00b427b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42780.md#insn-00b427b0) · [`00b42794`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42780.md#insn-00b42794) · [`00b42798`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42780.md#insn-00b42798)

~~~diff
- 00b42714 ["INT_ADD", "register:40f0:8", ["const:b42714:8", "const:4:8"]]
- 00b42714 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00b427b0 ["INT_ADD", "register:40f0:8", ["const:b427b0:8", "const:4:8"]]
+ 00b427b0 ["CALL", null, ["callee:00c5aad0:8"]]
- 00b42714 bytes bb600494
+ 00b427b0 bytes c8600494
- 00b426f8 ["INT_ADD", "register:40f0:8", ["const:b426f8:8", "const:4:8"]]
- 00b426f8 ["CALL", null, ["callee:00c5ad80:8"]]
+ 00b42794 ["INT_ADD", "register:40f0:8", ["const:b42794:8", "const:4:8"]]
+ 00b42794 ["CALL", null, ["callee:00c5ad80:8"]]
- 00b426f8 bytes 6e610494
+ 00b42794 bytes 7b610494
- 00b426fc ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00b426fc ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b42798 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00b42798 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b426fc bytes a00200b4
+ 00b42798 bytes a00200b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6cefc9612dca14c1876aa92ea0e0c966"></a>

### [`00b427c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b427c4.md) → [`00b42860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42860.md) _ZN8firebase9analytics25SetDefaultEventParametersEPKNS0_9ParameterEm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b040.md) · 呼出先 10件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af90.md)
- 新版 呼出元 1件 [`00c5b110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b110.md) · 呼出先 10件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00589734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589734.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b060.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 11.54% / 新版 11.54%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b42880",
      "incomplete_value": true,
      "site": "00b42880",
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
      "definition_site": "00b427e4",
      "incomplete_value": true,
      "site": "00b427e4",
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
      "definition_site": "00b4295c",
      "incomplete_value": true,
      "site": "00b4296c",
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
                "const:508:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b428c0",
      "incomplete_value": true,
      "site": "00b428d0",
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
              [
                "leaf",
                "const:408:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b42960",
      "incomplete_value": true,
      "site": "00b4296c",
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
                "const:490:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b428c4",
      "incomplete_value": true,
      "site": "00b428d0",
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
                "register:4048:8"
              ],
              [
                "leaf",
                "const:390:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4287c",
      "READ",
      [
        "storage",
        "01125400",
        null,
        "undefined8"
      ]
    ],
    [
      "00b428cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b42900"
      ]
    ],
    [
      "00b428d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b42900"
      ]
    ]
  ],
  "added": [
    [
      "00b4287c",
      "READ",
      [
        "storage",
        "01125500",
        null,
        "undefined8"
      ]
    ],
    [
      "00b428cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4299c"
      ]
    ],
    [
      "00b428d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4299c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b427e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b427c4.md#insn-00b427e4) · [`00b42880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b427c4.md#insn-00b42880) · [`00b428d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b427c4.md#insn-00b428d0)
- 新版 [`00b42880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42860.md#insn-00b42880) · [`00b4291c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42860.md#insn-00b4291c) · [`00b4296c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42860.md#insn-00b4296c)

~~~diff
- 00b427e4 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b427e4 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
+ 00b42880 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b42880 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
- 00b427e4 bytes a80500b4
+ 00b42880 bytes a80500b4
- 00b42880 ["INT_ADD", "register:40f0:8", ["const:b42880:8", "const:4:8"]]
- 00b42880 ["CALL", null, ["callee:00c5b0c0:8"]]
+ 00b4291c ["INT_ADD", "register:40f0:8", ["const:b4291c:8", "const:4:8"]]
+ 00b4291c ["CALL", null, ["callee:00c5b0c0:8"]]
- 00b42880 bytes dc610494
+ 00b4291c bytes e9610494
- 00b428d0 ["INT_ADD", "register:40f0:8", ["const:b428d0:8", "const:4:8"]]
- 00b428d0 ["CALL", null, ["callee:00574d2c:8"]]
+ 00b4296c ["INT_ADD", "register:40f0:8", ["const:b4296c:8", "const:4:8"]]
+ 00b4296c ["CALL", null, ["callee:00574d2c:8"]]
- 00b428d0 bytes 07c9e897
+ 00b4296c bytes f0c8e897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0836f2d40ce384785d106852c726769f"></a>

### [`00b42a08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b42a08.md) → [`00b42aa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42aa4.md) _ZN8firebase9analytics15SetUserPropertyEPKcS2_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 90.77% / 新版 90.77%

CFGの説明率　旧版 46.15% / 新版 46.15%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_call_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b42ac0",
      "incomplete_value": true,
      "site": "00b42ac0",
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
      "definition_site": "00b42a24",
      "incomplete_value": true,
      "site": "00b42a24",
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
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b42a64"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b42b3c",
      "incomplete_value": true,
      "site": "00b42b48",
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
      "00b42abc",
      "READ",
      [
        "storage",
        "01125400",
        null,
        "undefined8"
      ]
    ],
    [
      "00b42b1c",
      "PARAM",
      [
        "storage",
        "002a2915",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b42a98",
      "READ",
      [
        "storage",
        "01125408",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b42abc",
      "READ",
      [
        "storage",
        "01125500",
        null,
        "undefined8"
      ]
    ],
    [
      "00b42b1c",
      "PARAM",
      [
        "storage",
        "002a28c8",
        null,
        "string"
      ]
    ],
    [
      "00b42b34",
      "READ",
      [
        "storage",
        "01125508",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b42a24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b42a08.md#insn-00b42a24) · [`00b42a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b42a08.md#insn-00b42a64) · [`00b42aac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b42a08.md#insn-00b42aac)
- 新版 [`00b42ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42aa4.md#insn-00b42ac0) · [`00b42b48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42aa4.md#insn-00b42b48)

~~~diff
- 00b42a24 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b42a24 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b42ac0 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b42ac0 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b42a24 bytes 680200b4
+ 00b42ac0 bytes 680200b4
- 00b42a64 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b42a64 ["INT_ADD", "register:40f0:8", ["const:b42a64:8", "const:4:8"]]
- 00b42a64 ["CALLIND", null, ["register:0:8"]]
- 00b42a64 bytes 00013fd6
- 00b42aac ["INT_ADD", "register:40f0:8", ["const:b42aac:8", "const:4:8"]]
- 00b42aac ["CALL", null, ["callee:00574d2c:8"]]
+ 00b42b48 ["INT_ADD", "register:40f0:8", ["const:b42b48:8", "const:4:8"]]
+ 00b42b48 ["CALL", null, ["callee:00574d2c:8"]]
- 00b42aac bytes 90c8e897
+ 00b42b48 bytes 79c8e897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6372b83676cf8f4fb5204a8349bf1fb"></a>

### [`00b42b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b42b0c.md) → [`00b42ba8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42ba8.md) _ZN8firebase9analytics9SetUserIdEPKc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5a980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a980.md) · 呼出先 5件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md)
- 新版 呼出元 1件 [`00c5aa50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aa50.md) · 呼出先 5件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 92.45% / 新版 92.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b42bc0",
      "incomplete_value": true,
      "site": "00b42bc0",
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
      "definition_site": "00b42b24",
      "incomplete_value": true,
      "site": "00b42b24",
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
      "definition_site": "00b42c18",
      "incomplete_value": true,
      "site": "00b42c28",
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
                "const:508:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b42b7c",
      "incomplete_value": true,
      "site": "00b42b8c",
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
                "const:408:8"
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
      "definition_site": "00b42c1c",
      "incomplete_value": true,
      "site": "00b42c28",
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
                "const:460:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b42b80",
      "incomplete_value": true,
      "site": "00b42b8c",
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
                "const:360:8"
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
      "00b42bbc",
      "READ",
      [
        "storage",
        "01125400",
        null,
        "undefined8"
      ]
    ],
    [
      "00b42c00",
      "PARAM",
      [
        "storage",
        "002a2915",
        null,
        "string"
      ]
    ],
    [
      "00b42c18",
      "READ",
      [
        "storage",
        "01125408",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b42bbc",
      "READ",
      [
        "storage",
        "01125500",
        null,
        "undefined8"
      ]
    ],
    [
      "00b42c00",
      "PARAM",
      [
        "storage",
        "002a28c8",
        null,
        "string"
      ]
    ],
    [
      "00b42c18",
      "READ",
      [
        "storage",
        "01125508",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b42b8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b42b0c.md#insn-00b42b8c) · [`00b42ba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b42b0c.md#insn-00b42ba8) · [`00b42b20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b42b0c.md#insn-00b42b20)
- 新版 [`00b42c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42ba8.md#insn-00b42c28) · [`00b42c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42ba8.md#insn-00b42c44) · [`00b42bbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42ba8.md#insn-00b42bbc)

~~~diff
- 00b42b8c ["INT_ADD", "register:40f0:8", ["const:b42b8c:8", "const:4:8"]]
- 00b42b8c ["CALL", null, ["callee:00574d2c:8"]]
+ 00b42c28 ["INT_ADD", "register:40f0:8", ["const:b42c28:8", "const:4:8"]]
+ 00b42c28 ["CALL", null, ["callee:00574d2c:8"]]
- 00b42b8c bytes 58c8e897
+ 00b42c28 bytes 41c8e897
- 00b42ba8 ["INT_ADD", "register:40f0:8", ["const:b42ba8:8", "const:4:8"]]
- 00b42ba8 ["CALL", null, ["callee:00c5ad70:8"]]
+ 00b42c44 ["INT_ADD", "register:40f0:8", ["const:b42c44:8", "const:4:8"]]
+ 00b42c44 ["CALL", null, ["callee:00c5ad70:8"]]
- 00b42ba8 bytes 3e600494
+ 00b42c44 bytes 4b600494
- 00b42b20 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:400:8"]]
- 00b42b20 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b42bbc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:500:8"]]
+ 00b42bbc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b42b20 bytes 080142f9
+ 00b42bbc bytes 088142f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b58ac08268665f34b617c982f3895bf3"></a>

### [`00b42be0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b42be0.md) → [`00b42c7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42c7c.md) _ZN8firebase9analytics25SetSessionTimeoutDurationEl

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5a970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a970.md) · 呼出先 4件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md)
- 新版 呼出元 1件 [`00c5aa40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aa40.md) · 呼出先 4件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b42c90",
      "incomplete_value": true,
      "site": "00b42c90",
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
      "definition_site": "00b42bf4",
      "incomplete_value": true,
      "site": "00b42bf4",
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
      "definition_site": "00b42ca8",
      "incomplete_value": true,
      "site": "00b42cb8",
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
                "const:508:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b42c0c",
      "incomplete_value": true,
      "site": "00b42c1c",
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
                "const:408:8"
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
      "definition_site": "00b42cac",
      "incomplete_value": true,
      "site": "00b42cb8",
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
                "const:468:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b42c10",
      "incomplete_value": true,
      "site": "00b42c1c",
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
                "const:368:8"
              ]
            ]
          ]
        ]
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
      "00b42c8c",
      "READ",
      [
        "storage",
        "01125400",
        null,
        "undefined8"
      ]
    ],
    [
      "00b42ca8",
      "READ",
      [
        "storage",
        "01125408",
        null,
        "undefined8"
      ]
    ],
    [
      "00b42cac",
      "READ",
      [
        "storage",
        "01125368",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b42c8c",
      "READ",
      [
        "storage",
        "01125500",
        null,
        "undefined8"
      ]
    ],
    [
      "00b42ca8",
      "READ",
      [
        "storage",
        "01125508",
        null,
        "undefined8"
      ]
    ],
    [
      "00b42cac",
      "READ",
      [
        "storage",
        "01125468",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b42c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b42be0.md#insn-00b42c1c) · [`00b42bf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b42be0.md#insn-00b42bf0) · [`00b42c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b42be0.md#insn-00b42c00)
- 新版 [`00b42cb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42c7c.md#insn-00b42cb8) · [`00b42c8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42c7c.md#insn-00b42c8c) · [`00b42c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42c7c.md#insn-00b42c9c)

~~~diff
- 00b42c1c ["INT_ADD", "register:40f0:8", ["const:b42c1c:8", "const:4:8"]]
- 00b42c1c ["CALL", null, ["callee:00574d2c:8"]]
+ 00b42cb8 ["INT_ADD", "register:40f0:8", ["const:b42cb8:8", "const:4:8"]]
+ 00b42cb8 ["CALL", null, ["callee:00574d2c:8"]]
- 00b42c1c bytes 34c8e897
+ 00b42cb8 bytes 1dc8e897
- 00b42bf0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:400:8"]]
- 00b42bf0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b42c8c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:500:8"]]
+ 00b42c8c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b42bf0 bytes 080142f9
+ 00b42c8c bytes 088142f9
- 00b42c00 ["INT_ADD", "register:40f0:8", ["const:b42c00:8", "const:4:8"]]
- 00b42c00 ["CALL", null, ["callee:00c5b150:8"]]
+ 00b42c9c ["INT_ADD", "register:40f0:8", ["const:b42c9c:8", "const:4:8"]]
+ 00b42c9c ["CALL", null, ["callee:00c5b150:8"]]
- 00b42c00 bytes 20610494
+ 00b42c9c bytes 2d610494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45f9307521c9772c338abb0d81677108"></a>

### [`00b42c44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b42c44.md) → [`00b42ce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42ce0.md) _ZN8firebase9analytics18ResetAnalyticsDataEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 86.36% / 新版 86.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b42cf4",
      "incomplete_value": true,
      "site": "00b42cf4",
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
      "definition_site": "00b42c58",
      "incomplete_value": true,
      "site": "00b42c58",
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
      "definition_site": "00b42d04",
      "incomplete_value": true,
      "site": "00b42d10",
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
                "const:508:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b42c68",
      "incomplete_value": true,
      "site": "00b42c74",
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
                "const:408:8"
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
      "definition_site": "00b42d08",
      "incomplete_value": true,
      "site": "00b42d10",
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
                "const:470:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b42c6c",
      "incomplete_value": true,
      "site": "00b42c74",
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
                "const:370:8"
              ]
            ]
          ]
        ]
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
      "00b42cf0",
      "READ",
      [
        "storage",
        "01125400",
        null,
        "undefined8"
      ]
    ],
    [
      "00b42d04",
      "READ",
      [
        "storage",
        "01125408",
        null,
        "undefined8"
      ]
    ],
    [
      "00b42d08",
      "READ",
      [
        "storage",
        "01125370",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b42cf0",
      "READ",
      [
        "storage",
        "01125500",
        null,
        "undefined8"
      ]
    ],
    [
      "00b42d04",
      "READ",
      [
        "storage",
        "01125508",
        null,
        "undefined8"
      ]
    ],
    [
      "00b42d08",
      "READ",
      [
        "storage",
        "01125470",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b42c74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b42c44.md#insn-00b42c74) · [`00b42c54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b42c44.md#insn-00b42c54) · [`00b42c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b42c44.md#insn-00b42c5c)
- 新版 [`00b42d10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42ce0.md#insn-00b42d10) · [`00b42cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42ce0.md#insn-00b42cf0) · [`00b42cf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42ce0.md#insn-00b42cf8)

~~~diff
- 00b42c74 ["INT_ADD", "register:40f0:8", ["const:b42c74:8", "const:4:8"]]
- 00b42c74 ["CALL", null, ["callee:00574d2c:8"]]
+ 00b42d10 ["INT_ADD", "register:40f0:8", ["const:b42d10:8", "const:4:8"]]
+ 00b42d10 ["CALL", null, ["callee:00574d2c:8"]]
- 00b42c74 bytes 1ec8e897
+ 00b42d10 bytes 07c8e897
- 00b42c54 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:400:8"]]
- 00b42c54 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b42cf0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:500:8"]]
+ 00b42cf0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00b42c54 bytes 000142f9
+ 00b42cf0 bytes 008142f9
- 00b42c5c ["INT_ADD", "register:40f0:8", ["const:b42c5c:8", "const:4:8"]]
- 00b42c5c ["CALL", null, ["callee:00c5b150:8"]]
+ 00b42cf8 ["INT_ADD", "register:40f0:8", ["const:b42cf8:8", "const:4:8"]]
+ 00b42cf8 ["CALL", null, ["callee:00c5b150:8"]]
- 00b42c5c bytes 09610494
+ 00b42cf8 bytes 16610494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00bd70299e59b202597cee60f8f89afe"></a>

### [`00b42cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b42cb0.md) → [`00b42d4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42d4c.md) _ZN8firebase9analytics22GetAnalyticsInstanceIdEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 17件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00b4358c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b4358c.md) [`00b43fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43fb8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 17件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00b43628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b43628.md) [`00b44054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44054.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 94.92% / 新版 94.92%

CFGの説明率　旧版 26.32% / 新版 26.32%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_branch_alignment` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_condition` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b42d7c",
      "incomplete_value": true,
      "site": "00b42d7c",
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
      "definition_site": "00b42ce0",
      "incomplete_value": true,
      "site": "00b42ce0",
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
      "site": "00b42da4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b42e40"
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
      "00b42d78",
      "READ",
      [
        "storage",
        "01125400",
        null,
        "undefined8"
      ]
    ],
    [
      "00b42da4",
      "READ",
      [
        "storage",
        "00c9b6b8",
        null,
        "pointer"
      ]
    ],
    [
      "00b42da4",
      "PARAM",
      [
        "storage",
        "00b43fb8",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEvPv",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b42d78",
      "READ",
      [
        "storage",
        "01125500",
        null,
        "undefined8"
      ]
    ],
    [
      "00b42da4",
      "READ",
      [
        "storage",
        "00c9b788",
        null,
        "pointer"
      ]
    ],
    [
      "00b42da4",
      "PARAM",
      [
        "storage",
        "00b44054",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEvPv",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b42d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b42cb0.md#insn-00b42d08) · [`00b42d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b42cb0.md#insn-00b42d1c) · [`00b42d54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b42cb0.md#insn-00b42d54)
- 新版 [`00b42da4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42d4c.md#insn-00b42da4) · [`00b42db8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42d4c.md#insn-00b42db8) · [`00b42df0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42d4c.md#insn-00b42df0)

~~~diff
- 00b42d08 ["INT_ADD", "tmp:0:8", ["register:4018:8", "const:6b8:8"]]
- 00b42d08 ["LOAD", "register:4018:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b42da4 ["INT_ADD", "tmp:0:8", ["register:4018:8", "const:788:8"]]
+ 00b42da4 ["LOAD", "register:4018:8", ["const:1b1:8", "tmp:0:8"]]
- 00b42d08 bytes 635c43f9
+ 00b42da4 bytes 63c443f9
- 00b42d1c ["INT_ADD", "register:40f0:8", ["const:b42d1c:8", "const:4:8"]]
- 00b42d1c ["CALL", null, ["callee:00c5af10:8"]]
+ 00b42db8 ["INT_ADD", "register:40f0:8", ["const:b42db8:8", "const:4:8"]]
+ 00b42db8 ["CALL", null, ["callee:00c5af10:8"]]
- 00b42d1c bytes 49600494
+ 00b42db8 bytes 56600494
- 00b42d54 ["INT_ADD", "register:40f0:8", ["const:b42d54:8", "const:4:8"]]
- 00b42d54 ["CALL", null, ["callee:00497874:8"]]
+ 00b42df0 ["INT_ADD", "register:40f0:8", ["const:b42df0:8", "const:4:8"]]
+ 00b42df0 ["CALL", null, ["callee:00497874:8"]]
- 00b42d54 bytes b852e597
+ 00b42df0 bytes a152e597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac507ed2b02f3a80db99ca4da09ca7cd"></a>

### [`00b42f04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b42f04.md) → [`00b42fa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42fa0.md) _ZN8firebase9analytics32GetAnalyticsInstanceIdLastResultEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b050.md) · 呼出先 8件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5abe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abe0.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5acb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5acb0.md)
- 新版 呼出元 1件 [`00c5b120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b120.md) · 呼出先 8件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5acb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5acb0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ad80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad80.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_condition` 2件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b42f20"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b42fbc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b42f44",
      "incomplete_value": true,
      "site": "00b42f4c",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
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
      "00b42fb4",
      "READ",
      [
        "storage",
        "01125400",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b42f20",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4300c"
      ]
    ],
    [
      "unmatched:00b42f74",
      "PARAM",
      [
        "storage",
        "002a2915",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b42fb4",
      "READ",
      [
        "storage",
        "01125500",
        null,
        "undefined8"
      ]
    ],
    [
      "00b42fbc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4300c"
      ]
    ],
    [
      "00b43010",
      "PARAM",
      [
        "storage",
        "002a28c8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b42f20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b42f04.md#insn-00b42f20) · [`00b42f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b42f04.md#insn-00b42f4c) · [`00b42f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b42f04.md#insn-00b42f78)
- 新版 [`00b42fe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42fa0.md#insn-00b42fe8) · [`00b43014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42fa0.md#insn-00b43014)

~~~diff
- 00b42f20 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00b42f20 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b42f20 bytes 890200b4
- 00b42f4c ["INT_ADD", "register:40f0:8", ["const:b42f4c:8", "const:4:8"]]
- 00b42f4c ["CALL", null, ["callee:00c5ad40:8"]]
+ 00b42fe8 ["INT_ADD", "register:40f0:8", ["const:b42fe8:8", "const:4:8"]]
+ 00b42fe8 ["CALL", null, ["callee:00c5ad40:8"]]
- 00b42f4c bytes 495f0494
+ 00b42fe8 bytes 565f0494
- 00b42f78 ["INT_ADD", "register:40f0:8", ["const:b42f78:8", "const:4:8"]]
- 00b42f78 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b43014 ["INT_ADD", "register:40f0:8", ["const:b43014:8", "const:4:8"]]
+ 00b43014 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b42f78 bytes 22600494
+ 00b43014 bytes 2f600494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d649e66e7ec0ef3743afdf5e46100b6"></a>

### [`00b42fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b42fd8.md) → [`00b43074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b43074.md) _ZN8firebase6FutureINSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHand

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5adb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5adb0.md) · 呼出先 3件 [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5adf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5adf0.md) [`00c5ae00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae00.md)
- 新版 呼出元 1件 [`00c5ae80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae80.md) · 呼出先 3件 [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5aec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aec0.md) [`00c5aed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aed0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 74.19% / 新版 74.19%

CFGの説明率　旧版 12.50% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b42fd8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b42fdc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b42fdc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b42fd8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b42fdc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b42fe0",
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
      "00b43074",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b43078",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b4307c",
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

- 旧版 [`00b42fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b42fd8.md#insn-00b42fd8) · [`00b42fdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b42fd8.md#insn-00b42fdc) · [`00b42fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b42fd8.md#insn-00b42fe0)

~~~diff
- 00b42fd8 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b42fd8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b42fd8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b42fd8 bytes f50f1df8
- 00b42fdc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b42fdc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b42fdc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b42fdc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b42fdc bytes f44f01a9
- 00b42fe0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b42fe0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b42fe0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b42fe0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b42fe0 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0728642eb5ea625bd4776a93e0563c54"></a>

### [`00b43078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43078.md) → [`00b43114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b43114.md) _ZN8firebase9analytics12GetSessionIdEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 19件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00b43af0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43af0.md) [`00b43ff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43ff0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 19件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00b43b8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b43b8c.md) [`00b4408c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b4408c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 81.42% / 新版 81.42%

CFGの説明率　旧版 5.88% / 新版 4.76%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `store_condition` 1件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b430a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b43130"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b43144"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b430a4",
      "READ",
      [
        "storage",
        "01125400",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b430a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4321c"
      ]
    ],
    [
      "00b4315c",
      "READ",
      [
        "storage",
        "00c9b6c0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b43140",
      "READ",
      [
        "storage",
        "01125500",
        null,
        "undefined8"
      ]
    ],
    [
      "00b43144",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4321c"
      ]
    ],
    [
      "00b4315c",
      "READ",
      [
        "storage",
        "00c9b790",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b430a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43078.md#insn-00b430a8) · [`00b430d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43078.md#insn-00b430d4) · [`00b430f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43078.md#insn-00b430f0)
- 新版 [`00b43170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b43114.md#insn-00b43170)

~~~diff
- 00b430a8 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00b430a8 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b430a8 bytes c90600b4
- 00b430d4 ["INT_ADD", "register:40f0:8", ["const:b430d4:8", "const:4:8"]]
- 00b430d4 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b43170 ["INT_ADD", "register:40f0:8", ["const:b43170:8", "const:4:8"]]
+ 00b43170 ["CALL", null, ["callee:00c5af10:8"]]
- 00b430d4 bytes 5b5f0494
+ 00b43170 bytes 685f0494
- 00b430f0 ["INT_ADD", "register:40f0:8", ["const:b430f0:8", "const:4:8"]]
- 00b430f0 ["CALL", null, ["callee:00c5b150:8"]]
- 00b430f0 bytes e45f0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b564e93c2fc39ccd45b1ef8cb340095"></a>

### [`00b43340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43340.md) → [`00b433dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b433dc.md) _ZN8firebase9analytics22GetSessionIdLastResultEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 8件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5abe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abe0.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5acb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5acb0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5acb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5acb0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ad80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b43340"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b43340"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b43344"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b43340",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b43344",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b43348",
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
      "00b433dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b433e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b433e4",
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

- 旧版 [`00b43340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43340.md#insn-00b43340) · [`00b43344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43340.md#insn-00b43344) · [`00b43348`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43340.md#insn-00b43348)

~~~diff
- 00b43340 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b43340 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b43340 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b43340 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b43340 bytes f657bda9
- 00b43344 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b43344 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b43344 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b43344 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b43344 bytes f44f01a9
- 00b43348 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b43348 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b43348 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b43348 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b43348 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ca0593ea8f00525f450296e7a73b809"></a>

### [`00b43418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43418.md) → [`00b434b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b434b4.md) _ZN8firebase10FutureBaseaSERKS0_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) · 呼出先 6件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5ae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)
- 新版 呼出元 1件 [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md) · 呼出先 6件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md) [`00c5aee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aee0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 84.06% / 新版 84.06%

CFGの説明率　旧版 14.29% / 新版 14.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4343c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b434d8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b43458"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4343c",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b43458",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ],
    [
      "unmatched:00b4346c",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b434d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00b434f4",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ],
    [
      "00b43508",
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

- 旧版 [`00b4343c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43418.md#insn-00b4343c) · [`00b43458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43418.md#insn-00b43458) · [`00b4346c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43418.md#insn-00b4346c)

~~~diff
- 00b4343c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00b4343c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b4343c bytes e80f00f9
- 00b43458 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b43458 ["INT_ADD", "register:40f0:8", ["const:b43458:8", "const:4:8"]]
- 00b43458 ["CALLIND", null, ["register:0:8"]]
- 00b43458 bytes 00013fd6
- 00b4346c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4346c ["INT_ADD", "register:40f0:8", ["const:b4346c:8", "const:4:8"]]
- 00b4346c ["CALLIND", null, ["register:0:8"]]
- 00b4346c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60fddaedfcf18935c0152fbcb8567473"></a>

### [`00b4358c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b4358c.md) → [`00b43628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b43628.md) FUN_00b43628

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b42cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b42cb0.md) · 呼出先 12件 [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`00b42d4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42d4c.md) · 呼出先 12件 [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 87.60% / 新版 87.60%

CFGの説明率　旧版 20.00% / 新版 20.45%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 4件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b435a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b435a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b43660"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b435a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b43660",
      "WRITE",
      [
        "storage",
        "Stack[-0x80]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b43674",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b437f8"
      ]
    ]
  ],
  "added": [
    [
      "00b43640",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b436fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x80]",
        null,
        null
      ]
    ],
    [
      "00b43710",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b437f8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b435a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b4358c.md#insn-00b435a4) · [`00b43610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b4358c.md#insn-00b43610) · [`00b4361c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b4358c.md#insn-00b4361c)

~~~diff
- 00b435a4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b435a4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b435a4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:a0:8"]]
- 00b435a4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b435a4 bytes fd7b0aa9
- 00b43610 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b43610 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b43610 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b43610 ["COPY", "register:4040:8", ["tmp:0:8"]]
- 00b43610 bytes 0801969a
- 00b4361c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b4361c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00b4361c ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b4361c ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00b4361c bytes 3611889a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da437516363b27779cfeb553e00b17f3"></a>

### [`00b437b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b437b0.md) → [`00b4384c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b4384c.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEZNS0_26Complet

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5ad60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad60.md) · 呼出先 11件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ae30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae30.md) [`00c5ae50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae50.md) [`00c5ae60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae60.md)
- 新版 呼出元 1件 [`00c5ae30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae30.md) · 呼出先 11件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5af00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af00.md) [`00c5af20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af20.md) [`00c5af30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af30.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 28.57% / 新版 26.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b437c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b437c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4385c"
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
      "unmatched:00b437c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b43814",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b438c0"
      ]
    ],
    [
      "unmatched:00b4381c",
      "PARAM",
      [
        "storage",
        "002a70e4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4385c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b438b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b438c0"
      ]
    ],
    [
      "00b438b8",
      "PARAM",
      [
        "storage",
        "002a7088",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b437c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b437b0.md#insn-00b437c0) · [`00b4380c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b437b0.md#insn-00b4380c) · [`00b43814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b437b0.md#insn-00b43814)

~~~diff
- 00b437c0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b437c0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b437c0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b437c0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b437c0 bytes fd7b04a9
- 00b4380c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4380c ["INT_ADD", "register:40f0:8", ["const:b4380c:8", "const:4:8"]]
- 00b4380c ["CALLIND", null, ["register:0:8"]]
- 00b4380c bytes 00013fd6
- 00b43814 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 00b43814 bytes 80000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e96940cee5154b8e958a9c062827cebb"></a>

### [`00b438f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b438f0.md) → [`00b4398c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b4398c.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0b0.md) · 呼出先 2件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c5b0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0a0.md)
- 新版 呼出元 1件 [`00c5b180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b180.md) · 呼出先 2件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c5b170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b170.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 94.00% / 新版 94.00%

CFGの説明率　旧版 29.63% / 新版 29.63%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4391c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b439b8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b43960",
      "incomplete_value": true,
      "site": "00b43964",
      "value": [
        "live",
        "register:40a0:8"
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
      "unmatched:00b4391c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b439e0"
      ]
    ]
  ],
  "added": [
    [
      "00b439b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b439e0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4391c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b438f0.md#insn-00b4391c) · [`00b43964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b438f0.md#insn-00b43964) · [`00b439b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b438f0.md#insn-00b439b4)
- 新版 [`00b43a00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b4398c.md#insn-00b43a00)

~~~diff
- 00b4391c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b4391c ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00b4391c bytes 43010054
- 00b43964 ["INT_ADD", "register:40f0:8", ["const:b43964:8", "const:4:8"]]
- 00b43964 ["CALL", null, ["callee:00c58010:8"]]
+ 00b43a00 ["INT_ADD", "register:40f0:8", ["const:b43a00:8", "const:4:8"]]
+ 00b43a00 ["CALL", null, ["callee:00c58010:8"]]
- 00b43964 bytes 77510494
+ 00b43a00 bytes 84510494
- 00b439b4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b439b4 ["RETURN", null, ["register:0:8"]]
- 00b439b4 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dfe264c1edfbe473c6c9d0ccaefa8ff7"></a>

### [`00b439b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b439b8.md) → [`00b43a54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b43a54.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE21__grow_by_and_replaceEmmmmmmPKc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0a0.md) · 呼出先 4件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5b090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b090.md)
- 新版 呼出元 1件 [`00c5b170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b170.md) · 呼出先 4件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5b160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b160.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 89.74% / 新版 89.74%

CFGの説明率　旧版 44.44% / 新版 41.38%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b43adc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b43b78"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b43a90"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b43a90",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b43b44"
      ]
    ]
  ],
  "added": [
    [
      "00b43b2c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b43b44"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b43a40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b439b8.md#insn-00b43a40) · [`00b43a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b439b8.md#insn-00b43a48) · [`00b43a84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b439b8.md#insn-00b43a84)
- 新版 [`00b43adc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b43a54.md#insn-00b43adc) · [`00b43ae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b43a54.md#insn-00b43ae4) · [`00b43b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b43a54.md#insn-00b43b20)

~~~diff
- 00b43a40 ["BRANCH", null, ["local:b9:8"]]
+ 00b43adc ["BRANCH", null, ["local:b11:8"]]
- 00b43a40 bytes 05000014
+ 00b43adc bytes 05000014
- 00b43a48 ["BRANCH", null, ["local:b9:8"]]
+ 00b43ae4 ["BRANCH", null, ["local:b11:8"]]
- 00b43a48 bytes 03000014
+ 00b43ae4 bytes 03000014
- 00b43a84 ["INT_ADD", "register:40f0:8", ["const:b43a84:8", "const:4:8"]]
- 00b43a84 ["CALL", null, ["callee:00c580d0:8"]]
+ 00b43b20 ["INT_ADD", "register:40f0:8", ["const:b43b20:8", "const:4:8"]]
+ 00b43b20 ["CALL", null, ["callee:00c580d0:8"]]
- 00b43a84 bytes 5f510494
+ 00b43b20 bytes 6c510494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e5fb0410ae6b2390abeaca0100d9950"></a>

### [`00b43af0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43af0.md) → [`00b43b8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b43b8c.md) FUN_00b43b8c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b43078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43078.md) · 呼出先 9件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5abe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abe0.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5acb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5acb0.md)
- 新版 呼出元 1件 [`00b43114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b43114.md) · 呼出先 9件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md) [`00c5acb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5acb0.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5ad80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 91.86% / 新版 91.86%

CFGの説明率　旧版 47.83% / 新版 47.83%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b43b58"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b43bf4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b43bfc",
      "incomplete_value": true,
      "site": "00b43c0c",
      "value": [
        "live",
        "register:8:8"
      ]
    },
    "old": null,
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
      "unmatched:00b43b58",
      "PARAM",
      [
        "storage",
        "002a19b6",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b43b78",
      "PARAM",
      [
        "storage",
        "002aa711",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b43bac",
      "PARAM",
      [
        "storage",
        "002a63ea",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b43bf4",
      "PARAM",
      [
        "storage",
        "002a1969",
        null,
        "string"
      ]
    ],
    [
      "00b43c14",
      "PARAM",
      [
        "storage",
        "002aa6b5",
        null,
        "string"
      ]
    ],
    [
      "00b43c48",
      "PARAM",
      [
        "storage",
        "002a638e",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b43b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43af0.md#insn-00b43b58) · [`00b43b70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43af0.md#insn-00b43b70) · [`00b43b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43af0.md#insn-00b43b80)
- 新版 [`00b43c0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b43b8c.md#insn-00b43c0c) · [`00b43c1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b43b8c.md#insn-00b43c1c)

~~~diff
- 00b43b58 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b43b58 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b43b58 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b43b58 ["COPY", "register:4018:8", ["tmp:0:8"]]
- 00b43b58 bytes 0301969a
- 00b43b70 ["INT_ADD", "register:40f0:8", ["const:b43b70:8", "const:4:8"]]
- 00b43b70 ["CALL", null, ["callee:00c5ae40:8"]]
+ 00b43c0c ["INT_ADD", "register:40f0:8", ["const:b43c0c:8", "const:4:8"]]
+ 00b43c0c ["CALL", null, ["callee:00c5ae40:8"]]
- 00b43b70 bytes 805c0494
+ 00b43c0c bytes 8d5c0494
- 00b43b80 ["INT_ADD", "register:40f0:8", ["const:b43b80:8", "const:4:8"]]
- 00b43b80 ["CALL", null, ["callee:00c5ad70:8"]]
+ 00b43c1c ["INT_ADD", "register:40f0:8", ["const:b43c1c:8", "const:4:8"]]
+ 00b43c1c ["CALL", null, ["callee:00c5ad70:8"]]
- 00b43b80 bytes 485c0494
+ 00b43c1c bytes 555c0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7fa24e0f812c834d617e4a4d2a1b9629"></a>

### [`00b43c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43c68.md) → [`00b43d04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b43d04.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalImZNS0_26CompleteWithResultInternalImEEvRKNS_12FutureHandleEiPKcRKT_EUlPmE_EEvS5_i

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5ad90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad90.md) · 呼出先 10件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ae30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae30.md) [`00c5ae50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae50.md) [`00c5ae60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae60.md)
- 新版 呼出元 1件 [`00c5ae60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae60.md) · 呼出先 10件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5af00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af00.md) [`00c5af20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af20.md) [`00c5af30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 87.67% / 新版 87.67%

CFGの説明率　旧版 7.14% / 新版 9.09%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b43d24",
      "incomplete_value": true,
      "site": "00b43d38",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b43d70",
      "incomplete_value": false,
      "site": "00b43d74",
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
            "const:88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b43cd4",
      "incomplete_value": false,
      "site": "00b43cd8",
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
            "const:e4:8"
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
      "definition_site": "00b43cdc",
      "incomplete_value": true,
      "site": "00b43cec",
      "value": [
        "live",
        "register:4098:8"
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
      "00b43d48",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b43d58"
      ]
    ],
    [
      "unmatched:00b43cd4",
      "PARAM",
      [
        "storage",
        "002a70e4",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b43d48",
      "READ",
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
      "00b43d48",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b43df4"
      ]
    ],
    [
      "00b43d70",
      "PARAM",
      [
        "storage",
        "002a7088",
        null,
        "string"
      ]
    ],
    [
      "00b43de4",
      "READ",
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

- 旧版 [`00b43c9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43c68.md#insn-00b43c9c) · [`00b43cd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43c68.md#insn-00b43cd8) · [`00b43cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43c68.md#insn-00b43cec)
- 新版 [`00b43d38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b43d04.md#insn-00b43d38) · [`00b43d74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b43d04.md#insn-00b43d74) · [`00b43d88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b43d04.md#insn-00b43d88)

~~~diff
- 00b43c9c ["INT_ADD", "register:40f0:8", ["const:b43c9c:8", "const:4:8"]]
- 00b43c9c ["CALL", null, ["callee:00c5aad0:8"]]
+ 00b43d38 ["INT_ADD", "register:40f0:8", ["const:b43d38:8", "const:4:8"]]
+ 00b43d38 ["CALL", null, ["callee:00c5aad0:8"]]
- 00b43c9c bytes 595b0494
+ 00b43d38 bytes 665b0494
- 00b43cd8 ["INT_ADD", "register:40f0:8", ["const:b43cd8:8", "const:4:8"]]
- 00b43cd8 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b43d74 ["INT_ADD", "register:40f0:8", ["const:b43d74:8", "const:4:8"]]
+ 00b43d74 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b43cd8 bytes ca5c0494
+ 00b43d74 bytes d75c0494
- 00b43cec ["INT_ADD", "register:40f0:8", ["const:b43cec:8", "const:4:8"]]
- 00b43cec ["CALL", null, ["callee:00c5af40:8"]]
+ 00b43d88 ["INT_ADD", "register:40f0:8", ["const:b43d88:8", "const:4:8"]]
+ 00b43d88 ["CALL", null, ["callee:00c5af40:8"]]
- 00b43cec bytes 615c0494
+ 00b43d88 bytes 6e5c0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05bd087e2e60aa910121b69f80ae89a6"></a>

### [`00b43d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43d8c.md) → [`00b43e28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b43e28.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIiZNS0_26CompleteWithResultInternalIiEEvRKNS_12FutureHandleEiPKcRKT_EUlPiE_EEvS5_i

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5ad70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad70.md) · 呼出先 10件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ae30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae30.md) [`00c5ae50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae50.md) [`00c5ae60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae60.md)
- 新版 呼出元 1件 [`00c5ae40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae40.md) · 呼出先 10件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5af00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af00.md) [`00c5af20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af20.md) [`00c5af30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 91.78% / 新版 91.78%

CFGの説明率　旧版 20.00% / 新版 18.18%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b43df8",
      "incomplete_value": false,
      "site": "00b43dfc",
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
            "const:e4:8"
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
      "definition_site": "00b43e00",
      "incomplete_value": true,
      "site": "00b43e10",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b43e2c",
      "incomplete_value": true,
      "site": "00b43e30",
      "value": [
        "live",
        "register:4098:8"
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
      "unmatched:00b43df8",
      "PARAM",
      [
        "storage",
        "002a70e4",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b43e6c",
      "READ",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b43e70",
      "READ",
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
      "00b43e94",
      "PARAM",
      [
        "storage",
        "002a7088",
        null,
        "string"
      ]
    ],
    [
      "00b43f08",
      "READ",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b43f0c",
      "READ",
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

- 旧版 [`00b43dfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43d8c.md#insn-00b43dfc) · [`00b43e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43d8c.md#insn-00b43e10) · [`00b43e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43d8c.md#insn-00b43e30)
- 新版 [`00b43e98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b43e28.md#insn-00b43e98) · [`00b43eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b43e28.md#insn-00b43eac) · [`00b43ecc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b43e28.md#insn-00b43ecc)

~~~diff
- 00b43dfc ["INT_ADD", "register:40f0:8", ["const:b43dfc:8", "const:4:8"]]
- 00b43dfc ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b43e98 ["INT_ADD", "register:40f0:8", ["const:b43e98:8", "const:4:8"]]
+ 00b43e98 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b43dfc bytes 815c0494
+ 00b43e98 bytes 8e5c0494
- 00b43e10 ["INT_ADD", "register:40f0:8", ["const:b43e10:8", "const:4:8"]]
- 00b43e10 ["CALL", null, ["callee:00c5af40:8"]]
+ 00b43eac ["INT_ADD", "register:40f0:8", ["const:b43eac:8", "const:4:8"]]
+ 00b43eac ["CALL", null, ["callee:00c5af40:8"]]
- 00b43e10 bytes 185c0494
+ 00b43eac bytes 255c0494
- 00b43e30 ["INT_ADD", "register:40f0:8", ["const:b43e30:8", "const:4:8"]]
- 00b43e30 ["CALL", null, ["callee:00c5af30:8"]]
+ 00b43ecc ["INT_ADD", "register:40f0:8", ["const:b43ecc:8", "const:4:8"]]
+ 00b43ecc ["CALL", null, ["callee:00c5af30:8"]]
- 00b43e30 bytes 0c5c0494
+ 00b43ecc bytes 195c0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b0cd3e3d70a4e6c5d5492e03f3575b1"></a>

### [`00b43eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43eb0.md) → [`00b43f4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b43f4c.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalIvEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS5_iS7_RKT0_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5ada0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ada0.md) · 呼出先 10件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ae30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae30.md) [`00c5ae50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae50.md) [`00c5ae60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae60.md)
- 新版 呼出元 1件 [`00c5ae70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae70.md) · 呼出先 10件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5af00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af00.md) [`00c5af20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af20.md) [`00c5af30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.97% / 新版 96.97%

CFGの説明率　旧版 85.71% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b43fb0",
      "incomplete_value": false,
      "site": "00b43fb4",
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
            "const:88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b43f14",
      "incomplete_value": false,
      "site": "00b43f18",
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
            "const:e4:8"
          ]
        ]
      ]
    },
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
      "00b43fb0",
      "PARAM",
      [
        "storage",
        "002a70e4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b43fb0",
      "PARAM",
      [
        "storage",
        "002a7088",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b43f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43eb0.md#insn-00b43f18) · [`00b43edc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43eb0.md#insn-00b43edc) · [`00b43ee8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43eb0.md#insn-00b43ee8)
- 新版 [`00b43fb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b43f4c.md#insn-00b43fb4) · [`00b43f78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b43f4c.md#insn-00b43f78) · [`00b43f84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b43/00b43f4c.md#insn-00b43f84)

~~~diff
- 00b43f18 ["INT_ADD", "register:40f0:8", ["const:b43f18:8", "const:4:8"]]
- 00b43f18 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b43fb4 ["INT_ADD", "register:40f0:8", ["const:b43fb4:8", "const:4:8"]]
+ 00b43fb4 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b43f18 bytes 3a5c0494
+ 00b43fb4 bytes 475c0494
- 00b43edc ["INT_ADD", "register:40f0:8", ["const:b43edc:8", "const:4:8"]]
- 00b43edc ["CALL", null, ["callee:00c5aad0:8"]]
+ 00b43f78 ["INT_ADD", "register:40f0:8", ["const:b43f78:8", "const:4:8"]]
+ 00b43f78 ["CALL", null, ["callee:00c5aad0:8"]]
- 00b43edc bytes c95a0494
+ 00b43f78 bytes d65a0494
- 00b43ee8 ["INT_ADD", "register:40f0:8", ["const:b43ee8:8", "const:4:8"]]
- 00b43ee8 ["CALL", null, ["callee:00c5af50:8"]]
+ 00b43f84 ["INT_ADD", "register:40f0:8", ["const:b43f84:8", "const:4:8"]]
+ 00b43f84 ["CALL", null, ["callee:00c5af50:8"]]
- 00b43ee8 bytes e65b0494
+ 00b43f84 bytes f35b0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5af8420ceda8ed22aa40f540fc94649a"></a>

### [`00b43fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43fb8.md) → [`00b44054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44054.md) _ZN8firebase26ReferenceCountedFutureImpl7DeleteTINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEvPv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 3件 [`00b42cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b42/00b42cb0.md) [`00bbc7d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbc7d8.md) [`00bde818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bde/00bde818.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`00b42d4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b42/00b42d4c.md) [`00bbc874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbc874.md) [`00bde8b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bde/00bde8b4.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 33.33% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b43fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43fb8.md#insn-00b43fb8) · [`00b43fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43fb8.md#insn-00b43fd0) · [`00b43fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43fb8.md#insn-00b43fd8)
- 新版 [`00b44054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44054.md#insn-00b44054) · [`00b4406c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44054.md#insn-00b4406c) · [`00b44074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44054.md#insn-00b44074)

~~~diff
- 00b43fb8 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00b43fb8 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00b44054 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00b44054 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b43fb8 bytes a00100b4
+ 00b44054 bytes a00100b4
- 00b43fd0 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00b43fd0 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b43fd0 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b43fd0 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
+ 00b4406c ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
+ 00b4406c ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00b4406c ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00b4406c ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 00b43fd0 bytes 68000036
+ 00b4406c bytes 68000036
- 00b43fd8 ["INT_ADD", "register:40f0:8", ["const:b43fd8:8", "const:4:8"]]
- 00b43fd8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00b44074 ["INT_ADD", "register:40f0:8", ["const:b44074:8", "const:4:8"]]
+ 00b44074 ["CALL", null, ["callee:00c57f80:8"]]
- 00b43fd8 bytes b64f0494
+ 00b44074 bytes c34f0494
~~~


<a id="compare-ec42da4deafd2df8a05b0e8fa76feaab"></a>

### [`00b43ffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43ffc.md) → [`00b44098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44098.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIlZNS0_26CompleteWithResultInternalIlEEvRKNS_12FutureHandleEiPKcRKT_EUlPlE_EEvS5_i

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5ad80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad80.md) · 呼出先 10件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ae30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae30.md) [`00c5ae50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae50.md) [`00c5ae60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae60.md)
- 新版 呼出元 1件 [`00c5ae50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae50.md) · 呼出先 10件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5af00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af00.md) [`00c5af20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af20.md) [`00c5af30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af30.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 73.97% / 新版 73.97%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b43ffc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b44000"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b44000"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b43ffc",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b44000",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b44004",
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
      "00b44098",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b4409c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b440a0",
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

- 旧版 [`00b43ffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43ffc.md#insn-00b43ffc) · [`00b44000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43ffc.md#insn-00b44000) · [`00b44004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43ffc.md#insn-00b44004)

~~~diff
- 00b43ffc ["COPY", "tmp:0:8", ["register:40c8:8"]]
- 00b43ffc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 00b43ffc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b43ffc bytes f90f1bf8
- 00b44000 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b44000 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b44000 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b44000 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b44000 bytes f85f01a9
- 00b44004 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b44004 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b44004 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b44004 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b44004 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9e2e24cffb4c83d631e6c121a85299f"></a>

### [`00b44150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44150.md) → [`00b441ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b441ec.md) _ZN8firebase23LogMessageWithCallbackVENS_8LogLevelEPKcSt9__va_list

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b120.md) · 呼出先 8件 [`00b44120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44120.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)
- 新版 呼出元 1件 [`00c5b1f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b1f0.md) · 呼出先 8件 [`00b441bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b441bc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 62.30% / 新版 62.30%

CFGの説明率　旧版 7.69% / 新版 8.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 3件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4417c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b44218"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4418c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4417c",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b44180",
      "READ",
      [
        "storage",
        "00c9b6d8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b44188",
      "READ",
      [
        "storage",
        "01125418",
        "_ZN8firebase11g_log_mutexE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b44218",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00b4421c",
      "READ",
      [
        "storage",
        "00c9b7a8",
        null,
        "pointer"
      ]
    ],
    [
      "00b44224",
      "READ",
      [
        "storage",
        "01125518",
        "_ZN8firebase11g_log_mutexE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4417c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44150.md#insn-00b4417c) · [`00b4418c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44150.md#insn-00b4418c) · [`00b441a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44150.md#insn-00b441a0)
- 新版 [`00b4423c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b441ec.md#insn-00b4423c)

~~~diff
- 00b4417c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 00b4417c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b4417c bytes e81700f9
- 00b4418c ["INT_NOTEQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 00b4418c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b4418c bytes f30000b5
- 00b441a0 ["INT_ADD", "register:40f0:8", ["const:b441a0:8", "const:4:8"]]
- 00b441a0 ["CALL", null, ["callee:00c5ad50:8"]]
+ 00b4423c ["INT_ADD", "register:40f0:8", ["const:b4423c:8", "const:4:8"]]
+ 00b4423c ["CALL", null, ["callee:00c5ad50:8"]]
- 00b441a0 bytes b85a0494
+ 00b4423c bytes c55a0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ea6cf3a2886500af1d94a584cfe6cd9"></a>

### [`00b44470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44470.md) → [`00b4450c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b4450c.md) _ZN8firebase8LogErrorEPKcz

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5b120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b120.md)
- 新版 呼出元 1件 [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) · 呼出先 2件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5b1f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b1f0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 90.24% / 新版 90.24%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b444e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b444e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b44584"
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
      "unmatched:00b444e8",
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
      "00b44584",
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

- 旧版 [`00b444e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44470.md#insn-00b444e8) · [`00b444ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44470.md#insn-00b444ec)
- 新版 [`00b44588`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b4450c.md#insn-00b44588) · [`00b44584`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b4450c.md#insn-00b44584)

~~~diff
- 00b444e8 ["INT_ADD", "tmp:0:8", ["register:40e8:8", "const:ffffffffffffffa0:8"]]
- 00b444e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5020:16"]]
- 00b444e8 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00b444e8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5000:16"]]
- 00b444e8 bytes a1033dad
- 00b444ec ["INT_ADD", "register:40f0:8", ["const:b444ec:8", "const:4:8"]]
- 00b444ec ["CALL", null, ["callee:00c5b1f0:8"]]
+ 00b44588 ["INT_ADD", "register:40f0:8", ["const:b44588:8", "const:4:8"]]
+ 00b44588 ["CALL", null, ["callee:00c5b1f0:8"]]
- 00b444ec bytes 0d5b0494
+ 00b44588 bytes 1a5b0494
+ 00b44584 ["INT_ADD", "tmp:0:8", ["register:40e8:8", "const:ffffffffffffffa0:8"]]
+ 00b44584 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5020:16"]]
+ 00b44584 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
+ 00b44584 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5000:16"]]
+ 00b44584 bytes a1033dad
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5fbdf6e2c0015f36f56892f49b19c8a9"></a>

### [`00b44514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44514.md) → [`00b445b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b445b0.md) _ZN8firebase9LogAssertEPKcz

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5b120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b120.md)
- 新版 呼出元 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) · 呼出先 2件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5b1f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b1f0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 80.49% / 新版 80.49%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b44518"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b44518"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4451c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b44518",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4451c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4458c",
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
      "00b445b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b445b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b44628",
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

- 旧版 [`00b44518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44514.md#insn-00b44518) · [`00b4451c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44514.md#insn-00b4451c) · [`00b4458c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44514.md#insn-00b4458c)

~~~diff
- 00b44518 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b44518 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b44518 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:110:8"]]
- 00b44518 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b44518 bytes fc4f11a9
- 00b4451c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b4451c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b4451c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:120:8"]]
- 00b4451c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4451c bytes fd7b12a9
- 00b4458c ["INT_ADD", "tmp:0:8", ["register:40e8:8", "const:ffffffffffffffa0:8"]]
- 00b4458c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5020:16"]]
- 00b4458c ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00b4458c ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5000:16"]]
- 00b4458c bytes a1033dad
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9699c5c1dac62b425b9f8da4106876c"></a>

### [`00b44678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44678.md) → [`00b44714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44714.md) _ZN8firebase14LogGetCallbackEPPv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00b44120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44120.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00b441bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b441bc.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b446a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b44740"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b44694"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b44724",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b44698"
      ]
    ],
    [
      "unmatched:00b44690",
      "PARAM",
      [
        "storage",
        "002abf7a",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b44694",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b0d0"
      ]
    ]
  ],
  "added": [
    [
      "00b44724",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b44734"
      ]
    ],
    [
      "00b4472c",
      "PARAM",
      [
        "storage",
        "002abf1e",
        null,
        "string"
      ]
    ],
    [
      "00b44730",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b0d0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b44694`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44678.md#insn-00b44694) · [`00b446a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44678.md#insn-00b446a4)
- 新版 [`00b44730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44714.md#insn-00b44730)

~~~diff
- 00b44694 ["INT_ADD", "register:40f0:8", ["const:b44694:8", "const:4:8"]]
- 00b44694 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b44694 bytes 5b5a0494
- 00b446a4 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b446a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b446a4 bytes 680200f9
+ 00b44730 ["INT_ADD", "register:40f0:8", ["const:b44730:8", "const:4:8"]]
+ 00b44730 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b44730 bytes 685a0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-347623b32c194c647bdf5ef3f876e913"></a>

### [`00b446c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b446c0.md) → [`00b4475c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b4475c.md) FUN_00b4475c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00b44120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44120.md) · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5b0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0e0.md)
- 新版 呼出元 1件 [`00b441bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b441bc.md) · 呼出先 2件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5b1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b1b0.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b446d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b446d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b446dc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b446d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x80]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b446dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x120]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b446e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x100]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b44774",
      "WRITE",
      [
        "storage",
        "Stack[-0x80]",
        null,
        null
      ]
    ],
    [
      "00b44778",
      "WRITE",
      [
        "storage",
        "Stack[-0x120]",
        null,
        null
      ]
    ],
    [
      "00b4477c",
      "WRITE",
      [
        "storage",
        "Stack[-0x100]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b446d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b446c0.md#insn-00b446d8) · [`00b446dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b446c0.md#insn-00b446dc) · [`00b446e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b446c0.md#insn-00b446e0)

~~~diff
- 00b446d8 ["COPY", "tmp:0:8", ["register:4030:8"]]
- 00b446d8 ["COPY", "tmp:1:8", ["register:4038:8"]]
- 00b446d8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:a0:8"]]
- 00b446d8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b446d8 bytes e61f0aa9
- 00b446dc ["COPY", "tmp:0:8", ["register:8:8"]]
- 00b446dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b446dc ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00b446dc ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5020:16"]]
- 00b446dc bytes e00700ad
- 00b446e0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00b446e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5040:16"]]
- 00b446e0 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00b446e0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5060:16"]]
- 00b446e0 bytes e20f01ad
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74b1ea695e1f83917017c02524268997"></a>

### [`00b447a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b447a0.md) → [`00b4483c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b4483c.md) _ZN8firebase18AndroidLogMessageVEiPKcS1_St9__va_list

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5b1f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b1f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5b2c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b2c0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

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
      "site": "00b447a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b447a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b447a8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b447a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b447a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b447b8",
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
      "00b44840",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b44844",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b44854",
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

- 旧版 [`00b447a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b447a0.md#insn-00b447a4) · [`00b447a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b447a0.md#insn-00b447a8) · [`00b447b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b447a0.md#insn-00b447b8)

~~~diff
- 00b447a4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:30:8"]]
- 00b447a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00b447a4 bytes f31b00f9
- 00b447a8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b447a8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b447a8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b447a8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b447a8 bytes fd7b04a9
- 00b447b8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b447b8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffe8:8"]]
- 00b447b8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b447b8 bytes a8831ef8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7bae67b53002c970b8bbe5622ed76379"></a>

### [`00b448f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b448f8.md) → [`00b44994`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44994.md) _ZN8firebase4util12class_loader19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 33.33% / 新版 25.00%

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
      "site": "00b44924"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b449c0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b449a8",
      "incomplete_value": true,
      "site": "00b449a8",
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
      "definition_site": "00b4490c",
      "incomplete_value": true,
      "site": "00b4490c",
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
      "00b449a4",
      "READ",
      [
        "storage",
        "01125628",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b44918",
      "PARAM",
      [
        "storage",
        "002b8a26",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b4491c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5afe0"
      ]
    ]
  ],
  "added": [
    [
      "00b449a4",
      "READ",
      [
        "storage",
        "01125728",
        null,
        "undefined8"
      ]
    ],
    [
      "00b449b4",
      "PARAM",
      [
        "storage",
        "002b89d2",
        null,
        "string"
      ]
    ],
    [
      "00b449b8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5afe0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4490c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b448f8.md#insn-00b4490c) · [`00b4491c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b448f8.md#insn-00b4491c) · [`00b44924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b448f8.md#insn-00b44924)
- 新版 [`00b449a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44994.md#insn-00b449a8)

~~~diff
- 00b4490c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b4490c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b449a8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b449a8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b4490c bytes e80000b5
+ 00b449a8 bytes e80000b5
- 00b4491c ["INT_ADD", "register:40f0:8", ["const:b4491c:8", "const:4:8"]]
- 00b4491c ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4491c bytes 7d590494
- 00b44924 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:628:8"]]
- 00b44924 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b44924 bytes 601603f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41c4cc7391a6ec5139cefb90e4eb6ffd"></a>

### [`00b44938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44938.md) → [`00b449d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b449d4.md) _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassReq

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) · 呼出先 4件 [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5b130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b130.md) [`00c5b330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b330.md) [`00c5b570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b570.md)
- 新版 呼出元 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) · 呼出先 4件 [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b200.md) [`00c5b400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b400.md) [`00c5b640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b640.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 47.37% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b449f4",
      "incomplete_value": false,
      "site": "00b44a08",
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
            "const:c54:8"
          ]
        ]
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
      "definition_site": "00b449f8",
      "incomplete_value": true,
      "site": "00b44a08",
      "value": [
        "live",
        "register:4018:8"
      ]
    },
    "old": null,
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b44a40",
      "incomplete_value": false,
      "site": "00b44a4c",
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
            "const:5c6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b449a4",
      "incomplete_value": false,
      "site": "00b449b0",
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
            "const:595:8"
          ]
        ]
      ]
    },
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
      "unmatched:00b44958",
      "PARAM",
      [
        "storage",
        "002b6c14",
        null,
        "string"
      ]
    ],
    [
      "00b44a40",
      "PARAM",
      [
        "storage",
        "002b2595",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b449e8",
      "PARAM",
      [
        "storage",
        "002a9535",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b449f4",
      "PARAM",
      [
        "storage",
        "002b6c54",
        null,
        "string"
      ]
    ],
    [
      "00b44a40",
      "PARAM",
      [
        "storage",
        "002b25c6",
        null,
        "string"
      ]
    ],
    [
      "00b44a84",
      "PARAM",
      [
        "storage",
        "002a9564",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4496c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44938.md#insn-00b4496c) · [`00b449b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44938.md#insn-00b449b0) · [`00b449f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44938.md#insn-00b449f4)
- 新版 [`00b44a08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b449d4.md#insn-00b44a08) · [`00b44a4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b449d4.md#insn-00b44a4c) · [`00b44a90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b449d4.md#insn-00b44a90)

~~~diff
- 00b4496c ["INT_ADD", "register:40f0:8", ["const:b4496c:8", "const:4:8"]]
- 00b4496c ["CALL", null, ["callee:00c5b200:8"]]
+ 00b44a08 ["INT_ADD", "register:40f0:8", ["const:b44a08:8", "const:4:8"]]
+ 00b44a08 ["CALL", null, ["callee:00c5b200:8"]]
- 00b4496c bytes f1590494
+ 00b44a08 bytes fe590494
- 00b449b0 ["INT_ADD", "register:40f0:8", ["const:b449b0:8", "const:4:8"]]
- 00b449b0 ["CALL", null, ["callee:00c5b200:8"]]
+ 00b44a4c ["INT_ADD", "register:40f0:8", ["const:b44a4c:8", "const:4:8"]]
+ 00b44a4c ["CALL", null, ["callee:00c5b200:8"]]
- 00b449b0 bytes e0590494
+ 00b44a4c bytes ed590494
- 00b449f4 ["INT_ADD", "register:40f0:8", ["const:b449f4:8", "const:4:8"]]
- 00b449f4 ["CALL", null, ["callee:00c5b200:8"]]
+ 00b44a90 ["INT_ADD", "register:40f0:8", ["const:b44a90:8", "const:4:8"]]
+ 00b44a90 ["CALL", null, ["callee:00c5b200:8"]]
- 00b449f4 bytes cf590494
+ 00b44a90 bytes dc590494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-565ff5e6eeb29e5e3a4af3686acd41a0"></a>

### [`00b44a68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44a68.md) → [`00b44b04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44b04.md) _ZN8firebase4util12class_loader19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00b44b30",
      "incomplete_value": true,
      "site": "00b44b30",
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
            "const:728:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b44a94",
      "incomplete_value": true,
      "site": "00b44a94",
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
            "const:628:8"
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
      "definition_site": "00b44b18",
      "incomplete_value": true,
      "site": "00b44b18",
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
      "definition_site": "00b44a7c",
      "incomplete_value": true,
      "site": "00b44a7c",
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
      "definition_site": "00b44b20",
      "incomplete_value": false,
      "site": "00b44b28",
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
            "const:9d2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b44a84",
      "incomplete_value": false,
      "site": "00b44a8c",
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
            "const:a26:8"
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
      "00b44b14",
      "READ",
      [
        "storage",
        "01125628",
        null,
        "undefined8"
      ]
    ],
    [
      "00b44b20",
      "PARAM",
      [
        "storage",
        "002b8a26",
        null,
        "string"
      ]
    ],
    [
      "00b44b30",
      "WRITE",
      [
        "storage",
        "01125628",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b44b14",
      "READ",
      [
        "storage",
        "01125728",
        null,
        "undefined8"
      ]
    ],
    [
      "00b44b20",
      "PARAM",
      [
        "storage",
        "002b89d2",
        null,
        "string"
      ]
    ],
    [
      "00b44b30",
      "WRITE",
      [
        "storage",
        "01125728",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b44a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44a68.md#insn-00b44a8c) · [`00b44a94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44a68.md#insn-00b44a94) · [`00b44a78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44a68.md#insn-00b44a78)
- 新版 [`00b44b28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44b04.md#insn-00b44b28) · [`00b44b30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44b04.md#insn-00b44b30) · [`00b44b14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44b04.md#insn-00b44b14)

~~~diff
- 00b44a8c ["INT_ADD", "register:40f0:8", ["const:b44a8c:8", "const:4:8"]]
- 00b44a8c ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b44b28 ["INT_ADD", "register:40f0:8", ["const:b44b28:8", "const:4:8"]]
+ 00b44b28 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b44a8c bytes 21590494
+ 00b44b28 bytes 2e590494
- 00b44a94 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:628:8"]]
- 00b44a94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b44b30 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
+ 00b44b30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b44a94 bytes 601603f9
+ 00b44b30 bytes 609603f9
- 00b44a78 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:628:8"]]
- 00b44a78 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b44b14 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
+ 00b44b14 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b44a78 bytes 681643f9
+ 00b44b14 bytes 689643f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f13ab23916418171f3456628bf2dcfd"></a>

### [`00b44aa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44aa8.md) → [`00b44b44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44b44.md) _ZN8firebase4util12class_loader10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 70.59% / 新版 70.59%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b44ad8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b44b74"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b44b58",
      "incomplete_value": true,
      "site": "00b44b58",
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
      "definition_site": "00b44abc",
      "incomplete_value": true,
      "site": "00b44abc",
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
      "00b44b54",
      "READ",
      [
        "storage",
        "01125628",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b44ac8",
      "PARAM",
      [
        "storage",
        "002b8a26",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b44ad0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5afe0"
      ]
    ]
  ],
  "added": [
    [
      "00b44b54",
      "READ",
      [
        "storage",
        "01125728",
        null,
        "undefined8"
      ]
    ],
    [
      "00b44b64",
      "PARAM",
      [
        "storage",
        "002b89d2",
        null,
        "string"
      ]
    ],
    [
      "00b44b6c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5afe0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b44abc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44aa8.md#insn-00b44abc) · [`00b44ad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44aa8.md#insn-00b44ad0) · [`00b44ad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44aa8.md#insn-00b44ad8)
- 新版 [`00b44b58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44b44.md#insn-00b44b58)

~~~diff
- 00b44abc ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b44abc ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b44b58 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b44b58 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b44abc bytes 080100b5
+ 00b44b58 bytes 080100b5
- 00b44ad0 ["INT_ADD", "register:40f0:8", ["const:b44ad0:8", "const:4:8"]]
- 00b44ad0 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b44ad0 bytes 10590494
- 00b44ad8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:628:8"]]
- 00b44ad8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b44ad8 bytes 601603f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1fb9928d8049ea1bc43fa6c1c0823857"></a>

### [`00b44aec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44aec.md) → [`00b44b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44b88.md) _ZN8firebase4util12class_loader10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_value, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 64.71% / 新版 64.71%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b44b1c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b44bb8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b44b9c",
      "incomplete_value": true,
      "site": "00b44b9c",
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
      "definition_site": "00b44b00",
      "incomplete_value": true,
      "site": "00b44b00",
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
      "00b44b98",
      "READ",
      [
        "storage",
        "01125628",
        null,
        "undefined8"
      ]
    ],
    [
      "00b44b9c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b44b20"
      ]
    ],
    [
      "unmatched:00b44b08",
      "PARAM",
      [
        "storage",
        "002b8a26",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b44b98",
      "READ",
      [
        "storage",
        "01125728",
        null,
        "undefined8"
      ]
    ],
    [
      "00b44b9c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b44bbc"
      ]
    ],
    [
      "00b44ba4",
      "PARAM",
      [
        "storage",
        "002b89d2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b44b1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44aec.md#insn-00b44b1c) · [`00b44b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44aec.md#insn-00b44b2c)
- 新版 [`00b44bb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44b88.md#insn-00b44bb8)

~~~diff
- 00b44b1c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:628:8"]]
- 00b44b1c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b44b1c bytes 601603f9
- 00b44b2c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b44b2c ["RETURN", null, ["register:0:8"]]
- 00b44b2c bytes c0035fd6
+ 00b44bb8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
+ 00b44bb8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b44bb8 bytes 609603f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bdedbc3cd3937b7040ca87e0b001f1fc"></a>

### [`00b44c34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44c34.md) → [`00b44cd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44cd0.md) _ZN8firebase4util12class_loader12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 27.27% / 新版 30.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b44c70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b44d5c",
      "incomplete_value": true,
      "site": "00b44d5c",
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
            "const:728:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b44cc0",
      "incomplete_value": true,
      "site": "00b44cc0",
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
            "const:628:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b44d0c"
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
      "00b44ce4",
      "READ",
      [
        "storage",
        "01125628",
        null,
        "undefined8"
      ]
    ],
    [
      "00b44cf0",
      "READ",
      [
        "storage",
        "01125630",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b44c70",
      "WRITE",
      [
        "storage",
        "01125630",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b44ce4",
      "READ",
      [
        "storage",
        "01125728",
        null,
        "undefined8"
      ]
    ],
    [
      "00b44cf0",
      "READ",
      [
        "storage",
        "01125730",
        null,
        "undefined1"
      ]
    ],
    [
      "00b44d0c",
      "WRITE",
      [
        "storage",
        "01125730",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b44c4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44c34.md#insn-00b44c4c) · [`00b44c70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44c34.md#insn-00b44c70) · [`00b44ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44c34.md#insn-00b44ca8)
- 新版 [`00b44ce8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44cd0.md#insn-00b44ce8)

~~~diff
- 00b44c4c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b44c4c ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 00b44ce8 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b44ce8 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00b44c4c bytes c10300b4
+ 00b44ce8 bytes c10300b4
- 00b44c70 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b44c70 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b44c70 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:630:8"]]
- 00b44c70 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b44c70 bytes bfc21839
- 00b44ca8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b44ca8 ["INT_ADD", "register:40f0:8", ["const:b44ca8:8", "const:4:8"]]
- 00b44ca8 ["CALLIND", null, ["register:0:8"]]
- 00b44ca8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8799bde241b8e3c61fc04591293f8d4b"></a>

### [`00b44cd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44cd4.md) → [`00b44d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44d70.md) _ZN8firebase4util12class_loader14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b44db0",
      "incomplete_value": true,
      "site": "00b44db0",
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
            "const:728:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b44d14",
      "incomplete_value": true,
      "site": "00b44d14",
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
            "const:628:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b44d8c",
      "incomplete_value": true,
      "site": "00b44d8c",
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
      "definition_site": "00b44cf0",
      "incomplete_value": true,
      "site": "00b44cf0",
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
      "definition_site": "00b44d94",
      "incomplete_value": false,
      "site": "00b44da8",
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
            "const:9d2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b44cf8",
      "incomplete_value": false,
      "site": "00b44d0c",
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
            "const:a26:8"
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
      "00b44d84",
      "READ",
      [
        "storage",
        "01125628",
        null,
        "undefined8"
      ]
    ],
    [
      "00b44d94",
      "PARAM",
      [
        "storage",
        "002b8a26",
        null,
        "string"
      ]
    ],
    [
      "00b44db0",
      "WRITE",
      [
        "storage",
        "01125628",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b44d84",
      "READ",
      [
        "storage",
        "01125728",
        null,
        "undefined8"
      ]
    ],
    [
      "00b44d94",
      "PARAM",
      [
        "storage",
        "002b89d2",
        null,
        "string"
      ]
    ],
    [
      "00b44db0",
      "WRITE",
      [
        "storage",
        "01125728",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b44d0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44cd4.md#insn-00b44d0c) · [`00b44d14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44cd4.md#insn-00b44d14) · [`00b44ce8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44cd4.md#insn-00b44ce8)
- 新版 [`00b44da8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44d70.md#insn-00b44da8) · [`00b44db0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44d70.md#insn-00b44db0) · [`00b44d84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44d70.md#insn-00b44d84)

~~~diff
- 00b44d0c ["INT_ADD", "register:40f0:8", ["const:b44d0c:8", "const:4:8"]]
- 00b44d0c ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b44da8 ["INT_ADD", "register:40f0:8", ["const:b44da8:8", "const:4:8"]]
+ 00b44da8 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b44d0c bytes 81580494
+ 00b44da8 bytes 8e580494
- 00b44d14 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:628:8"]]
- 00b44d14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b44db0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:728:8"]]
+ 00b44db0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b44d14 bytes 801603f9
+ 00b44db0 bytes 809603f9
- 00b44ce8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:628:8"]]
- 00b44ce8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b44d84 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:728:8"]]
+ 00b44d84 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b44ce8 bytes 811643f9
+ 00b44d84 bytes 819643f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4438f1aeced5365de36e305ed58b4ba0"></a>

### [`00b44d44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44d44.md) → [`00b44de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44de0.md) _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md) · 呼出先 5件 [`00b517a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b51/00b517a0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b130.md)
- 新版 呼出元 1件 [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md) · 呼出先 5件 [`00b5183c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b51/00b5183c.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b200.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 77.42% / 新版 77.42%

CFGの説明率　旧版 42.59% / 新版 42.59%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b44e90"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b44ec0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b44f10"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b44e2c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b44f24"
      ]
    ],
    [
      "00b44e30",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b44f34"
      ]
    ],
    [
      "00b44e38",
      "PARAM",
      [
        "storage",
        "002c0834",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b44e2c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b44fc0"
      ]
    ],
    [
      "00b44e30",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b44fd0"
      ]
    ],
    [
      "00b44e38",
      "PARAM",
      [
        "storage",
        "002c0874",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b44da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44d44.md#insn-00b44da4) · [`00b44da8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44d44.md#insn-00b44da8) · [`00b44e40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44d44.md#insn-00b44e40)
- 新版 [`00b44e40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44de0.md#insn-00b44e40) · [`00b44e44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44de0.md#insn-00b44e44)

~~~diff
- 00b44da4 ["INT_ADD", "register:40f0:8", ["const:b44da4:8", "const:4:8"]]
- 00b44da4 ["CALL", null, ["callee:00c5b200:8"]]
+ 00b44e40 ["INT_ADD", "register:40f0:8", ["const:b44e40:8", "const:4:8"]]
+ 00b44e40 ["CALL", null, ["callee:00c5b200:8"]]
- 00b44da4 bytes e3580494
+ 00b44e40 bytes f0580494
- 00b44da8 ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
- 00b44da8 ["CBRANCH", null, ["local:b33:8", "tmp:0:1"]]
+ 00b44e44 ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
+ 00b44e44 ["CBRANCH", null, ["local:b34:8", "tmp:0:1"]]
- 00b44da8 bytes 950e00b4
+ 00b44e44 bytes 950e00b4
- 00b44e40 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:720:8"]]
- 00b44e40 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b44e40 bytes 089143f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2956ea8cde2c3ec8fa5a2182a92934d"></a>

### [`00b44fec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44fec.md) → [`00b45088`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45088.md) _ZN8firebase4util12class_loader13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00b4502c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b450c8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45008"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b45000",
      "READ",
      [
        "storage",
        "01125628",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b45008",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b450cc"
      ]
    ],
    [
      "unmatched:00b45010",
      "PARAM",
      [
        "storage",
        "002b8a26",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4509c",
      "READ",
      [
        "storage",
        "01125728",
        null,
        "undefined8"
      ]
    ],
    [
      "00b450a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b450cc"
      ]
    ],
    [
      "00b450ac",
      "PARAM",
      [
        "storage",
        "002b89d2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44fec.md#insn-00b45008) · [`00b45024`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44fec.md#insn-00b45024) · [`00b4502c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44fec.md#insn-00b4502c)
- 新版 [`00b450c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45088.md#insn-00b450c0)

~~~diff
- 00b45008 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b45008 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b45008 bytes 410100b5
- 00b45024 ["INT_ADD", "register:40f0:8", ["const:b45024:8", "const:4:8"]]
- 00b45024 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b450c0 ["INT_ADD", "register:40f0:8", ["const:b450c0:8", "const:4:8"]]
+ 00b450c0 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b45024 bytes bb570494
+ 00b450c0 bytes c8570494
- 00b4502c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:628:8"]]
- 00b4502c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4502c bytes 801603f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2bc9a2e4ccf5bc32b91821835a9dcb60"></a>

### [`00b4505c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b4505c.md) → [`00b450f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b450f8.md) _ZN8firebase4util14LookupFieldIdsEP7_JNIEnvP7_jclassPKNS0_15FieldDescriptorEmPP9_jfieldIDPKc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) · 呼出先 5件 [`00b517a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b51/00b517a0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b130.md)
- 新版 呼出元 1件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) · 呼出先 5件 [`00b5183c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b51/00b5183c.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b200.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 78.71% / 新版 78.71%

CFGの説明率　旧版 38.89% / 新版 38.89%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 4件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4509c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b45138"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45110"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4509c",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "00b45140",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b4522c"
      ]
    ],
    [
      "00b45148",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b4524c"
      ]
    ]
  ],
  "added": [
    [
      "00b45138",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "00b45140",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b452c8"
      ]
    ],
    [
      "00b45148",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b452e8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4509c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b4505c.md#insn-00b4509c) · [`00b450bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b4505c.md#insn-00b450bc) · [`00b45110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b4505c.md#insn-00b45110)
- 新版 [`00b45158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b450f8.md#insn-00b45158)

~~~diff
- 00b4509c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b4509c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffa0:8"]]
- 00b4509c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b4509c bytes a8031af8
- 00b450bc ["INT_ADD", "register:40f0:8", ["const:b450bc:8", "const:4:8"]]
- 00b450bc ["CALL", null, ["callee:00c5b200:8"]]
+ 00b45158 ["INT_ADD", "register:40f0:8", ["const:b45158:8", "const:4:8"]]
+ 00b45158 ["CALL", null, ["callee:00c5b200:8"]]
- 00b450bc bytes 1d580494
+ 00b45158 bytes 2a580494
- 00b45110 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b45110 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00b45110 bytes 08ffffb4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-631aab11a59cb7542ea9ec93585a9f58"></a>

### [`00b452c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b452c8.md) → [`00b45364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45364.md) _ZN8firebase4util12class_loader10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
      "definition_site": "00b45380",
      "incomplete_value": false,
      "site": "00b45384",
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
            "const:54d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b452e4",
      "incomplete_value": false,
      "site": "00b452e8",
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
            "const:51e:8"
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
      "definition_site": "00b45390",
      "incomplete_value": true,
      "site": "00b4539c",
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
      "definition_site": "00b452f4",
      "incomplete_value": true,
      "site": "00b45300",
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
      "00b45380",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b45390",
      "DATA",
      [
        "storage",
        "01125648",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b45380",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b45390",
      "DATA",
      [
        "storage",
        "01125748",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b452e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b452c8.md#insn-00b452e8) · [`00b452e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b452c8.md#insn-00b452e4) · [`00b452f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b452c8.md#insn-00b452f0)
- 新版 [`00b45384`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45364.md#insn-00b45384) · [`00b45380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45364.md#insn-00b45380) · [`00b4538c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45364.md#insn-00b4538c)

~~~diff
- 00b452e8 ["INT_ADD", "register:40f0:8", ["const:b452e8:8", "const:4:8"]]
- 00b452e8 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b45384 ["INT_ADD", "register:40f0:8", ["const:b45384:8", "const:4:8"]]
+ 00b45384 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b452e8 bytes 46570494
+ 00b45384 bytes 53570494
- 00b452e4 ["COPY", "tmp:0:8", ["const:51e:8"]]
- 00b452e4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b452e4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b452e4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b45380 ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00b45380 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b45380 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b45380 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b452e4 bytes 00781491
+ 00b45380 bytes 00341591
- 00b452f0 ["COPY", "tmp:0:8", ["const:648:8"]]
- 00b452f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b452f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b452f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4538c ["COPY", "tmp:0:8", ["const:748:8"]]
+ 00b4538c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4538c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4538c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b452f0 bytes 08211991
+ 00b4538c bytes 08211d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6dfeed44836070861afaef5e65a69b84"></a>

### [`00b45304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45304.md) → [`00b453a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b453a0.md) _ZN8firebase4util17jniresultcallback19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00b453cc",
      "incomplete_value": true,
      "site": "00b453cc",
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
            "const:750:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b45330",
      "incomplete_value": true,
      "site": "00b45330",
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
            "const:650:8"
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
      "definition_site": "00b453b4",
      "incomplete_value": true,
      "site": "00b453b4",
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
      "definition_site": "00b45318",
      "incomplete_value": true,
      "site": "00b45318",
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
      "definition_site": "00b453c0",
      "incomplete_value": false,
      "site": "00b453c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b0000:8"
          ],
          [
            "leaf",
            "const:4a1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b45324",
      "incomplete_value": false,
      "site": "00b45328",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b0000:8"
          ],
          [
            "leaf",
            "const:4fd:8"
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
      "00b453b0",
      "READ",
      [
        "storage",
        "01125650",
        null,
        "undefined8"
      ]
    ],
    [
      "00b453c0",
      "PARAM",
      [
        "storage",
        "002b04fd",
        null,
        "string"
      ]
    ],
    [
      "00b453cc",
      "WRITE",
      [
        "storage",
        "01125650",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b453b0",
      "READ",
      [
        "storage",
        "01125750",
        null,
        "undefined8"
      ]
    ],
    [
      "00b453c0",
      "PARAM",
      [
        "storage",
        "002b04a1",
        null,
        "string"
      ]
    ],
    [
      "00b453cc",
      "WRITE",
      [
        "storage",
        "01125750",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45328`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45304.md#insn-00b45328) · [`00b45330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45304.md#insn-00b45330) · [`00b45314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45304.md#insn-00b45314)
- 新版 [`00b453c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b453a0.md#insn-00b453c4) · [`00b453cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b453a0.md#insn-00b453cc) · [`00b453b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b453a0.md#insn-00b453b0)

~~~diff
- 00b45328 ["INT_ADD", "register:40f0:8", ["const:b45328:8", "const:4:8"]]
- 00b45328 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b453c4 ["INT_ADD", "register:40f0:8", ["const:b453c4:8", "const:4:8"]]
+ 00b453c4 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b45328 bytes fa560494
+ 00b453c4 bytes 07570494
- 00b45330 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:650:8"]]
- 00b45330 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b453cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:750:8"]]
+ 00b453cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b45330 bytes 602a03f9
+ 00b453cc bytes 60aa03f9
- 00b45314 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:650:8"]]
- 00b45314 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b453b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:750:8"]]
+ 00b453b0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b45314 bytes 682a43f9
+ 00b453b0 bytes 68aa43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bbbe7e3a896474799e2ec340c46008a4"></a>

### [`00b45344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45344.md) → [`00b453e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b453e0.md) _ZN8firebase4util17jniresultcallback19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00b4540c",
      "incomplete_value": true,
      "site": "00b4540c",
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
            "const:750:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b45370",
      "incomplete_value": true,
      "site": "00b45370",
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
            "const:650:8"
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
      "definition_site": "00b453f4",
      "incomplete_value": true,
      "site": "00b453f4",
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
      "definition_site": "00b45358",
      "incomplete_value": true,
      "site": "00b45358",
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
      "definition_site": "00b453fc",
      "incomplete_value": false,
      "site": "00b45404",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b0000:8"
          ],
          [
            "leaf",
            "const:4a1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b45360",
      "incomplete_value": false,
      "site": "00b45368",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b0000:8"
          ],
          [
            "leaf",
            "const:4fd:8"
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
      "00b453f0",
      "READ",
      [
        "storage",
        "01125650",
        null,
        "undefined8"
      ]
    ],
    [
      "00b453fc",
      "PARAM",
      [
        "storage",
        "002b04fd",
        null,
        "string"
      ]
    ],
    [
      "00b4540c",
      "WRITE",
      [
        "storage",
        "01125650",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b453f0",
      "READ",
      [
        "storage",
        "01125750",
        null,
        "undefined8"
      ]
    ],
    [
      "00b453fc",
      "PARAM",
      [
        "storage",
        "002b04a1",
        null,
        "string"
      ]
    ],
    [
      "00b4540c",
      "WRITE",
      [
        "storage",
        "01125750",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45344.md#insn-00b45368) · [`00b45370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45344.md#insn-00b45370) · [`00b45354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45344.md#insn-00b45354)
- 新版 [`00b45404`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b453e0.md#insn-00b45404) · [`00b4540c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b453e0.md#insn-00b4540c) · [`00b453f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b453e0.md#insn-00b453f0)

~~~diff
- 00b45368 ["INT_ADD", "register:40f0:8", ["const:b45368:8", "const:4:8"]]
- 00b45368 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b45404 ["INT_ADD", "register:40f0:8", ["const:b45404:8", "const:4:8"]]
+ 00b45404 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b45368 bytes ea560494
+ 00b45404 bytes f7560494
- 00b45370 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:650:8"]]
- 00b45370 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4540c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:750:8"]]
+ 00b4540c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b45370 bytes 602a03f9
+ 00b4540c bytes 60aa03f9
- 00b45354 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:650:8"]]
- 00b45354 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b453f0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:750:8"]]
+ 00b453f0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b45354 bytes 682a43f9
+ 00b453f0 bytes 68aa43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf105f21a588f475871dbf6a0c9dbf4a"></a>

### [`00b45384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45384.md) → [`00b45420`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45420.md) _ZN8firebase4util17jniresultcallback10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00b45450",
      "incomplete_value": true,
      "site": "00b45450",
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
            "const:750:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b453b4",
      "incomplete_value": true,
      "site": "00b453b4",
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
            "const:650:8"
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
      "definition_site": "00b45434",
      "incomplete_value": true,
      "site": "00b45434",
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
      "definition_site": "00b45398",
      "incomplete_value": true,
      "site": "00b45398",
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
      "definition_site": "00b45440",
      "incomplete_value": false,
      "site": "00b45448",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b0000:8"
          ],
          [
            "leaf",
            "const:4a1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b453a4",
      "incomplete_value": false,
      "site": "00b453ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b0000:8"
          ],
          [
            "leaf",
            "const:4fd:8"
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
      "00b45430",
      "READ",
      [
        "storage",
        "01125650",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45440",
      "PARAM",
      [
        "storage",
        "002b04fd",
        null,
        "string"
      ]
    ],
    [
      "00b45450",
      "WRITE",
      [
        "storage",
        "01125650",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b45430",
      "READ",
      [
        "storage",
        "01125750",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45440",
      "PARAM",
      [
        "storage",
        "002b04a1",
        null,
        "string"
      ]
    ],
    [
      "00b45450",
      "WRITE",
      [
        "storage",
        "01125750",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b453ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45384.md#insn-00b453ac) · [`00b453b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45384.md#insn-00b453b4) · [`00b45394`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45384.md#insn-00b45394)
- 新版 [`00b45448`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45420.md#insn-00b45448) · [`00b45450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45420.md#insn-00b45450) · [`00b45430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45420.md#insn-00b45430)

~~~diff
- 00b453ac ["INT_ADD", "register:40f0:8", ["const:b453ac:8", "const:4:8"]]
- 00b453ac ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b45448 ["INT_ADD", "register:40f0:8", ["const:b45448:8", "const:4:8"]]
+ 00b45448 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b453ac bytes d9560494
+ 00b45448 bytes e6560494
- 00b453b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:650:8"]]
- 00b453b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b45450 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:750:8"]]
+ 00b45450 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b453b4 bytes 602a03f9
+ 00b45450 bytes 60aa03f9
- 00b45394 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:650:8"]]
- 00b45394 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b45430 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:750:8"]]
+ 00b45430 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b45394 bytes 682a43f9
+ 00b45430 bytes 68aa43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62e0faa0d9275d19e27921bb6c41aa7c"></a>

### [`00b453c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b453c8.md) → [`00b45464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45464.md) _ZN8firebase4util17jniresultcallback10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

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
      "definition_site": "00b45494",
      "incomplete_value": true,
      "site": "00b45494",
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
            "const:750:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b453f8",
      "incomplete_value": true,
      "site": "00b453f8",
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
            "const:650:8"
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
      "definition_site": "00b45478",
      "incomplete_value": true,
      "site": "00b45478",
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
      "definition_site": "00b453dc",
      "incomplete_value": true,
      "site": "00b453dc",
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
      "definition_site": "00b45480",
      "incomplete_value": false,
      "site": "00b4548c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b0000:8"
          ],
          [
            "leaf",
            "const:4a1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b453e4",
      "incomplete_value": false,
      "site": "00b453f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b0000:8"
          ],
          [
            "leaf",
            "const:4fd:8"
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
      "00b45474",
      "READ",
      [
        "storage",
        "01125650",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45480",
      "PARAM",
      [
        "storage",
        "002b04fd",
        null,
        "string"
      ]
    ],
    [
      "00b45494",
      "WRITE",
      [
        "storage",
        "01125650",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b45474",
      "READ",
      [
        "storage",
        "01125750",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45480",
      "PARAM",
      [
        "storage",
        "002b04a1",
        null,
        "string"
      ]
    ],
    [
      "00b45494",
      "WRITE",
      [
        "storage",
        "01125750",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b453f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b453c8.md#insn-00b453f0) · [`00b453f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b453c8.md#insn-00b453f8) · [`00b453d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b453c8.md#insn-00b453d8)
- 新版 [`00b4548c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45464.md#insn-00b4548c) · [`00b45494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45464.md#insn-00b45494) · [`00b45474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45464.md#insn-00b45474)

~~~diff
- 00b453f0 ["INT_ADD", "register:40f0:8", ["const:b453f0:8", "const:4:8"]]
- 00b453f0 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b4548c ["INT_ADD", "register:40f0:8", ["const:b4548c:8", "const:4:8"]]
+ 00b4548c ["CALL", null, ["callee:00c5afe0:8"]]
- 00b453f0 bytes c8560494
+ 00b4548c bytes d5560494
- 00b453f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:650:8"]]
- 00b453f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b45494 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:750:8"]]
+ 00b45494 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b453f8 bytes 602a03f9
+ 00b45494 bytes 60aa03f9
- 00b453d8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:650:8"]]
- 00b453d8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b45474 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:750:8"]]
+ 00b45474 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b453d8 bytes 682a43f9
+ 00b45474 bytes 68aa43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4fb60cbf4e053766e5f52207840fdd6f"></a>

### [`00b45418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45418.md) → [`00b454b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b454b4.md) _ZN8firebase4util17jniresultcallback15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 71.79% / 新版 71.79%

CFGの説明率　旧版 37.50% / 新版 30.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4553c",
      "incomplete_value": true,
      "site": "00b4553c",
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
            "const:758:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b454a0",
      "incomplete_value": true,
      "site": "00b454a0",
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
            "const:658:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45474"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b45510"
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
      "00b454c8",
      "READ",
      [
        "storage",
        "01125658",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b4544c",
      "READ",
      [
        "storage",
        "01125650",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b45474",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b45534"
      ]
    ]
  ],
  "added": [
    [
      "00b454c8",
      "READ",
      [
        "storage",
        "01125758",
        null,
        "undefined1"
      ]
    ],
    [
      "00b454e8",
      "READ",
      [
        "storage",
        "01125750",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45510",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b45534"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45418.md#insn-00b45458) · [`00b45474`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45418.md#insn-00b45474) · [`00b45484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45418.md#insn-00b45484)
- 新版 [`00b454f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b454b4.md#insn-00b454f4)

~~~diff
- 00b45458 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b45458 ["INT_ADD", "register:40f0:8", ["const:b45458:8", "const:4:8"]]
- 00b45458 ["CALLIND", null, ["register:0:8"]]
+ 00b454f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b454f4 ["INT_ADD", "register:40f0:8", ["const:b454f4:8", "const:4:8"]]
+ 00b454f4 ["CALLIND", null, ["register:0:8"]]
- 00b45458 bytes 00013fd6
+ 00b454f4 bytes 00013fd6
- 00b45474 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
- 00b45474 bytes 20010054
- 00b45484 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b45484 ["INT_ADD", "register:40f0:8", ["const:b45484:8", "const:4:8"]]
- 00b45484 ["CALLIND", null, ["register:0:8"]]
- 00b45484 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83881e488fb20324a1f3b153c26f6827"></a>

### [`00b45554`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45554.md) → [`00b455f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b455f0.md) _ZN8firebase4util17jniresultcallback14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b45630",
      "incomplete_value": true,
      "site": "00b45630",
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
            "const:750:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b45594",
      "incomplete_value": true,
      "site": "00b45594",
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
            "const:650:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4560c",
      "incomplete_value": true,
      "site": "00b4560c",
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
      "definition_site": "00b45570",
      "incomplete_value": true,
      "site": "00b45570",
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
      "definition_site": "00b45614",
      "incomplete_value": false,
      "site": "00b45628",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b0000:8"
          ],
          [
            "leaf",
            "const:4a1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b45578",
      "incomplete_value": false,
      "site": "00b4558c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b0000:8"
          ],
          [
            "leaf",
            "const:4fd:8"
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
      "00b45604",
      "READ",
      [
        "storage",
        "01125650",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45614",
      "PARAM",
      [
        "storage",
        "002b04fd",
        null,
        "string"
      ]
    ],
    [
      "00b45630",
      "WRITE",
      [
        "storage",
        "01125650",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b45604",
      "READ",
      [
        "storage",
        "01125750",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45614",
      "PARAM",
      [
        "storage",
        "002b04a1",
        null,
        "string"
      ]
    ],
    [
      "00b45630",
      "WRITE",
      [
        "storage",
        "01125750",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4558c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45554.md#insn-00b4558c) · [`00b45594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45554.md#insn-00b45594) · [`00b45568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45554.md#insn-00b45568)
- 新版 [`00b45628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b455f0.md#insn-00b45628) · [`00b45630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b455f0.md#insn-00b45630) · [`00b45604`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b455f0.md#insn-00b45604)

~~~diff
- 00b4558c ["INT_ADD", "register:40f0:8", ["const:b4558c:8", "const:4:8"]]
- 00b4558c ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b45628 ["INT_ADD", "register:40f0:8", ["const:b45628:8", "const:4:8"]]
+ 00b45628 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b4558c bytes 61560494
+ 00b45628 bytes 6e560494
- 00b45594 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:650:8"]]
- 00b45594 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b45630 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:750:8"]]
+ 00b45630 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b45594 bytes 802a03f9
+ 00b45630 bytes 80aa03f9
- 00b45568 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:650:8"]]
- 00b45568 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b45604 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:750:8"]]
+ 00b45604 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b45568 bytes 812a43f9
+ 00b45604 bytes 81aa43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca9a116f1daa9b6f22a0e7287b940af4"></a>

### [`00b455c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b455c4.md) → [`00b45660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45660.md) _ZN8firebase4util17jniresultcallback11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
      "definition_site": "00b4567c",
      "incomplete_value": false,
      "site": "00b45680",
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
            "const:30b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b455e0",
      "incomplete_value": false,
      "site": "00b455e4",
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
            "const:367:8"
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
      "definition_site": "00b4568c",
      "incomplete_value": true,
      "site": "00b45698",
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
      "definition_site": "00b455f0",
      "incomplete_value": true,
      "site": "00b455fc",
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
      "00b4567c",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b4568c",
      "DATA",
      [
        "storage",
        "01125660",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4567c",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b4568c",
      "DATA",
      [
        "storage",
        "01125760",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b455e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b455c4.md#insn-00b455e4) · [`00b455e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b455c4.md#insn-00b455e0) · [`00b455ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b455c4.md#insn-00b455ec)
- 新版 [`00b45680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45660.md#insn-00b45680) · [`00b4567c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45660.md#insn-00b4567c) · [`00b45688`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45660.md#insn-00b45688)

~~~diff
- 00b455e4 ["INT_ADD", "register:40f0:8", ["const:b455e4:8", "const:4:8"]]
- 00b455e4 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b45680 ["INT_ADD", "register:40f0:8", ["const:b45680:8", "const:4:8"]]
+ 00b45680 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b455e4 bytes 87560494
+ 00b45680 bytes 94560494
- 00b455e0 ["COPY", "tmp:0:8", ["const:367:8"]]
- 00b455e0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b455e0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b455e0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4567c ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00b4567c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4567c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4567c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b455e0 bytes 009c0d91
+ 00b4567c bytes 002c0c91
- 00b455ec ["COPY", "tmp:0:8", ["const:660:8"]]
- 00b455ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b455ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b455ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b45688 ["COPY", "tmp:0:8", ["const:760:8"]]
+ 00b45688 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b45688 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b45688 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b455ec bytes 08811991
+ 00b45688 bytes 08811d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-237acb77bcef042ee05389f31dc7f625"></a>

### [`00b45600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45600.md) → [`00b4569c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b4569c.md) _ZN8firebase4util17jniresultcallback13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00b45640"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b456dc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4561c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b45614",
      "READ",
      [
        "storage",
        "01125650",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b4561c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b456e0"
      ]
    ],
    [
      "unmatched:00b45624",
      "PARAM",
      [
        "storage",
        "002b04fd",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b456b0",
      "READ",
      [
        "storage",
        "01125750",
        null,
        "undefined8"
      ]
    ],
    [
      "00b456b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b456e0"
      ]
    ],
    [
      "00b456c0",
      "PARAM",
      [
        "storage",
        "002b04a1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4561c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45600.md#insn-00b4561c) · [`00b45638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45600.md#insn-00b45638) · [`00b45640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45600.md#insn-00b45640)
- 新版 [`00b456d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b4569c.md#insn-00b456d4)

~~~diff
- 00b4561c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b4561c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b4561c bytes 410100b5
- 00b45638 ["INT_ADD", "register:40f0:8", ["const:b45638:8", "const:4:8"]]
- 00b45638 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b456d4 ["INT_ADD", "register:40f0:8", ["const:b456d4:8", "const:4:8"]]
+ 00b456d4 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b45638 bytes 36560494
+ 00b456d4 bytes 43560494
- 00b45640 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:650:8"]]
- 00b45640 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b45640 bytes 802a03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d6ae19365cafc8e70ae0178c16b9e14"></a>

### [`00b456ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b456ec.md) → [`00b45788`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45788.md) _ZN8firebase4util26cppthreaddispatchercontext19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9al

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_value, call_argument_candidate, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_destination, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 1件, `unresolved_store_alignment` 2件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b456f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b456f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b457b4",
      "incomplete_value": true,
      "site": "00b457b4",
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
            "const:778:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b45718",
      "incomplete_value": true,
      "site": "00b45718",
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
            "const:678:8"
          ]
        ]
      ]
    },
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
      "unmatched:00b456f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b45798",
      "READ",
      [
        "storage",
        "01125678",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b45708",
      "PARAM",
      [
        "storage",
        "002be58b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4578c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b45798",
      "READ",
      [
        "storage",
        "01125778",
        null,
        "undefined8"
      ]
    ],
    [
      "00b457a4",
      "PARAM",
      [
        "storage",
        "002be537",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b456f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b456ec.md#insn-00b456f0) · [`00b45710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b456ec.md#insn-00b45710) · [`00b45718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b456ec.md#insn-00b45718)
- 新版 [`00b457ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45788.md#insn-00b457ac) · [`00b457b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45788.md#insn-00b457b4)

~~~diff
- 00b456f0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b456f0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b456f0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b456f0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b456f0 bytes fd7b01a9
- 00b45710 ["INT_ADD", "register:40f0:8", ["const:b45710:8", "const:4:8"]]
- 00b45710 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b457ac ["INT_ADD", "register:40f0:8", ["const:b457ac:8", "const:4:8"]]
+ 00b457ac ["CALL", null, ["callee:00c5afe0:8"]]
- 00b45710 bytes 00560494
+ 00b457ac bytes 0d560494
- 00b45718 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:678:8"]]
- 00b45718 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b457b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:778:8"]]
+ 00b457b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b45718 bytes 603e03f9
+ 00b457b4 bytes 60be03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7d0032861e45941ba1c530bdc8c4638"></a>

### [`00b45770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45770.md) → [`00b4580c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b4580c.md) _ZN8firebase4util26cppthreaddispatchercontext10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 14.29% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b457a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4583c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b45820",
      "incomplete_value": true,
      "site": "00b45820",
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
      "definition_site": "00b45784",
      "incomplete_value": true,
      "site": "00b45784",
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
      "00b4581c",
      "READ",
      [
        "storage",
        "01125678",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b4578c",
      "PARAM",
      [
        "storage",
        "002be58b",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b457a0",
      "WRITE",
      [
        "storage",
        "01125678",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4581c",
      "READ",
      [
        "storage",
        "01125778",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45828",
      "PARAM",
      [
        "storage",
        "002be537",
        null,
        "string"
      ]
    ],
    [
      "00b4583c",
      "WRITE",
      [
        "storage",
        "01125778",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45770.md#insn-00b45784) · [`00b45798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45770.md#insn-00b45798) · [`00b457a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45770.md#insn-00b457a0)
- 新版 [`00b45820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b4580c.md#insn-00b45820) · [`00b45834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b4580c.md#insn-00b45834)

~~~diff
- 00b45784 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b45784 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b45820 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b45820 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b45784 bytes 080100b5
+ 00b45820 bytes 080100b5
- 00b45798 ["INT_ADD", "register:40f0:8", ["const:b45798:8", "const:4:8"]]
- 00b45798 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b45834 ["INT_ADD", "register:40f0:8", ["const:b45834:8", "const:4:8"]]
+ 00b45834 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b45798 bytes de550494
+ 00b45834 bytes eb550494
- 00b457a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:678:8"]]
- 00b457a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b457a0 bytes 603e03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df287fd1467a4a08d3c93dbf7b65ad9a"></a>

### [`00b458fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b458fc.md) → [`00b45998`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45998.md) _ZN8firebase4util26cppthreaddispatchercontext14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4593c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b459d8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45918"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b45910",
      "READ",
      [
        "storage",
        "01125678",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b45918",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b459dc"
      ]
    ],
    [
      "unmatched:00b45920",
      "PARAM",
      [
        "storage",
        "002be58b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b459ac",
      "READ",
      [
        "storage",
        "01125778",
        null,
        "undefined8"
      ]
    ],
    [
      "00b459b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b459dc"
      ]
    ],
    [
      "00b459bc",
      "PARAM",
      [
        "storage",
        "002be537",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b458fc.md#insn-00b45918) · [`00b45934`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b458fc.md#insn-00b45934) · [`00b4593c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b458fc.md#insn-00b4593c)
- 新版 [`00b459d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b45/00b45998.md#insn-00b459d0)

~~~diff
- 00b45918 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b45918 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00b45918 bytes 410100b5
- 00b45934 ["INT_ADD", "register:40f0:8", ["const:b45934:8", "const:4:8"]]
- 00b45934 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b459d0 ["INT_ADD", "register:40f0:8", ["const:b459d0:8", "const:4:8"]]
+ 00b459d0 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b45934 bytes 77550494
+ 00b459d0 bytes 84550494
- 00b4593c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:678:8"]]
- 00b4593c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4593c bytes 803e03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

