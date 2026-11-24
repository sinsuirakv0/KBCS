# v16.0.1 → v16.0.2 · 最優先の変更候補 (76)

[一覧の目次](README.md)

<a id="compare-3195bb5e6b1aae870e94d139c33c0eab"></a>

### [`00b62b94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b62/00b62b94.md) → [`00b62c30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b62c30.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN8firebase10InitResultEEENS_19__map_value_co

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bd70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bd70.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 1件 [`00c5be40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5be40.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 98.61% / 新版 98.61%

CFGの説明率　旧版 90.32% / 新版 93.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b62bbc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b62c58"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "CONDITIONAL_JUMP",
        "00b62bbc"
      ],
      [
        "CONDITIONAL_JUMP",
        "00b62c58"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b62c58",
      "incomplete_value": true,
      "site": "00b62d20",
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
      "definition_site": "00b62bbc",
      "incomplete_value": true,
      "site": "00b62c84",
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
      "unmatched:00b62bbc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b62d20"
      ]
    ]
  ],
  "added": [
    [
      "00b62c58",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b62d20"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62bbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b62/00b62b94.md#insn-00b62bbc) · [`00b62c58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b62/00b62b94.md#insn-00b62c58)
- 新版 `00b62cf4`（命令位置の公開資料なし） · `00b62c58`（命令位置の公開資料なし）

~~~diff
- 00b62bbc ["INT_EQUAL", "tmp:0:1", ["register:40b8:8", "const:0:8"]]
- 00b62bbc ["CBRANCH", null, ["local:b18:8", "tmp:0:1"]]
- 00b62bbc bytes 570600b4
- 00b62c58 ["INT_EQUAL", "tmp:0:1", ["register:40b0:8", "const:0:8"]]
- 00b62c58 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b62cf4 ["INT_EQUAL", "tmp:0:1", ["register:40b0:8", "const:0:8"]]
+ 00b62cf4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b62c58 bytes 56fcffb4
+ 00b62cf4 bytes 56fcffb4
+ 00b62c58 ["INT_EQUAL", "tmp:0:1", ["register:40b8:8", "const:0:8"]]
+ 00b62c58 ["CBRANCH", null, ["local:b17:8", "tmp:0:1"]]
+ 00b62c58 bytes 570600b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de9b293c6690b1f9b5feda040795d9ce"></a>

### [`00b62ee8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b62/00b62ee8.md) → [`00b62f84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b62f84.md) _INIT_283

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c5ac80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c5ad50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad50.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b62fb0",
      "incomplete_value": true,
      "site": "00b62fb0",
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
                "const:890:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62f14",
      "incomplete_value": true,
      "site": "00b62f14",
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
                "const:7c0:8"
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
    "kind": "store_destination",
    "new": {
      "definition_site": "00b62fd0",
      "incomplete_value": true,
      "site": "00b62fd0",
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
                "const:8a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62f34",
      "incomplete_value": true,
      "site": "00b62f34",
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
                "const:7d0:8"
              ]
            ]
          ]
        ]
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
      "definition_site": "00b62f1c",
      "incomplete_value": false,
      "site": "00b62f24",
      "value": [
        "leaf",
        "const:1:8"
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
      "00b62fa8",
      "READ",
      [
        "storage",
        "00c9b7c0",
        null,
        "pointer"
      ]
    ],
    [
      "00b62fb0",
      "WRITE",
      [
        "storage",
        "01126030",
        "_ZN8firebase11AppCallback16callbacks_mutex_E",
        "undefined8"
      ]
    ],
    [
      "00b62fc8",
      "READ",
      [
        "storage",
        "00c9b7d0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b62fa8",
      "READ",
      [
        "storage",
        "00c9b890",
        null,
        "pointer"
      ]
    ],
    [
      "00b62fb0",
      "WRITE",
      [
        "storage",
        "01126130",
        "_ZN8firebase11AppCallback16callbacks_mutex_E",
        "undefined8"
      ]
    ],
    [
      "00b62fc8",
      "READ",
      [
        "storage",
        "00c9b8a0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62f24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b62/00b62ee8.md#insn-00b62f24) · [`00b62ef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b62/00b62ee8.md#insn-00b62ef8) · [`00b62f04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b62/00b62ee8.md#insn-00b62f04)
- 新版 `00b62fc0`（命令位置の公開資料なし） · `00b62f94`（命令位置の公開資料なし） · `00b62fa0`（命令位置の公開資料なし）

~~~diff
- 00b62f24 ["INT_ADD", "register:40f0:8", ["const:b62f24:8", "const:4:8"]]
- 00b62f24 ["CALL", null, ["callee:00c5ad50:8"]]
+ 00b62fc0 ["INT_ADD", "register:40f0:8", ["const:b62fc0:8", "const:4:8"]]
+ 00b62fc0 ["CALL", null, ["callee:00c5ad50:8"]]
- 00b62f24 bytes 57df0394
+ 00b62fc0 bytes 64df0394
- 00b62ef8 ["INT_ADD", "register:40f0:8", ["const:b62ef8:8", "const:4:8"]]
- 00b62ef8 ["CALL", null, ["callee:00c57f60:8"]]
+ 00b62f94 ["INT_ADD", "register:40f0:8", ["const:b62f94:8", "const:4:8"]]
+ 00b62f94 ["CALL", null, ["callee:00c57f60:8"]]
- 00b62ef8 bytes e6d30394
+ 00b62f94 bytes f3d30394
- 00b62f04 ["INT_ADD", "register:40f0:8", ["const:b62f04:8", "const:4:8"]]
- 00b62f04 ["CALL", null, ["callee:00c5ad50:8"]]
+ 00b62fa0 ["INT_ADD", "register:40f0:8", ["const:b62fa0:8", "const:4:8"]]
+ 00b62fa0 ["CALL", null, ["callee:00c5ad50:8"]]
- 00b62f04 bytes 5fdf0394
+ 00b62fa0 bytes 6cdf0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ce83b2b071903be05b377cd54adf465"></a>

### [`00b62f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b62/00b62f40.md) → [`00b62fdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b62fdc.md) _ZN8firebase7VariantaSERKS0_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5a8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8f0.md) · 呼出先 11件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a830.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 1件 [`00c5a9c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a9c0.md) · 呼出先 11件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a900.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 69.38% / 新版 69.38%

CFGの説明率　旧版 65.28% / 新版 65.28%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 22件, `unresolved_call_alignment` 5件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b62f44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b62f48"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b62f48"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b62f44",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b62f48",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b62f4c",
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
      "00b62fe0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b62fe4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b62fe8",
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

- 旧版 [`00b62f44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b62/00b62f40.md#insn-00b62f44) · [`00b62f48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b62/00b62f40.md#insn-00b62f48) · [`00b62f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b62/00b62f40.md#insn-00b62f4c)

~~~diff
- 00b62f44 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00b62f44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00b62f44 bytes f51300f9
- 00b62f48 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b62f48 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b62f48 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b62f48 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b62f48 bytes f44f03a9
- 00b62f4c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b62f4c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b62f4c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b62f4c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b62f4c bytes fd7b04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76672c4a77e744c4db3eb362292d89a4"></a>

### [`00b63284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b63/00b63284.md) → [`00b63320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b63/00b63320.md) _ZN8firebase7Variant5ClearENS0_4TypeE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b63284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b63/00b63284.md) [`00c5a830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a830.md) · 呼出先 6件 [`00b63284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b63/00b63284.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5be20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be20.md)
- 新版 呼出元 2件 [`00b63320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b63/00b63320.md) [`00c5a900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a900.md) · 呼出先 6件 [`00b63320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b63/00b63320.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5bef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bef0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 56.31% / 新版 54.72%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b634e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b63580"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b63300"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b632bc",
      "DATA",
      [
        "storage",
        "0030bc14",
        "switchD_00b632c4::switchdataD_0030bc14",
        "byte"
      ]
    ],
    [
      "00b63360",
      "COMPUTED_JUMP",
      [
        "local_branch",
        "unmatched:00b632f8"
      ]
    ],
    [
      "unmatched:00b63300",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b63464"
      ]
    ]
  ],
  "added": [
    [
      "00b63358",
      "DATA",
      [
        "storage",
        "0030bc54",
        "switchD_00b63360::switchdataD_0030bc54",
        "byte"
      ]
    ],
    [
      "00b63360",
      "COMPUTED_JUMP",
      [
        "local_branch",
        "00b633f0"
      ]
    ],
    [
      "00b6339c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b63464"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b63/00b63284.md#insn-00b63300) · [`00b63324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b63/00b63284.md#insn-00b63324) · [`00b63330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b63/00b63284.md#insn-00b63330)
- 新版 `00b633c0`（命令位置の公開資料なし）

~~~diff
- 00b63300 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b63300 ["CBRANCH", null, ["local:b28:8", "tmp:0:1"]]
- 00b63300 bytes 41060054
- 00b63324 ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
- 00b63324 ["CBRANCH", null, ["local:b44:8", "tmp:0:1"]]
+ 00b633c0 ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
+ 00b633c0 ["CBRANCH", null, ["local:b48:8", "tmp:0:1"]]
- 00b63324 bytes b50900b4
+ 00b633c0 bytes b50900b4
- 00b63330 ["CBRANCH", null, ["local:b18:8", "register:101:1"]]
- 00b63330 bytes e0000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6efe145b8577f8bfa7a3b0d99703ef2a"></a>

### [`00b63540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b63/00b63540.md) → [`00b635dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b63/00b635dc.md) _ZNK8firebase7Variant14mutable_stringEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bde0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bde0.md) · 呼出先 3件 [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b5c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5c0.md)
- 新版 呼出元 1件 [`00c5beb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5beb0.md) · 呼出先 3件 [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b690.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 73.44% / 新版 73.44%

CFGの説明率　旧版 65.22% / 新版 62.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b635b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b635c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b63650"
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
      "00b635f8",
      "READ",
      [
        "storage",
        "00c9b7f0",
        null,
        "pointer"
      ]
    ],
    [
      "00b63620",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b635b8"
      ]
    ],
    [
      "unmatched:00b63590",
      "PARAM",
      [
        "storage",
        "002be63f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b635f8",
      "READ",
      [
        "storage",
        "00c9b8c0",
        null,
        "pointer"
      ]
    ],
    [
      "00b63620",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b63654"
      ]
    ],
    [
      "00b6362c",
      "PARAM",
      [
        "storage",
        "002be5eb",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b63/00b63540.md#insn-00b63594) · [`00b635a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b63/00b63540.md#insn-00b635a8) · [`00b635b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b63/00b63540.md#insn-00b635b4)

~~~diff
- 00b63594 ["INT_ADD", "register:40f0:8", ["const:b63594:8", "const:4:8"]]
- 00b63594 ["CALL", null, ["callee:00c5ad70:8"]]
- 00b63594 bytes c3dd0394
- 00b635a8 ["INT_ADD", "register:40f0:8", ["const:b635a8:8", "const:4:8"]]
- 00b635a8 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b635a8 bytes 96de0394
- 00b635b4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b635b4 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00b635b4 ["CBRANCH", null, ["local:b10:8", "tmp:1:1"]]
- 00b635b4 bytes a8010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7786a6b33067878162c1ad6d4169366"></a>

### [`00b63640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b63/00b63640.md) → [`00b636dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b63/00b636dc.md) _ZN8firebase7Variant16set_mutable_blobEPKvm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5bdd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bdd0.md) · 呼出先 5件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a830.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5be50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be50.md)
- 新版 呼出元 1件 [`00c5bea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bea0.md) · 呼出先 5件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a900.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5bf20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf20.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 86.49% / 新版 86.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b63738",
      "incomplete_value": false,
      "site": "00b6373c",
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
            "const:df4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6369c",
      "incomplete_value": false,
      "site": "00b636a0",
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
            "const:e48:8"
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
      "definition_site": "00b63750",
      "incomplete_value": false,
      "site": "00b63758",
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
            "const:159:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b636b4",
      "incomplete_value": false,
      "site": "00b636bc",
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
            "const:1b5:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b63754",
      "incomplete_value": true,
      "site": "00b63758",
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
              "LOAD",
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b636b8",
      "incomplete_value": true,
      "site": "00b636bc",
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
              "LOAD",
              "INT_LEFT"
            ]
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
      "00b63738",
      "PARAM",
      [
        "storage",
        "002bbe48",
        null,
        "string"
      ]
    ],
    [
      "00b63748",
      "READ",
      [
        "storage",
        "00c9b7f0",
        null,
        "pointer"
      ]
    ],
    [
      "00b63750",
      "PARAM",
      [
        "storage",
        "002a71b5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b63738",
      "PARAM",
      [
        "storage",
        "002bbdf4",
        null,
        "string"
      ]
    ],
    [
      "00b63748",
      "READ",
      [
        "storage",
        "00c9b8c0",
        null,
        "pointer"
      ]
    ],
    [
      "00b63750",
      "PARAM",
      [
        "storage",
        "002a7159",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b636a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b63/00b63640.md#insn-00b636a0) · [`00b636bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b63/00b63640.md#insn-00b636bc) · [`00b63660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b63/00b63640.md#insn-00b63660)
- 新版 `00b6373c`（命令位置の公開資料なし） · `00b63758`（命令位置の公開資料なし） · `00b636fc`（命令位置の公開資料なし）

~~~diff
- 00b636a0 ["INT_ADD", "register:40f0:8", ["const:b636a0:8", "const:4:8"]]
- 00b636a0 ["CALL", null, ["callee:00c5ad70:8"]]
+ 00b6373c ["INT_ADD", "register:40f0:8", ["const:b6373c:8", "const:4:8"]]
+ 00b6373c ["CALL", null, ["callee:00c5ad70:8"]]
- 00b636a0 bytes 80dd0394
+ 00b6373c bytes 8ddd0394
- 00b636bc ["INT_ADD", "register:40f0:8", ["const:b636bc:8", "const:4:8"]]
- 00b636bc ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b63758 ["INT_ADD", "register:40f0:8", ["const:b63758:8", "const:4:8"]]
+ 00b63758 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b636bc bytes 51de0394
+ 00b63758 bytes 5ede0394
- 00b63660 ["INT_ADD", "register:40f0:8", ["const:b63660:8", "const:4:8"]]
- 00b63660 ["CALL", null, ["callee:00c5bf20:8"]]
+ 00b636fc ["INT_ADD", "register:40f0:8", ["const:b636fc:8", "const:4:8"]]
+ 00b636fc ["CALL", null, ["callee:00c5bf20:8"]]
- 00b63660 bytes fce10394
+ 00b636fc bytes 09e20394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-daed272cd76e748fb32554d3a58cc604"></a>

### [`00b636d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b63/00b636d4.md) → [`00b63770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b63/00b63770.md) _ZN8firebase7VariantaSEOS0_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5a840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a840.md) · 呼出先 3件 [`00c5a830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a830.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 1件 [`00c5a910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a910.md) · 呼出先 3件 [`00c5a900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a900.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6381c",
      "incomplete_value": false,
      "site": "00b63820",
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
            "const:df4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63780",
      "incomplete_value": false,
      "site": "00b63784",
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
            "const:e48:8"
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
      "definition_site": "00b63834",
      "incomplete_value": false,
      "site": "00b6383c",
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
            "const:159:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63798",
      "incomplete_value": false,
      "site": "00b637a0",
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
            "const:1b5:8"
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
      "definition_site": "00b63838",
      "incomplete_value": true,
      "site": "00b6383c",
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
              "LOAD",
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6379c",
      "incomplete_value": true,
      "site": "00b637a0",
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
              "LOAD",
              "INT_LEFT"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b637c4",
      "DATA",
      [
        "storage",
        "0030bc2a",
        "switchD_00b63730::switchdataD_0030bc2a",
        "byte"
      ]
    ],
    [
      "00b6381c",
      "PARAM",
      [
        "storage",
        "002bbe48",
        null,
        "string"
      ]
    ],
    [
      "00b6382c",
      "READ",
      [
        "storage",
        "00c9b7f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b637c4",
      "DATA",
      [
        "storage",
        "0030bc6a",
        "switchD_00b637cc::switchdataD_0030bc6a",
        "byte"
      ]
    ],
    [
      "00b6381c",
      "PARAM",
      [
        "storage",
        "002bbdf4",
        null,
        "string"
      ]
    ],
    [
      "00b6382c",
      "READ",
      [
        "storage",
        "00c9b8c0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b63/00b636d4.md#insn-00b63784) · [`00b637a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b63/00b636d4.md#insn-00b637a0) · [`00b637d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b63/00b636d4.md#insn-00b637d4)
- 新版 `00b63820`（命令位置の公開資料なし） · `00b6383c`（命令位置の公開資料なし） · `00b63870`（命令位置の公開資料なし）

~~~diff
- 00b63784 ["INT_ADD", "register:40f0:8", ["const:b63784:8", "const:4:8"]]
- 00b63784 ["CALL", null, ["callee:00c5ad70:8"]]
+ 00b63820 ["INT_ADD", "register:40f0:8", ["const:b63820:8", "const:4:8"]]
+ 00b63820 ["CALL", null, ["callee:00c5ad70:8"]]
- 00b63784 bytes 47dd0394
+ 00b63820 bytes 54dd0394
- 00b637a0 ["INT_ADD", "register:40f0:8", ["const:b637a0:8", "const:4:8"]]
- 00b637a0 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b6383c ["INT_ADD", "register:40f0:8", ["const:b6383c:8", "const:4:8"]]
+ 00b6383c ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b637a0 bytes 18de0394
+ 00b6383c bytes 25de0394
- 00b637d4 ["INT_ADD", "register:40f0:8", ["const:b637d4:8", "const:4:8"]]
- 00b637d4 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b63870 ["INT_ADD", "register:40f0:8", ["const:b63870:8", "const:4:8"]]
+ 00b63870 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b637d4 bytes 0bde0394
+ 00b63870 bytes 18de0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3c2d93ae3339d6808da7729e8da0476"></a>

### [`00b637ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b63/00b637ec.md) → [`00b63888`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b63/00b63888.md) _ZNK8firebase7VarianteqERKS0_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b637ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b63/00b637ec.md) [`00c5bdf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bdf0.md) · 呼出先 5件 [`00b637ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b63/00b637ec.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b850.md)
- 新版 呼出元 2件 [`00b63888`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b63/00b63888.md) [`00c5bec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bec0.md) · 呼出先 5件 [`00b63888`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b63/00b63888.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b920.md)

変更の種類 call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 81.20% / 新版 81.20%

CFGの説明率　旧版 95.14% / 新版 95.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 29件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b63a08"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b63aa4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b63990",
      "incomplete_value": false,
      "site": "00b63994",
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
            "const:df4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b638f4",
      "incomplete_value": false,
      "site": "00b638f8",
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
            "const:e48:8"
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
      "00b63920",
      "DATA",
      [
        "storage",
        "0030bc35",
        "switchD_00b63890::switchdataD_0030bc35",
        "byte"
      ]
    ],
    [
      "00b6397c",
      "READ",
      [
        "storage",
        "00c9b7f0",
        null,
        "pointer"
      ]
    ],
    [
      "00b63990",
      "PARAM",
      [
        "storage",
        "002bbe48",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b63920",
      "DATA",
      [
        "storage",
        "0030bc75",
        "switchD_00b6392c::switchdataD_0030bc75",
        "byte"
      ]
    ],
    [
      "00b6397c",
      "READ",
      [
        "storage",
        "00c9b8c0",
        null,
        "pointer"
      ]
    ],
    [
      "00b63990",
      "PARAM",
      [
        "storage",
        "002bbdf4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b638f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b63/00b637ec.md#insn-00b638f8) · [`00b6390c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b63/00b637ec.md#insn-00b6390c) · [`00b6392c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b63/00b637ec.md#insn-00b6392c)
- 新版 `00b63994`（命令位置の公開資料なし） · `00b639a8`（命令位置の公開資料なし） · `00b639c8`（命令位置の公開資料なし）

~~~diff
- 00b638f8 ["INT_ADD", "register:40f0:8", ["const:b638f8:8", "const:4:8"]]
- 00b638f8 ["CALL", null, ["callee:00c5ad70:8"]]
+ 00b63994 ["INT_ADD", "register:40f0:8", ["const:b63994:8", "const:4:8"]]
+ 00b63994 ["CALL", null, ["callee:00c5ad70:8"]]
- 00b638f8 bytes eadc0394
+ 00b63994 bytes f7dc0394
- 00b6390c ["INT_ADD", "register:40f0:8", ["const:b6390c:8", "const:4:8"]]
- 00b6390c ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b639a8 ["INT_ADD", "register:40f0:8", ["const:b639a8:8", "const:4:8"]]
+ 00b639a8 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b6390c bytes bddd0394
+ 00b639a8 bytes cadd0394
- 00b6392c ["INT_ADD", "register:40f0:8", ["const:b6392c:8", "const:4:8"]]
- 00b6392c ["CALL", null, ["callee:00c5ad70:8"]]
+ 00b639c8 ["INT_ADD", "register:40f0:8", ["const:b639c8:8", "const:4:8"]]
+ 00b639c8 ["CALL", null, ["callee:00c5ad70:8"]]
- 00b6392c bytes dddc0394
+ 00b639c8 bytes eadc0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24cc7bf7f9e04e342c1ff28c74838584"></a>

### [`00b63d68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b63/00b63d68.md) → [`00b63e04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b63/00b63e04.md) _ZNK8firebase7VariantltERKS0_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b5a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5a0.md) · 呼出先 5件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b850.md) [`00c5bdf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bdf0.md)
- 新版 呼出元 1件 [`00c5b670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b670.md) · 呼出先 5件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b920.md) [`00c5bec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bec0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 74.40% / 新版 74.40%

CFGの説明率　旧版 68.95% / 新版 68.95%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 31件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b63f78"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b63fb4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b641e4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b63e28",
      "READ",
      [
        "storage",
        "00c9b7f0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b63e3c",
      "DATA",
      [
        "storage",
        "0030bc42",
        "switchD_00b63e44::switchdataD_0030bc42",
        "ushort"
      ]
    ],
    [
      "00b63ef4",
      "PARAM",
      [
        "storage",
        "002ae1fb",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b63e28",
      "READ",
      [
        "storage",
        "00c9b8c0",
        null,
        "pointer"
      ]
    ],
    [
      "00b63ed8",
      "DATA",
      [
        "storage",
        "0030bc82",
        "switchD_00b63ee0::switchdataD_0030bc82",
        "ushort"
      ]
    ],
    [
      "00b63ef4",
      "PARAM",
      [
        "storage",
        "002ae19f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b63/00b63d68.md#insn-00b63f34) · [`00b63f68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b63/00b63d68.md#insn-00b63f68) · [`00b63f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b63/00b63d68.md#insn-00b63f78)
- 新版 `00b64004`（命令位置の公開資料なし）

~~~diff
- 00b63f34 ["INT_ADD", "register:40f0:8", ["const:b63f34:8", "const:4:8"]]
- 00b63f34 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b63f34 bytes 33dc0394
- 00b63f68 ["INT_ADD", "register:40f0:8", ["const:b63f68:8", "const:4:8"]]
- 00b63f68 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b64004 ["INT_ADD", "register:40f0:8", ["const:b64004:8", "const:4:8"]]
+ 00b64004 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b63f68 bytes 26dc0394
+ 00b64004 bytes 33dc0394
- 00b63f78 ["CBRANCH", null, ["local:b57:8", "register:101:1"]]
- 00b63f78 bytes 400f0054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21e73a2ca0d75503e27adff9da9d9633"></a>

### [`00b645d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b64/00b645d4.md) → [`00b64670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b64670.md) _ZNK8firebase7Variant14assert_is_typeENS0_4TypeE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5ab00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ab00.md) · 呼出先 2件 [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 1件 [`00c5abd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5abd0.md) · 呼出先 2件 [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
      "definition_site": "00b6469c",
      "incomplete_value": false,
      "site": "00b646a4",
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
            "const:19f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b64600",
      "incomplete_value": false,
      "site": "00b64608",
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
            "const:1fb:8"
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
      "00b6469c",
      "PARAM",
      [
        "storage",
        "002ae1fb",
        null,
        "string"
      ]
    ],
    [
      "00b646b0",
      "READ",
      [
        "storage",
        "00c9b7f0",
        null,
        "pointer"
      ]
    ],
    [
      "00b646bc",
      "PARAM",
      [
        "storage",
        "002af3b7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6469c",
      "PARAM",
      [
        "storage",
        "002ae19f",
        null,
        "string"
      ]
    ],
    [
      "00b646b0",
      "READ",
      [
        "storage",
        "00c9b8c0",
        null,
        "pointer"
      ]
    ],
    [
      "00b646bc",
      "PARAM",
      [
        "storage",
        "002af35b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b64608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b64/00b645d4.md#insn-00b64608) · [`00b64600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b64/00b645d4.md#insn-00b64600) · [`00b64614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b64/00b645d4.md#insn-00b64614)
- 新版 `00b646a4`（命令位置の公開資料なし） · `00b6469c`（命令位置の公開資料なし） · `00b646b0`（命令位置の公開資料なし）

~~~diff
- 00b64608 ["INT_ADD", "register:40f0:8", ["const:b64608:8", "const:4:8"]]
- 00b64608 ["CALL", null, ["callee:00c5ad70:8"]]
+ 00b646a4 ["INT_ADD", "register:40f0:8", ["const:b646a4:8", "const:4:8"]]
+ 00b646a4 ["CALL", null, ["callee:00c5ad70:8"]]
- 00b64608 bytes a6d90394
+ 00b646a4 bytes b3d90394
- 00b64600 ["COPY", "tmp:0:8", ["const:1fb:8"]]
- 00b64600 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b64600 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b64600 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b6469c ["COPY", "tmp:0:8", ["const:19f:8"]]
+ 00b6469c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6469c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6469c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b64600 bytes 00ec0791
+ 00b6469c bytes 007c0691
- 00b64614 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:7f0:8"]]
- 00b64614 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b646b0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:8c0:8"]]
+ 00b646b0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00b64614 bytes 29f943f9
+ 00b646b0 bytes 296144f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7217725aec814f762c66698bfbc2214c"></a>

### [`00b64634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b64/00b64634.md) → [`00b646d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b646d0.md) _ZNK8firebase7Variant18assert_is_not_typeENS0_4TypeE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

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
      "definition_site": "00b646f8",
      "incomplete_value": false,
      "site": "00b64700",
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
            "const:19f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6465c",
      "incomplete_value": false,
      "site": "00b64664",
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
            "const:1fb:8"
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
      "00b646f8",
      "PARAM",
      [
        "storage",
        "002ae1fb",
        null,
        "string"
      ]
    ],
    [
      "00b64708",
      "READ",
      [
        "storage",
        "00c9b7f0",
        null,
        "pointer"
      ]
    ],
    [
      "00b64714",
      "PARAM",
      [
        "storage",
        "002a95ba",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b646f8",
      "PARAM",
      [
        "storage",
        "002ae19f",
        null,
        "string"
      ]
    ],
    [
      "00b64708",
      "READ",
      [
        "storage",
        "00c9b8c0",
        null,
        "pointer"
      ]
    ],
    [
      "00b64714",
      "PARAM",
      [
        "storage",
        "002a95e9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b64664`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b64/00b64634.md#insn-00b64664) · [`00b6465c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b64/00b64634.md#insn-00b6465c) · [`00b6466c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b64/00b64634.md#insn-00b6466c)
- 新版 `00b64700`（命令位置の公開資料なし） · `00b646f8`（命令位置の公開資料なし） · `00b64708`（命令位置の公開資料なし）

~~~diff
- 00b64664 ["INT_ADD", "register:40f0:8", ["const:b64664:8", "const:4:8"]]
- 00b64664 ["CALL", null, ["callee:00c5ad70:8"]]
+ 00b64700 ["INT_ADD", "register:40f0:8", ["const:b64700:8", "const:4:8"]]
+ 00b64700 ["CALL", null, ["callee:00c5ad70:8"]]
- 00b64664 bytes 8fd90394
+ 00b64700 bytes 9cd90394
- 00b6465c ["COPY", "tmp:0:8", ["const:1fb:8"]]
- 00b6465c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6465c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6465c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b646f8 ["COPY", "tmp:0:8", ["const:19f:8"]]
+ 00b646f8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b646f8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b646f8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6465c bytes 00ec0791
+ 00b646f8 bytes 007c0691
- 00b6466c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:7f0:8"]]
- 00b6466c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b64708 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:8c0:8"]]
+ 00b64708 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6466c bytes 08f943f9
+ 00b64708 bytes 086144f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66c5253bf689278aee650c3b3a9ff587"></a>

### [`00b64750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b64/00b64750.md) → [`00b647ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b647ec.md) _ZNK8firebase7Variant8AsStringEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5ab10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ab10.md) · 呼出先 10件 [`00b648f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b64/00b648f4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)
- 新版 呼出元 1件 [`00c5abe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5abe0.md) · 呼出先 10件 [`00b64990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b64990.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 62.50% / 新版 62.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6487c",
      "incomplete_value": false,
      "site": "00b64884",
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
            "const:bb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b647e0",
      "incomplete_value": false,
      "site": "00b647e8",
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
            "const:117:8"
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
      "definition_site": "00b648b0",
      "incomplete_value": false,
      "site": "00b648b8",
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
            "const:61b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b64814",
      "incomplete_value": false,
      "site": "00b6481c",
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
            "const:5ec:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b648e8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b64830",
      "DATA",
      [
        "storage",
        "0030bc58",
        "switchD_00b647a0::switchdataD_0030bc58",
        "byte"
      ]
    ],
    [
      "00b6483c",
      "COMPUTED_JUMP",
      [
        "local_branch",
        "unmatched:00b647d8"
      ]
    ],
    [
      "00b6483c",
      "COMPUTED_JUMP",
      [
        "local_branch",
        "unmatched:00b6480c"
      ]
    ]
  ],
  "added": [
    [
      "00b64830",
      "DATA",
      [
        "storage",
        "0030bc98",
        "switchD_00b6483c::switchdataD_0030bc98",
        "byte"
      ]
    ],
    [
      "00b6483c",
      "COMPUTED_JUMP",
      [
        "local_branch",
        "00b64874"
      ]
    ],
    [
      "00b6483c",
      "COMPUTED_JUMP",
      [
        "local_branch",
        "00b648a8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b647e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b64/00b64750.md#insn-00b647e8) · [`00b6481c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b64/00b64750.md#insn-00b6481c) · [`00b648e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b64/00b64750.md#insn-00b648e8)
- 新版 `00b64884`（命令位置の公開資料なし） · `00b648b8`（命令位置の公開資料なし）

~~~diff
- 00b647e8 ["INT_ADD", "register:40f0:8", ["const:b647e8:8", "const:4:8"]]
- 00b647e8 ["CALL", null, ["callee:00b64990:8"]]
+ 00b64884 ["INT_ADD", "register:40f0:8", ["const:b64884:8", "const:4:8"]]
+ 00b64884 ["CALL", null, ["callee:00b64990:8"]]
- 00b647e8 bytes 43000094
+ 00b64884 bytes 43000094
- 00b6481c ["INT_ADD", "register:40f0:8", ["const:b6481c:8", "const:4:8"]]
- 00b6481c ["CALL", null, ["callee:00b64990:8"]]
+ 00b648b8 ["INT_ADD", "register:40f0:8", ["const:b648b8:8", "const:4:8"]]
+ 00b648b8 ["CALL", null, ["callee:00b64990:8"]]
- 00b6481c bytes 36000094
+ 00b648b8 bytes 36000094
- 00b648e8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b648e8 ["RETURN", null, ["register:0:8"]]
- 00b648e8 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e59ef3fa9c91b48b15723e7d9f49cd2f"></a>

### [`00b64a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b64/00b64a80.md) → [`00b64b1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b64b1c.md) _ZNK8firebase7Variant8AsDoubleEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c585c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c585c0.md) [`00c5a830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a830.md) [`00c5a8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8f0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58690.md) [`00c5a900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a900.md) [`00c5a9c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a9c0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 35.71% / 新版 37.04%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b64bcc",
      "incomplete_value": true,
      "site": "00b64bd4",
      "value": [
        "live",
        "register:4098:8"
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
      "definition_site": "00b64bc8",
      "incomplete_value": false,
      "site": "00b64bd4",
      "value": [
        "leaf",
        "const:2:8"
      ]
    },
    "old": null,
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b64b74"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b64ab0",
      "DATA",
      [
        "storage",
        "0030bc6c",
        "switchD_00b64abc::switchdataD_0030bc6c",
        "byte"
      ]
    ]
  ],
  "added": [
    [
      "00b64b4c",
      "DATA",
      [
        "storage",
        "0030bcac",
        "switchD_00b64b58::switchdataD_0030bcac",
        "byte"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b64b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b64/00b64a80.md#insn-00b64b38) · [`00b64b74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b64/00b64a80.md#insn-00b64b74)
- 新版 `00b64bd4`（命令位置の公開資料なし） · `00b64b74`（命令位置の公開資料なし）

~~~diff
- 00b64b38 ["INT_ADD", "register:40f0:8", ["const:b64b38:8", "const:4:8"]]
- 00b64b38 ["CALL", null, ["callee:00c5a900:8"]]
+ 00b64bd4 ["INT_ADD", "register:40f0:8", ["const:b64bd4:8", "const:4:8"]]
+ 00b64bd4 ["CALL", null, ["callee:00c5a900:8"]]
- 00b64b38 bytes 3ed70394
+ 00b64bd4 bytes 4bd70394
- 00b64b74 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b64b74 ["RETURN", null, ["register:0:8"]]
- 00b64b74 bytes c0035fd6
+ 00b64b74 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00b64b74 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b64b74 ["INT_ZEXT", "register:4048:8", ["tmp:1:1"]]
+ 00b64b74 bytes 09014039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6e00859ed3594ca802bfeffea7341b0"></a>

### [`00b64b78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b64/00b64b78.md) → [`00b64c14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b64c14.md) _ZNK8firebase7Variant6AsBoolEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a830.md) [`00c5bdf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bdf0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a900.md) [`00c5bec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bec0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 72.22% / 新版 72.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b64ba0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b64ba4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b64ba8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b64ba0",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b64ba4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b64ba8",
      "WRITE",
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
      "00b64c3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00b64c40",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b64c44",
      "WRITE",
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

- 旧版 [`00b64ba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b64/00b64b78.md#insn-00b64ba0) · [`00b64ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b64/00b64b78.md#insn-00b64ba4) · [`00b64ba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b64/00b64b78.md#insn-00b64ba8)

~~~diff
- 00b64ba0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b64ba0 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffd8:8"]]
- 00b64ba0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b64ba0 bytes a8831df8
- 00b64ba4 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b64ba4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b64ba4 ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffffc0:8"]]
- 00b64ba4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:4"]]
- 00b64ba4 bytes bf031cb8
- 00b64ba8 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00b64ba8 ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 00b64ba8 ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffffc8:8"]]
- 00b64ba8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:8"]]
- 00b64ba8 bytes bf831cf8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5e8d77c5184d16df1a98793caa55cb0"></a>

### [`00b64ddc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b64/00b64ddc.md) → [`00b64e78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b64e78.md) _ZN8firebase7Variant8TypeNameENS0_4TypeE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5aff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aff0.md) · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 1件 [`00c5b0c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0c0.md) · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate, store_destination

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b64ea4",
      "incomplete_value": true,
      "site": "00b64ea4",
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
            "const:14c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b64e08",
      "incomplete_value": true,
      "site": "00b64e08",
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
            "const:4c:8"
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
      "definition_site": "00b64ebc",
      "incomplete_value": false,
      "site": "00b64ec0",
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
            "const:621:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b64e20",
      "incomplete_value": false,
      "site": "00b64e24",
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
            "const:5f2:8"
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
      "definition_site": "00b64ed0",
      "incomplete_value": true,
      "site": "00b64ed8",
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
              "LOAD",
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b64e34",
      "incomplete_value": true,
      "site": "00b64e3c",
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
              "LOAD",
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
      "00b64e88",
      "READ",
      [
        "storage",
        "0112604c",
        null,
        "undefined1"
      ]
    ],
    [
      "00b64ea4",
      "WRITE",
      [
        "storage",
        "0112604c",
        null,
        "undefined1"
      ]
    ],
    [
      "00b64ebc",
      "PARAM",
      [
        "storage",
        "002a95f2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b64e88",
      "READ",
      [
        "storage",
        "0112614c",
        null,
        "undefined1"
      ]
    ],
    [
      "00b64ea4",
      "WRITE",
      [
        "storage",
        "0112614c",
        null,
        "undefined1"
      ]
    ],
    [
      "00b64ebc",
      "PARAM",
      [
        "storage",
        "002a9621",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b64e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b64/00b64ddc.md#insn-00b64e08) · [`00b64e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b64/00b64ddc.md#insn-00b64e24) · [`00b64dec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b64/00b64ddc.md#insn-00b64dec)
- 新版 `00b64ea4`（命令位置の公開資料なし） · `00b64ec0`（命令位置の公開資料なし） · `00b64e88`（命令位置の公開資料なし）

~~~diff
- 00b64e08 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00b64e08 ["INT_ADD", "tmp:1:8", ["register:4048:8", "const:4c:8"]]
- 00b64e08 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b64ea4 ["COPY", "tmp:0:4", ["register:4040:4"]]
+ 00b64ea4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "const:14c:8"]]
+ 00b64ea4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b64e08 bytes 28310139
+ 00b64ea4 bytes 28310539
- 00b64e24 ["INT_ADD", "register:40f0:8", ["const:b64e24:8", "const:4:8"]]
- 00b64e24 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b64ec0 ["INT_ADD", "register:40f0:8", ["const:b64ec0:8", "const:4:8"]]
+ 00b64ec0 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b64e24 bytes 77d80394
+ 00b64ec0 bytes 84d80394
- 00b64dec ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:4c:8"]]
- 00b64dec ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b64dec ["INT_ZEXT", "register:4050:8", ["tmp:1:1"]]
+ 00b64e88 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:14c:8"]]
+ 00b64e88 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b64e88 ["INT_ZEXT", "register:4050:8", ["tmp:1:1"]]
- 00b64dec bytes 2a314139
+ 00b64e88 bytes 2a314539
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c98074329f02bc6885c9bb419355be46"></a>

### [`00b64e40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b64/00b64e40.md) → [`00b64edc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b64edc.md) _ZNSt6__ndk16vectorIN8firebase7VariantENS_9allocatorIS2_EEE6assignIPS2_EENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_constru

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5be30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be30.md) · 呼出先 5件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5a830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a830.md) [`00c5a8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8f0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 1件 [`00c5bf00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf00.md) · 呼出先 5件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5a900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a900.md) [`00c5a9c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a9c0.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 79.51% / 新版 79.51%

CFGの説明率　旧版 43.75% / 新版 43.75%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 4件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b64fe0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b6507c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b64e90"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b64e90",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b64f60"
      ]
    ],
    [
      "unmatched:00b64fb4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b65060"
      ]
    ],
    [
      "unmatched:00b64fe4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b650a4"
      ]
    ]
  ],
  "added": [
    [
      "00b64f2c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b64f60"
      ]
    ],
    [
      "00b65050",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b65060"
      ]
    ],
    [
      "00b65080",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b650a4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b64e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b64/00b64e40.md#insn-00b64e90) · [`00b64eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b64/00b64e40.md#insn-00b64eb0)
- 新版 `00b64f4c`（命令位置の公開資料なし） · `00b64f2c`（命令位置の公開資料なし）

~~~diff
- 00b64e90 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b64e90 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00b64e90 ["CBRANCH", null, ["local:b9:8", "tmp:1:1"]]
- 00b64e90 bytes a9010054
- 00b64eb0 ["INT_ADD", "register:40f0:8", ["const:b64eb0:8", "const:4:8"]]
- 00b64eb0 ["CALL", null, ["callee:00c5a900:8"]]
+ 00b64f4c ["INT_ADD", "register:40f0:8", ["const:b64f4c:8", "const:4:8"]]
+ 00b64f4c ["CALL", null, ["callee:00c5a900:8"]]
- 00b64eb0 bytes 60d60394
+ 00b64f4c bytes 6dd60394
+ 00b64f2c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00b64f2c ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
+ 00b64f2c ["CBRANCH", null, ["local:b9:8", "tmp:1:1"]]
+ 00b64f2c bytes a9010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c48d5c112c210e35c63dd9bf0d4f02d7"></a>

### [`00b65028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65028.md) → [`00b650c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b650c4.md) _ZNSt6__ndk16__treeINS_12__value_typeIN8firebase7VariantES3_EENS_19__map_value_compareIS3_S4_NS_4lessIS3_EELb1EEENS_9allocatorIS4_EEE14__ass

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5be00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be00.md) · 呼出先 5件 [`00c5a8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8f0.md) [`00c5b5a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5a0.md) [`00c5b5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5e0.md) [`00c5be10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be10.md) [`00c5be20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be20.md)
- 新版 呼出元 1件 [`00c5bed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bed0.md) · 呼出先 5件 [`00c5a9c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a9c0.md) [`00c5b670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b670.md) [`00c5b6b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b6b0.md) [`00c5bee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bee0.md) [`00c5bef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bef0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 61.11% / 新版 61.68%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_condition` 4件, `unresolved_branch_alignment` 4件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b65054"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b65080"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b650d8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b65054",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b65340"
      ]
    ],
    [
      "unmatched:00b65080",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b65154"
      ]
    ],
    [
      "unmatched:00b650d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b650d0"
      ]
    ]
  ],
  "added": [
    [
      "00b650f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b65340"
      ]
    ],
    [
      "00b6511c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b65154"
      ]
    ],
    [
      "00b6517c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6516c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65028.md#insn-00b65054) · [`00b65080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65028.md#insn-00b65080) · [`00b650d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65028.md#insn-00b650d8)

~~~diff
- 00b65054 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b65054 ["CBRANCH", null, ["local:b57:8", "tmp:0:1"]]
- 00b65054 bytes 881200b4
- 00b65080 ["INT_EQUAL", "tmp:0:1", ["register:40b0:8", "const:0:8"]]
- 00b65080 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00b65080 bytes d60100b4
- 00b650d8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b650d8 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 00b650d8 bytes c8ffffb5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e5599d13200df04090126b158106b10"></a>

### [`00b65454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65454.md) → [`00b654f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b654f0.md) _ZN8firebase5MutexC1ENS0_4ModeE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ac80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac80.md) · 呼出先 6件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5be80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be80.md) [`00c5be90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be90.md) [`00c5bea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bea0.md)
- 新版 呼出元 2件 [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ad50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad50.md) · 呼出先 6件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5bf50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf50.md) [`00c5bf60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf60.md) [`00c5bf70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf70.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, operands_and_dependencies, operation_sequence

命令の説明率　旧版 91.49% / 新版 91.49%

CFGの説明率　旧版 58.82% / 新版 58.82%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b65528",
      "incomplete_value": false,
      "site": "00b6552c",
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
            "const:bf:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6548c",
      "incomplete_value": false,
      "site": "00b65490",
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
            "const:11b:8"
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
      "definition_site": "00b65498",
      "incomplete_value": true,
      "site": "00b654a0",
      "value": [
        "live",
        "register:8:8"
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
      "definition_site": "00b6549c",
      "incomplete_value": false,
      "site": "00b654a0",
      "value": [
        "leaf",
        "const:1:8"
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
      "00b65528",
      "PARAM",
      [
        "storage",
        "002ad11b",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b654ac",
      "PARAM",
      [
        "storage",
        "002ad11b",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b654c8",
      "PARAM",
      [
        "storage",
        "002ad11b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b65528",
      "PARAM",
      [
        "storage",
        "002ad0bf",
        null,
        "string"
      ]
    ],
    [
      "00b65548",
      "PARAM",
      [
        "storage",
        "002ad0bf",
        null,
        "string"
      ]
    ],
    [
      "00b65564",
      "PARAM",
      [
        "storage",
        "002ad0bf",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65454.md#insn-00b65490) · [`00b654a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65454.md#insn-00b654a0) · [`00b654b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65454.md#insn-00b654b0)
- 新版 `00b6552c`（命令位置の公開資料なし） · `00b6553c`（命令位置の公開資料なし） · `00b6554c`（命令位置の公開資料なし）

~~~diff
- 00b65490 ["INT_ADD", "register:40f0:8", ["const:b65490:8", "const:4:8"]]
- 00b65490 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b6552c ["INT_ADD", "register:40f0:8", ["const:b6552c:8", "const:4:8"]]
+ 00b6552c ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b65490 bytes dcd60394
+ 00b6552c bytes e9d60394
- 00b654a0 ["INT_ADD", "register:40f0:8", ["const:b654a0:8", "const:4:8"]]
- 00b654a0 ["CALL", null, ["callee:00c5bf80:8"]]
+ 00b6553c ["INT_ADD", "register:40f0:8", ["const:b6553c:8", "const:4:8"]]
+ 00b6553c ["CALL", null, ["callee:00c5bf80:8"]]
- 00b654a0 bytes 84da0394
+ 00b6553c bytes 91da0394
- 00b654b0 ["INT_ADD", "register:40f0:8", ["const:b654b0:8", "const:4:8"]]
- 00b654b0 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b6554c ["INT_ADD", "register:40f0:8", ["const:b6554c:8", "const:4:8"]]
+ 00b6554c ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b654b0 bytes d4d60394
+ 00b6554c bytes e1d60394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5abb8e279fa4615063d8cb7b246eaac0"></a>

### [`00b65590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65590.md) → [`00b6562c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b6562c.md) _ZN8firebase3app19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEENS_4util16Clas

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
      "definition_site": "00b65658",
      "incomplete_value": true,
      "site": "00b65658",
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
            "const:150:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b655bc",
      "incomplete_value": true,
      "site": "00b655bc",
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
            "const:50:8"
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
      "definition_site": "00b65640",
      "incomplete_value": true,
      "site": "00b65640",
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
      "definition_site": "00b655a4",
      "incomplete_value": true,
      "site": "00b655a4",
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
      "definition_site": "00b6564c",
      "incomplete_value": false,
      "site": "00b65650",
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
            "const:ceb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b655b0",
      "incomplete_value": false,
      "site": "00b655b4",
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
            "const:cab:8"
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
      "00b6563c",
      "READ",
      [
        "storage",
        "01126050",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6564c",
      "PARAM",
      [
        "storage",
        "002b6cab",
        null,
        "string"
      ]
    ],
    [
      "00b65658",
      "WRITE",
      [
        "storage",
        "01126050",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6563c",
      "READ",
      [
        "storage",
        "01126150",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6564c",
      "PARAM",
      [
        "storage",
        "002b6ceb",
        null,
        "string"
      ]
    ],
    [
      "00b65658",
      "WRITE",
      [
        "storage",
        "01126150",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b655b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65590.md#insn-00b655b4) · [`00b655bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65590.md#insn-00b655bc) · [`00b655a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65590.md#insn-00b655a0)
- 新版 `00b65650`（命令位置の公開資料なし） · `00b65658`（命令位置の公開資料なし） · `00b6563c`（命令位置の公開資料なし）

~~~diff
- 00b655b4 ["INT_ADD", "register:40f0:8", ["const:b655b4:8", "const:4:8"]]
- 00b655b4 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b65650 ["INT_ADD", "register:40f0:8", ["const:b65650:8", "const:4:8"]]
+ 00b65650 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b655b4 bytes 57d60394
+ 00b65650 bytes 64d60394
- 00b655bc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:50:8"]]
- 00b655bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b65658 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:150:8"]]
+ 00b65658 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b655bc bytes 602a00f9
+ 00b65658 bytes 60aa00f9
- 00b655a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:50:8"]]
- 00b655a0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6563c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:150:8"]]
+ 00b6563c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b655a0 bytes 682a40f9
+ 00b6563c bytes 68aa40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3799605725ecff145ee5be3ad9e98f2b"></a>

### [`00b655d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b655d0.md) → [`00b6566c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b6566c.md) _ZN8firebase3app19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEE

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
      "definition_site": "00b65698",
      "incomplete_value": true,
      "site": "00b65698",
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
            "const:150:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b655fc",
      "incomplete_value": true,
      "site": "00b655fc",
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
            "const:50:8"
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
      "definition_site": "00b65680",
      "incomplete_value": true,
      "site": "00b65680",
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
      "definition_site": "00b655e4",
      "incomplete_value": true,
      "site": "00b655e4",
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
      "definition_site": "00b65688",
      "incomplete_value": false,
      "site": "00b65690",
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
            "const:ceb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b655ec",
      "incomplete_value": false,
      "site": "00b655f4",
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
            "const:cab:8"
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
      "00b6567c",
      "READ",
      [
        "storage",
        "01126050",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65688",
      "PARAM",
      [
        "storage",
        "002b6cab",
        null,
        "string"
      ]
    ],
    [
      "00b65698",
      "WRITE",
      [
        "storage",
        "01126050",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6567c",
      "READ",
      [
        "storage",
        "01126150",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65688",
      "PARAM",
      [
        "storage",
        "002b6ceb",
        null,
        "string"
      ]
    ],
    [
      "00b65698",
      "WRITE",
      [
        "storage",
        "01126150",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b655f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b655d0.md#insn-00b655f4) · [`00b655fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b655d0.md#insn-00b655fc) · [`00b655e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b655d0.md#insn-00b655e0)
- 新版 `00b65690`（命令位置の公開資料なし） · `00b65698`（命令位置の公開資料なし） · `00b6567c`（命令位置の公開資料なし）

~~~diff
- 00b655f4 ["INT_ADD", "register:40f0:8", ["const:b655f4:8", "const:4:8"]]
- 00b655f4 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b65690 ["INT_ADD", "register:40f0:8", ["const:b65690:8", "const:4:8"]]
+ 00b65690 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b655f4 bytes 47d60394
+ 00b65690 bytes 54d60394
- 00b655fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:50:8"]]
- 00b655fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b65698 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:150:8"]]
+ 00b65698 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b655fc bytes 602a00f9
+ 00b65698 bytes 60aa00f9
- 00b655e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:50:8"]]
- 00b655e0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6567c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:150:8"]]
+ 00b6567c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b655e0 bytes 682a40f9
+ 00b6567c bytes 68aa40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14e9058e4b91abc111584122ab10f081"></a>

### [`00b65610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65610.md) → [`00b656ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b656ac.md) _ZN8firebase3app10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b656dc",
      "incomplete_value": true,
      "site": "00b656dc",
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
            "const:150:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65640",
      "incomplete_value": true,
      "site": "00b65640",
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
            "const:50:8"
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
      "definition_site": "00b656c0",
      "incomplete_value": true,
      "site": "00b656c0",
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
      "definition_site": "00b65624",
      "incomplete_value": true,
      "site": "00b65624",
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
      "definition_site": "00b656cc",
      "incomplete_value": false,
      "site": "00b656d4",
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
            "const:ceb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65630",
      "incomplete_value": false,
      "site": "00b65638",
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
            "const:cab:8"
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
      "00b656bc",
      "READ",
      [
        "storage",
        "01126050",
        null,
        "undefined8"
      ]
    ],
    [
      "00b656cc",
      "PARAM",
      [
        "storage",
        "002b6cab",
        null,
        "string"
      ]
    ],
    [
      "00b656dc",
      "WRITE",
      [
        "storage",
        "01126050",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b656bc",
      "READ",
      [
        "storage",
        "01126150",
        null,
        "undefined8"
      ]
    ],
    [
      "00b656cc",
      "PARAM",
      [
        "storage",
        "002b6ceb",
        null,
        "string"
      ]
    ],
    [
      "00b656dc",
      "WRITE",
      [
        "storage",
        "01126150",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65610.md#insn-00b65638) · [`00b65640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65610.md#insn-00b65640) · [`00b65620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65610.md#insn-00b65620)
- 新版 `00b656d4`（命令位置の公開資料なし） · `00b656dc`（命令位置の公開資料なし） · `00b656bc`（命令位置の公開資料なし）

~~~diff
- 00b65638 ["INT_ADD", "register:40f0:8", ["const:b65638:8", "const:4:8"]]
- 00b65638 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b656d4 ["INT_ADD", "register:40f0:8", ["const:b656d4:8", "const:4:8"]]
+ 00b656d4 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b65638 bytes 36d60394
+ 00b656d4 bytes 43d60394
- 00b65640 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:50:8"]]
- 00b65640 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b656dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:150:8"]]
+ 00b656dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65640 bytes 602a00f9
+ 00b656dc bytes 60aa00f9
- 00b65620 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:50:8"]]
- 00b65620 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b656bc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:150:8"]]
+ 00b656bc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b65620 bytes 682a40f9
+ 00b656bc bytes 68aa40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-253dcd9b633915448a1581978be7ffbc"></a>

### [`00b65654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65654.md) → [`00b656f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b656f0.md) _ZN8firebase3app10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 64.71% / 新版 64.71%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b65684"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b65720"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b65704",
      "incomplete_value": true,
      "site": "00b65704",
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
      "definition_site": "00b65668",
      "incomplete_value": true,
      "site": "00b65668",
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
      "00b65700",
      "READ",
      [
        "storage",
        "01126050",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65704",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b65688"
      ]
    ],
    [
      "unmatched:00b65670",
      "PARAM",
      [
        "storage",
        "002b6cab",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b65700",
      "READ",
      [
        "storage",
        "01126150",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65704",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b65724"
      ]
    ],
    [
      "00b6570c",
      "PARAM",
      [
        "storage",
        "002b6ceb",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65654.md#insn-00b65668) · [`00b6567c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65654.md#insn-00b6567c) · [`00b65684`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65654.md#insn-00b65684)
- 新版 `00b65704`（命令位置の公開資料なし） · `00b65718`（命令位置の公開資料なし）

~~~diff
- 00b65668 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b65668 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b65704 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b65704 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b65668 bytes 080100b5
+ 00b65704 bytes 080100b5
- 00b6567c ["INT_ADD", "register:40f0:8", ["const:b6567c:8", "const:4:8"]]
- 00b6567c ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b65718 ["INT_ADD", "register:40f0:8", ["const:b65718:8", "const:4:8"]]
+ 00b65718 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b6567c bytes 25d60394
+ 00b65718 bytes 32d60394
- 00b65684 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:50:8"]]
- 00b65684 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65684 bytes 602a00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43d34dc0ab6b782dbd0f28f8815d0f82"></a>

### [`00b656a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b656a4.md) → [`00b65740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65740.md) _ZN8firebase3app15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 40.74% / 新版 40.74%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b656a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b656a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b656a8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b656a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b656a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b656ac",
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
      "00b65740",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b65744",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b65748",
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

- 旧版 [`00b656a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b656a4.md#insn-00b656a4) · [`00b656a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b656a4.md#insn-00b656a8) · [`00b656ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b656a4.md#insn-00b656ac)

~~~diff
- 00b656a4 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b656a4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b656a4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b656a4 bytes f50f1df8
- 00b656a8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b656a8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b656a8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b656a8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b656a8 bytes f44f01a9
- 00b656ac ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b656ac ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b656ac ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b656ac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b656ac bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6da7ea1cc8e0ba2d9f358ed7054ccfc"></a>

### [`00b65780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65780.md) → [`00b6581c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b6581c.md) _ZN8firebase3app14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b6585c",
      "incomplete_value": true,
      "site": "00b6585c",
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
            "const:150:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b657c0",
      "incomplete_value": true,
      "site": "00b657c0",
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
            "const:50:8"
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
      "definition_site": "00b65838",
      "incomplete_value": true,
      "site": "00b65838",
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
      "definition_site": "00b6579c",
      "incomplete_value": true,
      "site": "00b6579c",
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
      "definition_site": "00b65840",
      "incomplete_value": false,
      "site": "00b65854",
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
            "const:ceb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b657a4",
      "incomplete_value": false,
      "site": "00b657b8",
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
            "const:cab:8"
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
      "00b65830",
      "READ",
      [
        "storage",
        "01126050",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65840",
      "PARAM",
      [
        "storage",
        "002b6cab",
        null,
        "string"
      ]
    ],
    [
      "00b6585c",
      "WRITE",
      [
        "storage",
        "01126050",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b65830",
      "READ",
      [
        "storage",
        "01126150",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65840",
      "PARAM",
      [
        "storage",
        "002b6ceb",
        null,
        "string"
      ]
    ],
    [
      "00b6585c",
      "WRITE",
      [
        "storage",
        "01126150",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b657b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65780.md#insn-00b657b8) · [`00b657c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65780.md#insn-00b657c0) · [`00b65794`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65780.md#insn-00b65794)
- 新版 `00b65854`（命令位置の公開資料なし） · `00b6585c`（命令位置の公開資料なし） · `00b65830`（命令位置の公開資料なし）

~~~diff
- 00b657b8 ["INT_ADD", "register:40f0:8", ["const:b657b8:8", "const:4:8"]]
- 00b657b8 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b65854 ["INT_ADD", "register:40f0:8", ["const:b65854:8", "const:4:8"]]
+ 00b65854 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b657b8 bytes d6d50394
+ 00b65854 bytes e3d50394
- 00b657c0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:50:8"]]
- 00b657c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6585c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:150:8"]]
+ 00b6585c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b657c0 bytes 802a00f9
+ 00b6585c bytes 80aa00f9
- 00b65794 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:50:8"]]
- 00b65794 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b65830 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:150:8"]]
+ 00b65830 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b65794 bytes 812a40f9
+ 00b65830 bytes 81aa40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-353de3a6277ad38d0747d0bd5e322093"></a>

### [`00b657f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b657f0.md) → [`00b6588c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b6588c.md) _ZN8firebase3app11GetMethodIdENS0_6MethodE

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
      "definition_site": "00b658a8",
      "incomplete_value": false,
      "site": "00b658ac",
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
      "definition_site": "00b6580c",
      "incomplete_value": false,
      "site": "00b65810",
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
      "definition_site": "00b658b8",
      "incomplete_value": true,
      "site": "00b658c4",
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
      "definition_site": "00b6581c",
      "incomplete_value": true,
      "site": "00b65828",
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
      "00b658a8",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b658b8",
      "DATA",
      [
        "storage",
        "01126060",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b658a8",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b658b8",
      "DATA",
      [
        "storage",
        "01126160",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b657f0.md#insn-00b65810) · [`00b6580c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b657f0.md#insn-00b6580c) · [`00b65818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b657f0.md#insn-00b65818)
- 新版 `00b658ac`（命令位置の公開資料なし） · `00b658a8`（命令位置の公開資料なし） · `00b658b4`（命令位置の公開資料なし）

~~~diff
- 00b65810 ["INT_ADD", "register:40f0:8", ["const:b65810:8", "const:4:8"]]
- 00b65810 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b658ac ["INT_ADD", "register:40f0:8", ["const:b658ac:8", "const:4:8"]]
+ 00b658ac ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b65810 bytes fcd50394
+ 00b658ac bytes 09d60394
- 00b6580c ["COPY", "tmp:0:8", ["const:367:8"]]
- 00b6580c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6580c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6580c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b658a8 ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00b658a8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b658a8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b658a8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6580c bytes 009c0d91
+ 00b658a8 bytes 002c0c91
- 00b65818 ["COPY", "tmp:0:8", ["const:60:8"]]
- 00b65818 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b65818 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b65818 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b658b4 ["COPY", "tmp:0:8", ["const:160:8"]]
+ 00b658b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b658b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b658b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b65818 bytes 08810191
+ 00b658b4 bytes 08810591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-423e979f2f8caf3bb7fb6d00f0ee21e3"></a>

### [`00b6582c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b6582c.md) → [`00b658c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b658c8.md) _ZN8firebase3app13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b65908",
      "incomplete_value": true,
      "site": "00b65908",
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
            "const:150:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6586c",
      "incomplete_value": true,
      "site": "00b6586c",
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
            "const:50:8"
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
      "definition_site": "00b658e4",
      "incomplete_value": true,
      "site": "00b658e4",
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
      "definition_site": "00b65848",
      "incomplete_value": true,
      "site": "00b65848",
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
      "definition_site": "00b658ec",
      "incomplete_value": false,
      "site": "00b65900",
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
            "const:ceb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65850",
      "incomplete_value": false,
      "site": "00b65864",
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
            "const:cab:8"
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
      "00b658dc",
      "READ",
      [
        "storage",
        "01126050",
        null,
        "undefined8"
      ]
    ],
    [
      "00b658ec",
      "PARAM",
      [
        "storage",
        "002b6cab",
        null,
        "string"
      ]
    ],
    [
      "00b65908",
      "WRITE",
      [
        "storage",
        "01126050",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b658dc",
      "READ",
      [
        "storage",
        "01126150",
        null,
        "undefined8"
      ]
    ],
    [
      "00b658ec",
      "PARAM",
      [
        "storage",
        "002b6ceb",
        null,
        "string"
      ]
    ],
    [
      "00b65908",
      "WRITE",
      [
        "storage",
        "01126150",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65864`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b6582c.md#insn-00b65864) · [`00b6586c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b6582c.md#insn-00b6586c) · [`00b65840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b6582c.md#insn-00b65840)
- 新版 `00b65900`（命令位置の公開資料なし） · `00b65908`（命令位置の公開資料なし） · `00b658dc`（命令位置の公開資料なし）

~~~diff
- 00b65864 ["INT_ADD", "register:40f0:8", ["const:b65864:8", "const:4:8"]]
- 00b65864 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b65900 ["INT_ADD", "register:40f0:8", ["const:b65900:8", "const:4:8"]]
+ 00b65900 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b65864 bytes abd50394
+ 00b65900 bytes b8d50394
- 00b6586c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:50:8"]]
- 00b6586c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b65908 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:150:8"]]
+ 00b65908 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6586c bytes 802a00f9
+ 00b65908 bytes 80aa00f9
- 00b65840 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:50:8"]]
- 00b65840 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b658dc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:150:8"]]
+ 00b658dc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b65840 bytes 812a40f9
+ 00b658dc bytes 81aa40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92f70ca3d0bd74106e9fbc80f289fea0"></a>

### [`00b6589c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b6589c.md) → [`00b65938`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65938.md) _ZN8firebase3app10GetFieldIdENS0_5FieldE

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
      "definition_site": "00b65954",
      "incomplete_value": false,
      "site": "00b65958",
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
      "definition_site": "00b658b8",
      "incomplete_value": false,
      "site": "00b658bc",
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
      "definition_site": "00b65964",
      "incomplete_value": true,
      "site": "00b65970",
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
      "definition_site": "00b658c8",
      "incomplete_value": true,
      "site": "00b658d4",
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
      "00b65954",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b65964",
      "DATA",
      [
        "storage",
        "011260a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b65954",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b65964",
      "DATA",
      [
        "storage",
        "011261a8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b658bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b6589c.md#insn-00b658bc) · [`00b658b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b6589c.md#insn-00b658b8) · [`00b658c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b6589c.md#insn-00b658c4)
- 新版 `00b65958`（命令位置の公開資料なし） · `00b65954`（命令位置の公開資料なし） · `00b65960`（命令位置の公開資料なし）

~~~diff
- 00b658bc ["INT_ADD", "register:40f0:8", ["const:b658bc:8", "const:4:8"]]
- 00b658bc ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b65958 ["INT_ADD", "register:40f0:8", ["const:b65958:8", "const:4:8"]]
+ 00b65958 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b658bc bytes d1d50394
+ 00b65958 bytes ded50394
- 00b658b8 ["COPY", "tmp:0:8", ["const:51e:8"]]
- 00b658b8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b658b8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b658b8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b65954 ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00b65954 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b65954 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b65954 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b658b8 bytes 00781491
+ 00b65954 bytes 00341591
- 00b658c4 ["COPY", "tmp:0:8", ["const:a8:8"]]
- 00b658c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b658c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b658c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b65960 ["COPY", "tmp:0:8", ["const:1a8:8"]]
+ 00b65960 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b65960 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b65960 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b658c4 bytes 08a10291
+ 00b65960 bytes 08a10691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c7a8ff429415a73caefe36f78472d96"></a>

### [`00b658d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b658d8.md) → [`00b65974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65974.md) _ZN8firebase15options_builder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEN

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
      "definition_site": "00b659a0",
      "incomplete_value": true,
      "site": "00b659a0",
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
            "const:1b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65904",
      "incomplete_value": true,
      "site": "00b65904",
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
            "const:b0:8"
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
      "definition_site": "00b65988",
      "incomplete_value": true,
      "site": "00b65988",
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
      "definition_site": "00b658ec",
      "incomplete_value": true,
      "site": "00b658ec",
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
      "definition_site": "00b65994",
      "incomplete_value": false,
      "site": "00b65998",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a2000:8"
          ],
          [
            "leaf",
            "const:a09:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b658f8",
      "incomplete_value": false,
      "site": "00b658fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a2000:8"
          ],
          [
            "leaf",
            "const:a56:8"
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
      "00b65984",
      "READ",
      [
        "storage",
        "011260b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65994",
      "PARAM",
      [
        "storage",
        "002a2a56",
        null,
        "string"
      ]
    ],
    [
      "00b659a0",
      "WRITE",
      [
        "storage",
        "011260b0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b65984",
      "READ",
      [
        "storage",
        "011261b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65994",
      "PARAM",
      [
        "storage",
        "002a2a09",
        null,
        "string"
      ]
    ],
    [
      "00b659a0",
      "WRITE",
      [
        "storage",
        "011261b0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b658fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b658d8.md#insn-00b658fc) · [`00b65904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b658d8.md#insn-00b65904) · [`00b658e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b658d8.md#insn-00b658e8)
- 新版 `00b65998`（命令位置の公開資料なし） · `00b659a0`（命令位置の公開資料なし） · `00b65984`（命令位置の公開資料なし）

~~~diff
- 00b658fc ["INT_ADD", "register:40f0:8", ["const:b658fc:8", "const:4:8"]]
- 00b658fc ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b65998 ["INT_ADD", "register:40f0:8", ["const:b65998:8", "const:4:8"]]
+ 00b65998 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b658fc bytes 85d50394
+ 00b65998 bytes 92d50394
- 00b65904 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b0:8"]]
- 00b65904 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b659a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1b0:8"]]
+ 00b659a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65904 bytes 605a00f9
+ 00b659a0 bytes 60da00f9
- 00b658e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b0:8"]]
- 00b658e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b65984 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1b0:8"]]
+ 00b65984 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b658e8 bytes 685a40f9
+ 00b65984 bytes 68da40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df735ad5b3daaa6acd959b1089c164f1"></a>

### [`00b65918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65918.md) → [`00b659b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b659b4.md) _ZN8firebase15options_builder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEE

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
      "definition_site": "00b659e0",
      "incomplete_value": true,
      "site": "00b659e0",
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
            "const:1b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65944",
      "incomplete_value": true,
      "site": "00b65944",
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
            "const:b0:8"
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
      "definition_site": "00b659c8",
      "incomplete_value": true,
      "site": "00b659c8",
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
      "definition_site": "00b6592c",
      "incomplete_value": true,
      "site": "00b6592c",
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
      "definition_site": "00b659d0",
      "incomplete_value": false,
      "site": "00b659d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a2000:8"
          ],
          [
            "leaf",
            "const:a09:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65934",
      "incomplete_value": false,
      "site": "00b6593c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a2000:8"
          ],
          [
            "leaf",
            "const:a56:8"
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
      "00b659c4",
      "READ",
      [
        "storage",
        "011260b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b659d0",
      "PARAM",
      [
        "storage",
        "002a2a56",
        null,
        "string"
      ]
    ],
    [
      "00b659e0",
      "WRITE",
      [
        "storage",
        "011260b0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b659c4",
      "READ",
      [
        "storage",
        "011261b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b659d0",
      "PARAM",
      [
        "storage",
        "002a2a09",
        null,
        "string"
      ]
    ],
    [
      "00b659e0",
      "WRITE",
      [
        "storage",
        "011261b0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6593c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65918.md#insn-00b6593c) · [`00b65944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65918.md#insn-00b65944) · [`00b65928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65918.md#insn-00b65928)
- 新版 `00b659d8`（命令位置の公開資料なし） · `00b659e0`（命令位置の公開資料なし） · `00b659c4`（命令位置の公開資料なし）

~~~diff
- 00b6593c ["INT_ADD", "register:40f0:8", ["const:b6593c:8", "const:4:8"]]
- 00b6593c ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b659d8 ["INT_ADD", "register:40f0:8", ["const:b659d8:8", "const:4:8"]]
+ 00b659d8 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b6593c bytes 75d50394
+ 00b659d8 bytes 82d50394
- 00b65944 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b0:8"]]
- 00b65944 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b659e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1b0:8"]]
+ 00b659e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65944 bytes 605a00f9
+ 00b659e0 bytes 60da00f9
- 00b65928 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b0:8"]]
- 00b65928 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b659c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1b0:8"]]
+ 00b659c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b65928 bytes 685a40f9
+ 00b659c4 bytes 68da40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82a9dc6f021c4e9df880cb2c801e6d51"></a>

### [`00b65958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65958.md) → [`00b659f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b659f4.md) _ZN8firebase15options_builder10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b65a24",
      "incomplete_value": true,
      "site": "00b65a24",
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
            "const:1b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65988",
      "incomplete_value": true,
      "site": "00b65988",
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
            "const:b0:8"
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
      "definition_site": "00b65a08",
      "incomplete_value": true,
      "site": "00b65a08",
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
      "definition_site": "00b6596c",
      "incomplete_value": true,
      "site": "00b6596c",
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
      "definition_site": "00b65a14",
      "incomplete_value": false,
      "site": "00b65a1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a2000:8"
          ],
          [
            "leaf",
            "const:a09:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65978",
      "incomplete_value": false,
      "site": "00b65980",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a2000:8"
          ],
          [
            "leaf",
            "const:a56:8"
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
      "00b65a04",
      "READ",
      [
        "storage",
        "011260b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65a14",
      "PARAM",
      [
        "storage",
        "002a2a56",
        null,
        "string"
      ]
    ],
    [
      "00b65a24",
      "WRITE",
      [
        "storage",
        "011260b0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b65a04",
      "READ",
      [
        "storage",
        "011261b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65a14",
      "PARAM",
      [
        "storage",
        "002a2a09",
        null,
        "string"
      ]
    ],
    [
      "00b65a24",
      "WRITE",
      [
        "storage",
        "011261b0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65958.md#insn-00b65980) · [`00b65988`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65958.md#insn-00b65988) · [`00b65968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65958.md#insn-00b65968)
- 新版 `00b65a1c`（命令位置の公開資料なし） · `00b65a24`（命令位置の公開資料なし） · `00b65a04`（命令位置の公開資料なし）

~~~diff
- 00b65980 ["INT_ADD", "register:40f0:8", ["const:b65980:8", "const:4:8"]]
- 00b65980 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b65a1c ["INT_ADD", "register:40f0:8", ["const:b65a1c:8", "const:4:8"]]
+ 00b65a1c ["CALL", null, ["callee:00c5afe0:8"]]
- 00b65980 bytes 64d50394
+ 00b65a1c bytes 71d50394
- 00b65988 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b0:8"]]
- 00b65988 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b65a24 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1b0:8"]]
+ 00b65a24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65988 bytes 605a00f9
+ 00b65a24 bytes 60da00f9
- 00b65968 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b0:8"]]
- 00b65968 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b65a04 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1b0:8"]]
+ 00b65a04 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b65968 bytes 685a40f9
+ 00b65a04 bytes 68da40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17370ba65ea46e92492456150cb9b3c9"></a>

### [`00b6599c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b6599c.md) → [`00b65a38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65a38.md) _ZN8firebase15options_builder10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b65a68",
      "incomplete_value": true,
      "site": "00b65a68",
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
            "const:1b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b659cc",
      "incomplete_value": true,
      "site": "00b659cc",
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
            "const:b0:8"
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
      "definition_site": "00b65a4c",
      "incomplete_value": true,
      "site": "00b65a4c",
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
      "definition_site": "00b659b0",
      "incomplete_value": true,
      "site": "00b659b0",
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
      "definition_site": "00b65a54",
      "incomplete_value": false,
      "site": "00b65a60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a2000:8"
          ],
          [
            "leaf",
            "const:a09:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b659b8",
      "incomplete_value": false,
      "site": "00b659c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a2000:8"
          ],
          [
            "leaf",
            "const:a56:8"
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
      "00b65a48",
      "READ",
      [
        "storage",
        "011260b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65a54",
      "PARAM",
      [
        "storage",
        "002a2a56",
        null,
        "string"
      ]
    ],
    [
      "00b65a68",
      "WRITE",
      [
        "storage",
        "011260b0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b65a48",
      "READ",
      [
        "storage",
        "011261b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65a54",
      "PARAM",
      [
        "storage",
        "002a2a09",
        null,
        "string"
      ]
    ],
    [
      "00b65a68",
      "WRITE",
      [
        "storage",
        "011261b0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b659c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b6599c.md#insn-00b659c4) · [`00b659cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b6599c.md#insn-00b659cc) · [`00b659ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b6599c.md#insn-00b659ac)
- 新版 `00b65a60`（命令位置の公開資料なし） · `00b65a68`（命令位置の公開資料なし） · `00b65a48`（命令位置の公開資料なし）

~~~diff
- 00b659c4 ["INT_ADD", "register:40f0:8", ["const:b659c4:8", "const:4:8"]]
- 00b659c4 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b65a60 ["INT_ADD", "register:40f0:8", ["const:b65a60:8", "const:4:8"]]
+ 00b65a60 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b659c4 bytes 53d50394
+ 00b65a60 bytes 60d50394
- 00b659cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b0:8"]]
- 00b659cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b65a68 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1b0:8"]]
+ 00b65a68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b659cc bytes 605a00f9
+ 00b65a68 bytes 60da00f9
- 00b659ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b0:8"]]
- 00b659ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b65a48 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1b0:8"]]
+ 00b65a48 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b659ac bytes 685a40f9
+ 00b65a48 bytes 68da40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c14e0963b3b39ae1ce29571dc93d75c6"></a>

### [`00b659ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b659ec.md) → [`00b65a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65a88.md) _ZN8firebase15options_builder15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

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
      "site": "00b65a44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b65ae0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b65abc",
      "incomplete_value": true,
      "site": "00b65ac8",
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
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:1b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65a20",
      "incomplete_value": true,
      "site": "00b65a2c",
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
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:b0:8"
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
      "00b65a9c",
      "READ",
      [
        "storage",
        "011260b8",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b65a20",
      "READ",
      [
        "storage",
        "011260b0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b65a44",
      "WRITE",
      [
        "storage",
        "011260b8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b65a9c",
      "READ",
      [
        "storage",
        "011261b8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b65abc",
      "READ",
      [
        "storage",
        "011261b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65ae0",
      "WRITE",
      [
        "storage",
        "011261b8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65a2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b659ec.md#insn-00b65a2c) · [`00b65a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b659ec.md#insn-00b65a44)
- 新版 `00b65ac8`（命令位置の公開資料なし） · `00b65ae0`（命令位置の公開資料なし）

~~~diff
- 00b65a2c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b65a2c ["INT_ADD", "register:40f0:8", ["const:b65a2c:8", "const:4:8"]]
- 00b65a2c ["CALLIND", null, ["register:0:8"]]
+ 00b65ac8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b65ac8 ["INT_ADD", "register:40f0:8", ["const:b65ac8:8", "const:4:8"]]
+ 00b65ac8 ["CALLIND", null, ["register:0:8"]]
- 00b65a2c bytes 00013fd6
+ 00b65ac8 bytes 00013fd6
- 00b65a44 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b65a44 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:b8:8"]]
- 00b65a44 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b65a44 bytes a0e20239
+ 00b65ae0 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b65ae0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:1b8:8"]]
+ 00b65ae0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b65ae0 bytes a0e20639
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48ef72b4d3fcaaad5af0725d62999890"></a>

### [`00b65a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65a58.md) → [`00b65af4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65af4.md) _ZN8firebase15options_builder12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 53.57% / 新版 53.57%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件, `unresolved_store_alignment` 7件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b65a58"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b65a5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b65a5c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b65a58",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b65a5c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b65a60",
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
      "00b65af4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b65af8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b65afc",
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

- 旧版 [`00b65a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65a58.md#insn-00b65a58) · [`00b65a5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65a58.md#insn-00b65a5c) · [`00b65a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65a58.md#insn-00b65a60)

~~~diff
- 00b65a58 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b65a58 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b65a58 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b65a58 bytes f50f1df8
- 00b65a5c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b65a5c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b65a5c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b65a5c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b65a5c bytes f44f01a9
- 00b65a60 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b65a60 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b65a60 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b65a60 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b65a60 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0eaeec022804b42d542d36fc158dac26"></a>

### [`00b65ac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65ac8.md) → [`00b65b64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65b64.md) _ZN8firebase15options_builder14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b65ba4",
      "incomplete_value": true,
      "site": "00b65ba4",
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
            "const:1b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65b08",
      "incomplete_value": true,
      "site": "00b65b08",
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
            "const:b0:8"
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
      "definition_site": "00b65b80",
      "incomplete_value": true,
      "site": "00b65b80",
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
      "definition_site": "00b65ae4",
      "incomplete_value": true,
      "site": "00b65ae4",
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
      "definition_site": "00b65b88",
      "incomplete_value": false,
      "site": "00b65b9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a2000:8"
          ],
          [
            "leaf",
            "const:a09:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65aec",
      "incomplete_value": false,
      "site": "00b65b00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a2000:8"
          ],
          [
            "leaf",
            "const:a56:8"
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
      "00b65b78",
      "READ",
      [
        "storage",
        "011260b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65b88",
      "PARAM",
      [
        "storage",
        "002a2a56",
        null,
        "string"
      ]
    ],
    [
      "00b65ba4",
      "WRITE",
      [
        "storage",
        "011260b0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b65b78",
      "READ",
      [
        "storage",
        "011261b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65b88",
      "PARAM",
      [
        "storage",
        "002a2a09",
        null,
        "string"
      ]
    ],
    [
      "00b65ba4",
      "WRITE",
      [
        "storage",
        "011261b0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65b00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65ac8.md#insn-00b65b00) · [`00b65b08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65ac8.md#insn-00b65b08) · [`00b65adc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65ac8.md#insn-00b65adc)
- 新版 `00b65b9c`（命令位置の公開資料なし） · `00b65ba4`（命令位置の公開資料なし） · `00b65b78`（命令位置の公開資料なし）

~~~diff
- 00b65b00 ["INT_ADD", "register:40f0:8", ["const:b65b00:8", "const:4:8"]]
- 00b65b00 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b65b9c ["INT_ADD", "register:40f0:8", ["const:b65b9c:8", "const:4:8"]]
+ 00b65b9c ["CALL", null, ["callee:00c5afe0:8"]]
- 00b65b00 bytes 04d50394
+ 00b65b9c bytes 11d50394
- 00b65b08 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b0:8"]]
- 00b65b08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b65ba4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:1b0:8"]]
+ 00b65ba4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65b08 bytes 805a00f9
+ 00b65ba4 bytes 80da00f9
- 00b65adc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b0:8"]]
- 00b65adc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b65b78 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:1b0:8"]]
+ 00b65b78 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b65adc bytes 815a40f9
+ 00b65b78 bytes 81da40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d93e9471760557da54aa683f4a67a697"></a>

### [`00b65b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65b38.md) → [`00b65bd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65bd4.md) _ZN8firebase15options_builder11GetMethodIdENS0_6MethodE

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
      "definition_site": "00b65bf0",
      "incomplete_value": false,
      "site": "00b65bf4",
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
      "definition_site": "00b65b54",
      "incomplete_value": false,
      "site": "00b65b58",
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
      "definition_site": "00b65c00",
      "incomplete_value": true,
      "site": "00b65c0c",
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
      "definition_site": "00b65b64",
      "incomplete_value": true,
      "site": "00b65b70",
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
      "00b65bf0",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b65c00",
      "DATA",
      [
        "storage",
        "011260c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b65bf0",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b65c00",
      "DATA",
      [
        "storage",
        "011261c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65b38.md#insn-00b65b58) · [`00b65b54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65b38.md#insn-00b65b54) · [`00b65b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65b38.md#insn-00b65b60)
- 新版 `00b65bf4`（命令位置の公開資料なし） · `00b65bf0`（命令位置の公開資料なし） · `00b65bfc`（命令位置の公開資料なし）

~~~diff
- 00b65b58 ["INT_ADD", "register:40f0:8", ["const:b65b58:8", "const:4:8"]]
- 00b65b58 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b65bf4 ["INT_ADD", "register:40f0:8", ["const:b65bf4:8", "const:4:8"]]
+ 00b65bf4 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b65b58 bytes 2ad50394
+ 00b65bf4 bytes 37d50394
- 00b65b54 ["COPY", "tmp:0:8", ["const:367:8"]]
- 00b65b54 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b65b54 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b65b54 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b65bf0 ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00b65bf0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b65bf0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b65bf0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b65b54 bytes 009c0d91
+ 00b65bf0 bytes 002c0c91
- 00b65b60 ["COPY", "tmp:0:8", ["const:c0:8"]]
- 00b65b60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b65b60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b65b60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b65bfc ["COPY", "tmp:0:8", ["const:1c0:8"]]
+ 00b65bfc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b65bfc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b65bfc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b65b60 bytes 08010391
+ 00b65bfc bytes 08010791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ede394e7f0b390ecfd89b42a17e6e85"></a>

### [`00b65b74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65b74.md) → [`00b65c10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65c10.md) _ZN8firebase15options_builder13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

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
      "site": "00b65bb4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b65c50"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b65b90"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b65b88",
      "READ",
      [
        "storage",
        "011260b0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b65b90",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b65c54"
      ]
    ],
    [
      "unmatched:00b65b98",
      "PARAM",
      [
        "storage",
        "002a2a56",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b65c24",
      "READ",
      [
        "storage",
        "011261b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65c2c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b65c54"
      ]
    ],
    [
      "00b65c34",
      "PARAM",
      [
        "storage",
        "002a2a09",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65b74.md#insn-00b65b90) · [`00b65bac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65b74.md#insn-00b65bac) · [`00b65bb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65b74.md#insn-00b65bb4)
- 新版 `00b65c48`（命令位置の公開資料なし）

~~~diff
- 00b65b90 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b65b90 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b65b90 bytes 410100b5
- 00b65bac ["INT_ADD", "register:40f0:8", ["const:b65bac:8", "const:4:8"]]
- 00b65bac ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b65c48 ["INT_ADD", "register:40f0:8", ["const:b65c48:8", "const:4:8"]]
+ 00b65c48 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b65bac bytes d9d40394
+ 00b65c48 bytes e6d40394
- 00b65bb4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b0:8"]]
- 00b65bb4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65bb4 bytes 805a00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d99b9844d213c76051392e644466d919"></a>

### [`00b65c20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65c20.md) → [`00b65cbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65cbc.md) _ZN8firebase7options19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEENS_4util16

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 20.00% / 新版 33.33%

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
      "site": "00b65c4c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b65ce8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b65cd0",
      "incomplete_value": true,
      "site": "00b65cd0",
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
      "definition_site": "00b65c34",
      "incomplete_value": true,
      "site": "00b65c34",
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
      "00b65ccc",
      "READ",
      [
        "storage",
        "01126108",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b65c40",
      "PARAM",
      [
        "storage",
        "002b596b",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b65c44",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5afe0"
      ]
    ]
  ],
  "added": [
    [
      "00b65ccc",
      "READ",
      [
        "storage",
        "01126208",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65cdc",
      "PARAM",
      [
        "storage",
        "002b59ab",
        null,
        "string"
      ]
    ],
    [
      "00b65ce0",
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

- 旧版 [`00b65c34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65c20.md#insn-00b65c34) · [`00b65c44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65c20.md#insn-00b65c44) · [`00b65c4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65c20.md#insn-00b65c4c)
- 新版 `00b65cd0`（命令位置の公開資料なし）

~~~diff
- 00b65c34 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b65c34 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b65cd0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b65cd0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b65c34 bytes e80000b5
+ 00b65cd0 bytes e80000b5
- 00b65c44 ["INT_ADD", "register:40f0:8", ["const:b65c44:8", "const:4:8"]]
- 00b65c44 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b65c44 bytes b3d40394
- 00b65c4c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:108:8"]]
- 00b65c4c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65c4c bytes 608600f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0078a1b84b85af658b4eb30aa2c6991"></a>

### [`00b65c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65c60.md) → [`00b65cfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65cfc.md) _ZN8firebase7options19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEE

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
      "definition_site": "00b65d28",
      "incomplete_value": true,
      "site": "00b65d28",
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
            "const:208:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65c8c",
      "incomplete_value": true,
      "site": "00b65c8c",
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
            "const:108:8"
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
      "definition_site": "00b65d10",
      "incomplete_value": true,
      "site": "00b65d10",
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
      "definition_site": "00b65c74",
      "incomplete_value": true,
      "site": "00b65c74",
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
      "definition_site": "00b65d18",
      "incomplete_value": false,
      "site": "00b65d20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:9ab:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65c7c",
      "incomplete_value": false,
      "site": "00b65c84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:96b:8"
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
      "00b65d0c",
      "READ",
      [
        "storage",
        "01126108",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65d18",
      "PARAM",
      [
        "storage",
        "002b596b",
        null,
        "string"
      ]
    ],
    [
      "00b65d28",
      "WRITE",
      [
        "storage",
        "01126108",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b65d0c",
      "READ",
      [
        "storage",
        "01126208",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65d18",
      "PARAM",
      [
        "storage",
        "002b59ab",
        null,
        "string"
      ]
    ],
    [
      "00b65d28",
      "WRITE",
      [
        "storage",
        "01126208",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65c84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65c60.md#insn-00b65c84) · [`00b65c8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65c60.md#insn-00b65c8c) · [`00b65c70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65c60.md#insn-00b65c70)
- 新版 `00b65d20`（命令位置の公開資料なし） · `00b65d28`（命令位置の公開資料なし） · `00b65d0c`（命令位置の公開資料なし）

~~~diff
- 00b65c84 ["INT_ADD", "register:40f0:8", ["const:b65c84:8", "const:4:8"]]
- 00b65c84 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b65d20 ["INT_ADD", "register:40f0:8", ["const:b65d20:8", "const:4:8"]]
+ 00b65d20 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b65c84 bytes a3d40394
+ 00b65d20 bytes b0d40394
- 00b65c8c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:108:8"]]
- 00b65c8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b65d28 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:208:8"]]
+ 00b65d28 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65c8c bytes 608600f9
+ 00b65d28 bytes 600601f9
- 00b65c70 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:108:8"]]
- 00b65c70 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b65d0c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:208:8"]]
+ 00b65d0c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b65c70 bytes 688640f9
+ 00b65d0c bytes 680641f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2cb1fec87716d55c1effe09a462f5c02"></a>

### [`00b65ca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65ca0.md) → [`00b65d3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65d3c.md) _ZN8firebase7options10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b65d6c",
      "incomplete_value": true,
      "site": "00b65d6c",
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
            "const:208:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65cd0",
      "incomplete_value": true,
      "site": "00b65cd0",
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
            "const:108:8"
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
      "definition_site": "00b65d50",
      "incomplete_value": true,
      "site": "00b65d50",
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
      "definition_site": "00b65cb4",
      "incomplete_value": true,
      "site": "00b65cb4",
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
      "definition_site": "00b65d5c",
      "incomplete_value": false,
      "site": "00b65d64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:9ab:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65cc0",
      "incomplete_value": false,
      "site": "00b65cc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:96b:8"
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
      "00b65d4c",
      "READ",
      [
        "storage",
        "01126108",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65d5c",
      "PARAM",
      [
        "storage",
        "002b596b",
        null,
        "string"
      ]
    ],
    [
      "00b65d6c",
      "WRITE",
      [
        "storage",
        "01126108",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b65d4c",
      "READ",
      [
        "storage",
        "01126208",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65d5c",
      "PARAM",
      [
        "storage",
        "002b59ab",
        null,
        "string"
      ]
    ],
    [
      "00b65d6c",
      "WRITE",
      [
        "storage",
        "01126208",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65cc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65ca0.md#insn-00b65cc8) · [`00b65cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65ca0.md#insn-00b65cd0) · [`00b65cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65ca0.md#insn-00b65cb0)
- 新版 `00b65d64`（命令位置の公開資料なし） · `00b65d6c`（命令位置の公開資料なし） · `00b65d4c`（命令位置の公開資料なし）

~~~diff
- 00b65cc8 ["INT_ADD", "register:40f0:8", ["const:b65cc8:8", "const:4:8"]]
- 00b65cc8 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b65d64 ["INT_ADD", "register:40f0:8", ["const:b65d64:8", "const:4:8"]]
+ 00b65d64 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b65cc8 bytes 92d40394
+ 00b65d64 bytes 9fd40394
- 00b65cd0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:108:8"]]
- 00b65cd0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b65d6c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:208:8"]]
+ 00b65d6c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65cd0 bytes 608600f9
+ 00b65d6c bytes 600601f9
- 00b65cb0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:108:8"]]
- 00b65cb0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b65d4c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:208:8"]]
+ 00b65d4c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b65cb0 bytes 688640f9
+ 00b65d4c bytes 680641f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3148c1ae8f8bde7aa6e289271c20413"></a>

### [`00b65ce4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65ce4.md) → [`00b65d80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65d80.md) _ZN8firebase7options10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b65db0",
      "incomplete_value": true,
      "site": "00b65db0",
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
            "const:208:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65d14",
      "incomplete_value": true,
      "site": "00b65d14",
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
            "const:108:8"
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
      "definition_site": "00b65d94",
      "incomplete_value": true,
      "site": "00b65d94",
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
      "definition_site": "00b65cf8",
      "incomplete_value": true,
      "site": "00b65cf8",
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
      "definition_site": "00b65d9c",
      "incomplete_value": false,
      "site": "00b65da8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:9ab:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65d00",
      "incomplete_value": false,
      "site": "00b65d0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:96b:8"
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
      "00b65d90",
      "READ",
      [
        "storage",
        "01126108",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65d9c",
      "PARAM",
      [
        "storage",
        "002b596b",
        null,
        "string"
      ]
    ],
    [
      "00b65db0",
      "WRITE",
      [
        "storage",
        "01126108",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b65d90",
      "READ",
      [
        "storage",
        "01126208",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65d9c",
      "PARAM",
      [
        "storage",
        "002b59ab",
        null,
        "string"
      ]
    ],
    [
      "00b65db0",
      "WRITE",
      [
        "storage",
        "01126208",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65d0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65ce4.md#insn-00b65d0c) · [`00b65d14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65ce4.md#insn-00b65d14) · [`00b65cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65ce4.md#insn-00b65cf4)
- 新版 `00b65da8`（命令位置の公開資料なし） · `00b65db0`（命令位置の公開資料なし） · `00b65d90`（命令位置の公開資料なし）

~~~diff
- 00b65d0c ["INT_ADD", "register:40f0:8", ["const:b65d0c:8", "const:4:8"]]
- 00b65d0c ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b65da8 ["INT_ADD", "register:40f0:8", ["const:b65da8:8", "const:4:8"]]
+ 00b65da8 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b65d0c bytes 81d40394
+ 00b65da8 bytes 8ed40394
- 00b65d14 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:108:8"]]
- 00b65d14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b65db0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:208:8"]]
+ 00b65db0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65d14 bytes 608600f9
+ 00b65db0 bytes 600601f9
- 00b65cf4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:108:8"]]
- 00b65cf4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b65d90 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:208:8"]]
+ 00b65d90 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b65cf4 bytes 688640f9
+ 00b65d90 bytes 680641f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3968a78841256b2cc118626d459ccb2"></a>

### [`00b65d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65d34.md) → [`00b65dd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65dd0.md) _ZN8firebase7options15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b65e28",
      "incomplete_value": true,
      "site": "00b65e28",
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
            "const:210:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65d8c",
      "incomplete_value": true,
      "site": "00b65d8c",
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
            "const:110:8"
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
      "definition_site": "00b65e04",
      "incomplete_value": true,
      "site": "00b65e10",
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
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:208:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65d68",
      "incomplete_value": true,
      "site": "00b65d74",
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
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:108:8"
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
      "00b65de4",
      "READ",
      [
        "storage",
        "01126110",
        null,
        "undefined1"
      ]
    ],
    [
      "00b65e04",
      "READ",
      [
        "storage",
        "01126108",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65e28",
      "WRITE",
      [
        "storage",
        "01126110",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b65de4",
      "READ",
      [
        "storage",
        "01126210",
        null,
        "undefined1"
      ]
    ],
    [
      "00b65e04",
      "READ",
      [
        "storage",
        "01126208",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65e28",
      "WRITE",
      [
        "storage",
        "01126210",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65d34.md#insn-00b65d74) · [`00b65d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65d34.md#insn-00b65d8c) · [`00b65d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65d34.md#insn-00b65d48)
- 新版 `00b65e10`（命令位置の公開資料なし） · `00b65e28`（命令位置の公開資料なし） · `00b65de4`（命令位置の公開資料なし）

~~~diff
- 00b65d74 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b65d74 ["INT_ADD", "register:40f0:8", ["const:b65d74:8", "const:4:8"]]
- 00b65d74 ["CALLIND", null, ["register:0:8"]]
+ 00b65e10 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b65e10 ["INT_ADD", "register:40f0:8", ["const:b65e10:8", "const:4:8"]]
+ 00b65e10 ["CALLIND", null, ["register:0:8"]]
- 00b65d74 bytes 00013fd6
+ 00b65e10 bytes 00013fd6
- 00b65d8c ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b65d8c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:110:8"]]
- 00b65d8c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b65e28 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b65e28 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:210:8"]]
+ 00b65e28 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b65d8c bytes a0420439
+ 00b65e28 bytes a0420839
- 00b65d48 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:110:8"]]
- 00b65d48 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b65d48 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b65de4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:210:8"]]
+ 00b65de4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b65de4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b65d48 bytes a8424439
+ 00b65de4 bytes a8424839
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37333d59347b49b039c154d861d3c8c2"></a>

### [`00b65da0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65da0.md) → [`00b65e3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65e3c.md) _ZN8firebase7options12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b65e78",
      "incomplete_value": true,
      "site": "00b65e78",
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
            "const:210:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65ddc",
      "incomplete_value": true,
      "site": "00b65ddc",
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
            "const:110:8"
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
      "definition_site": "00b65e98",
      "incomplete_value": true,
      "site": "00b65e98",
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
            "const:208:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65dfc",
      "incomplete_value": true,
      "site": "00b65dfc",
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
            "const:108:8"
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
      "definition_site": "00b65e54",
      "incomplete_value": true,
      "site": "00b65e54",
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
      "definition_site": "00b65db8",
      "incomplete_value": true,
      "site": "00b65db8",
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
      "00b65e50",
      "READ",
      [
        "storage",
        "01126108",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65e5c",
      "READ",
      [
        "storage",
        "01126110",
        null,
        "undefined1"
      ]
    ],
    [
      "00b65e78",
      "WRITE",
      [
        "storage",
        "01126110",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b65e50",
      "READ",
      [
        "storage",
        "01126208",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65e5c",
      "READ",
      [
        "storage",
        "01126210",
        null,
        "undefined1"
      ]
    ],
    [
      "00b65e78",
      "WRITE",
      [
        "storage",
        "01126210",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65ddc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65da0.md#insn-00b65ddc) · [`00b65df8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65da0.md#insn-00b65df8) · [`00b65dfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65da0.md#insn-00b65dfc)
- 新版 `00b65e78`（命令位置の公開資料なし） · `00b65e94`（命令位置の公開資料なし） · `00b65e98`（命令位置の公開資料なし）

~~~diff
- 00b65ddc ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b65ddc ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b65ddc ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:110:8"]]
- 00b65ddc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b65e78 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b65e78 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b65e78 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:210:8"]]
+ 00b65e78 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b65ddc bytes bf420439
+ 00b65e78 bytes bf420839
- 00b65df8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b65df8 ["INT_ADD", "register:40f0:8", ["const:b65df8:8", "const:4:8"]]
- 00b65df8 ["CALLIND", null, ["register:0:8"]]
+ 00b65e94 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b65e94 ["INT_ADD", "register:40f0:8", ["const:b65e94:8", "const:4:8"]]
+ 00b65e94 ["CALLIND", null, ["register:0:8"]]
- 00b65df8 bytes 00013fd6
+ 00b65e94 bytes 00013fd6
- 00b65dfc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:108:8"]]
- 00b65dfc ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b65dfc ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b65e98 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:208:8"]]
+ 00b65e98 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b65e98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b65dfc bytes 9f8600f9
+ 00b65e98 bytes 9f0601f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb0d5d19bb8743b2f9c915629237e341"></a>

### [`00b65e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65e10.md) → [`00b65eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65eac.md) _ZN8firebase7options14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b65eec",
      "incomplete_value": true,
      "site": "00b65eec",
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
            "const:208:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65e50",
      "incomplete_value": true,
      "site": "00b65e50",
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
            "const:108:8"
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
      "definition_site": "00b65ec8",
      "incomplete_value": true,
      "site": "00b65ec8",
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
      "definition_site": "00b65e2c",
      "incomplete_value": true,
      "site": "00b65e2c",
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
      "definition_site": "00b65ed0",
      "incomplete_value": false,
      "site": "00b65ee4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:9ab:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65e34",
      "incomplete_value": false,
      "site": "00b65e48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:96b:8"
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
      "00b65ec0",
      "READ",
      [
        "storage",
        "01126108",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65ed0",
      "PARAM",
      [
        "storage",
        "002b596b",
        null,
        "string"
      ]
    ],
    [
      "00b65eec",
      "WRITE",
      [
        "storage",
        "01126108",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b65ec0",
      "READ",
      [
        "storage",
        "01126208",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65ed0",
      "PARAM",
      [
        "storage",
        "002b59ab",
        null,
        "string"
      ]
    ],
    [
      "00b65eec",
      "WRITE",
      [
        "storage",
        "01126208",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65e48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65e10.md#insn-00b65e48) · [`00b65e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65e10.md#insn-00b65e50) · [`00b65e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65e10.md#insn-00b65e24)
- 新版 `00b65ee4`（命令位置の公開資料なし） · `00b65eec`（命令位置の公開資料なし） · `00b65ec0`（命令位置の公開資料なし）

~~~diff
- 00b65e48 ["INT_ADD", "register:40f0:8", ["const:b65e48:8", "const:4:8"]]
- 00b65e48 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b65ee4 ["INT_ADD", "register:40f0:8", ["const:b65ee4:8", "const:4:8"]]
+ 00b65ee4 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b65e48 bytes 32d40394
+ 00b65ee4 bytes 3fd40394
- 00b65e50 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:108:8"]]
- 00b65e50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b65eec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:208:8"]]
+ 00b65eec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65e50 bytes 808600f9
+ 00b65eec bytes 800601f9
- 00b65e24 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:108:8"]]
- 00b65e24 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b65ec0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:208:8"]]
+ 00b65ec0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b65e24 bytes 818640f9
+ 00b65ec0 bytes 810641f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90d68b76d322acede050eba180034d17"></a>

### [`00b65e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65e80.md) → [`00b65f1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65f1c.md) _ZN8firebase7options11GetMethodIdENS0_6MethodE

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
      "definition_site": "00b65f38",
      "incomplete_value": false,
      "site": "00b65f3c",
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
      "definition_site": "00b65e9c",
      "incomplete_value": false,
      "site": "00b65ea0",
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
      "definition_site": "00b65f48",
      "incomplete_value": true,
      "site": "00b65f54",
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
      "definition_site": "00b65eac",
      "incomplete_value": true,
      "site": "00b65eb8",
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
      "00b65f38",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b65f48",
      "DATA",
      [
        "storage",
        "01126118",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b65f38",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b65f48",
      "DATA",
      [
        "storage",
        "01126218",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65e80.md#insn-00b65ea0) · [`00b65e9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65e80.md#insn-00b65e9c) · [`00b65ea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65e80.md#insn-00b65ea8)
- 新版 `00b65f3c`（命令位置の公開資料なし） · `00b65f38`（命令位置の公開資料なし） · `00b65f44`（命令位置の公開資料なし）

~~~diff
- 00b65ea0 ["INT_ADD", "register:40f0:8", ["const:b65ea0:8", "const:4:8"]]
- 00b65ea0 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b65f3c ["INT_ADD", "register:40f0:8", ["const:b65f3c:8", "const:4:8"]]
+ 00b65f3c ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b65ea0 bytes 58d40394
+ 00b65f3c bytes 65d40394
- 00b65e9c ["COPY", "tmp:0:8", ["const:367:8"]]
- 00b65e9c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b65e9c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b65e9c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b65f38 ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00b65f38 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b65f38 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b65f38 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b65e9c bytes 009c0d91
+ 00b65f38 bytes 002c0c91
- 00b65ea8 ["COPY", "tmp:0:8", ["const:118:8"]]
- 00b65ea8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b65ea8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b65ea8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b65f44 ["COPY", "tmp:0:8", ["const:218:8"]]
+ 00b65f44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b65f44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b65f44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b65ea8 bytes 08610491
+ 00b65f44 bytes 08610891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17f32102af3d9f03ae369b5fede4b814"></a>

### [`00b65ebc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65ebc.md) → [`00b65f58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65f58.md) _ZN8firebase7options13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b65f98",
      "incomplete_value": true,
      "site": "00b65f98",
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
            "const:208:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65efc",
      "incomplete_value": true,
      "site": "00b65efc",
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
            "const:108:8"
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
      "definition_site": "00b65f74",
      "incomplete_value": true,
      "site": "00b65f74",
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
      "definition_site": "00b65ed8",
      "incomplete_value": true,
      "site": "00b65ed8",
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
      "definition_site": "00b65f7c",
      "incomplete_value": false,
      "site": "00b65f90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:9ab:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65ee0",
      "incomplete_value": false,
      "site": "00b65ef4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:96b:8"
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
      "00b65f6c",
      "READ",
      [
        "storage",
        "01126108",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65f7c",
      "PARAM",
      [
        "storage",
        "002b596b",
        null,
        "string"
      ]
    ],
    [
      "00b65f98",
      "WRITE",
      [
        "storage",
        "01126108",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b65f6c",
      "READ",
      [
        "storage",
        "01126208",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65f7c",
      "PARAM",
      [
        "storage",
        "002b59ab",
        null,
        "string"
      ]
    ],
    [
      "00b65f98",
      "WRITE",
      [
        "storage",
        "01126208",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65ebc.md#insn-00b65ef4) · [`00b65efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65ebc.md#insn-00b65efc) · [`00b65ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65ebc.md#insn-00b65ed0)
- 新版 `00b65f90`（命令位置の公開資料なし） · `00b65f98`（命令位置の公開資料なし） · `00b65f6c`（命令位置の公開資料なし）

~~~diff
- 00b65ef4 ["INT_ADD", "register:40f0:8", ["const:b65ef4:8", "const:4:8"]]
- 00b65ef4 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b65f90 ["INT_ADD", "register:40f0:8", ["const:b65f90:8", "const:4:8"]]
+ 00b65f90 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b65ef4 bytes 07d40394
+ 00b65f90 bytes 14d40394
- 00b65efc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:108:8"]]
- 00b65efc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b65f98 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:208:8"]]
+ 00b65f98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65efc bytes 808600f9
+ 00b65f98 bytes 800601f9
- 00b65ed0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:108:8"]]
- 00b65ed0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b65f6c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:208:8"]]
+ 00b65f6c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b65ed0 bytes 818640f9
+ 00b65f6c bytes 810641f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed542f09669b7ef3e440d3ce1782d3b5"></a>

### [`00b65f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65f2c.md) → [`00b65fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65fc8.md) _ZN8firebase7options10GetFieldIdENS0_5FieldE

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
      "definition_site": "00b65fe4",
      "incomplete_value": false,
      "site": "00b65fe8",
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
      "definition_site": "00b65f48",
      "incomplete_value": false,
      "site": "00b65f4c",
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
      "definition_site": "00b65ff4",
      "incomplete_value": true,
      "site": "00b66000",
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
      "definition_site": "00b65f58",
      "incomplete_value": true,
      "site": "00b65f64",
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
      "00b65fe4",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b65ff4",
      "DATA",
      [
        "storage",
        "01126150",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b65fe4",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b65ff4",
      "DATA",
      [
        "storage",
        "01126250",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65f2c.md#insn-00b65f4c) · [`00b65f48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65f2c.md#insn-00b65f48) · [`00b65f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65f2c.md#insn-00b65f54)
- 新版 `00b65fe8`（命令位置の公開資料なし） · `00b65fe4`（命令位置の公開資料なし） · `00b65ff0`（命令位置の公開資料なし）

~~~diff
- 00b65f4c ["INT_ADD", "register:40f0:8", ["const:b65f4c:8", "const:4:8"]]
- 00b65f4c ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b65fe8 ["INT_ADD", "register:40f0:8", ["const:b65fe8:8", "const:4:8"]]
+ 00b65fe8 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b65f4c bytes 2dd40394
+ 00b65fe8 bytes 3ad40394
- 00b65f48 ["COPY", "tmp:0:8", ["const:51e:8"]]
- 00b65f48 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b65f48 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b65f48 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b65fe4 ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00b65fe4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b65fe4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b65fe4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b65f48 bytes 00781491
+ 00b65fe4 bytes 00341591
- 00b65f54 ["COPY", "tmp:0:8", ["const:150:8"]]
- 00b65f54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b65f54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b65f54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b65ff0 ["COPY", "tmp:0:8", ["const:250:8"]]
+ 00b65ff0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b65ff0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b65ff0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b65f54 bytes 08410591
+ 00b65ff0 bytes 08410991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d980f077430175b64be180d0d714f60"></a>

### [`00b65f68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65f68.md) → [`00b66004`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66004.md) _ZN8firebase17version_registrar19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEE

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
      "definition_site": "00b66030",
      "incomplete_value": true,
      "site": "00b66030",
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
            "const:258:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65f94",
      "incomplete_value": true,
      "site": "00b65f94",
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
            "const:158:8"
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
      "definition_site": "00b66018",
      "incomplete_value": true,
      "site": "00b66018",
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
      "definition_site": "00b65f7c",
      "incomplete_value": true,
      "site": "00b65f7c",
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
      "definition_site": "00b66024",
      "incomplete_value": false,
      "site": "00b66028",
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
            "const:9ba:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65f88",
      "incomplete_value": false,
      "site": "00b65f8c",
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
            "const:97a:8"
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
      "00b66014",
      "READ",
      [
        "storage",
        "01126158",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66024",
      "PARAM",
      [
        "storage",
        "002c097a",
        null,
        "string"
      ]
    ],
    [
      "00b66030",
      "WRITE",
      [
        "storage",
        "01126158",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b66014",
      "READ",
      [
        "storage",
        "01126258",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66024",
      "PARAM",
      [
        "storage",
        "002c09ba",
        null,
        "string"
      ]
    ],
    [
      "00b66030",
      "WRITE",
      [
        "storage",
        "01126258",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65f8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65f68.md#insn-00b65f8c) · [`00b65f94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65f68.md#insn-00b65f94) · [`00b65f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65f68.md#insn-00b65f78)
- 新版 `00b66028`（命令位置の公開資料なし） · `00b66030`（命令位置の公開資料なし） · `00b66014`（命令位置の公開資料なし）

~~~diff
- 00b65f8c ["INT_ADD", "register:40f0:8", ["const:b65f8c:8", "const:4:8"]]
- 00b65f8c ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b66028 ["INT_ADD", "register:40f0:8", ["const:b66028:8", "const:4:8"]]
+ 00b66028 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b65f8c bytes e1d30394
+ 00b66028 bytes eed30394
- 00b65f94 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:158:8"]]
- 00b65f94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b66030 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:258:8"]]
+ 00b66030 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65f94 bytes 60ae00f9
+ 00b66030 bytes 602e01f9
- 00b65f78 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:158:8"]]
- 00b65f78 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b66014 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:258:8"]]
+ 00b66014 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b65f78 bytes 68ae40f9
+ 00b66014 bytes 682e41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f3dd852fe8ad5831871355630e527d1"></a>

### [`00b65fa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65fa8.md) → [`00b66044`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66044.md) _ZN8firebase17version_registrar19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEE

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
      "definition_site": "00b66070",
      "incomplete_value": true,
      "site": "00b66070",
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
            "const:258:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65fd4",
      "incomplete_value": true,
      "site": "00b65fd4",
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
            "const:158:8"
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
      "definition_site": "00b66058",
      "incomplete_value": true,
      "site": "00b66058",
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
      "definition_site": "00b65fbc",
      "incomplete_value": true,
      "site": "00b65fbc",
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
      "definition_site": "00b66060",
      "incomplete_value": false,
      "site": "00b66068",
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
            "const:9ba:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65fc4",
      "incomplete_value": false,
      "site": "00b65fcc",
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
            "const:97a:8"
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
      "00b66054",
      "READ",
      [
        "storage",
        "01126158",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66060",
      "PARAM",
      [
        "storage",
        "002c097a",
        null,
        "string"
      ]
    ],
    [
      "00b66070",
      "WRITE",
      [
        "storage",
        "01126158",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b66054",
      "READ",
      [
        "storage",
        "01126258",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66060",
      "PARAM",
      [
        "storage",
        "002c09ba",
        null,
        "string"
      ]
    ],
    [
      "00b66070",
      "WRITE",
      [
        "storage",
        "01126258",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65fcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65fa8.md#insn-00b65fcc) · [`00b65fd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65fa8.md#insn-00b65fd4) · [`00b65fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65fa8.md#insn-00b65fb8)
- 新版 `00b66068`（命令位置の公開資料なし） · `00b66070`（命令位置の公開資料なし） · `00b66054`（命令位置の公開資料なし）

~~~diff
- 00b65fcc ["INT_ADD", "register:40f0:8", ["const:b65fcc:8", "const:4:8"]]
- 00b65fcc ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b66068 ["INT_ADD", "register:40f0:8", ["const:b66068:8", "const:4:8"]]
+ 00b66068 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b65fcc bytes d1d30394
+ 00b66068 bytes ded30394
- 00b65fd4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:158:8"]]
- 00b65fd4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b66070 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:258:8"]]
+ 00b66070 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65fd4 bytes 60ae00f9
+ 00b66070 bytes 602e01f9
- 00b65fb8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:158:8"]]
- 00b65fb8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b66054 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:258:8"]]
+ 00b66054 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b65fb8 bytes 68ae40f9
+ 00b66054 bytes 682e41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0310f42fd60a5b7668285f7437ea2f28"></a>

### [`00b65fe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65fe8.md) → [`00b66084`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66084.md) _ZN8firebase17version_registrar10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b660b4",
      "incomplete_value": true,
      "site": "00b660b4",
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
            "const:258:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66018",
      "incomplete_value": true,
      "site": "00b66018",
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
            "const:158:8"
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
      "definition_site": "00b66098",
      "incomplete_value": true,
      "site": "00b66098",
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
      "definition_site": "00b65ffc",
      "incomplete_value": true,
      "site": "00b65ffc",
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
      "definition_site": "00b660a4",
      "incomplete_value": false,
      "site": "00b660ac",
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
            "const:9ba:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66008",
      "incomplete_value": false,
      "site": "00b66010",
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
            "const:97a:8"
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
      "00b66094",
      "READ",
      [
        "storage",
        "01126158",
        null,
        "undefined8"
      ]
    ],
    [
      "00b660a4",
      "PARAM",
      [
        "storage",
        "002c097a",
        null,
        "string"
      ]
    ],
    [
      "00b660b4",
      "WRITE",
      [
        "storage",
        "01126158",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b66094",
      "READ",
      [
        "storage",
        "01126258",
        null,
        "undefined8"
      ]
    ],
    [
      "00b660a4",
      "PARAM",
      [
        "storage",
        "002c09ba",
        null,
        "string"
      ]
    ],
    [
      "00b660b4",
      "WRITE",
      [
        "storage",
        "01126258",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65fe8.md#insn-00b66010) · [`00b66018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65fe8.md#insn-00b66018) · [`00b65ff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65fe8.md#insn-00b65ff8)
- 新版 `00b660ac`（命令位置の公開資料なし） · `00b660b4`（命令位置の公開資料なし） · `00b66094`（命令位置の公開資料なし）

~~~diff
- 00b66010 ["INT_ADD", "register:40f0:8", ["const:b66010:8", "const:4:8"]]
- 00b66010 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b660ac ["INT_ADD", "register:40f0:8", ["const:b660ac:8", "const:4:8"]]
+ 00b660ac ["CALL", null, ["callee:00c5afe0:8"]]
- 00b66010 bytes c0d30394
+ 00b660ac bytes cdd30394
- 00b66018 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:158:8"]]
- 00b66018 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b660b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:258:8"]]
+ 00b660b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66018 bytes 60ae00f9
+ 00b660b4 bytes 602e01f9
- 00b65ff8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:158:8"]]
- 00b65ff8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b66094 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:258:8"]]
+ 00b66094 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b65ff8 bytes 68ae40f9
+ 00b66094 bytes 682e41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5618910c7fa0321815462c3c8a0fd6f2"></a>

### [`00b6602c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b6602c.md) → [`00b660c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b660c8.md) _ZN8firebase17version_registrar10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b660f8",
      "incomplete_value": true,
      "site": "00b660f8",
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
            "const:258:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6605c",
      "incomplete_value": true,
      "site": "00b6605c",
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
            "const:158:8"
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
      "definition_site": "00b660dc",
      "incomplete_value": true,
      "site": "00b660dc",
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
      "definition_site": "00b66040",
      "incomplete_value": true,
      "site": "00b66040",
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
      "definition_site": "00b660e4",
      "incomplete_value": false,
      "site": "00b660f0",
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
            "const:9ba:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66048",
      "incomplete_value": false,
      "site": "00b66054",
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
            "const:97a:8"
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
      "00b660d8",
      "READ",
      [
        "storage",
        "01126158",
        null,
        "undefined8"
      ]
    ],
    [
      "00b660e4",
      "PARAM",
      [
        "storage",
        "002c097a",
        null,
        "string"
      ]
    ],
    [
      "00b660f8",
      "WRITE",
      [
        "storage",
        "01126158",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b660d8",
      "READ",
      [
        "storage",
        "01126258",
        null,
        "undefined8"
      ]
    ],
    [
      "00b660e4",
      "PARAM",
      [
        "storage",
        "002c09ba",
        null,
        "string"
      ]
    ],
    [
      "00b660f8",
      "WRITE",
      [
        "storage",
        "01126258",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b6602c.md#insn-00b66054) · [`00b6605c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b6602c.md#insn-00b6605c) · [`00b6603c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b6602c.md#insn-00b6603c)
- 新版 `00b660f0`（命令位置の公開資料なし） · `00b660f8`（命令位置の公開資料なし） · `00b660d8`（命令位置の公開資料なし）

~~~diff
- 00b66054 ["INT_ADD", "register:40f0:8", ["const:b66054:8", "const:4:8"]]
- 00b66054 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b660f0 ["INT_ADD", "register:40f0:8", ["const:b660f0:8", "const:4:8"]]
+ 00b660f0 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b66054 bytes afd30394
+ 00b660f0 bytes bcd30394
- 00b6605c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:158:8"]]
- 00b6605c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b660f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:258:8"]]
+ 00b660f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6605c bytes 60ae00f9
+ 00b660f8 bytes 602e01f9
- 00b6603c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:158:8"]]
- 00b6603c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b660d8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:258:8"]]
+ 00b660d8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6603c bytes 68ae40f9
+ 00b660d8 bytes 682e41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04aa8c444ee143c2c5b72bedd0c6f2da"></a>

### [`00b6607c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b6607c.md) → [`00b66118`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66118.md) _ZN8firebase17version_registrar15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b66170",
      "incomplete_value": true,
      "site": "00b66170",
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
            "const:260:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b660d4",
      "incomplete_value": true,
      "site": "00b660d4",
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
            "const:160:8"
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
      "definition_site": "00b6614c",
      "incomplete_value": true,
      "site": "00b66158",
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
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:258:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b660b0",
      "incomplete_value": true,
      "site": "00b660bc",
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
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:158:8"
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
      "00b6612c",
      "READ",
      [
        "storage",
        "01126160",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6614c",
      "READ",
      [
        "storage",
        "01126158",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66170",
      "WRITE",
      [
        "storage",
        "01126160",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b6612c",
      "READ",
      [
        "storage",
        "01126260",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6614c",
      "READ",
      [
        "storage",
        "01126258",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66170",
      "WRITE",
      [
        "storage",
        "01126260",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b660bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b6607c.md#insn-00b660bc) · [`00b660d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b6607c.md#insn-00b660d4) · [`00b66090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b6607c.md#insn-00b66090)
- 新版 `00b66158`（命令位置の公開資料なし） · `00b66170`（命令位置の公開資料なし） · `00b6612c`（命令位置の公開資料なし）

~~~diff
- 00b660bc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b660bc ["INT_ADD", "register:40f0:8", ["const:b660bc:8", "const:4:8"]]
- 00b660bc ["CALLIND", null, ["register:0:8"]]
+ 00b66158 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b66158 ["INT_ADD", "register:40f0:8", ["const:b66158:8", "const:4:8"]]
+ 00b66158 ["CALLIND", null, ["register:0:8"]]
- 00b660bc bytes 00013fd6
+ 00b66158 bytes 00013fd6
- 00b660d4 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b660d4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:160:8"]]
- 00b660d4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b66170 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b66170 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:260:8"]]
+ 00b66170 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b660d4 bytes a0820539
+ 00b66170 bytes a0820939
- 00b66090 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:160:8"]]
- 00b66090 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b66090 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b6612c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:260:8"]]
+ 00b6612c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b6612c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b66090 bytes a8824539
+ 00b6612c bytes a8824939
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56c1bcbe772a9236c8b50db309167bd3"></a>

### [`00b660e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b660e8.md) → [`00b66184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66184.md) _ZN8firebase17version_registrar12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b661c0",
      "incomplete_value": true,
      "site": "00b661c0",
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
            "const:260:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66124",
      "incomplete_value": true,
      "site": "00b66124",
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
            "const:160:8"
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
      "definition_site": "00b661e0",
      "incomplete_value": true,
      "site": "00b661e0",
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
            "const:258:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66144",
      "incomplete_value": true,
      "site": "00b66144",
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
            "const:158:8"
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
      "definition_site": "00b6619c",
      "incomplete_value": true,
      "site": "00b6619c",
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
      "definition_site": "00b66100",
      "incomplete_value": true,
      "site": "00b66100",
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
      "00b66198",
      "READ",
      [
        "storage",
        "01126158",
        null,
        "undefined8"
      ]
    ],
    [
      "00b661a4",
      "READ",
      [
        "storage",
        "01126160",
        null,
        "undefined1"
      ]
    ],
    [
      "00b661c0",
      "WRITE",
      [
        "storage",
        "01126160",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b66198",
      "READ",
      [
        "storage",
        "01126258",
        null,
        "undefined8"
      ]
    ],
    [
      "00b661a4",
      "READ",
      [
        "storage",
        "01126260",
        null,
        "undefined1"
      ]
    ],
    [
      "00b661c0",
      "WRITE",
      [
        "storage",
        "01126260",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b660e8.md#insn-00b66124) · [`00b66140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b660e8.md#insn-00b66140) · [`00b66144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b660e8.md#insn-00b66144)
- 新版 `00b661c0`（命令位置の公開資料なし） · `00b661dc`（命令位置の公開資料なし） · `00b661e0`（命令位置の公開資料なし）

~~~diff
- 00b66124 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b66124 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b66124 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:160:8"]]
- 00b66124 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b661c0 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b661c0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b661c0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:260:8"]]
+ 00b661c0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b66124 bytes bf820539
+ 00b661c0 bytes bf820939
- 00b66140 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b66140 ["INT_ADD", "register:40f0:8", ["const:b66140:8", "const:4:8"]]
- 00b66140 ["CALLIND", null, ["register:0:8"]]
+ 00b661dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b661dc ["INT_ADD", "register:40f0:8", ["const:b661dc:8", "const:4:8"]]
+ 00b661dc ["CALLIND", null, ["register:0:8"]]
- 00b66140 bytes 00013fd6
+ 00b661dc bytes 00013fd6
- 00b66144 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:158:8"]]
- 00b66144 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b66144 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b661e0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:258:8"]]
+ 00b661e0 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b661e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b66144 bytes 9fae00f9
+ 00b661e0 bytes 9f2e01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da78d7ea959dd2b7b5f890ce23d3e82e"></a>

### [`00b66158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66158.md) → [`00b661f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b661f4.md) _ZN8firebase17version_registrar14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b66234",
      "incomplete_value": true,
      "site": "00b66234",
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
            "const:258:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66198",
      "incomplete_value": true,
      "site": "00b66198",
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
            "const:158:8"
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
      "definition_site": "00b66210",
      "incomplete_value": true,
      "site": "00b66210",
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
      "definition_site": "00b66174",
      "incomplete_value": true,
      "site": "00b66174",
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
      "definition_site": "00b66218",
      "incomplete_value": false,
      "site": "00b6622c",
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
            "const:9ba:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6617c",
      "incomplete_value": false,
      "site": "00b66190",
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
            "const:97a:8"
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
      "00b66208",
      "READ",
      [
        "storage",
        "01126158",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66218",
      "PARAM",
      [
        "storage",
        "002c097a",
        null,
        "string"
      ]
    ],
    [
      "00b66234",
      "WRITE",
      [
        "storage",
        "01126158",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b66208",
      "READ",
      [
        "storage",
        "01126258",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66218",
      "PARAM",
      [
        "storage",
        "002c09ba",
        null,
        "string"
      ]
    ],
    [
      "00b66234",
      "WRITE",
      [
        "storage",
        "01126258",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66158.md#insn-00b66190) · [`00b66198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66158.md#insn-00b66198) · [`00b6616c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66158.md#insn-00b6616c)
- 新版 `00b6622c`（命令位置の公開資料なし） · `00b66234`（命令位置の公開資料なし） · `00b66208`（命令位置の公開資料なし）

~~~diff
- 00b66190 ["INT_ADD", "register:40f0:8", ["const:b66190:8", "const:4:8"]]
- 00b66190 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b6622c ["INT_ADD", "register:40f0:8", ["const:b6622c:8", "const:4:8"]]
+ 00b6622c ["CALL", null, ["callee:00c5afe0:8"]]
- 00b66190 bytes 60d30394
+ 00b6622c bytes 6dd30394
- 00b66198 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:158:8"]]
- 00b66198 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b66234 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:258:8"]]
+ 00b66234 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66198 bytes 80ae00f9
+ 00b66234 bytes 802e01f9
- 00b6616c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:158:8"]]
- 00b6616c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b66208 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:258:8"]]
+ 00b66208 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6616c bytes 81ae40f9
+ 00b66208 bytes 812e41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f58c03dc5034fb1eb15ac9b29cdd3b3"></a>

### [`00b661c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b661c8.md) → [`00b66264`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66264.md) _ZN8firebase17version_registrar11GetMethodIdENS0_6MethodE

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
      "definition_site": "00b66280",
      "incomplete_value": false,
      "site": "00b66284",
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
      "definition_site": "00b661e4",
      "incomplete_value": false,
      "site": "00b661e8",
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
      "definition_site": "00b66290",
      "incomplete_value": true,
      "site": "00b6629c",
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
      "definition_site": "00b661f4",
      "incomplete_value": true,
      "site": "00b66200",
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
      "00b66280",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b66290",
      "DATA",
      [
        "storage",
        "01126168",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b66280",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b66290",
      "DATA",
      [
        "storage",
        "01126268",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b661e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b661c8.md#insn-00b661e8) · [`00b661e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b661c8.md#insn-00b661e4) · [`00b661f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b661c8.md#insn-00b661f0)
- 新版 `00b66284`（命令位置の公開資料なし） · `00b66280`（命令位置の公開資料なし） · `00b6628c`（命令位置の公開資料なし）

~~~diff
- 00b661e8 ["INT_ADD", "register:40f0:8", ["const:b661e8:8", "const:4:8"]]
- 00b661e8 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b66284 ["INT_ADD", "register:40f0:8", ["const:b66284:8", "const:4:8"]]
+ 00b66284 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b661e8 bytes 86d30394
+ 00b66284 bytes 93d30394
- 00b661e4 ["COPY", "tmp:0:8", ["const:367:8"]]
- 00b661e4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b661e4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b661e4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b66280 ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00b66280 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b66280 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b66280 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b661e4 bytes 009c0d91
+ 00b66280 bytes 002c0c91
- 00b661f0 ["COPY", "tmp:0:8", ["const:168:8"]]
- 00b661f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b661f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b661f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b6628c ["COPY", "tmp:0:8", ["const:268:8"]]
+ 00b6628c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b6628c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b6628c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b661f0 bytes 08a10591
+ 00b6628c bytes 08a10991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c9c33befd059aef50fd6624cea3eb2a"></a>

### [`00b66204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66204.md) → [`00b662a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b662a0.md) _ZN8firebase17version_registrar13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b662e0",
      "incomplete_value": true,
      "site": "00b662e0",
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
            "const:258:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66244",
      "incomplete_value": true,
      "site": "00b66244",
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
            "const:158:8"
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
      "definition_site": "00b662bc",
      "incomplete_value": true,
      "site": "00b662bc",
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
      "definition_site": "00b66220",
      "incomplete_value": true,
      "site": "00b66220",
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
      "definition_site": "00b662c4",
      "incomplete_value": false,
      "site": "00b662d8",
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
            "const:9ba:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66228",
      "incomplete_value": false,
      "site": "00b6623c",
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
            "const:97a:8"
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
      "00b662b4",
      "READ",
      [
        "storage",
        "01126158",
        null,
        "undefined8"
      ]
    ],
    [
      "00b662c4",
      "PARAM",
      [
        "storage",
        "002c097a",
        null,
        "string"
      ]
    ],
    [
      "00b662e0",
      "WRITE",
      [
        "storage",
        "01126158",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b662b4",
      "READ",
      [
        "storage",
        "01126258",
        null,
        "undefined8"
      ]
    ],
    [
      "00b662c4",
      "PARAM",
      [
        "storage",
        "002c09ba",
        null,
        "string"
      ]
    ],
    [
      "00b662e0",
      "WRITE",
      [
        "storage",
        "01126258",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6623c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66204.md#insn-00b6623c) · [`00b66244`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66204.md#insn-00b66244) · [`00b66218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66204.md#insn-00b66218)
- 新版 `00b662d8`（命令位置の公開資料なし） · `00b662e0`（命令位置の公開資料なし） · `00b662b4`（命令位置の公開資料なし）

~~~diff
- 00b6623c ["INT_ADD", "register:40f0:8", ["const:b6623c:8", "const:4:8"]]
- 00b6623c ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b662d8 ["INT_ADD", "register:40f0:8", ["const:b662d8:8", "const:4:8"]]
+ 00b662d8 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b6623c bytes 35d30394
+ 00b662d8 bytes 42d30394
- 00b66244 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:158:8"]]
- 00b66244 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b662e0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:258:8"]]
+ 00b662e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66244 bytes 80ae00f9
+ 00b662e0 bytes 802e01f9
- 00b66218 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:158:8"]]
- 00b66218 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b662b4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:258:8"]]
+ 00b662b4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b66218 bytes 81ae40f9
+ 00b662b4 bytes 812e41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3eeee9a211fcf06c43e3211a85115d3f"></a>

### [`00b66274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66274.md) → [`00b66310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66310.md) _ZN8firebase17version_registrar10GetFieldIdENS0_5FieldE

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
      "definition_site": "00b6632c",
      "incomplete_value": false,
      "site": "00b66330",
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
      "definition_site": "00b66290",
      "incomplete_value": false,
      "site": "00b66294",
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
      "definition_site": "00b6633c",
      "incomplete_value": true,
      "site": "00b66348",
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
      "definition_site": "00b662a0",
      "incomplete_value": true,
      "site": "00b662ac",
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
      "00b6632c",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b6633c",
      "DATA",
      [
        "storage",
        "01126180",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b6632c",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b6633c",
      "DATA",
      [
        "storage",
        "01126280",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66274.md#insn-00b66294) · [`00b66290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66274.md#insn-00b66290) · [`00b6629c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66274.md#insn-00b6629c)
- 新版 `00b66330`（命令位置の公開資料なし） · `00b6632c`（命令位置の公開資料なし） · `00b66338`（命令位置の公開資料なし）

~~~diff
- 00b66294 ["INT_ADD", "register:40f0:8", ["const:b66294:8", "const:4:8"]]
- 00b66294 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b66330 ["INT_ADD", "register:40f0:8", ["const:b66330:8", "const:4:8"]]
+ 00b66330 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b66294 bytes 5bd30394
+ 00b66330 bytes 68d30394
- 00b66290 ["COPY", "tmp:0:8", ["const:51e:8"]]
- 00b66290 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b66290 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b66290 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b6632c ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00b6632c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6632c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6632c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b66290 bytes 00781491
+ 00b6632c bytes 00341591
- 00b6629c ["COPY", "tmp:0:8", ["const:180:8"]]
- 00b6629c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b6629c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b6629c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b66338 ["COPY", "tmp:0:8", ["const:280:8"]]
+ 00b66338 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b66338 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b66338 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b6629c bytes 08010691
+ 00b66338 bytes 08010a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45127701307192a62604a0c1ed44f336"></a>

### [`00b662b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b662b0.md) → [`00b6634c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b6634c.md) _ZN8firebase10AppOptions11LoadDefaultEPS0_P7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5bec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bec0.md) · 呼出先 13件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00b66454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66454.md) [`00b6663c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b6663c.md) [`00b66a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66a48.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`00c5bf90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf90.md) · 呼出先 13件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00b664f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b664f0.md) [`00b666d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b666d8.md) [`00b66ae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66ae4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.10% / 新版 98.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b66394",
      "incomplete_value": true,
      "site": "00b663a4",
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
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:208:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b662f8",
      "incomplete_value": true,
      "site": "00b66308",
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
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:108:8"
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
      "definition_site": "00b66398",
      "incomplete_value": true,
      "site": "00b663a4",
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
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:218:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b662fc",
      "incomplete_value": true,
      "site": "00b66308",
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
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:118:8"
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
      "00b66394",
      "READ",
      [
        "storage",
        "01126108",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66398",
      "READ",
      [
        "storage",
        "01126118",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b66394",
      "READ",
      [
        "storage",
        "01126208",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66398",
      "READ",
      [
        "storage",
        "01126218",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b662b0.md#insn-00b66308) · [`00b662e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b662b0.md#insn-00b662e8) · [`00b662f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b662b0.md#insn-00b662f8)
- 新版 `00b663a4`（命令位置の公開資料なし） · `00b66384`（命令位置の公開資料なし） · `00b66394`（命令位置の公開資料なし）

~~~diff
- 00b66308 ["INT_ADD", "register:40f0:8", ["const:b66308:8", "const:4:8"]]
- 00b66308 ["CALL", null, ["callee:00c5ac70:8"]]
+ 00b663a4 ["INT_ADD", "register:40f0:8", ["const:b663a4:8", "const:4:8"]]
+ 00b663a4 ["CALL", null, ["callee:00c5ac70:8"]]
- 00b66308 bytes 26d20394
+ 00b663a4 bytes 33d20394
- 00b662e8 ["INT_ADD", "register:40f0:8", ["const:b662e8:8", "const:4:8"]]
- 00b662e8 ["CALL", null, ["callee:00b664f0:8"]]
+ 00b66384 ["INT_ADD", "register:40f0:8", ["const:b66384:8", "const:4:8"]]
+ 00b66384 ["CALL", null, ["callee:00b664f0:8"]]
- 00b662e8 bytes 5b000094
+ 00b66384 bytes 5b000094
- 00b662f8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:108:8"]]
- 00b662f8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b66394 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:208:8"]]
+ 00b66394 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b662f8 bytes 018540f9
+ 00b66394 bytes 010541f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7227fd451592b483a2151a98e4cb82c7"></a>

### [`00b66454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66454.md) → [`00b664f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b664f0.md) FUN_00b664f0

採用 · 移動量 `+0x9c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00b662b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b662b0.md) [`00b66cac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66cac.md) [`00b66da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66da4.md) [`00b68240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b68/00b68240.md) · 呼出先 5件 [`00b66a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66a48.md) [`00c5aea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aea0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md) [`00c5bd00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bd00.md)
- 新版 呼出元 4件 [`00b6634c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b6634c.md) [`00b66d48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66d48.md) [`00b66e40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66e40.md) [`00b682dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b68/00b682dc.md) · 呼出先 5件 [`00b66ae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66ae4.md) [`00c5af70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af70.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md) [`00c5bdd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bdd0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 81.97% / 新版 81.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 16件, `store_destination` 6件

アドレスに依存する影響 `branch_value` 4件, `store_condition` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b6650c",
      "incomplete_value": false,
      "site": "00b6650c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1126000:8"
          ],
          [
            "leaf",
            "const:288:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66470",
      "incomplete_value": false,
      "site": "00b66470",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1126000:8"
          ],
          [
            "leaf",
            "const:188:8"
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
      "definition_site": "00b66558",
      "incomplete_value": true,
      "site": "00b66558",
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
            "const:150:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b664bc",
      "incomplete_value": true,
      "site": "00b664bc",
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
            "const:50:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b665b0",
      "incomplete_value": true,
      "site": "00b665b0",
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
            "const:1b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66514",
      "incomplete_value": true,
      "site": "00b66514",
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
            "const:b0:8"
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
      "00b66504",
      "READ",
      [
        "storage",
        "01126188",
        null,
        "undefined4"
      ]
    ],
    [
      "00b6650c",
      "WRITE",
      [
        "storage",
        "01126188",
        null,
        "undefined4"
      ]
    ],
    [
      "00b66530",
      "READ",
      [
        "storage",
        "01126050",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b66504",
      "READ",
      [
        "storage",
        "01126288",
        null,
        "undefined4"
      ]
    ],
    [
      "00b6650c",
      "WRITE",
      [
        "storage",
        "01126288",
        null,
        "undefined4"
      ]
    ],
    [
      "00b66530",
      "READ",
      [
        "storage",
        "01126150",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66454.md#insn-00b66470) · [`00b664b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66454.md#insn-00b664b4) · [`00b664bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66454.md#insn-00b664bc)
- 新版 `00b6650c`（命令位置の公開資料なし） · `00b66550`（命令位置の公開資料なし） · `00b66558`（命令位置の公開資料なし）

~~~diff
- 00b66470 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:188:8"]]
- 00b66470 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
+ 00b6650c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:288:8"]]
+ 00b6650c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00b66470 bytes a98a01b9
+ 00b6650c bytes a98a02b9
- 00b664b4 ["INT_ADD", "register:40f0:8", ["const:b664b4:8", "const:4:8"]]
- 00b664b4 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00b66550 ["INT_ADD", "register:40f0:8", ["const:b66550:8", "const:4:8"]]
+ 00b66550 ["CALL", null, ["callee:00c5afe0:8"]]
- 00b664b4 bytes 97d20394
+ 00b66550 bytes a4d20394
- 00b664bc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:50:8"]]
- 00b664bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b66558 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:150:8"]]
+ 00b66558 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b664bc bytes a02a00f9
+ 00b66558 bytes a0aa00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d89be6da3de516679b001f357ebdbf6a"></a>

### [`00b66a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66a48.md) → [`00b66ae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66ae4.md) FUN_00b66ae4

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`00b662b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b662b0.md) [`00b66454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66454.md) [`00b66bf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66bf8.md) [`00b66cac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66cac.md) [`00b66da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66da4.md) · 呼出先 4件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5afd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5afd0.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5bd20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bd20.md)
- 新版 呼出元 6件 [`00b6634c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b6634c.md) [`00b664f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b664f0.md) [`00b66c94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66c94.md) [`00b66d48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66d48.md) [`00b66e40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66e40.md) · 呼出先 4件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b0a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0a0.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5bdf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bdf0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 85.05% / 新版 85.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 10件

アドレスに依存する影響 `branch_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b66b18",
      "incomplete_value": true,
      "site": "00b66b18",
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
            "const:288:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66a7c",
      "incomplete_value": true,
      "site": "00b66a7c",
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
            "const:188:8"
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
      "definition_site": "00b66b58",
      "incomplete_value": true,
      "site": "00b66b58",
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
            "const:158:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66abc",
      "incomplete_value": true,
      "site": "00b66abc",
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
            "const:58:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b66b78",
      "incomplete_value": true,
      "site": "00b66b78",
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
            "const:150:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66adc",
      "incomplete_value": true,
      "site": "00b66adc",
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
            "const:50:8"
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
      "00b66af8",
      "READ",
      [
        "storage",
        "01126188",
        null,
        "undefined4"
      ]
    ],
    [
      "00b66b08",
      "PARAM",
      [
        "storage",
        "002bbe52",
        null,
        "string"
      ]
    ],
    [
      "00b66b10",
      "READ",
      [
        "storage",
        "01126188",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00b66af8",
      "READ",
      [
        "storage",
        "01126288",
        null,
        "undefined4"
      ]
    ],
    [
      "00b66b08",
      "PARAM",
      [
        "storage",
        "002bbdfe",
        null,
        "string"
      ]
    ],
    [
      "00b66b10",
      "READ",
      [
        "storage",
        "01126288",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66a6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66a48.md#insn-00b66a6c) · [`00b66a70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66a48.md#insn-00b66a70) · [`00b66a7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66a48.md#insn-00b66a7c)
- 新版 `00b66b08`（命令位置の公開資料なし） · `00b66b0c`（命令位置の公開資料なし） · `00b66b18`（命令位置の公開資料なし）

~~~diff
- 00b66a6c ["COPY", "tmp:0:8", ["const:e52:8"]]
- 00b66a6c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b66a6c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b66a6c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b66b08 ["COPY", "tmp:0:8", ["const:dfe:8"]]
+ 00b66b08 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b66b08 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b66b08 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b66a6c bytes 00483991
+ 00b66b08 bytes 00f83791
- 00b66a70 ["INT_ADD", "register:40f0:8", ["const:b66a70:8", "const:4:8"]]
- 00b66a70 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b66b0c ["INT_ADD", "register:40f0:8", ["const:b66b0c:8", "const:4:8"]]
+ 00b66b0c ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b66a70 bytes 64d10394
+ 00b66b0c bytes 71d10394
- 00b66a7c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:188:8"]]
- 00b66a7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 00b66b18 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:288:8"]]
+ 00b66b18 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00b66a7c bytes 888a01b9
+ 00b66b18 bytes 888a02b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-149269313c241fae07ea12f9832f55a7"></a>

### [`00b66cac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66cac.md) → [`00b66d48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66d48.md) _ZN8firebase3App6CreateEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5a950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a950.md) · 呼出先 7件 [`00879c88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/00879c88.md) [`00b66454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66454.md) [`00b66a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66a48.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md)
- 新版 呼出元 1件 [`00c5aa20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aa20.md) · 呼出先 7件 [`00879ce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00879/00879ce0.md) [`00b664f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b664f0.md) [`00b66ae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66ae4.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.21% / 新版 98.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b66dc4",
      "incomplete_value": true,
      "site": "00b66dc8",
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
      "definition_site": "00b66d28",
      "incomplete_value": true,
      "site": "00b66d2c",
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b66de0",
      "incomplete_value": false,
      "site": "00b66de4",
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
            "const:cef:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66d44",
      "incomplete_value": false,
      "site": "00b66d48",
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
            "const:caf:8"
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
      "00b66db4",
      "READ",
      [
        "storage",
        "00c9b778",
        null,
        "pointer"
      ]
    ],
    [
      "00b66dc4",
      "READ",
      [
        "storage",
        "00c90200",
        "_ZN8firebase15kDefaultAppNameE",
        "pointer"
      ]
    ],
    [
      "00b66dc4",
      "PARAM",
      [
        "storage",
        "002b5932",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b66db4",
      "READ",
      [
        "storage",
        "00c9b848",
        null,
        "pointer"
      ]
    ],
    [
      "00b66dc4",
      "READ",
      [
        "storage",
        "00c902d0",
        "_ZN8firebase15kDefaultAppNameE",
        "pointer"
      ]
    ],
    [
      "00b66dc4",
      "PARAM",
      [
        "storage",
        "002b5972",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66d2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66cac.md#insn-00b66d2c) · [`00b66d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66cac.md#insn-00b66d48) · [`00b66cd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66cac.md#insn-00b66cd4)
- 新版 `00b66dc8`（命令位置の公開資料なし） · `00b66de4`（命令位置の公開資料なし） · `00b66d70`（命令位置の公開資料なし）

~~~diff
- 00b66d2c ["INT_ADD", "register:40f0:8", ["const:b66d2c:8", "const:4:8"]]
- 00b66d2c ["CALL", null, ["callee:00c5bfa0:8"]]
+ 00b66dc8 ["INT_ADD", "register:40f0:8", ["const:b66dc8:8", "const:4:8"]]
+ 00b66dc8 ["CALL", null, ["callee:00c5bfa0:8"]]
- 00b66d2c bytes 69d40394
+ 00b66dc8 bytes 76d40394
- 00b66d48 ["INT_ADD", "register:40f0:8", ["const:b66d48:8", "const:4:8"]]
- 00b66d48 ["CALL", null, ["callee:00c5ad70:8"]]
+ 00b66de4 ["INT_ADD", "register:40f0:8", ["const:b66de4:8", "const:4:8"]]
+ 00b66de4 ["CALL", null, ["callee:00c5ad70:8"]]
- 00b66d48 bytes d6cf0394
+ 00b66de4 bytes e3cf0394
- 00b66cd4 ["INT_ADD", "register:40f0:8", ["const:b66cd4:8", "const:4:8"]]
- 00b66cd4 ["CALL", null, ["callee:00b664f0:8"]]
+ 00b66d70 ["INT_ADD", "register:40f0:8", ["const:b66d70:8", "const:4:8"]]
+ 00b66d70 ["CALL", null, ["callee:00b664f0:8"]]
- 00b66cd4 bytes e0fdff97
+ 00b66d70 bytes e0fdff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66d1fb7d6d08169c30929f9b6f747b50"></a>

### [`00b66da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66da4.md) → [`00b66e40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66e40.md) _ZN8firebase3App6CreateERKNS_10AppOptionsEPKcP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bed0.md) · 呼出先 28件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md) [`00879c88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/00879c88.md) [`00b66454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66454.md)
- 新版 呼出元 1件 [`00c5bfa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bfa0.md) · 呼出先 28件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00589734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589734.md) [`00879ce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00879/00879ce0.md) [`00b664f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b664f0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 93.01% / 新版 93.01%

CFGの説明率　旧版 91.64% / 新版 91.35%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 11件

アドレスに依存する影響 `call_argument_candidate` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b67c6c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b67d0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b67d68"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b66e90",
      "PARAM",
      [
        "storage",
        "0029fa86",
        null,
        "string"
      ]
    ],
    [
      "00b66ea4",
      "READ",
      [
        "storage",
        "00c9b7f8",
        null,
        "pointer"
      ]
    ],
    [
      "00b66eac",
      "PARAM",
      [
        "storage",
        "002bd1be",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b66e90",
      "PARAM",
      [
        "storage",
        "0029fa39",
        null,
        "string"
      ]
    ],
    [
      "00b66ea4",
      "READ",
      [
        "storage",
        "00c9b8c8",
        null,
        "pointer"
      ]
    ],
    [
      "00b66eac",
      "PARAM",
      [
        "storage",
        "002bd16a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66dfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66da4.md#insn-00b66dfc) · [`00b66e1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66da4.md#insn-00b66e1c) · [`00b66e58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b66/00b66da4.md#insn-00b66e58)
- 新版 `00b66e98`（命令位置の公開資料なし） · `00b66eb8`（命令位置の公開資料なし） · `00b66ef4`（命令位置の公開資料なし）

~~~diff
- 00b66dfc ["INT_ADD", "register:40f0:8", ["const:b66dfc:8", "const:4:8"]]
- 00b66dfc ["CALL", null, ["callee:00c5ad70:8"]]
+ 00b66e98 ["INT_ADD", "register:40f0:8", ["const:b66e98:8", "const:4:8"]]
+ 00b66e98 ["CALL", null, ["callee:00c5ad70:8"]]
- 00b66dfc bytes a9cf0394
+ 00b66e98 bytes b6cf0394
- 00b66e1c ["INT_ADD", "register:40f0:8", ["const:b66e1c:8", "const:4:8"]]
- 00b66e1c ["CALL", null, ["callee:00c5b200:8"]]
+ 00b66eb8 ["INT_ADD", "register:40f0:8", ["const:b66eb8:8", "const:4:8"]]
+ 00b66eb8 ["CALL", null, ["callee:00c5b200:8"]]
- 00b66e1c bytes c5d00394
+ 00b66eb8 bytes d2d00394
- 00b66e58 ["INT_ADD", "register:40f0:8", ["const:b66e58:8", "const:4:8"]]
- 00b66e58 ["CALL", null, ["callee:00c5ac70:8"]]
+ 00b66ef4 ["INT_ADD", "register:40f0:8", ["const:b66ef4:8", "const:4:8"]]
+ 00b66ef4 ["CALL", null, ["callee:00c5ac70:8"]]
- 00b66e58 bytes 52cf0394
+ 00b66ef4 bytes 5fcf0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55c971ed05295199524773c20f7d83ca"></a>

### [`00b68048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b68/00b68048.md) → [`00b680e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b68/00b680e4.md) _ZN8firebase3App15RegisterLibraryEPKcS2_Pv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5b7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b7b0.md) · 呼出先 5件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00c5aba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aba0.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b720.md)
- 新版 呼出元 1件 [`00c5b880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b880.md) · 呼出先 5件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00c5ac70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ac70.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b7f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 91.18% / 新版 91.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6810c",
      "incomplete_value": false,
      "site": "00b68110",
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
            "const:adb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68070",
      "incomplete_value": false,
      "site": "00b68074",
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
            "const:b2f:8"
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
      "definition_site": "00b6811c",
      "incomplete_value": true,
      "site": "00b68128",
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
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:258:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68080",
      "incomplete_value": true,
      "site": "00b6808c",
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
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:158:8"
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
      "definition_site": "00b68120",
      "incomplete_value": true,
      "site": "00b68128",
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
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:268:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68084",
      "incomplete_value": true,
      "site": "00b6808c",
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
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:168:8"
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
      "00b68104",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b68078"
      ]
    ],
    [
      "00b6810c",
      "PARAM",
      [
        "storage",
        "002b8b2f",
        null,
        "string"
      ]
    ],
    [
      "00b6811c",
      "READ",
      [
        "storage",
        "01126158",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b68104",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b68114"
      ]
    ],
    [
      "00b6810c",
      "PARAM",
      [
        "storage",
        "002b8adb",
        null,
        "string"
      ]
    ],
    [
      "00b6811c",
      "READ",
      [
        "storage",
        "01126258",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b68/00b68048.md#insn-00b68074) · [`00b6808c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b68/00b68048.md#insn-00b6808c) · [`00b680a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b68/00b68048.md#insn-00b680a8)
- 新版 `00b68110`（命令位置の公開資料なし） · `00b68128`（命令位置の公開資料なし） · `00b68144`（命令位置の公開資料なし）

~~~diff
- 00b68074 ["INT_ADD", "register:40f0:8", ["const:b68074:8", "const:4:8"]]
- 00b68074 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b68110 ["INT_ADD", "register:40f0:8", ["const:b68110:8", "const:4:8"]]
+ 00b68110 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b68074 bytes e3cb0394
+ 00b68110 bytes f0cb0394
- 00b6808c ["INT_ADD", "register:40f0:8", ["const:b6808c:8", "const:4:8"]]
- 00b6808c ["CALL", null, ["callee:00c5ac70:8"]]
+ 00b68128 ["INT_ADD", "register:40f0:8", ["const:b68128:8", "const:4:8"]]
+ 00b68128 ["CALL", null, ["callee:00c5ac70:8"]]
- 00b6808c bytes c5ca0394
+ 00b68128 bytes d2ca0394
- 00b680a8 ["INT_ADD", "register:40f0:8", ["const:b680a8:8", "const:4:8"]]
- 00b680a8 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00b68144 ["INT_ADD", "register:40f0:8", ["const:b68144:8", "const:4:8"]]
+ 00b68144 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00b680a8 bytes d6cb0394
+ 00b68144 bytes e3cb0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ada7b98ea82a9e124225808f1ac60727"></a>

### [`00b6815c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b68/00b6815c.md) → [`00b681f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b68/00b681f8.md) _ZN8firebase3App31SetDataCollectionDefaultEnabledEb

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b3c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b3c0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b490.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b68210",
      "incomplete_value": true,
      "site": "00b68210",
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
      "definition_site": "00b68174",
      "incomplete_value": true,
      "site": "00b68174",
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
      "definition_site": "00b6822c",
      "incomplete_value": true,
      "site": "00b6823c",
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
                "const:1a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68190",
      "incomplete_value": true,
      "site": "00b681a0",
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
                "const:a0:8"
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
      "00b6820c",
      "READ",
      [
        "storage",
        "011260a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6822c",
      "READ",
      [
        "storage",
        "011260a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68260",
      "PARAM",
      [
        "storage",
        "002bd1de",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6820c",
      "READ",
      [
        "storage",
        "011261a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6822c",
      "READ",
      [
        "storage",
        "011261a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68260",
      "PARAM",
      [
        "storage",
        "002bd18a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b681a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b68/00b6815c.md#insn-00b681a0) · [`00b68170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b68/00b6815c.md#insn-00b68170) · [`00b68188`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b68/00b6815c.md#insn-00b68188)
- 新版 `00b6823c`（命令位置の公開資料なし） · `00b6820c`（命令位置の公開資料なし） · `00b68224`（命令位置の公開資料なし）

~~~diff
- 00b681a0 ["INT_ADD", "register:40f0:8", ["const:b681a0:8", "const:4:8"]]
- 00b681a0 ["CALL", null, ["callee:00574d2c:8"]]
+ 00b6823c ["INT_ADD", "register:40f0:8", ["const:b6823c:8", "const:4:8"]]
+ 00b6823c ["CALL", null, ["callee:00574d2c:8"]]
- 00b681a0 bytes d332e897
+ 00b6823c bytes bc32e897
- 00b68170 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:a0:8"]]
- 00b68170 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6820c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:1a0:8"]]
+ 00b6820c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b68170 bytes c85240f9
+ 00b6820c bytes c8d240f9
- 00b68188 ["INT_ADD", "register:40f0:8", ["const:b68188:8", "const:4:8"]]
- 00b68188 ["CALL", null, ["callee:00c5b490:8"]]
+ 00b68224 ["INT_ADD", "register:40f0:8", ["const:b68224:8", "const:4:8"]]
+ 00b68224 ["CALL", null, ["callee:00c5b490:8"]]
- 00b68188 bytes 8ecc0394
+ 00b68224 bytes 9bcc0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00bc42c7d90b9c89c7984ec99ddfca00"></a>

### [`00b681d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b68/00b681d0.md) → [`00b6826c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b68/00b6826c.md) _ZNK8firebase3App30IsDataCollectionDefaultEnabledEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5b3c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b3c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00497a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b490.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b68280",
      "incomplete_value": true,
      "site": "00b68280",
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
      "definition_site": "00b681e4",
      "incomplete_value": true,
      "site": "00b681e4",
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
      "definition_site": "00b68298",
      "incomplete_value": true,
      "site": "00b682a4",
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
                "const:198:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b681fc",
      "incomplete_value": true,
      "site": "00b68208",
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
                "const:98:8"
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
      "00b6827c",
      "READ",
      [
        "storage",
        "01126098",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68298",
      "READ",
      [
        "storage",
        "01126098",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6827c",
      "READ",
      [
        "storage",
        "01126198",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68298",
      "READ",
      [
        "storage",
        "01126198",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b68/00b681d0.md#insn-00b68208) · [`00b681e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b68/00b681d0.md#insn-00b681e0) · [`00b681f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b68/00b681d0.md#insn-00b681f4)
- 新版 `00b682a4`（命令位置の公開資料なし） · `00b6827c`（命令位置の公開資料なし） · `00b68290`（命令位置の公開資料なし）

~~~diff
- 00b68208 ["INT_ADD", "register:40f0:8", ["const:b68208:8", "const:4:8"]]
- 00b68208 ["CALL", null, ["callee:00497a88:8"]]
+ 00b682a4 ["INT_ADD", "register:40f0:8", ["const:b682a4:8", "const:4:8"]]
+ 00b682a4 ["CALL", null, ["callee:00497a88:8"]]
- 00b68208 bytes 10bee497
+ 00b682a4 bytes f9bde497
- 00b681e0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:98:8"]]
- 00b681e0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6827c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:198:8"]]
+ 00b6827c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b681e0 bytes 884e40f9
+ 00b6827c bytes 88ce40f9
- 00b681f4 ["INT_ADD", "register:40f0:8", ["const:b681f4:8", "const:4:8"]]
- 00b681f4 ["CALL", null, ["callee:00c5b490:8"]]
+ 00b68290 ["INT_ADD", "register:40f0:8", ["const:b68290:8", "const:4:8"]]
+ 00b68290 ["CALL", null, ["callee:00c5b490:8"]]
- 00b681f4 bytes 73cc0394
+ 00b68290 bytes 80cc0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18c8a02f4e2b76c49da6800a48f77f6c"></a>

### [`00b687e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b68/00b687e0.md) → [`00b6887c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b68/00b6887c.md) _ZN8firebase10AppOptions18LoadFromJsonConfigEPKcPS0_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 15件 [`00879c88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/00879c88.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)
- 新版 呼出元 0件  · 呼出先 15件 [`00879ce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00879/00879ce0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 91.87% / 新版 91.87%

CFGの説明率　旧版 78.45% / 新版 78.02%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 15件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b68814"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b68894"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b68898"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b68814",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "00b688d4",
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ],
    [
      "00b688d4",
      "PARAM",
      [
        "storage",
        "0030bcd8",
        "_ZN8firebase3fbs29google_services_resource_dataE",
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b688b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "00b688d4",
      "READ",
      [
        "storage",
        "00c9b810",
        null,
        "pointer"
      ]
    ],
    [
      "00b688d4",
      "PARAM",
      [
        "storage",
        "0030bd18",
        "_ZN8firebase3fbs29google_services_resource_dataE",
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b68/00b687e0.md#insn-00b68814) · [`00b68818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b68/00b687e0.md#insn-00b68818) · [`00b68848`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b68/00b687e0.md#insn-00b68848)
- 新版 `00b688b4`（命令位置の公開資料なし） · `00b688e4`（命令位置の公開資料なし）

~~~diff
- 00b68814 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b68814 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffa0:8"]]
- 00b68814 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b68814 bytes a8031af8
- 00b68818 ["INT_ADD", "register:40f0:8", ["const:b68818:8", "const:4:8"]]
- 00b68818 ["CALL", null, ["callee:00c5b960:8"]]
+ 00b688b4 ["INT_ADD", "register:40f0:8", ["const:b688b4:8", "const:4:8"]]
+ 00b688b4 ["CALL", null, ["callee:00c5b960:8"]]
- 00b68818 bytes 1ecc0394
+ 00b688b4 bytes 2bcc0394
- 00b68848 ["INT_ADD", "register:40f0:8", ["const:b68848:8", "const:4:8"]]
- 00b68848 ["CALL", null, ["callee:00c5bfe0:8"]]
+ 00b688e4 ["INT_ADD", "register:40f0:8", ["const:b688e4:8", "const:4:8"]]
+ 00b688e4 ["CALL", null, ["callee:00c5bfe0:8"]]
- 00b68848 bytes b2cd0394
+ 00b688e4 bytes bfcd0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bfb86a7752e518e0aceb0be247557f0b"></a>

### [`00b68fc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b68/00b68fc0.md) → [`00b6905c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b69/00b6905c.md) _ZN11flatbuffers10IDLOptionsC2Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b890.md) · 呼出先 1件 [`00c5b5c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5c0.md)
- 新版 呼出元 1件 [`00c5b960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b960.md) · 呼出先 1件 [`00c5b690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b690.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 89.13% / 新版 89.13%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b6906c",
      "incomplete_value": true,
      "site": "00b6909c",
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
                "const:c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68fd0",
      "incomplete_value": true,
      "site": "00b69000",
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
                "const:80:8"
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
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b69058"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6905c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b6906c",
      "READ",
      [
        "storage",
        "002c4080",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b68fec",
      "PARAM",
      [
        "storage",
        "002a8545",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b69014",
      "PARAM",
      [
        "storage",
        "002a00d6",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b6906c",
      "READ",
      [
        "storage",
        "002c40c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b69088",
      "PARAM",
      [
        "storage",
        "002a84e9",
        null,
        "string"
      ]
    ],
    [
      "00b690b0",
      "PARAM",
      [
        "storage",
        "002a0089",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b69008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b68/00b68fc0.md#insn-00b69008) · [`00b69040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b68/00b68fc0.md#insn-00b69040) · [`00b69058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b68/00b68fc0.md#insn-00b69058)
- 新版 `00b690a4`（命令位置の公開資料なし） · `00b690dc`（命令位置の公開資料なし）

~~~diff
- 00b69008 ["INT_ADD", "register:40f0:8", ["const:b69008:8", "const:4:8"]]
- 00b69008 ["CALL", null, ["callee:00c5b690:8"]]
+ 00b690a4 ["INT_ADD", "register:40f0:8", ["const:b690a4:8", "const:4:8"]]
+ 00b690a4 ["CALL", null, ["callee:00c5b690:8"]]
- 00b69008 bytes 6ec90394
+ 00b690a4 bytes 7bc90394
- 00b69040 ["INT_ADD", "register:40f0:8", ["const:b69040:8", "const:4:8"]]
- 00b69040 ["CALL", null, ["callee:00c5b690:8"]]
+ 00b690dc ["INT_ADD", "register:40f0:8", ["const:b690dc:8", "const:4:8"]]
+ 00b690dc ["CALL", null, ["callee:00c5b690:8"]]
- 00b69040 bytes 60c90394
+ 00b690dc bytes 6dc90394
- 00b69058 ["COPY", "tmp:0:4", ["register:40a0:4"]]
- 00b69058 ["INT_ADD", "tmp:1:8", ["register:4098:8", "const:ffffffffffffffd8:8"]]
- 00b69058 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 00b69058 bytes 74821d78
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42ba3c883797cbab34395a824e447dee"></a>

### [`00b69130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b69/00b69130.md) → [`00b691cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b69/00b691cc.md) _ZN11flatbuffers6ParserC2ERKNS_10IDLOptionsE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b900.md) · 呼出先 8件 [`006394bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00639/006394bc.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)
- 新版 呼出元 1件 [`00c5b9d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b9d0.md) · 呼出先 8件 [`006394fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00639/006394fc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 27.80% / 新版 27.80%

CFGの説明率　旧版 3.05% / 新版 3.06%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_condition` 2件, `unresolved_branch_alignment` 57件, `unresolved_call_alignment` 84件, `unresolved_store_alignment` 446件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6916c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b691ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b691ec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b69164",
      "READ",
      [
        "storage",
        "002c3130",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6916c",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00b692e4",
      "READ",
      [
        "storage",
        "002c42e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b69200",
      "READ",
      [
        "storage",
        "002c3170",
        null,
        null
      ]
    ],
    [
      "00b69208",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00b692e4",
      "READ",
      [
        "storage",
        "002c4320",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6916c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b69/00b69130.md#insn-00b6916c) · [`00b691ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b69/00b69130.md#insn-00b691ec) · [`00b691f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b69/00b69130.md#insn-00b691f0)

~~~diff
- 00b6916c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 00b6916c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00b6916c bytes e91700f9
- 00b691ec ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:50:8"]]
- 00b691ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5020:16"]]
- 00b691ec ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00b691ec ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5020:16"]]
- 00b691ec bytes 018702ad
- 00b691f0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b691f0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b691f0 ["INT_ADD", "tmp:2:8", ["register:40c0:8", "const:70:8"]]
- 00b691f0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b691f0 bytes 1fc30139
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c20ba23af0132a4e47bdcb407355e5fb"></a>

### [`00b6ab34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6a/00b6ab34.md) → [`00b6abd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6a/00b6abd0.md) _ZN11flatbuffers10IDLOptionsD2Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b8a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b8a0.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00c5b970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b970.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 89.51% / 新版 89.51%

CFGの説明率　旧版 31.53% / 新版 31.82%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 6件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6ab34"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6ab38"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6ab38"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6ab34",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6ab38",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6ab3c",
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
      "00b6abd0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b6abd4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b6abd8",
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

- 旧版 [`00b6ab34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6a/00b6ab34.md#insn-00b6ab34) · [`00b6ab38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6a/00b6ab34.md#insn-00b6ab38) · [`00b6ab3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6a/00b6ab34.md#insn-00b6ab3c)

~~~diff
- 00b6ab34 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b6ab34 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b6ab34 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b6ab34 bytes f50f1df8
- 00b6ab38 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b6ab38 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b6ab38 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b6ab38 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6ab38 bytes f44f01a9
- 00b6ab3c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b6ab3c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b6ab3c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b6ab3c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6ab3c bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f473cf416150375910f4271998793d1d"></a>

### [`00b6adbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6a/00b6adbc.md) → [`00b6ae58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6a/00b6ae58.md) _ZN8firebase10AppOptions28PopulateRequiredWithDefaultsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b930.md) · 呼出先 5件 [`00879c88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/00879c88.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5b0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0b0.md) [`00c5bec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bec0.md)
- 新版 呼出元 1件 [`00c5ba00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5ba00.md) · 呼出先 5件 [`00879ce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00879/00879ce0.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b180.md) [`00c5bf90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 95.80% / 新版 95.80%

CFGの説明率　旧版 28.05% / 新版 28.05%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6ade0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b6ae7c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6ae1c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6ade0",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6ae1c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6b05c"
      ]
    ],
    [
      "unmatched:00b6ae48",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6ae90"
      ]
    ]
  ],
  "added": [
    [
      "00b6ae7c",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00b6aeb8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6b05c"
      ]
    ],
    [
      "00b6aee4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6ae90"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6ade0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6a/00b6adbc.md#insn-00b6ade0) · [`00b6ae1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6a/00b6adbc.md#insn-00b6ae1c) · [`00b6ae48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6a/00b6adbc.md#insn-00b6ae48)

~~~diff
- 00b6ade0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b6ade0 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffd8:8"]]
- 00b6ade0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b6ade0 bytes a8831df8
- 00b6ae1c ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b6ae1c ["CBRANCH", null, ["local:b47:8", "tmp:0:1"]]
- 00b6ae1c bytes 280d00b4
- 00b6ae48 ["INT_NOTEQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00b6ae48 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b6ae48 bytes 69fdffb5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e53e621b7dfb7256c8e03dff9e79bd3"></a>

### [`00b6aff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6a/00b6aff8.md) → [`00b6b094`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6b/00b6b094.md) _ZN11flatbuffers10IDLOptionsC2ERKS0_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b880.md) · 呼出先 3件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md) [`00c5b5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5b0.md)
- 新版 呼出元 1件 [`00c5b950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b950.md) · 呼出先 3件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md) [`00c5b680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b680.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 97.67% / 新版 97.67%

CFGの説明率　旧版 45.00% / 新版 45.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 3件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6b24c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b6b2e8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6b124"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6b124",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6b340"
      ]
    ]
  ],
  "added": [
    [
      "00b6b1c0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6b340"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6b124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6a/00b6aff8.md#insn-00b6b124) · [`00b6b1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6a/00b6aff8.md#insn-00b6b1d0)
- 新版 `00b6b1c0`（命令位置の公開資料なし） · `00b6b26c`（命令位置の公開資料なし）

~~~diff
- 00b6b124 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b6b124 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00b6b124 ["CBRANCH", null, ["local:b13:8", "tmp:1:1"]]
- 00b6b124 bytes 080c0054
+ 00b6b1c0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b6b1c0 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
+ 00b6b1c0 ["CBRANCH", null, ["local:b13:8", "tmp:1:1"]]
+ 00b6b1c0 bytes 080c0054
- 00b6b1d0 ["INT_ADD", "register:40f0:8", ["const:b6b1d0:8", "const:4:8"]]
- 00b6b1d0 ["CALL", null, ["callee:00c5b680:8"]]
+ 00b6b26c ["INT_ADD", "register:40f0:8", ["const:b6b26c:8", "const:4:8"]]
+ 00b6b26c ["CALL", null, ["callee:00c5b680:8"]]
- 00b6b1d0 bytes f8c00394
+ 00b6b26c bytes 05c10394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bbc43124c922851b626e683deb652e08"></a>

### [`00b6c018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6c/00b6c018.md) → [`00b6c0b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6c/00b6c0b4.md) _ZNK8firebase3fbs10ClientInfo6VerifyERN11flatbuffers16VerifierTemplateILb0EEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b950.md) · 呼出先 1件 [`00c5b9c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b9c0.md)
- 新版 呼出元 1件 [`00c5ba20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5ba20.md) · 呼出先 1件 [`00c5ba90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5ba90.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 84.14% / 新版 84.14%

CFGの説明率　旧版 67.62% / 新版 68.27%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 3件, `unresolved_branch_alignment` 8件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6c01c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6c01c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b6c0b8"
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
      "unmatched:00b6c01c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6c030",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6c0d8"
      ]
    ],
    [
      "unmatched:00b6c048",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6c2e8"
      ]
    ]
  ],
  "added": [
    [
      "00b6c0b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b6c0cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6c0d8"
      ]
    ],
    [
      "00b6c0e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6c2e8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6c01c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6c/00b6c018.md#insn-00b6c01c) · [`00b6c030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6c/00b6c018.md#insn-00b6c030) · [`00b6c048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6c/00b6c018.md#insn-00b6c048)

~~~diff
- 00b6c01c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b6c01c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b6c01c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b6c01c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6c01c bytes fd7b01a9
- 00b6c030 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 00b6c030 bytes 60000054
- 00b6c048 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b6c048 ["CBRANCH", null, ["local:b61:8", "tmp:0:1"]]
- 00b6c048 bytes 23100054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f72593cbf3440663bc401e8ccc141647"></a>

### [`00b6d568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6d568.md) → [`00b6d604`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6d604.md) _ZN11flatbuffers11SymbolTableINS_10ServiceDefEED2Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b8b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b8b0.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5b870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b870.md) [`00c5ba30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba30.md) [`00c5ba80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba80.md)
- 新版 呼出元 1件 [`00c5b980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b980.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5b940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b940.md) [`00c5bb00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bb00.md) [`00c5bb50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bb50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 94.83% / 新版 94.83%

CFGの説明率　旧版 33.33% / 新版 29.03%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6d5e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6d630"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6d648"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6d5e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d674"
      ]
    ],
    [
      "unmatched:00b6d630",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d654"
      ]
    ],
    [
      "unmatched:00b6d648",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d62c"
      ]
    ]
  ],
  "added": [
    [
      "00b6d684",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d674"
      ]
    ],
    [
      "00b6d6cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d654"
      ]
    ],
    [
      "00b6d6e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d62c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6d568.md#insn-00b6d5e8) · [`00b6d630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6d568.md#insn-00b6d630) · [`00b6d63c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6d568.md#insn-00b6d63c)
- 新版 `00b6d6d8`（命令位置の公開資料なし）

~~~diff
- 00b6d5e8 ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
- 00b6d5e8 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b6d5e8 bytes 95ffffb4
- 00b6d630 ["INT_EQUAL", "tmp:0:1", ["register:40b0:8", "const:0:8"]]
- 00b6d630 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b6d630 bytes 56fcffb4
- 00b6d63c ["INT_ADD", "register:40f0:8", ["const:b6d63c:8", "const:4:8"]]
- 00b6d63c ["CALL", null, ["callee:00c57f80:8"]]
+ 00b6d6d8 ["INT_ADD", "register:40f0:8", ["const:b6d6d8:8", "const:4:8"]]
+ 00b6d6d8 ["CALL", null, ["callee:00c57f80:8"]]
- 00b6d63c bytes 1daa0394
+ 00b6d6d8 bytes 2aaa0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6f657585e2dfed32f854631f2fcf2e7"></a>

### [`00b6db24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6db24.md) → [`00b6dbc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6dbc0.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers5ValueEEENS_19__map_value_com

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00c5ba50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba50.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ba50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba50.md)
- 新版 呼出元 1件 [`00c5bb20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bb20.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bb20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bb20.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 40.00% / 新版 28.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b6db58",
      "incomplete_value": true,
      "site": "00b6db5c",
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
    "ordinal": 2,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b6db5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6db24.md#insn-00b6db5c) · [`00b6db24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6db24.md#insn-00b6db24) · [`00b6db40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6db24.md#insn-00b6db40)
- 新版 `00b6dbf8`（命令位置の公開資料なし） · `00b6dbc0`（命令位置の公開資料なし） · `00b6dbdc`（命令位置の公開資料なし）

~~~diff
- 00b6db5c ["INT_ADD", "register:40f0:8", ["const:b6db5c:8", "const:4:8"]]
- 00b6db5c ["CALL", null, ["callee:00c57f80:8"]]
+ 00b6dbf8 ["INT_ADD", "register:40f0:8", ["const:b6dbf8:8", "const:4:8"]]
+ 00b6dbf8 ["CALL", null, ["callee:00c57f80:8"]]
- 00b6db5c bytes d5a80394
+ 00b6dbf8 bytes e2a80394
- 00b6db24 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b6db24 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b6dbc0 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b6dbc0 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00b6db24 bytes 610200b4
+ 00b6dbc0 bytes 610200b4
- 00b6db40 ["INT_ADD", "register:40f0:8", ["const:b6db40:8", "const:4:8"]]
- 00b6db40 ["CALL", null, ["callee:00c5bb20:8"]]
+ 00b6dbdc ["INT_ADD", "register:40f0:8", ["const:b6dbdc:8", "const:4:8"]]
+ 00b6dbdc ["CALL", null, ["callee:00c5bb20:8"]]
- 00b6db40 bytes c4b70394
+ 00b6dbdc bytes d1b70394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c633150d42298db0c6dc9b3ac3382d60"></a>

### [`00b6db74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6db74.md) → [`00b6dc10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6dc10.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers10ServiceDefEEENS_19__map_val

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00c5ba30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba30.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ba30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba30.md)
- 新版 呼出元 1件 [`00c5bb00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bb00.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bb00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bb00.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 22.22% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6dc24",
      "incomplete_value": true,
      "site": "00b6dc2c",
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

- 旧版 [`00b6db90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6db74.md#insn-00b6db90) · [`00b6db74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6db74.md#insn-00b6db74) · [`00b6db9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6db74.md#insn-00b6db9c)
- 新版 `00b6dc2c`（命令位置の公開資料なし） · `00b6dc10`（命令位置の公開資料なし） · `00b6dc38`（命令位置の公開資料なし）

~~~diff
- 00b6db90 ["INT_ADD", "register:40f0:8", ["const:b6db90:8", "const:4:8"]]
- 00b6db90 ["CALL", null, ["callee:00c5bb00:8"]]
+ 00b6dc2c ["INT_ADD", "register:40f0:8", ["const:b6dc2c:8", "const:4:8"]]
+ 00b6dc2c ["CALL", null, ["callee:00c5bb00:8"]]
- 00b6db90 bytes a8b70394
+ 00b6dc2c bytes b5b70394
- 00b6db74 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b6db74 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 00b6dc10 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b6dc10 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b6db74 bytes 610200b4
+ 00b6dc10 bytes 610200b4
- 00b6db9c ["INT_ADD", "register:40f0:8", ["const:b6db9c:8", "const:4:8"]]
- 00b6db9c ["CALL", null, ["callee:00c5bb00:8"]]
+ 00b6dc38 ["INT_ADD", "register:40f0:8", ["const:b6dc38:8", "const:4:8"]]
+ 00b6dc38 ["CALL", null, ["callee:00c5bb00:8"]]
- 00b6db9c bytes a5b70394
+ 00b6dc38 bytes b2b70394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4074dad86d0f057822d891c8dba32431"></a>

### [`00b6dbc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6dbc4.md) → [`00b6dc60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6dc60.md) _ZN11flatbuffers7EnumValD2Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b920.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ba50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba50.md)
- 新版 呼出元 1件 [`00c5b9f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b9f0.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bb20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bb20.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 44.44% / 新版 41.03%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6dbc4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6dbc8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6dbc8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6dbc4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6dbc8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6dbcc",
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
      "00b6dc60",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b6dc64",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b6dc68",
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

- 旧版 [`00b6dbc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6dbc4.md#insn-00b6dbc4) · [`00b6dbc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6dbc4.md#insn-00b6dbc8) · [`00b6dbcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6dbc4.md#insn-00b6dbcc)

~~~diff
- 00b6dbc4 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b6dbc4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b6dbc4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b6dbc4 bytes f50f1df8
- 00b6dbc8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b6dbc8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b6dbc8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b6dbc8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6dbc8 bytes f44f01a9
- 00b6dbcc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b6dbcc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b6dbcc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b6dbcc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6dbcc bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09c7815b2d5d9921a93520bf5b05f522"></a>

### [`00b6dd10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6dd10.md) → [`00b6ddac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6ddac.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumDefEEENS_19__map_value_c

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00c5ba60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba60.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ba60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba60.md)
- 新版 呼出元 1件 [`00c5bb30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bb30.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bb30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bb30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 28.57% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6ddc0",
      "incomplete_value": true,
      "site": "00b6ddc8",
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

- 旧版 [`00b6dd2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6dd10.md#insn-00b6dd2c) · [`00b6dd10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6dd10.md#insn-00b6dd10) · [`00b6dd38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6dd10.md#insn-00b6dd38)
- 新版 `00b6ddc8`（命令位置の公開資料なし） · `00b6ddac`（命令位置の公開資料なし） · `00b6ddd4`（命令位置の公開資料なし）

~~~diff
- 00b6dd2c ["INT_ADD", "register:40f0:8", ["const:b6dd2c:8", "const:4:8"]]
- 00b6dd2c ["CALL", null, ["callee:00c5bb30:8"]]
+ 00b6ddc8 ["INT_ADD", "register:40f0:8", ["const:b6ddc8:8", "const:4:8"]]
+ 00b6ddc8 ["CALL", null, ["callee:00c5bb30:8"]]
- 00b6dd2c bytes 4db70394
+ 00b6ddc8 bytes 5ab70394
- 00b6dd10 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b6dd10 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00b6ddac ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b6ddac ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b6dd10 bytes 610200b4
+ 00b6ddac bytes 610200b4
- 00b6dd38 ["INT_ADD", "register:40f0:8", ["const:b6dd38:8", "const:4:8"]]
- 00b6dd38 ["CALL", null, ["callee:00c5bb30:8"]]
+ 00b6ddd4 ["INT_ADD", "register:40f0:8", ["const:b6ddd4:8", "const:4:8"]]
+ 00b6ddd4 ["CALL", null, ["callee:00c5bb30:8"]]
- 00b6dd38 bytes 4ab70394
+ 00b6ddd4 bytes 57b70394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75822cae5d7db4caa542d2cf297ad15a"></a>

### [`00b6dee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6dee0.md) → [`00b6df7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6d/00b6df7c.md) _ZN20google_play_services10InitializeEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bd00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bd00.md) · 呼出先 17件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md)
- 新版 呼出元 1件 [`00c5bdd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bdd0.md) · 呼出先 17件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_destination, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 76.45% / 新版 76.45%

CFGの説明率　旧版 43.55% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 12件, `store_condition` 3件, `store_destination` 2件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 4件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 9件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b6dfbc",
      "incomplete_value": false,
      "site": "00b6dfbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1126000:8"
          ],
          [
            "leaf",
            "const:290:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6df20",
      "incomplete_value": false,
      "site": "00b6df20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1126000:8"
          ],
          [
            "leaf",
            "const:190:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b6e00c",
      "incomplete_value": true,
      "site": "00b6e00c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c8:8"
          ],
          [
            "leaf",
            "const:298:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6df70",
      "incomplete_value": true,
      "site": "00b6df70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c8:8"
          ],
          [
            "leaf",
            "const:198:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6e0b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b6dfb0",
      "READ",
      [
        "storage",
        "01126190",
        null,
        "undefined4"
      ]
    ],
    [
      "00b6dfb4",
      "READ",
      [
        "storage",
        "01126198",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6dfbc",
      "WRITE",
      [
        "storage",
        "01126190",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00b6dfb0",
      "READ",
      [
        "storage",
        "01126290",
        null,
        "undefined4"
      ]
    ],
    [
      "00b6dfb4",
      "READ",
      [
        "storage",
        "01126298",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6dfbc",
      "WRITE",
      [
        "storage",
        "01126290",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6df20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6dee0.md#insn-00b6df20) · [`00b6df70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6dee0.md#insn-00b6df70) · [`00b6dfbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6dee0.md#insn-00b6dfbc)
- 新版 `00b6dfbc`（命令位置の公開資料なし） · `00b6e00c`（命令位置の公開資料なし） · `00b6e058`（命令位置の公開資料なし）

~~~diff
- 00b6df20 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:190:8"]]
- 00b6df20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 00b6dfbc ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:290:8"]]
+ 00b6dfbc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00b6df20 bytes 089301b9
+ 00b6dfbc bytes 089302b9
- 00b6df70 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:198:8"]]
- 00b6df70 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
+ 00b6e00c ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:298:8"]]
+ 00b6e00c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00b6df70 bytes 35cf00f9
+ 00b6e00c bytes 354f01f9
- 00b6dfbc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:810:8"]]
- 00b6dfbc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6e058 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:8e0:8"]]
+ 00b6e058 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6dfbc bytes 290944f9
+ 00b6e058 bytes 297144f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dba74e58f159b5569a59d14b44519faf"></a>

### [`00b6e2ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6e/00b6e2ec.md) → [`00b6e388`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6e/00b6e388.md) _ZN20google_play_services9TerminateEP7_JNIEnv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5bd20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bd20.md) · 呼出先 7件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5ac50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac50.md) [`00c5ade0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ade0.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 1件 [`00c5bdf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bdf0.md) · 呼出先 7件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md) [`00c5ad20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad20.md) [`00c5aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aeb0.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 80.82% / 新版 80.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 4件, `store_destination` 5件

アドレスに依存する影響 `branch_value` 2件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b6e3a8",
      "incomplete_value": true,
      "site": "00b6e3a8",
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
            "const:290:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e30c",
      "incomplete_value": true,
      "site": "00b6e30c",
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
            "const:190:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b6e40c",
      "incomplete_value": true,
      "site": "00b6e40c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b0:8"
          ],
          [
            "leaf",
            "const:2b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e370",
      "incomplete_value": true,
      "site": "00b6e370",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b0:8"
          ],
          [
            "leaf",
            "const:1b0:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b6e434",
      "incomplete_value": true,
      "site": "00b6e434",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b0:8"
          ],
          [
            "leaf",
            "const:2d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e398",
      "incomplete_value": true,
      "site": "00b6e398",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b0:8"
          ],
          [
            "leaf",
            "const:1d0:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b6e39c",
      "READ",
      [
        "storage",
        "01126190",
        null,
        "undefined4"
      ]
    ],
    [
      "00b6e3a8",
      "WRITE",
      [
        "storage",
        "01126190",
        null,
        "undefined4"
      ]
    ],
    [
      "00b6e3b4",
      "READ",
      [
        "storage",
        "01126198",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6e39c",
      "READ",
      [
        "storage",
        "01126290",
        null,
        "undefined4"
      ]
    ],
    [
      "00b6e3a8",
      "WRITE",
      [
        "storage",
        "01126290",
        null,
        "undefined4"
      ]
    ],
    [
      "00b6e3b4",
      "READ",
      [
        "storage",
        "01126298",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e30c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6e/00b6e2ec.md#insn-00b6e30c) · [`00b6e318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6e/00b6e2ec.md#insn-00b6e318) · [`00b6e33c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6e/00b6e2ec.md#insn-00b6e33c)
- 新版 `00b6e3a8`（命令位置の公開資料なし） · `00b6e3b4`（命令位置の公開資料なし） · `00b6e3d8`（命令位置の公開資料なし）

~~~diff
- 00b6e30c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:190:8"]]
- 00b6e30c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
+ 00b6e3a8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:290:8"]]
+ 00b6e3a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00b6e30c bytes 099101b9
+ 00b6e3a8 bytes 099102b9
- 00b6e318 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:198:8"]]
- 00b6e318 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6e3b4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:298:8"]]
+ 00b6e3b4 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6e318 bytes b4ce40f9
+ 00b6e3b4 bytes b44e41f9
- 00b6e33c ["INT_ADD", "register:40f0:8", ["const:b6e33c:8", "const:4:8"]]
- 00b6e33c ["CALL", null, ["callee:00c5b310:8"]]
+ 00b6e3d8 ["INT_ADD", "register:40f0:8", ["const:b6e3d8:8", "const:4:8"]]
+ 00b6e3d8 ["CALL", null, ["callee:00c5b310:8"]]
- 00b6e33c bytes c1b30394
+ 00b6e3d8 bytes ceb30394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1304756abd776e2ce97677270721d910"></a>

### [`00b6e410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6e/00b6e410.md) → [`00b6e4ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6e/00b6e4ac.md) _ZN20google_play_services17CheckAvailabilityEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5bf20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bf20.md) · 呼出先 4件 [`005762b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005762b8.md) [`00c5aba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aba0.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5bd00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bd00.md)
- 新版 呼出元 1件 [`00c5bff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bff0.md) · 呼出先 4件 [`005762f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005762f8.md) [`00c5ac70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ac70.md) [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5bdd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bdd0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 80.72% / 新版 80.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b6e5e0",
      "incomplete_value": true,
      "site": "00b6e5e0",
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
            "const:141:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e544",
      "incomplete_value": true,
      "site": "00b6e544",
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
            "const:141:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b6e5e4",
      "incomplete_value": true,
      "site": "00b6e5e4",
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
            "const:144:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e548",
      "incomplete_value": true,
      "site": "00b6e548",
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
            "const:144:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b6e4cc",
      "incomplete_value": true,
      "site": "00b6e4cc",
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
      "definition_site": "00b6e430",
      "incomplete_value": true,
      "site": "00b6e430",
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
      "00b6e4c0",
      "READ",
      [
        "storage",
        "01126198",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e4d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b6e460"
      ]
    ],
    [
      "00b6e4f0",
      "READ",
      [
        "storage",
        "01126198",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6e4c0",
      "READ",
      [
        "storage",
        "01126298",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e4d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6e4fc"
      ]
    ],
    [
      "00b6e4f0",
      "READ",
      [
        "storage",
        "01126298",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e474`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6e/00b6e410.md#insn-00b6e474) · [`00b6e4a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6e/00b6e410.md#insn-00b6e4a8) · [`00b6e424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6e/00b6e410.md#insn-00b6e424)
- 新版 `00b6e510`（命令位置の公開資料なし） · `00b6e544`（命令位置の公開資料なし） · `00b6e4c0`（命令位置の公開資料なし）

~~~diff
- 00b6e474 ["INT_ADD", "register:40f0:8", ["const:b6e474:8", "const:4:8"]]
- 00b6e474 ["CALL", null, ["callee:00c5ac70:8"]]
+ 00b6e510 ["INT_ADD", "register:40f0:8", ["const:b6e510:8", "const:4:8"]]
+ 00b6e510 ["CALL", null, ["callee:00c5ac70:8"]]
- 00b6e474 bytes cbb10394
+ 00b6e510 bytes d8b10394
- 00b6e4a8 ["INT_ADD", "register:40f0:8", ["const:b6e4a8:8", "const:4:8"]]
- 00b6e4a8 ["CALL", null, ["callee:005762f8:8"]]
+ 00b6e544 ["INT_ADD", "register:40f0:8", ["const:b6e544:8", "const:4:8"]]
+ 00b6e544 ["CALL", null, ["callee:005762f8:8"]]
- 00b6e4a8 bytes 841fe897
+ 00b6e544 bytes 6d1fe897
- 00b6e424 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:198:8"]]
- 00b6e424 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6e4c0 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:298:8"]]
+ 00b6e4c0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6e424 bytes c8ce40f9
+ 00b6e4c0 bytes c84e41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce141fb74046ef40ead26f4838a037a7"></a>

### [`00b6e55c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6e/00b6e55c.md) → [`00b6e5f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6e/00b6e5f8.md) _ZN20google_play_services17CallMakeAvailableEPv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b6e6d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6e/00b6e6d0.md) · 呼出先 8件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5ada0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ada0.md) [`00c5ae00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae00.md)
- 新版 呼出元 1件 [`00b6e76c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6e/00b6e76c.md) · 呼出先 8件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md) [`00c5ae70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae70.md) [`00c5aed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aed0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6e630",
      "incomplete_value": true,
      "site": "00b6e640",
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
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:2b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e594",
      "incomplete_value": true,
      "site": "00b6e5a4",
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
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:1b8:8"
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
      "definition_site": "00b6e634",
      "incomplete_value": true,
      "site": "00b6e640",
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
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:2c8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e598",
      "incomplete_value": true,
      "site": "00b6e5a4",
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
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:1c8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6e674",
      "incomplete_value": true,
      "site": "00b6e678",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e5d8",
      "incomplete_value": true,
      "site": "00b6e5dc",
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
            "const:130:8"
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
      "00b6e630",
      "READ",
      [
        "storage",
        "011261b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e634",
      "READ",
      [
        "storage",
        "011261c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e66c",
      "READ",
      [
        "storage",
        "01126198",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6e630",
      "READ",
      [
        "storage",
        "011262b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e634",
      "READ",
      [
        "storage",
        "011262c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e66c",
      "READ",
      [
        "storage",
        "01126298",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e5a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6e/00b6e55c.md#insn-00b6e5a4) · [`00b6e5dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6e/00b6e55c.md#insn-00b6e5dc) · [`00b6e5f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6e/00b6e55c.md#insn-00b6e5f8)
- 新版 `00b6e640`（命令位置の公開資料なし） · `00b6e678`（命令位置の公開資料なし） · `00b6e694`（命令位置の公開資料なし）

~~~diff
- 00b6e5a4 ["INT_ADD", "register:40f0:8", ["const:b6e5a4:8", "const:4:8"]]
- 00b6e5a4 ["CALL", null, ["callee:00c5c010:8"]]
+ 00b6e640 ["INT_ADD", "register:40f0:8", ["const:b6e640:8", "const:4:8"]]
+ 00b6e640 ["CALL", null, ["callee:00c5c010:8"]]
- 00b6e5a4 bytes 67b60394
+ 00b6e640 bytes 74b60394
- 00b6e5dc ["INT_ADD", "register:40f0:8", ["const:b6e5dc:8", "const:4:8"]]
- 00b6e5dc ["CALL", null, ["callee:00c5aed0:8"]]
+ 00b6e678 ["INT_ADD", "register:40f0:8", ["const:b6e678:8", "const:4:8"]]
+ 00b6e678 ["CALL", null, ["callee:00c5aed0:8"]]
- 00b6e5dc bytes 09b20394
+ 00b6e678 bytes 16b20394
- 00b6e5f8 ["INT_ADD", "register:40f0:8", ["const:b6e5f8:8", "const:4:8"]]
- 00b6e5f8 ["CALL", null, ["callee:00c5ae70:8"]]
+ 00b6e694 ["INT_ADD", "register:40f0:8", ["const:b6e694:8", "const:4:8"]]
+ 00b6e694 ["CALL", null, ["callee:00c5ae70:8"]]
- 00b6e5f8 bytes eab10394
+ 00b6e694 bytes f7b10394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3890039bcc9261b258335328c2bcd27"></a>

### [`00b6e6d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6e/00b6e6d0.md) → [`00b6e76c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6e/00b6e76c.md) _ZN20google_play_services13MakeAvailableEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5bd10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bd10.md) · 呼出先 14件 [`00b6e55c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6e/00b6e55c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5aba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aba0.md)
- 新版 呼出元 1件 [`00c5bde0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bde0.md) · 呼出先 14件 [`00b6e5f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6e/00b6e5f8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md) [`00c5ac70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ac70.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 91.24% / 新版 91.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 4件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b6e7a8",
      "incomplete_value": true,
      "site": "00b6e7a8",
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
      "definition_site": "00b6e70c",
      "incomplete_value": true,
      "site": "00b6e70c",
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00b6e7c4",
      "incomplete_value": true,
      "site": "00b6e7c4",
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
      "definition_site": "00b6e728",
      "incomplete_value": true,
      "site": "00b6e728",
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
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b6e858",
      "incomplete_value": true,
      "site": "00b6e858",
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
      "definition_site": "00b6e7bc",
      "incomplete_value": true,
      "site": "00b6e7bc",
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
      "00b6e7a0",
      "READ",
      [
        "storage",
        "01126198",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e7c0",
      "READ",
      [
        "storage",
        "01126198",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e7f4",
      "READ",
      [
        "storage",
        "01126198",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6e7a0",
      "READ",
      [
        "storage",
        "01126298",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e7c0",
      "READ",
      [
        "storage",
        "01126298",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e7f4",
      "READ",
      [
        "storage",
        "01126298",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6e/00b6e6d0.md#insn-00b6e720) · [`00b6e76c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6e/00b6e6d0.md#insn-00b6e76c) · [`00b6e790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6e/00b6e6d0.md#insn-00b6e790)
- 新版 `00b6e7bc`（命令位置の公開資料なし） · `00b6e808`（命令位置の公開資料なし） · `00b6e82c`（命令位置の公開資料なし）

~~~diff
- 00b6e720 ["INT_ADD", "register:40f0:8", ["const:b6e720:8", "const:4:8"]]
- 00b6e720 ["CALL", null, ["callee:00c5bdd0:8"]]
+ 00b6e7bc ["INT_ADD", "register:40f0:8", ["const:b6e7bc:8", "const:4:8"]]
+ 00b6e7bc ["CALL", null, ["callee:00c5bdd0:8"]]
- 00b6e720 bytes 78b50394
+ 00b6e7bc bytes 85b50394
- 00b6e76c ["INT_ADD", "register:40f0:8", ["const:b6e76c:8", "const:4:8"]]
- 00b6e76c ["CALL", null, ["callee:00c5af10:8"]]
+ 00b6e808 ["INT_ADD", "register:40f0:8", ["const:b6e808:8", "const:4:8"]]
+ 00b6e808 ["CALL", null, ["callee:00c5af10:8"]]
- 00b6e76c bytes b5b10394
+ 00b6e808 bytes c2b10394
- 00b6e790 ["INT_ADD", "register:40f0:8", ["const:b6e790:8", "const:4:8"]]
- 00b6e790 ["CALL", null, ["callee:00c5bd40:8"]]
+ 00b6e82c ["INT_ADD", "register:40f0:8", ["const:b6e82c:8", "const:4:8"]]
+ 00b6e82c ["CALL", null, ["callee:00c5bd40:8"]]
- 00b6e790 bytes 38b50394
+ 00b6e82c bytes 45b50394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c0ec1a3412579fc2fcf2f7d8218bd98"></a>

### [`00b6ea60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6e/00b6ea60.md) → [`00b6eafc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6e/00b6eafc.md) _ZN11flatbuffers19FLATBUFFERS_VERSIONEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b6eb00",
      "incomplete_value": false,
      "site": "00b6eb04",
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
            "const:e20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6ea64",
      "incomplete_value": false,
      "site": "00b6ea68",
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
            "const:e74:8"
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
      "00b6eb00",
      "DATA",
      [
        "storage",
        "002bbe74",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6eb00",
      "DATA",
      [
        "storage",
        "002bbe20",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6ea64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6e/00b6ea60.md#insn-00b6ea64)
- 新版 `00b6eb00`（命令位置の公開資料なし）

~~~diff
- 00b6ea64 ["COPY", "tmp:0:8", ["const:e74:8"]]
- 00b6ea64 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6ea64 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6ea64 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b6eb00 ["COPY", "tmp:0:8", ["const:e20:8"]]
+ 00b6eb00 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6eb00 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6eb00 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6ea64 bytes 00d03991
+ 00b6eb00 bytes 00803891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b8cd1a08f183af0cb005cc78050d951"></a>

### [`00b6ea6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6e/00b6ea6c.md) → [`00b6eb08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6e/00b6eb08.md) _ZN11flatbuffers6Parser7MessageERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5c770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c770.md) · 呼出先 7件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) [`00c5bfe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bfe0.md)
- 新版 呼出元 1件 [`00c5c840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c840.md) · 呼出先 7件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md) [`00c5c0b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c0b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.55% / 新版 97.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6eb58",
      "incomplete_value": false,
      "site": "00b6eb64",
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
            "const:c11:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6eabc",
      "incomplete_value": false,
      "site": "00b6eac8",
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
            "const:be0:8"
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
      "definition_site": "00b6ec00",
      "incomplete_value": false,
      "site": "00b6ec0c",
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
            "const:96b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6eb64",
      "incomplete_value": false,
      "site": "00b6eb70",
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
            "const:9c7:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6ec20",
      "incomplete_value": false,
      "site": "00b6ec2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bd000:8"
          ],
          [
            "leaf",
            "const:71a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6eb84",
      "incomplete_value": false,
      "site": "00b6eb90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bd000:8"
          ],
          [
            "leaf",
            "const:76e:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b6eb58",
      "PARAM",
      [
        "storage",
        "002b4be0",
        null,
        null
      ]
    ],
    [
      "00b6ec00",
      "PARAM",
      [
        "storage",
        "002b09c7",
        null,
        null
      ]
    ],
    [
      "00b6ec20",
      "PARAM",
      [
        "storage",
        "002bd76e",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b6eb58",
      "PARAM",
      [
        "storage",
        "002b4c11",
        null,
        null
      ]
    ],
    [
      "00b6ec00",
      "PARAM",
      [
        "storage",
        "002b096b",
        null,
        null
      ]
    ],
    [
      "00b6ec20",
      "PARAM",
      [
        "storage",
        "002bd71a",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6eac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6e/00b6ea6c.md#insn-00b6eac8) · [`00b6eb64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6e/00b6ea6c.md#insn-00b6eb64) · [`00b6eb70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6e/00b6ea6c.md#insn-00b6eb70)
- 新版 `00b6eb64`（命令位置の公開資料なし） · `00b6ec00`（命令位置の公開資料なし） · `00b6ec0c`（命令位置の公開資料なし）

~~~diff
- 00b6eac8 ["INT_ADD", "register:40f0:8", ["const:b6eac8:8", "const:4:8"]]
- 00b6eac8 ["CALL", null, ["callee:00c58050:8"]]
+ 00b6eb64 ["INT_ADD", "register:40f0:8", ["const:b6eb64:8", "const:4:8"]]
+ 00b6eb64 ["CALL", null, ["callee:00c58050:8"]]
- 00b6eac8 bytes 2ea50394
+ 00b6eb64 bytes 3ba50394
- 00b6eb64 ["COPY", "tmp:0:8", ["const:9c7:8"]]
- 00b6eb64 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00b6eb64 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00b6eb64 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00b6ec00 ["COPY", "tmp:0:8", ["const:96b:8"]]
+ 00b6ec00 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00b6ec00 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00b6ec00 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00b6eb64 bytes 211c2791
+ 00b6ec00 bytes 21ac2591
- 00b6eb70 ["INT_ADD", "register:40f0:8", ["const:b6eb70:8", "const:4:8"]]
- 00b6eb70 ["CALL", null, ["callee:00c58050:8"]]
+ 00b6ec0c ["INT_ADD", "register:40f0:8", ["const:b6ec0c:8", "const:4:8"]]
+ 00b6ec0c ["CALL", null, ["callee:00c58050:8"]]
- 00b6eb70 bytes 04a50394
+ 00b6ec0c bytes 11a50394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4c3b753db47cd0289487bb1859d882e"></a>

### [`00b6ecf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6e/00b6ecf8.md) → [`00b6ed94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6e/00b6ed94.md) _ZN11flatbuffers11NumToStringIiEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEET_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5bfe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bfe0.md) · 呼出先 8件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c581b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581b0.md) [`00c581e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581e0.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md)
- 新版 呼出元 1件 [`00c5c0b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c0b0.md) · 呼出先 8件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58280.md) [`00c582b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c582b0.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.21% / 新版 91.21%

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
      "definition_site": "00b6edf0",
      "incomplete_value": true,
      "site": "00b6ee04",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6ed54",
      "incomplete_value": true,
      "site": "00b6ed68",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b6ede8",
      "incomplete_value": true,
      "site": "00b6ee08",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6ed4c",
      "incomplete_value": true,
      "site": "00b6ed6c",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b6ee78",
      "incomplete_value": true,
      "site": "00b6ee84",
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
      "definition_site": "00b6eddc",
      "incomplete_value": true,
      "site": "00b6ede8",
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
    "ordinal": 28,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b6edc8",
      "READ",
      [
        "storage",
        "00c9ac18",
        null,
        "pointer"
      ]
    ],
    [
      "00b6edcc",
      "READ",
      [
        "storage",
        "00c9b840",
        null,
        "pointer"
      ]
    ],
    [
      "00b6ee04",
      "DATA",
      [
        "storage",
        "00c90bd0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b6edc8",
      "READ",
      [
        "storage",
        "00c9ace8",
        null,
        "pointer"
      ]
    ],
    [
      "00b6edcc",
      "READ",
      [
        "storage",
        "00c9b910",
        null,
        "pointer"
      ]
    ],
    [
      "00b6ee04",
      "DATA",
      [
        "storage",
        "00c90ca0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6ed2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6e/00b6ecf8.md#insn-00b6ed2c) · [`00b6ed30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6e/00b6ecf8.md#insn-00b6ed30) · [`00b6ed74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6e/00b6ecf8.md#insn-00b6ed74)
- 新版 `00b6edc8`（命令位置の公開資料なし） · `00b6edcc`（命令位置の公開資料なし） · `00b6ee10`（命令位置の公開資料なし）

~~~diff
- 00b6ed2c ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:c18:8"]]
- 00b6ed2c ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6edc8 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:ce8:8"]]
+ 00b6edc8 ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6ed2c bytes 5a0f46f9
+ 00b6edc8 bytes 5a7746f9
- 00b6ed30 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:840:8"]]
- 00b6ed30 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6edcc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:910:8"]]
+ 00b6edcc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6ed30 bytes 082144f9
+ 00b6edcc bytes 088944f9
- 00b6ed74 ["INT_ADD", "register:40f0:8", ["const:b6ed74:8", "const:4:8"]]
- 00b6ed74 ["CALL", null, ["callee:00c582b0:8"]]
+ 00b6ee10 ["INT_ADD", "register:40f0:8", ["const:b6ee10:8", "const:4:8"]]
+ 00b6ee10 ["CALL", null, ["callee:00c582b0:8"]]
- 00b6ed74 bytes 1ba50394
+ 00b6ee10 bytes 28a50394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6ba8e8ec4ea7566ffe63115b2a8287f"></a>

### [`00b6ee64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6e/00b6ee64.md) → [`00b6ef00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6e/00b6ef00.md) _ZN11flatbuffers11NumToStringIlEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEET_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5c000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c000.md) · 呼出先 8件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c581b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581b0.md) [`00c581e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581e0.md) [`00c58220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58220.md)
- 新版 呼出元 1件 [`00c5c0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c0d0.md) · 呼出先 8件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58280.md) [`00c582b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c582b0.md) [`00c582f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c582f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.11% / 新版 91.11%

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
      "definition_site": "00b6ef58",
      "incomplete_value": true,
      "site": "00b6ef6c",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6eebc",
      "incomplete_value": true,
      "site": "00b6eed0",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b6ef50",
      "incomplete_value": true,
      "site": "00b6ef70",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6eeb4",
      "incomplete_value": true,
      "site": "00b6eed4",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b6efe0",
      "incomplete_value": true,
      "site": "00b6efec",
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
      "definition_site": "00b6ef44",
      "incomplete_value": true,
      "site": "00b6ef50",
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
    "ordinal": 28,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b6ef30",
      "READ",
      [
        "storage",
        "00c9ac18",
        null,
        "pointer"
      ]
    ],
    [
      "00b6ef34",
      "READ",
      [
        "storage",
        "00c9b840",
        null,
        "pointer"
      ]
    ],
    [
      "00b6ef6c",
      "DATA",
      [
        "storage",
        "00c90bd0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b6ef30",
      "READ",
      [
        "storage",
        "00c9ace8",
        null,
        "pointer"
      ]
    ],
    [
      "00b6ef34",
      "READ",
      [
        "storage",
        "00c9b910",
        null,
        "pointer"
      ]
    ],
    [
      "00b6ef6c",
      "DATA",
      [
        "storage",
        "00c90ca0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6ee94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6e/00b6ee64.md#insn-00b6ee94) · [`00b6ee98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6e/00b6ee64.md#insn-00b6ee98) · [`00b6eedc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6e/00b6ee64.md#insn-00b6eedc)
- 新版 `00b6ef30`（命令位置の公開資料なし） · `00b6ef34`（命令位置の公開資料なし） · `00b6ef78`（命令位置の公開資料なし）

~~~diff
- 00b6ee94 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:c18:8"]]
- 00b6ee94 ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6ef30 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:ce8:8"]]
+ 00b6ef30 ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6ee94 bytes 5a0f46f9
+ 00b6ef30 bytes 5a7746f9
- 00b6ee98 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:840:8"]]
- 00b6ee98 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6ef34 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:910:8"]]
+ 00b6ef34 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6ee98 bytes 082144f9
+ 00b6ef34 bytes 088944f9
- 00b6eedc ["INT_ADD", "register:40f0:8", ["const:b6eedc:8", "const:4:8"]]
- 00b6eedc ["CALL", null, ["callee:00c582b0:8"]]
+ 00b6ef78 ["INT_ADD", "register:40f0:8", ["const:b6ef78:8", "const:4:8"]]
+ 00b6ef78 ["CALL", null, ["callee:00c582b0:8"]]
- 00b6eedc bytes c1a40394
+ 00b6ef78 bytes cea40394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1230fb74b096d4d8132c80caee818fa5"></a>

### [`00b6f0ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6f/00b6f0ac.md) → [`00b6f148`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6f/00b6f148.md) _ZN11flatbuffers6Parser7WarningERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) [`00c5c770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c770.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md) [`00c5c840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c840.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.88% / 新版 96.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6f174",
      "incomplete_value": false,
      "site": "00b6f17c",
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
            "const:b5f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6f0d8",
      "incomplete_value": false,
      "site": "00b6f0e0",
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
            "const:bac:8"
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
      "00b6f174",
      "PARAM",
      [
        "storage",
        "002a0bac",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6f174",
      "PARAM",
      [
        "storage",
        "002a0b5f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6f0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6f/00b6f0ac.md#insn-00b6f0e0) · [`00b6f0d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6f/00b6f0ac.md#insn-00b6f0d8) · [`00b6f0ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6f/00b6f0ac.md#insn-00b6f0ec)
- 新版 `00b6f17c`（命令位置の公開資料なし） · `00b6f174`（命令位置の公開資料なし） · `00b6f188`（命令位置の公開資料なし）

~~~diff
- 00b6f0e0 ["INT_ADD", "register:40f0:8", ["const:b6f0e0:8", "const:4:8"]]
- 00b6f0e0 ["CALL", null, ["callee:00c58180:8"]]
+ 00b6f17c ["INT_ADD", "register:40f0:8", ["const:b6f17c:8", "const:4:8"]]
+ 00b6f17c ["CALL", null, ["callee:00c58180:8"]]
- 00b6f0e0 bytes f4a30394
+ 00b6f17c bytes 01a40394
- 00b6f0d8 ["COPY", "tmp:0:8", ["const:bac:8"]]
- 00b6f0d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6f0d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6f0d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b6f174 ["COPY", "tmp:0:8", ["const:b5f:8"]]
+ 00b6f174 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6f174 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6f174 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6f0d8 bytes 00b02e91
+ 00b6f174 bytes 007c2d91
- 00b6f0ec ["INT_ADD", "register:40f0:8", ["const:b6f0ec:8", "const:4:8"]]
- 00b6f0ec ["CALL", null, ["callee:00c5c840:8"]]
+ 00b6f188 ["INT_ADD", "register:40f0:8", ["const:b6f188:8", "const:4:8"]]
+ 00b6f188 ["CALL", null, ["callee:00c5c840:8"]]
- 00b6f0ec bytes a1b50394
+ 00b6f188 bytes aeb50394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e479a78a92f78dbacd6d736a8ea5c5cb"></a>

### [`00b6f12c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6f/00b6f12c.md) → [`00b6f1c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6f/00b6f1c8.md) _ZN11flatbuffers6Parser5ErrorERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) [`00c5c770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c770.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md) [`00c5c840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c840.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.97% / 新版 96.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6f1f0",
      "incomplete_value": false,
      "site": "00b6f1fc",
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
            "const:b69:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6f154",
      "incomplete_value": false,
      "site": "00b6f160",
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
            "const:bb6:8"
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
      "00b6f1f0",
      "PARAM",
      [
        "storage",
        "002a0bb6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6f1f0",
      "PARAM",
      [
        "storage",
        "002a0b69",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6f160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6f/00b6f12c.md#insn-00b6f160) · [`00b6f154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6f/00b6f12c.md#insn-00b6f154) · [`00b6f16c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6f/00b6f12c.md#insn-00b6f16c)
- 新版 `00b6f1fc`（命令位置の公開資料なし） · `00b6f1f0`（命令位置の公開資料なし） · `00b6f208`（命令位置の公開資料なし）

~~~diff
- 00b6f160 ["INT_ADD", "register:40f0:8", ["const:b6f160:8", "const:4:8"]]
- 00b6f160 ["CALL", null, ["callee:00c58180:8"]]
+ 00b6f1fc ["INT_ADD", "register:40f0:8", ["const:b6f1fc:8", "const:4:8"]]
+ 00b6f1fc ["CALL", null, ["callee:00c58180:8"]]
- 00b6f160 bytes d4a30394
+ 00b6f1fc bytes e1a30394
- 00b6f154 ["COPY", "tmp:0:8", ["const:bb6:8"]]
- 00b6f154 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6f154 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6f154 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b6f1f0 ["COPY", "tmp:0:8", ["const:b69:8"]]
+ 00b6f1f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6f1f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6f1f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6f154 bytes 00d82e91
+ 00b6f1f0 bytes 00a42d91
- 00b6f16c ["INT_ADD", "register:40f0:8", ["const:b6f16c:8", "const:4:8"]]
- 00b6f16c ["CALL", null, ["callee:00c5c840:8"]]
+ 00b6f208 ["INT_ADD", "register:40f0:8", ["const:b6f208:8", "const:4:8"]]
+ 00b6f208 ["CALL", null, ["callee:00c5c840:8"]]
- 00b6f16c bytes 81b50394
+ 00b6f208 bytes 8eb50394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a809d1df18b12063b15bc419776d8967"></a>

### [`00b6f1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6f/00b6f1b0.md) → [`00b6f24c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6f/00b6f24c.md) _ZN11flatbuffers6Parser12RecurseErrorEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5c520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c520.md) · 呼出先 7件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) [`00c58fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58fd0.md)
- 新版 呼出元 1件 [`00c5c5f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c5f0.md) · 呼出先 7件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md) [`00c590a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c590a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.10% / 新版 96.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6f284",
      "incomplete_value": false,
      "site": "00b6f294",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c1000:8"
          ],
          [
            "leaf",
            "const:c38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6f1e8",
      "incomplete_value": false,
      "site": "00b6f1f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c1000:8"
          ],
          [
            "leaf",
            "const:bf8:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6f2a4",
      "incomplete_value": false,
      "site": "00b6f2c0",
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
            "const:50e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6f208",
      "incomplete_value": false,
      "site": "00b6f224",
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
            "const:56a:8"
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
      "definition_site": "00b6f2e4",
      "incomplete_value": false,
      "site": "00b6f2ec",
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
            "const:b69:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6f248",
      "incomplete_value": false,
      "site": "00b6f250",
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
            "const:bb6:8"
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
      "00b6f284",
      "PARAM",
      [
        "storage",
        "002c1bf8",
        null,
        "string"
      ]
    ],
    [
      "00b6f2a4",
      "PARAM",
      [
        "storage",
        "002a856a",
        null,
        "string"
      ]
    ],
    [
      "00b6f2e4",
      "PARAM",
      [
        "storage",
        "002a0bb6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6f284",
      "PARAM",
      [
        "storage",
        "002c1c38",
        null,
        "string"
      ]
    ],
    [
      "00b6f2a4",
      "PARAM",
      [
        "storage",
        "002a850e",
        null,
        "string"
      ]
    ],
    [
      "00b6f2e4",
      "PARAM",
      [
        "storage",
        "002a0b69",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6f1f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6f/00b6f1b0.md#insn-00b6f1f8) · [`00b6f224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6f/00b6f1b0.md#insn-00b6f224) · [`00b6f250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6f/00b6f1b0.md#insn-00b6f250)
- 新版 `00b6f294`（命令位置の公開資料なし） · `00b6f2c0`（命令位置の公開資料なし） · `00b6f2ec`（命令位置の公開資料なし）

~~~diff
- 00b6f1f8 ["INT_ADD", "register:40f0:8", ["const:b6f1f8:8", "const:4:8"]]
- 00b6f1f8 ["CALL", null, ["callee:00c590a0:8"]]
+ 00b6f294 ["INT_ADD", "register:40f0:8", ["const:b6f294:8", "const:4:8"]]
+ 00b6f294 ["CALL", null, ["callee:00c590a0:8"]]
- 00b6f1f8 bytes 76a70394
+ 00b6f294 bytes 83a70394
- 00b6f224 ["INT_ADD", "register:40f0:8", ["const:b6f224:8", "const:4:8"]]
- 00b6f224 ["CALL", null, ["callee:00c58050:8"]]
+ 00b6f2c0 ["INT_ADD", "register:40f0:8", ["const:b6f2c0:8", "const:4:8"]]
+ 00b6f2c0 ["CALL", null, ["callee:00c58050:8"]]
- 00b6f224 bytes 57a30394
+ 00b6f2c0 bytes 64a30394
- 00b6f250 ["INT_ADD", "register:40f0:8", ["const:b6f250:8", "const:4:8"]]
- 00b6f250 ["CALL", null, ["callee:00c58180:8"]]
+ 00b6f2ec ["INT_ADD", "register:40f0:8", ["const:b6f2ec:8", "const:4:8"]]
+ 00b6f2ec ["CALL", null, ["callee:00c58180:8"]]
- 00b6f250 bytes 98a30394
+ 00b6f2ec bytes a5a30394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e15bfdb4cf82baf92fe440a8dd96f7b"></a>

### [`00b6f6bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6f/00b6f6bc.md) → [`00b6f758`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6f/00b6f758.md) _ZN11flatbuffers6Parser11ParseHexNumEiPm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c4c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c4c0.md) · 呼出先 11件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md)
- 新版 呼出元 1件 [`00c5c590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c590.md) · 呼出先 11件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 96.77% / 新版 96.77%

CFGの説明率　旧版 72.13% / 新版 72.13%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6f930"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6f930"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b6f9cc"
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
      "unmatched:00b6f748",
      "PARAM",
      [
        "storage",
        "002be68c",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b6f768",
      "PARAM",
      [
        "storage",
        "002a2b00",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b6f7a8",
      "PARAM",
      [
        "storage",
        "002a0bb6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6f7e4",
      "PARAM",
      [
        "storage",
        "002be638",
        null,
        "string"
      ]
    ],
    [
      "00b6f804",
      "PARAM",
      [
        "storage",
        "002a2ab3",
        null,
        "string"
      ]
    ],
    [
      "00b6f844",
      "PARAM",
      [
        "storage",
        "002a0b69",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6f758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6f/00b6f6bc.md#insn-00b6f758) · [`00b6f784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6f/00b6f6bc.md#insn-00b6f784) · [`00b6f7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6f/00b6f6bc.md#insn-00b6f7b0)
- 新版 `00b6f7f4`（命令位置の公開資料なし） · `00b6f820`（命令位置の公開資料なし） · `00b6f84c`（命令位置の公開資料なし）

~~~diff
- 00b6f758 ["INT_ADD", "register:40f0:8", ["const:b6f758:8", "const:4:8"]]
- 00b6f758 ["CALL", null, ["callee:00c590a0:8"]]
+ 00b6f7f4 ["INT_ADD", "register:40f0:8", ["const:b6f7f4:8", "const:4:8"]]
+ 00b6f7f4 ["CALL", null, ["callee:00c590a0:8"]]
- 00b6f758 bytes 1ea60394
+ 00b6f7f4 bytes 2ba60394
- 00b6f784 ["INT_ADD", "register:40f0:8", ["const:b6f784:8", "const:4:8"]]
- 00b6f784 ["CALL", null, ["callee:00c58050:8"]]
+ 00b6f820 ["INT_ADD", "register:40f0:8", ["const:b6f820:8", "const:4:8"]]
+ 00b6f820 ["CALL", null, ["callee:00c58050:8"]]
- 00b6f784 bytes ffa10394
+ 00b6f820 bytes 0ca20394
- 00b6f7b0 ["INT_ADD", "register:40f0:8", ["const:b6f7b0:8", "const:4:8"]]
- 00b6f7b0 ["CALL", null, ["callee:00c58180:8"]]
+ 00b6f84c ["INT_ADD", "register:40f0:8", ["const:b6f84c:8", "const:4:8"]]
+ 00b6f84c ["CALL", null, ["callee:00c58180:8"]]
- 00b6f7b0 bytes 40a20394
+ 00b6f84c bytes 4da20394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18e4ada25be8af571acb513092d1973f"></a>

### [`00b6f9a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6f/00b6f9a4.md) → [`00b6fa40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6f/00b6fa40.md) _ZN11flatbuffers6Parser17SkipByteOrderMarkEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c650.md) · 呼出先 5件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) [`00c5c770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c770.md)
- 新版 呼出元 1件 [`00c5c720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c720.md) · 呼出先 5件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md) [`00c5c840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c840.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 79.71% / 新版 79.71%

CFGの説明率　旧版 70.59% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6fa34"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6fa38"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6fa3c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6fa24",
      "READ",
      [
        "storage",
        "002b265a",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b6fa28",
      "READ",
      [
        "storage",
        "002b264d",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b6fa30",
      "READ",
      [
        "storage",
        "002c2b50",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b6fac0",
      "READ",
      [
        "storage",
        "002b268b",
        null,
        "string"
      ]
    ],
    [
      "00b6fac4",
      "READ",
      [
        "storage",
        "002b267e",
        null,
        "string"
      ]
    ],
    [
      "00b6facc",
      "READ",
      [
        "storage",
        "002c2b90",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6fa34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6f/00b6f9a4.md#insn-00b6fa34) · [`00b6fa38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6f/00b6f9a4.md#insn-00b6fa38) · [`00b6fa3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6f/00b6f9a4.md#insn-00b6fa3c)

~~~diff
- 00b6fa34 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00b6fa34 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6fa34 bytes e00b00f9
- 00b6fa38 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:d:8"]]
- 00b6fa38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5020:16"]]
- 00b6fa38 bytes 01d0803c
- 00b6fa3c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00b6fa3c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5040:16"]]
- 00b6fa3c bytes 0200803d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6c5e744c045398f75e4ace11228b9ef"></a>

### [`00b6fab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6f/00b6fab8.md) → [`00b6fb54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6f/00b6fb54.md) _ZN11flatbuffers6Parser4NextEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c6f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c6f0.md) · 呼出先 14件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) [`00c58fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58fd0.md)
- 新版 呼出元 1件 [`00c5c7c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c7c0.md) · 呼出先 14件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md) [`00c590a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c590a0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 77.18% / 新版 77.18%

CFGの説明率　旧版 56.28% / 新版 55.69%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `store_condition` 10件, `store_value` 12件, `unresolved_branch_alignment` 40件, `unresolved_call_alignment` 11件, `unresolved_store_alignment` 25件

アドレスに依存する影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6fadc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6faf0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6fd14"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6fadc",
      "WRITE",
      [
        "storage",
        "Stack[-0xb8]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6faf0",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6fba0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6ff00"
      ]
    ]
  ],
  "added": [
    [
      "00b6fb78",
      "WRITE",
      [
        "storage",
        "Stack[-0xb8]",
        null,
        null
      ]
    ],
    [
      "00b6fb8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00b6fc3c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6ff00"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6fadc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6f/00b6fab8.md#insn-00b6fadc) · [`00b6faf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6f/00b6fab8.md#insn-00b6faf0) · [`00b6fca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6f/00b6fab8.md#insn-00b6fca0)
- 新版 `00b6fd3c`（命令位置の公開資料なし）

~~~diff
- 00b6fadc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 00b6fadc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00b6fadc bytes e91700f9
- 00b6faf0 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b6faf0 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffa8:8"]]
- 00b6faf0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b6faf0 bytes a9831af8
- 00b6fca0 ["BRANCH", null, ["local:b44:8"]]
+ 00b6fd3c ["BRANCH", null, ["local:b46:8"]]
- 00b6fca0 bytes 1d000014
+ 00b6fd3c bytes 1d000014
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b90e0bf2c91d9f437a311e66b5e25268"></a>

### [`00b7119c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b71/00b7119c.md) → [`00b71238`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b71/00b71238.md) _ZN11flatbuffers6Parser6ExpectEi

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c750.md) · 呼出先 12件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)
- 新版 呼出元 1件 [`00c5c820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c820.md) · 呼出先 12件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 92.44% / 新版 92.44%

CFGの説明率　旧版 35.00% / 新版 33.73%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 14件, `store_condition` 2件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7132c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b713e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b713e0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b712cc",
      "DATA",
      [
        "storage",
        "00c90158",
        null,
        null
      ]
    ],
    [
      "unmatched:00b712a8",
      "PARAM",
      [
        "storage",
        "002c09f8",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b712c8",
      "PARAM",
      [
        "storage",
        "002bf8db",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b712cc",
      "DATA",
      [
        "storage",
        "00c90228",
        null,
        null
      ]
    ],
    [
      "00b71344",
      "PARAM",
      [
        "storage",
        "002c0a38",
        null,
        "string"
      ]
    ],
    [
      "00b71364",
      "PARAM",
      [
        "storage",
        "002bf887",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b71248`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b71/00b7119c.md#insn-00b71248) · [`00b712b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b71/00b7119c.md#insn-00b712b8) · [`00b712e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b71/00b7119c.md#insn-00b712e4)
- 新版 `00b712e4`（命令位置の公開資料なし） · `00b71354`（命令位置の公開資料なし） · `00b71380`（命令位置の公開資料なし）

~~~diff
- 00b71248 ["CBRANCH", null, ["local:b56:8", "register:102:1"]]
+ 00b712e4 ["CBRANCH", null, ["local:b59:8", "register:102:1"]]
- 00b71248 bytes 42180054
+ 00b712e4 bytes 42180054
- 00b712b8 ["INT_ADD", "register:40f0:8", ["const:b712b8:8", "const:4:8"]]
- 00b712b8 ["CALL", null, ["callee:00c590a0:8"]]
+ 00b71354 ["INT_ADD", "register:40f0:8", ["const:b71354:8", "const:4:8"]]
+ 00b71354 ["CALL", null, ["callee:00c590a0:8"]]
- 00b712b8 bytes 469f0394
+ 00b71354 bytes 539f0394
- 00b712e4 ["INT_ADD", "register:40f0:8", ["const:b712e4:8", "const:4:8"]]
- 00b712e4 ["CALL", null, ["callee:00c58050:8"]]
+ 00b71380 ["INT_ADD", "register:40f0:8", ["const:b71380:8", "const:4:8"]]
+ 00b71380 ["CALL", null, ["callee:00c58050:8"]]
- 00b712e4 bytes 279b0394
+ 00b71380 bytes 349b0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-729b32fd0a0acb7eab95f4094a7e9e19"></a>

### [`00b71554`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b71/00b71554.md) → [`00b715f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b71/00b715f0.md) _ZN11flatbuffers6Parser16ParseNamespacingEPNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES8_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c600.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md) [`00c5b0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0b0.md) [`00c5c6f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c6f0.md) [`00c5c750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c750.md)
- 新版 呼出元 1件 [`00c5c6d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c6d0.md) · 呼出先 4件 [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md) [`00c5b180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b180.md) [`00c5c7c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c7c0.md) [`00c5c820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c820.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 81.82% / 新版 81.82%

CFGの説明率　旧版 7.14% / 新版 5.88%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b71554"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b71554"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b71558"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b71554",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b71558",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b7155c",
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
      "00b715f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b715f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b715f8",
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

- 旧版 [`00b71554`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b71/00b71554.md#insn-00b71554) · [`00b71558`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b71/00b71554.md#insn-00b71558) · [`00b7155c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b71/00b71554.md#insn-00b7155c)

~~~diff
- 00b71554 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b71554 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b71554 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 00b71554 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b71554 bytes fa67bba9
- 00b71558 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b71558 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b71558 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b71558 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b71558 bytes f85f01a9
- 00b7155c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b7155c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b7155c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b7155c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b7155c bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-120dcd5b7140517777c6dd19343625aa"></a>

### [`00b7165c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b71/00b7165c.md) → [`00b716f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b71/00b716f8.md) _ZN11flatbuffers6Parser10LookupEnumERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c450.md) · 呼出先 6件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md) [`00c5a8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8e0.md) [`00c5be70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be70.md)
- 新版 呼出元 1件 [`00c5c520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c520.md) · 呼出先 6件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md) [`00c5a9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a9b0.md) [`00c5bf40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf40.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 90.53% / 新版 90.53%

CFGの説明率　旧版 38.60% / 新版 38.60%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 6件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b71684"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b71860"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b71720"
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
      "unmatched:00b71684",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b716b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b71924"
      ]
    ],
    [
      "unmatched:00b7172c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b717ec"
      ]
    ]
  ],
  "added": [
    [
      "00b71720",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00b71750",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b71924"
      ]
    ],
    [
      "00b717c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b717ec"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b71684`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b71/00b7165c.md#insn-00b71684) · [`00b716b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b71/00b7165c.md#insn-00b716b4) · [`00b716f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b71/00b7165c.md#insn-00b716f4)

~~~diff
- 00b71684 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 00b71684 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b71684 bytes e81700f9
- 00b716b4 ["CBRANCH", null, ["local:b31:8", "register:101:1"]]
- 00b716b4 bytes a00e0054
- 00b716f4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b716f4 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00b716f4 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b716f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:1:8"]]
- 00b716f4 bytes 4115889a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6570232c4f133ee22bc2fea4d33417c"></a>

### [`00b7194c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b71/00b7194c.md) → [`00b719e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b71/00b719e8.md) _ZNK11flatbuffers6Parser32LookupStructThruParentNamespacesERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c9e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c9e0.md) · 呼出先 6件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md) [`00c5a8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8e0.md) [`00c5be70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be70.md)
- 新版 呼出元 1件 [`00c5cab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cab0.md) · 呼出先 6件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md) [`00c5a9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a9b0.md) [`00c5bf40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf40.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 46.67% / 新版 45.90%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b71a14"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b71a18"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b71a38"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b71a38",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b71aec"
      ]
    ],
    [
      "unmatched:00b71ae8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b71b90"
      ]
    ],
    [
      "unmatched:00b71b4c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b71b40"
      ]
    ]
  ],
  "added": [
    [
      "00b71ad4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b71aec"
      ]
    ],
    [
      "00b71b84",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b71b90"
      ]
    ],
    [
      "00b71be8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b71b40"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b71a14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b71/00b7194c.md#insn-00b71a14) · [`00b71a18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b71/00b7194c.md#insn-00b71a18) · [`00b71a38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b71/00b7194c.md#insn-00b71a38)

~~~diff
- 00b71a14 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b71a14 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00b71a14 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b71a14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:1:8"]]
- 00b71a14 bytes 4115889a
- 00b71a18 ["COPY", "tmp:0:8", ["register:4060:8"]]
- 00b71a18 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b71a18 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b71a18 ["COPY", "register:4010:8", ["tmp:0:8"]]
- 00b71a18 bytes 82018b9a
- 00b71a38 ["CBRANCH", null, ["local:b12:8", "register:101:1"]]
- 00b71a38 bytes c0000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50fa43fc1e94f67429c1d2f5bc1b279b"></a>

### [`00b71c0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b71/00b71c0c.md) → [`00b71ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b71/00b71ca8.md) _ZN11flatbuffers6Parser14ParseTypeIdentERNS_4TypeE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c5a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c5a0.md) · 呼出先 9件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 1件 [`00c5c670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c670.md) · 呼出先 9件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 93.40% / 新版 93.40%

CFGの説明率　旧版 45.71% / 新版 45.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b71c3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b71c40"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b71c40"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b71c3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b71c40",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b71c44",
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
      "00b71cd8",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00b71cdc",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00b71ce0",
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

- 旧版 [`00b71c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b71/00b71c0c.md#insn-00b71c3c) · [`00b71c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b71/00b71c0c.md#insn-00b71c40) · [`00b71c44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b71/00b71c0c.md#insn-00b71c44)

~~~diff
- 00b71c3c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00b71c3c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00b71c3c bytes e90f00f9
- 00b71c40 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00b71c40 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b71c40 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00b71c40 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00b71c40 bytes ffff00a9
- 00b71c44 ["COPY", "tmp:0:8", ["register:8:8"]]
- 00b71c44 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b71c44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b71c44 bytes ff0300f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43370a02f7db7f5cbd510cae74c490ea"></a>

### [`00b71db4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b71/00b71db4.md) → [`00b71e50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b71/00b71e50.md) _ZN11flatbuffers6Parser18LookupCreateStructERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEbb

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c660.md) · 呼出先 17件 [`00b5abb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5a/00b5abb4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00c5c730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c730.md) · 呼出先 17件 [`00b5ac50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5a/00b5ac50.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 96.26% / 新版 96.26%

CFGの説明率　旧版 60.19% / 新版 57.52%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b71dc8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b71dc8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b71f08"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b71dc8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b71ed0",
      "READ",
      [
        "storage",
        "002c3ed8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b72090",
      "PARAM",
      [
        "storage",
        "002b09c7",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b71e64",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b71f6c",
      "READ",
      [
        "storage",
        "002c3f18",
        null,
        "undefined8"
      ]
    ],
    [
      "00b72090",
      "PARAM",
      [
        "storage",
        "002b096b",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b71dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b71/00b71db4.md#insn-00b71dc8) · [`00b71dfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b71/00b71db4.md#insn-00b71dfc)
- 新版 `00b71e98`（命令位置の公開資料なし） · `00b71e64`（命令位置の公開資料なし）

~~~diff
- 00b71dc8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b71dc8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b71dc8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:90:8"]]
- 00b71dc8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b71dc8 bytes f44f09a9
- 00b71dfc ["INT_ADD", "register:40f0:8", ["const:b71dfc:8", "const:4:8"]]
- 00b71dfc ["CALL", null, ["callee:00c5cb10:8"]]
+ 00b71e98 ["INT_ADD", "register:40f0:8", ["const:b71e98:8", "const:4:8"]]
+ 00b71e98 ["CALL", null, ["callee:00c5cb10:8"]]
- 00b71dfc bytes 11ab0394
+ 00b71e98 bytes 1eab0394
+ 00b71e64 ["COPY", "tmp:0:8", ["register:40a0:8"]]
+ 00b71e64 ["COPY", "tmp:1:8", ["register:4098:8"]]
+ 00b71e64 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:90:8"]]
+ 00b71e64 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00b71e64 bytes f44f09a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b5900f0d38240fb2d8d07ece970cbe48"></a>

### [`00b7224c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b72/00b7224c.md) → [`00b722e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b72/00b722e8.md) _ZN11flatbuffers6Parser9ParseTypeERNS_4TypeE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b7224c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b72/00b7224c.md) [`00c5c7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c7d0.md) · 呼出先 12件 [`00b7224c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b72/00b7224c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 2件 [`00b722e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b72/00b722e8.md) [`00c5c8a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c8a0.md) · 呼出先 12件 [`00b722e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b72/00b722e8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 63.84% / 新版 63.84%

CFGの説明率　旧版 19.69% / 新版 19.90%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `store_value` 5件, `unresolved_branch_alignment` 31件, `unresolved_call_alignment` 10件, `unresolved_store_alignment` 25件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b72250"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b72254"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b72254"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b72250",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b72254",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b72258",
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
      "00b722ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b722f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b722f4",
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

- 旧版 [`00b72250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b72/00b7224c.md#insn-00b72250) · [`00b72254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b72/00b7224c.md#insn-00b72254) · [`00b72258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b72/00b7224c.md#insn-00b72258)

~~~diff
- 00b72250 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:60:8"]]
- 00b72250 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 00b72250 bytes f93300f9
- 00b72254 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b72254 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b72254 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00b72254 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b72254 bytes f85f07a9
- 00b72258 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b72258 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b72258 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 00b72258 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b72258 bytes f65708a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c615085b68245818b3d0f88fa14a0582"></a>

### [`00b72a08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b72/00b72a08.md) → [`00b72aa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b72/00b72aa4.md) _ZN11flatbuffers6Parser8AddFieldERNS_9StructDefERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEERKNS_4TypeEPPNS_8FieldD

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c780.md) · 呼出先 9件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) [`00c5b0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0b0.md)
- 新版 呼出元 1件 [`00c5c850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c850.md) · 呼出先 9件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md) [`00c5b180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b180.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 82.58% / 新版 82.58%

CFGの説明率　旧版 39.29% / 新版 38.60%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 4件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b72a4c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b72a80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b72a80"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b72a4c",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00b72af4",
      "READ",
      [
        "storage",
        "002c3ed8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b72a7c",
      "PARAM",
      [
        "storage",
        "002b807b",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b72ae8",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00b72af4",
      "READ",
      [
        "storage",
        "002c3f18",
        null,
        "undefined8"
      ]
    ],
    [
      "00b72b18",
      "PARAM",
      [
        "storage",
        "002b80bb",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b72a4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b72/00b72a08.md#insn-00b72a4c) · [`00b72a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b72/00b72a08.md#insn-00b72a80) · [`00b72a84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b72/00b72a08.md#insn-00b72a84)

~~~diff
- 00b72a4c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:38:8"]]
- 00b72a4c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b72a4c bytes e81f00f9
- 00b72a80 ["COPY", "tmp:0:8", ["register:40b8:8"]]
- 00b72a80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5020:16"]]
- 00b72a80 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00b72a80 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5020:16"]]
- 00b72a80 bytes e10600ad
- 00b72a84 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:20:8"]]
- 00b72a84 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5020:16"]]
- 00b72a84 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00b72a84 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5020:16"]]
- 00b72a84 bytes e10601ad
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-184620ff3c3994627e97e10cb1a1b947"></a>

### [`00b72cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b72/00b72cd0.md) → [`00b72d6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b72/00b72d6c.md) _ZN11flatbuffers10InlineSizeERKNS_4TypeE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bfb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bfb0.md) · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5bfb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bfb0.md)
- 新版 呼出元 1件 [`00c5c080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c080.md) · 呼出先 2件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5c080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c080.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 90.57% / 新版 90.57%

CFGの説明率　旧版 50.00% / 新版 52.17%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b72d6c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b72e08"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b72e00",
      "incomplete_value": true,
      "site": "00b72e10",
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
      "00b72dc4",
      "DATA",
      [
        "storage",
        "0030e083",
        "switchD_00b72d34::switchdataD_0030e083",
        "byte"
      ]
    ],
    [
      "unmatched:00b72d6c",
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
      "00b72dc4",
      "DATA",
      [
        "storage",
        "0030e0c3",
        "switchD_00b72dd0::switchdataD_0030e0c3",
        "byte"
      ]
    ],
    [
      "00b72e08",
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

- 旧版 [`00b72d6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b72/00b72cd0.md#insn-00b72d6c) · [`00b72d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b72/00b72cd0.md#insn-00b72d74)
- 新版 `00b72e10`（命令位置の公開資料なし） · `00b72e08`（命令位置の公開資料なし）

~~~diff
- 00b72d6c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00b72d6c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b72d6c bytes e003813c
- 00b72d74 ["INT_ADD", "register:40f0:8", ["const:b72d74:8", "const:4:8"]]
- 00b72d74 ["CALL", null, ["callee:00c5c080:8"]]
+ 00b72e10 ["INT_ADD", "register:40f0:8", ["const:b72e10:8", "const:4:8"]]
+ 00b72e10 ["CALL", null, ["callee:00c5c080:8"]]
- 00b72d74 bytes 8fa40394
+ 00b72e10 bytes 9ca40394
+ 00b72e08 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
+ 00b72e08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
+ 00b72e08 bytes e003813c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

