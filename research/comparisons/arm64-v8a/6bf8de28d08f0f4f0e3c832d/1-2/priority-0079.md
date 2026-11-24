# v16.0.1 → v16.0.2 · 最優先の変更候補 (79)

[一覧の目次](README.md)

<a id="compare-9ada0aae198cb9a6cdb48c859c886333"></a>

### [`00bb5168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb5168.md) → [`00bb5204`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5204.md) _ZN11flatbuffers11CharToLowerEc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00bb4010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb4/00bb4010.md) · 呼出先 1件 [`00c5d250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d250.md)
- 新版 呼出元 1件 [`00bb40ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb4/00bb40ac.md) · 呼出先 1件 [`00c5d320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d320.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb5174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb5168.md#insn-00bb5174)
- 新版 [`00bb5210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5204.md#insn-00bb5210)

~~~diff
- 00bb5174 ["INT_ADD", "register:40f0:8", ["const:bb5174:8", "const:4:8"]]
- 00bb5174 ["CALL", null, ["callee:00c5d320:8"]]
+ 00bb5210 ["INT_ADD", "register:40f0:8", ["const:bb5210:8", "const:4:8"]]
+ 00bb5210 ["CALL", null, ["callee:00c5d320:8"]]
- 00bb5174 bytes 37a00294
+ 00bb5210 bytes 44a00294
~~~


<a id="compare-6556e8a90067ed69a5ca25e4e88612ec"></a>

### [`00bb5180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb5180.md) → [`00bb521c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb521c.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE5seekgExNS_8ios_base7seekdirE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c597f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c597f0.md) · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c58ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58ef0.md)
- 新版 呼出元 1件 [`00c598c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c598c0.md) · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c58fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58fc0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 64.71% / 新版 64.71%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb5180"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb5180"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb5184"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb5180",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb5184",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb5188",
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
      "00bb521c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bb5220",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bb5224",
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

- 旧版 [`00bb5180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb5180.md#insn-00bb5180) · [`00bb5184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb5180.md#insn-00bb5184) · [`00bb5188`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb5180.md#insn-00bb5188)

~~~diff
- 00bb5180 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bb5180 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bb5180 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bb5180 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bb5180 bytes f657bda9
- 00bb5184 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bb5184 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bb5184 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bb5184 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb5184 bytes f44f01a9
- 00bb5188 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bb5188 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bb5188 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bb5188 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb5188 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b01122e5444daeee32c621a3d86e35a"></a>

### [`00bb524c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb524c.md) → [`00bb52e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb52e8.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE5tellgEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c597e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c597e0.md) · 呼出先 2件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c58ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58ef0.md)
- 新版 呼出元 1件 [`00c598b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c598b0.md) · 呼出先 2件 [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c58fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58fc0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 55.81% / 新版 55.81%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb524c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb524c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb5250"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb524c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb5250",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb52c0",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00bb52e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bb52ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bb535c",
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

- 旧版 [`00bb524c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb524c.md#insn-00bb524c) · [`00bb5250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb524c.md#insn-00bb5250) · [`00bb52c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb524c.md#insn-00bb52c0)

~~~diff
- 00bb524c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bb524c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bb524c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bb524c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bb524c bytes f44fbea9
- 00bb5250 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bb5250 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bb5250 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bb5250 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb5250 bytes fd7b01a9
- 00bb52c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bb52c0 ["INT_ADD", "register:40f0:8", ["const:bb52c0:8", "const:4:8"]]
- 00bb52c0 ["CALLIND", null, ["register:0:8"]]
- 00bb52c0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17abea0bee22b97754036b7de8510fa2"></a>

### [`00bb54e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb54e8.md) → [`00bb5584`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5584.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEEC2Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d1a0.md) · 呼出先 7件 [`00bb59c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb59c0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5a7a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7a0.md)
- 新版 呼出元 1件 [`00c5d270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d270.md) · 呼出先 7件 [`00bb5a5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5a5c.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58350.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md) [`00c5a870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a870.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.77% / 新版 95.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb55b4",
      "incomplete_value": true,
      "site": "00bb55b8",
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
      "definition_site": "00bb5518",
      "incomplete_value": true,
      "site": "00bb551c",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb55d8",
      "incomplete_value": true,
      "site": "00bb55f4",
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
      "definition_site": "00bb553c",
      "incomplete_value": true,
      "site": "00bb5558",
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
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb5604",
      "incomplete_value": true,
      "site": "00bb560c",
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
                "const:988:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb5568",
      "incomplete_value": true,
      "site": "00bb5570",
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
                "const:8b8:8"
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
      "00bb55a4",
      "READ",
      [
        "storage",
        "00c9b848",
        null,
        "pointer"
      ]
    ],
    [
      "00bb55b8",
      "DATA",
      [
        "storage",
        "00c90cb0",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "00bb55c8",
      "READ",
      [
        "storage",
        "00c9b8f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bb55a4",
      "READ",
      [
        "storage",
        "00c9b918",
        null,
        "pointer"
      ]
    ],
    [
      "00bb55b8",
      "DATA",
      [
        "storage",
        "00c90d80",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "00bb55c8",
      "READ",
      [
        "storage",
        "00c9b9c0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb5570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb54e8.md#insn-00bb5570) · [`00bb559c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb54e8.md#insn-00bb559c) · [`00bb55b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb54e8.md#insn-00bb55b8)
- 新版 [`00bb560c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5584.md#insn-00bb560c) · [`00bb5638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5584.md#insn-00bb5638) · [`00bb5654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5584.md#insn-00bb5654)

~~~diff
- 00bb5570 ["INT_ADD", "register:40f0:8", ["const:bb5570:8", "const:4:8"]]
- 00bb5570 ["CALL", null, ["callee:00c5d250:8"]]
+ 00bb560c ["INT_ADD", "register:40f0:8", ["const:bb560c:8", "const:4:8"]]
+ 00bb560c ["CALL", null, ["callee:00c5d250:8"]]
- 00bb5570 bytes 049f0294
+ 00bb560c bytes 119f0294
- 00bb559c ["INT_ADD", "register:40f0:8", ["const:bb559c:8", "const:4:8"]]
- 00bb559c ["CALL", null, ["callee:00c58350:8"]]
+ 00bb5638 ["INT_ADD", "register:40f0:8", ["const:bb5638:8", "const:4:8"]]
+ 00bb5638 ["CALL", null, ["callee:00c58350:8"]]
- 00bb559c bytes 398b0294
+ 00bb5638 bytes 468b0294
- 00bb55b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bb55b8 ["INT_ADD", "register:40f0:8", ["const:bb55b8:8", "const:4:8"]]
- 00bb55b8 ["CALLIND", null, ["register:0:8"]]
+ 00bb5654 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bb5654 ["INT_ADD", "register:40f0:8", ["const:bb5654:8", "const:4:8"]]
+ 00bb5654 ["CALLIND", null, ["register:0:8"]]
- 00bb55b8 bytes 00013fd6
+ 00bb5654 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5439cb4a55bf471834eb1df8af0b2b12"></a>

### [`00bb5774`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb5774.md) → [`00bb5810`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5810.md) FUN_00bb5810

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5d0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0e0.md) [`00c5d1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d1b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5d1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d1b0.md) [`00c5d280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d280.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 72.22% / 新版 72.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb583c",
      "incomplete_value": true,
      "site": "00bb583c",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb57a0",
      "incomplete_value": true,
      "site": "00bb57a0",
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
            "const:18:8"
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
      "definition_site": "00bb5840",
      "incomplete_value": true,
      "site": "00bb5840",
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
      "definition_site": "00bb57a4",
      "incomplete_value": true,
      "site": "00bb57a4",
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
      "00bb5828",
      "READ",
      [
        "storage",
        "00c9b030",
        null,
        "pointer"
      ]
    ],
    [
      "00bb583c",
      "DATA",
      [
        "storage",
        "00c90ec0",
        null,
        "pointer"
      ]
    ],
    [
      "00bb5840",
      "DATA",
      [
        "storage",
        "00c90ee8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bb5828",
      "READ",
      [
        "storage",
        "00c9b100",
        null,
        "pointer"
      ]
    ],
    [
      "00bb583c",
      "DATA",
      [
        "storage",
        "00c90f90",
        null,
        "pointer"
      ]
    ],
    [
      "00bb5840",
      "DATA",
      [
        "storage",
        "00c90fb8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb578c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb5774.md#insn-00bb578c) · [`00bb57a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb5774.md#insn-00bb57a8)
- 新版 [`00bb5828`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5810.md#insn-00bb5828) · [`00bb5844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5810.md#insn-00bb5844)

~~~diff
- 00bb578c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:30:8"]]
- 00bb578c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb5828 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:100:8"]]
+ 00bb5828 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb578c bytes 291940f9
+ 00bb5828 bytes 298140f9
- 00bb57a8 ["INT_ADD", "register:40f0:8", ["const:bb57a8:8", "const:4:8"]]
- 00bb57a8 ["CALL", null, ["callee:00c5d280:8"]]
+ 00bb5844 ["INT_ADD", "register:40f0:8", ["const:bb5844:8", "const:4:8"]]
+ 00bb5844 ["CALL", null, ["callee:00c5d280:8"]]
- 00bb57a8 bytes 829e0294
+ 00bb5844 bytes 8f9e0294
~~~


<a id="compare-a6f9cae92b97d00ce05ced0e49907414"></a>

### [`00bb57bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb57bc.md) → [`00bb5858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5858.md) FUN_00bb5858

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5d0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0e0.md) [`00c5d1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d1b0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5d1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d1b0.md) [`00c5d280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d280.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 76.19% / 新版 76.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb5888",
      "incomplete_value": true,
      "site": "00bb5888",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb57ec",
      "incomplete_value": true,
      "site": "00bb57ec",
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
            "const:18:8"
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
      "definition_site": "00bb588c",
      "incomplete_value": true,
      "site": "00bb588c",
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
      "definition_site": "00bb57f0",
      "incomplete_value": true,
      "site": "00bb57f0",
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
      "00bb5870",
      "READ",
      [
        "storage",
        "00c9b030",
        null,
        "pointer"
      ]
    ],
    [
      "00bb5888",
      "DATA",
      [
        "storage",
        "00c90ec0",
        null,
        "pointer"
      ]
    ],
    [
      "00bb588c",
      "DATA",
      [
        "storage",
        "00c90ee8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bb5870",
      "READ",
      [
        "storage",
        "00c9b100",
        null,
        "pointer"
      ]
    ],
    [
      "00bb5888",
      "DATA",
      [
        "storage",
        "00c90f90",
        null,
        "pointer"
      ]
    ],
    [
      "00bb588c",
      "DATA",
      [
        "storage",
        "00c90fb8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb57d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb57bc.md#insn-00bb57d4) · [`00bb57f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb57bc.md#insn-00bb57f4) · [`00bb57fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb57bc.md#insn-00bb57fc)
- 新版 [`00bb5870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5858.md#insn-00bb5870) · [`00bb5890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5858.md#insn-00bb5890) · [`00bb5898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5858.md#insn-00bb5898)

~~~diff
- 00bb57d4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:30:8"]]
- 00bb57d4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb5870 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:100:8"]]
+ 00bb5870 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb57d4 bytes 291940f9
+ 00bb5870 bytes 298140f9
- 00bb57f4 ["INT_ADD", "register:40f0:8", ["const:bb57f4:8", "const:4:8"]]
- 00bb57f4 ["CALL", null, ["callee:00c5d280:8"]]
+ 00bb5890 ["INT_ADD", "register:40f0:8", ["const:bb5890:8", "const:4:8"]]
+ 00bb5890 ["CALL", null, ["callee:00c5d280:8"]]
- 00bb57f4 bytes 6f9e0294
+ 00bb5890 bytes 7c9e0294
- 00bb57fc ["INT_ADD", "register:40f0:8", ["const:bb57fc:8", "const:4:8"]]
- 00bb57fc ["CALL", null, ["callee:00c5d1b0:8"]]
+ 00bb5898 ["INT_ADD", "register:40f0:8", ["const:bb5898:8", "const:4:8"]]
+ 00bb5898 ["CALL", null, ["callee:00c5d1b0:8"]]
- 00bb57fc bytes 399e0294
+ 00bb5898 bytes 469e0294
~~~


<a id="compare-543d6457795f0f8f986b3f18d2fa16fe"></a>

### [`00bb5810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb5810.md) → [`00bb58ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb58ac.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEED2Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5d1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d1b0.md) · 呼出先 5件 [`00bb59c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb59c0.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5a000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a000.md) [`00c5be40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be40.md) [`00c5d190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d190.md)
- 新版 呼出元 1件 [`00c5d280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d280.md) · 呼出先 5件 [`00bb5a5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5a5c.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md) [`00c5a0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0d0.md) [`00c5bf10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf10.md) [`00c5d260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d260.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.31% / 新版 92.31%

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
      "definition_site": "00bb58c8",
      "incomplete_value": true,
      "site": "00bb58cc",
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
      "definition_site": "00bb582c",
      "incomplete_value": true,
      "site": "00bb5830",
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
      "definition_site": "00bb5934",
      "incomplete_value": true,
      "site": "00bb5934",
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
      "definition_site": "00bb5898",
      "incomplete_value": true,
      "site": "00bb5898",
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
      "00bb58c0",
      "READ",
      [
        "storage",
        "00c9b8f0",
        null,
        "pointer"
      ]
    ],
    [
      "00bb58cc",
      "DATA",
      [
        "storage",
        "00c90f70",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "00bb58f4",
      "READ",
      [
        "storage",
        "00c90f88",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      "00bb58c0",
      "READ",
      [
        "storage",
        "00c9b9c0",
        null,
        "pointer"
      ]
    ],
    [
      "00bb58cc",
      "DATA",
      [
        "storage",
        "00c91040",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "00bb58f4",
      "READ",
      [
        "storage",
        "00c91058",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb5824`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb5810.md#insn-00bb5824) · [`00bb583c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb5810.md#insn-00bb583c) · [`00bb5844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb5810.md#insn-00bb5844)
- 新版 [`00bb58c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb58ac.md#insn-00bb58c0) · [`00bb58d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb58ac.md#insn-00bb58d8) · [`00bb58e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb58ac.md#insn-00bb58e0)

~~~diff
- 00bb5824 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:8f0:8"]]
- 00bb5824 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb58c0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9c0:8"]]
+ 00bb58c0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb5824 bytes 087944f9
+ 00bb58c0 bytes 08e144f9
- 00bb583c ["INT_ADD", "register:40f0:8", ["const:bb583c:8", "const:4:8"]]
- 00bb583c ["CALL", null, ["callee:00c5d260:8"]]
+ 00bb58d8 ["INT_ADD", "register:40f0:8", ["const:bb58d8:8", "const:4:8"]]
+ 00bb58d8 ["CALL", null, ["callee:00c5d260:8"]]
- 00bb583c bytes 559e0294
+ 00bb58d8 bytes 629e0294
- 00bb5844 ["INT_ADD", "register:40f0:8", ["const:bb5844:8", "const:4:8"]]
- 00bb5844 ["CALL", null, ["callee:00c5a0d0:8"]]
+ 00bb58e0 ["INT_ADD", "register:40f0:8", ["const:bb58e0:8", "const:4:8"]]
+ 00bb58e0 ["CALL", null, ["callee:00c5a0d0:8"]]
- 00bb5844 bytes ef910294
+ 00bb58e0 bytes fc910294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66e0e02681b5e188f4efbee7436d2c54"></a>

### [`00bb59c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb59c0.md) → [`00bb5a5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5a5c.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEE6setbufEPcl

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 4件 [`00bb54e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb54e8.md) [`00bb5810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb5810.md) [`00c0568c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c0568c.md) [`00c05944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05944.md) · 呼出先 2件 [`00c5be40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be40.md) [`00c5be50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be50.md)
- 新版 呼出元 4件 [`00bb5584`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5584.md) [`00bb58ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb58ac.md) [`00c05728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c05728.md) [`00c059e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c059e0.md) · 呼出先 2件 [`00c5bf10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf10.md) [`00c5bf20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 92.31% / 新版 88.89%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb59f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb59c0.md#insn-00bb59f8) · [`00bb5a0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb59c0.md#insn-00bb5a0c) · [`00bb5a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb59c0.md#insn-00bb5a58)
- 新版 [`00bb5a94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5a5c.md#insn-00bb5a94) · [`00bb5aa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5a5c.md#insn-00bb5aa8) · [`00bb5af4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5a5c.md#insn-00bb5af4)

~~~diff
- 00bb59f8 ["INT_ADD", "register:40f0:8", ["const:bb59f8:8", "const:4:8"]]
- 00bb59f8 ["CALL", null, ["callee:00c5bf10:8"]]
+ 00bb5a94 ["INT_ADD", "register:40f0:8", ["const:bb5a94:8", "const:4:8"]]
+ 00bb5a94 ["CALL", null, ["callee:00c5bf10:8"]]
- 00bb59f8 bytes 12990294
+ 00bb5a94 bytes 1f990294
- 00bb5a0c ["INT_ADD", "register:40f0:8", ["const:bb5a0c:8", "const:4:8"]]
- 00bb5a0c ["CALL", null, ["callee:00c5bf10:8"]]
+ 00bb5aa8 ["INT_ADD", "register:40f0:8", ["const:bb5aa8:8", "const:4:8"]]
+ 00bb5aa8 ["CALL", null, ["callee:00c5bf10:8"]]
- 00bb5a0c bytes 0d990294
+ 00bb5aa8 bytes 1a990294
- 00bb5a58 ["BRANCH", null, ["local:b16:8"]]
+ 00bb5af4 ["BRANCH", null, ["local:b17:8"]]
- 00bb5a58 bytes 13000014
+ 00bb5af4 bytes 13000014
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f89b744d4f3da27e0d88a0c9ec00282"></a>

### [`00bb5ab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb5ab8.md) → [`00bb5b54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5b54.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEE7seekoffExNS_8ios_base7seekdirEj

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bb62ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb62ec.md) [`00c5d1e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d1e0.md) [`00c5d1f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d1f0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bb6388`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6388.md) [`00c5d2b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2b0.md) [`00c5d2c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2c0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 72.92% / 新版 72.92%

CFGの説明率　旧版 23.81% / 新版 23.81%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb5ab8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb5ab8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb5abc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb5ab8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb5abc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb5ac0",
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
      "00bb5b54",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bb5b58",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bb5b5c",
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

- 旧版 [`00bb5ab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb5ab8.md#insn-00bb5ab8) · [`00bb5abc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb5ab8.md#insn-00bb5abc) · [`00bb5ac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb5ab8.md#insn-00bb5ac0)

~~~diff
- 00bb5ab8 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bb5ab8 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bb5ab8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bb5ab8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bb5ab8 bytes f657bda9
- 00bb5abc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bb5abc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bb5abc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bb5abc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb5abc bytes f44f01a9
- 00bb5ac0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bb5ac0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bb5ac0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bb5ac0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb5ac0 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da75e4964d74aa0626a56eef530f8bb9"></a>

### [`00bb5be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb5be8.md) → [`00bb5c84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5c84.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEE4syncEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d190.md) · 呼出先 5件 [`00bb62ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb62ec.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a1b0.md) [`00c5a220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a220.md) [`00c5d1e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d1e0.md)
- 新版 呼出元 1件 [`00c5d260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d260.md) · 呼出先 5件 [`00bb6388`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6388.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a280.md) [`00c5a2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a2f0.md) [`00c5d2b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2b0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 67.39% / 新版 65.96%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb5bec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb5bf0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb5bf0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb5bec",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb5bf0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb5bf4",
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
      "00bb5c88",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00bb5c8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bb5c90",
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

- 旧版 [`00bb5bec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb5be8.md#insn-00bb5bec) · [`00bb5bf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb5be8.md#insn-00bb5bf0) · [`00bb5bf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb5be8.md#insn-00bb5bf4)

~~~diff
- 00bb5bec ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00bb5bec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 00bb5bec bytes f70b00f9
- 00bb5bf0 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bb5bf0 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bb5bf0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bb5bf0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb5bf0 bytes f65702a9
- 00bb5bf4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bb5bf4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bb5bf4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00bb5bf4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb5bf4 bytes f44f03a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59bd418274810e0d522719c14c6f1150"></a>

### [`00bb5dd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb5dd8.md) → [`00bb5e74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5e74.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEE9underflowEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bb62ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb62ec.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c5a080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a080.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bb6388`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6388.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c5a150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a150.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 88.05% / 新版 88.05%

CFGの説明率　旧版 52.83% / 新版 52.83%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 4件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb5e90"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb5e90"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb5e94"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bb5ef4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bb5e88"
      ]
    ],
    [
      "unmatched:00bb5e84",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb5ef8"
      ]
    ]
  ],
  "added": [
    [
      "00bb5ef4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb5f24"
      ]
    ],
    [
      "00bb5f20",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb5ef8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb5e84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb5dd8.md#insn-00bb5e84) · [`00bb5e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb5dd8.md#insn-00bb5e90) · [`00bb5e94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb5dd8.md#insn-00bb5e94)

~~~diff
- 00bb5e84 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bb5e84 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bb5e84 bytes c8feffb5
- 00bb5e90 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00bb5e90 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00bb5e90 ["INT_ADD", "tmp:2:8", ["register:4098:8", "const:10:8"]]
- 00bb5e90 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb5e90 bytes 6a2201a9
- 00bb5e94 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:20:8"]]
- 00bb5e94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bb5e94 bytes 681200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83b724df85bbc51ab351c21c2a8a9b15"></a>

### [`00bb636c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb636c.md) → [`00bb6408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6408.md) FUN_00bb6408

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5d0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0e0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md) [`00c5d1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d1b0.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 86.21% / 新版 86.21%

CFGの説明率　旧版 25.00% / 新版 12.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb642c",
      "incomplete_value": true,
      "site": "00bb6434",
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
      "definition_site": "00bb6390",
      "incomplete_value": true,
      "site": "00bb6398",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb643c",
      "incomplete_value": true,
      "site": "00bb643c",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb63a0",
      "incomplete_value": true,
      "site": "00bb63a0",
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
            "const:18:8"
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
      "definition_site": "00bb643c",
      "incomplete_value": true,
      "site": "00bb643c",
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
      "definition_site": "00bb63a0",
      "incomplete_value": true,
      "site": "00bb63a0",
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
      "00bb6418",
      "READ",
      [
        "storage",
        "00c9ac88",
        null,
        "pointer"
      ]
    ],
    [
      "00bb6420",
      "READ",
      [
        "storage",
        "00c9abc0",
        null,
        "pointer"
      ]
    ],
    [
      "00bb6434",
      "DATA",
      [
        "storage",
        "00c91038",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bb6418",
      "READ",
      [
        "storage",
        "00c9ad58",
        null,
        "pointer"
      ]
    ],
    [
      "00bb6420",
      "READ",
      [
        "storage",
        "00c9ac90",
        null,
        "pointer"
      ]
    ],
    [
      "00bb6434",
      "DATA",
      [
        "storage",
        "00c91108",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb63c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb636c.md#insn-00bb63c0) · [`00bb63c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb636c.md#insn-00bb63c4)
- 新版 [`00bb6460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6408.md#insn-00bb6460) · [`00bb645c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6408.md#insn-00bb645c)

~~~diff
- 00bb63c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8:8"]]
- 00bb63c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bb63c0 bytes 680600f9
- 00bb63c4 ["INT_ADD", "register:40f0:8", ["const:bb63c4:8", "const:4:8"]]
- 00bb63c4 ["CALL", null, ["callee:00c58360:8"]]
+ 00bb6460 ["INT_ADD", "register:40f0:8", ["const:bb6460:8", "const:4:8"]]
+ 00bb6460 ["CALL", null, ["callee:00c58360:8"]]
- 00bb63c4 bytes b3870294
+ 00bb6460 bytes c0870294
+ 00bb645c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8:8"]]
+ 00bb645c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00bb645c bytes 680600f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c746c44157195d854e8c877efa9f1acb"></a>

### [`00bb63e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb63e0.md) → [`00bb647c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb647c.md) FUN_00bb647c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5d0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0e0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md) [`00c5d1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d1b0.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 41.94% / 新版 41.94%

CFGの説明率　旧版 9.09% / 新版 11.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 7件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb63e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb63e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb63e4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb63e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb63e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb63f8",
      "READ",
      [
        "storage",
        "00c9ac88",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bb647c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bb6480",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bb6494",
      "READ",
      [
        "storage",
        "00c9ad58",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb63e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb63e0.md#insn-00bb63e0) · [`00bb63e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb63e0.md#insn-00bb63e4) · [`00bb640c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb63e0.md#insn-00bb640c)

~~~diff
- 00bb63e0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bb63e0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bb63e0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bb63e0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bb63e0 bytes f44fbea9
- 00bb63e4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bb63e4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bb63e4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bb63e4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb63e4 bytes fd7b01a9
- 00bb640c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bb640c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 00bb640c bytes 8a0200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6af081bc5b9d65d9e3f57d28677ece6"></a>

### [`00bb645c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb645c.md) → [`00bb64f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb64f8.md) FUN_00bb64f8

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5d0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0e0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md) [`00c5d1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d1b0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 63.64% / 新版 63.64%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb6488"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb648c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb64a0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb6474",
      "READ",
      [
        "storage",
        "00c9ac88",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bb6488",
      "DATA",
      [
        "storage",
        "00c91010",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bb648c",
      "DATA",
      [
        "storage",
        "00c91038",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bb6510",
      "READ",
      [
        "storage",
        "00c9ad58",
        null,
        "pointer"
      ]
    ],
    [
      "00bb6524",
      "DATA",
      [
        "storage",
        "00c910e0",
        null,
        "pointer"
      ]
    ],
    [
      "00bb6528",
      "DATA",
      [
        "storage",
        "00c91108",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb6488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb645c.md#insn-00bb6488) · [`00bb648c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb645c.md#insn-00bb648c) · [`00bb64a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb645c.md#insn-00bb64a0)

~~~diff
- 00bb6488 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bb6488 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 00bb6488 bytes 6a0200f9
- 00bb648c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bb648c ["INT_ADD", "register:40a0:8", ["register:40a0:8", "const:70:8"]]
- 00bb648c ["STORE", null, ["const:1b1:8", "register:40a0:8", "tmp:0:8"]]
- 00bb648c bytes 880e07f8
- 00bb64a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8:8"]]
- 00bb64a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00bb64a0 bytes 690600f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-edd2258717a1d536e0bcbfb2297391bd"></a>

### [`00bb64e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb64e0.md) → [`00bb657c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb657c.md) FUN_00bb657c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5d0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0e0.md) [`00c5d1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d1b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5d1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d1b0.md) [`00c5d280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d280.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 30.00% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb650c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb6510"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bb65a8"
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
      "unmatched:00bb64f8",
      "READ",
      [
        "storage",
        "00c9aec0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bb650c",
      "DATA",
      [
        "storage",
        "00c910c8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bb6510",
      "DATA",
      [
        "storage",
        "00c910f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bb6594",
      "READ",
      [
        "storage",
        "00c9af90",
        null,
        "pointer"
      ]
    ],
    [
      "00bb65a8",
      "DATA",
      [
        "storage",
        "00c91198",
        null,
        "pointer"
      ]
    ],
    [
      "00bb65ac",
      "DATA",
      [
        "storage",
        "00c911c0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb650c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb64e0.md#insn-00bb650c) · [`00bb6510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb64e0.md#insn-00bb6510) · [`00bb6514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb64e0.md#insn-00bb6514)
- 新版 [`00bb65b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb657c.md#insn-00bb65b0)

~~~diff
- 00bb650c ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00bb650c ["COPY", "tmp:1:8", ["register:4000:8"]]
- 00bb650c ["INT_ADD", "register:4000:8", ["register:4000:8", "const:8:8"]]
- 00bb650c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00bb650c bytes 0a8400f8
- 00bb6510 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bb6510 ["INT_ADD", "register:4098:8", ["register:4098:8", "const:b0:8"]]
- 00bb6510 ["STORE", null, ["const:1b1:8", "register:4098:8", "tmp:0:8"]]
- 00bb6510 bytes 680e0bf8
- 00bb6514 ["INT_ADD", "register:40f0:8", ["const:bb6514:8", "const:4:8"]]
- 00bb6514 ["CALL", null, ["callee:00c5d280:8"]]
+ 00bb65b0 ["INT_ADD", "register:40f0:8", ["const:bb65b0:8", "const:4:8"]]
+ 00bb65b0 ["CALL", null, ["callee:00c5d280:8"]]
- 00bb6514 bytes 279b0294
+ 00bb65b0 bytes 349b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0bf5d9dc3b92fe55b27fc0027a0bb6c8"></a>

### [`00bb6528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6528.md) → [`00bb65c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb65c4.md) FUN_00bb65c4

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5d0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0e0.md) [`00c5d1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d1b0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5d1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d1b0.md) [`00c5d280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d280.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 18.18% / 新版 22.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb6528"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb6528"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb652c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb6528",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb652c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb6538",
      "READ",
      [
        "storage",
        "00c9aec0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bb65c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bb65c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bb65d4",
      "READ",
      [
        "storage",
        "00c9af90",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb6528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6528.md#insn-00bb6528) · [`00bb652c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6528.md#insn-00bb652c) · [`00bb6550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6528.md#insn-00bb6550)

~~~diff
- 00bb6528 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bb6528 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bb6528 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bb6528 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bb6528 bytes f44fbea9
- 00bb652c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bb652c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bb652c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bb652c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb652c bytes fd7b01a9
- 00bb6550 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bb6550 ["INT_ADD", "register:40a0:8", ["register:40a0:8", "const:b0:8"]]
- 00bb6550 ["STORE", null, ["const:1b1:8", "register:40a0:8", "tmp:0:8"]]
- 00bb6550 bytes 880e0bf8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8349e43673619149e85106d518ea22b"></a>

### [`00bb6604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6604.md) → [`00bb66a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb66a0.md) _ZNKSt6__ndk110__function6__funcIPFccENS_9allocatorIS3_EES2_E7__cloneEPNS0_6__baseIS2_EE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies, store_value

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb66a8",
      "incomplete_value": true,
      "site": "00bb66ac",
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
      "definition_site": "00bb660c",
      "incomplete_value": true,
      "site": "00bb6610",
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
      "00bb66a4",
      "READ",
      [
        "storage",
        "00c9b8e8",
        null,
        "pointer"
      ]
    ],
    [
      "00bb66ac",
      "DATA",
      [
        "storage",
        "00c91178",
        null,
        "undefined1[88]"
      ]
    ]
  ],
  "added": [
    [
      "00bb66a4",
      "READ",
      [
        "storage",
        "00c9b9b8",
        null,
        "pointer"
      ]
    ],
    [
      "00bb66ac",
      "DATA",
      [
        "storage",
        "00c91248",
        null,
        "undefined1[88]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb6608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6604.md#insn-00bb6608)
- 新版 [`00bb66a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb66a0.md#insn-00bb66a4)

~~~diff
- 00bb6608 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:8e8:8"]]
- 00bb6608 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb66a4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
+ 00bb66a4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb6608 bytes 087544f9
+ 00bb66a4 bytes 08dd44f9
~~~


<a id="compare-46bb2a20929123bb54b8b3f6ba2eee2a"></a>

### [`00bb6660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6660.md) → [`00bb66fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb66fc.md) _INIT_284

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bb3db4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb3/00bb3db4.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bb3e50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb3/00bb3e50.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 29.41% / 新版 29.41%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb6660"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb6660"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb6694"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb6660",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb666c",
      "PARAM",
      [
        "storage",
        "002b617c",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb6684",
      "READ",
      [
        "storage",
        "00c9b830",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bb66fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bb6708",
      "PARAM",
      [
        "storage",
        "002b61bc",
        null,
        null
      ]
    ],
    [
      "00bb6720",
      "READ",
      [
        "storage",
        "00c9b900",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb6660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6660.md#insn-00bb6660) · [`00bb6678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6660.md#insn-00bb6678) · [`00bb6694`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6660.md#insn-00bb6694)
- 新版 [`00bb6714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb66fc.md#insn-00bb6714)

~~~diff
- 00bb6660 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bb6660 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bb6660 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 00bb6660 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bb6660 bytes fd7bbfa9
- 00bb6678 ["INT_ADD", "register:40f0:8", ["const:bb6678:8", "const:4:8"]]
- 00bb6678 ["CALL", null, ["callee:00c5d2f0:8"]]
+ 00bb6714 ["INT_ADD", "register:40f0:8", ["const:bb6714:8", "const:4:8"]]
+ 00bb6714 ["CALL", null, ["callee:00c5d2f0:8"]]
- 00bb6678 bytes ea9a0294
+ 00bb6714 bytes f79a0294
- 00bb6694 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00bb6694 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb6694 bytes 200000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b910561eb6fafc6e33cb3e60f664f7b0"></a>

### [`00bb66e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb66e4.md) → [`00bb6780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6780.md) FUN_00bb6780

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00bb8bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8bdc.md) · 呼出先 2件 [`00c5ac60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac60.md) [`00c5d440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d440.md)
- 新版 呼出元 1件 [`00bb8c78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8c78.md) · 呼出先 2件 [`00c5ad30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad30.md) [`00c5d510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d510.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 50.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb66f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb66e4.md#insn-00bb66f4)
- 新版 [`00bb6790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6780.md#insn-00bb6790)

~~~diff
- 00bb66f4 ["INT_ADD", "register:40f0:8", ["const:bb66f4:8", "const:4:8"]]
- 00bb66f4 ["CALL", null, ["callee:00c5ad30:8"]]
+ 00bb6790 ["INT_ADD", "register:40f0:8", ["const:bb6790:8", "const:4:8"]]
+ 00bb6790 ["CALL", null, ["callee:00c5ad30:8"]]
- 00bb66f4 bytes 5b910294
+ 00bb6790 bytes 68910294
~~~


<a id="compare-b6b32c5666700781f5e61ca711950a80"></a>

### [`00bb6718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6718.md) → [`00bb67b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb67b4.md) _ZN8firebase9messaging8internal36RegisterTerminateOnDefaultAppDestroyEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d420.md) · 呼出先 5件 [`00bb764c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb764c.md) [`00c5abd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abd0.md) [`00c5abf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abf0.md) [`00c5ac00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac00.md) [`00c5ac60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac60.md)
- 新版 呼出元 1件 [`00c5d4f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d4f0.md) · 呼出先 5件 [`00bb76e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb76e8.md) [`00c5aca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aca0.md) [`00c5acc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5acc0.md) [`00c5acd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5acd0.md) [`00c5ad30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad30.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 68.75% / 新版 68.75%

CFGの説明率　旧版 33.33% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb67c0",
      "incomplete_value": false,
      "site": "00bb67c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:30e000:8"
          ],
          [
            "leaf",
            "const:71f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb6724",
      "incomplete_value": false,
      "site": "00bb6728",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:30e000:8"
          ],
          [
            "leaf",
            "const:6df:8"
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
      "00bb67c0",
      "PARAM",
      [
        "storage",
        "0030e6df",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bb6748",
      "PARAM",
      [
        "storage",
        "0030e6df",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bb674c",
      "PARAM",
      [
        "storage",
        "00bb764c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bb67c0",
      "PARAM",
      [
        "storage",
        "0030e71f",
        null,
        "string"
      ]
    ],
    [
      "00bb67e4",
      "PARAM",
      [
        "storage",
        "0030e71f",
        null,
        "string"
      ]
    ],
    [
      "00bb67e8",
      "PARAM",
      [
        "storage",
        "00bb76e8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb6728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6718.md#insn-00bb6728) · [`00bb6724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6718.md#insn-00bb6724) · [`00bb6738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6718.md#insn-00bb6738)
- 新版 [`00bb67c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb67b4.md#insn-00bb67c4) · [`00bb67c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb67b4.md#insn-00bb67c0) · [`00bb67d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb67b4.md#insn-00bb67d4)

~~~diff
- 00bb6728 ["INT_ADD", "register:40f0:8", ["const:bb6728:8", "const:4:8"]]
- 00bb6728 ["CALL", null, ["callee:00c5aca0:8"]]
+ 00bb67c4 ["INT_ADD", "register:40f0:8", ["const:bb67c4:8", "const:4:8"]]
+ 00bb67c4 ["CALL", null, ["callee:00c5aca0:8"]]
- 00bb6728 bytes 2a910294
+ 00bb67c4 bytes 37910294
- 00bb6724 ["COPY", "tmp:0:8", ["const:6df:8"]]
- 00bb6724 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bb6724 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bb6724 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bb67c0 ["COPY", "tmp:0:8", ["const:71f:8"]]
+ 00bb67c0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bb67c0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bb67c0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bb6724 bytes 007c1b91
+ 00bb67c0 bytes 007c1c91
- 00bb6738 ["INT_ADD", "register:40f0:8", ["const:bb6738:8", "const:4:8"]]
- 00bb6738 ["CALL", null, ["callee:00c5ad30:8"]]
+ 00bb67d4 ["INT_ADD", "register:40f0:8", ["const:bb67d4:8", "const:4:8"]]
+ 00bb67d4 ["CALL", null, ["callee:00c5ad30:8"]]
- 00bb6738 bytes 4a910294
+ 00bb67d4 bytes 57910294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27bd8f0985b9a7d3eefd3dd2f4a34b5b"></a>

### [`00bb6758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6758.md) → [`00bb67f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb67f4.md) _ZN8firebase9messaging8internal38UnregisterTerminateOnDefaultAppDestroyEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5d430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d430.md) · 呼出先 5件 [`00c5abd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abd0.md) [`00c5abf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abf0.md) [`00c5ac10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac10.md) [`00c5ac60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac60.md) [`00c5d410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d410.md)
- 新版 呼出元 1件 [`00c5d500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d500.md) · 呼出先 5件 [`00c5aca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aca0.md) [`00c5acc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5acc0.md) [`00c5ace0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ace0.md) [`00c5ad30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad30.md) [`00c5d4e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d4e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb6800",
      "incomplete_value": false,
      "site": "00bb6804",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:30e000:8"
          ],
          [
            "leaf",
            "const:71f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb6764",
      "incomplete_value": false,
      "site": "00bb6768",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:30e000:8"
          ],
          [
            "leaf",
            "const:6df:8"
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
      "00bb6800",
      "PARAM",
      [
        "storage",
        "0030e6df",
        null,
        "string"
      ]
    ],
    [
      "00bb6820",
      "PARAM",
      [
        "storage",
        "0030e6df",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bb6800",
      "PARAM",
      [
        "storage",
        "0030e71f",
        null,
        "string"
      ]
    ],
    [
      "00bb6820",
      "PARAM",
      [
        "storage",
        "0030e71f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb6768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6758.md#insn-00bb6768) · [`00bb6764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6758.md#insn-00bb6764) · [`00bb6770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6758.md#insn-00bb6770)
- 新版 [`00bb6804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb67f4.md#insn-00bb6804) · [`00bb6800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb67f4.md#insn-00bb6800) · [`00bb680c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb67f4.md#insn-00bb680c)

~~~diff
- 00bb6768 ["INT_ADD", "register:40f0:8", ["const:bb6768:8", "const:4:8"]]
- 00bb6768 ["CALL", null, ["callee:00c5aca0:8"]]
+ 00bb6804 ["INT_ADD", "register:40f0:8", ["const:bb6804:8", "const:4:8"]]
+ 00bb6804 ["CALL", null, ["callee:00c5aca0:8"]]
- 00bb6768 bytes 1a910294
+ 00bb6804 bytes 27910294
- 00bb6764 ["COPY", "tmp:0:8", ["const:6df:8"]]
- 00bb6764 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bb6764 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bb6764 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bb6800 ["COPY", "tmp:0:8", ["const:71f:8"]]
+ 00bb6800 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bb6800 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bb6800 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bb6764 bytes 007c1b91
+ 00bb6800 bytes 007c1c91
- 00bb6770 ["INT_ADD", "register:40f0:8", ["const:bb6770:8", "const:4:8"]]
- 00bb6770 ["CALL", null, ["callee:00c5d4e0:8"]]
+ 00bb680c ["INT_ADD", "register:40f0:8", ["const:bb680c:8", "const:4:8"]]
+ 00bb680c ["CALL", null, ["callee:00c5d4e0:8"]]
- 00bb6770 bytes 289b0294
+ 00bb680c bytes 359b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4e7ed68ef46601f405be3bc5b8310df"></a>

### [`00bb6798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6798.md) → [`00bb6834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6834.md) _ZN8firebase9messaging11SetListenerEPNS0_8ListenerE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d2b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d2b0.md) · 呼出先 5件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5d2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d2f0.md)
- 新版 呼出元 1件 [`00c5d380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d380.md) · 呼出先 5件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5d3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d3c0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 75.47% / 新版 75.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 5件, `call_argument_candidate` 2件, `store_condition` 7件, `store_destination` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb6888",
      "incomplete_value": true,
      "site": "00bb6888",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:338:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb67ec",
      "incomplete_value": true,
      "site": "00bb67ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:238:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb68b4",
      "incomplete_value": true,
      "site": "00bb68b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c0:8"
          ],
          [
            "leaf",
            "const:340:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb6818",
      "incomplete_value": true,
      "site": "00bb6818",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c0:8"
          ],
          [
            "leaf",
            "const:240:8"
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb68b8",
      "incomplete_value": true,
      "site": "00bb68b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d0:8"
          ],
          [
            "leaf",
            "const:330:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb681c",
      "incomplete_value": true,
      "site": "00bb681c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d0:8"
          ],
          [
            "leaf",
            "const:230:8"
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bb6854",
      "PARAM",
      [
        "storage",
        "01126208",
        null,
        null
      ]
    ],
    [
      "00bb6864",
      "READ",
      [
        "storage",
        "01126230",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb6868",
      "READ",
      [
        "storage",
        "01126238",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bb6854",
      "PARAM",
      [
        "storage",
        "01126308",
        null,
        null
      ]
    ],
    [
      "00bb6864",
      "READ",
      [
        "storage",
        "01126330",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb6868",
      "READ",
      [
        "storage",
        "01126338",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb67bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6798.md#insn-00bb67bc) · [`00bb67ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6798.md#insn-00bb67ec) · [`00bb6818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6798.md#insn-00bb6818)
- 新版 [`00bb6858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6834.md#insn-00bb6858) · [`00bb6888`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6834.md#insn-00bb6888) · [`00bb68b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6834.md#insn-00bb68b4)

~~~diff
- 00bb67bc ["INT_ADD", "register:40f0:8", ["const:bb67bc:8", "const:4:8"]]
- 00bb67bc ["CALL", null, ["callee:00c5aad0:8"]]
+ 00bb6858 ["INT_ADD", "register:40f0:8", ["const:bb6858:8", "const:4:8"]]
+ 00bb6858 ["CALL", null, ["callee:00c5aad0:8"]]
- 00bb67bc bytes 91900294
+ 00bb6858 bytes 9e900294
- 00bb67ec ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:238:8"]]
- 00bb67ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bb6888 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:338:8"]]
+ 00bb6888 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb67ec bytes e01e01f9
+ 00bb6888 bytes e09e01f9
- 00bb6818 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:240:8"]]
- 00bb6818 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bb68b4 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:340:8"]]
+ 00bb68b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb6818 bytes 002301f9
+ 00bb68b4 bytes 00a301f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0060222d661a926511d98a168a958cca"></a>

### [`00bb6960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6960.md) → [`00bb69fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb69fc.md) _ZN8firebase9messaging11HasListenerEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5d2a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d2a0.md) · 呼出先 2件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)
- 新版 呼出元 1件 [`00c5d370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d370.md) · 呼出先 2件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb6a10",
      "incomplete_value": false,
      "site": "00bb6a14",
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
            "const:308:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb6974",
      "incomplete_value": false,
      "site": "00bb6978",
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
            "const:208:8"
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
      "00bb6a10",
      "PARAM",
      [
        "storage",
        "01126208",
        null,
        null
      ]
    ],
    [
      "00bb6a1c",
      "READ",
      [
        "storage",
        "01126230",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb6a20",
      "PARAM",
      [
        "storage",
        "01126208",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bb6a10",
      "PARAM",
      [
        "storage",
        "01126308",
        null,
        null
      ]
    ],
    [
      "00bb6a1c",
      "READ",
      [
        "storage",
        "01126330",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb6a20",
      "PARAM",
      [
        "storage",
        "01126308",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb6978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6960.md#insn-00bb6978) · [`00bb6970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6960.md#insn-00bb6970) · [`00bb6980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6960.md#insn-00bb6980)
- 新版 [`00bb6a14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb69fc.md#insn-00bb6a14) · [`00bb6a0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb69fc.md#insn-00bb6a0c) · [`00bb6a1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb69fc.md#insn-00bb6a1c)

~~~diff
- 00bb6978 ["INT_ADD", "register:40f0:8", ["const:bb6978:8", "const:4:8"]]
- 00bb6978 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00bb6a14 ["INT_ADD", "register:40f0:8", ["const:bb6a14:8", "const:4:8"]]
+ 00bb6a14 ["CALL", null, ["callee:00c5aad0:8"]]
- 00bb6978 bytes 22900294
+ 00bb6a14 bytes 2f900294
- 00bb6970 ["COPY", "tmp:0:8", ["const:208:8"]]
- 00bb6970 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00bb6970 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00bb6970 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00bb6a0c ["COPY", "tmp:0:8", ["const:308:8"]]
+ 00bb6a0c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00bb6a0c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00bb6a0c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00bb6970 bytes 73220891
+ 00bb6a0c bytes 73220c91
- 00bb6980 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:230:8"]]
- 00bb6980 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb6a1c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:330:8"]]
+ 00bb6a1c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb6980 bytes 141941f9
+ 00bb6a1c bytes 149941f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-188228be60e7c686cf73df9f6a9bb8b9"></a>

### [`00bb69b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb69b8.md) → [`00bb6a54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6a54.md) _ZN8firebase9messaging23NotifyListenerOnMessageERKNS0_7MessageE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d3a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d3a0.md) · 呼出先 2件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)
- 新版 呼出元 1件 [`00c5d470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d470.md) · 呼出先 2件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 20.00% / 新版 20.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb69b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb69bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb69bc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb69b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb69bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb69cc",
      "PARAM",
      [
        "storage",
        "01126208",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bb6a54",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bb6a58",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bb6a68",
      "PARAM",
      [
        "storage",
        "01126308",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb69b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb69b8.md#insn-00bb69b8) · [`00bb69bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb69b8.md#insn-00bb69bc) · [`00bb69d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb69b8.md#insn-00bb69d0)

~~~diff
- 00bb69b8 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bb69b8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bb69b8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bb69b8 bytes f30f1ef8
- 00bb69bc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bb69bc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bb69bc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bb69bc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb69bc bytes fd7b01a9
- 00bb69d0 ["INT_ADD", "register:40f0:8", ["const:bb69d0:8", "const:4:8"]]
- 00bb69d0 ["CALL", null, ["callee:00c5aad0:8"]]
- 00bb69d0 bytes 0c900294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3107d57132905c83a833c6cc29f069a"></a>

### [`00bb6a28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6a28.md) → [`00bb6ac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6ac4.md) _ZN8firebase9messaging29NotifyListenerOnTokenReceivedEPKc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d3b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d3b0.md) · 呼出先 8件 [`00440c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440c3c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md)
- 新版 呼出元 1件 [`00c5d480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d480.md) · 呼出先 8件 [`00440c7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440c7c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 2件, `store_condition` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb6b54",
      "incomplete_value": true,
      "site": "00bb6b54",
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
    "old": {
      "definition_site": "00bb6ab8",
      "incomplete_value": true,
      "site": "00bb6ab8",
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
            "const:238:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb6b98",
      "incomplete_value": false,
      "site": "00bb6b98",
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
            "const:348:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb6afc",
      "incomplete_value": false,
      "site": "00bb6afc",
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
            "const:248:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bb6aec",
      "incomplete_value": true,
      "site": "00bb6aec",
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
      "definition_site": "00bb6a50",
      "incomplete_value": true,
      "site": "00bb6a50",
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
      "00bb6adc",
      "PARAM",
      [
        "storage",
        "01126208",
        null,
        null
      ]
    ],
    [
      "00bb6ae8",
      "READ",
      [
        "storage",
        "01126238",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb6b54",
      "WRITE",
      [
        "storage",
        "01126238",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bb6adc",
      "PARAM",
      [
        "storage",
        "01126308",
        null,
        null
      ]
    ],
    [
      "00bb6ae8",
      "READ",
      [
        "storage",
        "01126338",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb6b54",
      "WRITE",
      [
        "storage",
        "01126338",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb6a40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6a28.md#insn-00bb6a40) · [`00bb6a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6a28.md#insn-00bb6a44) · [`00bb6ab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6a28.md#insn-00bb6ab8)
- 新版 [`00bb6adc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6ac4.md#insn-00bb6adc) · [`00bb6ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6ac4.md#insn-00bb6ae0) · [`00bb6b54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6ac4.md#insn-00bb6b54)

~~~diff
- 00bb6a40 ["COPY", "tmp:0:8", ["const:208:8"]]
- 00bb6a40 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bb6a40 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bb6a40 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bb6adc ["COPY", "tmp:0:8", ["const:308:8"]]
+ 00bb6adc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bb6adc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bb6adc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bb6a40 bytes 00200891
+ 00bb6adc bytes 00200c91
- 00bb6a44 ["INT_ADD", "register:40f0:8", ["const:bb6a44:8", "const:4:8"]]
- 00bb6a44 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00bb6ae0 ["INT_ADD", "register:40f0:8", ["const:bb6ae0:8", "const:4:8"]]
+ 00bb6ae0 ["CALL", null, ["callee:00c5aad0:8"]]
- 00bb6a44 bytes ef8f0294
+ 00bb6ae0 bytes fc8f0294
- 00bb6ab8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:238:8"]]
- 00bb6ab8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bb6b54 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:338:8"]]
+ 00bb6b54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb6ab8 bytes a01e01f9
+ 00bb6b54 bytes a09e01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f94aa5c4801b6f316ef55229f485c580"></a>

### [`00bb6b48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6b48.md) → [`00bb6be4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6be4.md) _ZN8firebase9messaging36NotifyListenerOnRegistrationReceivedEPKc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d3c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d3c0.md) · 呼出先 5件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5b0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0b0.md)
- 新版 呼出元 1件 [`00c5d490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d490.md) · 呼出先 5件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5b180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b180.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 2件, `store_condition` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb6c30",
      "incomplete_value": true,
      "site": "00bb6c30",
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
            "const:340:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb6b94",
      "incomplete_value": true,
      "site": "00bb6b94",
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
            "const:240:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb6c74",
      "incomplete_value": false,
      "site": "00bb6c74",
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
            "const:349:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb6bd8",
      "incomplete_value": false,
      "site": "00bb6bd8",
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
            "const:249:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bb6c18",
      "incomplete_value": true,
      "site": "00bb6c18",
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
      "definition_site": "00bb6b7c",
      "incomplete_value": true,
      "site": "00bb6b7c",
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
      "00bb6c08",
      "PARAM",
      [
        "storage",
        "01126208",
        null,
        null
      ]
    ],
    [
      "00bb6c14",
      "READ",
      [
        "storage",
        "01126240",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb6c30",
      "WRITE",
      [
        "storage",
        "01126240",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bb6c08",
      "PARAM",
      [
        "storage",
        "01126308",
        null,
        null
      ]
    ],
    [
      "00bb6c14",
      "READ",
      [
        "storage",
        "01126340",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb6c30",
      "WRITE",
      [
        "storage",
        "01126340",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb6b70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6b48.md#insn-00bb6b70) · [`00bb6b94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6b48.md#insn-00bb6b94) · [`00bb6bd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6b48.md#insn-00bb6bd8)
- 新版 [`00bb6c0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6be4.md#insn-00bb6c0c) · [`00bb6c30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6be4.md#insn-00bb6c30) · [`00bb6c74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6be4.md#insn-00bb6c74)

~~~diff
- 00bb6b70 ["INT_ADD", "register:40f0:8", ["const:bb6b70:8", "const:4:8"]]
- 00bb6b70 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00bb6c0c ["INT_ADD", "register:40f0:8", ["const:bb6c0c:8", "const:4:8"]]
+ 00bb6c0c ["CALL", null, ["callee:00c5aad0:8"]]
- 00bb6b70 bytes a48f0294
+ 00bb6c0c bytes b18f0294
- 00bb6b94 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:240:8"]]
- 00bb6b94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bb6c30 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:340:8"]]
+ 00bb6c30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb6b94 bytes a02201f9
+ 00bb6c30 bytes a0a201f9
- 00bb6bd8 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00bb6bd8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:249:8"]]
- 00bb6bd8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bb6c74 ["COPY", "tmp:0:4", ["register:4048:4"]]
+ 00bb6c74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:349:8"]]
+ 00bb6c74 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bb6bd8 bytes 09250939
+ 00bb6c74 bytes 09250d39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-401ef49beaeb2775a694564453661c8f"></a>

### [`00bb6c18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6c18.md) → [`00bb6cb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6cb4.md) _ZN8firebase9messaging38NotifyListenerOnUnregistrationReceivedEPKc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d3d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d3d0.md) · 呼出先 7件 [`00440c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440c3c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md)
- 新版 呼出元 1件 [`00c5d4a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d4a0.md) · 呼出先 7件 [`00440c7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440c7c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb6d50",
      "incomplete_value": true,
      "site": "00bb6d50",
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
            "const:340:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb6cb4",
      "incomplete_value": true,
      "site": "00bb6cb4",
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
            "const:240:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb6d54",
      "incomplete_value": false,
      "site": "00bb6d54",
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
            "const:349:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb6cb8",
      "incomplete_value": false,
      "site": "00bb6cb8",
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
            "const:249:8"
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
      "definition_site": "00bb6ce8",
      "incomplete_value": true,
      "site": "00bb6ce8",
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
      "definition_site": "00bb6c4c",
      "incomplete_value": true,
      "site": "00bb6c4c",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bb6cd8",
      "PARAM",
      [
        "storage",
        "01126208",
        null,
        null
      ]
    ],
    [
      "00bb6ce4",
      "READ",
      [
        "storage",
        "01126240",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb6d50",
      "WRITE",
      [
        "storage",
        "01126240",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bb6cd8",
      "PARAM",
      [
        "storage",
        "01126308",
        null,
        null
      ]
    ],
    [
      "00bb6ce4",
      "READ",
      [
        "storage",
        "01126340",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb6d50",
      "WRITE",
      [
        "storage",
        "01126340",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb6c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6c18.md#insn-00bb6c40) · [`00bb6cb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6c18.md#insn-00bb6cb4) · [`00bb6cb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6c18.md#insn-00bb6cb8)
- 新版 [`00bb6cdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6cb4.md#insn-00bb6cdc) · [`00bb6d50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6cb4.md#insn-00bb6d50) · [`00bb6d54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6cb4.md#insn-00bb6d54)

~~~diff
- 00bb6c40 ["INT_ADD", "register:40f0:8", ["const:bb6c40:8", "const:4:8"]]
- 00bb6c40 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00bb6cdc ["INT_ADD", "register:40f0:8", ["const:bb6cdc:8", "const:4:8"]]
+ 00bb6cdc ["CALL", null, ["callee:00c5aad0:8"]]
- 00bb6c40 bytes 708f0294
+ 00bb6cdc bytes 7d8f0294
- 00bb6cb4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:240:8"]]
- 00bb6cb4 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bb6cb4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bb6d50 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:340:8"]]
+ 00bb6d50 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bb6d50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00bb6cb4 bytes bf2201f9
+ 00bb6d50 bytes bfa201f9
- 00bb6cb8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bb6cb8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bb6cb8 ["INT_ADD", "tmp:2:8", ["register:4040:8", "const:249:8"]]
- 00bb6cb8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bb6d54 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bb6d54 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bb6d54 ["INT_ADD", "tmp:2:8", ["register:4040:8", "const:349:8"]]
+ 00bb6d54 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bb6cb8 bytes 1f250939
+ 00bb6d54 bytes 1f250d39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ed46924939e10a104a704a201611ae9"></a>

### [`00bb6db4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6db4.md) → [`00bb6e50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6e50.md) _ZN8firebase9messaging16PollableListenerD2Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5aac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aac0.md) [`00c5d380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d380.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ab90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab90.md) [`00c5d450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d450.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb6e6c",
      "incomplete_value": true,
      "site": "00bb6e70",
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
      "definition_site": "00bb6dd0",
      "incomplete_value": true,
      "site": "00bb6dd4",
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
      "00bb6e64",
      "READ",
      [
        "storage",
        "00c9b900",
        null,
        "pointer"
      ]
    ],
    [
      "00bb6e70",
      "DATA",
      [
        "storage",
        "00c91228",
        null,
        "undefined1[64]"
      ]
    ]
  ],
  "added": [
    [
      "00bb6e64",
      "READ",
      [
        "storage",
        "00c9b9d0",
        null,
        "pointer"
      ]
    ],
    [
      "00bb6e70",
      "DATA",
      [
        "storage",
        "00c912f8",
        null,
        "undefined1[64]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb6dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6db4.md#insn-00bb6dc8) · [`00bb6de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6db4.md#insn-00bb6de0) · [`00bb6de8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6db4.md#insn-00bb6de8)
- 新版 [`00bb6e64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6e50.md#insn-00bb6e64) · [`00bb6e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6e50.md#insn-00bb6e7c) · [`00bb6e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6e50.md#insn-00bb6e84)

~~~diff
- 00bb6dc8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:900:8"]]
- 00bb6dc8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb6e64 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
+ 00bb6e64 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb6dc8 bytes 088144f9
+ 00bb6e64 bytes 08e944f9
- 00bb6de0 ["INT_ADD", "register:40f0:8", ["const:bb6de0:8", "const:4:8"]]
- 00bb6de0 ["CALL", null, ["callee:00c5d450:8"]]
+ 00bb6e7c ["INT_ADD", "register:40f0:8", ["const:bb6e7c:8", "const:4:8"]]
+ 00bb6e7c ["CALL", null, ["callee:00c5d450:8"]]
- 00bb6de0 bytes 68990294
+ 00bb6e7c bytes 75990294
- 00bb6de8 ["INT_ADD", "register:40f0:8", ["const:bb6de8:8", "const:4:8"]]
- 00bb6de8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00bb6e84 ["INT_ADD", "register:40f0:8", ["const:bb6e84:8", "const:4:8"]]
+ 00bb6e84 ["CALL", null, ["callee:00c57f80:8"]]
- 00bb6de8 bytes 32840294
+ 00bb6e84 bytes 3f840294
~~~


<a id="compare-cb90b704b7451d6f5f73a6e889a2369d"></a>

### [`00bb6ebc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6ebc.md) → [`00bb6f58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6f58.md) _ZN8firebase9messaging16PollableListenerD0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5aac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aac0.md) [`00c5d380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d380.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ab90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab90.md) [`00c5d450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d450.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb6f74",
      "incomplete_value": true,
      "site": "00bb6f78",
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
      "definition_site": "00bb6ed8",
      "incomplete_value": true,
      "site": "00bb6edc",
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
      "00bb6f6c",
      "READ",
      [
        "storage",
        "00c9b900",
        null,
        "pointer"
      ]
    ],
    [
      "00bb6f78",
      "DATA",
      [
        "storage",
        "00c91228",
        null,
        "undefined1[64]"
      ]
    ]
  ],
  "added": [
    [
      "00bb6f6c",
      "READ",
      [
        "storage",
        "00c9b9d0",
        null,
        "pointer"
      ]
    ],
    [
      "00bb6f78",
      "DATA",
      [
        "storage",
        "00c912f8",
        null,
        "undefined1[64]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb6ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6ebc.md#insn-00bb6ed0) · [`00bb6ee8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6ebc.md#insn-00bb6ee8) · [`00bb6ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6ebc.md#insn-00bb6ef0)
- 新版 [`00bb6f6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6f58.md#insn-00bb6f6c) · [`00bb6f84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6f58.md#insn-00bb6f84) · [`00bb6f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6f58.md#insn-00bb6f8c)

~~~diff
- 00bb6ed0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:900:8"]]
- 00bb6ed0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb6f6c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
+ 00bb6f6c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb6ed0 bytes 088144f9
+ 00bb6f6c bytes 08e944f9
- 00bb6ee8 ["INT_ADD", "register:40f0:8", ["const:bb6ee8:8", "const:4:8"]]
- 00bb6ee8 ["CALL", null, ["callee:00c5d450:8"]]
+ 00bb6f84 ["INT_ADD", "register:40f0:8", ["const:bb6f84:8", "const:4:8"]]
+ 00bb6f84 ["CALL", null, ["callee:00c5d450:8"]]
- 00bb6ee8 bytes 26990294
+ 00bb6f84 bytes 33990294
- 00bb6ef0 ["INT_ADD", "register:40f0:8", ["const:bb6ef0:8", "const:4:8"]]
- 00bb6ef0 ["CALL", null, ["callee:00c57f80:8"]]
+ 00bb6f8c ["INT_ADD", "register:40f0:8", ["const:bb6f8c:8", "const:4:8"]]
+ 00bb6f8c ["CALL", null, ["callee:00c57f80:8"]]
- 00bb6ef0 bytes f0830294
+ 00bb6f8c bytes fd830294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-506e49a72997ce590b9ba5b098055f31"></a>

### [`00bb764c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb764c.md) → [`00bb76e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb76e8.md) FUN_00bb76e8

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bb6718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6718.md) · 呼出先 3件 [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5d410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d410.md) [`00c5d440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d440.md)
- 新版 呼出元 1件 [`00bb67b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb67b4.md) · 呼出先 3件 [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5d4e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d4e0.md) [`00c5d510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d510.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb76f4",
      "incomplete_value": false,
      "site": "00bb76f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29f000:8"
          ],
          [
            "leaf",
            "const:b33:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb7658",
      "incomplete_value": false,
      "site": "00bb765c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29f000:8"
          ],
          [
            "leaf",
            "const:b80:8"
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
      "00bb76f4",
      "PARAM",
      [
        "storage",
        "0029fb80",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bb76f4",
      "PARAM",
      [
        "storage",
        "0029fb33",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb765c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb764c.md#insn-00bb765c) · [`00bb7658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb764c.md#insn-00bb7658) · [`00bb7660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb7/00bb764c.md#insn-00bb7660)
- 新版 [`00bb76f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb76e8.md#insn-00bb76f8) · [`00bb76f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb76e8.md#insn-00bb76f4) · [`00bb76fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb76e8.md#insn-00bb76fc)

~~~diff
- 00bb765c ["INT_ADD", "register:40f0:8", ["const:bb765c:8", "const:4:8"]]
- 00bb765c ["CALL", null, ["callee:00c5ad70:8"]]
+ 00bb76f8 ["INT_ADD", "register:40f0:8", ["const:bb76f8:8", "const:4:8"]]
+ 00bb76f8 ["CALL", null, ["callee:00c5ad70:8"]]
- 00bb765c bytes 918d0294
+ 00bb76f8 bytes 9e8d0294
- 00bb7658 ["COPY", "tmp:0:8", ["const:b80:8"]]
- 00bb7658 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bb7658 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bb7658 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bb76f4 ["COPY", "tmp:0:8", ["const:b33:8"]]
+ 00bb76f4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bb76f4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bb76f4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bb7658 bytes 00002e91
+ 00bb76f4 bytes 00cc2c91
- 00bb7660 ["INT_ADD", "register:40f0:8", ["const:bb7660:8", "const:4:8"]]
- 00bb7660 ["CALL", null, ["callee:00c5d4e0:8"]]
+ 00bb76fc ["INT_ADD", "register:40f0:8", ["const:bb76fc:8", "const:4:8"]]
+ 00bb76fc ["CALL", null, ["callee:00c5d4e0:8"]]
- 00bb7660 bytes 6c970294
+ 00bb76fc bytes 79970294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9130d825c2c85814af83251982a4d0cb"></a>

### [`00bb8388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8388.md) → [`00bb8424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8424.md) _ZNSt6__ndk15dequeIN8firebase9messaging7MessageENS_9allocatorIS3_EEE19__add_back_capacityEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d4b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d4b0.md) · 呼出先 9件 [`00b402c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b402c0.md) [`00bb859c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb859c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00c5d580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d580.md) · 呼出先 9件 [`00b4035c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b4035c.md) [`00bb8638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8638.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 95.45% / 新版 95.45%

CFGの説明率　旧版 64.00% / 新版 61.54%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb84e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb84ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bb8584"
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
      "unmatched:00bb84ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb84f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb85a8"
      ]
    ],
    [
      "unmatched:00bb8538",
      "PARAM",
      [
        "storage",
        "002a867b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bb8588",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00bb858c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb85a8"
      ]
    ],
    [
      "00bb85d4",
      "PARAM",
      [
        "storage",
        "002a861f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb84a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8388.md#insn-00bb84a0) · [`00bb84e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8388.md#insn-00bb84e8) · [`00bb84ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8388.md#insn-00bb84ec)
- 新版 [`00bb853c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8424.md#insn-00bb853c)

~~~diff
- 00bb84a0 ["INT_ADD", "register:40f0:8", ["const:bb84a0:8", "const:4:8"]]
- 00bb84a0 ["CALL", null, ["callee:00c5d570:8"]]
+ 00bb853c ["INT_ADD", "register:40f0:8", ["const:bb853c:8", "const:4:8"]]
+ 00bb853c ["CALL", null, ["callee:00c5d570:8"]]
- 00bb84a0 bytes 00940294
+ 00bb853c bytes 0d940294
- 00bb84e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:10:8"]]
- 00bb84e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00bb84e8 bytes 6006803d
- 00bb84ec ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00bb84ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5020:16"]]
- 00bb84ec bytes e10b803d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6af3d9071fdfb0621dddae7b25373521"></a>

### [`00bb859c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb859c.md) → [`00bb8638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8638.md) FUN_00bb8638

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bb8388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8388.md) · 呼出先 4件 [`00b402c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b402c0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`00bb8424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8424.md) · 呼出先 4件 [`00b4035c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b4035c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 60.00% / 新版 54.55%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00bb8638",
      "incomplete_value": true,
      "site": "00bb8640",
      "value": [
        "INT_LEFT",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "leaf",
            "const:3:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb86d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bb8774"
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
      "00bb86cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bb86d0"
      ]
    ],
    [
      "unmatched:00bb86d4",
      "PARAM",
      [
        "storage",
        "002a867b",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bb86d8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00b4035c"
      ]
    ]
  ],
  "added": [
    [
      "00bb86cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb876c"
      ]
    ],
    [
      "00bb8770",
      "PARAM",
      [
        "storage",
        "002a861f",
        null,
        "string"
      ]
    ],
    [
      "00bb8774",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00b4035c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb8630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb859c.md#insn-00bb8630) · [`00bb8640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb859c.md#insn-00bb8640) · [`00bb86cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb859c.md#insn-00bb86cc)
- 新版 [`00bb86cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8638.md#insn-00bb86cc) · [`00bb86dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8638.md#insn-00bb86dc)

~~~diff
- 00bb8630 ["INT_NOTEQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00bb8630 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
+ 00bb86cc ["INT_NOTEQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
+ 00bb86cc ["CBRANCH", null, ["local:b16:8", "tmp:0:1"]]
- 00bb8630 bytes 090500b5
+ 00bb86cc bytes 090500b5
- 00bb8640 ["INT_ADD", "register:40f0:8", ["const:bb8640:8", "const:4:8"]]
- 00bb8640 ["CALL", null, ["callee:00c57f60:8"]]
+ 00bb86dc ["INT_ADD", "register:40f0:8", ["const:bb86dc:8", "const:4:8"]]
+ 00bb86dc ["CALL", null, ["callee:00c57f60:8"]]
- 00bb8640 bytes 147e0294
+ 00bb86dc bytes 217e0294
- 00bb86cc ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bb86cc ["RETURN", null, ["register:0:8"]]
- 00bb86cc bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d83b6b755afe991b018697c10dd0efa"></a>

### [`00bb86dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb86dc.md) → [`00bb8778`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8778.md) _ZNSt6__ndk114__split_bufferIPN8firebase9messaging7MessageENS_9allocatorIS4_EEE9push_backEOS4_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d480.md) · 呼出先 4件 [`00b402c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b402c0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`00c5d550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d550.md) · 呼出先 4件 [`00b4035c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b4035c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.50% / 新版 97.50%

CFGの説明率　旧版 63.64% / 新版 70.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb88b0",
      "incomplete_value": false,
      "site": "00bb88b4",
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
            "const:61f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb8814",
      "incomplete_value": false,
      "site": "00bb8818",
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
            "const:67b:8"
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
      "00bb88b0",
      "PARAM",
      [
        "storage",
        "002a867b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bb88b0",
      "PARAM",
      [
        "storage",
        "002a861f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb8818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb86dc.md#insn-00bb8818) · [`00bb86f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb86dc.md#insn-00bb86f0) · [`00bb8704`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb86dc.md#insn-00bb8704)
- 新版 [`00bb88b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8778.md#insn-00bb88b4) · [`00bb87a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8778.md#insn-00bb87a0)

~~~diff
- 00bb8818 ["INT_ADD", "register:40f0:8", ["const:bb8818:8", "const:4:8"]]
- 00bb8818 ["CALL", null, ["callee:00b4035c:8"]]
+ 00bb88b4 ["INT_ADD", "register:40f0:8", ["const:bb88b4:8", "const:4:8"]]
+ 00bb88b4 ["CALL", null, ["callee:00b4035c:8"]]
- 00bb8818 bytes aa1efe97
+ 00bb88b4 bytes aa1efe97
- 00bb86f0 ["COPY", "tmp:0:8", ["const:40:8"]]
- 00bb86f0 ["INT_CARRY", "register:105:1", ["register:8:8", "tmp:0:8"]]
- 00bb86f0 ["INT_SCARRY", "register:106:1", ["register:8:8", "tmp:0:8"]]
- 00bb86f0 ["INT_ADD", "tmp:1:8", ["register:8:8", "tmp:0:8"]]
- 00bb86f0 bytes fd030191
- 00bb8704 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bb8704 ["CBRANCH", null, ["local:b15:8", "tmp:0:1"]]
+ 00bb87a0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00bb87a0 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 00bb8704 bytes 01070054
+ 00bb87a0 bytes 01070054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a637e341c8558eb14c9e3631b60239d6"></a>

### [`00bb881c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb881c.md) → [`00bb88b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb88b8.md) _ZNSt6__ndk114__split_bufferIPN8firebase9messaging7MessageENS_9allocatorIS4_EEE10push_frontEOS4_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d470.md) · 呼出先 4件 [`00b402c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b402c0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`00c5d540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d540.md) · 呼出先 4件 [`00b4035c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b4035c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 91.25% / 新版 91.25%

CFGの説明率　旧版 59.09% / 新版 56.52%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb887c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb88a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bb8918"
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
      "unmatched:00bb887c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb892c"
      ]
    ],
    [
      "unmatched:00bb8954",
      "PARAM",
      [
        "storage",
        "002a867b",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bb8958",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00b4035c"
      ]
    ]
  ],
  "added": [
    [
      "00bb8918",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb892c"
      ]
    ],
    [
      "00bb89f0",
      "PARAM",
      [
        "storage",
        "002a861f",
        null,
        "string"
      ]
    ],
    [
      "00bb89f4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00b4035c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb887c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb881c.md#insn-00bb887c) · [`00bb88a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb881c.md#insn-00bb88a8) · [`00bb88c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb881c.md#insn-00bb88c4)
- 新版 [`00bb8960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb88b8.md#insn-00bb8960)

~~~diff
- 00bb887c ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
- 00bb887c bytes a0000054
- 00bb88a8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bb88a8 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00bb88a8 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00bb88a8 ["INT_ADD", "tmp:1:8", ["const:0:8", "const:1:8"]]
- 00bb88a8 bytes 08159f9a
- 00bb88c4 ["INT_ADD", "register:40f0:8", ["const:bb88c4:8", "const:4:8"]]
- 00bb88c4 ["CALL", null, ["callee:00c57f60:8"]]
+ 00bb8960 ["INT_ADD", "register:40f0:8", ["const:bb8960:8", "const:4:8"]]
+ 00bb8960 ["CALL", null, ["callee:00c57f60:8"]]
- 00bb88c4 bytes 737d0294
+ 00bb8960 bytes 807d0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f3ca8e32d6d2a1285d2644cbd702a6e"></a>

### [`00bb895c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb895c.md) → [`00bb89f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb89f8.md) _ZNSt6__ndk114__split_bufferIPN8firebase9messaging7MessageERNS_9allocatorIS4_EEE9push_backEOS4_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d4a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d4a0.md) · 呼出先 4件 [`00b402c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b402c0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`00c5d570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d570.md) · 呼出先 4件 [`00b4035c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b4035c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 17.39% / 新版 18.18%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb8a30"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bb8acc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb8984"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb8984",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb8b00"
      ]
    ],
    [
      "unmatched:00bb8a94",
      "PARAM",
      [
        "storage",
        "002a867b",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bb8a98",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00b4035c"
      ]
    ]
  ],
  "added": [
    [
      "00bb8a20",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb8b00"
      ]
    ],
    [
      "00bb8b30",
      "PARAM",
      [
        "storage",
        "002a861f",
        null,
        "string"
      ]
    ],
    [
      "00bb8b34",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00b4035c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb8984`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb895c.md#insn-00bb8984) · [`00bb89a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb895c.md#insn-00bb89a4) · [`00bb8a00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb895c.md#insn-00bb8a00)
- 新版 [`00bb8a9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb89f8.md#insn-00bb8a9c)

~~~diff
- 00bb8984 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bb8984 ["CBRANCH", null, ["local:b16:8", "tmp:0:1"]]
- 00bb8984 bytes 01070054
- 00bb89a4 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00bb89a4 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00bb89a4 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00bb89a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:1:8"]]
- 00bb89a4 bytes 48b5889a
- 00bb8a00 ["INT_ADD", "register:40f0:8", ["const:bb8a00:8", "const:4:8"]]
- 00bb8a00 ["CALL", null, ["callee:00c57f60:8"]]
+ 00bb8a9c ["INT_ADD", "register:40f0:8", ["const:bb8a9c:8", "const:4:8"]]
+ 00bb8a9c ["CALL", null, ["callee:00c57f60:8"]]
- 00bb8a00 bytes 247d0294
+ 00bb8a9c bytes 317d0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aaa36d333d13e38f6d05fecf71b7ba0a"></a>

### [`00bb8a9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8a9c.md) → [`00bb8b38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8b38.md) _ZNSt6__ndk114__split_bufferIPN8firebase9messaging7MessageERNS_9allocatorIS4_EEE10push_frontERKS4_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d490.md) · 呼出先 4件 [`00b402c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b402c0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`00c5d560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d560.md) · 呼出先 4件 [`00b4035c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b4035c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 91.25% / 新版 91.25%

CFGの説明率　旧版 59.09% / 新版 56.52%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb8b74"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb8bb8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bb8c10"
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
      "unmatched:00bb8b80",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb8c08"
      ]
    ],
    [
      "00bb8c70",
      "PARAM",
      [
        "storage",
        "002a867b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bb8c1c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb8c08"
      ]
    ],
    [
      "00bb8c70",
      "PARAM",
      [
        "storage",
        "002a861f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb8b74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8a9c.md#insn-00bb8b74) · [`00bb8b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8a9c.md#insn-00bb8b80) · [`00bb8ba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8a9c.md#insn-00bb8ba0)
- 新版 [`00bb8c3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8b38.md#insn-00bb8c3c)

~~~diff
- 00bb8b74 ["COPY", "tmp:0:8", ["register:4060:8"]]
- 00bb8b74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4068:8"]]
- 00bb8b74 bytes 8d0100f9
- 00bb8b80 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bb8b80 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00bb8b80 bytes 61ffff54
- 00bb8ba0 ["INT_ADD", "register:40f0:8", ["const:bb8ba0:8", "const:4:8"]]
- 00bb8ba0 ["CALL", null, ["callee:00c57f80:8"]]
+ 00bb8c3c ["INT_ADD", "register:40f0:8", ["const:bb8c3c:8", "const:4:8"]]
+ 00bb8c3c ["CALL", null, ["callee:00c57f80:8"]]
- 00bb8ba0 bytes c47c0294
+ 00bb8c3c bytes d17c0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29ab9791eb62cdde3f71d2ca6f5cc460"></a>

### [`00bb8bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8bdc.md) → [`00bb8c78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8c78.md) _INIT_285

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00b65510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65510.md) [`00bb66a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb66a4.md) [`00bb66e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb66e4.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c5abc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abc0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00b655ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b655ac.md) [`00bb6740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6740.md) [`00bb6780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6780.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c5ac90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ac90.md)

変更の種類 call, call_argument_candidate, call_count, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb8be0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb8be0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb8c08"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb8be0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb8bf8",
      "PARAM",
      [
        "storage",
        "011261e8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bb8c08",
      "WRITE",
      [
        "storage",
        "011261e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bb8c7c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bb8c94",
      "PARAM",
      [
        "storage",
        "011262e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb8ca4",
      "WRITE",
      [
        "storage",
        "011262e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb8be0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8bdc.md#insn-00bb8be0) · [`00bb8c08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8bdc.md#insn-00bb8c08) · [`00bb8c0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8bdc.md#insn-00bb8c0c)

~~~diff
- 00bb8be0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bb8be0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bb8be0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bb8be0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb8be0 bytes fd7b01a9
- 00bb8c08 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bb8c08 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00bb8c08 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00bb8c08 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb8c08 bytes 082400a9
- 00bb8c0c ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:10:8"]]
- 00bb8c0c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 00bb8c0c bytes 0a0800f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-876527e358b4a8b9f20543d452496d16"></a>

### [`00bb8c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8c60.md) → [`00bb8cfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8cfc.md) _ZN8firebase9messaging18firebase_messaging19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9alloc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 31.25% / 新版 31.25%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb8c60"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb8c64"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb8c64"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb8c60",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb8c64",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bb8d0c",
      "READ",
      [
        "storage",
        "011262a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bb8cfc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bb8d00",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bb8d0c",
      "READ",
      [
        "storage",
        "011263a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb8c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8c60.md#insn-00bb8c60) · [`00bb8c64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8c60.md#insn-00bb8c64) · [`00bb8c74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8c60.md#insn-00bb8c74)
- 新版 [`00bb8d10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8cfc.md#insn-00bb8d10)

~~~diff
- 00bb8c60 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bb8c60 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bb8c60 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bb8c60 bytes f30f1ef8
- 00bb8c64 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bb8c64 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bb8c64 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bb8c64 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb8c64 bytes fd7b01a9
- 00bb8c74 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bb8c74 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bb8d10 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bb8d10 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bb8c74 bytes e80000b5
+ 00bb8d10 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-22d3408b8478fecf23d7e4b21c7cf060"></a>

### [`00bb8ca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8ca0.md) → [`00bb8d3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8d3c.md) _ZN8firebase9messaging18firebase_messaging19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9alloc

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
      "definition_site": "00bb8d68",
      "incomplete_value": true,
      "site": "00bb8d68",
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
            "const:3a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb8ccc",
      "incomplete_value": true,
      "site": "00bb8ccc",
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
            "const:2a8:8"
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
      "definition_site": "00bb8d50",
      "incomplete_value": true,
      "site": "00bb8d50",
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
      "definition_site": "00bb8cb4",
      "incomplete_value": true,
      "site": "00bb8cb4",
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
      "definition_site": "00bb8d58",
      "incomplete_value": false,
      "site": "00bb8d60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ba000:8"
          ],
          [
            "leaf",
            "const:e4a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb8cbc",
      "incomplete_value": false,
      "site": "00bb8cc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ba000:8"
          ],
          [
            "leaf",
            "const:e9e:8"
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
      "00bb8d4c",
      "READ",
      [
        "storage",
        "011262a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb8d58",
      "PARAM",
      [
        "storage",
        "002bae9e",
        null,
        "string"
      ]
    ],
    [
      "00bb8d68",
      "WRITE",
      [
        "storage",
        "011262a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bb8d4c",
      "READ",
      [
        "storage",
        "011263a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb8d58",
      "PARAM",
      [
        "storage",
        "002bae4a",
        null,
        "string"
      ]
    ],
    [
      "00bb8d68",
      "WRITE",
      [
        "storage",
        "011263a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb8cc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8ca0.md#insn-00bb8cc4) · [`00bb8ccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8ca0.md#insn-00bb8ccc) · [`00bb8cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8ca0.md#insn-00bb8cb0)
- 新版 [`00bb8d60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8d3c.md#insn-00bb8d60) · [`00bb8d68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8d3c.md#insn-00bb8d68) · [`00bb8d4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8d3c.md#insn-00bb8d4c)

~~~diff
- 00bb8cc4 ["INT_ADD", "register:40f0:8", ["const:bb8cc4:8", "const:4:8"]]
- 00bb8cc4 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bb8d60 ["INT_ADD", "register:40f0:8", ["const:bb8d60:8", "const:4:8"]]
+ 00bb8d60 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bb8cc4 bytes 93880294
+ 00bb8d60 bytes a0880294
- 00bb8ccc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2a8:8"]]
- 00bb8ccc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bb8d68 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3a8:8"]]
+ 00bb8d68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb8ccc bytes 605601f9
+ 00bb8d68 bytes 60d601f9
- 00bb8cb0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2a8:8"]]
- 00bb8cb0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb8d4c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3a8:8"]]
+ 00bb8d4c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb8cb0 bytes 685641f9
+ 00bb8d4c bytes 68d641f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4593a6f78f56ad26a6d643800151d94f"></a>

### [`00bb8ce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8ce0.md) → [`00bb8d7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8d7c.md) _ZN8firebase9messaging18firebase_messaging10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bb8dac",
      "incomplete_value": true,
      "site": "00bb8dac",
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
            "const:3a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb8d10",
      "incomplete_value": true,
      "site": "00bb8d10",
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
            "const:2a8:8"
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
      "definition_site": "00bb8d90",
      "incomplete_value": true,
      "site": "00bb8d90",
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
      "definition_site": "00bb8cf4",
      "incomplete_value": true,
      "site": "00bb8cf4",
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
      "definition_site": "00bb8d9c",
      "incomplete_value": false,
      "site": "00bb8da4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ba000:8"
          ],
          [
            "leaf",
            "const:e4a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb8d00",
      "incomplete_value": false,
      "site": "00bb8d08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ba000:8"
          ],
          [
            "leaf",
            "const:e9e:8"
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
      "00bb8d8c",
      "READ",
      [
        "storage",
        "011262a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb8d9c",
      "PARAM",
      [
        "storage",
        "002bae9e",
        null,
        "string"
      ]
    ],
    [
      "00bb8dac",
      "WRITE",
      [
        "storage",
        "011262a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bb8d8c",
      "READ",
      [
        "storage",
        "011263a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb8d9c",
      "PARAM",
      [
        "storage",
        "002bae4a",
        null,
        "string"
      ]
    ],
    [
      "00bb8dac",
      "WRITE",
      [
        "storage",
        "011263a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb8d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8ce0.md#insn-00bb8d08) · [`00bb8d10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8ce0.md#insn-00bb8d10) · [`00bb8cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8ce0.md#insn-00bb8cf0)
- 新版 [`00bb8da4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8d7c.md#insn-00bb8da4) · [`00bb8dac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8d7c.md#insn-00bb8dac) · [`00bb8d8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8d7c.md#insn-00bb8d8c)

~~~diff
- 00bb8d08 ["INT_ADD", "register:40f0:8", ["const:bb8d08:8", "const:4:8"]]
- 00bb8d08 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bb8da4 ["INT_ADD", "register:40f0:8", ["const:bb8da4:8", "const:4:8"]]
+ 00bb8da4 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bb8d08 bytes 82880294
+ 00bb8da4 bytes 8f880294
- 00bb8d10 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2a8:8"]]
- 00bb8d10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bb8dac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3a8:8"]]
+ 00bb8dac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb8d10 bytes 605601f9
+ 00bb8dac bytes 60d601f9
- 00bb8cf0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2a8:8"]]
- 00bb8cf0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb8d8c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3a8:8"]]
+ 00bb8d8c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb8cf0 bytes 685641f9
+ 00bb8d8c bytes 68d641f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-276a7fbf434ff3ffbf94c0f774a0f505"></a>

### [`00bb8d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8d24.md) → [`00bb8dc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8dc0.md) _ZN8firebase9messaging18firebase_messaging10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00bb8df0",
      "incomplete_value": true,
      "site": "00bb8df0",
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
            "const:3a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb8d54",
      "incomplete_value": true,
      "site": "00bb8d54",
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
            "const:2a8:8"
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
      "definition_site": "00bb8dd4",
      "incomplete_value": true,
      "site": "00bb8dd4",
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
      "definition_site": "00bb8d38",
      "incomplete_value": true,
      "site": "00bb8d38",
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
      "definition_site": "00bb8ddc",
      "incomplete_value": false,
      "site": "00bb8de8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ba000:8"
          ],
          [
            "leaf",
            "const:e4a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb8d40",
      "incomplete_value": false,
      "site": "00bb8d4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ba000:8"
          ],
          [
            "leaf",
            "const:e9e:8"
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
      "00bb8dd0",
      "READ",
      [
        "storage",
        "011262a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb8ddc",
      "PARAM",
      [
        "storage",
        "002bae9e",
        null,
        "string"
      ]
    ],
    [
      "00bb8df0",
      "WRITE",
      [
        "storage",
        "011262a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bb8dd0",
      "READ",
      [
        "storage",
        "011263a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb8ddc",
      "PARAM",
      [
        "storage",
        "002bae4a",
        null,
        "string"
      ]
    ],
    [
      "00bb8df0",
      "WRITE",
      [
        "storage",
        "011263a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb8d4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8d24.md#insn-00bb8d4c) · [`00bb8d54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8d24.md#insn-00bb8d54) · [`00bb8d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8d24.md#insn-00bb8d34)
- 新版 [`00bb8de8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8dc0.md#insn-00bb8de8) · [`00bb8df0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8dc0.md#insn-00bb8df0) · [`00bb8dd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8dc0.md#insn-00bb8dd0)

~~~diff
- 00bb8d4c ["INT_ADD", "register:40f0:8", ["const:bb8d4c:8", "const:4:8"]]
- 00bb8d4c ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bb8de8 ["INT_ADD", "register:40f0:8", ["const:bb8de8:8", "const:4:8"]]
+ 00bb8de8 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bb8d4c bytes 71880294
+ 00bb8de8 bytes 7e880294
- 00bb8d54 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2a8:8"]]
- 00bb8d54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bb8df0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3a8:8"]]
+ 00bb8df0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb8d54 bytes 605601f9
+ 00bb8df0 bytes 60d601f9
- 00bb8d34 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2a8:8"]]
- 00bb8d34 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb8dd0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3a8:8"]]
+ 00bb8dd0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb8d34 bytes 685641f9
+ 00bb8dd0 bytes 68d641f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a23b7d4b1b2c40aeb4ac702968b644f"></a>

### [`00bb8de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8de0.md) → [`00bb8e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8e7c.md) _ZN8firebase9messaging18firebase_messaging12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 33.33% / 新版 28.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件, `unresolved_store_alignment` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb8e1c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb8e3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bb8eb8"
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
      "00bb8e90",
      "READ",
      [
        "storage",
        "011262a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb8e9c",
      "READ",
      [
        "storage",
        "011262b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb8ea4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bb8e20"
      ]
    ]
  ],
  "added": [
    [
      "00bb8e90",
      "READ",
      [
        "storage",
        "011263a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb8e9c",
      "READ",
      [
        "storage",
        "011263b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb8ea4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb8ebc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb8df8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8de0.md#insn-00bb8df8) · [`00bb8e1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8de0.md#insn-00bb8e1c) · [`00bb8e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8de0.md#insn-00bb8e24)
- 新版 [`00bb8e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8e7c.md#insn-00bb8e94)

~~~diff
- 00bb8df8 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bb8df8 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bb8e94 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00bb8e94 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00bb8df8 bytes 410200b4
+ 00bb8e94 bytes 410200b4
- 00bb8e1c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bb8e1c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bb8e1c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:2b0:8"]]
- 00bb8e1c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bb8e1c bytes bfc20a39
- 00bb8e24 ["INT_ADD", "register:40f0:8", ["const:bb8e24:8", "const:4:8"]]
- 00bb8e24 ["CALL", null, ["callee:00c5b030:8"]]
- 00bb8e24 bytes 4f880294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d35b0fbeade6f4c662a71aee1c4e3abc"></a>

### [`00bb8e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8e50.md) → [`00bb8eec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8eec.md) _ZN8firebase9messaging18firebase_messaging14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00bb8e90"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bb8f2c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb8e6c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb8e64",
      "READ",
      [
        "storage",
        "011262a8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bb8e6c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb8f30"
      ]
    ],
    [
      "unmatched:00bb8e74",
      "PARAM",
      [
        "storage",
        "002bae9e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bb8f00",
      "READ",
      [
        "storage",
        "011263a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb8f08",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb8f30"
      ]
    ],
    [
      "00bb8f10",
      "PARAM",
      [
        "storage",
        "002bae4a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb8e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8e50.md#insn-00bb8e6c) · [`00bb8e88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8e50.md#insn-00bb8e88) · [`00bb8e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8e50.md#insn-00bb8e90)
- 新版 [`00bb8f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8eec.md#insn-00bb8f24)

~~~diff
- 00bb8e6c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bb8e6c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bb8e6c bytes 410100b5
- 00bb8e88 ["INT_ADD", "register:40f0:8", ["const:bb8e88:8", "const:4:8"]]
- 00bb8e88 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bb8f24 ["INT_ADD", "register:40f0:8", ["const:bb8f24:8", "const:4:8"]]
+ 00bb8f24 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bb8e88 bytes 22880294
+ 00bb8f24 bytes 2f880294
- 00bb8e90 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2a8:8"]]
- 00bb8e90 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb8e90 bytes 805601f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84e36d5c7e91e7a0961e3c9b1f371bdb"></a>

### [`00bb8ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8ec0.md) → [`00bb8f5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8f5c.md) _ZN8firebase9messaging18firebase_messaging11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bb8f78",
      "incomplete_value": false,
      "site": "00bb8f7c",
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
      "definition_site": "00bb8edc",
      "incomplete_value": false,
      "site": "00bb8ee0",
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
      "definition_site": "00bb8f88",
      "incomplete_value": true,
      "site": "00bb8f94",
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
      "definition_site": "00bb8eec",
      "incomplete_value": true,
      "site": "00bb8ef8",
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
      "00bb8f78",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bb8f88",
      "DATA",
      [
        "storage",
        "011262b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bb8f78",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00bb8f88",
      "DATA",
      [
        "storage",
        "011263b8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb8ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8ec0.md#insn-00bb8ee0) · [`00bb8edc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8ec0.md#insn-00bb8edc) · [`00bb8ee8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8ec0.md#insn-00bb8ee8)
- 新版 [`00bb8f7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8f5c.md#insn-00bb8f7c) · [`00bb8f78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8f5c.md#insn-00bb8f78) · [`00bb8f84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8f5c.md#insn-00bb8f84)

~~~diff
- 00bb8ee0 ["INT_ADD", "register:40f0:8", ["const:bb8ee0:8", "const:4:8"]]
- 00bb8ee0 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bb8f7c ["INT_ADD", "register:40f0:8", ["const:bb8f7c:8", "const:4:8"]]
+ 00bb8f7c ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bb8ee0 bytes 48880294
+ 00bb8f7c bytes 55880294
- 00bb8edc ["COPY", "tmp:0:8", ["const:367:8"]]
- 00bb8edc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bb8edc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bb8edc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bb8f78 ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00bb8f78 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bb8f78 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bb8f78 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bb8edc bytes 009c0d91
+ 00bb8f78 bytes 002c0c91
- 00bb8ee8 ["COPY", "tmp:0:8", ["const:2b8:8"]]
- 00bb8ee8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bb8ee8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bb8ee8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bb8f84 ["COPY", "tmp:0:8", ["const:3b8:8"]]
+ 00bb8f84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bb8f84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bb8f84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bb8ee8 bytes 08e10a91
+ 00bb8f84 bytes 08e10e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8386f65ae9f3d0f5981c3a4488dace8b"></a>

### [`00bb8efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8efc.md) → [`00bb8f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8f98.md) _ZN8firebase9messaging18firebase_messaging13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb8efc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb8efc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb8f00"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb8efc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb8f00",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb8f10",
      "READ",
      [
        "storage",
        "011262a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bb8f98",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bb8f9c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bb8fac",
      "READ",
      [
        "storage",
        "011263a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb8efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8efc.md#insn-00bb8efc) · [`00bb8f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8efc.md#insn-00bb8f00) · [`00bb8f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8efc.md#insn-00bb8f18)

~~~diff
- 00bb8efc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bb8efc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bb8efc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bb8efc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bb8efc bytes f44fbea9
- 00bb8f00 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bb8f00 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bb8f00 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bb8f00 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb8f00 bytes fd7b01a9
- 00bb8f18 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bb8f18 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bb8f18 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5dde4498361df2eb8e8b464d215cde5a"></a>

### [`00bb8fa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8fa8.md) → [`00bb9044`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9044.md) _ZN8firebase9messaging27registration_intent_service19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileEN

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
      "definition_site": "00bb9070",
      "incomplete_value": true,
      "site": "00bb9070",
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
            "const:418:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb8fd4",
      "incomplete_value": true,
      "site": "00bb8fd4",
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
            "const:318:8"
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
      "definition_site": "00bb9058",
      "incomplete_value": true,
      "site": "00bb9058",
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
      "definition_site": "00bb8fbc",
      "incomplete_value": true,
      "site": "00bb8fbc",
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
      "definition_site": "00bb9064",
      "incomplete_value": false,
      "site": "00bb9068",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:b23:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb8fc8",
      "incomplete_value": false,
      "site": "00bb8fcc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:b77:8"
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
      "00bb9054",
      "READ",
      [
        "storage",
        "01126318",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9064",
      "PARAM",
      [
        "storage",
        "002b9b77",
        null,
        "string"
      ]
    ],
    [
      "00bb9070",
      "WRITE",
      [
        "storage",
        "01126318",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bb9054",
      "READ",
      [
        "storage",
        "01126418",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9064",
      "PARAM",
      [
        "storage",
        "002b9b23",
        null,
        "string"
      ]
    ],
    [
      "00bb9070",
      "WRITE",
      [
        "storage",
        "01126418",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb8fcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8fa8.md#insn-00bb8fcc) · [`00bb8fd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8fa8.md#insn-00bb8fd4) · [`00bb8fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8fa8.md#insn-00bb8fb8)
- 新版 [`00bb9068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9044.md#insn-00bb9068) · [`00bb9070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9044.md#insn-00bb9070) · [`00bb9054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9044.md#insn-00bb9054)

~~~diff
- 00bb8fcc ["INT_ADD", "register:40f0:8", ["const:bb8fcc:8", "const:4:8"]]
- 00bb8fcc ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bb9068 ["INT_ADD", "register:40f0:8", ["const:bb9068:8", "const:4:8"]]
+ 00bb9068 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bb8fcc bytes d1870294
+ 00bb9068 bytes de870294
- 00bb8fd4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:318:8"]]
- 00bb8fd4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bb9070 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:418:8"]]
+ 00bb9070 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb8fd4 bytes 608e01f9
+ 00bb9070 bytes 600e02f9
- 00bb8fb8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:318:8"]]
- 00bb8fb8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb9054 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:418:8"]]
+ 00bb9054 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb8fb8 bytes 688e41f9
+ 00bb9054 bytes 680e42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc61a2d2ab36f6b7367547d1e5a4873b"></a>

### [`00bb8fe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8fe8.md) → [`00bb9084`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9084.md) _ZN8firebase9messaging27registration_intent_service19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileEN

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
      "definition_site": "00bb90b0",
      "incomplete_value": true,
      "site": "00bb90b0",
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
            "const:418:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb9014",
      "incomplete_value": true,
      "site": "00bb9014",
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
            "const:318:8"
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
      "definition_site": "00bb9098",
      "incomplete_value": true,
      "site": "00bb9098",
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
      "definition_site": "00bb8ffc",
      "incomplete_value": true,
      "site": "00bb8ffc",
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
      "definition_site": "00bb90a0",
      "incomplete_value": false,
      "site": "00bb90a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:b23:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb9004",
      "incomplete_value": false,
      "site": "00bb900c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:b77:8"
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
      "00bb9094",
      "READ",
      [
        "storage",
        "01126318",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb90a0",
      "PARAM",
      [
        "storage",
        "002b9b77",
        null,
        "string"
      ]
    ],
    [
      "00bb90b0",
      "WRITE",
      [
        "storage",
        "01126318",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bb9094",
      "READ",
      [
        "storage",
        "01126418",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb90a0",
      "PARAM",
      [
        "storage",
        "002b9b23",
        null,
        "string"
      ]
    ],
    [
      "00bb90b0",
      "WRITE",
      [
        "storage",
        "01126418",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb900c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8fe8.md#insn-00bb900c) · [`00bb9014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8fe8.md#insn-00bb9014) · [`00bb8ff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8fe8.md#insn-00bb8ff8)
- 新版 [`00bb90a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9084.md#insn-00bb90a8) · [`00bb90b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9084.md#insn-00bb90b0) · [`00bb9094`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9084.md#insn-00bb9094)

~~~diff
- 00bb900c ["INT_ADD", "register:40f0:8", ["const:bb900c:8", "const:4:8"]]
- 00bb900c ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bb90a8 ["INT_ADD", "register:40f0:8", ["const:bb90a8:8", "const:4:8"]]
+ 00bb90a8 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bb900c bytes c1870294
+ 00bb90a8 bytes ce870294
- 00bb9014 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:318:8"]]
- 00bb9014 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bb90b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:418:8"]]
+ 00bb90b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb9014 bytes 608e01f9
+ 00bb90b0 bytes 600e02f9
- 00bb8ff8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:318:8"]]
- 00bb8ff8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb9094 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:418:8"]]
+ 00bb9094 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb8ff8 bytes 688e41f9
+ 00bb9094 bytes 680e42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-935299b9a37ac48658f6daa360538441"></a>

### [`00bb9028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9028.md) → [`00bb90c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb90c4.md) _ZN8firebase9messaging27registration_intent_service10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "site": "00bb9028"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb902c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb902c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb9028",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb902c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bb90d4",
      "READ",
      [
        "storage",
        "01126318",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bb90c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bb90c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bb90d4",
      "READ",
      [
        "storage",
        "01126418",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb9028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9028.md#insn-00bb9028) · [`00bb902c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9028.md#insn-00bb902c) · [`00bb903c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9028.md#insn-00bb903c)
- 新版 [`00bb90d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb90c4.md#insn-00bb90d8)

~~~diff
- 00bb9028 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bb9028 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bb9028 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bb9028 bytes f30f1ef8
- 00bb902c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bb902c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bb902c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bb902c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb902c bytes fd7b01a9
- 00bb903c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bb903c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bb90d8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bb90d8 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00bb903c bytes 080100b5
+ 00bb90d8 bytes 080100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28f8083d96c62a56f8f914ae2bc026c5"></a>

### [`00bb906c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb906c.md) → [`00bb9108`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9108.md) _ZN8firebase9messaging27registration_intent_service10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 23.53% / 新版 23.53%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb906c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb9070"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb9070"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb906c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb9070",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb907c",
      "READ",
      [
        "storage",
        "01126318",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bb9108",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bb910c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bb9118",
      "READ",
      [
        "storage",
        "01126418",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb906c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb906c.md#insn-00bb906c) · [`00bb9070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb906c.md#insn-00bb9070) · [`00bb9080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb906c.md#insn-00bb9080)

~~~diff
- 00bb906c ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bb906c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bb906c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bb906c bytes f30f1ef8
- 00bb9070 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bb9070 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bb9070 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bb9070 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb9070 bytes fd7b01a9
- 00bb9080 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bb9080 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00bb9080 bytes 080100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f08d887c97b18988ed7fbf83beb90bd0"></a>

### [`00bb90bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb90bc.md) → [`00bb9158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9158.md) _ZN8firebase9messaging27registration_intent_service15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 59.26% / 新版 59.26%

CFGの説明率　旧版 16.67% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb90bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb90c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb90c0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb90bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb90c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb90c4",
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
      "00bb9158",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bb915c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bb9160",
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

- 旧版 [`00bb90bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb90bc.md#insn-00bb90bc) · [`00bb90c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb90bc.md#insn-00bb90c0) · [`00bb90c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb90bc.md#insn-00bb90c4)

~~~diff
- 00bb90bc ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00bb90bc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bb90bc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bb90bc bytes f50f1df8
- 00bb90c0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bb90c0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bb90c0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bb90c0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb90c0 bytes f44f01a9
- 00bb90c4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bb90c4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bb90c4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bb90c4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb90c4 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4685330377202950d20c8f443d986ced"></a>

### [`00bb9128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9128.md) → [`00bb91c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb91c4.md) _ZN8firebase9messaging27registration_intent_service12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

変更の種類 branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 53.57% / 新版 53.57%

CFGの説明率　旧版 16.67% / 新版 14.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb9164"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb9184"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bb9200"
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
      "00bb91d8",
      "READ",
      [
        "storage",
        "01126318",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb91dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bb9188"
      ]
    ],
    [
      "00bb91e4",
      "READ",
      [
        "storage",
        "01126320",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bb91d8",
      "READ",
      [
        "storage",
        "01126418",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb91dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb9224"
      ]
    ],
    [
      "00bb91e4",
      "READ",
      [
        "storage",
        "01126420",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb9164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9128.md#insn-00bb9164) · [`00bb916c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9128.md#insn-00bb916c) · [`00bb9180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9128.md#insn-00bb9180)

~~~diff
- 00bb9164 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bb9164 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bb9164 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:320:8"]]
- 00bb9164 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bb9164 bytes bf820c39
- 00bb916c ["INT_ADD", "register:40f0:8", ["const:bb916c:8", "const:4:8"]]
- 00bb916c ["CALL", null, ["callee:00c5b030:8"]]
- 00bb916c bytes 7d870294
- 00bb9180 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bb9180 ["INT_ADD", "register:40f0:8", ["const:bb9180:8", "const:4:8"]]
- 00bb9180 ["CALLIND", null, ["register:0:8"]]
- 00bb9180 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bce1b115e5dc5d23e05a31fc90bf22b2"></a>

### [`00bb9198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9198.md) → [`00bb9234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9234.md) _ZN8firebase9messaging27registration_intent_service14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00bb91d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bb9274"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb91b4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb91ac",
      "READ",
      [
        "storage",
        "01126318",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bb91b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb9278"
      ]
    ],
    [
      "unmatched:00bb91bc",
      "PARAM",
      [
        "storage",
        "002b9b77",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bb9248",
      "READ",
      [
        "storage",
        "01126418",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9250",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb9278"
      ]
    ],
    [
      "00bb9258",
      "PARAM",
      [
        "storage",
        "002b9b23",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb91b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9198.md#insn-00bb91b4) · [`00bb91d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9198.md#insn-00bb91d0) · [`00bb91d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9198.md#insn-00bb91d8)
- 新版 [`00bb926c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9234.md#insn-00bb926c)

~~~diff
- 00bb91b4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bb91b4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bb91b4 bytes 410100b5
- 00bb91d0 ["INT_ADD", "register:40f0:8", ["const:bb91d0:8", "const:4:8"]]
- 00bb91d0 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bb926c ["INT_ADD", "register:40f0:8", ["const:bb926c:8", "const:4:8"]]
+ 00bb926c ["CALL", null, ["callee:00c5afe0:8"]]
- 00bb91d0 bytes 50870294
+ 00bb926c bytes 5d870294
- 00bb91d8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:318:8"]]
- 00bb91d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb91d8 bytes 808e01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-008e9ef262402db3737a04cf999ab7e0"></a>

### [`00bb9244`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9244.md) → [`00bb92e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb92e0.md) _ZN8firebase9messaging27registration_intent_service13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "site": "00bb9284"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bb9320"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb9260"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb9258",
      "READ",
      [
        "storage",
        "01126318",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bb9260",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb9324"
      ]
    ],
    [
      "unmatched:00bb9268",
      "PARAM",
      [
        "storage",
        "002b9b77",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bb92f4",
      "READ",
      [
        "storage",
        "01126418",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb92fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb9324"
      ]
    ],
    [
      "00bb9304",
      "PARAM",
      [
        "storage",
        "002b9b23",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb9260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9244.md#insn-00bb9260) · [`00bb927c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9244.md#insn-00bb927c) · [`00bb9284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9244.md#insn-00bb9284)
- 新版 [`00bb9318`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb92e0.md#insn-00bb9318)

~~~diff
- 00bb9260 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bb9260 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bb9260 bytes 410100b5
- 00bb927c ["INT_ADD", "register:40f0:8", ["const:bb927c:8", "const:4:8"]]
- 00bb927c ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bb9318 ["INT_ADD", "register:40f0:8", ["const:bb9318:8", "const:4:8"]]
+ 00bb9318 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bb927c bytes 25870294
+ 00bb9318 bytes 32870294
- 00bb9284 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:318:8"]]
- 00bb9284 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb9284 bytes 808e01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4bc7fa69642ad86703694610b228b701"></a>

### [`00bb92b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb92b4.md) → [`00bb9350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9350.md) _ZN8firebase9messaging27registration_intent_service10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bb936c",
      "incomplete_value": false,
      "site": "00bb9370",
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
      "definition_site": "00bb92d0",
      "incomplete_value": false,
      "site": "00bb92d4",
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
      "definition_site": "00bb937c",
      "incomplete_value": true,
      "site": "00bb9388",
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
      "definition_site": "00bb92e0",
      "incomplete_value": true,
      "site": "00bb92ec",
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
      "00bb936c",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bb937c",
      "DATA",
      [
        "storage",
        "01126330",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bb936c",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00bb937c",
      "DATA",
      [
        "storage",
        "01126430",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb92d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb92b4.md#insn-00bb92d4) · [`00bb92d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb92b4.md#insn-00bb92d0) · [`00bb92dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb92b4.md#insn-00bb92dc)
- 新版 [`00bb9370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9350.md#insn-00bb9370) · [`00bb936c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9350.md#insn-00bb936c) · [`00bb9378`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9350.md#insn-00bb9378)

~~~diff
- 00bb92d4 ["INT_ADD", "register:40f0:8", ["const:bb92d4:8", "const:4:8"]]
- 00bb92d4 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bb9370 ["INT_ADD", "register:40f0:8", ["const:bb9370:8", "const:4:8"]]
+ 00bb9370 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bb92d4 bytes 4b870294
+ 00bb9370 bytes 58870294
- 00bb92d0 ["COPY", "tmp:0:8", ["const:51e:8"]]
- 00bb92d0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bb92d0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bb92d0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bb936c ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00bb936c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bb936c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bb936c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bb92d0 bytes 00781491
+ 00bb936c bytes 00341591
- 00bb92dc ["COPY", "tmp:0:8", ["const:330:8"]]
- 00bb92dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bb92dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bb92dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bb9378 ["COPY", "tmp:0:8", ["const:430:8"]]
+ 00bb9378 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bb9378 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bb9378 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bb92dc bytes 08c10c91
+ 00bb9378 bytes 08c11091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ebebeca28d90f800fd8835be6e627e5"></a>

### [`00bb92f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb92f0.md) → [`00bb938c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb938c.md) _ZN8firebase9messaging26illegal_argument_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS

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
      "definition_site": "00bb93b8",
      "incomplete_value": true,
      "site": "00bb93b8",
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
            "const:438:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb931c",
      "incomplete_value": true,
      "site": "00bb931c",
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
            "const:338:8"
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
      "definition_site": "00bb93a0",
      "incomplete_value": true,
      "site": "00bb93a0",
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
      "definition_site": "00bb9304",
      "incomplete_value": true,
      "site": "00bb9304",
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
      "definition_site": "00bb93ac",
      "incomplete_value": false,
      "site": "00bb93b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:eb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb9310",
      "incomplete_value": false,
      "site": "00bb9314",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:f14:8"
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
      "00bb939c",
      "READ",
      [
        "storage",
        "01126338",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb93ac",
      "PARAM",
      [
        "storage",
        "002a4f14",
        null,
        "string"
      ]
    ],
    [
      "00bb93b8",
      "WRITE",
      [
        "storage",
        "01126338",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bb939c",
      "READ",
      [
        "storage",
        "01126438",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb93ac",
      "PARAM",
      [
        "storage",
        "002a4eb8",
        null,
        "string"
      ]
    ],
    [
      "00bb93b8",
      "WRITE",
      [
        "storage",
        "01126438",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb9314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb92f0.md#insn-00bb9314) · [`00bb931c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb92f0.md#insn-00bb931c) · [`00bb9300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb92f0.md#insn-00bb9300)
- 新版 [`00bb93b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb938c.md#insn-00bb93b0) · [`00bb93b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb938c.md#insn-00bb93b8) · [`00bb939c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb938c.md#insn-00bb939c)

~~~diff
- 00bb9314 ["INT_ADD", "register:40f0:8", ["const:bb9314:8", "const:4:8"]]
- 00bb9314 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bb93b0 ["INT_ADD", "register:40f0:8", ["const:bb93b0:8", "const:4:8"]]
+ 00bb93b0 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bb9314 bytes ff860294
+ 00bb93b0 bytes 0c870294
- 00bb931c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:338:8"]]
- 00bb931c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bb93b8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:438:8"]]
+ 00bb93b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb931c bytes 609e01f9
+ 00bb93b8 bytes 601e02f9
- 00bb9300 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:338:8"]]
- 00bb9300 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb939c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:438:8"]]
+ 00bb939c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb9300 bytes 689e41f9
+ 00bb939c bytes 681e42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d2b3fcbb141f402ad7348852f1fc0da"></a>

### [`00bb9330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9330.md) → [`00bb93cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb93cc.md) _ZN8firebase9messaging26illegal_argument_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS

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
      "definition_site": "00bb93f8",
      "incomplete_value": true,
      "site": "00bb93f8",
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
            "const:438:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb935c",
      "incomplete_value": true,
      "site": "00bb935c",
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
            "const:338:8"
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
      "definition_site": "00bb93e0",
      "incomplete_value": true,
      "site": "00bb93e0",
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
      "definition_site": "00bb9344",
      "incomplete_value": true,
      "site": "00bb9344",
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
      "definition_site": "00bb93e8",
      "incomplete_value": false,
      "site": "00bb93f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:eb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb934c",
      "incomplete_value": false,
      "site": "00bb9354",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:f14:8"
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
      "00bb93dc",
      "READ",
      [
        "storage",
        "01126338",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb93e8",
      "PARAM",
      [
        "storage",
        "002a4f14",
        null,
        "string"
      ]
    ],
    [
      "00bb93f8",
      "WRITE",
      [
        "storage",
        "01126338",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bb93dc",
      "READ",
      [
        "storage",
        "01126438",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb93e8",
      "PARAM",
      [
        "storage",
        "002a4eb8",
        null,
        "string"
      ]
    ],
    [
      "00bb93f8",
      "WRITE",
      [
        "storage",
        "01126438",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb9354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9330.md#insn-00bb9354) · [`00bb935c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9330.md#insn-00bb935c) · [`00bb9340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9330.md#insn-00bb9340)
- 新版 [`00bb93f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb93cc.md#insn-00bb93f0) · [`00bb93f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb93cc.md#insn-00bb93f8) · [`00bb93dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb93cc.md#insn-00bb93dc)

~~~diff
- 00bb9354 ["INT_ADD", "register:40f0:8", ["const:bb9354:8", "const:4:8"]]
- 00bb9354 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bb93f0 ["INT_ADD", "register:40f0:8", ["const:bb93f0:8", "const:4:8"]]
+ 00bb93f0 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bb9354 bytes ef860294
+ 00bb93f0 bytes fc860294
- 00bb935c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:338:8"]]
- 00bb935c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bb93f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:438:8"]]
+ 00bb93f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb935c bytes 609e01f9
+ 00bb93f8 bytes 601e02f9
- 00bb9340 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:338:8"]]
- 00bb9340 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb93dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:438:8"]]
+ 00bb93dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb9340 bytes 689e41f9
+ 00bb93dc bytes 681e42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40666f1507ed8f3db845cb65a7886c64"></a>

### [`00bb9370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9370.md) → [`00bb940c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb940c.md) _ZN8firebase9messaging26illegal_argument_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bb943c",
      "incomplete_value": true,
      "site": "00bb943c",
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
            "const:438:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb93a0",
      "incomplete_value": true,
      "site": "00bb93a0",
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
            "const:338:8"
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
      "definition_site": "00bb9420",
      "incomplete_value": true,
      "site": "00bb9420",
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
      "definition_site": "00bb9384",
      "incomplete_value": true,
      "site": "00bb9384",
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
      "definition_site": "00bb942c",
      "incomplete_value": false,
      "site": "00bb9434",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:eb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb9390",
      "incomplete_value": false,
      "site": "00bb9398",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:f14:8"
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
      "00bb941c",
      "READ",
      [
        "storage",
        "01126338",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb942c",
      "PARAM",
      [
        "storage",
        "002a4f14",
        null,
        "string"
      ]
    ],
    [
      "00bb943c",
      "WRITE",
      [
        "storage",
        "01126338",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bb941c",
      "READ",
      [
        "storage",
        "01126438",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb942c",
      "PARAM",
      [
        "storage",
        "002a4eb8",
        null,
        "string"
      ]
    ],
    [
      "00bb943c",
      "WRITE",
      [
        "storage",
        "01126438",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb9398`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9370.md#insn-00bb9398) · [`00bb93a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9370.md#insn-00bb93a0) · [`00bb9380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9370.md#insn-00bb9380)
- 新版 [`00bb9434`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb940c.md#insn-00bb9434) · [`00bb943c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb940c.md#insn-00bb943c) · [`00bb941c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb940c.md#insn-00bb941c)

~~~diff
- 00bb9398 ["INT_ADD", "register:40f0:8", ["const:bb9398:8", "const:4:8"]]
- 00bb9398 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bb9434 ["INT_ADD", "register:40f0:8", ["const:bb9434:8", "const:4:8"]]
+ 00bb9434 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bb9398 bytes de860294
+ 00bb9434 bytes eb860294
- 00bb93a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:338:8"]]
- 00bb93a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bb943c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:438:8"]]
+ 00bb943c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb93a0 bytes 609e01f9
+ 00bb943c bytes 601e02f9
- 00bb9380 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:338:8"]]
- 00bb9380 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb941c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:438:8"]]
+ 00bb941c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb9380 bytes 689e41f9
+ 00bb941c bytes 681e42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50dbead783498ba2fdf5d250faa238e9"></a>

### [`00bb93b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb93b4.md) → [`00bb9450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9450.md) _ZN8firebase9messaging26illegal_argument_exception10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00bb9480",
      "incomplete_value": true,
      "site": "00bb9480",
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
            "const:438:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb93e4",
      "incomplete_value": true,
      "site": "00bb93e4",
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
            "const:338:8"
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
      "definition_site": "00bb9464",
      "incomplete_value": true,
      "site": "00bb9464",
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
      "definition_site": "00bb93c8",
      "incomplete_value": true,
      "site": "00bb93c8",
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
      "definition_site": "00bb946c",
      "incomplete_value": false,
      "site": "00bb9478",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:eb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb93d0",
      "incomplete_value": false,
      "site": "00bb93dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:f14:8"
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
      "00bb9460",
      "READ",
      [
        "storage",
        "01126338",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb946c",
      "PARAM",
      [
        "storage",
        "002a4f14",
        null,
        "string"
      ]
    ],
    [
      "00bb9480",
      "WRITE",
      [
        "storage",
        "01126338",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bb9460",
      "READ",
      [
        "storage",
        "01126438",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb946c",
      "PARAM",
      [
        "storage",
        "002a4eb8",
        null,
        "string"
      ]
    ],
    [
      "00bb9480",
      "WRITE",
      [
        "storage",
        "01126438",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb93dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb93b4.md#insn-00bb93dc) · [`00bb93e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb93b4.md#insn-00bb93e4) · [`00bb93c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb93b4.md#insn-00bb93c4)
- 新版 [`00bb9478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9450.md#insn-00bb9478) · [`00bb9480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9450.md#insn-00bb9480) · [`00bb9460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9450.md#insn-00bb9460)

~~~diff
- 00bb93dc ["INT_ADD", "register:40f0:8", ["const:bb93dc:8", "const:4:8"]]
- 00bb93dc ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bb9478 ["INT_ADD", "register:40f0:8", ["const:bb9478:8", "const:4:8"]]
+ 00bb9478 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bb93dc bytes cd860294
+ 00bb9478 bytes da860294
- 00bb93e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:338:8"]]
- 00bb93e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bb9480 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:438:8"]]
+ 00bb9480 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb93e4 bytes 609e01f9
+ 00bb9480 bytes 601e02f9
- 00bb93c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:338:8"]]
- 00bb93c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb9460 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:438:8"]]
+ 00bb9460 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb93c4 bytes 689e41f9
+ 00bb9460 bytes 681e42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f1f6f4a6bf8f3363f5a256c1d76b164"></a>

### [`00bb9404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9404.md) → [`00bb94a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb94a0.md) _ZN8firebase9messaging26illegal_argument_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00bb94f8",
      "incomplete_value": true,
      "site": "00bb94f8",
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
            "const:440:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb945c",
      "incomplete_value": true,
      "site": "00bb945c",
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
            "const:340:8"
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
      "definition_site": "00bb94d4",
      "incomplete_value": true,
      "site": "00bb94e0",
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
                "const:438:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb9438",
      "incomplete_value": true,
      "site": "00bb9444",
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
                "const:338:8"
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
      "00bb94b4",
      "READ",
      [
        "storage",
        "01126340",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb94d4",
      "READ",
      [
        "storage",
        "01126338",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb94f8",
      "WRITE",
      [
        "storage",
        "01126340",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bb94b4",
      "READ",
      [
        "storage",
        "01126440",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb94d4",
      "READ",
      [
        "storage",
        "01126438",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb94f8",
      "WRITE",
      [
        "storage",
        "01126440",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb9444`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9404.md#insn-00bb9444) · [`00bb945c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9404.md#insn-00bb945c) · [`00bb9418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9404.md#insn-00bb9418)
- 新版 [`00bb94e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb94a0.md#insn-00bb94e0) · [`00bb94f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb94a0.md#insn-00bb94f8) · [`00bb94b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb94a0.md#insn-00bb94b4)

~~~diff
- 00bb9444 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bb9444 ["INT_ADD", "register:40f0:8", ["const:bb9444:8", "const:4:8"]]
- 00bb9444 ["CALLIND", null, ["register:0:8"]]
+ 00bb94e0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bb94e0 ["INT_ADD", "register:40f0:8", ["const:bb94e0:8", "const:4:8"]]
+ 00bb94e0 ["CALLIND", null, ["register:0:8"]]
- 00bb9444 bytes 00013fd6
+ 00bb94e0 bytes 00013fd6
- 00bb945c ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bb945c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:340:8"]]
- 00bb945c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bb94f8 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bb94f8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:440:8"]]
+ 00bb94f8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bb945c bytes a0020d39
+ 00bb94f8 bytes a0021139
- 00bb9418 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:340:8"]]
- 00bb9418 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00bb9418 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00bb94b4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:440:8"]]
+ 00bb94b4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00bb94b4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00bb9418 bytes a8024d39
+ 00bb94b4 bytes a8025139
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4ac7ea41a06668ddca29311097701a1"></a>

### [`00bb9470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9470.md) → [`00bb950c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb950c.md) _ZN8firebase9messaging26illegal_argument_exception12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00bb9548",
      "incomplete_value": true,
      "site": "00bb9548",
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
            "const:440:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb94ac",
      "incomplete_value": true,
      "site": "00bb94ac",
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
            "const:340:8"
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
      "definition_site": "00bb9568",
      "incomplete_value": true,
      "site": "00bb9568",
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
            "const:438:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb94cc",
      "incomplete_value": true,
      "site": "00bb94cc",
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
            "const:338:8"
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
      "definition_site": "00bb9524",
      "incomplete_value": true,
      "site": "00bb9524",
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
      "definition_site": "00bb9488",
      "incomplete_value": true,
      "site": "00bb9488",
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
      "00bb9520",
      "READ",
      [
        "storage",
        "01126338",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb952c",
      "READ",
      [
        "storage",
        "01126340",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb9548",
      "WRITE",
      [
        "storage",
        "01126340",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bb9520",
      "READ",
      [
        "storage",
        "01126438",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb952c",
      "READ",
      [
        "storage",
        "01126440",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb9548",
      "WRITE",
      [
        "storage",
        "01126440",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb94ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9470.md#insn-00bb94ac) · [`00bb94c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9470.md#insn-00bb94c8) · [`00bb94cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9470.md#insn-00bb94cc)
- 新版 [`00bb9548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb950c.md#insn-00bb9548) · [`00bb9564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb950c.md#insn-00bb9564) · [`00bb9568`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb950c.md#insn-00bb9568)

~~~diff
- 00bb94ac ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bb94ac ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bb94ac ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:340:8"]]
- 00bb94ac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bb9548 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bb9548 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bb9548 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:440:8"]]
+ 00bb9548 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bb94ac bytes bf020d39
+ 00bb9548 bytes bf021139
- 00bb94c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bb94c8 ["INT_ADD", "register:40f0:8", ["const:bb94c8:8", "const:4:8"]]
- 00bb94c8 ["CALLIND", null, ["register:0:8"]]
+ 00bb9564 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bb9564 ["INT_ADD", "register:40f0:8", ["const:bb9564:8", "const:4:8"]]
+ 00bb9564 ["CALLIND", null, ["register:0:8"]]
- 00bb94c8 bytes 00013fd6
+ 00bb9564 bytes 00013fd6
- 00bb94cc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:338:8"]]
- 00bb94cc ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bb94cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bb9568 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:438:8"]]
+ 00bb9568 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bb9568 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00bb94cc bytes 9f9e01f9
+ 00bb9568 bytes 9f1e02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae9a09b9d10c7eb417277ff78019f1db"></a>

### [`00bb94e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb94e0.md) → [`00bb957c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb957c.md) _ZN8firebase9messaging26illegal_argument_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bb95bc",
      "incomplete_value": true,
      "site": "00bb95bc",
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
            "const:438:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb9520",
      "incomplete_value": true,
      "site": "00bb9520",
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
            "const:338:8"
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
      "definition_site": "00bb9598",
      "incomplete_value": true,
      "site": "00bb9598",
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
      "definition_site": "00bb94fc",
      "incomplete_value": true,
      "site": "00bb94fc",
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
      "definition_site": "00bb95a0",
      "incomplete_value": false,
      "site": "00bb95b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:eb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb9504",
      "incomplete_value": false,
      "site": "00bb9518",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:f14:8"
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
      "00bb9590",
      "READ",
      [
        "storage",
        "01126338",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb95a0",
      "PARAM",
      [
        "storage",
        "002a4f14",
        null,
        "string"
      ]
    ],
    [
      "00bb95bc",
      "WRITE",
      [
        "storage",
        "01126338",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bb9590",
      "READ",
      [
        "storage",
        "01126438",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb95a0",
      "PARAM",
      [
        "storage",
        "002a4eb8",
        null,
        "string"
      ]
    ],
    [
      "00bb95bc",
      "WRITE",
      [
        "storage",
        "01126438",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb9518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb94e0.md#insn-00bb9518) · [`00bb9520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb94e0.md#insn-00bb9520) · [`00bb94f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb94e0.md#insn-00bb94f4)
- 新版 [`00bb95b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb957c.md#insn-00bb95b4) · [`00bb95bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb957c.md#insn-00bb95bc) · [`00bb9590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb957c.md#insn-00bb9590)

~~~diff
- 00bb9518 ["INT_ADD", "register:40f0:8", ["const:bb9518:8", "const:4:8"]]
- 00bb9518 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bb95b4 ["INT_ADD", "register:40f0:8", ["const:bb95b4:8", "const:4:8"]]
+ 00bb95b4 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bb9518 bytes 7e860294
+ 00bb95b4 bytes 8b860294
- 00bb9520 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:338:8"]]
- 00bb9520 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bb95bc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:438:8"]]
+ 00bb95bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb9520 bytes 809e01f9
+ 00bb95bc bytes 801e02f9
- 00bb94f4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:338:8"]]
- 00bb94f4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb9590 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:438:8"]]
+ 00bb9590 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb94f4 bytes 819e41f9
+ 00bb9590 bytes 811e42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52a3b913ef2424b226b67f6209b7b51e"></a>

### [`00bb9550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9550.md) → [`00bb95ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb95ec.md) _ZN8firebase9messaging26illegal_argument_exception11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bb9608",
      "incomplete_value": false,
      "site": "00bb960c",
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
      "definition_site": "00bb956c",
      "incomplete_value": false,
      "site": "00bb9570",
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
      "definition_site": "00bb9618",
      "incomplete_value": true,
      "site": "00bb9624",
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
      "definition_site": "00bb957c",
      "incomplete_value": true,
      "site": "00bb9588",
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
      "00bb9608",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00bb9618",
      "DATA",
      [
        "storage",
        "01126348",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bb9608",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00bb9618",
      "DATA",
      [
        "storage",
        "01126448",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb9570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9550.md#insn-00bb9570) · [`00bb956c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9550.md#insn-00bb956c) · [`00bb9578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9550.md#insn-00bb9578)
- 新版 [`00bb960c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb95ec.md#insn-00bb960c) · [`00bb9608`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb95ec.md#insn-00bb9608) · [`00bb9614`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb95ec.md#insn-00bb9614)

~~~diff
- 00bb9570 ["INT_ADD", "register:40f0:8", ["const:bb9570:8", "const:4:8"]]
- 00bb9570 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bb960c ["INT_ADD", "register:40f0:8", ["const:bb960c:8", "const:4:8"]]
+ 00bb960c ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bb9570 bytes a4860294
+ 00bb960c bytes b1860294
- 00bb956c ["COPY", "tmp:0:8", ["const:367:8"]]
- 00bb956c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bb956c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bb956c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bb9608 ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00bb9608 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bb9608 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bb9608 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bb956c bytes 009c0d91
+ 00bb9608 bytes 002c0c91
- 00bb9578 ["COPY", "tmp:0:8", ["const:348:8"]]
- 00bb9578 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bb9578 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bb9578 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bb9614 ["COPY", "tmp:0:8", ["const:448:8"]]
+ 00bb9614 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bb9614 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bb9614 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bb9578 bytes 08210d91
+ 00bb9614 bytes 08211191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be0b7f77068d99f606801c1d5d4287c7"></a>

### [`00bb958c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb958c.md) → [`00bb9628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9628.md) _ZN8firebase9messaging26illegal_argument_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bb9668",
      "incomplete_value": true,
      "site": "00bb9668",
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
            "const:438:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb95cc",
      "incomplete_value": true,
      "site": "00bb95cc",
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
            "const:338:8"
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
      "definition_site": "00bb9644",
      "incomplete_value": true,
      "site": "00bb9644",
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
      "definition_site": "00bb95a8",
      "incomplete_value": true,
      "site": "00bb95a8",
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
      "definition_site": "00bb964c",
      "incomplete_value": false,
      "site": "00bb9660",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:eb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb95b0",
      "incomplete_value": false,
      "site": "00bb95c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:f14:8"
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
      "00bb963c",
      "READ",
      [
        "storage",
        "01126338",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb964c",
      "PARAM",
      [
        "storage",
        "002a4f14",
        null,
        "string"
      ]
    ],
    [
      "00bb9668",
      "WRITE",
      [
        "storage",
        "01126338",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bb963c",
      "READ",
      [
        "storage",
        "01126438",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb964c",
      "PARAM",
      [
        "storage",
        "002a4eb8",
        null,
        "string"
      ]
    ],
    [
      "00bb9668",
      "WRITE",
      [
        "storage",
        "01126438",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb95c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb958c.md#insn-00bb95c4) · [`00bb95cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb958c.md#insn-00bb95cc) · [`00bb95a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb958c.md#insn-00bb95a0)
- 新版 [`00bb9660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9628.md#insn-00bb9660) · [`00bb9668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9628.md#insn-00bb9668) · [`00bb963c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9628.md#insn-00bb963c)

~~~diff
- 00bb95c4 ["INT_ADD", "register:40f0:8", ["const:bb95c4:8", "const:4:8"]]
- 00bb95c4 ["CALL", null, ["callee:00c5afe0:8"]]
+ 00bb9660 ["INT_ADD", "register:40f0:8", ["const:bb9660:8", "const:4:8"]]
+ 00bb9660 ["CALL", null, ["callee:00c5afe0:8"]]
- 00bb95c4 bytes 53860294
+ 00bb9660 bytes 60860294
- 00bb95cc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:338:8"]]
- 00bb95cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bb9668 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:438:8"]]
+ 00bb9668 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb95cc bytes 809e01f9
+ 00bb9668 bytes 801e02f9
- 00bb95a0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:338:8"]]
- 00bb95a0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb963c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:438:8"]]
+ 00bb963c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb95a0 bytes 819e41f9
+ 00bb963c bytes 811e42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5fa890b62083f7a863fa9c7422940cb"></a>

### [`00bb95fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb95fc.md) → [`00bb9698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9698.md) _ZN8firebase9messaging26illegal_argument_exception10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bb96b4",
      "incomplete_value": false,
      "site": "00bb96b8",
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
      "definition_site": "00bb9618",
      "incomplete_value": false,
      "site": "00bb961c",
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
      "definition_site": "00bb96c4",
      "incomplete_value": true,
      "site": "00bb96d0",
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
      "definition_site": "00bb9628",
      "incomplete_value": true,
      "site": "00bb9634",
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
      "00bb96b4",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00bb96c4",
      "DATA",
      [
        "storage",
        "01126350",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bb96b4",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00bb96c4",
      "DATA",
      [
        "storage",
        "01126450",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb961c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb95fc.md#insn-00bb961c) · [`00bb9618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb95fc.md#insn-00bb9618) · [`00bb9624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb95fc.md#insn-00bb9624)
- 新版 [`00bb96b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9698.md#insn-00bb96b8) · [`00bb96b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9698.md#insn-00bb96b4) · [`00bb96c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9698.md#insn-00bb96c0)

~~~diff
- 00bb961c ["INT_ADD", "register:40f0:8", ["const:bb961c:8", "const:4:8"]]
- 00bb961c ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bb96b8 ["INT_ADD", "register:40f0:8", ["const:bb96b8:8", "const:4:8"]]
+ 00bb96b8 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bb961c bytes 79860294
+ 00bb96b8 bytes 86860294
- 00bb9618 ["COPY", "tmp:0:8", ["const:51e:8"]]
- 00bb9618 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bb9618 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bb9618 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bb96b4 ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00bb96b4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bb96b4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bb96b4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bb9618 bytes 00781491
+ 00bb96b4 bytes 00341591
- 00bb9624 ["COPY", "tmp:0:8", ["const:350:8"]]
- 00bb9624 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bb9624 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bb9624 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bb96c0 ["COPY", "tmp:0:8", ["const:450:8"]]
+ 00bb96c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bb96c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bb96c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bb9624 bytes 08410d91
+ 00bb96c0 bytes 08411191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3b7ca4b59ce74ec8ec5c092f21f7e38"></a>

### [`00bb972c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb972c.md) → [`00bb97c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb97c8.md) _ZN8firebase9messaging17NotifyListenerSetEPNS0_8ListenerE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d2f0.md) · 呼出先 6件 [`00c597d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c597d0.md) [`00c5a000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a000.md) [`00c5a090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a090.md) [`00c5a260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a260.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)
- 新版 呼出元 1件 [`00c5d3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d3c0.md) · 呼出先 6件 [`00c598a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c598a0.md) [`00c5a0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0d0.md) [`00c5a160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a160.md) [`00c5a330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a330.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 97.56% / 新版 97.56%

CFGの説明率　旧版 71.43% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bb97e0",
      "incomplete_value": true,
      "site": "00bb97e0",
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
      "definition_site": "00bb9744",
      "incomplete_value": true,
      "site": "00bb9744",
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
      "definition_site": "00bb9858",
      "incomplete_value": true,
      "site": "00bb9858",
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
      "definition_site": "00bb97bc",
      "incomplete_value": true,
      "site": "00bb97bc",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb982c",
      "incomplete_value": false,
      "site": "00bb9830",
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
            "const:ea:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb9790",
      "incomplete_value": false,
      "site": "00bb9794",
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
            "const:137:8"
          ]
        ]
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
      "00bb97dc",
      "READ",
      [
        "storage",
        "01126360",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb97e8",
      "READ",
      [
        "storage",
        "01126390",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb980c",
      "READ",
      [
        "storage",
        "01126368",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bb97dc",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb97e8",
      "READ",
      [
        "storage",
        "01126490",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb980c",
      "READ",
      [
        "storage",
        "01126468",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb9794`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb972c.md#insn-00bb9794) · [`00bb97b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb972c.md#insn-00bb97b0) · [`00bb9740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb972c.md#insn-00bb9740)
- 新版 [`00bb9830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb97c8.md#insn-00bb9830) · [`00bb984c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb97c8.md#insn-00bb984c) · [`00bb97dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb97c8.md#insn-00bb97dc)

~~~diff
- 00bb9794 ["INT_ADD", "register:40f0:8", ["const:bb9794:8", "const:4:8"]]
- 00bb9794 ["CALL", null, ["callee:00c5a160:8"]]
+ 00bb9830 ["INT_ADD", "register:40f0:8", ["const:bb9830:8", "const:4:8"]]
+ 00bb9830 ["CALL", null, ["callee:00c5a160:8"]]
- 00bb9794 bytes 3f820294
+ 00bb9830 bytes 4c820294
- 00bb97b0 ["INT_ADD", "register:40f0:8", ["const:bb97b0:8", "const:4:8"]]
- 00bb97b0 ["CALL", null, ["callee:00c598a0:8"]]
+ 00bb984c ["INT_ADD", "register:40f0:8", ["const:bb984c:8", "const:4:8"]]
+ 00bb984c ["CALL", null, ["callee:00c598a0:8"]]
- 00bb97b0 bytes 08800294
+ 00bb984c bytes 15800294
- 00bb9740 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:360:8"]]
- 00bb9740 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb97dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:460:8"]]
+ 00bb97dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb9740 bytes 08b141f9
+ 00bb97dc bytes 083142f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-855dee8fa82cf4cd33535e29c51285ec"></a>

### [`00bb9818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9818.md) → [`00bb98b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb98b4.md) _ZN8firebase9messaging17RequestPermissionEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5ada0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ada0.md) [`00c5add0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5add0.md) [`00c5ae00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae00.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md) [`00c5ae70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae70.md) [`00c5aea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aea0.md) [`00c5aed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aed0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.25% / 新版 98.25%

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
      "definition_site": "00bb98e0",
      "incomplete_value": true,
      "site": "00bb98e0",
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
      "definition_site": "00bb9844",
      "incomplete_value": true,
      "site": "00bb9844",
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
      "definition_site": "00bb9960",
      "incomplete_value": false,
      "site": "00bb9964",
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
            "const:8c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb98c4",
      "incomplete_value": false,
      "site": "00bb98c8",
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
            "const:915:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bb98dc",
      "READ",
      [
        "storage",
        "01126360",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9960",
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
      "00bb98dc",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9960",
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

- 旧版 [`00bb98c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9818.md#insn-00bb98c8) · [`00bb9840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9818.md#insn-00bb9840) · [`00bb9848`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9818.md#insn-00bb9848)
- 新版 [`00bb9964`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb98b4.md#insn-00bb9964) · [`00bb98dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb98b4.md#insn-00bb98dc) · [`00bb98e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb98b4.md#insn-00bb98e4)

~~~diff
- 00bb98c8 ["INT_ADD", "register:40f0:8", ["const:bb98c8:8", "const:4:8"]]
- 00bb98c8 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bb9964 ["INT_ADD", "register:40f0:8", ["const:bb9964:8", "const:4:8"]]
+ 00bb9964 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bb98c8 bytes ce850294
+ 00bb9964 bytes db850294
- 00bb9840 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:360:8"]]
- 00bb9840 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb98dc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:460:8"]]
+ 00bb98dc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb9840 bytes 29b141f9
+ 00bb98dc bytes 293142f9
- 00bb9848 ["INT_ADD", "register:40f0:8", ["const:bb9848:8", "const:4:8"]]
- 00bb9848 ["CALL", null, ["callee:00c5d340:8"]]
+ 00bb98e4 ["INT_ADD", "register:40f0:8", ["const:bb98e4:8", "const:4:8"]]
+ 00bb98e4 ["CALL", null, ["callee:00c5d340:8"]]
- 00bb9848 bytes 8a8e0294
+ 00bb98e4 bytes 978e0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8014120350930887ea6df62cbe53193e"></a>

### [`00bb9940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9940.md) → [`00bb99dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb99dc.md) _ZN8firebase9messaging27RequestPermissionLastResultEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d5b0.md) · 呼出先 8件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5abe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abe0.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md)
- 新版 呼出元 1件 [`00c5d680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d680.md) · 呼出先 8件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5acb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5acb0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, comparison, comparison_count, constant, control_flow, operands_and_dependencies, operation_sequence, store_condition

命令の説明率　旧版 97.62% / 新版 97.62%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bb99f8",
      "incomplete_value": true,
      "site": "00bb99f8",
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
      "definition_site": "00bb995c",
      "incomplete_value": true,
      "site": "00bb995c",
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
      "definition_site": "00bb996c",
      "incomplete_value": true,
      "site": "00bb9970",
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
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00bb999c",
      "incomplete_value": true,
      "site": "00bb99a4",
      "value": [
        "live",
        "register:4098:8"
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
      "00bb99f0",
      "READ",
      [
        "storage",
        "01126360",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bb99b0",
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
      "00bb99f0",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9a4c",
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

- 旧版 [`00bb995c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9940.md#insn-00bb995c) · [`00bb9970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9940.md#insn-00bb9970) · [`00bb99a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9940.md#insn-00bb99a4)
- 新版 [`00bb99f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb99dc.md#insn-00bb99f8) · [`00bb9a0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb99dc.md#insn-00bb9a0c) · [`00bb9a40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb99dc.md#insn-00bb9a40)

~~~diff
- 00bb995c ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00bb995c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bb99f8 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
+ 00bb99f8 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00bb995c bytes 890200b4
+ 00bb99f8 bytes 890200b4
- 00bb9970 ["INT_ADD", "register:40f0:8", ["const:bb9970:8", "const:4:8"]]
- 00bb9970 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00bb9a0c ["INT_ADD", "register:40f0:8", ["const:bb9a0c:8", "const:4:8"]]
+ 00bb9a0c ["CALL", null, ["callee:00c5aad0:8"]]
- 00bb9970 bytes 24840294
+ 00bb9a0c bytes 31840294
- 00bb99a4 ["INT_ADD", "register:40f0:8", ["const:bb99a4:8", "const:4:8"]]
- 00bb99a4 ["CALL", null, ["callee:00c5ae20:8"]]
+ 00bb9a40 ["INT_ADD", "register:40f0:8", ["const:bb9a40:8", "const:4:8"]]
+ 00bb9a40 ["CALL", null, ["callee:00c5ae20:8"]]
- 00bb99a4 bytes eb840294
+ 00bb9a40 bytes f8840294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e2ddf7ae6ccbb3778c9350d88345eaa"></a>

### [`00bb9a14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9a14.md) → [`00bb9ab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9ab0.md) _ZN8firebase9messaging15ProcessMessagesEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d5a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d5a0.md) · 呼出先 41件 [`0046d5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d5a8.md) [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`00bbd154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd154.md) [`00bbd158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd158.md)
- 新版 呼出元 1件 [`00c5d670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d670.md) · 呼出先 41件 [`0046d5e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d5e8.md) [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00497a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md) [`00bbd1f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd1f0.md) [`00bbd1f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd1f4.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 24.72% / 新版 24.72%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 21件, `unresolved_branch_alignment` 8件, `unresolved_call_alignment` 31件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 31件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb9a14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb9a14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb9a18"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb9a14",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb9a18",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb9a1c",
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
      "00bb9ab0",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00bb9ab4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00bb9ab8",
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

- 旧版 [`00bb9a14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9a14.md#insn-00bb9a14) · [`00bb9a18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9a14.md#insn-00bb9a18) · [`00bb9a1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9a14.md#insn-00bb9a1c)

~~~diff
- 00bb9a14 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00bb9a14 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00bb9a14 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffa0:8"]]
- 00bb9a14 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bb9a14 bytes fc6fbaa9
- 00bb9a18 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00bb9a18 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00bb9a18 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bb9a18 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb9a18 bytes fa6701a9
- 00bb9a1c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00bb9a1c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00bb9a1c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bb9a1c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bb9a1c bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a43dbf3fb6f65a8713126038e6dbc01c"></a>

### [`00bba628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bba/00bba628.md) → [`00bba6c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bba6c4.md) _ZN8firebase9messaging10InitializeERKNS_3AppEPNS0_8ListenerERKNS0_16MessagingOptionsE

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d590.md) · 呼出先 33件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`00b5abb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5a/00b5abb4.md) [`00bbab50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bba/00bbab50.md) [`00bbac0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bba/00bbac0c.md)
- 新版 呼出元 1件 [`00c5d660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d660.md) · 呼出先 33件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00497a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md) [`00b5ac50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5a/00b5ac50.md) [`00bbabec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbabec.md) [`00bbaca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbaca8.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 61.79% / 新版 61.79%

CFGの説明率　旧版 40.98% / 新版 40.98%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 19件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 13件, `unresolved_store_alignment` 26件

アドレスに依存する影響 `branch_value` 2件, `call_argument_candidate` 2件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bba6fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bba754"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bba790"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bba714",
      "READ",
      [
        "storage",
        "01126360",
        null,
        "undefined8"
      ]
    ],
    [
      "00bba720",
      "PARAM",
      [
        "storage",
        "002a3ba9",
        null,
        "string"
      ]
    ],
    [
      "00bba770",
      "READ",
      [
        "storage",
        "011262a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bba714",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ],
    [
      "00bba720",
      "PARAM",
      [
        "storage",
        "002a3b5c",
        null,
        "string"
      ]
    ],
    [
      "00bba770",
      "READ",
      [
        "storage",
        "011263a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bba6fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bba/00bba628.md#insn-00bba6fc) · [`00bba754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bba/00bba628.md#insn-00bba754) · [`00bba790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bba/00bba628.md#insn-00bba790)

~~~diff
- 00bba6fc ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:2a8:8"]]
- 00bba6fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bba6fc bytes 005701f9
- 00bba754 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:318:8"]]
- 00bba754 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bba754 bytes a08e01f9
- 00bba790 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:360:8"]]
- 00bba790 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 00bba790 bytes f4b201f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73e20f37f23fe134e136aec305f7b2e4"></a>

### [`00bbab50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bba/00bbab50.md) → [`00bbabec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbabec.md) FUN_00bbabec

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00bba628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bba/00bba628.md) [`00bbb058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbb058.md) · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)
- 新版 呼出元 2件 [`00bba6c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bba6c4.md) [`00bbb0f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbb0f4.md) · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 87.23% / 新版 87.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 4件

アドレスに依存する影響 `branch_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bbac28",
      "incomplete_value": true,
      "site": "00bbac28",
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
            "const:3b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbab8c",
      "incomplete_value": true,
      "site": "00bbab8c",
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
            "const:2b0:8"
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
      "definition_site": "00bbac48",
      "incomplete_value": true,
      "site": "00bbac48",
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
            "const:3a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbabac",
      "incomplete_value": true,
      "site": "00bbabac",
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
            "const:2a8:8"
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
      "definition_site": "00bbac74",
      "incomplete_value": true,
      "site": "00bbac74",
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
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbabd8",
      "incomplete_value": true,
      "site": "00bbabd8",
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
            "const:320:8"
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
      "00bbac00",
      "READ",
      [
        "storage",
        "011262a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbac10",
      "READ",
      [
        "storage",
        "011262b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bbac28",
      "WRITE",
      [
        "storage",
        "011262b0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bbac00",
      "READ",
      [
        "storage",
        "011263a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbac10",
      "READ",
      [
        "storage",
        "011263b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bbac28",
      "WRITE",
      [
        "storage",
        "011263b0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbab8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bba/00bbab50.md#insn-00bbab8c) · [`00bbaba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bba/00bbab50.md#insn-00bbaba8) · [`00bbabac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bba/00bbab50.md#insn-00bbabac)
- 新版 [`00bbac28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbabec.md#insn-00bbac28) · [`00bbac44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbabec.md#insn-00bbac44) · [`00bbac48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbabec.md#insn-00bbac48)

~~~diff
- 00bbab8c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bbab8c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bbab8c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:2b0:8"]]
- 00bbab8c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bbac28 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bbac28 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bbac28 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:3b0:8"]]
+ 00bbac28 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bbab8c bytes bfc20a39
+ 00bbac28 bytes bfc20e39
- 00bbaba8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bbaba8 ["INT_ADD", "register:40f0:8", ["const:bbaba8:8", "const:4:8"]]
- 00bbaba8 ["CALLIND", null, ["register:0:8"]]
+ 00bbac44 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bbac44 ["INT_ADD", "register:40f0:8", ["const:bbac44:8", "const:4:8"]]
+ 00bbac44 ["CALLIND", null, ["register:0:8"]]
- 00bbaba8 bytes 00013fd6
+ 00bbac44 bytes 00013fd6
- 00bbabac ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2a8:8"]]
- 00bbabac ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bbabac ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bbac48 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3a8:8"]]
+ 00bbac48 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bbac48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00bbabac bytes 9f5601f9
+ 00bbac48 bytes 9fd601f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47e4c92410456f3281f1774ac33e3499"></a>

### [`00bbac0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bba/00bbac0c.md) → [`00bbaca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbaca8.md) FUN_00bbaca8

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bba628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bba/00bba628.md) · 呼出先 11件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 1件 [`00bba6c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bba6c4.md) · 呼出先 11件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 92.47% / 新版 92.47%

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
      "definition_site": "00bbace8",
      "incomplete_value": true,
      "site": "00bbace8",
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
      "definition_site": "00bbac4c",
      "incomplete_value": true,
      "site": "00bbac4c",
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
      "definition_site": "00bbacd4",
      "incomplete_value": false,
      "site": "00bbacdc",
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
            "const:358:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbac38",
      "incomplete_value": false,
      "site": "00bbac40",
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
            "const:258:8"
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
      "definition_site": "00bbad00",
      "incomplete_value": false,
      "site": "00bbad04",
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
            "const:358:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbac64",
      "incomplete_value": false,
      "site": "00bbac68",
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
            "const:258:8"
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
      "00bbacd4",
      "PARAM",
      [
        "storage",
        "01126258",
        null,
        null
      ]
    ],
    [
      "00bbace4",
      "READ",
      [
        "storage",
        "01126360",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbad00",
      "PARAM",
      [
        "storage",
        "01126258",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bbacd4",
      "PARAM",
      [
        "storage",
        "01126358",
        null,
        null
      ]
    ],
    [
      "00bbace4",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbad00",
      "PARAM",
      [
        "storage",
        "01126358",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbac40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bba/00bbac0c.md#insn-00bbac40) · [`00bbac68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bba/00bbac0c.md#insn-00bbac68) · [`00bbace8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bba/00bbac0c.md#insn-00bbace8)
- 新版 [`00bbacdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbaca8.md#insn-00bbacdc) · [`00bbad04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbaca8.md#insn-00bbad04) · [`00bbad84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbaca8.md#insn-00bbad84)

~~~diff
- 00bbac40 ["INT_ADD", "register:40f0:8", ["const:bbac40:8", "const:4:8"]]
- 00bbac40 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00bbacdc ["INT_ADD", "register:40f0:8", ["const:bbacdc:8", "const:4:8"]]
+ 00bbacdc ["CALL", null, ["callee:00c5aad0:8"]]
- 00bbac40 bytes 707f0294
+ 00bbacdc bytes 7d7f0294
- 00bbac68 ["INT_ADD", "register:40f0:8", ["const:bbac68:8", "const:4:8"]]
- 00bbac68 ["CALL", null, ["callee:00c5aae0:8"]]
+ 00bbad04 ["INT_ADD", "register:40f0:8", ["const:bbad04:8", "const:4:8"]]
+ 00bbad04 ["CALL", null, ["callee:00c5aae0:8"]]
- 00bbac68 bytes 6a7f0294
+ 00bbad04 bytes 777f0294
- 00bbace8 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:360:8"]]
- 00bbace8 ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bbad84 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:460:8"]]
+ 00bbad84 ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
- 00bbace8 bytes 1ab341f9
+ 00bbad84 bytes 1a3342f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27bae1336b980350b9b6b971199fd5ec"></a>

### [`00bbada4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bba/00bbada4.md) → [`00bbae40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbae40.md) _ZN8firebase9messaging33SetTokenRegistrationOnInitEnabledEb

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5aae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aae0.md) · 呼出先 6件 [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00bbaf50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bba/00bbaf50.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)
- 新版 呼出元 1件 [`00c5abb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5abb0.md) · 呼出先 6件 [`00497a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md) [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00bbafec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbafec.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_condition, store_destination

命令の説明率　旧版 70.00% / 新版 70.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 4件, `call_argument_candidate` 9件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bbaf3c",
      "incomplete_value": false,
      "site": "00bbaf3c",
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
            "const:500:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbaea0",
      "incomplete_value": false,
      "site": "00bbaea0",
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
            "const:400:8"
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
      "definition_site": "00bbae60",
      "incomplete_value": true,
      "site": "00bbae60",
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
      "definition_site": "00bbadc4",
      "incomplete_value": true,
      "site": "00bbadc4",
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
      "definition_site": "00bbae74",
      "incomplete_value": true,
      "site": "00bbae74",
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
      "definition_site": "00bbadd8",
      "incomplete_value": true,
      "site": "00bbadd8",
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
      "00bbae58",
      "READ",
      [
        "storage",
        "01126360",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbae6c",
      "READ",
      [
        "storage",
        "01126360",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbae7c",
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
      "00bbae58",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbae6c",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbae7c",
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

- 旧版 [`00bbade4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bba/00bbada4.md#insn-00bbade4) · [`00bbadf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bba/00bbada4.md#insn-00bbadf0) · [`00bbae18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bba/00bbada4.md#insn-00bbae18)
- 新版 [`00bbae80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbae40.md#insn-00bbae80) · [`00bbae8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbae40.md#insn-00bbae8c) · [`00bbaeb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbae40.md#insn-00bbaeb4)

~~~diff
- 00bbade4 ["INT_ADD", "register:40f0:8", ["const:bbade4:8", "const:4:8"]]
- 00bbade4 ["CALL", null, ["callee:00c5ad70:8"]]
+ 00bbae80 ["INT_ADD", "register:40f0:8", ["const:bbae80:8", "const:4:8"]]
+ 00bbae80 ["CALL", null, ["callee:00c5ad70:8"]]
- 00bbade4 bytes af7f0294
+ 00bbae80 bytes bc7f0294
- 00bbadf0 ["INT_ADD", "register:40f0:8", ["const:bbadf0:8", "const:4:8"]]
- 00bbadf0 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bbae8c ["INT_ADD", "register:40f0:8", ["const:bbae8c:8", "const:4:8"]]
+ 00bbae8c ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bbadf0 bytes 84800294
+ 00bbae8c bytes 91800294
- 00bbae18 ["INT_ADD", "register:40f0:8", ["const:bbae18:8", "const:4:8"]]
- 00bbae18 ["CALL", null, ["callee:00497a88:8"]]
+ 00bbaeb4 ["INT_ADD", "register:40f0:8", ["const:bbaeb4:8", "const:4:8"]]
+ 00bbaeb4 ["CALL", null, ["callee:00497a88:8"]]
- 00bbae18 bytes 0c73e397
+ 00bbaeb4 bytes f572e397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1beacfd6972405f21dfef01d6239337b"></a>

### [`00bbaee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bba/00bbaee4.md) → [`00bbaf80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbaf80.md) _ZN8firebase9messaging32IsTokenRegistrationOnInitEnabledEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00497a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 74.07% / 新版 74.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bbaf94",
      "incomplete_value": true,
      "site": "00bbaf94",
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
      "definition_site": "00bbaef8",
      "incomplete_value": true,
      "site": "00bbaef8",
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00bbafb4",
      "incomplete_value": true,
      "site": "00bbafb4",
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
      "definition_site": "00bbaf18",
      "incomplete_value": true,
      "site": "00bbaf18",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bbaf9c",
      "incomplete_value": false,
      "site": "00bbafa0",
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
            "const:8c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbaf00",
      "incomplete_value": false,
      "site": "00bbaf04",
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
            "const:915:8"
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
      "00bbaf90",
      "READ",
      [
        "storage",
        "01126360",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbaf9c",
      "PARAM",
      [
        "storage",
        "002a2915",
        null,
        "string"
      ]
    ],
    [
      "00bbafa8",
      "PARAM",
      [
        "storage",
        "002b0777",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bbaf90",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbaf9c",
      "PARAM",
      [
        "storage",
        "002a28c8",
        null,
        "string"
      ]
    ],
    [
      "00bbafa8",
      "PARAM",
      [
        "storage",
        "002b071b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbaf04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bba/00bbaee4.md#insn-00bbaf04) · [`00bbaf10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bba/00bbaee4.md#insn-00bbaf10) · [`00bbaf30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bba/00bbaee4.md#insn-00bbaf30)
- 新版 [`00bbafa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbaf80.md#insn-00bbafa0) · [`00bbafac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbaf80.md#insn-00bbafac) · [`00bbafcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbaf80.md#insn-00bbafcc)

~~~diff
- 00bbaf04 ["INT_ADD", "register:40f0:8", ["const:bbaf04:8", "const:4:8"]]
- 00bbaf04 ["CALL", null, ["callee:00c5ad70:8"]]
+ 00bbafa0 ["INT_ADD", "register:40f0:8", ["const:bbafa0:8", "const:4:8"]]
+ 00bbafa0 ["CALL", null, ["callee:00c5ad70:8"]]
- 00bbaf04 bytes 677f0294
+ 00bbafa0 bytes 747f0294
- 00bbaf10 ["INT_ADD", "register:40f0:8", ["const:bbaf10:8", "const:4:8"]]
- 00bbaf10 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bbafac ["INT_ADD", "register:40f0:8", ["const:bbafac:8", "const:4:8"]]
+ 00bbafac ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bbaf10 bytes 3c800294
+ 00bbafac bytes 49800294
- 00bbaf30 ["INT_ADD", "register:40f0:8", ["const:bbaf30:8", "const:4:8"]]
- 00bbaf30 ["CALL", null, ["callee:00497a88:8"]]
+ 00bbafcc ["INT_ADD", "register:40f0:8", ["const:bbafcc:8", "const:4:8"]]
+ 00bbafcc ["CALL", null, ["callee:00497a88:8"]]
- 00bbaf30 bytes c672e397
+ 00bbafcc bytes af72e397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c3152d5c81e7c53f46cc1d3a2f444bb"></a>

### [`00bbaf50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bba/00bbaf50.md) → [`00bbafec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbafec.md) FUN_00bbafec

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00bba628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bba/00bba628.md) [`00bbada4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bba/00bbada4.md) · 呼出先 11件 [`0087b3bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b3bc.md) [`00bbd374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd374.md) [`00bbd38c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd38c.md) [`00bbd398`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd398.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 2件 [`00bba6c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bba6c4.md) [`00bbae40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbae40.md) · 呼出先 11件 [`0087b414`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b414.md) [`00bbd410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd410.md) [`00bbd428`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd428.md) [`00bbd434`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd434.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.74% / 新版 90.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

アドレスに依存する影響 `branch_value` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bbb03c",
      "incomplete_value": false,
      "site": "00bbb03c",
      "value": [
        "leaf",
        "const:bbd434:8"
      ]
    },
    "old": {
      "definition_site": "00bbafa0",
      "incomplete_value": false,
      "site": "00bbafa0",
      "value": [
        "leaf",
        "const:bbd398:8"
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bbb010",
      "incomplete_value": true,
      "site": "00bbb010",
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
      "definition_site": "00bbaf74",
      "incomplete_value": true,
      "site": "00bbaf74",
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
      "definition_site": "00bbb05c",
      "incomplete_value": true,
      "site": "00bbb070",
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
                "const:9e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbafc0",
      "incomplete_value": true,
      "site": "00bbafd4",
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
                "const:910:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bbb00c",
      "READ",
      [
        "storage",
        "01126360",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbb03c",
      "DATA",
      [
        "storage",
        "00bbd398",
        null,
        null
      ]
    ],
    [
      "00bbb05c",
      "READ",
      [
        "storage",
        "00c9b910",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bbb00c",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbb03c",
      "DATA",
      [
        "storage",
        "00bbd434",
        null,
        null
      ]
    ],
    [
      "00bbb05c",
      "READ",
      [
        "storage",
        "00c9b9e0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbafd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bba/00bbaf50.md#insn-00bbafd4) · [`00bbaff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bba/00bbaf50.md#insn-00bbaff4) · [`00bbb000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bba/00bbaf50.md#insn-00bbb000)
- 新版 [`00bbb070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbafec.md#insn-00bbb070) · [`00bbb090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbafec.md#insn-00bbb090) · [`00bbb09c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbafec.md#insn-00bbb09c)

~~~diff
- 00bbafd4 ["COPY", "register:0:8", ["register:4048:8"]]
- 00bbafd4 ["INT_ADD", "register:40f0:8", ["const:bbafd4:8", "const:4:8"]]
- 00bbafd4 ["CALLIND", null, ["register:0:8"]]
+ 00bbb070 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00bbb070 ["INT_ADD", "register:40f0:8", ["const:bbb070:8", "const:4:8"]]
+ 00bbb070 ["CALLIND", null, ["register:0:8"]]
- 00bbafd4 bytes 20013fd6
+ 00bbb070 bytes 20013fd6
- 00bbaff4 ["INT_ADD", "register:40f0:8", ["const:bbaff4:8", "const:4:8"]]
- 00bbaff4 ["CALL", null, ["callee:00c5ad70:8"]]
+ 00bbb090 ["INT_ADD", "register:40f0:8", ["const:bbb090:8", "const:4:8"]]
+ 00bbb090 ["CALL", null, ["callee:00c5ad70:8"]]
- 00bbaff4 bytes 2b7f0294
+ 00bbb090 bytes 387f0294
- 00bbb000 ["INT_ADD", "register:40f0:8", ["const:bbb000:8", "const:4:8"]]
- 00bbb000 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bbb09c ["INT_ADD", "register:40f0:8", ["const:bbb09c:8", "const:4:8"]]
+ 00bbb09c ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bbb000 bytes 00800294
+ 00bbb09c bytes 0d800294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ccc98428028613b9d5184d347e93c73"></a>

### [`00bbb058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbb058.md) → [`00bbb0f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbb0f4.md) _ZN8firebase9messaging9TerminateEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d440.md) · 呼出先 23件 [`00bbab50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bba/00bbab50.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c597d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c597d0.md) [`00c5a000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a000.md) [`00c5a090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a090.md)
- 新版 呼出元 1件 [`00c5d510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d510.md) · 呼出先 23件 [`00bbabec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbabec.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c598a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c598a0.md) [`00c5a0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0d0.md) [`00c5a160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a160.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_destination, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 73.50% / 新版 73.50%

CFGの説明率　旧版 61.33% / 新版 61.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 8件, `store_destination` 2件, `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 8件, `unresolved_store_alignment` 7件

アドレスに依存する影響 `branch_value` 3件, `call_argument_candidate` 2件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bbb144",
      "incomplete_value": true,
      "site": "00bbb144",
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
            "const:460:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbb0a8",
      "incomplete_value": true,
      "site": "00bbb0a8",
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
            "const:360:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbb1c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbb1e4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bbb110",
      "READ",
      [
        "storage",
        "01126360",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbb11c",
      "READ",
      [
        "storage",
        "01126360",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbb128",
      "PARAM",
      [
        "storage",
        "0030e7c1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bbb110",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbb11c",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbb128",
      "PARAM",
      [
        "storage",
        "0030e801",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbb0a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbb058.md#insn-00bbb0a8) · [`00bbb12c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbb058.md#insn-00bbb12c) · [`00bbb144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbb058.md#insn-00bbb144)
- 新版 [`00bbb144`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbb0f4.md#insn-00bbb144) · [`00bbb1c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbb0f4.md#insn-00bbb1c8) · [`00bbb1e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbb0f4.md#insn-00bbb1e0)

~~~diff
- 00bbb0a8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:360:8"]]
- 00bbb0a8 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bbb0a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bbb144 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:460:8"]]
+ 00bbb144 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bbb144 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00bbb0a8 bytes bfb201f9
+ 00bbb144 bytes bf3202f9
- 00bbb12c ["INT_ADD", "register:40f0:8", ["const:bbb12c:8", "const:4:8"]]
- 00bbb12c ["CALL", null, ["callee:00c5a0d0:8"]]
+ 00bbb1c8 ["INT_ADD", "register:40f0:8", ["const:bbb1c8:8", "const:4:8"]]
+ 00bbb1c8 ["CALL", null, ["callee:00c5a0d0:8"]]
- 00bbb12c bytes b57b0294
+ 00bbb1c8 bytes c27b0294
- 00bbb144 ["INT_ADD", "register:40f0:8", ["const:bbb144:8", "const:4:8"]]
- 00bbb144 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bbb1e0 ["INT_ADD", "register:40f0:8", ["const:bbb1e0:8", "const:4:8"]]
+ 00bbb1e0 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bbb144 bytes af7f0294
+ 00bbb1e0 bytes bc7f0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce79b67b67826ffc0085b9f688d7bf2b"></a>

### [`00bbb3cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbb3cc.md) → [`00bbb468`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbb468.md) _ZN8firebase9messaging9SubscribeEPKc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 18件 [`00bbb69c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbb69c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)
- 新版 呼出元 0件  · 呼出先 18件 [`00bbb738`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbb738.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 94.93% / 新版 94.93%

CFGの説明率　旧版 64.00% / 新版 64.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 2件, `call_argument_candidate` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbb3f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bbb490"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bbb49c",
      "incomplete_value": true,
      "site": "00bbb49c",
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
      "definition_site": "00bbb400",
      "incomplete_value": true,
      "site": "00bbb400",
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
      "unmatched:00bbb3f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00bbb498",
      "READ",
      [
        "storage",
        "01126360",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbb4a4",
      "READ",
      [
        "storage",
        "01126370",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bbb490",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00bbb498",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbb4a4",
      "READ",
      [
        "storage",
        "01126470",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbb3f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbb3cc.md#insn-00bbb3f4) · [`00bbb400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbb3cc.md#insn-00bbb400) · [`00bbb414`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbb3cc.md#insn-00bbb414)
- 新版 [`00bbb49c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbb468.md#insn-00bbb49c) · [`00bbb4b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbb468.md#insn-00bbb4b0)

~~~diff
- 00bbb3f4 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00bbb3f4 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffb8:8"]]
- 00bbb3f4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00bbb3f4 bytes a9831bf8
- 00bbb400 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00bbb400 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bbb49c ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
+ 00bbb49c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bbb400 bytes 490300b4
+ 00bbb49c bytes 490300b4
- 00bbb414 ["INT_ADD", "register:40f0:8", ["const:bbb414:8", "const:4:8"]]
- 00bbb414 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00bbb4b0 ["INT_ADD", "register:40f0:8", ["const:bbb4b0:8", "const:4:8"]]
+ 00bbb4b0 ["CALL", null, ["callee:00c5aad0:8"]]
- 00bbb414 bytes 7b7d0294
+ 00bbb4b0 bytes 887d0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f355a18386ed3be1f78c531931458f02"></a>

### [`00bbb69c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbb69c.md) → [`00bbb738`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbb738.md) FUN_00bbb738

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00bbb3cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbb3cc.md) [`00bbd1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd1c0.md) · 呼出先 14件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bbd460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd460.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 2件 [`00bbb468`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbb468.md) [`00bbd25c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd25c.md) · 呼出先 14件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00bbd4fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd4fc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 86.49% / 新版 86.49%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbb6d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bbb76c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbb838"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbb6c8",
      "PARAM",
      [
        "storage",
        "002ae3d1",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bbb6d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00bbb778",
      "READ",
      [
        "storage",
        "01126360",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bbb764",
      "PARAM",
      [
        "storage",
        "002ae375",
        null,
        "string"
      ]
    ],
    [
      "00bbb76c",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00bbb778",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbb6d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbb69c.md#insn-00bbb6d0) · [`00bbb6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbb69c.md#insn-00bbb6d4) · [`00bbb6e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbb69c.md#insn-00bbb6e0)
- 新版 [`00bbb770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbb738.md#insn-00bbb770) · [`00bbb77c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbb738.md#insn-00bbb77c)

~~~diff
- 00bbb6d0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:38:8"]]
- 00bbb6d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bbb6d0 bytes e81f00f9
- 00bbb6d4 ["INT_ADD", "register:40f0:8", ["const:bbb6d4:8", "const:4:8"]]
- 00bbb6d4 ["CALL", null, ["callee:00c5b200:8"]]
+ 00bbb770 ["INT_ADD", "register:40f0:8", ["const:bbb770:8", "const:4:8"]]
+ 00bbb770 ["CALL", null, ["callee:00c5b200:8"]]
- 00bbb6d4 bytes 977e0294
+ 00bbb770 bytes a47e0294
- 00bbb6e0 ["INT_ADD", "register:40f0:8", ["const:bbb6e0:8", "const:4:8"]]
- 00bbb6e0 ["CALL", null, ["callee:00c5b150:8"]]
+ 00bbb77c ["INT_ADD", "register:40f0:8", ["const:bbb77c:8", "const:4:8"]]
+ 00bbb77c ["CALL", null, ["callee:00c5b150:8"]]
- 00bbb6e0 bytes 687e0294
+ 00bbb77c bytes 757e0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c0d98fb04c16480fc4fdb34cb1db428"></a>

### [`00bbb898`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbb898.md) → [`00bbb934`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbb934.md) _ZN8firebase9messaging19SubscribeLastResultEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 8件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5abe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abe0.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5acb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5acb0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, comparison, comparison_count, constant, control_flow, operands_and_dependencies, operation_sequence, store_condition

命令の説明率　旧版 97.62% / 新版 97.62%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bbb950",
      "incomplete_value": true,
      "site": "00bbb950",
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
      "definition_site": "00bbb8b4",
      "incomplete_value": true,
      "site": "00bbb8b4",
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
      "definition_site": "00bbb9a4",
      "incomplete_value": false,
      "site": "00bbb9a8",
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
            "const:8c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbb908",
      "incomplete_value": false,
      "site": "00bbb90c",
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
            "const:915:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bbb9b8",
      "incomplete_value": true,
      "site": "00bbb9c8",
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
            "const:30:8"
          ]
        ]
      ]
    },
    "old": null,
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
      "00bbb948",
      "READ",
      [
        "storage",
        "01126360",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bbb908",
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
      "00bbb948",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbb9a4",
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

- 旧版 [`00bbb8b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbb898.md#insn-00bbb8b4) · [`00bbb90c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbb898.md#insn-00bbb90c) · [`00bbb92c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbb898.md#insn-00bbb92c)
- 新版 [`00bbb950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbb934.md#insn-00bbb950) · [`00bbb9a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbb934.md#insn-00bbb9a8) · [`00bbb9c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbb934.md#insn-00bbb9c8)

~~~diff
- 00bbb8b4 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00bbb8b4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bbb950 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
+ 00bbb950 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bbb8b4 bytes 890200b4
+ 00bbb950 bytes 890200b4
- 00bbb90c ["INT_ADD", "register:40f0:8", ["const:bbb90c:8", "const:4:8"]]
- 00bbb90c ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bbb9a8 ["INT_ADD", "register:40f0:8", ["const:bbb9a8:8", "const:4:8"]]
+ 00bbb9a8 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bbb90c bytes bd7d0294
+ 00bbb9a8 bytes ca7d0294
- 00bbb92c ["INT_ADD", "register:40f0:8", ["const:bbb92c:8", "const:4:8"]]
- 00bbb92c ["CALL", null, ["callee:00c5acb0:8"]]
+ 00bbb9c8 ["INT_ADD", "register:40f0:8", ["const:bbb9c8:8", "const:4:8"]]
+ 00bbb9c8 ["CALL", null, ["callee:00c5acb0:8"]]
- 00bbb92c bytes ad7c0294
+ 00bbb9c8 bytes ba7c0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8d4128530da96956478c9ed0f11b30d"></a>

### [`00bbb970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbb970.md) → [`00bbba0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbba0c.md) _ZN8firebase9messaging11UnsubscribeEPKc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 18件 [`00bbbc40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbbc40.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md)
- 新版 呼出元 0件  · 呼出先 18件 [`00bbbcdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbbcdc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 92.75% / 新版 92.75%

CFGの説明率　旧版 13.79% / 新版 13.79%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

アドレスに依存する影響 `branch_value` 2件, `call_argument_candidate` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbb998"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbbad0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bbba34"
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
      "unmatched:00bbb998",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00bbba3c",
      "READ",
      [
        "storage",
        "01126360",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbba48",
      "READ",
      [
        "storage",
        "01126370",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bbba34",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00bbba3c",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbba48",
      "READ",
      [
        "storage",
        "01126470",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbb998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbb970.md#insn-00bbb998) · [`00bbb9a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbb970.md#insn-00bbb9a4) · [`00bbb9b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbb970.md#insn-00bbb9b8)
- 新版 [`00bbba40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbba0c.md#insn-00bbba40) · [`00bbba54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbba0c.md#insn-00bbba54)

~~~diff
- 00bbb998 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00bbb998 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffb8:8"]]
- 00bbb998 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00bbb998 bytes a9831bf8
- 00bbb9a4 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00bbb9a4 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00bbba40 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
+ 00bbba40 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bbb9a4 bytes 490300b4
+ 00bbba40 bytes 490300b4
- 00bbb9b8 ["INT_ADD", "register:40f0:8", ["const:bbb9b8:8", "const:4:8"]]
- 00bbb9b8 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00bbba54 ["INT_ADD", "register:40f0:8", ["const:bbba54:8", "const:4:8"]]
+ 00bbba54 ["CALL", null, ["callee:00c5aad0:8"]]
- 00bbb9b8 bytes 127c0294
+ 00bbba54 bytes 1f7c0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef774e060e8858a61c26dfccf7368d38"></a>

### [`00bbbc40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbbc40.md) → [`00bbbcdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbbcdc.md) FUN_00bbbcdc

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00bbb970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbb970.md) [`00bbd1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd1c0.md) · 呼出先 14件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bbd460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd460.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 2件 [`00bbba0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbba0c.md) [`00bbd25c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd25c.md) · 呼出先 14件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00bbd4fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd4fc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 90.99% / 新版 90.99%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbbc74"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bbbd10"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bbbd08",
      "incomplete_value": false,
      "site": "00bbbd14",
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
            "const:bd3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbbc6c",
      "incomplete_value": false,
      "site": "00bbbc78",
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
            "const:b93:8"
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
      "unmatched:00bbbc6c",
      "PARAM",
      [
        "storage",
        "002c0b93",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bbbc74",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00bbbd1c",
      "READ",
      [
        "storage",
        "01126360",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bbbd08",
      "PARAM",
      [
        "storage",
        "002c0bd3",
        null,
        "string"
      ]
    ],
    [
      "00bbbd10",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00bbbd1c",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbbc74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbbc40.md#insn-00bbbc74) · [`00bbbc78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbbc40.md#insn-00bbbc78) · [`00bbbc84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbbc40.md#insn-00bbbc84)
- 新版 [`00bbbd14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbbcdc.md#insn-00bbbd14) · [`00bbbd20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbbcdc.md#insn-00bbbd20)

~~~diff
- 00bbbc74 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:38:8"]]
- 00bbbc74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bbbc74 bytes e81f00f9
- 00bbbc78 ["INT_ADD", "register:40f0:8", ["const:bbbc78:8", "const:4:8"]]
- 00bbbc78 ["CALL", null, ["callee:00c5b200:8"]]
+ 00bbbd14 ["INT_ADD", "register:40f0:8", ["const:bbbd14:8", "const:4:8"]]
+ 00bbbd14 ["CALL", null, ["callee:00c5b200:8"]]
- 00bbbc78 bytes 2e7d0294
+ 00bbbd14 bytes 3b7d0294
- 00bbbc84 ["INT_ADD", "register:40f0:8", ["const:bbbc84:8", "const:4:8"]]
- 00bbbc84 ["CALL", null, ["callee:00c5b150:8"]]
+ 00bbbd20 ["INT_ADD", "register:40f0:8", ["const:bbbd20:8", "const:4:8"]]
+ 00bbbd20 ["CALL", null, ["callee:00c5b150:8"]]
- 00bbbc84 bytes ff7c0294
+ 00bbbd20 bytes 0c7d0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ccb268ef4c03666833291ce30fc360a"></a>

### [`00bbbe3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbbe3c.md) → [`00bbbed8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbbed8.md) _ZN8firebase9messaging21UnsubscribeLastResultEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 8件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5abe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abe0.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5acb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5acb0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md)

変更の種類 branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_store_alignment

命令の説明率　旧版 88.10% / 新版 88.10%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_store_alignment` 6件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbbe3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbbe3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbbe40"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbbe3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbbe40",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbbe44",
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
      "00bbbed8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bbbedc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bbbee0",
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

- 旧版 [`00bbbe3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbbe3c.md#insn-00bbbe3c) · [`00bbbe40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbbe3c.md#insn-00bbbe40) · [`00bbbe44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbbe3c.md#insn-00bbbe44)

~~~diff
- 00bbbe3c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bbbe3c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bbbe3c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bbbe3c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bbbe3c bytes f657bda9
- 00bbbe40 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bbbe40 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bbbe40 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bbbe40 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bbbe40 bytes f44f01a9
- 00bbbe44 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bbbe44 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bbbe44 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bbbe44 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bbbe44 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09a566895a11a4fe17c67bd16f1ea4b4"></a>

### [`00bbbf14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbbf14.md) → [`00bbbfb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbbfb0.md) _ZN8firebase9messaging38DeliveryMetricsExportToBigQueryEnabledEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00497a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 76.19% / 新版 76.19%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_return_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bbbfc0",
      "incomplete_value": true,
      "site": "00bbbfc0",
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
      "definition_site": "00bbbf24",
      "incomplete_value": true,
      "site": "00bbbf24",
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
      "definition_site": "00bbbfd0",
      "incomplete_value": true,
      "site": "00bbbfd8",
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
                "const:498:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbbf34",
      "incomplete_value": true,
      "site": "00bbbf3c",
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
                "const:398:8"
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
      "definition_site": "00bbbfd4",
      "incomplete_value": true,
      "site": "00bbbfd8",
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
                "const:3e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbbf38",
      "incomplete_value": true,
      "site": "00bbbf3c",
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
                "const:2e0:8"
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
      "00bbbfbc",
      "READ",
      [
        "storage",
        "01126360",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bbbf34",
      "READ",
      [
        "storage",
        "01126398",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bbbf38",
      "READ",
      [
        "storage",
        "011262e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bbbfbc",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbbfd0",
      "READ",
      [
        "storage",
        "01126498",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbbfd4",
      "READ",
      [
        "storage",
        "011263e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbbf24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbbf14.md#insn-00bbbf24) · [`00bbbf3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbbf14.md#insn-00bbbf3c) · [`00bbbf64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbbf14.md#insn-00bbbf64)
- 新版 [`00bbbfc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbbfb0.md#insn-00bbbfc0) · [`00bbbfd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbbfb0.md#insn-00bbbfd8)

~~~diff
- 00bbbf24 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00bbbf24 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bbbfc0 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00bbbfc0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bbbf24 bytes 600100b4
+ 00bbbfc0 bytes 600100b4
- 00bbbf3c ["INT_ADD", "register:40f0:8", ["const:bbbf3c:8", "const:4:8"]]
- 00bbbf3c ["CALL", null, ["callee:00497a88:8"]]
+ 00bbbfd8 ["INT_ADD", "register:40f0:8", ["const:bbbfd8:8", "const:4:8"]]
+ 00bbbfd8 ["CALL", null, ["callee:00497a88:8"]]
- 00bbbf3c bytes c36ee397
+ 00bbbfd8 bytes ac6ee397
- 00bbbf64 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bbbf64 ["RETURN", null, ["register:0:8"]]
- 00bbbf64 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9fe6bf5e7444858bf92fe1be13de09a"></a>

### [`00bbbf68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbbf68.md) → [`00bbc004`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbc004.md) _ZN8firebase9messaging34SetDeliveryMetricsExportToBigQueryEb

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md)

変更の種類 branch_value, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, store_destination, unresolved_branch_alignment

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bbc058",
      "incomplete_value": false,
      "site": "00bbc058",
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
            "const:504:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbbfbc",
      "incomplete_value": false,
      "site": "00bbbfbc",
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
            "const:404:8"
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
      "definition_site": "00bbc01c",
      "incomplete_value": true,
      "site": "00bbc01c",
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
      "definition_site": "00bbbf80",
      "incomplete_value": true,
      "site": "00bbbf80",
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
      "site": "00bbbfb4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bbc014",
      "READ",
      [
        "storage",
        "01126360",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bbbf94",
      "READ",
      [
        "storage",
        "01126398",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bbbf98",
      "READ",
      [
        "storage",
        "011262e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bbc014",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbc030",
      "READ",
      [
        "storage",
        "01126498",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbc034",
      "READ",
      [
        "storage",
        "011263e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbbfb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbbf68.md#insn-00bbbfb4) · [`00bbbfbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbbf68.md#insn-00bbbfbc)
- 新版 [`00bbc058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbc004.md#insn-00bbc058) · [`00bbc050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbc004.md#insn-00bbc050)

~~~diff
- 00bbbfb4 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00bbbfb4 ["BOOL_NEGATE", "tmp:1:1", ["register:101:1"]]
- 00bbbfb4 ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 00bbbfb4 ["INT_ADD", "tmp:0:4", ["register:4040:4", "const:1:4"]]
- 00bbbfb4 bytes 0815881a
- 00bbbfbc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:404:8"]]
- 00bbbfbc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 00bbc058 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:504:8"]]
+ 00bbc058 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00bbbfbc bytes 280504b9
+ 00bbc058 bytes 280505b9
+ 00bbc050 ["COPY", "tmp:0:4", ["register:4040:4"]]
+ 00bbc050 ["BOOL_NEGATE", "tmp:1:1", ["register:101:1"]]
+ 00bbc050 ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
+ 00bbc050 ["INT_ADD", "tmp:0:4", ["register:4040:4", "const:1:4"]]
+ 00bbc050 bytes 0815881a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-491d46596a42e90500355fd281db9eb3"></a>

### [`00bbbfd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbbfd4.md) → [`00bbc070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbc070.md) _ZN8firebase9messaging27IsRegistrationOnInitEnabledEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b080.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00497a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 55.56% / 新版 55.56%

CFGの説明率　旧版 14.29% / 新版 14.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 3件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bbc084",
      "incomplete_value": true,
      "site": "00bbc084",
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
      "definition_site": "00bbbfe8",
      "incomplete_value": true,
      "site": "00bbbfe8",
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
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbc008"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bbc0a4"
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
      "00bbc080",
      "READ",
      [
        "storage",
        "01126360",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbc084",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bbc00c"
      ]
    ],
    [
      "unmatched:00bbbff0",
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
      "00bbc080",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbc084",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bbc0a8"
      ]
    ],
    [
      "00bbc08c",
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

- 旧版 [`00bbbfe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbbfd4.md#insn-00bbbfe8) · [`00bbbff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbbfd4.md#insn-00bbbff4) · [`00bbc000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbbfd4.md#insn-00bbc000)
- 新版 [`00bbc084`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbc070.md#insn-00bbc084)

~~~diff
- 00bbbfe8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00bbbfe8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bbc084 ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00bbc084 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bbbfe8 bytes 200100b5
+ 00bbc084 bytes 200100b5
- 00bbbff4 ["INT_ADD", "register:40f0:8", ["const:bbbff4:8", "const:4:8"]]
- 00bbbff4 ["CALL", null, ["callee:00c5ad70:8"]]
- 00bbbff4 bytes 2b7b0294
- 00bbc000 ["INT_ADD", "register:40f0:8", ["const:bbc000:8", "const:4:8"]]
- 00bbc000 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bbc000 bytes 007c0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-992bc10d832ead27591a47536c8690db"></a>

### [`00bbc040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbc040.md) → [`00bbc0dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbc0dc.md) _ZN8firebase9messaging8RegisterEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 20件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bbc2a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbc2a8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md)
- 新版 呼出元 0件  · 呼出先 20件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00bbc344`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbc344.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 82.05% / 新版 82.05%

CFGの説明率　旧版 11.76% / 新版 11.76%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 9件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbc044"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbc044"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbc048"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbc044",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbc048",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbc04c",
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
      "00bbc0e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00bbc0e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bbc0e8",
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

- 旧版 [`00bbc044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbc040.md#insn-00bbc044) · [`00bbc048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbc040.md#insn-00bbc048) · [`00bbc04c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbc040.md#insn-00bbc04c)

~~~diff
- 00bbc044 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00bbc044 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00bbc044 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00bbc044 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bbc044 bytes f85f05a9
- 00bbc048 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bbc048 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bbc048 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00bbc048 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bbc048 bytes f65706a9
- 00bbc04c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bbc04c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bbc04c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00bbc04c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bbc04c bytes f44f07a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2da718675af8689604cc6f39bdc629b"></a>

### [`00bbc2a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbc2a8.md) → [`00bbc344`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbc344.md) FUN_00bbc344

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00bbc040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbc040.md) [`00bbc498`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbc498.md) [`00bbce14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbce14.md) · 呼出先 8件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5abe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abe0.md)
- 新版 呼出元 3件 [`00bbc0dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbc0dc.md) [`00bbc534`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbc534.md) [`00bbceb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbceb0.md) · 呼出先 8件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md) [`00c5acb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5acb0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 64.91% / 新版 64.91%

CFGの説明率　旧版 30.77% / 新版 30.77%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbc2ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbc2b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbc2b0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbc2ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbc2b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbc2b4",
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
      "00bbc348",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00bbc34c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bbc350",
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

- 旧版 [`00bbc2ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbc2a8.md#insn-00bbc2ac) · [`00bbc2b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbc2a8.md#insn-00bbc2b0) · [`00bbc2b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbc2a8.md#insn-00bbc2b4)

~~~diff
- 00bbc2ac ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00bbc2ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 00bbc2ac bytes f71300f9
- 00bbc2b0 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bbc2b0 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bbc2b0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00bbc2b0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bbc2b0 bytes f65703a9
- 00bbc2b4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bbc2b4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bbc2b4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00bbc2b4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bbc2b4 bytes f44f04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6846c4e94aafbb14f0790a19dea9fca5"></a>

### [`00bbc3c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbc3c0.md) → [`00bbc45c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbc45c.md) _ZN8firebase9messaging18RegisterLastResultEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 8件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5abe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abe0.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5acb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5acb0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md)

変更の種類 branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence, store_condition

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bbc478",
      "incomplete_value": true,
      "site": "00bbc478",
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
      "definition_site": "00bbc3dc",
      "incomplete_value": true,
      "site": "00bbc3dc",
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
      "definition_site": "00bbc488",
      "incomplete_value": true,
      "site": "00bbc48c",
      "value": [
        "live",
        "register:40a8:8"
      ]
    },
    "old": {
      "definition_site": "00bbc3ec",
      "incomplete_value": true,
      "site": "00bbc3f0",
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
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bbc4b0",
      "incomplete_value": true,
      "site": "00bbc4b4",
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
            "const:30:8"
          ]
        ]
      ]
    },
    "old": null,
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
      "00bbc470",
      "READ",
      [
        "storage",
        "01126360",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bbc430",
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
      "00bbc470",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbc4cc",
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

- 旧版 [`00bbc3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbc3c0.md#insn-00bbc3f0) · [`00bbc418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbc3c0.md#insn-00bbc418) · [`00bbc434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbc3c0.md#insn-00bbc434)
- 新版 [`00bbc48c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbc45c.md#insn-00bbc48c) · [`00bbc4b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbc45c.md#insn-00bbc4b4) · [`00bbc4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbc45c.md#insn-00bbc4d0)

~~~diff
- 00bbc3f0 ["INT_ADD", "register:40f0:8", ["const:bbc3f0:8", "const:4:8"]]
- 00bbc3f0 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00bbc48c ["INT_ADD", "register:40f0:8", ["const:bbc48c:8", "const:4:8"]]
+ 00bbc48c ["CALL", null, ["callee:00c5aad0:8"]]
- 00bbc3f0 bytes 84790294
+ 00bbc48c bytes 91790294
- 00bbc418 ["INT_ADD", "register:40f0:8", ["const:bbc418:8", "const:4:8"]]
- 00bbc418 ["CALL", null, ["callee:00c5aee0:8"]]
+ 00bbc4b4 ["INT_ADD", "register:40f0:8", ["const:bbc4b4:8", "const:4:8"]]
+ 00bbc4b4 ["CALL", null, ["callee:00c5aee0:8"]]
- 00bbc418 bytes 7e7a0294
+ 00bbc4b4 bytes 8b7a0294
- 00bbc434 ["INT_ADD", "register:40f0:8", ["const:bbc434:8", "const:4:8"]]
- 00bbc434 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bbc4d0 ["INT_ADD", "register:40f0:8", ["const:bbc4d0:8", "const:4:8"]]
+ 00bbc4d0 ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bbc434 bytes f37a0294
+ 00bbc4d0 bytes 007b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70ff4b1441e317e2a0f52c9c28108dbd"></a>

### [`00bbc498`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbc498.md) → [`00bbc534`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbc534.md) _ZN8firebase9messaging10UnregisterEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 20件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bbc2a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbc2a8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md)
- 新版 呼出元 0件  · 呼出先 20件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00bbc344`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbc344.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 43.75% / 新版 43.75%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `store_condition` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbc4c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbc550"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bbc564"
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
      "unmatched:00bbc4c4",
      "READ",
      [
        "storage",
        "01126360",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bbc4c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bbc634"
      ]
    ],
    [
      "unmatched:00bbc4d0",
      "READ",
      [
        "storage",
        "01126370",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bbc560",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbc564",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bbc634"
      ]
    ],
    [
      "00bbc56c",
      "READ",
      [
        "storage",
        "01126470",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbc4c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbc498.md#insn-00bbc4c8) · [`00bbc4d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbc498.md#insn-00bbc4d8) · [`00bbc500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbc498.md#insn-00bbc500)
- 新版 [`00bbc574`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbc534.md#insn-00bbc574) · [`00bbc59c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbc534.md#insn-00bbc59c)

~~~diff
- 00bbc4c8 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00bbc4c8 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00bbc4c8 bytes 890600b4
- 00bbc4d8 ["INT_ADD", "register:40f0:8", ["const:bbc4d8:8", "const:4:8"]]
- 00bbc4d8 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00bbc574 ["INT_ADD", "register:40f0:8", ["const:bbc574:8", "const:4:8"]]
+ 00bbc574 ["CALL", null, ["callee:00c5aad0:8"]]
- 00bbc4d8 bytes 4a790294
+ 00bbc574 bytes 57790294
- 00bbc500 ["INT_ADD", "register:40f0:8", ["const:bbc500:8", "const:4:8"]]
- 00bbc500 ["CALL", null, ["callee:00c5aed0:8"]]
+ 00bbc59c ["INT_ADD", "register:40f0:8", ["const:bbc59c:8", "const:4:8"]]
+ 00bbc59c ["CALL", null, ["callee:00c5aed0:8"]]
- 00bbc500 bytes 407a0294
+ 00bbc59c bytes 4d7a0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0cefb39cdb99592c96fcc423741b7e17"></a>

### [`00bbc700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbc700.md) → [`00bbc79c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbc79c.md) _ZN8firebase9messaging20UnregisterLastResultEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 8件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5abe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abe0.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5acb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5acb0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 51.72% / 新版 45.45%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_condition` 2件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbc700"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbc700"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbc704"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbc700",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbc704",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbc708",
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
      "00bbc79c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bbc7a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bbc7a4",
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

- 旧版 [`00bbc700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbc700.md#insn-00bbc700) · [`00bbc704`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbc700.md#insn-00bbc704) · [`00bbc708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbc700.md#insn-00bbc708)

~~~diff
- 00bbc700 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bbc700 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bbc700 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bbc700 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bbc700 bytes f657bda9
- 00bbc704 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bbc704 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bbc704 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bbc704 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bbc704 bytes f44f01a9
- 00bbc708 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bbc708 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bbc708 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bbc708 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bbc708 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2aa52cff0d4af9ce27ad7b46a8de201"></a>

### [`00bbc7d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbc7d8.md) → [`00bbc874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbc874.md) _ZN8firebase9messaging8GetTokenEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d5c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d5c0.md) · 呼出先 22件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00b43fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b43/00b43fb8.md) [`00bbcab4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbcab4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00c5d690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d690.md) · 呼出先 22件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00b44054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44054.md) [`00bbcb50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbcb50.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 78.68% / 新版 78.68%

CFGの説明率　旧版 8.33% / 新版 8.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 14件, `store_condition` 4件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 10件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbc7dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbc7e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbc7e0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbc7dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbc7e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbc7e4",
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
      "00bbc878",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00bbc87c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00bbc880",
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

- 旧版 [`00bbc7dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbc7d8.md#insn-00bbc7dc) · [`00bbc7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbc7d8.md#insn-00bbc7e0) · [`00bbc7e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbc7d8.md#insn-00bbc7e4)

~~~diff
- 00bbc7dc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:60:8"]]
- 00bbc7dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 00bbc7dc bytes f93300f9
- 00bbc7e0 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00bbc7e0 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00bbc7e0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00bbc7e0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bbc7e0 bytes f85f07a9
- 00bbc7e4 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bbc7e4 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bbc7e4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 00bbc7e4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bbc7e4 bytes f65708a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39a10b2848cc68153a76d1cce5b7f345"></a>

### [`00bbcab4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbcab4.md) → [`00bbcb50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbcb50.md) FUN_00bbcb50

採用 · 移動量 `+0x9c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bbc7d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbc7d8.md) · 呼出先 15件 [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`00bbc874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbc874.md) · 呼出先 15件 [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 93.92% / 新版 93.92%

CFGの説明率　旧版 50.98% / 新版 54.17%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_condition` 4件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbcc38"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bbccd4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bbcb84",
      "incomplete_value": false,
      "site": "00bbcb9c",
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
      "definition_site": "00bbcae8",
      "incomplete_value": false,
      "site": "00bbcb00",
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
      "00bbcb84",
      "PARAM",
      [
        "storage",
        "002a63ea",
        null,
        "undefined1"
      ]
    ],
    [
      "00bbcc04",
      "PARAM",
      [
        "storage",
        "01126280",
        null,
        null
      ]
    ],
    [
      "00bbcc58",
      "PARAM",
      [
        "storage",
        "002ac195",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bbcb84",
      "PARAM",
      [
        "storage",
        "002a638e",
        null,
        "undefined1"
      ]
    ],
    [
      "00bbcc04",
      "PARAM",
      [
        "storage",
        "01126380",
        null,
        null
      ]
    ],
    [
      "00bbcc58",
      "PARAM",
      [
        "storage",
        "002ac139",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbcb00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbcab4.md#insn-00bbcb00) · [`00bbcb44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbcab4.md#insn-00bbcb44) · [`00bbcb6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbcab4.md#insn-00bbcb6c)
- 新版 [`00bbcb9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbcb50.md#insn-00bbcb9c) · [`00bbcbe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbcb50.md#insn-00bbcbe0) · [`00bbcc08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbcb50.md#insn-00bbcc08)

~~~diff
- 00bbcb00 ["INT_ADD", "register:40f0:8", ["const:bbcb00:8", "const:4:8"]]
- 00bbcb00 ["CALL", null, ["callee:00c5b690:8"]]
+ 00bbcb9c ["INT_ADD", "register:40f0:8", ["const:bbcb9c:8", "const:4:8"]]
+ 00bbcb9c ["CALL", null, ["callee:00c5b690:8"]]
- 00bbcb00 bytes b07a0294
+ 00bbcb9c bytes bd7a0294
- 00bbcb44 ["INT_ADD", "register:40f0:8", ["const:bbcb44:8", "const:4:8"]]
- 00bbcb44 ["CALL", null, ["callee:00c57f80:8"]]
+ 00bbcbe0 ["INT_ADD", "register:40f0:8", ["const:bbcbe0:8", "const:4:8"]]
+ 00bbcbe0 ["CALL", null, ["callee:00c57f80:8"]]
- 00bbcb44 bytes db6c0294
+ 00bbcbe0 bytes e86c0294
- 00bbcb6c ["INT_ADD", "register:40f0:8", ["const:bbcb6c:8", "const:4:8"]]
- 00bbcb6c ["CALL", null, ["callee:00c5aad0:8"]]
+ 00bbcc08 ["INT_ADD", "register:40f0:8", ["const:bbcc08:8", "const:4:8"]]
+ 00bbcc08 ["CALL", null, ["callee:00c5aad0:8"]]
- 00bbcb6c bytes a5770294
+ 00bbcc08 bytes b2770294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d1a90df260122044b5f3a7087af8a26"></a>

### [`00bbcd3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbcd3c.md) → [`00bbcdd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbcdd8.md) _ZN8firebase9messaging18GetTokenLastResultEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 8件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5abe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abe0.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5acb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5acb0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_return_alignment

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_return_alignment` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bbcdf4",
      "incomplete_value": true,
      "site": "00bbcdf4",
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
      "definition_site": "00bbcd58",
      "incomplete_value": true,
      "site": "00bbcd58",
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
      "definition_site": "00bbcdac",
      "incomplete_value": false,
      "site": "00bbcdb0",
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
            "const:915:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00bbcdc8",
      "incomplete_value": false,
      "site": "00bbcdd0",
      "value": [
        "leaf",
        "const:0:8"
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
      "00bbcdec",
      "READ",
      [
        "storage",
        "01126360",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00bbcdac",
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
      "00bbcdec",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbce48",
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

- 旧版 [`00bbcd58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbcd3c.md#insn-00bbcd58) · [`00bbcdb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbcd3c.md#insn-00bbcdb0) · [`00bbcdd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbcd3c.md#insn-00bbcdd0)
- 新版 [`00bbcdf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbcdd8.md#insn-00bbcdf4) · [`00bbce4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbcdd8.md#insn-00bbce4c) · [`00bbce6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbcdd8.md#insn-00bbce6c)

~~~diff
- 00bbcd58 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00bbcd58 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bbcdf4 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
+ 00bbcdf4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bbcd58 bytes 890200b4
+ 00bbcdf4 bytes 890200b4
- 00bbcdb0 ["INT_ADD", "register:40f0:8", ["const:bbcdb0:8", "const:4:8"]]
- 00bbcdb0 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bbce4c ["INT_ADD", "register:40f0:8", ["const:bbce4c:8", "const:4:8"]]
+ 00bbce4c ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bbcdb0 bytes 94780294
+ 00bbce4c bytes a1780294
- 00bbcdd0 ["INT_ADD", "register:40f0:8", ["const:bbcdd0:8", "const:4:8"]]
- 00bbcdd0 ["CALL", null, ["callee:00c5acb0:8"]]
+ 00bbce6c ["INT_ADD", "register:40f0:8", ["const:bbce6c:8", "const:4:8"]]
+ 00bbce6c ["CALL", null, ["callee:00c5acb0:8"]]
- 00bbcdd0 bytes 84770294
+ 00bbce6c bytes 91770294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99ae576ef2523ab2cf55661e31ec796c"></a>

### [`00bbce14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbce14.md) → [`00bbceb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbceb0.md) _ZN8firebase9messaging11DeleteTokenEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 20件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00bbc2a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbc2a8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md)
- 新版 呼出元 0件  · 呼出先 20件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00bbc344`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbc344.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 80.34% / 新版 80.34%

CFGの説明率　旧版 32.14% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbce18"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbce18"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbce1c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbce18",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbce1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbce20",
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
      "00bbceb4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00bbceb8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bbcebc",
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

- 旧版 [`00bbce18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbce14.md#insn-00bbce18) · [`00bbce1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbce14.md#insn-00bbce1c) · [`00bbce20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbc/00bbce14.md#insn-00bbce20)

~~~diff
- 00bbce18 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00bbce18 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00bbce18 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00bbce18 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bbce18 bytes f85f05a9
- 00bbce1c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bbce1c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bbce1c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00bbce1c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bbce1c bytes f65706a9
- 00bbce20 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bbce20 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bbce20 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00bbce20 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bbce20 bytes f44f07a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-404fb2e8178850c86edbcc682c742991"></a>

### [`00bbd07c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd07c.md) → [`00bbd118`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd118.md) _ZN8firebase9messaging21DeleteTokenLastResultEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5abe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abe0.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5acb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5acb0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 97.62% / 新版 97.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bbd134",
      "incomplete_value": true,
      "site": "00bbd134",
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
      "definition_site": "00bbd098",
      "incomplete_value": true,
      "site": "00bbd098",
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
      "definition_site": "00bbd188",
      "incomplete_value": false,
      "site": "00bbd18c",
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
            "const:8c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbd0ec",
      "incomplete_value": false,
      "site": "00bbd0f0",
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
            "const:915:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00bbd098"
      ],
      [
        "FALL_THROUGH",
        "00bbd134"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00bbd134",
      "incomplete_value": true,
      "site": "00bbd168",
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
      "definition_site": "00bbd098",
      "incomplete_value": true,
      "site": "00bbd0cc",
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
      "00bbd12c",
      "READ",
      [
        "storage",
        "01126360",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbd188",
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
      "00bbd12c",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbd188",
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

- 旧版 [`00bbd0f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd07c.md#insn-00bbd0f0) · [`00bbd090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd07c.md#insn-00bbd090) · [`00bbd09c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd07c.md#insn-00bbd09c)
- 新版 [`00bbd18c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd118.md#insn-00bbd18c) · [`00bbd12c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd118.md#insn-00bbd12c) · [`00bbd138`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd118.md#insn-00bbd138)

~~~diff
- 00bbd0f0 ["INT_ADD", "register:40f0:8", ["const:bbd0f0:8", "const:4:8"]]
- 00bbd0f0 ["CALL", null, ["callee:00c5b0d0:8"]]
+ 00bbd18c ["INT_ADD", "register:40f0:8", ["const:bbd18c:8", "const:4:8"]]
+ 00bbd18c ["CALL", null, ["callee:00c5b0d0:8"]]
- 00bbd0f0 bytes c4770294
+ 00bbd18c bytes d1770294
- 00bbd090 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:360:8"]]
- 00bbd090 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bbd12c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:460:8"]]
+ 00bbd12c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00bbd090 bytes 29b141f9
+ 00bbd12c bytes 293142f9
- 00bbd09c ["INT_ADD", "register:40f0:8", ["const:bbd09c:8", "const:4:8"]]
- 00bbd09c ["CALL", null, ["callee:00c5d340:8"]]
+ 00bbd138 ["INT_ADD", "register:40f0:8", ["const:bbd138:8", "const:4:8"]]
+ 00bbd138 ["CALL", null, ["callee:00c5d340:8"]]
- 00bbd09c bytes 75800294
+ 00bbd138 bytes 82800294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-107d06e61fe345224605f562d09066c7"></a>

### [`00bbd158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd158.md) → [`00bbd1f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd1f4.md) FUN_00bbd1f4

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bb9a14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9a14.md) · 呼出先 4件 [`00bbd1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd1c0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5d3b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d3b0.md)
- 新版 呼出元 1件 [`00bb9ab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9ab0.md) · 呼出先 4件 [`00bbd25c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd25c.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5d480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d480.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bbd220",
      "incomplete_value": false,
      "site": "00bbd220",
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
            "const:508:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbd184",
      "incomplete_value": false,
      "site": "00bbd184",
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
            "const:408:8"
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
      "definition_site": "00bbd20c",
      "incomplete_value": true,
      "site": "00bbd20c",
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
      "definition_site": "00bbd170",
      "incomplete_value": true,
      "site": "00bbd170",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00bbd170"
      ],
      [
        "FALL_THROUGH",
        "00bbd20c"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00bbd20c",
      "incomplete_value": true,
      "site": "00bbd220",
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
      "definition_site": "00bbd170",
      "incomplete_value": true,
      "site": "00bbd184",
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
    "ordinal": 4,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bbd204",
      "READ",
      [
        "storage",
        "01126370",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbd220",
      "WRITE",
      [
        "storage",
        "01126408",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bbd204",
      "READ",
      [
        "storage",
        "01126470",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbd220",
      "WRITE",
      [
        "storage",
        "01126508",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbd184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd158.md#insn-00bbd184) · [`00bbd168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd158.md#insn-00bbd168) · [`00bbd178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd158.md#insn-00bbd178)
- 新版 [`00bbd220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd1f4.md#insn-00bbd220) · [`00bbd204`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd1f4.md#insn-00bbd204) · [`00bbd214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd1f4.md#insn-00bbd214)

~~~diff
- 00bbd184 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00bbd184 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:408:8"]]
- 00bbd184 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bbd220 ["COPY", "tmp:0:4", ["register:4048:4"]]
+ 00bbd220 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:508:8"]]
+ 00bbd220 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bbd184 bytes 09211039
+ 00bbd220 bytes 09211439
- 00bbd168 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:370:8"]]
- 00bbd168 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bbd204 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:470:8"]]
+ 00bbd204 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00bbd168 bytes 14b941f9
+ 00bbd204 bytes 143942f9
- 00bbd178 ["INT_ADD", "register:40f0:8", ["const:bbd178:8", "const:4:8"]]
- 00bbd178 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00bbd214 ["INT_ADD", "register:40f0:8", ["const:bbd214:8", "const:4:8"]]
+ 00bbd214 ["CALL", null, ["callee:00c5aad0:8"]]
- 00bbd178 bytes 22760294
+ 00bbd214 bytes 2f760294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-800eec2127b4a33b06d25c4593c02909"></a>

### [`00bbd1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd1c0.md) → [`00bbd25c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd25c.md) FUN_00bbd25c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00bbd158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd158.md) [`00bbd308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd308.md) [`00bbd398`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd398.md) · 呼出先 4件 [`00bbb69c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbb69c.md) [`00bbbc40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbbc40.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md)
- 新版 呼出元 3件 [`00bbd1f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd1f4.md) [`00bbd3a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd3a4.md) [`00bbd434`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd434.md) · 呼出先 4件 [`00bbb738`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbb738.md) [`00bbbcdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbbcdc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 43.90% / 新版 43.90%

CFGの説明率　旧版 13.33% / 新版 13.04%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 10件, `unresolved_call_alignment` 4件

アドレスに依存する影響 `branch_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bbd274",
      "incomplete_value": true,
      "site": "00bbd274",
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
      "definition_site": "00bbd1d8",
      "incomplete_value": true,
      "site": "00bbd1d8",
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
      "site": "00bbd20c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbd214"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bbd270",
      "READ",
      [
        "storage",
        "01126378",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbd284",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bbd210"
      ]
    ],
    [
      "unmatched:00bbd1fc",
      "READ",
      [
        "storage",
        "01126378",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bbd270",
      "READ",
      [
        "storage",
        "01126478",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbd284",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bbd2ac"
      ]
    ],
    [
      "00bbd298",
      "READ",
      [
        "storage",
        "01126478",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbd1d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd1c0.md#insn-00bbd1d8) · [`00bbd20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd1c0.md#insn-00bbd20c) · [`00bbd214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd1c0.md#insn-00bbd214)
- 新版 [`00bbd274`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd25c.md#insn-00bbd274)

~~~diff
- 00bbd1d8 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 00bbd1d8 ["CBRANCH", null, ["local:b16:8", "tmp:0:1"]]
+ 00bbd274 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
+ 00bbd274 ["CBRANCH", null, ["local:b17:8", "tmp:0:1"]]
- 00bbd1d8 bytes 740400b4
+ 00bbd274 bytes 740400b4
- 00bbd20c ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
- 00bbd20c bytes a0000054
- 00bbd214 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00bbd214 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00bbd214 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00bbd214 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 00bbd214 bytes e8fe0736
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5baaedb21bfb9026ee1a8b76325b19c3"></a>

### [`00bbd308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd308.md) → [`00bbd3a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd3a4.md) FUN_00bbd3a4

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bb9a14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb9/00bb9a14.md) · 呼出先 4件 [`00bbd1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd1c0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5d3c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d3c0.md)
- 新版 呼出元 1件 [`00bb9ab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9ab0.md) · 呼出先 4件 [`00bbd25c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd25c.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5d490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d490.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bbd3d0",
      "incomplete_value": false,
      "site": "00bbd3d0",
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
            "const:508:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbd334",
      "incomplete_value": false,
      "site": "00bbd334",
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
            "const:408:8"
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
      "definition_site": "00bbd3bc",
      "incomplete_value": true,
      "site": "00bbd3bc",
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
      "definition_site": "00bbd320",
      "incomplete_value": true,
      "site": "00bbd320",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00bbd320"
      ],
      [
        "FALL_THROUGH",
        "00bbd3bc"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00bbd3bc",
      "incomplete_value": true,
      "site": "00bbd3d0",
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
      "definition_site": "00bbd320",
      "incomplete_value": true,
      "site": "00bbd334",
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
    "ordinal": 4,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bbd3b4",
      "READ",
      [
        "storage",
        "01126370",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbd3d0",
      "WRITE",
      [
        "storage",
        "01126408",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bbd3b4",
      "READ",
      [
        "storage",
        "01126470",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbd3d0",
      "WRITE",
      [
        "storage",
        "01126508",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbd334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd308.md#insn-00bbd334) · [`00bbd318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd308.md#insn-00bbd318) · [`00bbd328`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd308.md#insn-00bbd328)
- 新版 [`00bbd3d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd3a4.md#insn-00bbd3d0) · [`00bbd3b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd3a4.md#insn-00bbd3b4) · [`00bbd3c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd3a4.md#insn-00bbd3c4)

~~~diff
- 00bbd334 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00bbd334 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:408:8"]]
- 00bbd334 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bbd3d0 ["COPY", "tmp:0:4", ["register:4048:4"]]
+ 00bbd3d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:508:8"]]
+ 00bbd3d0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bbd334 bytes 09211039
+ 00bbd3d0 bytes 09211439
- 00bbd318 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:370:8"]]
- 00bbd318 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bbd3b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:470:8"]]
+ 00bbd3b4 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00bbd318 bytes 14b941f9
+ 00bbd3b4 bytes 143942f9
- 00bbd328 ["INT_ADD", "register:40f0:8", ["const:bbd328:8", "const:4:8"]]
- 00bbd328 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00bbd3c4 ["INT_ADD", "register:40f0:8", ["const:bbd3c4:8", "const:4:8"]]
+ 00bbd3c4 ["CALL", null, ["callee:00c5aad0:8"]]
- 00bbd328 bytes b6750294
+ 00bbd3c4 bytes c3750294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c065a3f1e4a70126713660334b1602c6"></a>

### [`00bbd374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd374.md) → [`00bbd410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd410.md) _ZN8firebase6detail33TypedCompletionCallbackTrampolineINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEvRKNS_10FutureBa

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`00bbaf50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bba/00bbaf50.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00bbafec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbafec.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 75.00% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bbd374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd374.md#insn-00bbd374) · [`00bbd37c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd374.md#insn-00bbd37c)
- 新版 [`00bbd410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd410.md#insn-00bbd410) · [`00bbd418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd410.md#insn-00bbd418)

~~~diff
- 00bbd374 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bbd374 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bbd410 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00bbd410 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bbd374 bytes a10000b4
+ 00bbd410 bytes a10000b4
- 00bbd37c ["INT_EQUAL", "tmp:0:1", ["register:4010:8", "const:0:8"]]
- 00bbd37c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bbd418 ["INT_EQUAL", "tmp:0:1", ["register:4010:8", "const:0:8"]]
+ 00bbd418 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bbd37c bytes 620000b4
+ 00bbd418 bytes 620000b4
~~~


<a id="compare-1b5b4c88ee3492b874725ca62d2c72ca"></a>

### [`00bbd51c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd51c.md) → [`00bbd5b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd5b8.md) _ZNSt6__ndk16vectorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN8firebase16SafeFutureHandleIvEEEENS5_ISB_EEE21__push

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5d5d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d5d0.md) · 呼出先 5件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5ad10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad10.md) [`00c5bc60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bc60.md)
- 新版 呼出元 1件 [`00c5d6a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d6a0.md) · 呼出先 5件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md) [`00c5ade0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ade0.md) [`00c5bd30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bd30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 40.00% / 新版 36.36%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbd608"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbd60c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbd610"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbd658",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bbd714"
      ]
    ]
  ],
  "added": [
    [
      "00bbd6f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bbd714"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbd608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd51c.md#insn-00bbd608) · [`00bbd60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd51c.md#insn-00bbd60c) · [`00bbd610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd51c.md#insn-00bbd610)

~~~diff
- 00bbd608 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00bbd608 ["INT_ADD", "tmp:1:8", ["register:4050:8", "const:ffffffffffffffe8:8"]]
- 00bbd608 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00bbd608 bytes 49811ef8
- 00bbd60c ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:ffffffffffffffd8:8"]]
- 00bbd60c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00bbd60c bytes 40819d3c
- 00bbd610 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00bbd610 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bbd610 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00bbd610 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00bbd610 bytes 1f7d3ea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-170f79042fd80ad4ede9a3859f6a2e9b"></a>

### [`00bbd6c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd6c0.md) → [`00bbd75c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd75c.md) _INIT_286

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00b65510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65510.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c5ac80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00b655ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b655ac.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c5ad50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad50.md)

変更の種類 call, call_argument_candidate, call_count, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 48.28% / 新版 48.28%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbd6c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbd6c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbd6c8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbd6c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbd6c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbd6dc",
      "PARAM",
      [
        "storage",
        "01126258",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bbd760",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bbd764",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bbd778",
      "PARAM",
      [
        "storage",
        "01126358",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbd6c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd6c0.md#insn-00bbd6c4) · [`00bbd6c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd6c0.md#insn-00bbd6c8) · [`00bbd6e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd6c0.md#insn-00bbd6e0)
- 新版 [`00bbd77c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd75c.md#insn-00bbd77c)

~~~diff
- 00bbd6c4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bbd6c4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bbd6c4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bbd6c4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bbd6c4 bytes f44f01a9
- 00bbd6c8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bbd6c8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bbd6c8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bbd6c8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bbd6c8 bytes fd7b02a9
- 00bbd6e0 ["INT_ADD", "register:40f0:8", ["const:bbd6e0:8", "const:4:8"]]
- 00bbd6e0 ["CALL", null, ["callee:00c5ad50:8"]]
+ 00bbd77c ["INT_ADD", "register:40f0:8", ["const:bbd77c:8", "const:4:8"]]
+ 00bbd77c ["CALL", null, ["callee:00c5ad50:8"]]
- 00bbd6e0 bytes 68750294
+ 00bbd77c bytes 75750294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

