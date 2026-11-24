# v16.0.1 → v16.0.2 · 最優先の変更候補 (2)

[一覧の目次](README.md)

<a id="compare-e52cc66faee2db6f22d5edadd9337a93"></a>

### [`0044b844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b844.md) → [`0044b884`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b884.md) FUN_0044b884

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0043dfb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043dfb0.md) [`00458af0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/00458af0.md) [`0097f894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097f/0097f894.md) · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 3件 [`0043dff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043dff0.md) [`00458b30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00458/00458b30.md) [`0097f8e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0097f/0097f8e8.md) · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044b8a8",
      "incomplete_value": true,
      "site": "0044b8c0",
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
                "const:cf0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044b868",
      "incomplete_value": true,
      "site": "0044b880",
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
                "const:cb0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044b8b4",
      "incomplete_value": true,
      "site": "0044b8c4",
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
                "const:2b5000:8"
              ],
              [
                "leaf",
                "const:e4e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044b874",
      "incomplete_value": true,
      "site": "0044b884",
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
                "const:2b5000:8"
              ],
              [
                "leaf",
                "const:e0e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044b8b4",
      "incomplete_value": true,
      "site": "0044b8c4",
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
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044b874",
      "incomplete_value": true,
      "site": "0044b884",
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
                "const:10:8"
              ]
            ]
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
      "0044b8a8",
      "READ",
      [
        "storage",
        "002c2cb0",
        null,
        null
      ]
    ],
    [
      "0044b8b4",
      "READ",
      [
        "storage",
        "002b5e0e",
        null,
        "string"
      ]
    ],
    [
      "0044b8b4",
      "READ",
      [
        "storage",
        "002b5e1e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044b8a8",
      "READ",
      [
        "storage",
        "002c2cf0",
        null,
        null
      ]
    ],
    [
      "0044b8b4",
      "READ",
      [
        "storage",
        "002b5e4e",
        null,
        "string"
      ]
    ],
    [
      "0044b8b4",
      "READ",
      [
        "storage",
        "002b5e5e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044b858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b844.md#insn-0044b858) · [`0044b868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b844.md#insn-0044b868) · [`0044b86c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b844.md#insn-0044b86c)
- 新版 [`0044b898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b884.md#insn-0044b898) · [`0044b8a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b884.md#insn-0044b8a8)

~~~diff
- 0044b858 ["INT_ADD", "register:40f0:8", ["const:44b858:8", "const:4:8"]]
- 0044b858 ["CALL", null, ["callee:00c57f60:8"]]
+ 0044b898 ["INT_ADD", "register:40f0:8", ["const:44b898:8", "const:4:8"]]
+ 0044b898 ["CALL", null, ["callee:00c57f60:8"]]
- 0044b858 bytes 8e312094
+ 0044b898 bytes b2312094
- 0044b868 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cb0:8"]]
- 0044b868 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
- 0044b868 ["COPY", "register:5010:8", ["const:0:8"]]
- 0044b868 ["COPY", "register:5018:8", ["const:0:8"]]
+ 0044b8a8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cf0:8"]]
+ 0044b8a8 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
+ 0044b8a8 ["COPY", "register:5010:8", ["const:0:8"]]
+ 0044b8a8 ["COPY", "register:5018:8", ["const:0:8"]]
- 0044b868 bytes 002dc33d
+ 0044b8a8 bytes 003dc33d
- 0044b86c ["COPY", "register:4040:8", ["const:2b5000:8"]]
- 0044b86c bytes 48f3ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f139b424f7559694b53f80d8451b1dff"></a>

### [`0044b898`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b898.md) → [`0044b8d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b8d8.md) FUN_0044b8d8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0043c258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043c/0043c258.md) [`0043ec60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043ec60.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md)
- 新版 呼出元 2件 [`0043c298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043c/0043c298.md) [`0043eca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043eca0.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 89.19% / 新版 89.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044b8f4",
      "incomplete_value": false,
      "site": "0044b90c",
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
            "const:e73:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044b8b4",
      "incomplete_value": false,
      "site": "0044b8cc",
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
            "const:e33:8"
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
      "definition_site": "0044b900",
      "incomplete_value": false,
      "site": "0044b90c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca4000:8"
          ],
          [
            "leaf",
            "const:b68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044b8c0",
      "incomplete_value": false,
      "site": "0044b8cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca4000:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044b914",
      "incomplete_value": false,
      "site": "0044b91c",
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
            "const:5a9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044b8d4",
      "incomplete_value": false,
      "site": "0044b8dc",
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
            "const:605:8"
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
      "0044b8f4",
      "PARAM",
      [
        "storage",
        "002b5e33",
        null,
        "string"
      ]
    ],
    [
      "0044b900",
      "PARAM",
      [
        "storage",
        "00ca4a68",
        null,
        "undefined2"
      ]
    ],
    [
      "0044b914",
      "PARAM",
      [
        "storage",
        "002a7605",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044b8f4",
      "PARAM",
      [
        "storage",
        "002b5e73",
        null,
        "string"
      ]
    ],
    [
      "0044b900",
      "PARAM",
      [
        "storage",
        "00ca4b68",
        null,
        "undefined2"
      ]
    ],
    [
      "0044b914",
      "PARAM",
      [
        "storage",
        "002a75a9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044b8cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b898.md#insn-0044b8cc) · [`0044b8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b898.md#insn-0044b8dc) · [`0044b8b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b898.md#insn-0044b8b4)
- 新版 [`0044b90c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b8d8.md#insn-0044b90c) · [`0044b91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b8d8.md#insn-0044b91c) · [`0044b8f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b8d8.md#insn-0044b8f4)

~~~diff
- 0044b8cc ["INT_ADD", "register:40f0:8", ["const:44b8cc:8", "const:4:8"]]
- 0044b8cc ["CALL", null, ["callee:00c58180:8"]]
+ 0044b90c ["INT_ADD", "register:40f0:8", ["const:44b90c:8", "const:4:8"]]
+ 0044b90c ["CALL", null, ["callee:00c58180:8"]]
- 0044b8cc bytes f9312094
+ 0044b90c bytes 1d322094
- 0044b8dc ["INT_ADD", "register:40f0:8", ["const:44b8dc:8", "const:4:8"]]
- 0044b8dc ["CALL", null, ["callee:00c58040:8"]]
+ 0044b91c ["INT_ADD", "register:40f0:8", ["const:44b91c:8", "const:4:8"]]
+ 0044b91c ["CALL", null, ["callee:00c58040:8"]]
- 0044b8dc bytes a5312094
+ 0044b91c bytes c9312094
- 0044b8b4 ["COPY", "tmp:0:8", ["const:e33:8"]]
- 0044b8b4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0044b8b4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0044b8b4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0044b8f4 ["COPY", "tmp:0:8", ["const:e73:8"]]
+ 0044b8f4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0044b8f4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0044b8f4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0044b8b4 bytes 00cc3891
+ 0044b8f4 bytes 00cc3991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e80d8667fef4b783f1ea5e46698818a2"></a>

### [`0044b958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b958.md) → [`0044b998`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b998.md) FUN_0044b998

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00458af0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/00458af0.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md)
- 新版 呼出元 1件 [`00458b30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00458/00458b30.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 89.19% / 新版 89.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044b9b4",
      "incomplete_value": false,
      "site": "0044b9cc",
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
            "const:3b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044b974",
      "incomplete_value": false,
      "site": "0044b98c",
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
            "const:414:8"
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
      "definition_site": "0044b9c0",
      "incomplete_value": false,
      "site": "0044b9cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca4000:8"
          ],
          [
            "leaf",
            "const:b68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044b980",
      "incomplete_value": false,
      "site": "0044b98c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca4000:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044b9d4",
      "incomplete_value": false,
      "site": "0044b9dc",
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
            "const:8f3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044b994",
      "incomplete_value": false,
      "site": "0044b99c",
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
            "const:94f:8"
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
      "0044b9b4",
      "PARAM",
      [
        "storage",
        "002a6414",
        null,
        "string"
      ]
    ],
    [
      "0044b9c0",
      "PARAM",
      [
        "storage",
        "00ca4a68",
        null,
        "undefined2"
      ]
    ],
    [
      "0044b9d4",
      "PARAM",
      [
        "storage",
        "002b094f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044b9b4",
      "PARAM",
      [
        "storage",
        "002a63b8",
        null,
        "string"
      ]
    ],
    [
      "0044b9c0",
      "PARAM",
      [
        "storage",
        "00ca4b68",
        null,
        "undefined2"
      ]
    ],
    [
      "0044b9d4",
      "PARAM",
      [
        "storage",
        "002b08f3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044b98c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b958.md#insn-0044b98c) · [`0044b99c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b958.md#insn-0044b99c) · [`0044b974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b958.md#insn-0044b974)
- 新版 [`0044b9cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b998.md#insn-0044b9cc) · [`0044b9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b998.md#insn-0044b9dc) · [`0044b9b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b998.md#insn-0044b9b4)

~~~diff
- 0044b98c ["INT_ADD", "register:40f0:8", ["const:44b98c:8", "const:4:8"]]
- 0044b98c ["CALL", null, ["callee:00c58180:8"]]
+ 0044b9cc ["INT_ADD", "register:40f0:8", ["const:44b9cc:8", "const:4:8"]]
+ 0044b9cc ["CALL", null, ["callee:00c58180:8"]]
- 0044b98c bytes c9312094
+ 0044b9cc bytes ed312094
- 0044b99c ["INT_ADD", "register:40f0:8", ["const:44b99c:8", "const:4:8"]]
- 0044b99c ["CALL", null, ["callee:00c58040:8"]]
+ 0044b9dc ["INT_ADD", "register:40f0:8", ["const:44b9dc:8", "const:4:8"]]
+ 0044b9dc ["CALL", null, ["callee:00c58040:8"]]
- 0044b99c bytes 75312094
+ 0044b9dc bytes 99312094
- 0044b974 ["COPY", "tmp:0:8", ["const:414:8"]]
- 0044b974 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0044b974 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0044b974 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0044b9b4 ["COPY", "tmp:0:8", ["const:3b8:8"]]
+ 0044b9b4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0044b9b4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0044b9b4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0044b974 bytes 00501091
+ 0044b9b4 bytes 00e00e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5da40a9d280465d2290c7ffd762b5238"></a>

### [`0044ba18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044ba18.md) → [`0044ba58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044ba58.md) FUN_0044ba58

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0097f894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097f/0097f894.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md)
- 新版 呼出元 1件 [`0097f8e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0097f/0097f8e8.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 89.19% / 新版 89.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044ba74",
      "incomplete_value": false,
      "site": "0044ba8c",
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
            "const:901:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044ba34",
      "incomplete_value": false,
      "site": "0044ba4c",
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
            "const:95d:8"
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
      "definition_site": "0044ba80",
      "incomplete_value": false,
      "site": "0044ba8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca4000:8"
          ],
          [
            "leaf",
            "const:b68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044ba40",
      "incomplete_value": false,
      "site": "0044ba4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca4000:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044ba94",
      "incomplete_value": false,
      "site": "0044ba9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a5000:8"
          ],
          [
            "leaf",
            "const:2fe:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044ba54",
      "incomplete_value": false,
      "site": "0044ba5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a5000:8"
          ],
          [
            "leaf",
            "const:35a:8"
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
      "0044ba74",
      "PARAM",
      [
        "storage",
        "002b095d",
        null,
        "string"
      ]
    ],
    [
      "0044ba80",
      "PARAM",
      [
        "storage",
        "00ca4a68",
        null,
        "undefined2"
      ]
    ],
    [
      "0044ba94",
      "PARAM",
      [
        "storage",
        "002a535a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044ba74",
      "PARAM",
      [
        "storage",
        "002b0901",
        null,
        "string"
      ]
    ],
    [
      "0044ba80",
      "PARAM",
      [
        "storage",
        "00ca4b68",
        null,
        "undefined2"
      ]
    ],
    [
      "0044ba94",
      "PARAM",
      [
        "storage",
        "002a52fe",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044ba4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044ba18.md#insn-0044ba4c) · [`0044ba5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044ba18.md#insn-0044ba5c) · [`0044ba34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044ba18.md#insn-0044ba34)
- 新版 [`0044ba8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044ba58.md#insn-0044ba8c) · [`0044ba9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044ba58.md#insn-0044ba9c) · [`0044ba74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044ba58.md#insn-0044ba74)

~~~diff
- 0044ba4c ["INT_ADD", "register:40f0:8", ["const:44ba4c:8", "const:4:8"]]
- 0044ba4c ["CALL", null, ["callee:00c58180:8"]]
+ 0044ba8c ["INT_ADD", "register:40f0:8", ["const:44ba8c:8", "const:4:8"]]
+ 0044ba8c ["CALL", null, ["callee:00c58180:8"]]
- 0044ba4c bytes 99312094
+ 0044ba8c bytes bd312094
- 0044ba5c ["INT_ADD", "register:40f0:8", ["const:44ba5c:8", "const:4:8"]]
- 0044ba5c ["CALL", null, ["callee:00c58040:8"]]
+ 0044ba9c ["INT_ADD", "register:40f0:8", ["const:44ba9c:8", "const:4:8"]]
+ 0044ba9c ["CALL", null, ["callee:00c58040:8"]]
- 0044ba5c bytes 45312094
+ 0044ba9c bytes 69312094
- 0044ba34 ["COPY", "tmp:0:8", ["const:95d:8"]]
- 0044ba34 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0044ba34 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0044ba34 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0044ba74 ["COPY", "tmp:0:8", ["const:901:8"]]
+ 0044ba74 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0044ba74 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0044ba74 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0044ba34 bytes 00742591
+ 0044ba74 bytes 00042491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-307362587eb00564c9a4311e0fffd2c3"></a>

### [`0044bad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044bad8.md) → [`0044bb18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044bb18.md) FUN_0044bb18

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`006a9764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a9/006a9764.md) [`00a75dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a75/00a75dac.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)
- 新版 呼出元 2件 [`006a97bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a9/006a97bc.md) [`00a75e1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a75/00a75e1c.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044bb40",
      "incomplete_value": true,
      "site": "0044bb50",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044bb00",
      "incomplete_value": true,
      "site": "0044bb10",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044bb54",
      "incomplete_value": true,
      "site": "0044bb54",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044bb14",
      "incomplete_value": true,
      "site": "0044bb14",
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
                "const:e:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044bb60",
      "incomplete_value": false,
      "site": "0044bb68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d89:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044bb20",
      "incomplete_value": false,
      "site": "0044bb28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
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
      "0044bb40",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044bb48",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044bb60",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044bb40",
      "READ",
      [
        "storage",
        "002bfb46",
        null,
        "string"
      ]
    ],
    [
      "0044bb48",
      "READ",
      [
        "storage",
        "002bfb54",
        null,
        "string"
      ]
    ],
    [
      "0044bb60",
      "PARAM",
      [
        "storage",
        "002a1d89",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044bad8.md#insn-0044bb20) · [`0044bb28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044bad8.md#insn-0044bb28) · [`0044bb50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044bad8.md#insn-0044bb50)
- 新版 [`0044bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044bb18.md#insn-0044bb60) · [`0044bb68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044bb18.md#insn-0044bb68) · [`0044bb90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044bb18.md#insn-0044bb90)

~~~diff
- 0044bb20 ["COPY", "tmp:0:8", ["const:dd6:8"]]
- 0044bb20 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044bb20 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044bb20 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044bb60 ["COPY", "tmp:0:8", ["const:d89:8"]]
+ 0044bb60 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044bb60 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044bb60 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044bb20 bytes 21583791
+ 0044bb60 bytes 21243691
- 0044bb28 ["INT_ADD", "register:40f0:8", ["const:44bb28:8", "const:4:8"]]
- 0044bb28 ["CALL", null, ["callee:00c58040:8"]]
+ 0044bb68 ["INT_ADD", "register:40f0:8", ["const:44bb68:8", "const:4:8"]]
+ 0044bb68 ["CALL", null, ["callee:00c58040:8"]]
- 0044bb28 bytes 12312094
+ 0044bb68 bytes 36312094
- 0044bb50 ["INT_ADD", "register:40f0:8", ["const:44bb50:8", "const:4:8"]]
- 0044bb50 ["CALL", null, ["callee:00c57f80:8"]]
+ 0044bb90 ["INT_ADD", "register:40f0:8", ["const:44bb90:8", "const:4:8"]]
+ 0044bb90 ["CALL", null, ["callee:00c57f80:8"]]
- 0044bb50 bytes d8302094
+ 0044bb90 bytes fc302094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94151ac984be2e094938afa413cd6216"></a>

### [`0044bbf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044bbf0.md) → [`0044bc30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044bc30.md) FUN_0044bc30

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`006b3ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b3/006b3ba4.md) [`008f6ae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f6/008f6ae8.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)
- 新版 呼出元 2件 [`006b3bfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b3/006b3bfc.md) [`008f6b3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f6/008f6b3c.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044bc58",
      "incomplete_value": true,
      "site": "0044bc68",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044bc18",
      "incomplete_value": true,
      "site": "0044bc28",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044bc6c",
      "incomplete_value": true,
      "site": "0044bc6c",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044bc2c",
      "incomplete_value": true,
      "site": "0044bc2c",
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
                "const:e:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044bc78",
      "incomplete_value": false,
      "site": "0044bc80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d89:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044bc38",
      "incomplete_value": false,
      "site": "0044bc40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
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
      "0044bc58",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044bc60",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044bc78",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044bc58",
      "READ",
      [
        "storage",
        "002bfb46",
        null,
        "string"
      ]
    ],
    [
      "0044bc60",
      "READ",
      [
        "storage",
        "002bfb54",
        null,
        "string"
      ]
    ],
    [
      "0044bc78",
      "PARAM",
      [
        "storage",
        "002a1d89",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044bc38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044bbf0.md#insn-0044bc38) · [`0044bc40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044bbf0.md#insn-0044bc40) · [`0044bc68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044bbf0.md#insn-0044bc68)
- 新版 [`0044bc78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044bc30.md#insn-0044bc78) · [`0044bc80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044bc30.md#insn-0044bc80) · [`0044bca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044bc30.md#insn-0044bca8)

~~~diff
- 0044bc38 ["COPY", "tmp:0:8", ["const:dd6:8"]]
- 0044bc38 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044bc38 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044bc38 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044bc78 ["COPY", "tmp:0:8", ["const:d89:8"]]
+ 0044bc78 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044bc78 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044bc78 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044bc38 bytes 21583791
+ 0044bc78 bytes 21243691
- 0044bc40 ["INT_ADD", "register:40f0:8", ["const:44bc40:8", "const:4:8"]]
- 0044bc40 ["CALL", null, ["callee:00c58040:8"]]
+ 0044bc80 ["INT_ADD", "register:40f0:8", ["const:44bc80:8", "const:4:8"]]
+ 0044bc80 ["CALL", null, ["callee:00c58040:8"]]
- 0044bc40 bytes cc302094
+ 0044bc80 bytes f0302094
- 0044bc68 ["INT_ADD", "register:40f0:8", ["const:44bc68:8", "const:4:8"]]
- 0044bc68 ["CALL", null, ["callee:00c57f80:8"]]
+ 0044bca8 ["INT_ADD", "register:40f0:8", ["const:44bca8:8", "const:4:8"]]
+ 0044bca8 ["CALL", null, ["callee:00c57f80:8"]]
- 0044bc68 bytes 92302094
+ 0044bca8 bytes b6302094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00cf0fbba8041dbd571ac2f41ff54b55"></a>

### [`0044bd08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044bd08.md) → [`0044bd48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044bd48.md) FUN_0044bd48

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.49% / 新版 91.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044bd74",
      "incomplete_value": true,
      "site": "0044bd88",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044bd34",
      "incomplete_value": true,
      "site": "0044bd48",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b9a:8"
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
      "definition_site": "0044bd8c",
      "incomplete_value": true,
      "site": "0044bd8c",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044bd4c",
      "incomplete_value": true,
      "site": "0044bd4c",
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
                "const:e:8"
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
      "definition_site": "0044bd98",
      "incomplete_value": false,
      "site": "0044bda0",
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
            "const:e2a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044bd58",
      "incomplete_value": false,
      "site": "0044bd60",
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
            "const:dea:8"
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
      "0044bd74",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044bd80",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044bd98",
      "PARAM",
      [
        "storage",
        "002b5dea",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044bd74",
      "READ",
      [
        "storage",
        "002bfb46",
        null,
        "string"
      ]
    ],
    [
      "0044bd80",
      "READ",
      [
        "storage",
        "002bfb54",
        null,
        "string"
      ]
    ],
    [
      "0044bd98",
      "PARAM",
      [
        "storage",
        "002b5e2a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044bd58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044bd08.md#insn-0044bd58) · [`0044bd60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044bd08.md#insn-0044bd60) · [`0044bd88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044bd08.md#insn-0044bd88)
- 新版 [`0044bd98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044bd48.md#insn-0044bd98) · [`0044bda0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044bd48.md#insn-0044bda0) · [`0044bdc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044bd48.md#insn-0044bdc8)

~~~diff
- 0044bd58 ["COPY", "tmp:0:8", ["const:dea:8"]]
- 0044bd58 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044bd58 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044bd58 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044bd98 ["COPY", "tmp:0:8", ["const:e2a:8"]]
+ 0044bd98 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044bd98 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044bd98 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044bd58 bytes 21a83791
+ 0044bd98 bytes 21a83891
- 0044bd60 ["INT_ADD", "register:40f0:8", ["const:44bd60:8", "const:4:8"]]
- 0044bd60 ["CALL", null, ["callee:00c58040:8"]]
+ 0044bda0 ["INT_ADD", "register:40f0:8", ["const:44bda0:8", "const:4:8"]]
+ 0044bda0 ["CALL", null, ["callee:00c58040:8"]]
- 0044bd60 bytes 84302094
+ 0044bda0 bytes a8302094
- 0044bd88 ["INT_ADD", "register:40f0:8", ["const:44bd88:8", "const:4:8"]]
- 0044bd88 ["CALL", null, ["callee:00c57f80:8"]]
+ 0044bdc8 ["INT_ADD", "register:40f0:8", ["const:44bdc8:8", "const:4:8"]]
+ 0044bdc8 ["CALL", null, ["callee:00c57f80:8"]]
- 0044bd88 bytes 4a302094
+ 0044bdc8 bytes 6e302094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2f8b95f7eca4cf4dea208114f1084ab"></a>

### [`0044bf14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044bf14.md) → [`0044bf54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044bf54.md) FUN_0044bf54

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00783274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00783/00783274.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)
- 新版 呼出元 1件 [`007832cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00783/007832cc.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044bf7c",
      "incomplete_value": true,
      "site": "0044bf8c",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044bf3c",
      "incomplete_value": true,
      "site": "0044bf4c",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044bf90",
      "incomplete_value": true,
      "site": "0044bf90",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044bf50",
      "incomplete_value": true,
      "site": "0044bf50",
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
                "const:e:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044bf9c",
      "incomplete_value": false,
      "site": "0044bfa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d89:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044bf5c",
      "incomplete_value": false,
      "site": "0044bf64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
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
      "0044bf7c",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044bf84",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044bf9c",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044bf7c",
      "READ",
      [
        "storage",
        "002bfb46",
        null,
        "string"
      ]
    ],
    [
      "0044bf84",
      "READ",
      [
        "storage",
        "002bfb54",
        null,
        "string"
      ]
    ],
    [
      "0044bf9c",
      "PARAM",
      [
        "storage",
        "002a1d89",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044bf5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044bf14.md#insn-0044bf5c) · [`0044bf64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044bf14.md#insn-0044bf64) · [`0044bf8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044bf14.md#insn-0044bf8c)
- 新版 [`0044bf9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044bf54.md#insn-0044bf9c) · [`0044bfa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044bf54.md#insn-0044bfa4) · [`0044bfcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044bf54.md#insn-0044bfcc)

~~~diff
- 0044bf5c ["COPY", "tmp:0:8", ["const:dd6:8"]]
- 0044bf5c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044bf5c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044bf5c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044bf9c ["COPY", "tmp:0:8", ["const:d89:8"]]
+ 0044bf9c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044bf9c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044bf9c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044bf5c bytes 21583791
+ 0044bf9c bytes 21243691
- 0044bf64 ["INT_ADD", "register:40f0:8", ["const:44bf64:8", "const:4:8"]]
- 0044bf64 ["CALL", null, ["callee:00c58040:8"]]
+ 0044bfa4 ["INT_ADD", "register:40f0:8", ["const:44bfa4:8", "const:4:8"]]
+ 0044bfa4 ["CALL", null, ["callee:00c58040:8"]]
- 0044bf64 bytes 03302094
+ 0044bfa4 bytes 27302094
- 0044bf8c ["INT_ADD", "register:40f0:8", ["const:44bf8c:8", "const:4:8"]]
- 0044bf8c ["CALL", null, ["callee:00c57f80:8"]]
+ 0044bfcc ["INT_ADD", "register:40f0:8", ["const:44bfcc:8", "const:4:8"]]
+ 0044bfcc ["CALL", null, ["callee:00c57f80:8"]]
- 0044bf8c bytes c92f2094
+ 0044bfcc bytes ed2f2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f835e3be544a5cfc66614e4d038aba5f"></a>

### [`0044c02c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c02c.md) → [`0044c06c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044c/0044c06c.md) FUN_0044c06c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00783274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00783/00783274.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)
- 新版 呼出元 1件 [`007832cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00783/007832cc.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044c094",
      "incomplete_value": true,
      "site": "0044c0a4",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044c054",
      "incomplete_value": true,
      "site": "0044c064",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044c0a8",
      "incomplete_value": true,
      "site": "0044c0a8",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044c068",
      "incomplete_value": true,
      "site": "0044c068",
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
                "const:e:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044c0b4",
      "incomplete_value": false,
      "site": "0044c0bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d89:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044c074",
      "incomplete_value": false,
      "site": "0044c07c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
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
      "0044c094",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044c09c",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044c0b4",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044c094",
      "READ",
      [
        "storage",
        "002bfb46",
        null,
        "string"
      ]
    ],
    [
      "0044c09c",
      "READ",
      [
        "storage",
        "002bfb54",
        null,
        "string"
      ]
    ],
    [
      "0044c0b4",
      "PARAM",
      [
        "storage",
        "002a1d89",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044c074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c02c.md#insn-0044c074) · [`0044c07c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c02c.md#insn-0044c07c) · [`0044c0a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c02c.md#insn-0044c0a4)
- 新版 [`0044c0b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044c/0044c06c.md#insn-0044c0b4) · [`0044c0bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044c/0044c06c.md#insn-0044c0bc) · [`0044c0e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044c/0044c06c.md#insn-0044c0e4)

~~~diff
- 0044c074 ["COPY", "tmp:0:8", ["const:dd6:8"]]
- 0044c074 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044c074 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044c074 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044c0b4 ["COPY", "tmp:0:8", ["const:d89:8"]]
+ 0044c0b4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044c0b4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044c0b4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044c074 bytes 21583791
+ 0044c0b4 bytes 21243691
- 0044c07c ["INT_ADD", "register:40f0:8", ["const:44c07c:8", "const:4:8"]]
- 0044c07c ["CALL", null, ["callee:00c58040:8"]]
+ 0044c0bc ["INT_ADD", "register:40f0:8", ["const:44c0bc:8", "const:4:8"]]
+ 0044c0bc ["CALL", null, ["callee:00c58040:8"]]
- 0044c07c bytes bd2f2094
+ 0044c0bc bytes e12f2094
- 0044c0a4 ["INT_ADD", "register:40f0:8", ["const:44c0a4:8", "const:4:8"]]
- 0044c0a4 ["CALL", null, ["callee:00c57f80:8"]]
+ 0044c0e4 ["INT_ADD", "register:40f0:8", ["const:44c0e4:8", "const:4:8"]]
+ 0044c0e4 ["CALL", null, ["callee:00c57f80:8"]]
- 0044c0a4 bytes 832f2094
+ 0044c0e4 bytes a72f2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96f990f1fed9f9b8563171d7c6f30735"></a>

### [`0044c144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c144.md) → [`0044c184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044c/0044c184.md) FUN_0044c184

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)
- 新版 呼出元 1件 [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044c1ac",
      "incomplete_value": true,
      "site": "0044c1bc",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044c16c",
      "incomplete_value": true,
      "site": "0044c17c",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044c1c0",
      "incomplete_value": true,
      "site": "0044c1c0",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044c180",
      "incomplete_value": true,
      "site": "0044c180",
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
                "const:e:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044c1cc",
      "incomplete_value": false,
      "site": "0044c1d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d89:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044c18c",
      "incomplete_value": false,
      "site": "0044c194",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
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
      "0044c1ac",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044c1b4",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044c1cc",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044c1ac",
      "READ",
      [
        "storage",
        "002bfb46",
        null,
        "string"
      ]
    ],
    [
      "0044c1b4",
      "READ",
      [
        "storage",
        "002bfb54",
        null,
        "string"
      ]
    ],
    [
      "0044c1cc",
      "PARAM",
      [
        "storage",
        "002a1d89",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044c18c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c144.md#insn-0044c18c) · [`0044c194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c144.md#insn-0044c194) · [`0044c1bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c144.md#insn-0044c1bc)
- 新版 [`0044c1cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044c/0044c184.md#insn-0044c1cc) · [`0044c1d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044c/0044c184.md#insn-0044c1d4) · [`0044c1fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044c/0044c184.md#insn-0044c1fc)

~~~diff
- 0044c18c ["COPY", "tmp:0:8", ["const:dd6:8"]]
- 0044c18c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044c18c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044c18c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044c1cc ["COPY", "tmp:0:8", ["const:d89:8"]]
+ 0044c1cc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044c1cc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044c1cc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044c18c bytes 21583791
+ 0044c1cc bytes 21243691
- 0044c194 ["INT_ADD", "register:40f0:8", ["const:44c194:8", "const:4:8"]]
- 0044c194 ["CALL", null, ["callee:00c58040:8"]]
+ 0044c1d4 ["INT_ADD", "register:40f0:8", ["const:44c1d4:8", "const:4:8"]]
+ 0044c1d4 ["CALL", null, ["callee:00c58040:8"]]
- 0044c194 bytes 772f2094
+ 0044c1d4 bytes 9b2f2094
- 0044c1bc ["INT_ADD", "register:40f0:8", ["const:44c1bc:8", "const:4:8"]]
- 0044c1bc ["CALL", null, ["callee:00c57f80:8"]]
+ 0044c1fc ["INT_ADD", "register:40f0:8", ["const:44c1fc:8", "const:4:8"]]
+ 0044c1fc ["CALL", null, ["callee:00c57f80:8"]]
- 0044c1bc bytes 3d2f2094
+ 0044c1fc bytes 612f2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3c0d615ac59d8e3326f1c234aeeceab"></a>

### [`0044c25c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c25c.md) → [`0044c29c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044c/0044c29c.md) FUN_0044c29c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0082f128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082f/0082f128.md) [`0089e87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089e/0089e87c.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)
- 新版 呼出元 2件 [`0082f180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082f/0082f180.md) [`0089e8d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089e/0089e8d4.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044c2c4",
      "incomplete_value": true,
      "site": "0044c2d4",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044c284",
      "incomplete_value": true,
      "site": "0044c294",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044c2d8",
      "incomplete_value": true,
      "site": "0044c2d8",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044c298",
      "incomplete_value": true,
      "site": "0044c298",
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
                "const:e:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044c2e4",
      "incomplete_value": false,
      "site": "0044c2ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d89:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044c2a4",
      "incomplete_value": false,
      "site": "0044c2ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
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
      "0044c2c4",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044c2cc",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044c2e4",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044c2c4",
      "READ",
      [
        "storage",
        "002bfb46",
        null,
        "string"
      ]
    ],
    [
      "0044c2cc",
      "READ",
      [
        "storage",
        "002bfb54",
        null,
        "string"
      ]
    ],
    [
      "0044c2e4",
      "PARAM",
      [
        "storage",
        "002a1d89",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044c2a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c25c.md#insn-0044c2a4) · [`0044c2ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c25c.md#insn-0044c2ac) · [`0044c2d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c25c.md#insn-0044c2d4)
- 新版 [`0044c2e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044c/0044c29c.md#insn-0044c2e4) · [`0044c2ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044c/0044c29c.md#insn-0044c2ec) · [`0044c314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044c/0044c29c.md#insn-0044c314)

~~~diff
- 0044c2a4 ["COPY", "tmp:0:8", ["const:dd6:8"]]
- 0044c2a4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044c2a4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044c2a4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044c2e4 ["COPY", "tmp:0:8", ["const:d89:8"]]
+ 0044c2e4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044c2e4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044c2e4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044c2a4 bytes 21583791
+ 0044c2e4 bytes 21243691
- 0044c2ac ["INT_ADD", "register:40f0:8", ["const:44c2ac:8", "const:4:8"]]
- 0044c2ac ["CALL", null, ["callee:00c58040:8"]]
+ 0044c2ec ["INT_ADD", "register:40f0:8", ["const:44c2ec:8", "const:4:8"]]
+ 0044c2ec ["CALL", null, ["callee:00c58040:8"]]
- 0044c2ac bytes 312f2094
+ 0044c2ec bytes 552f2094
- 0044c2d4 ["INT_ADD", "register:40f0:8", ["const:44c2d4:8", "const:4:8"]]
- 0044c2d4 ["CALL", null, ["callee:00c57f80:8"]]
+ 0044c314 ["INT_ADD", "register:40f0:8", ["const:44c314:8", "const:4:8"]]
+ 0044c314 ["CALL", null, ["callee:00c57f80:8"]]
- 0044c2d4 bytes f72e2094
+ 0044c314 bytes 1b2f2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d26dd214352a18c8f74e1a9383639f3"></a>

### [`0044c374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c374.md) → [`0044c3b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044c/0044c3b4.md) FUN_0044c3b4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)
- 新版 呼出元 1件 [`00856e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856e84.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044c3dc",
      "incomplete_value": true,
      "site": "0044c3ec",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044c39c",
      "incomplete_value": true,
      "site": "0044c3ac",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044c3f0",
      "incomplete_value": true,
      "site": "0044c3f0",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044c3b0",
      "incomplete_value": true,
      "site": "0044c3b0",
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
                "const:e:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044c3fc",
      "incomplete_value": false,
      "site": "0044c404",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d89:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044c3bc",
      "incomplete_value": false,
      "site": "0044c3c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
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
      "0044c3dc",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044c3e4",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044c3fc",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044c3dc",
      "READ",
      [
        "storage",
        "002bfb46",
        null,
        "string"
      ]
    ],
    [
      "0044c3e4",
      "READ",
      [
        "storage",
        "002bfb54",
        null,
        "string"
      ]
    ],
    [
      "0044c3fc",
      "PARAM",
      [
        "storage",
        "002a1d89",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044c3bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c374.md#insn-0044c3bc) · [`0044c3c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c374.md#insn-0044c3c4) · [`0044c3ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c374.md#insn-0044c3ec)
- 新版 [`0044c3fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044c/0044c3b4.md#insn-0044c3fc) · [`0044c404`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044c/0044c3b4.md#insn-0044c404) · [`0044c42c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044c/0044c3b4.md#insn-0044c42c)

~~~diff
- 0044c3bc ["COPY", "tmp:0:8", ["const:dd6:8"]]
- 0044c3bc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044c3bc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044c3bc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044c3fc ["COPY", "tmp:0:8", ["const:d89:8"]]
+ 0044c3fc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044c3fc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044c3fc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044c3bc bytes 21583791
+ 0044c3fc bytes 21243691
- 0044c3c4 ["INT_ADD", "register:40f0:8", ["const:44c3c4:8", "const:4:8"]]
- 0044c3c4 ["CALL", null, ["callee:00c58040:8"]]
+ 0044c404 ["INT_ADD", "register:40f0:8", ["const:44c404:8", "const:4:8"]]
+ 0044c404 ["CALL", null, ["callee:00c58040:8"]]
- 0044c3c4 bytes eb2e2094
+ 0044c404 bytes 0f2f2094
- 0044c3ec ["INT_ADD", "register:40f0:8", ["const:44c3ec:8", "const:4:8"]]
- 0044c3ec ["CALL", null, ["callee:00c57f80:8"]]
+ 0044c42c ["INT_ADD", "register:40f0:8", ["const:44c42c:8", "const:4:8"]]
+ 0044c42c ["CALL", null, ["callee:00c57f80:8"]]
- 0044c3ec bytes b12e2094
+ 0044c42c bytes d52e2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-600ff8fbbcc6898454cdcd97857a8be1"></a>

### [`0044c48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c48c.md) → [`0044c4cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044c/0044c4cc.md) FUN_0044c4cc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007aed38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aed38.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)
- 新版 呼出元 1件 [`007aed90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ae/007aed90.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044c4f4",
      "incomplete_value": true,
      "site": "0044c504",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044c4b4",
      "incomplete_value": true,
      "site": "0044c4c4",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044c508",
      "incomplete_value": true,
      "site": "0044c508",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044c4c8",
      "incomplete_value": true,
      "site": "0044c4c8",
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
                "const:e:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044c514",
      "incomplete_value": false,
      "site": "0044c51c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d89:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044c4d4",
      "incomplete_value": false,
      "site": "0044c4dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
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
      "0044c4f4",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044c4fc",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044c514",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044c4f4",
      "READ",
      [
        "storage",
        "002bfb46",
        null,
        "string"
      ]
    ],
    [
      "0044c4fc",
      "READ",
      [
        "storage",
        "002bfb54",
        null,
        "string"
      ]
    ],
    [
      "0044c514",
      "PARAM",
      [
        "storage",
        "002a1d89",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044c4d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c48c.md#insn-0044c4d4) · [`0044c4dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c48c.md#insn-0044c4dc) · [`0044c504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c48c.md#insn-0044c504)
- 新版 [`0044c514`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044c/0044c4cc.md#insn-0044c514) · [`0044c51c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044c/0044c4cc.md#insn-0044c51c) · [`0044c544`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044c/0044c4cc.md#insn-0044c544)

~~~diff
- 0044c4d4 ["COPY", "tmp:0:8", ["const:dd6:8"]]
- 0044c4d4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044c4d4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044c4d4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044c514 ["COPY", "tmp:0:8", ["const:d89:8"]]
+ 0044c514 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044c514 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044c514 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044c4d4 bytes 21583791
+ 0044c514 bytes 21243691
- 0044c4dc ["INT_ADD", "register:40f0:8", ["const:44c4dc:8", "const:4:8"]]
- 0044c4dc ["CALL", null, ["callee:00c58040:8"]]
+ 0044c51c ["INT_ADD", "register:40f0:8", ["const:44c51c:8", "const:4:8"]]
+ 0044c51c ["CALL", null, ["callee:00c58040:8"]]
- 0044c4dc bytes a52e2094
+ 0044c51c bytes c92e2094
- 0044c504 ["INT_ADD", "register:40f0:8", ["const:44c504:8", "const:4:8"]]
- 0044c504 ["CALL", null, ["callee:00c57f80:8"]]
+ 0044c544 ["INT_ADD", "register:40f0:8", ["const:44c544:8", "const:4:8"]]
+ 0044c544 ["CALL", null, ["callee:00c57f80:8"]]
- 0044c504 bytes 6b2e2094
+ 0044c544 bytes 8f2e2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-559392dee5de5ee01574ab29a17c09d6"></a>

### [`0044c5a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c5a4.md) → [`0044c5e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044c/0044c5e4.md) FUN_0044c5e4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00814bf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00814/00814bf8.md) [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)
- 新版 呼出元 2件 [`00814c50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00814/00814c50.md) [`00856e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856e84.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044c60c",
      "incomplete_value": true,
      "site": "0044c61c",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044c5cc",
      "incomplete_value": true,
      "site": "0044c5dc",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044c620",
      "incomplete_value": true,
      "site": "0044c620",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044c5e0",
      "incomplete_value": true,
      "site": "0044c5e0",
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
                "const:e:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044c62c",
      "incomplete_value": false,
      "site": "0044c634",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d89:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044c5ec",
      "incomplete_value": false,
      "site": "0044c5f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
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
      "0044c60c",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044c614",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044c62c",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044c60c",
      "READ",
      [
        "storage",
        "002bfb46",
        null,
        "string"
      ]
    ],
    [
      "0044c614",
      "READ",
      [
        "storage",
        "002bfb54",
        null,
        "string"
      ]
    ],
    [
      "0044c62c",
      "PARAM",
      [
        "storage",
        "002a1d89",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044c5ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c5a4.md#insn-0044c5ec) · [`0044c5f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c5a4.md#insn-0044c5f4) · [`0044c61c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c5a4.md#insn-0044c61c)
- 新版 [`0044c62c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044c/0044c5e4.md#insn-0044c62c) · [`0044c634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044c/0044c5e4.md#insn-0044c634) · [`0044c65c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044c/0044c5e4.md#insn-0044c65c)

~~~diff
- 0044c5ec ["COPY", "tmp:0:8", ["const:dd6:8"]]
- 0044c5ec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044c5ec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044c5ec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044c62c ["COPY", "tmp:0:8", ["const:d89:8"]]
+ 0044c62c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044c62c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044c62c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044c5ec bytes 21583791
+ 0044c62c bytes 21243691
- 0044c5f4 ["INT_ADD", "register:40f0:8", ["const:44c5f4:8", "const:4:8"]]
- 0044c5f4 ["CALL", null, ["callee:00c58040:8"]]
+ 0044c634 ["INT_ADD", "register:40f0:8", ["const:44c634:8", "const:4:8"]]
+ 0044c634 ["CALL", null, ["callee:00c58040:8"]]
- 0044c5f4 bytes 5f2e2094
+ 0044c634 bytes 832e2094
- 0044c61c ["INT_ADD", "register:40f0:8", ["const:44c61c:8", "const:4:8"]]
- 0044c61c ["CALL", null, ["callee:00c57f80:8"]]
+ 0044c65c ["INT_ADD", "register:40f0:8", ["const:44c65c:8", "const:4:8"]]
+ 0044c65c ["CALL", null, ["callee:00c57f80:8"]]
- 0044c61c bytes 252e2094
+ 0044c65c bytes 492e2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02c74d3f462ab9090763ff19ae8b145a"></a>

### [`0044c6bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c6bc.md) → [`0044c6fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044c/0044c6fc.md) FUN_0044c6fc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)
- 新版 呼出元 1件 [`00856e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856e84.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044c724",
      "incomplete_value": true,
      "site": "0044c734",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044c6e4",
      "incomplete_value": true,
      "site": "0044c6f4",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044c738",
      "incomplete_value": true,
      "site": "0044c738",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044c6f8",
      "incomplete_value": true,
      "site": "0044c6f8",
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
                "const:e:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044c744",
      "incomplete_value": false,
      "site": "0044c74c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d89:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044c704",
      "incomplete_value": false,
      "site": "0044c70c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
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
      "0044c724",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044c72c",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044c744",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044c724",
      "READ",
      [
        "storage",
        "002bfb46",
        null,
        "string"
      ]
    ],
    [
      "0044c72c",
      "READ",
      [
        "storage",
        "002bfb54",
        null,
        "string"
      ]
    ],
    [
      "0044c744",
      "PARAM",
      [
        "storage",
        "002a1d89",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044c704`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c6bc.md#insn-0044c704) · [`0044c70c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c6bc.md#insn-0044c70c) · [`0044c734`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c6bc.md#insn-0044c734)
- 新版 [`0044c744`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044c/0044c6fc.md#insn-0044c744) · [`0044c74c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044c/0044c6fc.md#insn-0044c74c) · [`0044c774`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044c/0044c6fc.md#insn-0044c774)

~~~diff
- 0044c704 ["COPY", "tmp:0:8", ["const:dd6:8"]]
- 0044c704 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044c704 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044c704 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044c744 ["COPY", "tmp:0:8", ["const:d89:8"]]
+ 0044c744 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044c744 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044c744 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044c704 bytes 21583791
+ 0044c744 bytes 21243691
- 0044c70c ["INT_ADD", "register:40f0:8", ["const:44c70c:8", "const:4:8"]]
- 0044c70c ["CALL", null, ["callee:00c58040:8"]]
+ 0044c74c ["INT_ADD", "register:40f0:8", ["const:44c74c:8", "const:4:8"]]
+ 0044c74c ["CALL", null, ["callee:00c58040:8"]]
- 0044c70c bytes 192e2094
+ 0044c74c bytes 3d2e2094
- 0044c734 ["INT_ADD", "register:40f0:8", ["const:44c734:8", "const:4:8"]]
- 0044c734 ["CALL", null, ["callee:00c57f80:8"]]
+ 0044c774 ["INT_ADD", "register:40f0:8", ["const:44c774:8", "const:4:8"]]
+ 0044c774 ["CALL", null, ["callee:00c57f80:8"]]
- 0044c734 bytes df2d2094
+ 0044c774 bytes 032e2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c14ddb61146eb5c19a20694f04ac4519"></a>

### [`0044c7d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c7d4.md) → [`0044c814`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044c/0044c814.md) FUN_0044c814

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0088c4ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c4ac.md) · 呼出先 4件 [`0044b254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b254.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)
- 新版 呼出元 1件 [`0088c504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c504.md) · 呼出先 4件 [`0044b294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b294.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md)

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
      "definition_site": "0044c840",
      "incomplete_value": false,
      "site": "0044c848",
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
            "const:fbe:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044c800",
      "incomplete_value": false,
      "site": "0044c808",
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
            "const:f7e:8"
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
      "0044c840",
      "PARAM",
      [
        "storage",
        "002b7f7e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044c840",
      "PARAM",
      [
        "storage",
        "002b7fbe",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044c808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c7d4.md#insn-0044c808) · [`0044c7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c7d4.md#insn-0044c7f8) · [`0044c800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c7d4.md#insn-0044c800)
- 新版 [`0044c848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044c/0044c814.md#insn-0044c848) · [`0044c838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044c/0044c814.md#insn-0044c838) · [`0044c840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044c/0044c814.md#insn-0044c840)

~~~diff
- 0044c808 ["INT_ADD", "register:40f0:8", ["const:44c808:8", "const:4:8"]]
- 0044c808 ["CALL", null, ["callee:00c58040:8"]]
+ 0044c848 ["INT_ADD", "register:40f0:8", ["const:44c848:8", "const:4:8"]]
+ 0044c848 ["CALL", null, ["callee:00c58040:8"]]
- 0044c808 bytes da2d2094
+ 0044c848 bytes fe2d2094
- 0044c7f8 ["INT_ADD", "register:40f0:8", ["const:44c7f8:8", "const:4:8"]]
- 0044c7f8 ["CALL", null, ["callee:0044b294:8"]]
+ 0044c838 ["INT_ADD", "register:40f0:8", ["const:44c838:8", "const:4:8"]]
+ 0044c838 ["CALL", null, ["callee:0044b294:8"]]
- 0044c7f8 bytes 97faff97
+ 0044c838 bytes 97faff97
- 0044c800 ["COPY", "tmp:0:8", ["const:f7e:8"]]
- 0044c800 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044c800 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044c800 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044c840 ["COPY", "tmp:0:8", ["const:fbe:8"]]
+ 0044c840 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044c840 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044c840 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044c800 bytes 21f83d91
+ 0044c840 bytes 21f83e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b5541e566c3cd84b0532fb9e426383e9"></a>

### [`0044c884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c884.md) → [`0044c8c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044c/0044c8c4.md) FUN_0044c8c4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008cb434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cb434.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)
- 新版 呼出元 1件 [`008cb488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008cb/008cb488.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044c8ec",
      "incomplete_value": true,
      "site": "0044c8fc",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044c8ac",
      "incomplete_value": true,
      "site": "0044c8bc",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044c900",
      "incomplete_value": true,
      "site": "0044c900",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044c8c0",
      "incomplete_value": true,
      "site": "0044c8c0",
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
                "const:e:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044c90c",
      "incomplete_value": false,
      "site": "0044c914",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d89:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044c8cc",
      "incomplete_value": false,
      "site": "0044c8d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
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
      "0044c8ec",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044c8f4",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044c90c",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044c8ec",
      "READ",
      [
        "storage",
        "002bfb46",
        null,
        "string"
      ]
    ],
    [
      "0044c8f4",
      "READ",
      [
        "storage",
        "002bfb54",
        null,
        "string"
      ]
    ],
    [
      "0044c90c",
      "PARAM",
      [
        "storage",
        "002a1d89",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044c8cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c884.md#insn-0044c8cc) · [`0044c8d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c884.md#insn-0044c8d4) · [`0044c8fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c884.md#insn-0044c8fc)
- 新版 [`0044c90c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044c/0044c8c4.md#insn-0044c90c) · [`0044c914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044c/0044c8c4.md#insn-0044c914) · [`0044c93c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044c/0044c8c4.md#insn-0044c93c)

~~~diff
- 0044c8cc ["COPY", "tmp:0:8", ["const:dd6:8"]]
- 0044c8cc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044c8cc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044c8cc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044c90c ["COPY", "tmp:0:8", ["const:d89:8"]]
+ 0044c90c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044c90c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044c90c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044c8cc bytes 21583791
+ 0044c90c bytes 21243691
- 0044c8d4 ["INT_ADD", "register:40f0:8", ["const:44c8d4:8", "const:4:8"]]
- 0044c8d4 ["CALL", null, ["callee:00c58040:8"]]
+ 0044c914 ["INT_ADD", "register:40f0:8", ["const:44c914:8", "const:4:8"]]
+ 0044c914 ["CALL", null, ["callee:00c58040:8"]]
- 0044c8d4 bytes a72d2094
+ 0044c914 bytes cb2d2094
- 0044c8fc ["INT_ADD", "register:40f0:8", ["const:44c8fc:8", "const:4:8"]]
- 0044c8fc ["CALL", null, ["callee:00c57f80:8"]]
+ 0044c93c ["INT_ADD", "register:40f0:8", ["const:44c93c:8", "const:4:8"]]
+ 0044c93c ["CALL", null, ["callee:00c57f80:8"]]
- 0044c8fc bytes 6d2d2094
+ 0044c93c bytes 912d2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41008d346060ae74da51009e421b55cb"></a>

### [`0044c99c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c99c.md) → [`0044c9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044c/0044c9dc.md) FUN_0044c9dc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00a3e214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3e/00a3e214.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00a3e268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3e/00a3e268.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.49% / 新版 91.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044ca08",
      "incomplete_value": true,
      "site": "0044ca1c",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044c9c8",
      "incomplete_value": true,
      "site": "0044c9dc",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b9a:8"
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
      "definition_site": "0044ca20",
      "incomplete_value": true,
      "site": "0044ca20",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044c9e0",
      "incomplete_value": true,
      "site": "0044c9e0",
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
                "const:e:8"
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
      "definition_site": "0044ca2c",
      "incomplete_value": false,
      "site": "0044ca34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d89:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044c9ec",
      "incomplete_value": false,
      "site": "0044c9f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
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
      "0044ca08",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044ca14",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044ca2c",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044ca08",
      "READ",
      [
        "storage",
        "002bfb46",
        null,
        "string"
      ]
    ],
    [
      "0044ca14",
      "READ",
      [
        "storage",
        "002bfb54",
        null,
        "string"
      ]
    ],
    [
      "0044ca2c",
      "PARAM",
      [
        "storage",
        "002a1d89",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044c9ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c99c.md#insn-0044c9ec) · [`0044c9f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c99c.md#insn-0044c9f4) · [`0044ca1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c99c.md#insn-0044ca1c)
- 新版 [`0044ca2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044c/0044c9dc.md#insn-0044ca2c) · [`0044ca34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044c/0044c9dc.md#insn-0044ca34) · [`0044ca5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044c/0044c9dc.md#insn-0044ca5c)

~~~diff
- 0044c9ec ["COPY", "tmp:0:8", ["const:dd6:8"]]
- 0044c9ec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044c9ec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044c9ec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044ca2c ["COPY", "tmp:0:8", ["const:d89:8"]]
+ 0044ca2c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044ca2c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044ca2c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044c9ec bytes 21583791
+ 0044ca2c bytes 21243691
- 0044c9f4 ["INT_ADD", "register:40f0:8", ["const:44c9f4:8", "const:4:8"]]
- 0044c9f4 ["CALL", null, ["callee:00c58040:8"]]
+ 0044ca34 ["INT_ADD", "register:40f0:8", ["const:44ca34:8", "const:4:8"]]
+ 0044ca34 ["CALL", null, ["callee:00c58040:8"]]
- 0044c9f4 bytes 5f2d2094
+ 0044ca34 bytes 832d2094
- 0044ca1c ["INT_ADD", "register:40f0:8", ["const:44ca1c:8", "const:4:8"]]
- 0044ca1c ["CALL", null, ["callee:00c57f80:8"]]
+ 0044ca5c ["INT_ADD", "register:40f0:8", ["const:44ca5c:8", "const:4:8"]]
+ 0044ca5c ["CALL", null, ["callee:00c57f80:8"]]
- 0044ca1c bytes 252d2094
+ 0044ca5c bytes 492d2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28b353701c9b89c65d0226f73d9a64ab"></a>

### [`0044cba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044cba8.md) → [`0044cbe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044c/0044cbe8.md) FUN_0044cbe8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00a3e214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3e/00a3e214.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00a3e268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3e/00a3e268.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.49% / 新版 91.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044cc14",
      "incomplete_value": true,
      "site": "0044cc28",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044cbd4",
      "incomplete_value": true,
      "site": "0044cbe8",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b9a:8"
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
      "definition_site": "0044cc2c",
      "incomplete_value": true,
      "site": "0044cc2c",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044cbec",
      "incomplete_value": true,
      "site": "0044cbec",
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
                "const:e:8"
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
      "definition_site": "0044cc38",
      "incomplete_value": false,
      "site": "0044cc40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d89:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044cbf8",
      "incomplete_value": false,
      "site": "0044cc00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
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
      "0044cc14",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044cc20",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044cc38",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044cc14",
      "READ",
      [
        "storage",
        "002bfb46",
        null,
        "string"
      ]
    ],
    [
      "0044cc20",
      "READ",
      [
        "storage",
        "002bfb54",
        null,
        "string"
      ]
    ],
    [
      "0044cc38",
      "PARAM",
      [
        "storage",
        "002a1d89",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044cbf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044cba8.md#insn-0044cbf8) · [`0044cc00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044cba8.md#insn-0044cc00) · [`0044cc28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044cba8.md#insn-0044cc28)
- 新版 [`0044cc38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044c/0044cbe8.md#insn-0044cc38) · [`0044cc40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044c/0044cbe8.md#insn-0044cc40) · [`0044cc68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044c/0044cbe8.md#insn-0044cc68)

~~~diff
- 0044cbf8 ["COPY", "tmp:0:8", ["const:dd6:8"]]
- 0044cbf8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044cbf8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044cbf8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044cc38 ["COPY", "tmp:0:8", ["const:d89:8"]]
+ 0044cc38 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044cc38 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044cc38 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044cbf8 bytes 21583791
+ 0044cc38 bytes 21243691
- 0044cc00 ["INT_ADD", "register:40f0:8", ["const:44cc00:8", "const:4:8"]]
- 0044cc00 ["CALL", null, ["callee:00c58040:8"]]
+ 0044cc40 ["INT_ADD", "register:40f0:8", ["const:44cc40:8", "const:4:8"]]
+ 0044cc40 ["CALL", null, ["callee:00c58040:8"]]
- 0044cc00 bytes dc2c2094
+ 0044cc40 bytes 002d2094
- 0044cc28 ["INT_ADD", "register:40f0:8", ["const:44cc28:8", "const:4:8"]]
- 0044cc28 ["CALL", null, ["callee:00c57f80:8"]]
+ 0044cc68 ["INT_ADD", "register:40f0:8", ["const:44cc68:8", "const:4:8"]]
+ 0044cc68 ["CALL", null, ["callee:00c57f80:8"]]
- 0044cc28 bytes a22c2094
+ 0044cc68 bytes c62c2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c9851488a28e9dabf142b2c7bc7df0c"></a>

### [`0044cdb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044cdb4.md) → [`0044cdf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044c/0044cdf4.md) FUN_0044cdf4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008fed30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fe/008fed30.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`008fed84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008fe/008fed84.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.49% / 新版 91.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044ce20",
      "incomplete_value": true,
      "site": "0044ce34",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044cde0",
      "incomplete_value": true,
      "site": "0044cdf4",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b9a:8"
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
      "definition_site": "0044ce38",
      "incomplete_value": true,
      "site": "0044ce38",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044cdf8",
      "incomplete_value": true,
      "site": "0044cdf8",
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
                "const:e:8"
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
      "definition_site": "0044ce44",
      "incomplete_value": false,
      "site": "0044ce4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d89:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044ce04",
      "incomplete_value": false,
      "site": "0044ce0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
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
      "0044ce20",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044ce2c",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044ce44",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044ce20",
      "READ",
      [
        "storage",
        "002bfb46",
        null,
        "string"
      ]
    ],
    [
      "0044ce2c",
      "READ",
      [
        "storage",
        "002bfb54",
        null,
        "string"
      ]
    ],
    [
      "0044ce44",
      "PARAM",
      [
        "storage",
        "002a1d89",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044ce04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044cdb4.md#insn-0044ce04) · [`0044ce0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044cdb4.md#insn-0044ce0c) · [`0044ce34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044cdb4.md#insn-0044ce34)
- 新版 [`0044ce44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044c/0044cdf4.md#insn-0044ce44) · [`0044ce4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044c/0044cdf4.md#insn-0044ce4c) · [`0044ce74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044c/0044cdf4.md#insn-0044ce74)

~~~diff
- 0044ce04 ["COPY", "tmp:0:8", ["const:dd6:8"]]
- 0044ce04 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044ce04 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044ce04 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044ce44 ["COPY", "tmp:0:8", ["const:d89:8"]]
+ 0044ce44 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044ce44 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044ce44 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044ce04 bytes 21583791
+ 0044ce44 bytes 21243691
- 0044ce0c ["INT_ADD", "register:40f0:8", ["const:44ce0c:8", "const:4:8"]]
- 0044ce0c ["CALL", null, ["callee:00c58040:8"]]
+ 0044ce4c ["INT_ADD", "register:40f0:8", ["const:44ce4c:8", "const:4:8"]]
+ 0044ce4c ["CALL", null, ["callee:00c58040:8"]]
- 0044ce0c bytes 592c2094
+ 0044ce4c bytes 7d2c2094
- 0044ce34 ["INT_ADD", "register:40f0:8", ["const:44ce34:8", "const:4:8"]]
- 0044ce34 ["CALL", null, ["callee:00c57f80:8"]]
+ 0044ce74 ["INT_ADD", "register:40f0:8", ["const:44ce74:8", "const:4:8"]]
+ 0044ce74 ["CALL", null, ["callee:00c57f80:8"]]
- 0044ce34 bytes 1f2c2094
+ 0044ce74 bytes 432c2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65bc6f563e5555f33ede98936cdda6e2"></a>

### [`0044cfc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044cfc0.md) → [`0044d000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044d000.md) FUN_0044d000

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008fed30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fe/008fed30.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`008fed84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008fe/008fed84.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.49% / 新版 91.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044d02c",
      "incomplete_value": true,
      "site": "0044d040",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044cfec",
      "incomplete_value": true,
      "site": "0044d000",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b9a:8"
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
      "definition_site": "0044d044",
      "incomplete_value": true,
      "site": "0044d044",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044d004",
      "incomplete_value": true,
      "site": "0044d004",
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
                "const:e:8"
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
      "definition_site": "0044d050",
      "incomplete_value": false,
      "site": "0044d058",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d89:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044d010",
      "incomplete_value": false,
      "site": "0044d018",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
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
      "0044d02c",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044d038",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044d050",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044d02c",
      "READ",
      [
        "storage",
        "002bfb46",
        null,
        "string"
      ]
    ],
    [
      "0044d038",
      "READ",
      [
        "storage",
        "002bfb54",
        null,
        "string"
      ]
    ],
    [
      "0044d050",
      "PARAM",
      [
        "storage",
        "002a1d89",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044d010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044cfc0.md#insn-0044d010) · [`0044d018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044cfc0.md#insn-0044d018) · [`0044d040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044cfc0.md#insn-0044d040)
- 新版 [`0044d050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044d000.md#insn-0044d050) · [`0044d058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044d000.md#insn-0044d058) · [`0044d080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044d000.md#insn-0044d080)

~~~diff
- 0044d010 ["COPY", "tmp:0:8", ["const:dd6:8"]]
- 0044d010 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044d010 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044d010 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044d050 ["COPY", "tmp:0:8", ["const:d89:8"]]
+ 0044d050 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044d050 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044d050 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044d010 bytes 21583791
+ 0044d050 bytes 21243691
- 0044d018 ["INT_ADD", "register:40f0:8", ["const:44d018:8", "const:4:8"]]
- 0044d018 ["CALL", null, ["callee:00c58040:8"]]
+ 0044d058 ["INT_ADD", "register:40f0:8", ["const:44d058:8", "const:4:8"]]
+ 0044d058 ["CALL", null, ["callee:00c58040:8"]]
- 0044d018 bytes d62b2094
+ 0044d058 bytes fa2b2094
- 0044d040 ["INT_ADD", "register:40f0:8", ["const:44d040:8", "const:4:8"]]
- 0044d040 ["CALL", null, ["callee:00c57f80:8"]]
+ 0044d080 ["INT_ADD", "register:40f0:8", ["const:44d080:8", "const:4:8"]]
+ 0044d080 ["CALL", null, ["callee:00c57f80:8"]]
- 0044d040 bytes 9c2b2094
+ 0044d080 bytes c02b2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e84e809b0a0f70039c4e3d8404d7c464"></a>

### [`0044d1cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044d1cc.md) → [`0044d20c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044d20c.md) FUN_0044d20c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0091a294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0091a/0091a294.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`0091a2e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0091a/0091a2e8.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.18% / 新版 93.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044d244",
      "incomplete_value": true,
      "site": "0044d258",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044d204",
      "incomplete_value": true,
      "site": "0044d218",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b9a:8"
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
      "definition_site": "0044d25c",
      "incomplete_value": true,
      "site": "0044d25c",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044d21c",
      "incomplete_value": true,
      "site": "0044d21c",
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
                "const:e:8"
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
      "definition_site": "0044d264",
      "incomplete_value": false,
      "site": "0044d26c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d89:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044d224",
      "incomplete_value": false,
      "site": "0044d22c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
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
      "0044d244",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044d248",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044d264",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044d244",
      "READ",
      [
        "storage",
        "002bfb46",
        null,
        "string"
      ]
    ],
    [
      "0044d248",
      "READ",
      [
        "storage",
        "002bfb54",
        null,
        "string"
      ]
    ],
    [
      "0044d264",
      "PARAM",
      [
        "storage",
        "002a1d89",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044d224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044d1cc.md#insn-0044d224) · [`0044d22c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044d1cc.md#insn-0044d22c) · [`0044d25c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044d1cc.md#insn-0044d25c)
- 新版 [`0044d264`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044d20c.md#insn-0044d264) · [`0044d26c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044d20c.md#insn-0044d26c) · [`0044d29c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044d20c.md#insn-0044d29c)

~~~diff
- 0044d224 ["COPY", "tmp:0:8", ["const:dd6:8"]]
- 0044d224 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044d224 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044d224 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044d264 ["COPY", "tmp:0:8", ["const:d89:8"]]
+ 0044d264 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044d264 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044d264 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044d224 bytes 21583791
+ 0044d264 bytes 21243691
- 0044d22c ["INT_ADD", "register:40f0:8", ["const:44d22c:8", "const:4:8"]]
- 0044d22c ["CALL", null, ["callee:00c58040:8"]]
+ 0044d26c ["INT_ADD", "register:40f0:8", ["const:44d26c:8", "const:4:8"]]
+ 0044d26c ["CALL", null, ["callee:00c58040:8"]]
- 0044d22c bytes 512b2094
+ 0044d26c bytes 752b2094
- 0044d25c ["COPY", "tmp:0:8", ["const:dec:8"]]
- 0044d25c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044d25c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044d25c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044d29c ["COPY", "tmp:0:8", ["const:d98:8"]]
+ 0044d29c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044d29c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044d29c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044d25c bytes 21b03791
+ 0044d29c bytes 21603691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2df76328da5eb0dbd10a9057d1c44678"></a>

### [`0044d4c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044d4c0.md) → [`0044d500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044d500.md) FUN_0044d500

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00914e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00914/00914e30.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)
- 新版 呼出元 1件 [`00914e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00914/00914e84.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044d528",
      "incomplete_value": true,
      "site": "0044d538",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044d4e8",
      "incomplete_value": true,
      "site": "0044d4f8",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044d53c",
      "incomplete_value": true,
      "site": "0044d53c",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044d4fc",
      "incomplete_value": true,
      "site": "0044d4fc",
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
                "const:e:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044d548",
      "incomplete_value": false,
      "site": "0044d550",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d89:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044d508",
      "incomplete_value": false,
      "site": "0044d510",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
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
      "0044d528",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044d530",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044d548",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044d528",
      "READ",
      [
        "storage",
        "002bfb46",
        null,
        "string"
      ]
    ],
    [
      "0044d530",
      "READ",
      [
        "storage",
        "002bfb54",
        null,
        "string"
      ]
    ],
    [
      "0044d548",
      "PARAM",
      [
        "storage",
        "002a1d89",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044d508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044d4c0.md#insn-0044d508) · [`0044d510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044d4c0.md#insn-0044d510) · [`0044d538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044d4c0.md#insn-0044d538)
- 新版 [`0044d548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044d500.md#insn-0044d548) · [`0044d550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044d500.md#insn-0044d550) · [`0044d578`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044d500.md#insn-0044d578)

~~~diff
- 0044d508 ["COPY", "tmp:0:8", ["const:dd6:8"]]
- 0044d508 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044d508 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044d508 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044d548 ["COPY", "tmp:0:8", ["const:d89:8"]]
+ 0044d548 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044d548 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044d548 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044d508 bytes 21583791
+ 0044d548 bytes 21243691
- 0044d510 ["INT_ADD", "register:40f0:8", ["const:44d510:8", "const:4:8"]]
- 0044d510 ["CALL", null, ["callee:00c58040:8"]]
+ 0044d550 ["INT_ADD", "register:40f0:8", ["const:44d550:8", "const:4:8"]]
+ 0044d550 ["CALL", null, ["callee:00c58040:8"]]
- 0044d510 bytes 982a2094
+ 0044d550 bytes bc2a2094
- 0044d538 ["INT_ADD", "register:40f0:8", ["const:44d538:8", "const:4:8"]]
- 0044d538 ["CALL", null, ["callee:00c57f80:8"]]
+ 0044d578 ["INT_ADD", "register:40f0:8", ["const:44d578:8", "const:4:8"]]
+ 0044d578 ["CALL", null, ["callee:00c57f80:8"]]
- 0044d538 bytes 5e2a2094
+ 0044d578 bytes 822a2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd236be57263b55462f6d2dcea38e112"></a>

### [`0044d5d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044d5d8.md) → [`0044d618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044d618.md) FUN_0044d618

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)
- 新版 呼出元 1件 [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044d640",
      "incomplete_value": true,
      "site": "0044d650",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044d600",
      "incomplete_value": true,
      "site": "0044d610",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044d654",
      "incomplete_value": true,
      "site": "0044d654",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044d614",
      "incomplete_value": true,
      "site": "0044d614",
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
                "const:e:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044d660",
      "incomplete_value": false,
      "site": "0044d668",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d89:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044d620",
      "incomplete_value": false,
      "site": "0044d628",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
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
      "0044d640",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044d648",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044d660",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044d640",
      "READ",
      [
        "storage",
        "002bfb46",
        null,
        "string"
      ]
    ],
    [
      "0044d648",
      "READ",
      [
        "storage",
        "002bfb54",
        null,
        "string"
      ]
    ],
    [
      "0044d660",
      "PARAM",
      [
        "storage",
        "002a1d89",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044d620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044d5d8.md#insn-0044d620) · [`0044d628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044d5d8.md#insn-0044d628) · [`0044d650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044d5d8.md#insn-0044d650)
- 新版 [`0044d660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044d618.md#insn-0044d660) · [`0044d668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044d618.md#insn-0044d668) · [`0044d690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044d618.md#insn-0044d690)

~~~diff
- 0044d620 ["COPY", "tmp:0:8", ["const:dd6:8"]]
- 0044d620 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044d620 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044d620 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044d660 ["COPY", "tmp:0:8", ["const:d89:8"]]
+ 0044d660 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044d660 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044d660 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044d620 bytes 21583791
+ 0044d660 bytes 21243691
- 0044d628 ["INT_ADD", "register:40f0:8", ["const:44d628:8", "const:4:8"]]
- 0044d628 ["CALL", null, ["callee:00c58040:8"]]
+ 0044d668 ["INT_ADD", "register:40f0:8", ["const:44d668:8", "const:4:8"]]
+ 0044d668 ["CALL", null, ["callee:00c58040:8"]]
- 0044d628 bytes 522a2094
+ 0044d668 bytes 762a2094
- 0044d650 ["INT_ADD", "register:40f0:8", ["const:44d650:8", "const:4:8"]]
- 0044d650 ["CALL", null, ["callee:00c57f80:8"]]
+ 0044d690 ["INT_ADD", "register:40f0:8", ["const:44d690:8", "const:4:8"]]
+ 0044d690 ["CALL", null, ["callee:00c57f80:8"]]
- 0044d650 bytes 182a2094
+ 0044d690 bytes 3c2a2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-707a4484d14efddede78468c3f733d1b"></a>

### [`0044d6f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044d6f0.md) → [`0044d730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044d730.md) FUN_0044d730

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0093b770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093b/0093b770.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)
- 新版 呼出元 7件 [`006ea54c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ea/006ea54c.md) [`006ecde8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ec/006ecde8.md) [`006ef79c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ef/006ef79c.md) [`006fda84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006fd/006fda84.md) [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044d758",
      "incomplete_value": true,
      "site": "0044d768",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044d718",
      "incomplete_value": true,
      "site": "0044d728",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044d76c",
      "incomplete_value": true,
      "site": "0044d76c",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044d72c",
      "incomplete_value": true,
      "site": "0044d72c",
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
                "const:e:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044d778",
      "incomplete_value": false,
      "site": "0044d780",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d89:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044d738",
      "incomplete_value": false,
      "site": "0044d740",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
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
      "0044d758",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044d760",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044d778",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044d758",
      "READ",
      [
        "storage",
        "002bfb46",
        null,
        "string"
      ]
    ],
    [
      "0044d760",
      "READ",
      [
        "storage",
        "002bfb54",
        null,
        "string"
      ]
    ],
    [
      "0044d778",
      "PARAM",
      [
        "storage",
        "002a1d89",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044d738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044d6f0.md#insn-0044d738) · [`0044d740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044d6f0.md#insn-0044d740) · [`0044d768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044d6f0.md#insn-0044d768)
- 新版 [`0044d778`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044d730.md#insn-0044d778) · [`0044d780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044d730.md#insn-0044d780) · [`0044d7a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044d730.md#insn-0044d7a8)

~~~diff
- 0044d738 ["COPY", "tmp:0:8", ["const:dd6:8"]]
- 0044d738 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044d738 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044d738 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044d778 ["COPY", "tmp:0:8", ["const:d89:8"]]
+ 0044d778 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044d778 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044d778 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044d738 bytes 21583791
+ 0044d778 bytes 21243691
- 0044d740 ["INT_ADD", "register:40f0:8", ["const:44d740:8", "const:4:8"]]
- 0044d740 ["CALL", null, ["callee:00c58040:8"]]
+ 0044d780 ["INT_ADD", "register:40f0:8", ["const:44d780:8", "const:4:8"]]
+ 0044d780 ["CALL", null, ["callee:00c58040:8"]]
- 0044d740 bytes 0c2a2094
+ 0044d780 bytes 302a2094
- 0044d768 ["INT_ADD", "register:40f0:8", ["const:44d768:8", "const:4:8"]]
- 0044d768 ["CALL", null, ["callee:00c57f80:8"]]
+ 0044d7a8 ["INT_ADD", "register:40f0:8", ["const:44d7a8:8", "const:4:8"]]
+ 0044d7a8 ["CALL", null, ["callee:00c57f80:8"]]
- 0044d768 bytes d2292094
+ 0044d7a8 bytes f6292094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43c836b0667ae2972e4195a54f9d35e4"></a>

### [`0044d808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044d808.md) → [`0044d848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044d848.md) FUN_0044d848

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)
- 新版 呼出元 2件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`00856e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856e84.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044d870",
      "incomplete_value": true,
      "site": "0044d880",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044d830",
      "incomplete_value": true,
      "site": "0044d840",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044d884",
      "incomplete_value": true,
      "site": "0044d884",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044d844",
      "incomplete_value": true,
      "site": "0044d844",
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
                "const:e:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044d890",
      "incomplete_value": false,
      "site": "0044d898",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d89:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044d850",
      "incomplete_value": false,
      "site": "0044d858",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
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
      "0044d870",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044d878",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044d890",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044d870",
      "READ",
      [
        "storage",
        "002bfb46",
        null,
        "string"
      ]
    ],
    [
      "0044d878",
      "READ",
      [
        "storage",
        "002bfb54",
        null,
        "string"
      ]
    ],
    [
      "0044d890",
      "PARAM",
      [
        "storage",
        "002a1d89",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044d850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044d808.md#insn-0044d850) · [`0044d858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044d808.md#insn-0044d858) · [`0044d880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044d808.md#insn-0044d880)
- 新版 [`0044d890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044d848.md#insn-0044d890) · [`0044d898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044d848.md#insn-0044d898) · [`0044d8c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044d848.md#insn-0044d8c0)

~~~diff
- 0044d850 ["COPY", "tmp:0:8", ["const:dd6:8"]]
- 0044d850 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044d850 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044d850 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044d890 ["COPY", "tmp:0:8", ["const:d89:8"]]
+ 0044d890 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044d890 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044d890 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044d850 bytes 21583791
+ 0044d890 bytes 21243691
- 0044d858 ["INT_ADD", "register:40f0:8", ["const:44d858:8", "const:4:8"]]
- 0044d858 ["CALL", null, ["callee:00c58040:8"]]
+ 0044d898 ["INT_ADD", "register:40f0:8", ["const:44d898:8", "const:4:8"]]
+ 0044d898 ["CALL", null, ["callee:00c58040:8"]]
- 0044d858 bytes c6292094
+ 0044d898 bytes ea292094
- 0044d880 ["INT_ADD", "register:40f0:8", ["const:44d880:8", "const:4:8"]]
- 0044d880 ["CALL", null, ["callee:00c57f80:8"]]
+ 0044d8c0 ["INT_ADD", "register:40f0:8", ["const:44d8c0:8", "const:4:8"]]
+ 0044d8c0 ["CALL", null, ["callee:00c57f80:8"]]
- 0044d880 bytes 8c292094
+ 0044d8c0 bytes b0292094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7394b097793b7bc51f93347d4597dffb"></a>

### [`0044d920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044d920.md) → [`0044d960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044d960.md) FUN_0044d960

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005c6978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c6/005c6978.md) [`00a75dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a75/00a75dac.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)
- 新版 呼出元 2件 [`005c69b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c6/005c69b8.md) [`00a75e1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a75/00a75e1c.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044d988",
      "incomplete_value": true,
      "site": "0044d998",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044d948",
      "incomplete_value": true,
      "site": "0044d958",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044d99c",
      "incomplete_value": true,
      "site": "0044d99c",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044d95c",
      "incomplete_value": true,
      "site": "0044d95c",
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
                "const:e:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044d9a8",
      "incomplete_value": false,
      "site": "0044d9b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d89:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044d968",
      "incomplete_value": false,
      "site": "0044d970",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
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
      "0044d988",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044d990",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044d9a8",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044d988",
      "READ",
      [
        "storage",
        "002bfb46",
        null,
        "string"
      ]
    ],
    [
      "0044d990",
      "READ",
      [
        "storage",
        "002bfb54",
        null,
        "string"
      ]
    ],
    [
      "0044d9a8",
      "PARAM",
      [
        "storage",
        "002a1d89",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044d968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044d920.md#insn-0044d968) · [`0044d970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044d920.md#insn-0044d970) · [`0044d998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044d920.md#insn-0044d998)
- 新版 [`0044d9a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044d960.md#insn-0044d9a8) · [`0044d9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044d960.md#insn-0044d9b0) · [`0044d9d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044d960.md#insn-0044d9d8)

~~~diff
- 0044d968 ["COPY", "tmp:0:8", ["const:dd6:8"]]
- 0044d968 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044d968 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044d968 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044d9a8 ["COPY", "tmp:0:8", ["const:d89:8"]]
+ 0044d9a8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044d9a8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044d9a8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044d968 bytes 21583791
+ 0044d9a8 bytes 21243691
- 0044d970 ["INT_ADD", "register:40f0:8", ["const:44d970:8", "const:4:8"]]
- 0044d970 ["CALL", null, ["callee:00c58040:8"]]
+ 0044d9b0 ["INT_ADD", "register:40f0:8", ["const:44d9b0:8", "const:4:8"]]
+ 0044d9b0 ["CALL", null, ["callee:00c58040:8"]]
- 0044d970 bytes 80292094
+ 0044d9b0 bytes a4292094
- 0044d998 ["INT_ADD", "register:40f0:8", ["const:44d998:8", "const:4:8"]]
- 0044d998 ["CALL", null, ["callee:00c57f80:8"]]
+ 0044d9d8 ["INT_ADD", "register:40f0:8", ["const:44d9d8:8", "const:4:8"]]
+ 0044d9d8 ["CALL", null, ["callee:00c57f80:8"]]
- 0044d998 bytes 46292094
+ 0044d9d8 bytes 6a292094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cdb2448588fc41d5b3eee334f33f6346"></a>

### [`0044da38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044da38.md) → [`0044da78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044da78.md) FUN_0044da78

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`008d31f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d3/008d31f8.md) [`008d9c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d9c04.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)
- 新版 呼出元 2件 [`008d324c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d3/008d324c.md) [`008d9c58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d9/008d9c58.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044daa0",
      "incomplete_value": true,
      "site": "0044dab0",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044da60",
      "incomplete_value": true,
      "site": "0044da70",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044dab4",
      "incomplete_value": true,
      "site": "0044dab4",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044da74",
      "incomplete_value": true,
      "site": "0044da74",
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
                "const:e:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044dac0",
      "incomplete_value": false,
      "site": "0044dac8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d89:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044da80",
      "incomplete_value": false,
      "site": "0044da88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
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
      "0044daa0",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044daa8",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044dac0",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044daa0",
      "READ",
      [
        "storage",
        "002bfb46",
        null,
        "string"
      ]
    ],
    [
      "0044daa8",
      "READ",
      [
        "storage",
        "002bfb54",
        null,
        "string"
      ]
    ],
    [
      "0044dac0",
      "PARAM",
      [
        "storage",
        "002a1d89",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044da80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044da38.md#insn-0044da80) · [`0044da88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044da38.md#insn-0044da88) · [`0044dab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044da38.md#insn-0044dab0)
- 新版 [`0044dac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044da78.md#insn-0044dac0) · [`0044dac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044da78.md#insn-0044dac8) · [`0044daf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044da78.md#insn-0044daf0)

~~~diff
- 0044da80 ["COPY", "tmp:0:8", ["const:dd6:8"]]
- 0044da80 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044da80 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044da80 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044dac0 ["COPY", "tmp:0:8", ["const:d89:8"]]
+ 0044dac0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044dac0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044dac0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044da80 bytes 21583791
+ 0044dac0 bytes 21243691
- 0044da88 ["INT_ADD", "register:40f0:8", ["const:44da88:8", "const:4:8"]]
- 0044da88 ["CALL", null, ["callee:00c58040:8"]]
+ 0044dac8 ["INT_ADD", "register:40f0:8", ["const:44dac8:8", "const:4:8"]]
+ 0044dac8 ["CALL", null, ["callee:00c58040:8"]]
- 0044da88 bytes 3a292094
+ 0044dac8 bytes 5e292094
- 0044dab0 ["INT_ADD", "register:40f0:8", ["const:44dab0:8", "const:4:8"]]
- 0044dab0 ["CALL", null, ["callee:00c57f80:8"]]
+ 0044daf0 ["INT_ADD", "register:40f0:8", ["const:44daf0:8", "const:4:8"]]
+ 0044daf0 ["CALL", null, ["callee:00c57f80:8"]]
- 0044dab0 bytes 00292094
+ 0044daf0 bytes 24292094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-153b79b26ef4c18ad18debe8274ca89d"></a>

### [`0044db50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044db50.md) → [`0044db90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044db90.md) FUN_0044db90

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00657f8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00657/00657f8c.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)
- 新版 呼出元 1件 [`00657fcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00657/00657fcc.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044dbb8",
      "incomplete_value": true,
      "site": "0044dbc8",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044db78",
      "incomplete_value": true,
      "site": "0044db88",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044dbcc",
      "incomplete_value": true,
      "site": "0044dbcc",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044db8c",
      "incomplete_value": true,
      "site": "0044db8c",
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
                "const:e:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044dbd8",
      "incomplete_value": false,
      "site": "0044dbe0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d89:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044db98",
      "incomplete_value": false,
      "site": "0044dba0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
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
      "0044dbb8",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044dbc0",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044dbd8",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044dbb8",
      "READ",
      [
        "storage",
        "002bfb46",
        null,
        "string"
      ]
    ],
    [
      "0044dbc0",
      "READ",
      [
        "storage",
        "002bfb54",
        null,
        "string"
      ]
    ],
    [
      "0044dbd8",
      "PARAM",
      [
        "storage",
        "002a1d89",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044db98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044db50.md#insn-0044db98) · [`0044dba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044db50.md#insn-0044dba0) · [`0044dbc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044db50.md#insn-0044dbc8)
- 新版 [`0044dbd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044db90.md#insn-0044dbd8) · [`0044dbe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044db90.md#insn-0044dbe0) · [`0044dc08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044db90.md#insn-0044dc08)

~~~diff
- 0044db98 ["COPY", "tmp:0:8", ["const:dd6:8"]]
- 0044db98 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044db98 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044db98 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044dbd8 ["COPY", "tmp:0:8", ["const:d89:8"]]
+ 0044dbd8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044dbd8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044dbd8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044db98 bytes 21583791
+ 0044dbd8 bytes 21243691
- 0044dba0 ["INT_ADD", "register:40f0:8", ["const:44dba0:8", "const:4:8"]]
- 0044dba0 ["CALL", null, ["callee:00c58040:8"]]
+ 0044dbe0 ["INT_ADD", "register:40f0:8", ["const:44dbe0:8", "const:4:8"]]
+ 0044dbe0 ["CALL", null, ["callee:00c58040:8"]]
- 0044dba0 bytes f4282094
+ 0044dbe0 bytes 18292094
- 0044dbc8 ["INT_ADD", "register:40f0:8", ["const:44dbc8:8", "const:4:8"]]
- 0044dbc8 ["CALL", null, ["callee:00c57f80:8"]]
+ 0044dc08 ["INT_ADD", "register:40f0:8", ["const:44dc08:8", "const:4:8"]]
+ 0044dc08 ["CALL", null, ["callee:00c57f80:8"]]
- 0044dbc8 bytes ba282094
+ 0044dc08 bytes de282094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-471173c6eb324d1845afd4c769d7d449"></a>

### [`0044dc68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044dc68.md) → [`0044dca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044dca8.md) FUN_0044dca8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0064ecb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064e/0064ecb8.md) [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)
- 新版 呼出元 1件 [`0064ecf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064e/0064ecf8.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044dcd0",
      "incomplete_value": true,
      "site": "0044dce0",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044dc90",
      "incomplete_value": true,
      "site": "0044dca0",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044dce4",
      "incomplete_value": true,
      "site": "0044dce4",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044dca4",
      "incomplete_value": true,
      "site": "0044dca4",
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
                "const:e:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044dcf0",
      "incomplete_value": false,
      "site": "0044dcf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d89:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044dcb0",
      "incomplete_value": false,
      "site": "0044dcb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
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
      "0044dcd0",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044dcd8",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044dcf0",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044dcd0",
      "READ",
      [
        "storage",
        "002bfb46",
        null,
        "string"
      ]
    ],
    [
      "0044dcd8",
      "READ",
      [
        "storage",
        "002bfb54",
        null,
        "string"
      ]
    ],
    [
      "0044dcf0",
      "PARAM",
      [
        "storage",
        "002a1d89",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044dcb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044dc68.md#insn-0044dcb0) · [`0044dcb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044dc68.md#insn-0044dcb8) · [`0044dce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044dc68.md#insn-0044dce0)
- 新版 [`0044dcf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044dca8.md#insn-0044dcf0) · [`0044dcf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044dca8.md#insn-0044dcf8) · [`0044dd20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044dca8.md#insn-0044dd20)

~~~diff
- 0044dcb0 ["COPY", "tmp:0:8", ["const:dd6:8"]]
- 0044dcb0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044dcb0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044dcb0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044dcf0 ["COPY", "tmp:0:8", ["const:d89:8"]]
+ 0044dcf0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044dcf0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044dcf0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044dcb0 bytes 21583791
+ 0044dcf0 bytes 21243691
- 0044dcb8 ["INT_ADD", "register:40f0:8", ["const:44dcb8:8", "const:4:8"]]
- 0044dcb8 ["CALL", null, ["callee:00c58040:8"]]
+ 0044dcf8 ["INT_ADD", "register:40f0:8", ["const:44dcf8:8", "const:4:8"]]
+ 0044dcf8 ["CALL", null, ["callee:00c58040:8"]]
- 0044dcb8 bytes ae282094
+ 0044dcf8 bytes d2282094
- 0044dce0 ["INT_ADD", "register:40f0:8", ["const:44dce0:8", "const:4:8"]]
- 0044dce0 ["CALL", null, ["callee:00c57f80:8"]]
+ 0044dd20 ["INT_ADD", "register:40f0:8", ["const:44dd20:8", "const:4:8"]]
+ 0044dd20 ["CALL", null, ["callee:00c57f80:8"]]
- 0044dce0 bytes 74282094
+ 0044dd20 bytes 98282094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6114a20dde9fefdf5a818b45e41e9f23"></a>

### [`0044dd80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044dd80.md) → [`0044ddc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044ddc0.md) FUN_0044ddc0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0086f91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086f/0086f91c.md) [`008959d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00895/008959d0.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)
- 新版 呼出元 2件 [`0086f974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086f/0086f974.md) [`00895a28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00895/00895a28.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044dde8",
      "incomplete_value": true,
      "site": "0044ddf8",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044dda8",
      "incomplete_value": true,
      "site": "0044ddb8",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044ddfc",
      "incomplete_value": true,
      "site": "0044ddfc",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044ddbc",
      "incomplete_value": true,
      "site": "0044ddbc",
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
                "const:e:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044de08",
      "incomplete_value": false,
      "site": "0044de10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d89:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044ddc8",
      "incomplete_value": false,
      "site": "0044ddd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
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
      "0044dde8",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044ddf0",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044de08",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044dde8",
      "READ",
      [
        "storage",
        "002bfb46",
        null,
        "string"
      ]
    ],
    [
      "0044ddf0",
      "READ",
      [
        "storage",
        "002bfb54",
        null,
        "string"
      ]
    ],
    [
      "0044de08",
      "PARAM",
      [
        "storage",
        "002a1d89",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044ddc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044dd80.md#insn-0044ddc8) · [`0044ddd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044dd80.md#insn-0044ddd0) · [`0044ddf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044dd80.md#insn-0044ddf8)
- 新版 [`0044de08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044ddc0.md#insn-0044de08) · [`0044de10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044ddc0.md#insn-0044de10) · [`0044de38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044ddc0.md#insn-0044de38)

~~~diff
- 0044ddc8 ["COPY", "tmp:0:8", ["const:dd6:8"]]
- 0044ddc8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044ddc8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044ddc8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044de08 ["COPY", "tmp:0:8", ["const:d89:8"]]
+ 0044de08 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044de08 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044de08 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044ddc8 bytes 21583791
+ 0044de08 bytes 21243691
- 0044ddd0 ["INT_ADD", "register:40f0:8", ["const:44ddd0:8", "const:4:8"]]
- 0044ddd0 ["CALL", null, ["callee:00c58040:8"]]
+ 0044de10 ["INT_ADD", "register:40f0:8", ["const:44de10:8", "const:4:8"]]
+ 0044de10 ["CALL", null, ["callee:00c58040:8"]]
- 0044ddd0 bytes 68282094
+ 0044de10 bytes 8c282094
- 0044ddf8 ["INT_ADD", "register:40f0:8", ["const:44ddf8:8", "const:4:8"]]
- 0044ddf8 ["CALL", null, ["callee:00c57f80:8"]]
+ 0044de38 ["INT_ADD", "register:40f0:8", ["const:44de38:8", "const:4:8"]]
+ 0044de38 ["CALL", null, ["callee:00c57f80:8"]]
- 0044ddf8 bytes 2e282094
+ 0044de38 bytes 52282094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3074c6543726a47bd0e207aef0c6a918"></a>

### [`0044de98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044de98.md) → [`0044ded8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044ded8.md) FUN_0044ded8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`008cabc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ca/008cabc0.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)
- 新版 呼出元 1件 [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044df00",
      "incomplete_value": true,
      "site": "0044df10",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044dec0",
      "incomplete_value": true,
      "site": "0044ded0",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044df14",
      "incomplete_value": true,
      "site": "0044df14",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044ded4",
      "incomplete_value": true,
      "site": "0044ded4",
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
                "const:e:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044df20",
      "incomplete_value": false,
      "site": "0044df28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d89:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044dee0",
      "incomplete_value": false,
      "site": "0044dee8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
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
      "0044df00",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044df08",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044df20",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044df00",
      "READ",
      [
        "storage",
        "002bfb46",
        null,
        "string"
      ]
    ],
    [
      "0044df08",
      "READ",
      [
        "storage",
        "002bfb54",
        null,
        "string"
      ]
    ],
    [
      "0044df20",
      "PARAM",
      [
        "storage",
        "002a1d89",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044dee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044de98.md#insn-0044dee0) · [`0044dee8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044de98.md#insn-0044dee8) · [`0044df10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044de98.md#insn-0044df10)
- 新版 [`0044df20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044ded8.md#insn-0044df20) · [`0044df28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044ded8.md#insn-0044df28) · [`0044df50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044ded8.md#insn-0044df50)

~~~diff
- 0044dee0 ["COPY", "tmp:0:8", ["const:dd6:8"]]
- 0044dee0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044dee0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044dee0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044df20 ["COPY", "tmp:0:8", ["const:d89:8"]]
+ 0044df20 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044df20 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044df20 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044dee0 bytes 21583791
+ 0044df20 bytes 21243691
- 0044dee8 ["INT_ADD", "register:40f0:8", ["const:44dee8:8", "const:4:8"]]
- 0044dee8 ["CALL", null, ["callee:00c58040:8"]]
+ 0044df28 ["INT_ADD", "register:40f0:8", ["const:44df28:8", "const:4:8"]]
+ 0044df28 ["CALL", null, ["callee:00c58040:8"]]
- 0044dee8 bytes 22282094
+ 0044df28 bytes 46282094
- 0044df10 ["INT_ADD", "register:40f0:8", ["const:44df10:8", "const:4:8"]]
- 0044df10 ["CALL", null, ["callee:00c57f80:8"]]
+ 0044df50 ["INT_ADD", "register:40f0:8", ["const:44df50:8", "const:4:8"]]
+ 0044df50 ["CALL", null, ["callee:00c57f80:8"]]
- 0044df10 bytes e8272094
+ 0044df50 bytes 0c282094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75700a45888621d5ae44fa0d46586c46"></a>

### [`0044dfb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044dfb0.md) → [`0044dff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044dff0.md) FUN_0044dff0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)
- 新版 呼出元 1件 [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044e018",
      "incomplete_value": true,
      "site": "0044e028",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044dfd8",
      "incomplete_value": true,
      "site": "0044dfe8",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044e02c",
      "incomplete_value": true,
      "site": "0044e02c",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044dfec",
      "incomplete_value": true,
      "site": "0044dfec",
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
                "const:e:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044e038",
      "incomplete_value": false,
      "site": "0044e040",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d89:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044dff8",
      "incomplete_value": false,
      "site": "0044e000",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
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
      "0044e018",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044e020",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044e038",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044e018",
      "READ",
      [
        "storage",
        "002bfb46",
        null,
        "string"
      ]
    ],
    [
      "0044e020",
      "READ",
      [
        "storage",
        "002bfb54",
        null,
        "string"
      ]
    ],
    [
      "0044e038",
      "PARAM",
      [
        "storage",
        "002a1d89",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044dff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044dfb0.md#insn-0044dff8) · [`0044e000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044dfb0.md#insn-0044e000) · [`0044e028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044dfb0.md#insn-0044e028)
- 新版 [`0044e038`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044dff0.md#insn-0044e038) · [`0044e040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044dff0.md#insn-0044e040) · [`0044e068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044dff0.md#insn-0044e068)

~~~diff
- 0044dff8 ["COPY", "tmp:0:8", ["const:dd6:8"]]
- 0044dff8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044dff8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044dff8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044e038 ["COPY", "tmp:0:8", ["const:d89:8"]]
+ 0044e038 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044e038 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044e038 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044dff8 bytes 21583791
+ 0044e038 bytes 21243691
- 0044e000 ["INT_ADD", "register:40f0:8", ["const:44e000:8", "const:4:8"]]
- 0044e000 ["CALL", null, ["callee:00c58040:8"]]
+ 0044e040 ["INT_ADD", "register:40f0:8", ["const:44e040:8", "const:4:8"]]
+ 0044e040 ["CALL", null, ["callee:00c58040:8"]]
- 0044e000 bytes dc272094
+ 0044e040 bytes 00282094
- 0044e028 ["INT_ADD", "register:40f0:8", ["const:44e028:8", "const:4:8"]]
- 0044e028 ["CALL", null, ["callee:00c57f80:8"]]
+ 0044e068 ["INT_ADD", "register:40f0:8", ["const:44e068:8", "const:4:8"]]
+ 0044e068 ["CALL", null, ["callee:00c57f80:8"]]
- 0044e028 bytes a2272094
+ 0044e068 bytes c6272094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb7e3941d7210cddef346538f49e80e9"></a>

### [`0044e0c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e0c8.md) → [`0044e108`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044e108.md) FUN_0044e108

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)
- 新版 呼出元 11件 [`0075ebd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075e/0075ebd8.md) [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`0083f8dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083f/0083f8dc.md) [`0084e5f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0084e/0084e5f4.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044e130",
      "incomplete_value": true,
      "site": "0044e140",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044e0f0",
      "incomplete_value": true,
      "site": "0044e100",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044e144",
      "incomplete_value": true,
      "site": "0044e144",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044e104",
      "incomplete_value": true,
      "site": "0044e104",
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
                "const:e:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044e150",
      "incomplete_value": false,
      "site": "0044e158",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d89:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044e110",
      "incomplete_value": false,
      "site": "0044e118",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
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
      "0044e130",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044e138",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044e150",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044e130",
      "READ",
      [
        "storage",
        "002bfb46",
        null,
        "string"
      ]
    ],
    [
      "0044e138",
      "READ",
      [
        "storage",
        "002bfb54",
        null,
        "string"
      ]
    ],
    [
      "0044e150",
      "PARAM",
      [
        "storage",
        "002a1d89",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044e110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e0c8.md#insn-0044e110) · [`0044e118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e0c8.md#insn-0044e118) · [`0044e140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e0c8.md#insn-0044e140)
- 新版 [`0044e150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044e108.md#insn-0044e150) · [`0044e158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044e108.md#insn-0044e158) · [`0044e180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044e108.md#insn-0044e180)

~~~diff
- 0044e110 ["COPY", "tmp:0:8", ["const:dd6:8"]]
- 0044e110 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044e110 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044e110 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044e150 ["COPY", "tmp:0:8", ["const:d89:8"]]
+ 0044e150 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044e150 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044e150 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044e110 bytes 21583791
+ 0044e150 bytes 21243691
- 0044e118 ["INT_ADD", "register:40f0:8", ["const:44e118:8", "const:4:8"]]
- 0044e118 ["CALL", null, ["callee:00c58040:8"]]
+ 0044e158 ["INT_ADD", "register:40f0:8", ["const:44e158:8", "const:4:8"]]
+ 0044e158 ["CALL", null, ["callee:00c58040:8"]]
- 0044e118 bytes 96272094
+ 0044e158 bytes ba272094
- 0044e140 ["INT_ADD", "register:40f0:8", ["const:44e140:8", "const:4:8"]]
- 0044e140 ["CALL", null, ["callee:00c57f80:8"]]
+ 0044e180 ["INT_ADD", "register:40f0:8", ["const:44e180:8", "const:4:8"]]
+ 0044e180 ["CALL", null, ["callee:00c57f80:8"]]
- 0044e140 bytes 5c272094
+ 0044e180 bytes 80272094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf77511d3ecaef853d54138f0df18e2e"></a>

### [`0044e1e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e1e0.md) → [`0044e220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044e220.md) FUN_0044e220

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`0083f884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083f/0083f884.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)
- 新版 呼出元 5件 [`00677a80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00677/00677a80.md) [`00678920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00678/00678920.md) [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) [`00922e1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00922/00922e1c.md) [`0092491c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00924/0092491c.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044e248",
      "incomplete_value": true,
      "site": "0044e258",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044e208",
      "incomplete_value": true,
      "site": "0044e218",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044e25c",
      "incomplete_value": true,
      "site": "0044e25c",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044e21c",
      "incomplete_value": true,
      "site": "0044e21c",
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
                "const:e:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044e268",
      "incomplete_value": false,
      "site": "0044e270",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d89:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044e228",
      "incomplete_value": false,
      "site": "0044e230",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
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
      "0044e248",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044e250",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044e268",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044e248",
      "READ",
      [
        "storage",
        "002bfb46",
        null,
        "string"
      ]
    ],
    [
      "0044e250",
      "READ",
      [
        "storage",
        "002bfb54",
        null,
        "string"
      ]
    ],
    [
      "0044e268",
      "PARAM",
      [
        "storage",
        "002a1d89",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044e228`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e1e0.md#insn-0044e228) · [`0044e230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e1e0.md#insn-0044e230) · [`0044e258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e1e0.md#insn-0044e258)
- 新版 [`0044e268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044e220.md#insn-0044e268) · [`0044e270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044e220.md#insn-0044e270) · [`0044e298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044e220.md#insn-0044e298)

~~~diff
- 0044e228 ["COPY", "tmp:0:8", ["const:dd6:8"]]
- 0044e228 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044e228 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044e228 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044e268 ["COPY", "tmp:0:8", ["const:d89:8"]]
+ 0044e268 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044e268 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044e268 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044e228 bytes 21583791
+ 0044e268 bytes 21243691
- 0044e230 ["INT_ADD", "register:40f0:8", ["const:44e230:8", "const:4:8"]]
- 0044e230 ["CALL", null, ["callee:00c58040:8"]]
+ 0044e270 ["INT_ADD", "register:40f0:8", ["const:44e270:8", "const:4:8"]]
+ 0044e270 ["CALL", null, ["callee:00c58040:8"]]
- 0044e230 bytes 50272094
+ 0044e270 bytes 74272094
- 0044e258 ["INT_ADD", "register:40f0:8", ["const:44e258:8", "const:4:8"]]
- 0044e258 ["CALL", null, ["callee:00c57f80:8"]]
+ 0044e298 ["INT_ADD", "register:40f0:8", ["const:44e298:8", "const:4:8"]]
+ 0044e298 ["CALL", null, ["callee:00c57f80:8"]]
- 0044e258 bytes 16272094
+ 0044e298 bytes 3a272094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-342abbb6c5ad1685a1ac96018c213a97"></a>

### [`0044e2f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e2f8.md) → [`0044e338`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044e338.md) FUN_0044e338

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)
- 新版 呼出元 2件 [`00856e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856e84.md) [`0090dd50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0090d/0090dd50.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044e360",
      "incomplete_value": true,
      "site": "0044e370",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044e320",
      "incomplete_value": true,
      "site": "0044e330",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044e374",
      "incomplete_value": true,
      "site": "0044e374",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044e334",
      "incomplete_value": true,
      "site": "0044e334",
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
                "const:e:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044e380",
      "incomplete_value": false,
      "site": "0044e388",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d89:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044e340",
      "incomplete_value": false,
      "site": "0044e348",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
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
      "0044e360",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044e368",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044e380",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044e360",
      "READ",
      [
        "storage",
        "002bfb46",
        null,
        "string"
      ]
    ],
    [
      "0044e368",
      "READ",
      [
        "storage",
        "002bfb54",
        null,
        "string"
      ]
    ],
    [
      "0044e380",
      "PARAM",
      [
        "storage",
        "002a1d89",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044e340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e2f8.md#insn-0044e340) · [`0044e348`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e2f8.md#insn-0044e348) · [`0044e370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e2f8.md#insn-0044e370)
- 新版 [`0044e380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044e338.md#insn-0044e380) · [`0044e388`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044e338.md#insn-0044e388) · [`0044e3b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044e338.md#insn-0044e3b0)

~~~diff
- 0044e340 ["COPY", "tmp:0:8", ["const:dd6:8"]]
- 0044e340 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044e340 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044e340 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044e380 ["COPY", "tmp:0:8", ["const:d89:8"]]
+ 0044e380 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044e380 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044e380 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044e340 bytes 21583791
+ 0044e380 bytes 21243691
- 0044e348 ["INT_ADD", "register:40f0:8", ["const:44e348:8", "const:4:8"]]
- 0044e348 ["CALL", null, ["callee:00c58040:8"]]
+ 0044e388 ["INT_ADD", "register:40f0:8", ["const:44e388:8", "const:4:8"]]
+ 0044e388 ["CALL", null, ["callee:00c58040:8"]]
- 0044e348 bytes 0a272094
+ 0044e388 bytes 2e272094
- 0044e370 ["INT_ADD", "register:40f0:8", ["const:44e370:8", "const:4:8"]]
- 0044e370 ["CALL", null, ["callee:00c57f80:8"]]
+ 0044e3b0 ["INT_ADD", "register:40f0:8", ["const:44e3b0:8", "const:4:8"]]
+ 0044e3b0 ["CALL", null, ["callee:00c57f80:8"]]
- 0044e370 bytes d0262094
+ 0044e3b0 bytes f4262094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e77a62b842f4bd9a0839ec69acff6e79"></a>

### [`0044e410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e410.md) → [`0044e450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044e450.md) FUN_0044e450

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)
- 新版 呼出元 1件 [`00856e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856e84.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044e478",
      "incomplete_value": true,
      "site": "0044e488",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044e438",
      "incomplete_value": true,
      "site": "0044e448",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044e48c",
      "incomplete_value": true,
      "site": "0044e48c",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044e44c",
      "incomplete_value": true,
      "site": "0044e44c",
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
                "const:e:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044e498",
      "incomplete_value": false,
      "site": "0044e4a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d89:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044e458",
      "incomplete_value": false,
      "site": "0044e460",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
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
      "0044e478",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044e480",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044e498",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044e478",
      "READ",
      [
        "storage",
        "002bfb46",
        null,
        "string"
      ]
    ],
    [
      "0044e480",
      "READ",
      [
        "storage",
        "002bfb54",
        null,
        "string"
      ]
    ],
    [
      "0044e498",
      "PARAM",
      [
        "storage",
        "002a1d89",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044e458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e410.md#insn-0044e458) · [`0044e460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e410.md#insn-0044e460) · [`0044e488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e410.md#insn-0044e488)
- 新版 [`0044e498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044e450.md#insn-0044e498) · [`0044e4a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044e450.md#insn-0044e4a0) · [`0044e4c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044e450.md#insn-0044e4c8)

~~~diff
- 0044e458 ["COPY", "tmp:0:8", ["const:dd6:8"]]
- 0044e458 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044e458 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044e458 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044e498 ["COPY", "tmp:0:8", ["const:d89:8"]]
+ 0044e498 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044e498 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044e498 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044e458 bytes 21583791
+ 0044e498 bytes 21243691
- 0044e460 ["INT_ADD", "register:40f0:8", ["const:44e460:8", "const:4:8"]]
- 0044e460 ["CALL", null, ["callee:00c58040:8"]]
+ 0044e4a0 ["INT_ADD", "register:40f0:8", ["const:44e4a0:8", "const:4:8"]]
+ 0044e4a0 ["CALL", null, ["callee:00c58040:8"]]
- 0044e460 bytes c4262094
+ 0044e4a0 bytes e8262094
- 0044e488 ["INT_ADD", "register:40f0:8", ["const:44e488:8", "const:4:8"]]
- 0044e488 ["CALL", null, ["callee:00c57f80:8"]]
+ 0044e4c8 ["INT_ADD", "register:40f0:8", ["const:44e4c8:8", "const:4:8"]]
+ 0044e4c8 ["CALL", null, ["callee:00c57f80:8"]]
- 0044e488 bytes 8a262094
+ 0044e4c8 bytes ae262094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a37ca4a8b65f2c41b268abecf3f21072"></a>

### [`0044e528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e528.md) → [`0044e568`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044e568.md) FUN_0044e568

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)
- 新版 呼出元 1件 [`00856e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856e84.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044e590",
      "incomplete_value": true,
      "site": "0044e5a0",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044e550",
      "incomplete_value": true,
      "site": "0044e560",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044e5a4",
      "incomplete_value": true,
      "site": "0044e5a4",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044e564",
      "incomplete_value": true,
      "site": "0044e564",
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
                "const:e:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044e5b0",
      "incomplete_value": false,
      "site": "0044e5b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d89:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044e570",
      "incomplete_value": false,
      "site": "0044e578",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
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
      "0044e590",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044e598",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044e5b0",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044e590",
      "READ",
      [
        "storage",
        "002bfb46",
        null,
        "string"
      ]
    ],
    [
      "0044e598",
      "READ",
      [
        "storage",
        "002bfb54",
        null,
        "string"
      ]
    ],
    [
      "0044e5b0",
      "PARAM",
      [
        "storage",
        "002a1d89",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044e570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e528.md#insn-0044e570) · [`0044e578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e528.md#insn-0044e578) · [`0044e5a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e528.md#insn-0044e5a0)
- 新版 [`0044e5b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044e568.md#insn-0044e5b0) · [`0044e5b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044e568.md#insn-0044e5b8) · [`0044e5e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044e568.md#insn-0044e5e0)

~~~diff
- 0044e570 ["COPY", "tmp:0:8", ["const:dd6:8"]]
- 0044e570 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044e570 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044e570 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044e5b0 ["COPY", "tmp:0:8", ["const:d89:8"]]
+ 0044e5b0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044e5b0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044e5b0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044e570 bytes 21583791
+ 0044e5b0 bytes 21243691
- 0044e578 ["INT_ADD", "register:40f0:8", ["const:44e578:8", "const:4:8"]]
- 0044e578 ["CALL", null, ["callee:00c58040:8"]]
+ 0044e5b8 ["INT_ADD", "register:40f0:8", ["const:44e5b8:8", "const:4:8"]]
+ 0044e5b8 ["CALL", null, ["callee:00c58040:8"]]
- 0044e578 bytes 7e262094
+ 0044e5b8 bytes a2262094
- 0044e5a0 ["INT_ADD", "register:40f0:8", ["const:44e5a0:8", "const:4:8"]]
- 0044e5a0 ["CALL", null, ["callee:00c57f80:8"]]
+ 0044e5e0 ["INT_ADD", "register:40f0:8", ["const:44e5e0:8", "const:4:8"]]
+ 0044e5e0 ["CALL", null, ["callee:00c57f80:8"]]
- 0044e5a0 bytes 44262094
+ 0044e5e0 bytes 68262094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-abd2e76984298b7c87cdef11563adcaa"></a>

### [`0044e640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e640.md) → [`0044e680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044e680.md) FUN_0044e680

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00ac08fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac0/00ac08fc.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)
- 新版 呼出元 1件 [`00ac096c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac0/00ac096c.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044e6a8",
      "incomplete_value": true,
      "site": "0044e6b8",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044e668",
      "incomplete_value": true,
      "site": "0044e678",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044e6bc",
      "incomplete_value": true,
      "site": "0044e6bc",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044e67c",
      "incomplete_value": true,
      "site": "0044e67c",
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
                "const:e:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044e6c8",
      "incomplete_value": false,
      "site": "0044e6d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d89:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044e688",
      "incomplete_value": false,
      "site": "0044e690",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
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
      "0044e6a8",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044e6b0",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044e6c8",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044e6a8",
      "READ",
      [
        "storage",
        "002bfb46",
        null,
        "string"
      ]
    ],
    [
      "0044e6b0",
      "READ",
      [
        "storage",
        "002bfb54",
        null,
        "string"
      ]
    ],
    [
      "0044e6c8",
      "PARAM",
      [
        "storage",
        "002a1d89",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044e688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e640.md#insn-0044e688) · [`0044e690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e640.md#insn-0044e690) · [`0044e6b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e640.md#insn-0044e6b8)
- 新版 [`0044e6c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044e680.md#insn-0044e6c8) · [`0044e6d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044e680.md#insn-0044e6d0) · [`0044e6f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044e680.md#insn-0044e6f8)

~~~diff
- 0044e688 ["COPY", "tmp:0:8", ["const:dd6:8"]]
- 0044e688 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044e688 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044e688 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044e6c8 ["COPY", "tmp:0:8", ["const:d89:8"]]
+ 0044e6c8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044e6c8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044e6c8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044e688 bytes 21583791
+ 0044e6c8 bytes 21243691
- 0044e690 ["INT_ADD", "register:40f0:8", ["const:44e690:8", "const:4:8"]]
- 0044e690 ["CALL", null, ["callee:00c58040:8"]]
+ 0044e6d0 ["INT_ADD", "register:40f0:8", ["const:44e6d0:8", "const:4:8"]]
+ 0044e6d0 ["CALL", null, ["callee:00c58040:8"]]
- 0044e690 bytes 38262094
+ 0044e6d0 bytes 5c262094
- 0044e6b8 ["INT_ADD", "register:40f0:8", ["const:44e6b8:8", "const:4:8"]]
- 0044e6b8 ["CALL", null, ["callee:00c57f80:8"]]
+ 0044e6f8 ["INT_ADD", "register:40f0:8", ["const:44e6f8:8", "const:4:8"]]
+ 0044e6f8 ["CALL", null, ["callee:00c57f80:8"]]
- 0044e6b8 bytes fe252094
+ 0044e6f8 bytes 22262094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc6cb54678c7b89209aca74dafcc2c89"></a>

### [`0044e758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e758.md) → [`0044e798`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044e798.md) FUN_0044e798

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)
- 新版 呼出元 1件 [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044e7c0",
      "incomplete_value": true,
      "site": "0044e7d0",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044e780",
      "incomplete_value": true,
      "site": "0044e790",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044e7d4",
      "incomplete_value": true,
      "site": "0044e7d4",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044e794",
      "incomplete_value": true,
      "site": "0044e794",
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
                "const:e:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044e7e0",
      "incomplete_value": false,
      "site": "0044e7e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d89:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044e7a0",
      "incomplete_value": false,
      "site": "0044e7a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
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
      "0044e7c0",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044e7c8",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044e7e0",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044e7c0",
      "READ",
      [
        "storage",
        "002bfb46",
        null,
        "string"
      ]
    ],
    [
      "0044e7c8",
      "READ",
      [
        "storage",
        "002bfb54",
        null,
        "string"
      ]
    ],
    [
      "0044e7e0",
      "PARAM",
      [
        "storage",
        "002a1d89",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044e7a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e758.md#insn-0044e7a0) · [`0044e7a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e758.md#insn-0044e7a8) · [`0044e7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e758.md#insn-0044e7d0)
- 新版 [`0044e7e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044e798.md#insn-0044e7e0) · [`0044e7e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044e798.md#insn-0044e7e8) · [`0044e810`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044e798.md#insn-0044e810)

~~~diff
- 0044e7a0 ["COPY", "tmp:0:8", ["const:dd6:8"]]
- 0044e7a0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044e7a0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044e7a0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044e7e0 ["COPY", "tmp:0:8", ["const:d89:8"]]
+ 0044e7e0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044e7e0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044e7e0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044e7a0 bytes 21583791
+ 0044e7e0 bytes 21243691
- 0044e7a8 ["INT_ADD", "register:40f0:8", ["const:44e7a8:8", "const:4:8"]]
- 0044e7a8 ["CALL", null, ["callee:00c58040:8"]]
+ 0044e7e8 ["INT_ADD", "register:40f0:8", ["const:44e7e8:8", "const:4:8"]]
+ 0044e7e8 ["CALL", null, ["callee:00c58040:8"]]
- 0044e7a8 bytes f2252094
+ 0044e7e8 bytes 16262094
- 0044e7d0 ["INT_ADD", "register:40f0:8", ["const:44e7d0:8", "const:4:8"]]
- 0044e7d0 ["CALL", null, ["callee:00c57f80:8"]]
+ 0044e810 ["INT_ADD", "register:40f0:8", ["const:44e810:8", "const:4:8"]]
+ 0044e810 ["CALL", null, ["callee:00c57f80:8"]]
- 0044e7d0 bytes b8252094
+ 0044e810 bytes dc252094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a81c670b7e471813db997d53c07ef81f"></a>

### [`0044e870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e870.md) → [`0044e8b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044e8b0.md) FUN_0044e8b0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00a75dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a75/00a75dac.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)
- 新版 呼出元 1件 [`00a75e1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a75/00a75e1c.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044e8d8",
      "incomplete_value": true,
      "site": "0044e8e8",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044e898",
      "incomplete_value": true,
      "site": "0044e8a8",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044e8ec",
      "incomplete_value": true,
      "site": "0044e8ec",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044e8ac",
      "incomplete_value": true,
      "site": "0044e8ac",
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
                "const:e:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044e8f8",
      "incomplete_value": false,
      "site": "0044e900",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d89:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044e8b8",
      "incomplete_value": false,
      "site": "0044e8c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
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
      "0044e8d8",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044e8e0",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044e8f8",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044e8d8",
      "READ",
      [
        "storage",
        "002bfb46",
        null,
        "string"
      ]
    ],
    [
      "0044e8e0",
      "READ",
      [
        "storage",
        "002bfb54",
        null,
        "string"
      ]
    ],
    [
      "0044e8f8",
      "PARAM",
      [
        "storage",
        "002a1d89",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044e8b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e870.md#insn-0044e8b8) · [`0044e8c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e870.md#insn-0044e8c0) · [`0044e8e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e870.md#insn-0044e8e8)
- 新版 [`0044e8f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044e8b0.md#insn-0044e8f8) · [`0044e900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044e8b0.md#insn-0044e900) · [`0044e928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044e8b0.md#insn-0044e928)

~~~diff
- 0044e8b8 ["COPY", "tmp:0:8", ["const:dd6:8"]]
- 0044e8b8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044e8b8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044e8b8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044e8f8 ["COPY", "tmp:0:8", ["const:d89:8"]]
+ 0044e8f8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044e8f8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044e8f8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044e8b8 bytes 21583791
+ 0044e8f8 bytes 21243691
- 0044e8c0 ["INT_ADD", "register:40f0:8", ["const:44e8c0:8", "const:4:8"]]
- 0044e8c0 ["CALL", null, ["callee:00c58040:8"]]
+ 0044e900 ["INT_ADD", "register:40f0:8", ["const:44e900:8", "const:4:8"]]
+ 0044e900 ["CALL", null, ["callee:00c58040:8"]]
- 0044e8c0 bytes ac252094
+ 0044e900 bytes d0252094
- 0044e8e8 ["INT_ADD", "register:40f0:8", ["const:44e8e8:8", "const:4:8"]]
- 0044e8e8 ["CALL", null, ["callee:00c57f80:8"]]
+ 0044e928 ["INT_ADD", "register:40f0:8", ["const:44e928:8", "const:4:8"]]
+ 0044e928 ["CALL", null, ["callee:00c57f80:8"]]
- 0044e8e8 bytes 72252094
+ 0044e928 bytes 96252094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a487ed5cf69eaeb08c54a24bec449d28"></a>

### [`0044e988`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e988.md) → [`0044e9c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044e9c8.md) FUN_0044e9c8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008e66ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e6/008e66ac.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)
- 新版 呼出元 1件 [`008e6700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e6/008e6700.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044e9f0",
      "incomplete_value": true,
      "site": "0044ea00",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044e9b0",
      "incomplete_value": true,
      "site": "0044e9c0",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044ea04",
      "incomplete_value": true,
      "site": "0044ea04",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044e9c4",
      "incomplete_value": true,
      "site": "0044e9c4",
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
                "const:e:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044ea10",
      "incomplete_value": false,
      "site": "0044ea18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d89:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044e9d0",
      "incomplete_value": false,
      "site": "0044e9d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
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
      "0044e9f0",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044e9f8",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044ea10",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044e9f0",
      "READ",
      [
        "storage",
        "002bfb46",
        null,
        "string"
      ]
    ],
    [
      "0044e9f8",
      "READ",
      [
        "storage",
        "002bfb54",
        null,
        "string"
      ]
    ],
    [
      "0044ea10",
      "PARAM",
      [
        "storage",
        "002a1d89",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044e9d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e988.md#insn-0044e9d0) · [`0044e9d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e988.md#insn-0044e9d8) · [`0044ea00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e988.md#insn-0044ea00)
- 新版 [`0044ea10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044e9c8.md#insn-0044ea10) · [`0044ea18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044e9c8.md#insn-0044ea18) · [`0044ea40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044e9c8.md#insn-0044ea40)

~~~diff
- 0044e9d0 ["COPY", "tmp:0:8", ["const:dd6:8"]]
- 0044e9d0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044e9d0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044e9d0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044ea10 ["COPY", "tmp:0:8", ["const:d89:8"]]
+ 0044ea10 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044ea10 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044ea10 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044e9d0 bytes 21583791
+ 0044ea10 bytes 21243691
- 0044e9d8 ["INT_ADD", "register:40f0:8", ["const:44e9d8:8", "const:4:8"]]
- 0044e9d8 ["CALL", null, ["callee:00c58040:8"]]
+ 0044ea18 ["INT_ADD", "register:40f0:8", ["const:44ea18:8", "const:4:8"]]
+ 0044ea18 ["CALL", null, ["callee:00c58040:8"]]
- 0044e9d8 bytes 66252094
+ 0044ea18 bytes 8a252094
- 0044ea00 ["INT_ADD", "register:40f0:8", ["const:44ea00:8", "const:4:8"]]
- 0044ea00 ["CALL", null, ["callee:00c57f80:8"]]
+ 0044ea40 ["INT_ADD", "register:40f0:8", ["const:44ea40:8", "const:4:8"]]
+ 0044ea40 ["CALL", null, ["callee:00c57f80:8"]]
- 0044ea00 bytes 2c252094
+ 0044ea40 bytes 50252094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9f34fb0225282de9c0f999872d01180"></a>

### [`0044eaf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044eaf0.md) → [`0044eb30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044eb30.md) FUN_0044eb30

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)
- 新版 呼出元 1件 [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044eb58",
      "incomplete_value": true,
      "site": "0044eb68",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044eb18",
      "incomplete_value": true,
      "site": "0044eb28",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044eb6c",
      "incomplete_value": true,
      "site": "0044eb6c",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044eb2c",
      "incomplete_value": true,
      "site": "0044eb2c",
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
                "const:e:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044eb78",
      "incomplete_value": false,
      "site": "0044eb80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d89:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044eb38",
      "incomplete_value": false,
      "site": "0044eb40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
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
      "0044eb58",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044eb60",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044eb78",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044eb58",
      "READ",
      [
        "storage",
        "002bfb46",
        null,
        "string"
      ]
    ],
    [
      "0044eb60",
      "READ",
      [
        "storage",
        "002bfb54",
        null,
        "string"
      ]
    ],
    [
      "0044eb78",
      "PARAM",
      [
        "storage",
        "002a1d89",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044eb38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044eaf0.md#insn-0044eb38) · [`0044eb40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044eaf0.md#insn-0044eb40) · [`0044eb68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044eaf0.md#insn-0044eb68)
- 新版 [`0044eb78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044eb30.md#insn-0044eb78) · [`0044eb80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044eb30.md#insn-0044eb80) · [`0044eba8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044eb30.md#insn-0044eba8)

~~~diff
- 0044eb38 ["COPY", "tmp:0:8", ["const:dd6:8"]]
- 0044eb38 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044eb38 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044eb38 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044eb78 ["COPY", "tmp:0:8", ["const:d89:8"]]
+ 0044eb78 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044eb78 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044eb78 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044eb38 bytes 21583791
+ 0044eb78 bytes 21243691
- 0044eb40 ["INT_ADD", "register:40f0:8", ["const:44eb40:8", "const:4:8"]]
- 0044eb40 ["CALL", null, ["callee:00c58040:8"]]
+ 0044eb80 ["INT_ADD", "register:40f0:8", ["const:44eb80:8", "const:4:8"]]
+ 0044eb80 ["CALL", null, ["callee:00c58040:8"]]
- 0044eb40 bytes 0c252094
+ 0044eb80 bytes 30252094
- 0044eb68 ["INT_ADD", "register:40f0:8", ["const:44eb68:8", "const:4:8"]]
- 0044eb68 ["CALL", null, ["callee:00c57f80:8"]]
+ 0044eba8 ["INT_ADD", "register:40f0:8", ["const:44eba8:8", "const:4:8"]]
+ 0044eba8 ["CALL", null, ["callee:00c57f80:8"]]
- 0044eb68 bytes d2242094
+ 0044eba8 bytes f6242094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d92723be72ed3ea30a39386968c7d49e"></a>

### [`0044ec08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044ec08.md) → [`0044ec48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044ec48.md) FUN_0044ec48

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)
- 新版 呼出元 1件 [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044ec70",
      "incomplete_value": true,
      "site": "0044ec80",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044ec30",
      "incomplete_value": true,
      "site": "0044ec40",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044ec84",
      "incomplete_value": true,
      "site": "0044ec84",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044ec44",
      "incomplete_value": true,
      "site": "0044ec44",
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
                "const:e:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044ec90",
      "incomplete_value": false,
      "site": "0044ec98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d89:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044ec50",
      "incomplete_value": false,
      "site": "0044ec58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
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
      "0044ec70",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044ec78",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044ec90",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044ec70",
      "READ",
      [
        "storage",
        "002bfb46",
        null,
        "string"
      ]
    ],
    [
      "0044ec78",
      "READ",
      [
        "storage",
        "002bfb54",
        null,
        "string"
      ]
    ],
    [
      "0044ec90",
      "PARAM",
      [
        "storage",
        "002a1d89",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044ec50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044ec08.md#insn-0044ec50) · [`0044ec58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044ec08.md#insn-0044ec58) · [`0044ec80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044ec08.md#insn-0044ec80)
- 新版 [`0044ec90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044ec48.md#insn-0044ec90) · [`0044ec98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044ec48.md#insn-0044ec98) · [`0044ecc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044ec48.md#insn-0044ecc0)

~~~diff
- 0044ec50 ["COPY", "tmp:0:8", ["const:dd6:8"]]
- 0044ec50 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044ec50 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044ec50 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044ec90 ["COPY", "tmp:0:8", ["const:d89:8"]]
+ 0044ec90 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044ec90 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044ec90 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044ec50 bytes 21583791
+ 0044ec90 bytes 21243691
- 0044ec58 ["INT_ADD", "register:40f0:8", ["const:44ec58:8", "const:4:8"]]
- 0044ec58 ["CALL", null, ["callee:00c58040:8"]]
+ 0044ec98 ["INT_ADD", "register:40f0:8", ["const:44ec98:8", "const:4:8"]]
+ 0044ec98 ["CALL", null, ["callee:00c58040:8"]]
- 0044ec58 bytes c6242094
+ 0044ec98 bytes ea242094
- 0044ec80 ["INT_ADD", "register:40f0:8", ["const:44ec80:8", "const:4:8"]]
- 0044ec80 ["CALL", null, ["callee:00c57f80:8"]]
+ 0044ecc0 ["INT_ADD", "register:40f0:8", ["const:44ecc0:8", "const:4:8"]]
+ 0044ecc0 ["CALL", null, ["callee:00c57f80:8"]]
- 0044ec80 bytes 8c242094
+ 0044ecc0 bytes b0242094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-667e3dc037b81e697e3eecdeb78c6252"></a>

### [`0044ed20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044ed20.md) → [`0044ed60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044ed60.md) FUN_0044ed60

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008a4c50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a4/008a4c50.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)
- 新版 呼出元 1件 [`008a4ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008a4/008a4ca8.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044ed88",
      "incomplete_value": true,
      "site": "0044ed98",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044ed48",
      "incomplete_value": true,
      "site": "0044ed58",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044ed9c",
      "incomplete_value": true,
      "site": "0044ed9c",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044ed5c",
      "incomplete_value": true,
      "site": "0044ed5c",
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
                "const:e:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044eda8",
      "incomplete_value": false,
      "site": "0044edb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d89:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044ed68",
      "incomplete_value": false,
      "site": "0044ed70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
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
      "0044ed88",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044ed90",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044eda8",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044ed88",
      "READ",
      [
        "storage",
        "002bfb46",
        null,
        "string"
      ]
    ],
    [
      "0044ed90",
      "READ",
      [
        "storage",
        "002bfb54",
        null,
        "string"
      ]
    ],
    [
      "0044eda8",
      "PARAM",
      [
        "storage",
        "002a1d89",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044ed68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044ed20.md#insn-0044ed68) · [`0044ed70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044ed20.md#insn-0044ed70) · [`0044ed98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044ed20.md#insn-0044ed98)
- 新版 [`0044eda8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044ed60.md#insn-0044eda8) · [`0044edb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044ed60.md#insn-0044edb0) · [`0044edd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044ed60.md#insn-0044edd8)

~~~diff
- 0044ed68 ["COPY", "tmp:0:8", ["const:dd6:8"]]
- 0044ed68 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044ed68 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044ed68 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044eda8 ["COPY", "tmp:0:8", ["const:d89:8"]]
+ 0044eda8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044eda8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044eda8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044ed68 bytes 21583791
+ 0044eda8 bytes 21243691
- 0044ed70 ["INT_ADD", "register:40f0:8", ["const:44ed70:8", "const:4:8"]]
- 0044ed70 ["CALL", null, ["callee:00c58040:8"]]
+ 0044edb0 ["INT_ADD", "register:40f0:8", ["const:44edb0:8", "const:4:8"]]
+ 0044edb0 ["CALL", null, ["callee:00c58040:8"]]
- 0044ed70 bytes 80242094
+ 0044edb0 bytes a4242094
- 0044ed98 ["INT_ADD", "register:40f0:8", ["const:44ed98:8", "const:4:8"]]
- 0044ed98 ["CALL", null, ["callee:00c57f80:8"]]
+ 0044edd8 ["INT_ADD", "register:40f0:8", ["const:44edd8:8", "const:4:8"]]
+ 0044edd8 ["CALL", null, ["callee:00c57f80:8"]]
- 0044ed98 bytes 46242094
+ 0044edd8 bytes 6a242094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2d1453c353714acc643e3b745acb056"></a>

### [`0044ee3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044ee3c.md) → [`0044ee7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044ee7c.md) FUN_0044ee7c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007834b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00783/007834b0.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)
- 新版 呼出元 1件 [`00783508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00783/00783508.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044eea4",
      "incomplete_value": true,
      "site": "0044eeb4",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044ee64",
      "incomplete_value": true,
      "site": "0044ee74",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044eeb8",
      "incomplete_value": true,
      "site": "0044eeb8",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044ee78",
      "incomplete_value": true,
      "site": "0044ee78",
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
                "const:e:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044eec4",
      "incomplete_value": false,
      "site": "0044eecc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d89:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044ee84",
      "incomplete_value": false,
      "site": "0044ee8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
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
      "0044eea4",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044eeac",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044eec4",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044eea4",
      "READ",
      [
        "storage",
        "002bfb46",
        null,
        "string"
      ]
    ],
    [
      "0044eeac",
      "READ",
      [
        "storage",
        "002bfb54",
        null,
        "string"
      ]
    ],
    [
      "0044eec4",
      "PARAM",
      [
        "storage",
        "002a1d89",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044ee84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044ee3c.md#insn-0044ee84) · [`0044ee8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044ee3c.md#insn-0044ee8c) · [`0044eeb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044ee3c.md#insn-0044eeb4)
- 新版 [`0044eec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044ee7c.md#insn-0044eec4) · [`0044eecc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044ee7c.md#insn-0044eecc) · [`0044eef4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044ee7c.md#insn-0044eef4)

~~~diff
- 0044ee84 ["COPY", "tmp:0:8", ["const:dd6:8"]]
- 0044ee84 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044ee84 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044ee84 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044eec4 ["COPY", "tmp:0:8", ["const:d89:8"]]
+ 0044eec4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044eec4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044eec4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044ee84 bytes 21583791
+ 0044eec4 bytes 21243691
- 0044ee8c ["INT_ADD", "register:40f0:8", ["const:44ee8c:8", "const:4:8"]]
- 0044ee8c ["CALL", null, ["callee:00c58040:8"]]
+ 0044eecc ["INT_ADD", "register:40f0:8", ["const:44eecc:8", "const:4:8"]]
+ 0044eecc ["CALL", null, ["callee:00c58040:8"]]
- 0044ee8c bytes 39242094
+ 0044eecc bytes 5d242094
- 0044eeb4 ["INT_ADD", "register:40f0:8", ["const:44eeb4:8", "const:4:8"]]
- 0044eeb4 ["CALL", null, ["callee:00c57f80:8"]]
+ 0044eef4 ["INT_ADD", "register:40f0:8", ["const:44eef4:8", "const:4:8"]]
+ 0044eef4 ["CALL", null, ["callee:00c57f80:8"]]
- 0044eeb4 bytes ff232094
+ 0044eef4 bytes 23242094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ed51da03ceeb28326a3025b86f6ec1e"></a>

### [`0044ef54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044ef54.md) → [`0044ef94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044ef94.md) FUN_0044ef94

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) [`008a78a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a7/008a78a4.md) [`008a7b3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a7/008a7b3c.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md)
- 新版 呼出元 3件 [`00856e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856e84.md) [`008a78fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008a7/008a78fc.md) [`008a7b94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008a7/008a7b94.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.49% / 新版 91.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044efc0",
      "incomplete_value": true,
      "site": "0044efd4",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044ef80",
      "incomplete_value": true,
      "site": "0044ef94",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b9a:8"
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
      "definition_site": "0044efd8",
      "incomplete_value": true,
      "site": "0044efd8",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044ef98",
      "incomplete_value": true,
      "site": "0044ef98",
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
                "const:e:8"
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
      "definition_site": "0044efe4",
      "incomplete_value": false,
      "site": "0044efec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d89:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044efa4",
      "incomplete_value": false,
      "site": "0044efac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
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
      "0044efc0",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044efcc",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044efe4",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044efc0",
      "READ",
      [
        "storage",
        "002bfb46",
        null,
        "string"
      ]
    ],
    [
      "0044efcc",
      "READ",
      [
        "storage",
        "002bfb54",
        null,
        "string"
      ]
    ],
    [
      "0044efe4",
      "PARAM",
      [
        "storage",
        "002a1d89",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044efa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044ef54.md#insn-0044efa4) · [`0044efac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044ef54.md#insn-0044efac) · [`0044efd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044ef54.md#insn-0044efd4)
- 新版 [`0044efe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044ef94.md#insn-0044efe4) · [`0044efec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044ef94.md#insn-0044efec) · [`0044f014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044ef94.md#insn-0044f014)

~~~diff
- 0044efa4 ["COPY", "tmp:0:8", ["const:dd6:8"]]
- 0044efa4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044efa4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044efa4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044efe4 ["COPY", "tmp:0:8", ["const:d89:8"]]
+ 0044efe4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044efe4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044efe4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044efa4 bytes 21583791
+ 0044efe4 bytes 21243691
- 0044efac ["INT_ADD", "register:40f0:8", ["const:44efac:8", "const:4:8"]]
- 0044efac ["CALL", null, ["callee:00c58040:8"]]
+ 0044efec ["INT_ADD", "register:40f0:8", ["const:44efec:8", "const:4:8"]]
+ 0044efec ["CALL", null, ["callee:00c58040:8"]]
- 0044efac bytes f1232094
+ 0044efec bytes 15242094
- 0044efd4 ["INT_ADD", "register:40f0:8", ["const:44efd4:8", "const:4:8"]]
- 0044efd4 ["CALL", null, ["callee:00c57f80:8"]]
+ 0044f014 ["INT_ADD", "register:40f0:8", ["const:44f014:8", "const:4:8"]]
+ 0044f014 ["CALL", null, ["callee:00c57f80:8"]]
- 0044efd4 bytes b7232094
+ 0044f014 bytes db232094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5459a47d4d12029c83b353b65633db1d"></a>

### [`0044f160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f160.md) → [`0044f1a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f1a0.md) FUN_0044f1a0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)
- 新版 呼出元 1件 [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044f1c8",
      "incomplete_value": true,
      "site": "0044f1d8",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044f188",
      "incomplete_value": true,
      "site": "0044f198",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044f1dc",
      "incomplete_value": true,
      "site": "0044f1dc",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044f19c",
      "incomplete_value": true,
      "site": "0044f19c",
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
                "const:e:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044f1e8",
      "incomplete_value": false,
      "site": "0044f1f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d89:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044f1a8",
      "incomplete_value": false,
      "site": "0044f1b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
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
      "0044f1c8",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044f1d0",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044f1e8",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044f1c8",
      "READ",
      [
        "storage",
        "002bfb46",
        null,
        "string"
      ]
    ],
    [
      "0044f1d0",
      "READ",
      [
        "storage",
        "002bfb54",
        null,
        "string"
      ]
    ],
    [
      "0044f1e8",
      "PARAM",
      [
        "storage",
        "002a1d89",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044f1a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f160.md#insn-0044f1a8) · [`0044f1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f160.md#insn-0044f1b0) · [`0044f1d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f160.md#insn-0044f1d8)
- 新版 [`0044f1e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f1a0.md#insn-0044f1e8) · [`0044f1f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f1a0.md#insn-0044f1f0) · [`0044f218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f1a0.md#insn-0044f218)

~~~diff
- 0044f1a8 ["COPY", "tmp:0:8", ["const:dd6:8"]]
- 0044f1a8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044f1a8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044f1a8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044f1e8 ["COPY", "tmp:0:8", ["const:d89:8"]]
+ 0044f1e8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044f1e8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044f1e8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044f1a8 bytes 21583791
+ 0044f1e8 bytes 21243691
- 0044f1b0 ["INT_ADD", "register:40f0:8", ["const:44f1b0:8", "const:4:8"]]
- 0044f1b0 ["CALL", null, ["callee:00c58040:8"]]
+ 0044f1f0 ["INT_ADD", "register:40f0:8", ["const:44f1f0:8", "const:4:8"]]
+ 0044f1f0 ["CALL", null, ["callee:00c58040:8"]]
- 0044f1b0 bytes 70232094
+ 0044f1f0 bytes 94232094
- 0044f1d8 ["INT_ADD", "register:40f0:8", ["const:44f1d8:8", "const:4:8"]]
- 0044f1d8 ["CALL", null, ["callee:00c57f80:8"]]
+ 0044f218 ["INT_ADD", "register:40f0:8", ["const:44f218:8", "const:4:8"]]
+ 0044f218 ["CALL", null, ["callee:00c57f80:8"]]
- 0044f1d8 bytes 36232094
+ 0044f218 bytes 5a232094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ffc542e6794fe71e4ef37057ebe4707b"></a>

### [`0044f278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f278.md) → [`0044f2b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f2b8.md) FUN_0044f2b8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)
- 新版 呼出元 1件 [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044f2e0",
      "incomplete_value": true,
      "site": "0044f2f0",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044f2a0",
      "incomplete_value": true,
      "site": "0044f2b0",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b9a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044f2f4",
      "incomplete_value": true,
      "site": "0044f2f4",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044f2b4",
      "incomplete_value": true,
      "site": "0044f2b4",
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
                "const:e:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044f300",
      "incomplete_value": false,
      "site": "0044f308",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:d89:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044f2c0",
      "incomplete_value": false,
      "site": "0044f2c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a1000:8"
          ],
          [
            "leaf",
            "const:dd6:8"
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
      "0044f2e0",
      "READ",
      [
        "storage",
        "002bfb9a",
        null,
        "string"
      ]
    ],
    [
      "0044f2e8",
      "READ",
      [
        "storage",
        "002bfba8",
        null,
        "string"
      ]
    ],
    [
      "0044f300",
      "PARAM",
      [
        "storage",
        "002a1dd6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044f2e0",
      "READ",
      [
        "storage",
        "002bfb46",
        null,
        "string"
      ]
    ],
    [
      "0044f2e8",
      "READ",
      [
        "storage",
        "002bfb54",
        null,
        "string"
      ]
    ],
    [
      "0044f300",
      "PARAM",
      [
        "storage",
        "002a1d89",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044f2c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f278.md#insn-0044f2c0) · [`0044f2c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f278.md#insn-0044f2c8) · [`0044f2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f278.md#insn-0044f2f0)
- 新版 [`0044f300`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f2b8.md#insn-0044f300) · [`0044f308`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f2b8.md#insn-0044f308) · [`0044f330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f2b8.md#insn-0044f330)

~~~diff
- 0044f2c0 ["COPY", "tmp:0:8", ["const:dd6:8"]]
- 0044f2c0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044f2c0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044f2c0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044f300 ["COPY", "tmp:0:8", ["const:d89:8"]]
+ 0044f300 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044f300 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044f300 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044f2c0 bytes 21583791
+ 0044f300 bytes 21243691
- 0044f2c8 ["INT_ADD", "register:40f0:8", ["const:44f2c8:8", "const:4:8"]]
- 0044f2c8 ["CALL", null, ["callee:00c58040:8"]]
+ 0044f308 ["INT_ADD", "register:40f0:8", ["const:44f308:8", "const:4:8"]]
+ 0044f308 ["CALL", null, ["callee:00c58040:8"]]
- 0044f2c8 bytes 2a232094
+ 0044f308 bytes 4e232094
- 0044f2f0 ["INT_ADD", "register:40f0:8", ["const:44f2f0:8", "const:4:8"]]
- 0044f2f0 ["CALL", null, ["callee:00c57f80:8"]]
+ 0044f330 ["INT_ADD", "register:40f0:8", ["const:44f330:8", "const:4:8"]]
+ 0044f330 ["CALL", null, ["callee:00c57f80:8"]]
- 0044f2f0 bytes f0222094
+ 0044f330 bytes 14232094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e084323d59e747c5810a0cca6f80dc0c"></a>

### [`0044f390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f390.md) → [`0044f3d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f3d0.md) FUN_0044f3d0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00876a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876a10.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) [`00c58190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58190.md)
- 新版 呼出元 1件 [`00876a68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876a68.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md) [`00c58260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58260.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044f3fc",
      "incomplete_value": false,
      "site": "0044f404",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ab000:8"
          ],
          [
            "leaf",
            "const:279:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044f3bc",
      "incomplete_value": false,
      "site": "0044f3c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ab000:8"
          ],
          [
            "leaf",
            "const:2d5:8"
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
      "definition_site": "0044f40c",
      "incomplete_value": false,
      "site": "0044f418",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bf000:8"
          ],
          [
            "leaf",
            "const:b71:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044f3cc",
      "incomplete_value": false,
      "site": "0044f3d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bf000:8"
          ],
          [
            "leaf",
            "const:bc5:8"
          ]
        ]
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
      "0044f3fc",
      "PARAM",
      [
        "storage",
        "002ab2d5",
        null,
        "string"
      ]
    ],
    [
      "0044f40c",
      "PARAM",
      [
        "storage",
        "002bfbc5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044f3fc",
      "PARAM",
      [
        "storage",
        "002ab279",
        null,
        "string"
      ]
    ],
    [
      "0044f40c",
      "PARAM",
      [
        "storage",
        "002bfb71",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044f3c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f390.md#insn-0044f3c4) · [`0044f3d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f390.md#insn-0044f3d8) · [`0044f3bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f390.md#insn-0044f3bc)
- 新版 [`0044f404`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f3d0.md#insn-0044f404) · [`0044f418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f3d0.md#insn-0044f418) · [`0044f3fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f3d0.md#insn-0044f3fc)

~~~diff
- 0044f3c4 ["INT_ADD", "register:40f0:8", ["const:44f3c4:8", "const:4:8"]]
- 0044f3c4 ["CALL", null, ["callee:00c58260:8"]]
+ 0044f404 ["INT_ADD", "register:40f0:8", ["const:44f404:8", "const:4:8"]]
+ 0044f404 ["CALL", null, ["callee:00c58260:8"]]
- 0044f3c4 bytes 73232094
+ 0044f404 bytes 97232094
- 0044f3d8 ["INT_ADD", "register:40f0:8", ["const:44f3d8:8", "const:4:8"]]
- 0044f3d8 ["CALL", null, ["callee:00c58180:8"]]
+ 0044f418 ["INT_ADD", "register:40f0:8", ["const:44f418:8", "const:4:8"]]
+ 0044f418 ["CALL", null, ["callee:00c58180:8"]]
- 0044f3d8 bytes 36232094
+ 0044f418 bytes 5a232094
- 0044f3bc ["COPY", "tmp:0:8", ["const:2d5:8"]]
- 0044f3bc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044f3bc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044f3bc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044f3fc ["COPY", "tmp:0:8", ["const:279:8"]]
+ 0044f3fc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044f3fc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044f3fc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044f3bc bytes 21540b91
+ 0044f3fc bytes 21e40991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56a7160165e5c42e1d87352f3ad683d7"></a>

### [`0044f43c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f43c.md) → [`0044f47c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f47c.md) FUN_0044f47c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00876a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876a10.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) [`00c58190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58190.md)
- 新版 呼出元 1件 [`00876a68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876a68.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md) [`00c58260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58260.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044f4a8",
      "incomplete_value": false,
      "site": "0044f4b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ab000:8"
          ],
          [
            "leaf",
            "const:279:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044f468",
      "incomplete_value": false,
      "site": "0044f470",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ab000:8"
          ],
          [
            "leaf",
            "const:2d5:8"
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
      "definition_site": "0044f4b8",
      "incomplete_value": false,
      "site": "0044f4c4",
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
            "const:f7e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044f478",
      "incomplete_value": false,
      "site": "0044f484",
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
            "const:f3e:8"
          ]
        ]
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
      "0044f4a8",
      "PARAM",
      [
        "storage",
        "002ab2d5",
        null,
        "string"
      ]
    ],
    [
      "0044f4b8",
      "PARAM",
      [
        "storage",
        "002c0f3e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044f4a8",
      "PARAM",
      [
        "storage",
        "002ab279",
        null,
        "string"
      ]
    ],
    [
      "0044f4b8",
      "PARAM",
      [
        "storage",
        "002c0f7e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044f470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f43c.md#insn-0044f470) · [`0044f484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f43c.md#insn-0044f484) · [`0044f468`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f43c.md#insn-0044f468)
- 新版 [`0044f4b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f47c.md#insn-0044f4b0) · [`0044f4c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f47c.md#insn-0044f4c4) · [`0044f4a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f47c.md#insn-0044f4a8)

~~~diff
- 0044f470 ["INT_ADD", "register:40f0:8", ["const:44f470:8", "const:4:8"]]
- 0044f470 ["CALL", null, ["callee:00c58260:8"]]
+ 0044f4b0 ["INT_ADD", "register:40f0:8", ["const:44f4b0:8", "const:4:8"]]
+ 0044f4b0 ["CALL", null, ["callee:00c58260:8"]]
- 0044f470 bytes 48232094
+ 0044f4b0 bytes 6c232094
- 0044f484 ["INT_ADD", "register:40f0:8", ["const:44f484:8", "const:4:8"]]
- 0044f484 ["CALL", null, ["callee:00c58180:8"]]
+ 0044f4c4 ["INT_ADD", "register:40f0:8", ["const:44f4c4:8", "const:4:8"]]
+ 0044f4c4 ["CALL", null, ["callee:00c58180:8"]]
- 0044f484 bytes 0b232094
+ 0044f4c4 bytes 2f232094
- 0044f468 ["COPY", "tmp:0:8", ["const:2d5:8"]]
- 0044f468 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0044f468 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0044f468 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0044f4a8 ["COPY", "tmp:0:8", ["const:279:8"]]
+ 0044f4a8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0044f4a8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0044f4a8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0044f468 bytes 21540b91
+ 0044f4a8 bytes 21e40991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-515ddd87e36a4e4ae6f917c1c574fc6d"></a>

### [`0044f4e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f4e8.md) → [`0044f528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f528.md) _INIT_10

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00bc47f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc47f0.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00bc488c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc4/00bc488c.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 call, call_argument_candidate, call_count, constant, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_call_alignment

命令の説明率　旧版 80.54% / 新版 80.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 4件, `store_value` 8件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0044f564",
      "incomplete_value": true,
      "site": "0044f580",
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
    "old": {
      "definition_site": "0044f524",
      "incomplete_value": true,
      "site": "0044f540",
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
                "const:f26:8"
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
      "definition_site": "0044f588",
      "incomplete_value": true,
      "site": "0044f5a4",
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
    "old": {
      "definition_site": "0044f548",
      "incomplete_value": true,
      "site": "0044f564",
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
                "const:f39:8"
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
      "definition_site": "0044f5a8",
      "incomplete_value": true,
      "site": "0044f5c4",
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
                "const:d6e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044f568",
      "incomplete_value": true,
      "site": "0044f584",
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
                "const:dc2:8"
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
      "0044f564",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "0044f588",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "0044f5a8",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0044f564",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "0044f588",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "0044f5a8",
      "READ",
      [
        "storage",
        "002b8d6e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044f560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f4e8.md#insn-0044f560) · [`0044f580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f4e8.md#insn-0044f580) · [`0044f648`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f4e8.md#insn-0044f648)
- 新版 [`0044f5a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f528.md#insn-0044f5a0) · [`0044f5c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f528.md#insn-0044f5c0) · [`0044f688`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f528.md#insn-0044f688)

~~~diff
- 0044f560 ["COPY", "tmp:0:8", ["const:dc2:8"]]
- 0044f560 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0044f560 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0044f560 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0044f5a0 ["COPY", "tmp:0:8", ["const:d6e:8"]]
+ 0044f5a0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0044f5a0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0044f5a0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0044f560 bytes 4a093791
+ 0044f5a0 bytes 4ab93591
- 0044f580 ["COPY", "tmp:0:8", ["const:f62:8"]]
- 0044f580 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0044f580 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0044f580 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0044f5c0 ["COPY", "tmp:0:8", ["const:f15:8"]]
+ 0044f5c0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0044f5c0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0044f5c0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0044f580 bytes 4a893d91
+ 0044f5c0 bytes 4a553c91
- 0044f648 ["INT_ADD", "register:40f0:8", ["const:44f648:8", "const:4:8"]]
- 0044f648 ["CALL", null, ["callee:0043b838:8"]]
+ 0044f688 ["INT_ADD", "register:40f0:8", ["const:44f688:8", "const:4:8"]]
+ 0044f688 ["CALL", null, ["callee:0043b838:8"]]
- 0044f648 bytes 6cb0ff97
+ 0044f688 bytes 6cb0ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-693cb334355b6488cd8cc1e2cf620106"></a>

### [`0044f898`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f898.md) → [`0044f8d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f8d8.md) FUN_0044f8d8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 6件 [`0086d71c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086d71c.md) [`0086de04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086de04.md) [`008a6e4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a6/008a6e4c.md) [`008a72a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a7/008a72a8.md) [`008a74a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a7/008a74a8.md) · 呼出先 2件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)
- 新版 呼出元 6件 [`0086d774`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086d/0086d774.md) [`0086de5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086d/0086de5c.md) [`008a6ea4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008a6/008a6ea4.md) [`008a7300`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008a7/008a7300.md) [`008a7500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008a7/008a7500.md) · 呼出先 2件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044f904",
      "incomplete_value": false,
      "site": "0044f908",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca4000:8"
          ],
          [
            "leaf",
            "const:ba0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044f8c4",
      "incomplete_value": false,
      "site": "0044f8c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca4000:8"
          ],
          [
            "leaf",
            "const:aa0:8"
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
      "definition_site": "0044f914",
      "incomplete_value": false,
      "site": "0044f918",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca4000:8"
          ],
          [
            "leaf",
            "const:ba0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044f8d4",
      "incomplete_value": false,
      "site": "0044f8d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca4000:8"
          ],
          [
            "leaf",
            "const:aa0:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "0044f8f4",
      "incomplete_value": true,
      "site": "0044f8fc",
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
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:b98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044f8b4",
      "incomplete_value": true,
      "site": "0044f8bc",
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
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:a98:8"
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
      "0044f8e8",
      "READ",
      [
        "storage",
        "00ca4aa0",
        null,
        "undefined1"
      ]
    ],
    [
      "0044f8f4",
      "READ",
      [
        "storage",
        "00ca4a98",
        null,
        "undefined8"
      ]
    ],
    [
      "0044f904",
      "PARAM",
      [
        "storage",
        "00ca4aa0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0044f8e8",
      "READ",
      [
        "storage",
        "00ca4ba0",
        null,
        "undefined1"
      ]
    ],
    [
      "0044f8f4",
      "READ",
      [
        "storage",
        "00ca4b98",
        null,
        "undefined8"
      ]
    ],
    [
      "0044f904",
      "PARAM",
      [
        "storage",
        "00ca4ba0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044f8c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f898.md#insn-0044f8c8) · [`0044f8d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f898.md#insn-0044f8d8) · [`0044f8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f898.md#insn-0044f8a4)
- 新版 [`0044f908`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f8d8.md#insn-0044f908) · [`0044f918`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f8d8.md#insn-0044f918) · [`0044f8e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f8d8.md#insn-0044f8e4)

~~~diff
- 0044f8c8 ["INT_ADD", "register:40f0:8", ["const:44f8c8:8", "const:4:8"]]
- 0044f8c8 ["CALL", null, ["callee:00c57f20:8"]]
+ 0044f908 ["INT_ADD", "register:40f0:8", ["const:44f908:8", "const:4:8"]]
+ 0044f908 ["CALL", null, ["callee:00c57f20:8"]]
- 0044f8c8 bytes 62212094
+ 0044f908 bytes 86212094
- 0044f8d8 ["INT_ADD", "register:40f0:8", ["const:44f8d8:8", "const:4:8"]]
- 0044f8d8 ["CALL", null, ["callee:00c57f40:8"]]
+ 0044f918 ["INT_ADD", "register:40f0:8", ["const:44f918:8", "const:4:8"]]
+ 0044f918 ["CALL", null, ["callee:00c57f40:8"]]
- 0044f8d8 bytes 66212094
+ 0044f918 bytes 8a212094
- 0044f8a4 ["COPY", "tmp:0:8", ["const:aa0:8"]]
- 0044f8a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0044f8a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0044f8a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0044f8e4 ["COPY", "tmp:0:8", ["const:ba0:8"]]
+ 0044f8e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0044f8e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0044f8e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0044f8a4 bytes 08812a91
+ 0044f8e4 bytes 08812e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7519d84be4ea6ee0d0169e67d7bbcfde"></a>

### [`0044f8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f8e0.md) → [`0044f920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f920.md) FUN_0044f920

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 23件 [`004766c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/004766c8.md) [`004779cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00477/004779cc.md) [`00599804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599804.md) [`0075eb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075eb80.md) [`0079b110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079b/0079b110.md) · 呼出先 2件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)
- 新版 呼出元 23件 [`00476708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00476/00476708.md) [`00477a0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00477/00477a0c.md) [`00599844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599844.md) [`0075ebd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075e/0075ebd8.md) [`0079b168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079b/0079b168.md) · 呼出先 2件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 72.22% / 新版 72.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044f94c",
      "incomplete_value": false,
      "site": "0044f950",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca4000:8"
          ],
          [
            "leaf",
            "const:ba0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044f90c",
      "incomplete_value": false,
      "site": "0044f910",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca4000:8"
          ],
          [
            "leaf",
            "const:aa0:8"
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
      "definition_site": "0044f95c",
      "incomplete_value": false,
      "site": "0044f960",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca4000:8"
          ],
          [
            "leaf",
            "const:ba0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044f91c",
      "incomplete_value": false,
      "site": "0044f920",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca4000:8"
          ],
          [
            "leaf",
            "const:aa0:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "0044f93c",
      "incomplete_value": false,
      "site": "0044f944",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca4000:8"
          ],
          [
            "leaf",
            "const:b98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044f8fc",
      "incomplete_value": false,
      "site": "0044f904",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca4000:8"
          ],
          [
            "leaf",
            "const:a98:8"
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
      "0044f930",
      "READ",
      [
        "storage",
        "00ca4aa0",
        null,
        "undefined1"
      ]
    ],
    [
      "0044f93c",
      "DATA",
      [
        "storage",
        "00ca4a98",
        null,
        "undefined8"
      ]
    ],
    [
      "0044f94c",
      "PARAM",
      [
        "storage",
        "00ca4aa0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0044f930",
      "READ",
      [
        "storage",
        "00ca4ba0",
        null,
        "undefined1"
      ]
    ],
    [
      "0044f93c",
      "DATA",
      [
        "storage",
        "00ca4b98",
        null,
        "undefined8"
      ]
    ],
    [
      "0044f94c",
      "PARAM",
      [
        "storage",
        "00ca4ba0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044f910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f8e0.md#insn-0044f910) · [`0044f920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f8e0.md#insn-0044f920) · [`0044f8ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f8e0.md#insn-0044f8ec)
- 新版 [`0044f950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f920.md#insn-0044f950) · [`0044f960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f920.md#insn-0044f960) · [`0044f92c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f920.md#insn-0044f92c)

~~~diff
- 0044f910 ["INT_ADD", "register:40f0:8", ["const:44f910:8", "const:4:8"]]
- 0044f910 ["CALL", null, ["callee:00c57f20:8"]]
+ 0044f950 ["INT_ADD", "register:40f0:8", ["const:44f950:8", "const:4:8"]]
+ 0044f950 ["CALL", null, ["callee:00c57f20:8"]]
- 0044f910 bytes 50212094
+ 0044f950 bytes 74212094
- 0044f920 ["INT_ADD", "register:40f0:8", ["const:44f920:8", "const:4:8"]]
- 0044f920 ["CALL", null, ["callee:00c57f40:8"]]
+ 0044f960 ["INT_ADD", "register:40f0:8", ["const:44f960:8", "const:4:8"]]
+ 0044f960 ["CALL", null, ["callee:00c57f40:8"]]
- 0044f920 bytes 54212094
+ 0044f960 bytes 78212094
- 0044f8ec ["COPY", "tmp:0:8", ["const:aa0:8"]]
- 0044f8ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0044f8ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0044f8ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0044f92c ["COPY", "tmp:0:8", ["const:ba0:8"]]
+ 0044f92c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0044f92c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0044f92c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0044f8ec bytes 08812a91
+ 0044f92c bytes 08812e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb1100dd17e44c14f78d9826b440ad8d"></a>

### [`0044f948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f948.md) → [`0044f988`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f988.md) FUN_0044f988

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00873aa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873aa8.md) · 呼出先 10件 [`0044b534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b534.md) [`00459fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459fa0.md) [`00561d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561d34.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`00873b00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873b00.md) · 呼出先 10件 [`0044b574`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b574.md) [`00459fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459fe0.md) [`00561d74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/00561d74.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.37% / 新版 97.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0044fadc",
      "incomplete_value": false,
      "site": "0044fadc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:8f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044fa9c",
      "incomplete_value": false,
      "site": "0044fa9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:820:8"
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044f9bc",
      "incomplete_value": false,
      "site": "0044f9c4",
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
            "const:eaa:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044f97c",
      "incomplete_value": false,
      "site": "0044f984",
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
            "const:e6a:8"
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
      "definition_site": "0044fa28",
      "incomplete_value": true,
      "site": "0044fa30",
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
                "const:c98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044f9e8",
      "incomplete_value": true,
      "site": "0044f9f0",
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
                "const:bc8:8"
              ]
            ]
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
      "0044f9bc",
      "PARAM",
      [
        "storage",
        "002b5e6a",
        null,
        "string"
      ]
    ],
    [
      "0044fa28",
      "READ",
      [
        "storage",
        "00c9abc8",
        null,
        "pointer"
      ]
    ],
    [
      "0044fa28",
      "PARAM",
      [
        "storage",
        "00ca5cd0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0044f9bc",
      "PARAM",
      [
        "storage",
        "002b5eaa",
        null,
        "string"
      ]
    ],
    [
      "0044fa28",
      "READ",
      [
        "storage",
        "00c9ac98",
        null,
        "pointer"
      ]
    ],
    [
      "0044fa28",
      "PARAM",
      [
        "storage",
        "00ca5dd0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044f984`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f948.md#insn-0044f984) · [`0044f9f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f948.md#insn-0044f9f0) · [`0044fa30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f948.md#insn-0044fa30)
- 新版 [`0044f9c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f988.md#insn-0044f9c4) · [`0044fa30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f988.md#insn-0044fa30) · [`0044fa70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f988.md#insn-0044fa70)

~~~diff
- 0044f984 ["INT_ADD", "register:40f0:8", ["const:44f984:8", "const:4:8"]]
- 0044f984 ["CALL", null, ["callee:00c58040:8"]]
+ 0044f9c4 ["INT_ADD", "register:40f0:8", ["const:44f9c4:8", "const:4:8"]]
+ 0044f9c4 ["CALL", null, ["callee:00c58040:8"]]
- 0044f984 bytes 7b212094
+ 0044f9c4 bytes 9f212094
- 0044f9f0 ["INT_ADD", "register:40f0:8", ["const:44f9f0:8", "const:4:8"]]
- 0044f9f0 ["CALL", null, ["callee:00561d74:8"]]
+ 0044fa30 ["INT_ADD", "register:40f0:8", ["const:44fa30:8", "const:4:8"]]
+ 0044fa30 ["CALL", null, ["callee:00561d74:8"]]
- 0044f9f0 bytes d1480494
+ 0044fa30 bytes d1480494
- 0044fa30 ["COPY", "register:0:8", ["register:4040:8"]]
- 0044fa30 ["INT_ADD", "register:40f0:8", ["const:44fa30:8", "const:4:8"]]
- 0044fa30 ["CALLIND", null, ["register:0:8"]]
+ 0044fa70 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0044fa70 ["INT_ADD", "register:40f0:8", ["const:44fa70:8", "const:4:8"]]
+ 0044fa70 ["CALLIND", null, ["register:0:8"]]
- 0044fa30 bytes 00013fd6
+ 0044fa70 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d6439a525fa6a73eff32de2a2cf4614"></a>

### [`0044fd0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044fd0c.md) → [`0044fd4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044fd4c.md) FUN_0044fd4c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 10件 [`0044b534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b534.md) [`0045a768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a768.md) [`0045a76c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a76c.md) [`00561d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561d34.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)
- 新版 呼出元 1件 [`00856e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856e84.md) · 呼出先 10件 [`0044b574`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b574.md) [`0045a7a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a7a8.md) [`0045a7ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a7ac.md) [`00561d74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/00561d74.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0044fe20",
      "incomplete_value": false,
      "site": "0044fe20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:9d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044fde0",
      "incomplete_value": false,
      "site": "0044fde0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:900:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0044fd78",
      "incomplete_value": false,
      "site": "0044fd80",
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
            "const:fad:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044fd38",
      "incomplete_value": false,
      "site": "0044fd40",
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
            "const:f6d:8"
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
      "definition_site": "0044fde4",
      "incomplete_value": true,
      "site": "0044fdec",
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
                "const:c98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0044fda4",
      "incomplete_value": true,
      "site": "0044fdac",
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
                "const:bc8:8"
              ]
            ]
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
      "0044fd78",
      "PARAM",
      [
        "storage",
        "002c0f6d",
        null,
        "string"
      ]
    ],
    [
      "0044fde4",
      "READ",
      [
        "storage",
        "00c9abc8",
        null,
        "pointer"
      ]
    ],
    [
      "0044fde4",
      "PARAM",
      [
        "storage",
        "00ca5cd0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0044fd78",
      "PARAM",
      [
        "storage",
        "002c0fad",
        null,
        "string"
      ]
    ],
    [
      "0044fde4",
      "READ",
      [
        "storage",
        "00c9ac98",
        null,
        "pointer"
      ]
    ],
    [
      "0044fde4",
      "PARAM",
      [
        "storage",
        "00ca5dd0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0044fd40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044fd0c.md#insn-0044fd40) · [`0044fdac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044fd0c.md#insn-0044fdac) · [`0044fd30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044fd0c.md#insn-0044fd30)
- 新版 [`0044fd80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044fd4c.md#insn-0044fd80) · [`0044fdec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044fd4c.md#insn-0044fdec) · [`0044fd70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044fd4c.md#insn-0044fd70)

~~~diff
- 0044fd40 ["INT_ADD", "register:40f0:8", ["const:44fd40:8", "const:4:8"]]
- 0044fd40 ["CALL", null, ["callee:00c58040:8"]]
+ 0044fd80 ["INT_ADD", "register:40f0:8", ["const:44fd80:8", "const:4:8"]]
+ 0044fd80 ["CALL", null, ["callee:00c58040:8"]]
- 0044fd40 bytes 8c202094
+ 0044fd80 bytes b0202094
- 0044fdac ["INT_ADD", "register:40f0:8", ["const:44fdac:8", "const:4:8"]]
- 0044fdac ["CALL", null, ["callee:00561d74:8"]]
+ 0044fdec ["INT_ADD", "register:40f0:8", ["const:44fdec:8", "const:4:8"]]
+ 0044fdec ["CALL", null, ["callee:00561d74:8"]]
- 0044fdac bytes e2470494
+ 0044fdec bytes e2470494
- 0044fd30 ["INT_ADD", "register:40f0:8", ["const:44fd30:8", "const:4:8"]]
- 0044fd30 ["CALL", null, ["callee:0044b574:8"]]
+ 0044fd70 ["INT_ADD", "register:40f0:8", ["const:44fd70:8", "const:4:8"]]
+ 0044fd70 ["CALL", null, ["callee:0044b574:8"]]
- 0044fd30 bytes 01eeff97
+ 0044fd70 bytes 01eeff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99c4855e1f14c435d3ca101984541b70"></a>

### [`00450180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/00450180.md) → [`004501c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/004501c0.md) FUN_004501c0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`0045035c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/0045035c.md) [`0046593c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/0046593c.md) [`005ad7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad7e0.md) [`005ae8e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae8e4.md) · 呼出先 14件 [`0043db54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043db54.md) [`00446580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00446/00446580.md) [`0044b160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b160.md) [`00550c38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550c38.md) [`0055ec80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055ec80.md)
- 新版 呼出元 4件 [`0045039c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/0045039c.md) [`0046597c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00465/0046597c.md) [`005ad820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ad/005ad820.md) [`005ae924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ae/005ae924.md) · 呼出先 14件 [`0043db94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043db94.md) [`004465c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/004465c0.md) [`0044b1a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b1a0.md) [`00550c78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550c78.md) [`0055ecc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055ecc0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 78.12% / 新版 78.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `call_target` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00450228",
      "value": [
        "leaf",
        "ram:55ecc8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004501e8",
      "value": [
        "leaf",
        "ram:55ec88:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0045021c",
      "incomplete_value": false,
      "site": "00450228",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca4000:8"
          ],
          [
            "leaf",
            "const:bc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004501dc",
      "incomplete_value": false,
      "site": "004501e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca4000:8"
          ],
          [
            "leaf",
            "const:ac8:8"
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
      "definition_site": "0045028c",
      "incomplete_value": false,
      "site": "00450290",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca4000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045024c",
      "incomplete_value": false,
      "site": "00450250",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca4000:8"
          ],
          [
            "leaf",
            "const:ac0:8"
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
      "004501f0",
      "READ",
      [
        "storage",
        "00ca4ac0",
        null,
        "undefined1"
      ]
    ],
    [
      "00450200",
      "READ",
      [
        "storage",
        "00ca4ad8",
        null,
        "undefined1"
      ]
    ],
    [
      "0045021c",
      "PARAM",
      [
        "storage",
        "00ca4ac8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004501f0",
      "READ",
      [
        "storage",
        "00ca4bc0",
        null,
        "undefined1"
      ]
    ],
    [
      "00450200",
      "READ",
      [
        "storage",
        "00ca4bd8",
        null,
        "undefined1"
      ]
    ],
    [
      "0045021c",
      "PARAM",
      [
        "storage",
        "00ca4bc8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004501e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/00450180.md#insn-004501e8) · [`00450250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/00450180.md#insn-00450250) · [`0045026c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/00450180.md#insn-0045026c)
- 新版 [`00450228`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/004501c0.md#insn-00450228) · [`00450290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/004501c0.md#insn-00450290) · [`004502ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/004501c0.md#insn-004502ac)

~~~diff
- 004501e8 ["INT_ADD", "register:40f0:8", ["const:4501e8:8", "const:4:8"]]
- 004501e8 ["CALL", null, ["ram:55ec88:8"]]
+ 00450228 ["INT_ADD", "register:40f0:8", ["const:450228:8", "const:4:8"]]
+ 00450228 ["CALL", null, ["ram:55ecc8:8"]]
- 004501e8 bytes a83a0494
+ 00450228 bytes a83a0494
- 00450250 ["INT_ADD", "register:40f0:8", ["const:450250:8", "const:4:8"]]
- 00450250 ["CALL", null, ["callee:00c57f20:8"]]
+ 00450290 ["INT_ADD", "register:40f0:8", ["const:450290:8", "const:4:8"]]
+ 00450290 ["CALL", null, ["callee:00c57f20:8"]]
- 00450250 bytes 001f2094
+ 00450290 bytes 241f2094
- 0045026c ["COPY", "tmp:0:8", ["const:aa8:8"]]
- 0045026c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0045026c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0045026c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004502ac ["COPY", "tmp:0:8", ["const:ba8:8"]]
+ 004502ac ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004502ac ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004502ac ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0045026c bytes 21a02a91
+ 004502ac bytes 21a02e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56daaea9a5c06b405ed2a007f969990b"></a>

### [`0045035c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/0045035c.md) → [`0045039c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/0045039c.md) FUN_0045039c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00450750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/00450750.md) · 呼出先 9件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00450180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/00450180.md) [`00596f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596f2c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)
- 新版 呼出元 1件 [`00450790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/00450790.md) · 呼出先 9件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`004501c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/004501c0.md) [`00596f6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596f6c.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.54% / 新版 98.54%

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
      "definition_site": "00450434",
      "incomplete_value": true,
      "site": "00450434",
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
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:1e5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004503f4",
      "incomplete_value": true,
      "site": "004503f4",
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
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:1a5:8"
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
      "definition_site": "00450584",
      "incomplete_value": true,
      "site": "0045058c",
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
                "const:330:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00450544",
      "incomplete_value": true,
      "site": "0045054c",
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
                "const:2f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00450424",
      "READ",
      [
        "storage",
        "002b71a5",
        null,
        "string"
      ]
    ],
    [
      "00450584",
      "READ",
      [
        "storage",
        "002c42f0",
        null,
        "undefined8"
      ]
    ],
    [
      "004505c8",
      "READ",
      [
        "storage",
        "002c40d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00450424",
      "READ",
      [
        "storage",
        "002b71e5",
        null,
        "string"
      ]
    ],
    [
      "00450584",
      "READ",
      [
        "storage",
        "002c4330",
        null,
        "undefined8"
      ]
    ],
    [
      "004505c8",
      "READ",
      [
        "storage",
        "002c4110",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004503b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/0045035c.md#insn-004503b4) · [`00450434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/0045035c.md#insn-00450434) · [`004503a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/0045035c.md#insn-004503a8)
- 新版 [`004503f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/0045039c.md#insn-004503f4) · [`00450474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/0045039c.md#insn-00450474) · [`004503e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/0045039c.md#insn-004503e8)

~~~diff
- 004503b4 ["INT_ADD", "register:40f0:8", ["const:4503b4:8", "const:4:8"]]
- 004503b4 ["CALL", null, ["callee:00596f6c:8"]]
+ 004503f4 ["INT_ADD", "register:40f0:8", ["const:4503f4:8", "const:4:8"]]
+ 004503f4 ["CALL", null, ["callee:00596f6c:8"]]
- 004503b4 bytes de1a0594
+ 004503f4 bytes de1a0594
- 00450434 ["INT_ADD", "register:40f0:8", ["const:450434:8", "const:4:8"]]
- 00450434 ["CALL", null, ["callee:00c57f80:8"]]
+ 00450474 ["INT_ADD", "register:40f0:8", ["const:450474:8", "const:4:8"]]
+ 00450474 ["CALL", null, ["callee:00c57f80:8"]]
- 00450434 bytes 9f1e2094
+ 00450474 bytes c31e2094
- 004503a8 ["INT_ADD", "register:40f0:8", ["const:4503a8:8", "const:4:8"]]
- 004503a8 ["CALL", null, ["callee:00c53d70:8"]]
+ 004503e8 ["INT_ADD", "register:40f0:8", ["const:4503e8:8", "const:4:8"]]
+ 004503e8 ["CALL", null, ["callee:00c53d70:8"]]
- 004503a8 bytes 4a0e2094
+ 004503e8 bytes 620e2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e2ce33510b1a38b5d309cc4df45da8c"></a>

### [`00450750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/00450750.md) → [`00450790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/00450790.md) FUN_00450790

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`0045ab6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045ab6c.md) [`0046593c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/0046593c.md) [`005ad7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad7e0.md) [`005ae8e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae8e4.md) · 呼出先 3件 [`0045035c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/0045035c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 4件 [`0045abac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045abac.md) [`0046597c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00465/0046597c.md) [`005ad820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ad/005ad820.md) [`005ae924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ae/005ae924.md) · 呼出先 3件 [`0045039c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/0045039c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.62% / 新版 93.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004507b4",
      "incomplete_value": true,
      "site": "004507d4",
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
                "const:29f000:8"
              ],
              [
                "leaf",
                "const:eb6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00450774",
      "incomplete_value": true,
      "site": "00450794",
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
                "const:29f000:8"
              ],
              [
                "leaf",
                "const:f03:8"
              ]
            ]
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
      "004507b4",
      "READ",
      [
        "storage",
        "0029ff03",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004507b4",
      "READ",
      [
        "storage",
        "0029feb6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045076c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/00450750.md#insn-0045076c) · [`004507ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/00450750.md#insn-004507ac) · [`004507bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/00450750.md#insn-004507bc)
- 新版 [`004507ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/00450790.md#insn-004507ac) · [`004507ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/00450790.md#insn-004507ec) · [`004507fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/00450790.md#insn-004507fc)

~~~diff
- 0045076c ["COPY", "tmp:0:8", ["const:f03:8"]]
- 0045076c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0045076c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0045076c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 004507ac ["COPY", "tmp:0:8", ["const:eb6:8"]]
+ 004507ac ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 004507ac ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 004507ac ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0045076c bytes 4a0d3c91
+ 004507ac bytes 4ad93a91
- 004507ac ["COPY", "register:0:8", ["register:4048:8"]]
- 004507ac ["INT_ADD", "register:40f0:8", ["const:4507ac:8", "const:4:8"]]
- 004507ac ["CALLIND", null, ["register:0:8"]]
+ 004507ec ["COPY", "register:0:8", ["register:4048:8"]]
+ 004507ec ["INT_ADD", "register:40f0:8", ["const:4507ec:8", "const:4:8"]]
+ 004507ec ["CALLIND", null, ["register:0:8"]]
- 004507ac bytes 20013fd6
+ 004507ec bytes 20013fd6
- 004507bc ["INT_ADD", "register:40f0:8", ["const:4507bc:8", "const:4:8"]]
- 004507bc ["CALL", null, ["callee:00c57f80:8"]]
+ 004507fc ["INT_ADD", "register:40f0:8", ["const:4507fc:8", "const:4:8"]]
+ 004507fc ["CALL", null, ["callee:00c57f80:8"]]
- 004507bc bytes bd1d2094
+ 004507fc bytes e11d2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4a269d32c67ecaa71a0ec4ea2cc3ea3"></a>

### [`0045084c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/0045084c.md) → [`0045088c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/0045088c.md) FUN_0045088c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`00451ed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/00451ed8.md) [`004524e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00452/004524e8.md) [`00452c54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00452/00452c54.md) [`004532b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/004532b8.md) [`00453cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/00453cb0.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`004509b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/004509b0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 5件 [`00451f18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/00451f18.md) [`00452528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00452/00452528.md) [`00452c94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00452/00452c94.md) [`004532f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00453/004532f8.md) [`00453cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00453/00453cf0.md) · 呼出先 4件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`004509f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/004509f0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.59% / 新版 98.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0045093c",
      "incomplete_value": true,
      "site": "00450950",
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
                "const:cd8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004508fc",
      "incomplete_value": true,
      "site": "00450910",
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
                "const:c08:8"
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
      "0045093c",
      "READ",
      [
        "storage",
        "00c9ac08",
        null,
        "pointer"
      ]
    ],
    [
      "0045093c",
      "PARAM",
      [
        "storage",
        "00ca5ce8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0045093c",
      "READ",
      [
        "storage",
        "00c9acd8",
        null,
        "pointer"
      ]
    ],
    [
      "0045093c",
      "PARAM",
      [
        "storage",
        "00ca5de8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00450910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/0045084c.md#insn-00450910) · [`004508ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/0045084c.md#insn-004508ac) · [`004508e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/0045084c.md#insn-004508e4)
- 新版 [`00450950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/0045088c.md#insn-00450950) · [`004508ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/0045088c.md#insn-004508ec) · [`00450924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/0045088c.md#insn-00450924)

~~~diff
- 00450910 ["INT_ADD", "register:40f0:8", ["const:450910:8", "const:4:8"]]
- 00450910 ["CALL", null, ["callee:004509f0:8"]]
+ 00450950 ["INT_ADD", "register:40f0:8", ["const:450950:8", "const:4:8"]]
+ 00450950 ["CALL", null, ["callee:004509f0:8"]]
- 00450910 bytes 28000094
+ 00450950 bytes 28000094
- 004508ac ["INT_ADD", "register:40f0:8", ["const:4508ac:8", "const:4:8"]]
- 004508ac ["CALL", null, ["callee:0043bb60:8"]]
+ 004508ec ["INT_ADD", "register:40f0:8", ["const:4508ec:8", "const:4:8"]]
+ 004508ec ["CALL", null, ["callee:0043bb60:8"]]
- 004508ac bytes 9dacff97
+ 004508ec bytes 9dacff97
- 004508e4 ["INT_ADD", "register:40f0:8", ["const:4508e4:8", "const:4:8"]]
- 004508e4 ["CALL", null, ["callee:0043bb60:8"]]
+ 00450924 ["INT_ADD", "register:40f0:8", ["const:450924:8", "const:4:8"]]
+ 00450924 ["CALL", null, ["callee:0043bb60:8"]]
- 004508e4 bytes 8facff97
+ 00450924 bytes 8facff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b652bea9aea24f8abb94b1969b74068f"></a>

### [`004509b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/004509b0.md) → [`004509f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/004509f0.md) FUN_004509f0

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 11件 [`0045084c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/0045084c.md) [`00454844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00454/00454844.md) [`00454d28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00454/00454d28.md) [`004552f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00455/004552f8.md) [`004557dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00455/004557dc.md) · 呼出先 28件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044ff5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044ff5c.md) [`0045179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/0045179c.md) [`004518b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004518b0.md) [`004519d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004519d8.md)
- 新版 呼出元 11件 [`0045088c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/0045088c.md) [`00454884`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00454/00454884.md) [`00454d68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00454/00454d68.md) [`00455338`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00455/00455338.md) [`0045581c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00455/0045581c.md) · 呼出先 28件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0044ff9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044ff9c.md) [`004517dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/004517dc.md) [`004518f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/004518f0.md) [`00451a18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/00451a18.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 91.65% / 新版 91.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 1件, `store_value` 19件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00450b58",
      "incomplete_value": true,
      "site": "00450b60",
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
      "definition_site": "00450b18",
      "incomplete_value": true,
      "site": "00450b20",
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
    "ordinal": 25,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00450b68",
      "incomplete_value": true,
      "site": "00450b68",
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
                "register:8:8"
              ],
              [
                "leaf",
                "const:180:8"
              ]
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "LOAD",
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
      "definition_site": "00450b28",
      "incomplete_value": true,
      "site": "00450b28",
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
                "register:8:8"
              ],
              [
                "leaf",
                "const:180:8"
              ]
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00450b68",
      "incomplete_value": true,
      "site": "00450b68",
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
              [
                "leaf",
                "const:40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00450b28",
      "incomplete_value": true,
      "site": "00450b28",
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
              [
                "leaf",
                "const:40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00450b54",
      "READ",
      [
        "storage",
        "00c9ac10",
        null,
        "pointer"
      ]
    ],
    [
      "00450b58",
      "READ",
      [
        "storage",
        "00c930e8",
        "_ZTTNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "00450b5c",
      "READ",
      [
        "storage",
        "00c93128",
        null,
        "pointer __((offset(0x68)))"
      ]
    ]
  ],
  "added": [
    [
      "00450b54",
      "READ",
      [
        "storage",
        "00c9ace0",
        null,
        "pointer"
      ]
    ],
    [
      "00450b58",
      "READ",
      [
        "storage",
        "00c931b8",
        "_ZTTNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "00450b5c",
      "READ",
      [
        "storage",
        "00c931f8",
        null,
        "pointer __((offset(0x68)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00450bf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/004509b0.md#insn-00450bf4) · [`00450c34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/004509b0.md#insn-00450c34) · [`00450c70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/004509b0.md#insn-00450c70)
- 新版 [`00450c34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/004509f0.md#insn-00450c34) · [`00450c74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/004509f0.md#insn-00450c74) · [`00450cb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/004509f0.md#insn-00450cb0)

~~~diff
- 00450bf4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00450bf4 ["INT_ADD", "register:40f0:8", ["const:450bf4:8", "const:4:8"]]
- 00450bf4 ["CALLIND", null, ["register:0:8"]]
+ 00450c34 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00450c34 ["INT_ADD", "register:40f0:8", ["const:450c34:8", "const:4:8"]]
+ 00450c34 ["CALLIND", null, ["register:0:8"]]
- 00450bf4 bytes 00013fd6
+ 00450c34 bytes 00013fd6
- 00450c34 ["INT_ADD", "register:40f0:8", ["const:450c34:8", "const:4:8"]]
- 00450c34 ["CALL", null, ["callee:00c58180:8"]]
+ 00450c74 ["INT_ADD", "register:40f0:8", ["const:450c74:8", "const:4:8"]]
+ 00450c74 ["CALL", null, ["callee:00c58180:8"]]
- 00450c34 bytes 1f1d2094
+ 00450c74 bytes 431d2094
- 00450c70 ["INT_ADD", "register:40f0:8", ["const:450c70:8", "const:4:8"]]
- 00450c70 ["CALL", null, ["callee:00c58180:8"]]
+ 00450cb0 ["INT_ADD", "register:40f0:8", ["const:450cb0:8", "const:4:8"]]
+ 00450cb0 ["CALL", null, ["callee:00c58180:8"]]
- 00450c70 bytes 101d2094
+ 00450cb0 bytes 341d2094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b2bfc59dc557ec06a6d2da5bfe64e30"></a>

### [`0045179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/0045179c.md) → [`004517dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/004517dc.md) FUN_004517dc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 27件 [`004509b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/004509b0.md) [`00451ed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/00451ed8.md) [`004524e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00452/004524e8.md) [`00452c54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00452/00452c54.md) [`004532b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/004532b8.md) · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00458d28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/00458d28.md) [`004593f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004593f0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 27件 [`004509f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/004509f0.md) [`00451f18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/00451f18.md) [`00452528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00452/00452528.md) [`00452c94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00452/00452c94.md) [`004532f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00453/004532f8.md) · 呼出先 5件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00458d68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00458/00458d68.md) [`00459430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459430.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.15% / 新版 96.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00451828",
      "incomplete_value": false,
      "site": "0045182c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:830:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004517e8",
      "incomplete_value": false,
      "site": "004517ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:760:8"
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
      "0045182c",
      "DATA",
      [
        "storage",
        "00c63760",
        null,
        "pointer"
      ]
    ],
    [
      "00451878",
      "READ",
      [
        "storage",
        "00c63768",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045182c",
      "DATA",
      [
        "storage",
        "00c63830",
        null,
        "pointer"
      ]
    ],
    [
      "00451878",
      "READ",
      [
        "storage",
        "00c63838",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004517d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/0045179c.md#insn-004517d0) · [`004517e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/0045179c.md#insn-004517e8) · [`00451810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/0045179c.md#insn-00451810)
- 新版 [`00451810`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/004517dc.md#insn-00451810) · [`00451828`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/004517dc.md#insn-00451828) · [`00451850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/004517dc.md#insn-00451850)

~~~diff
- 004517d0 ["INT_ADD", "register:40f0:8", ["const:4517d0:8", "const:4:8"]]
- 004517d0 ["CALL", null, ["callee:00c57f60:8"]]
+ 00451810 ["INT_ADD", "register:40f0:8", ["const:451810:8", "const:4:8"]]
+ 00451810 ["CALL", null, ["callee:00c57f60:8"]]
- 004517d0 bytes b0192094
+ 00451810 bytes d4192094
- 004517e8 ["COPY", "tmp:0:8", ["const:760:8"]]
- 004517e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004517e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004517e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00451828 ["COPY", "tmp:0:8", ["const:830:8"]]
+ 00451828 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00451828 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00451828 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004517e8 bytes 08811d91
+ 00451828 bytes 08c12091
- 00451810 ["INT_ADD", "register:40f0:8", ["const:451810:8", "const:4:8"]]
- 00451810 ["CALL", null, ["callee:0043bb60:8"]]
+ 00451850 ["INT_ADD", "register:40f0:8", ["const:451850:8", "const:4:8"]]
+ 00451850 ["CALL", null, ["callee:0043bb60:8"]]
- 00451810 bytes c4a8ff97
+ 00451850 bytes c4a8ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afd036f8d79699608d3550e5ac10ee7f"></a>

### [`004518b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004518b0.md) → [`004518f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/004518f0.md) FUN_004518f0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 15件 [`004509b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/004509b0.md) [`00456efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00456/00456efc.md) [`00457400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00457/00457400.md) [`00457878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00457/00457878.md) [`004973c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/004973c0.md) · 呼出先 2件 [`00c581e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581e0.md) [`00c581f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581f0.md)
- 新版 呼出元 15件 [`004509f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/004509f0.md) [`00456f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00456/00456f3c.md) [`00457440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00457/00457440.md) [`004578b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00457/004578b8.md) [`00497400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497400.md) · 呼出先 2件 [`00c582b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c582b0.md) [`00c582c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c582c0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00451934",
      "incomplete_value": true,
      "site": "00451934",
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
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004518f4",
      "incomplete_value": true,
      "site": "004518f4",
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
            "const:68:8"
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
      "definition_site": "00451938",
      "incomplete_value": true,
      "site": "00451938",
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
      "definition_site": "004518f8",
      "incomplete_value": true,
      "site": "004518f8",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00451930",
      "incomplete_value": true,
      "site": "00451940",
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
              [
                "leaf",
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004518f0",
      "incomplete_value": true,
      "site": "00451900",
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
              [
                "leaf",
                "const:10:8"
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
      "00451914",
      "READ",
      [
        "storage",
        "00c9ac18",
        null,
        "pointer"
      ]
    ],
    [
      "00451920",
      "READ",
      [
        "storage",
        "00c9ac10",
        null,
        "pointer"
      ]
    ],
    [
      "00451930",
      "READ",
      [
        "storage",
        "00c930f8",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "00451914",
      "READ",
      [
        "storage",
        "00c9ace8",
        null,
        "pointer"
      ]
    ],
    [
      "00451920",
      "READ",
      [
        "storage",
        "00c9ace0",
        null,
        "pointer"
      ]
    ],
    [
      "00451930",
      "READ",
      [
        "storage",
        "00c931c8",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004518d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004518b0.md#insn-004518d4) · [`004518dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004518b0.md#insn-004518dc) · [`004518e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004518b0.md#insn-004518e0)
- 新版 [`00451914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/004518f0.md#insn-00451914) · [`00451920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/004518f0.md#insn-00451920)

~~~diff
- 004518d4 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:c18:8"]]
- 004518d4 ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00451914 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:ce8:8"]]
+ 00451914 ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
- 004518d4 bytes f70e46f9
+ 00451914 bytes f77646f9
- 004518dc ["COPY", "register:40d0:8", ["register:4000:8"]]
- 004518dc bytes fa0300aa
- 004518e0 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:c10:8"]]
- 004518e0 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00451920 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:ce0:8"]]
+ 00451920 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
- 004518e0 bytes d60a46f9
+ 00451920 bytes d67246f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e6d86ceb5b43a7632e011742b525471"></a>

### [`004519d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004519d8.md) → [`00451a18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/00451a18.md) FUN_00451a18

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 15件 [`004509b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/004509b0.md) [`004519d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004519d8.md) [`00456efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00456/00456efc.md) [`00457400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00457/00457400.md) [`00457878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00457/00457878.md) · 呼出先 7件 [`004519d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004519d8.md) [`004594d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004594d0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58200.md)
- 新版 呼出元 15件 [`004509f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/004509f0.md) [`00451a18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/00451a18.md) [`00456f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00456/00456f3c.md) [`00457440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00457/00457440.md) [`004578b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00457/004578b8.md) · 呼出先 7件 [`00451a18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/00451a18.md) [`00459510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459510.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c582d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c582d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00451ac4",
      "incomplete_value": false,
      "site": "00451acc",
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
            "const:ecd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00451a84",
      "incomplete_value": false,
      "site": "00451a8c",
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
            "const:e8d:8"
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
      "definition_site": "00451b10",
      "incomplete_value": false,
      "site": "00451b18",
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
            "const:ecd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00451ad0",
      "incomplete_value": false,
      "site": "00451ad8",
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
            "const:e8d:8"
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
      "definition_site": "00451b80",
      "incomplete_value": false,
      "site": "00451b88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bf000:8"
          ],
          [
            "leaf",
            "const:b86:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00451b40",
      "incomplete_value": false,
      "site": "00451b48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bf000:8"
          ],
          [
            "leaf",
            "const:bda:8"
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
      "00451a8c",
      "PARAM",
      [
        "storage",
        "0029eda0",
        null,
        "string"
      ]
    ],
    [
      "00451ac4",
      "PARAM",
      [
        "storage",
        "002b5e8d",
        null,
        null
      ]
    ],
    [
      "00451b10",
      "PARAM",
      [
        "storage",
        "002b5e8d",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00451a8c",
      "PARAM",
      [
        "storage",
        "0029ede0",
        null,
        "string"
      ]
    ],
    [
      "00451ac4",
      "PARAM",
      [
        "storage",
        "002b5ecd",
        null,
        null
      ]
    ],
    [
      "00451b10",
      "PARAM",
      [
        "storage",
        "002b5ecd",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00451a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004519d8.md#insn-00451a8c) · [`00451ad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004519d8.md#insn-00451ad8) · [`00451b18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004519d8.md#insn-00451b18)
- 新版 [`00451acc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/00451a18.md#insn-00451acc) · [`00451b18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/00451a18.md#insn-00451b18) · [`00451b58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/00451a18.md#insn-00451b58)

~~~diff
- 00451a8c ["INT_ADD", "register:40f0:8", ["const:451a8c:8", "const:4:8"]]
- 00451a8c ["CALL", null, ["callee:00459510:8"]]
+ 00451acc ["INT_ADD", "register:40f0:8", ["const:451acc:8", "const:4:8"]]
+ 00451acc ["CALL", null, ["callee:00459510:8"]]
- 00451a8c bytes 911e0094
+ 00451acc bytes 911e0094
- 00451ad8 ["INT_ADD", "register:40f0:8", ["const:451ad8:8", "const:4:8"]]
- 00451ad8 ["CALL", null, ["callee:00459510:8"]]
+ 00451b18 ["INT_ADD", "register:40f0:8", ["const:451b18:8", "const:4:8"]]
+ 00451b18 ["CALL", null, ["callee:00459510:8"]]
- 00451ad8 bytes 7e1e0094
+ 00451b18 bytes 7e1e0094
- 00451b18 ["INT_ADD", "register:40f0:8", ["const:451b18:8", "const:4:8"]]
- 00451b18 ["CALL", null, ["callee:00c582d0:8"]]
+ 00451b58 ["INT_ADD", "register:40f0:8", ["const:451b58:8", "const:4:8"]]
+ 00451b58 ["CALL", null, ["callee:00c582d0:8"]]
- 00451b18 bytes ba192094
+ 00451b58 bytes de192094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20ac2139054246332d71f3944756564a"></a>

### [`00451d4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/00451d4c.md) → [`00451d8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/00451d8c.md) FUN_00451d8c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fa0.md) [`00c57fc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fc0.md) [`00c581c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581c0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58070.md) [`00c58090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58090.md) [`00c58290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58290.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 65.62% / 新版 65.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00451db0",
      "incomplete_value": true,
      "site": "00451db8",
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
      "definition_site": "00451d70",
      "incomplete_value": true,
      "site": "00451d78",
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00451dc4",
      "incomplete_value": true,
      "site": "00451dc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4000:8"
          ],
          [
            "INT_LEFT",
            "8",
            [
              "LOAD",
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
      "definition_site": "00451d84",
      "incomplete_value": true,
      "site": "00451d84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4000:8"
          ],
          [
            "INT_LEFT",
            "8",
            [
              "LOAD",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00451dc4",
      "incomplete_value": true,
      "site": "00451dc4",
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
              [
                "leaf",
                "const:40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00451d84",
      "incomplete_value": true,
      "site": "00451d84",
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
              [
                "leaf",
                "const:40:8"
              ]
            ]
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
      "00451da8",
      "READ",
      [
        "storage",
        "00c9ac10",
        null,
        "pointer"
      ]
    ],
    [
      "00451db0",
      "READ",
      [
        "storage",
        "00c930e8",
        "_ZTTNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "00451db4",
      "READ",
      [
        "storage",
        "00c93128",
        null,
        "pointer __((offset(0x68)))"
      ]
    ]
  ],
  "added": [
    [
      "00451da8",
      "READ",
      [
        "storage",
        "00c9ace0",
        null,
        "pointer"
      ]
    ],
    [
      "00451db0",
      "READ",
      [
        "storage",
        "00c931b8",
        "_ZTTNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "00451db4",
      "READ",
      [
        "storage",
        "00c931f8",
        null,
        "pointer __((offset(0x68)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00451d68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/00451d4c.md#insn-00451d68) · [`00451d6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/00451d4c.md#insn-00451d6c) · [`00451d80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/00451d4c.md#insn-00451d80)
- 新版 [`00451da8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/00451d8c.md#insn-00451da8) · [`00451dc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/00451d8c.md#insn-00451dc0)

~~~diff
- 00451d68 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:c10:8"]]
- 00451d68 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00451da8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:ce0:8"]]
+ 00451da8 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
- 00451d68 bytes b50a46f9
+ 00451da8 bytes b57246f9
- 00451d6c ["COPY", "register:4098:8", ["register:4000:8"]]
- 00451d6c bytes f30300aa
- 00451d80 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:bc0:8"]]
- 00451d80 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00451dc0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:c90:8"]]
+ 00451dc0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00451d80 bytes 29e145f9
+ 00451dc0 bytes 294946f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8fe2dbe57b40d71309628f5f118530c4"></a>

### [`00451ed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/00451ed8.md) → [`00451f18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/00451f18.md) FUN_00451f18

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008806a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/008806a8.md) · 呼出先 16件 [`0044b3f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b3f4.md) [`0045084c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/0045084c.md) [`0045179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/0045179c.md) [`0045982c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/0045982c.md) [`0045bdcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bdcc.md)
- 新版 呼出元 1件 [`00880700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00880/00880700.md) · 呼出先 16件 [`0044b434`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b434.md) [`0045088c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/0045088c.md) [`004517dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/004517dc.md) [`0045986c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/0045986c.md) [`0045be0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045be0c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.21% / 新版 93.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 7件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00451fa0",
      "incomplete_value": false,
      "site": "00451fa8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:b60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00451f60",
      "incomplete_value": false,
      "site": "00451f68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:a90:8"
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00451fc8",
      "incomplete_value": false,
      "site": "00451fc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:bb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00451f88",
      "incomplete_value": false,
      "site": "00451f88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
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
      "definition_site": "00452004",
      "incomplete_value": true,
      "site": "00452004",
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
                "const:ee0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00451fc4",
      "incomplete_value": true,
      "site": "00451fc4",
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
                "const:f2d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00451f60",
      "PARAM",
      [
        "storage",
        "002b7f92",
        null,
        "string"
      ]
    ],
    [
      "00451fa8",
      "DATA",
      [
        "storage",
        "00c63a90",
        null,
        "pointer"
      ]
    ],
    [
      "00451fc8",
      "DATA",
      [
        "storage",
        "00c63ae0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00451f60",
      "PARAM",
      [
        "storage",
        "002b7fd2",
        null,
        "string"
      ]
    ],
    [
      "00451fa8",
      "DATA",
      [
        "storage",
        "00c63b60",
        null,
        "pointer"
      ]
    ],
    [
      "00451fc8",
      "DATA",
      [
        "storage",
        "00c63bb0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00451f28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/00451ed8.md#insn-00451f28) · [`00451f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/00451ed8.md#insn-00451f18) · [`00451f20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/00451ed8.md#insn-00451f20)
- 新版 [`00451f68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/00451f18.md#insn-00451f68) · [`00451f58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/00451f18.md#insn-00451f58) · [`00451f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/00451f18.md#insn-00451f60)

~~~diff
- 00451f28 ["INT_ADD", "register:40f0:8", ["const:451f28:8", "const:4:8"]]
- 00451f28 ["CALL", null, ["callee:00c58040:8"]]
+ 00451f68 ["INT_ADD", "register:40f0:8", ["const:451f68:8", "const:4:8"]]
+ 00451f68 ["CALL", null, ["callee:00c58040:8"]]
- 00451f28 bytes 12182094
+ 00451f68 bytes 36182094
- 00451f18 ["INT_ADD", "register:40f0:8", ["const:451f18:8", "const:4:8"]]
- 00451f18 ["CALL", null, ["callee:0044b434:8"]]
+ 00451f58 ["INT_ADD", "register:40f0:8", ["const:451f58:8", "const:4:8"]]
+ 00451f58 ["CALL", null, ["callee:0044b434:8"]]
- 00451f18 bytes 37e5ff97
+ 00451f58 bytes 37e5ff97
- 00451f20 ["COPY", "tmp:0:8", ["const:f92:8"]]
- 00451f20 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00451f20 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00451f20 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00451f60 ["COPY", "tmp:0:8", ["const:fd2:8"]]
+ 00451f60 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00451f60 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00451f60 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00451f20 bytes 21483e91
+ 00451f60 bytes 21483f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8eb259cf4e5c5122819ed6c44acd1422"></a>

### [`004524e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00452/004524e8.md) → [`00452528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00452/00452528.md) FUN_00452528

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008806a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/008806a8.md) · 呼出先 20件 [`0044b3f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b3f4.md) [`0045084c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/0045084c.md) [`0045179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/0045179c.md) [`00452bc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00452/00452bc4.md) [`0045bdcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bdcc.md)
- 新版 呼出元 1件 [`00880700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00880/00880700.md) · 呼出先 20件 [`0044b434`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b434.md) [`0045088c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/0045088c.md) [`004517dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/004517dc.md) [`00452c04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00452/00452c04.md) [`0045be0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045be0c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 86.31% / 新版 86.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 13件, `store_destination` 6件, `store_value` 6件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "004525fc",
      "incomplete_value": true,
      "site": "004525fc",
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
            "const:c18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004525bc",
      "incomplete_value": true,
      "site": "004525bc",
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
            "const:b18:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00452604",
      "incomplete_value": true,
      "site": "00452604",
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
            "const:c18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004525c4",
      "incomplete_value": true,
      "site": "004525c4",
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
            "const:b18:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00452614",
      "incomplete_value": true,
      "site": "00452614",
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
            "const:c30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004525d4",
      "incomplete_value": true,
      "site": "004525d4",
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
            "const:b30:8"
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
      "0045256c",
      "READ",
      [
        "storage",
        "00ca4b08",
        null,
        "undefined1"
      ]
    ],
    [
      "0045257c",
      "READ",
      [
        "storage",
        "00ca4b28",
        null,
        "undefined1"
      ]
    ],
    [
      "00452588",
      "PARAM",
      [
        "storage",
        "00ca4ae0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0045256c",
      "READ",
      [
        "storage",
        "00ca4c08",
        null,
        "undefined1"
      ]
    ],
    [
      "0045257c",
      "READ",
      [
        "storage",
        "00ca4c28",
        null,
        "undefined1"
      ]
    ],
    [
      "00452588",
      "PARAM",
      [
        "storage",
        "00ca4be0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045254c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00452/004524e8.md#insn-0045254c) · [`00452598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00452/004524e8.md#insn-00452598)
- 新版 [`0045258c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00452/00452528.md#insn-0045258c) · [`004525d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00452/00452528.md#insn-004525d8) · [`00452598`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00452/00452528.md#insn-00452598)

~~~diff
- 0045254c ["INT_ADD", "register:40f0:8", ["const:45254c:8", "const:4:8"]]
- 0045254c ["CALL", null, ["callee:00c581b0:8"]]
+ 0045258c ["INT_ADD", "register:40f0:8", ["const:45258c:8", "const:4:8"]]
+ 0045258c ["CALL", null, ["callee:00c581b0:8"]]
- 0045254c bytes e5162094
+ 0045258c bytes 09172094
- 00452598 ["INT_ADD", "register:40f0:8", ["const:452598:8", "const:4:8"]]
- 00452598 ["CALL", null, ["callee:0045cad8:8"]]
+ 004525d8 ["INT_ADD", "register:40f0:8", ["const:4525d8:8", "const:4:8"]]
+ 004525d8 ["CALL", null, ["callee:0045cad8:8"]]
- 00452598 bytes 40290094
+ 004525d8 bytes 40290094
+ 00452598 ["COPY", "register:40b0:8", ["const:ca4000:8"]]
+ 00452598 bytes 964200d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-677dc266c95e4ca26432ad60d234c7cd"></a>

### [`00452c54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00452/00452c54.md) → [`00452c94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00452/00452c94.md) FUN_00452c94

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 5件 [`0045ab6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045ab6c.md) [`00599804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00599/00599804.md) [`0079b110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079b/0079b110.md) [`00880cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/00880cf4.md) [`008a6e4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a6/008a6e4c.md) · 呼出先 24件 [`0044b3f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b3f4.md) [`0045084c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/0045084c.md) [`0045179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/0045179c.md) [`004531d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/004531d8.md) [`00459ad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459ad0.md)
- 新版 呼出元 5件 [`0045abac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045abac.md) [`00599844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/00599844.md) [`0079b168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079b/0079b168.md) [`00880d4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00880/00880d4c.md) [`008a6ea4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008a6/008a6ea4.md) · 呼出先 24件 [`0044b434`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b434.md) [`0045088c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/0045088c.md) [`004517dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/004517dc.md) [`00453218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00453/00453218.md) [`00459b10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459b10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 82.78% / 新版 82.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 13件, `store_destination` 6件, `store_value` 6件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00452d68",
      "incomplete_value": true,
      "site": "00452d68",
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
            "const:c70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00452d28",
      "incomplete_value": true,
      "site": "00452d28",
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
            "const:b70:8"
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
      "definition_site": "00452d70",
      "incomplete_value": true,
      "site": "00452d70",
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
            "const:c70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00452d30",
      "incomplete_value": true,
      "site": "00452d30",
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
            "const:b70:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00452d80",
      "incomplete_value": true,
      "site": "00452d80",
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
            "const:c88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00452d40",
      "incomplete_value": true,
      "site": "00452d40",
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
            "const:b88:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00452cd8",
      "READ",
      [
        "storage",
        "00ca4b60",
        null,
        "undefined1"
      ]
    ],
    [
      "00452ce8",
      "READ",
      [
        "storage",
        "00ca4b80",
        null,
        "undefined1"
      ]
    ],
    [
      "00452cf4",
      "PARAM",
      [
        "storage",
        "00ca4b34",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00452cd8",
      "READ",
      [
        "storage",
        "00ca4c60",
        null,
        "undefined1"
      ]
    ],
    [
      "00452ce8",
      "READ",
      [
        "storage",
        "00ca4c80",
        null,
        "undefined1"
      ]
    ],
    [
      "00452cf4",
      "PARAM",
      [
        "storage",
        "00ca4c34",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00452cb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00452/00452c54.md#insn-00452cb8) · [`00452d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00452/00452c54.md#insn-00452d04)
- 新版 [`00452cf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00452/00452c94.md#insn-00452cf8) · [`00452d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00452/00452c94.md#insn-00452d44) · [`00452d04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00452/00452c94.md#insn-00452d04)

~~~diff
- 00452cb8 ["INT_ADD", "register:40f0:8", ["const:452cb8:8", "const:4:8"]]
- 00452cb8 ["CALL", null, ["callee:00c581b0:8"]]
+ 00452cf8 ["INT_ADD", "register:40f0:8", ["const:452cf8:8", "const:4:8"]]
+ 00452cf8 ["CALL", null, ["callee:00c581b0:8"]]
- 00452cb8 bytes 0a152094
+ 00452cf8 bytes 2e152094
- 00452d04 ["INT_ADD", "register:40f0:8", ["const:452d04:8", "const:4:8"]]
- 00452d04 ["CALL", null, ["callee:0045dbb8:8"]]
+ 00452d44 ["INT_ADD", "register:40f0:8", ["const:452d44:8", "const:4:8"]]
+ 00452d44 ["CALL", null, ["callee:0045dbb8:8"]]
- 00452d04 bytes 9d2b0094
+ 00452d44 bytes 9d2b0094
+ 00452d04 ["COPY", "register:40c0:8", ["const:ca4000:8"]]
+ 00452d04 bytes 984200d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d290a12e8cdc8cc1f473a1be703db31d"></a>

### [`004532b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/004532b8.md) → [`004532f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00453/004532f8.md) FUN_004532f8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`004539dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/004539dc.md) · 呼出先 16件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044b444`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b444.md) [`0045084c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/0045084c.md) [`0045179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/0045179c.md) [`0045982c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/0045982c.md)
- 新版 呼出元 1件 [`00453a1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00453/00453a1c.md) · 呼出先 16件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0044b484`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b484.md) [`0045088c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/0045088c.md) [`004517dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/004517dc.md) [`0045986c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/0045986c.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.22% / 新版 93.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `store_value` 8件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00453398",
      "incomplete_value": false,
      "site": "004533a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:b60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00453358",
      "incomplete_value": false,
      "site": "00453360",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:a90:8"
          ]
        ]
      ]
    },
    "ordinal": 21,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004533ac",
      "incomplete_value": false,
      "site": "004533ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:bb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045336c",
      "incomplete_value": false,
      "site": "0045336c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00453450",
      "incomplete_value": true,
      "site": "00453460",
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
                "const:94c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00453410",
      "incomplete_value": true,
      "site": "00453420",
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
                "const:91b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 37,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0045334c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0044b444"
      ]
    ],
    [
      "00453354",
      "PARAM",
      [
        "storage",
        "002c0f8a",
        null,
        "string"
      ]
    ],
    [
      "004533a0",
      "DATA",
      [
        "storage",
        "00c63a90",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0045334c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0044b484"
      ]
    ],
    [
      "00453354",
      "PARAM",
      [
        "storage",
        "002c0fca",
        null,
        "string"
      ]
    ],
    [
      "004533a0",
      "DATA",
      [
        "storage",
        "00c63b60",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045330c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/004532b8.md#insn-0045330c) · [`0045331c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/004532b8.md#insn-0045331c) · [`0045335c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/004532b8.md#insn-0045335c)
- 新版 [`0045334c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00453/004532f8.md#insn-0045334c) · [`0045335c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00453/004532f8.md#insn-0045335c)

~~~diff
- 0045330c ["INT_ADD", "register:40f0:8", ["const:45330c:8", "const:4:8"]]
- 0045330c ["CALL", null, ["ram:44b444:8"]]
+ 0045334c ["INT_ADD", "register:40f0:8", ["const:45334c:8", "const:4:8"]]
+ 0045334c ["CALL", null, ["ram:44b484:8"]]
- 0045330c bytes 4ee0ff97
+ 0045334c bytes 4ee0ff97
- 0045331c ["INT_ADD", "register:40f0:8", ["const:45331c:8", "const:4:8"]]
- 0045331c ["CALL", null, ["callee:00c58040:8"]]
+ 0045335c ["INT_ADD", "register:40f0:8", ["const:45335c:8", "const:4:8"]]
+ 0045335c ["CALL", null, ["callee:00c58040:8"]]
- 0045331c bytes 15132094
+ 0045335c bytes 39132094
- 0045335c ["COPY", "register:40e0:8", ["register:4000:8"]]
- 0045335c bytes fc0300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2bed246c7a91114fd844e69bf99aecaf"></a>

### [`004539dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/004539dc.md) → [`00453a1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00453/00453a1c.md) FUN_00453a1c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`004766c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/004766c8.md) [`004779cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00477/004779cc.md) · 呼出先 12件 [`004532b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/004532b8.md) [`0045a6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a6d4.md) [`0045ee5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045ee5c.md) [`0045fa3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fa3c.md) [`0045fa8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fa8c.md)
- 新版 呼出元 2件 [`00476708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00476/00476708.md) [`00477a0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00477/00477a0c.md) · 呼出先 12件 [`004532f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00453/004532f8.md) [`0045a714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a714.md) [`0045ee9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045ee9c.md) [`0045fa7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045fa7c.md) [`0045facc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045facc.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00453a74",
      "incomplete_value": false,
      "site": "00453a84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:f40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00453a34",
      "incomplete_value": false,
      "site": "00453a44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:e70:8"
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00453aa8",
      "incomplete_value": false,
      "site": "00453ab0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:f90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00453a68",
      "incomplete_value": false,
      "site": "00453a70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:ec0:8"
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00453b1c",
      "incomplete_value": false,
      "site": "00453b1c",
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
            "const:e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00453adc",
      "incomplete_value": false,
      "site": "00453adc",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "ordinal": 36,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00453a84",
      "DATA",
      [
        "storage",
        "00c63e70",
        null,
        "pointer"
      ]
    ],
    [
      "00453ab0",
      "DATA",
      [
        "storage",
        "00c63ec0",
        null,
        "undefined *"
      ]
    ],
    [
      "00453b1c",
      "DATA",
      [
        "storage",
        "00c64018",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00453a84",
      "DATA",
      [
        "storage",
        "00c63f40",
        null,
        "pointer"
      ]
    ],
    [
      "00453ab0",
      "DATA",
      [
        "storage",
        "00c63f90",
        null,
        "undefined *"
      ]
    ],
    [
      "00453b1c",
      "DATA",
      [
        "storage",
        "00c640e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00453a9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/004539dc.md#insn-00453a9c) · [`00453ab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/004539dc.md#insn-00453ab0) · [`00453a28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/004539dc.md#insn-00453a28)
- 新版 [`00453adc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00453/00453a1c.md#insn-00453adc) · [`00453af0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00453/00453a1c.md#insn-00453af0) · [`00453a68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00453/00453a1c.md#insn-00453a68)

~~~diff
- 00453a9c ["INT_ADD", "register:40f0:8", ["const:453a9c:8", "const:4:8"]]
- 00453a9c ["CALL", null, ["callee:00c581b0:8"]]
+ 00453adc ["INT_ADD", "register:40f0:8", ["const:453adc:8", "const:4:8"]]
+ 00453adc ["CALL", null, ["callee:00c581b0:8"]]
- 00453a9c bytes 91112094
+ 00453adc bytes b5112094
- 00453ab0 ["INT_ADD", "register:40f0:8", ["const:453ab0:8", "const:4:8"]]
- 00453ab0 ["CALL", null, ["callee:00c53d70:8"]]
+ 00453af0 ["INT_ADD", "register:40f0:8", ["const:453af0:8", "const:4:8"]]
+ 00453af0 ["CALL", null, ["callee:00c53d70:8"]]
- 00453ab0 bytes 88002094
+ 00453af0 bytes a0002094
- 00453a28 ["INT_ADD", "register:40f0:8", ["const:453a28:8", "const:4:8"]]
- 00453a28 ["CALL", null, ["callee:00c57f60:8"]]
+ 00453a68 ["INT_ADD", "register:40f0:8", ["const:453a68:8", "const:4:8"]]
+ 00453a68 ["CALL", null, ["callee:00c57f60:8"]]
- 00453a28 bytes 1a112094
+ 00453a68 bytes 3e112094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c6219a2c7f17acf1dfe118ff2e5acea"></a>

### [`00453cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/00453cb0.md) → [`00453cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00453/00453cf0.md) FUN_00453cf0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00873f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00873/00873f40.md) · 呼出先 14件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044b494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b494.md) [`0045084c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/0045084c.md) [`0045982c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/0045982c.md) [`0045bdcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bdcc.md)
- 新版 呼出元 1件 [`00873f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00873/00873f98.md) · 呼出先 14件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0044b4d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b4d4.md) [`0045088c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/0045088c.md) [`0045986c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/0045986c.md) [`0045be0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045be0c.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.77% / 新版 94.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00453d84",
      "incomplete_value": false,
      "site": "00453d8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:b60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00453d44",
      "incomplete_value": false,
      "site": "00453d4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:a90:8"
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00453da0",
      "incomplete_value": false,
      "site": "00453da0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:bb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00453d60",
      "incomplete_value": false,
      "site": "00453d60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
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
      "definition_site": "00453ed4",
      "incomplete_value": true,
      "site": "00453edc",
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
      "definition_site": "00453e94",
      "incomplete_value": true,
      "site": "00453e9c",
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
    "ordinal": 45,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00453d3c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0044b494"
      ]
    ],
    [
      "00453d44",
      "PARAM",
      [
        "storage",
        "002ac60e",
        null,
        "string"
      ]
    ],
    [
      "00453d8c",
      "DATA",
      [
        "storage",
        "00c63a90",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00453d3c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0044b4d4"
      ]
    ],
    [
      "00453d44",
      "PARAM",
      [
        "storage",
        "002ac5b2",
        null,
        "string"
      ]
    ],
    [
      "00453d8c",
      "DATA",
      [
        "storage",
        "00c63b60",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00453cfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/00453cb0.md#insn-00453cfc) · [`00453d0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/00453cb0.md#insn-00453d0c) · [`00453d3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/00453cb0.md#insn-00453d3c)
- 新版 [`00453d3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00453/00453cf0.md#insn-00453d3c) · [`00453d4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00453/00453cf0.md#insn-00453d4c) · [`00453d7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00453/00453cf0.md#insn-00453d7c)

~~~diff
- 00453cfc ["INT_ADD", "register:40f0:8", ["const:453cfc:8", "const:4:8"]]
- 00453cfc ["CALL", null, ["ram:44b494:8"]]
+ 00453d3c ["INT_ADD", "register:40f0:8", ["const:453d3c:8", "const:4:8"]]
+ 00453d3c ["CALL", null, ["ram:44b4d4:8"]]
- 00453cfc bytes e6ddff97
+ 00453d3c bytes e6ddff97
- 00453d0c ["INT_ADD", "register:40f0:8", ["const:453d0c:8", "const:4:8"]]
- 00453d0c ["CALL", null, ["callee:00c58040:8"]]
+ 00453d4c ["INT_ADD", "register:40f0:8", ["const:453d4c:8", "const:4:8"]]
+ 00453d4c ["CALL", null, ["callee:00c58040:8"]]
- 00453d0c bytes 99102094
+ 00453d4c bytes bd102094
- 00453d3c ["INT_ADD", "register:40f0:8", ["const:453d3c:8", "const:4:8"]]
- 00453d3c ["CALL", null, ["callee:00c57f60:8"]]
+ 00453d7c ["INT_ADD", "register:40f0:8", ["const:453d7c:8", "const:4:8"]]
+ 00453d7c ["CALL", null, ["callee:00c57f60:8"]]
- 00453d3c bytes 55102094
+ 00453d7c bytes 79102094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-446dd67b9b144cbdf1a410cffc9870e9"></a>

### [`0045440c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00454/0045440c.md) → [`0045444c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00454/0045444c.md) FUN_0045444c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00881758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881758.md) · 呼出先 15件 [`0044b534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b534.md) [`00460104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/00460104.md) [`00460108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/00460108.md) [`00561064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561064.md) [`005610b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/005610b4.md)
- 新版 呼出元 1件 [`008817b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00881/008817b0.md) · 呼出先 15件 [`0044b574`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b574.md) [`00460144`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00460/00460144.md) [`00460148`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00460/00460148.md) [`005610a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/005610a4.md) [`005610f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/005610f4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.37% / 新版 93.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0045457c",
      "incomplete_value": true,
      "site": "0045458c",
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
                "const:2a5000:8"
              ],
              [
                "leaf",
                "const:30a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045453c",
      "incomplete_value": true,
      "site": "0045454c",
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
                "const:2a5000:8"
              ],
              [
                "leaf",
                "const:366:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00454580",
      "incomplete_value": true,
      "site": "00454590",
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
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00454540",
      "incomplete_value": true,
      "site": "00454550",
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
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 24,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00454584",
      "incomplete_value": true,
      "site": "00454594",
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
                "const:2e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00454544",
      "incomplete_value": true,
      "site": "00454554",
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
                "const:2a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00454484",
      "PARAM",
      [
        "storage",
        "002b8e06",
        null,
        "string"
      ]
    ],
    [
      "004544f4",
      "READ",
      [
        "storage",
        "00c9ac08",
        null,
        "pointer"
      ]
    ],
    [
      "004544f4",
      "PARAM",
      [
        "storage",
        "00ca5ce8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00454484",
      "PARAM",
      [
        "storage",
        "002b8db2",
        null,
        "string"
      ]
    ],
    [
      "004544f4",
      "READ",
      [
        "storage",
        "00c9acd8",
        null,
        "pointer"
      ]
    ],
    [
      "004544f4",
      "PARAM",
      [
        "storage",
        "00ca5de8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045444c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00454/0045440c.md#insn-0045444c) · [`004544bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00454/0045440c.md#insn-004544bc) · [`00454570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00454/0045440c.md#insn-00454570)
- 新版 [`0045448c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00454/0045444c.md#insn-0045448c) · [`004544fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00454/0045444c.md#insn-004544fc) · [`004545b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00454/0045444c.md#insn-004545b0)

~~~diff
- 0045444c ["INT_ADD", "register:40f0:8", ["const:45444c:8", "const:4:8"]]
- 0045444c ["CALL", null, ["callee:00c58040:8"]]
+ 0045448c ["INT_ADD", "register:40f0:8", ["const:45448c:8", "const:4:8"]]
+ 0045448c ["CALL", null, ["callee:00c58040:8"]]
- 0045444c bytes c90e2094
+ 0045448c bytes ed0e2094
- 004544bc ["INT_ADD", "register:40f0:8", ["const:4544bc:8", "const:4:8"]]
- 004544bc ["CALL", null, ["callee:00561d74:8"]]
+ 004544fc ["INT_ADD", "register:40f0:8", ["const:4544fc:8", "const:4:8"]]
+ 004544fc ["CALL", null, ["callee:00561d74:8"]]
- 004544bc bytes 1e360494
+ 004544fc bytes 1e360494
- 00454570 ["INT_ADD", "register:40f0:8", ["const:454570:8", "const:4:8"]]
- 00454570 ["CALL", null, ["callee:005610a4:8"]]
+ 004545b0 ["INT_ADD", "register:40f0:8", ["const:4545b0:8", "const:4:8"]]
+ 004545b0 ["CALL", null, ["callee:005610a4:8"]]
- 00454570 bytes bd320494
+ 004545b0 bytes bd320494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb5d1ec27618d0e932499e2d7126ad6b"></a>

### [`00454844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00454/00454844.md) → [`00454884`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00454/00454884.md) FUN_00454884

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009bd7ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009bd/009bd7ec.md) · 呼出先 9件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044b700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b700.md) [`004509b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/004509b0.md) [`00460740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/00460740.md) [`00462204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462204.md)
- 新版 呼出元 1件 [`009bd840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009bd/009bd840.md) · 呼出先 9件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0044b740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b740.md) [`004509f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/004509f0.md) [`00460780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00460/00460780.md) [`00462244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462244.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.25% / 新版 97.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004549c4",
      "incomplete_value": false,
      "site": "004549c4",
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
            "const:2e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00454984",
      "incomplete_value": false,
      "site": "00454984",
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
            "const:218:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00454a64",
      "incomplete_value": false,
      "site": "00454a64",
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
            "const:368:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00454a24",
      "incomplete_value": false,
      "site": "00454a24",
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
            "const:298:8"
          ]
        ]
      ]
    },
    "ordinal": 36,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004548c4",
      "incomplete_value": false,
      "site": "004548cc",
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
            "const:fad:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00454884",
      "incomplete_value": false,
      "site": "0045488c",
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
            "const:1:8"
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
      "004548c4",
      "PARAM",
      [
        "storage",
        "002ba001",
        null,
        "string"
      ]
    ],
    [
      "004549c4",
      "DATA",
      [
        "storage",
        "00c64218",
        null,
        "undefined *"
      ]
    ],
    [
      "00454a64",
      "DATA",
      [
        "storage",
        "00c64298",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004548c4",
      "PARAM",
      [
        "storage",
        "002b9fad",
        null,
        "string"
      ]
    ],
    [
      "004549c4",
      "DATA",
      [
        "storage",
        "00c642e8",
        null,
        "undefined *"
      ]
    ],
    [
      "00454a64",
      "DATA",
      [
        "storage",
        "00c64368",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045488c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00454/00454844.md#insn-0045488c) · [`00454a88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00454/00454844.md#insn-00454a88) · [`0045487c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00454/00454844.md#insn-0045487c)
- 新版 [`004548cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00454/00454884.md#insn-004548cc) · [`00454ac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00454/00454884.md#insn-00454ac8) · [`004548bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00454/00454884.md#insn-004548bc)

~~~diff
- 0045488c ["INT_ADD", "register:40f0:8", ["const:45488c:8", "const:4:8"]]
- 0045488c ["CALL", null, ["callee:00c58040:8"]]
+ 004548cc ["INT_ADD", "register:40f0:8", ["const:4548cc:8", "const:4:8"]]
+ 004548cc ["CALL", null, ["callee:00c58040:8"]]
- 0045488c bytes b90d2094
+ 004548cc bytes dd0d2094
- 00454a88 ["INT_ADD", "register:40f0:8", ["const:454a88:8", "const:4:8"]]
- 00454a88 ["CALL", null, ["callee:004509f0:8"]]
+ 00454ac8 ["INT_ADD", "register:40f0:8", ["const:454ac8:8", "const:4:8"]]
+ 00454ac8 ["CALL", null, ["callee:004509f0:8"]]
- 00454a88 bytes caefff97
+ 00454ac8 bytes caefff97
- 0045487c ["INT_ADD", "register:40f0:8", ["const:45487c:8", "const:4:8"]]
- 0045487c ["CALL", null, ["callee:0044b740:8"]]
+ 004548bc ["INT_ADD", "register:40f0:8", ["const:4548bc:8", "const:4:8"]]
+ 004548bc ["CALL", null, ["callee:0044b740:8"]]
- 0045487c bytes a1dbff97
+ 004548bc bytes a1dbff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce46ac29b02383ad1a545812c49c0a8b"></a>

### [`00454d28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00454/00454d28.md) → [`00454d68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00454/00454d68.md) FUN_00454d68

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009ba95c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ba/009ba95c.md) · 呼出先 10件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044b700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b700.md) [`004509b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/004509b0.md) [`00462594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462594.md) [`00462854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462854.md)
- 新版 呼出元 1件 [`009ba9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ba/009ba9b0.md) · 呼出先 10件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0044b740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b740.md) [`004509f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/004509f0.md) [`004625d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/004625d4.md) [`00462894`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462894.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.27% / 新版 97.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00454f40",
      "incomplete_value": false,
      "site": "00454f40",
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
            "const:3e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00454f00",
      "incomplete_value": false,
      "site": "00454f00",
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
            "const:318:8"
          ]
        ]
      ]
    },
    "ordinal": 39,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00454fe0",
      "incomplete_value": false,
      "site": "00454fe0",
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
            "const:468:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00454fa0",
      "incomplete_value": false,
      "site": "00454fa0",
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
            "const:398:8"
          ]
        ]
      ]
    },
    "ordinal": 46,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00454dac",
      "incomplete_value": false,
      "site": "00454db4",
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
            "const:5d4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00454d6c",
      "incomplete_value": false,
      "site": "00454d74",
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
            "const:630:8"
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
      "00454dac",
      "PARAM",
      [
        "storage",
        "002ad630",
        null,
        "string"
      ]
    ],
    [
      "00454e0c",
      "PARAM",
      [
        "storage",
        "002a3f62",
        null,
        "string"
      ]
    ],
    [
      "00454f40",
      "DATA",
      [
        "storage",
        "00c64318",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00454dac",
      "PARAM",
      [
        "storage",
        "002ad5d4",
        null,
        "string"
      ]
    ],
    [
      "00454e0c",
      "PARAM",
      [
        "storage",
        "002a3f15",
        null,
        "string"
      ]
    ],
    [
      "00454f40",
      "DATA",
      [
        "storage",
        "00c643e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00454d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00454/00454d28.md#insn-00454d74) · [`00454dd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00454/00454d28.md#insn-00454dd4) · [`00455004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00454/00454d28.md#insn-00455004)
- 新版 [`00454db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00454/00454d68.md#insn-00454db4) · [`00454e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00454/00454d68.md#insn-00454e14) · [`00455044`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00454/00454d68.md#insn-00455044)

~~~diff
- 00454d74 ["INT_ADD", "register:40f0:8", ["const:454d74:8", "const:4:8"]]
- 00454d74 ["CALL", null, ["callee:00c58040:8"]]
+ 00454db4 ["INT_ADD", "register:40f0:8", ["const:454db4:8", "const:4:8"]]
+ 00454db4 ["CALL", null, ["callee:00c58040:8"]]
- 00454d74 bytes 7f0c2094
+ 00454db4 bytes a30c2094
- 00454dd4 ["INT_ADD", "register:40f0:8", ["const:454dd4:8", "const:4:8"]]
- 00454dd4 ["CALL", null, ["callee:00c58040:8"]]
+ 00454e14 ["INT_ADD", "register:40f0:8", ["const:454e14:8", "const:4:8"]]
+ 00454e14 ["CALL", null, ["callee:00c58040:8"]]
- 00454dd4 bytes 670c2094
+ 00454e14 bytes 8b0c2094
- 00455004 ["INT_ADD", "register:40f0:8", ["const:455004:8", "const:4:8"]]
- 00455004 ["CALL", null, ["callee:004509f0:8"]]
+ 00455044 ["INT_ADD", "register:40f0:8", ["const:455044:8", "const:4:8"]]
+ 00455044 ["CALL", null, ["callee:004509f0:8"]]
- 00455004 bytes 6beeff97
+ 00455044 bytes 6beeff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8af778c623b5d140a197171cccfd36c4"></a>

### [`004552f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00455/004552f8.md) → [`00455338`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00455/00455338.md) FUN_00455338

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00a8a418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a8a/00a8a418.md) [`00a9a804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a9a/00a9a804.md) · 呼出先 9件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044b700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b700.md) [`004509b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/004509b0.md) [`00462b14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462b14.md) [`00462f90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462f90.md)
- 新版 呼出元 2件 [`00a8a488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a8a/00a8a488.md) [`00a9a874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a9a/00a9a874.md) · 呼出先 9件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0044b740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b740.md) [`004509f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/004509f0.md) [`00462b54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462b54.md) [`00462fd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462fd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.25% / 新版 97.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00455478",
      "incomplete_value": false,
      "site": "00455478",
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
            "const:4e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00455438",
      "incomplete_value": false,
      "site": "00455438",
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
            "const:418:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00455518",
      "incomplete_value": false,
      "site": "00455518",
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
            "const:568:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004554d8",
      "incomplete_value": false,
      "site": "004554d8",
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
            "const:498:8"
          ]
        ]
      ]
    },
    "ordinal": 36,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00455378",
      "incomplete_value": false,
      "site": "00455380",
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
            "const:5e2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00455338",
      "incomplete_value": false,
      "site": "00455340",
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
            "const:63e:8"
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
      "00455378",
      "PARAM",
      [
        "storage",
        "002ad63e",
        null,
        "string"
      ]
    ],
    [
      "00455478",
      "DATA",
      [
        "storage",
        "00c64418",
        null,
        "undefined *"
      ]
    ],
    [
      "00455518",
      "DATA",
      [
        "storage",
        "00c64498",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00455378",
      "PARAM",
      [
        "storage",
        "002ad5e2",
        null,
        "string"
      ]
    ],
    [
      "00455478",
      "DATA",
      [
        "storage",
        "00c644e8",
        null,
        "undefined *"
      ]
    ],
    [
      "00455518",
      "DATA",
      [
        "storage",
        "00c64568",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00455340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00455/004552f8.md#insn-00455340) · [`0045553c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00455/004552f8.md#insn-0045553c) · [`00455330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00455/004552f8.md#insn-00455330)
- 新版 [`00455380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00455/00455338.md#insn-00455380) · [`0045557c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00455/00455338.md#insn-0045557c) · [`00455370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00455/00455338.md#insn-00455370)

~~~diff
- 00455340 ["INT_ADD", "register:40f0:8", ["const:455340:8", "const:4:8"]]
- 00455340 ["CALL", null, ["callee:00c58040:8"]]
+ 00455380 ["INT_ADD", "register:40f0:8", ["const:455380:8", "const:4:8"]]
+ 00455380 ["CALL", null, ["callee:00c58040:8"]]
- 00455340 bytes 0c0b2094
+ 00455380 bytes 300b2094
- 0045553c ["INT_ADD", "register:40f0:8", ["const:45553c:8", "const:4:8"]]
- 0045553c ["CALL", null, ["callee:004509f0:8"]]
+ 0045557c ["INT_ADD", "register:40f0:8", ["const:45557c:8", "const:4:8"]]
+ 0045557c ["CALL", null, ["callee:004509f0:8"]]
- 0045553c bytes 1dedff97
+ 0045557c bytes 1dedff97
- 00455330 ["INT_ADD", "register:40f0:8", ["const:455330:8", "const:4:8"]]
- 00455330 ["CALL", null, ["callee:0044b740:8"]]
+ 00455370 ["INT_ADD", "register:40f0:8", ["const:455370:8", "const:4:8"]]
+ 00455370 ["CALL", null, ["callee:0044b740:8"]]
- 00455330 bytes f4d8ff97
+ 00455370 bytes f4d8ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52a8e700cea55a2a2a6d738e94b0e3e1"></a>

### [`004557dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00455/004557dc.md) → [`0045581c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00455/0045581c.md) FUN_0045581c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00886200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886200.md) · 呼出先 12件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044b3f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b3f4.md) [`004509b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/004509b0.md) [`0045bdcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bdcc.md) [`00463258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463258.md)
- 新版 呼出元 1件 [`00886258`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886258.md) · 呼出先 12件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0044b434`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b434.md) [`004509f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/004509f0.md) [`0045be0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045be0c.md) [`00463298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00463/00463298.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004558a8",
      "incomplete_value": false,
      "site": "004558b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:b60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00455868",
      "incomplete_value": false,
      "site": "00455870",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:a90:8"
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004558cc",
      "incomplete_value": false,
      "site": "004558cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:bb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045588c",
      "incomplete_value": false,
      "site": "0045588c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004559b0",
      "incomplete_value": false,
      "site": "004559b0",
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
            "const:5e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00455970",
      "incomplete_value": false,
      "site": "00455970",
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
            "const:518:8"
          ]
        ]
      ]
    },
    "ordinal": 39,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00455860",
      "PARAM",
      [
        "storage",
        "002ab2ec",
        null,
        "string"
      ]
    ],
    [
      "004558b0",
      "DATA",
      [
        "storage",
        "00c63a90",
        null,
        "pointer"
      ]
    ],
    [
      "004558cc",
      "DATA",
      [
        "storage",
        "00c63ae0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00455860",
      "PARAM",
      [
        "storage",
        "002ab290",
        null,
        "string"
      ]
    ],
    [
      "004558b0",
      "DATA",
      [
        "storage",
        "00c63b60",
        null,
        "pointer"
      ]
    ],
    [
      "004558cc",
      "DATA",
      [
        "storage",
        "00c63bb0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00455828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00455/004557dc.md#insn-00455828) · [`00455868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00455/004557dc.md#insn-00455868) · [`00455a74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00455/004557dc.md#insn-00455a74)
- 新版 [`00455868`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00455/0045581c.md#insn-00455868) · [`004558a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00455/0045581c.md#insn-004558a8) · [`00455ab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00455/0045581c.md#insn-00455ab4)

~~~diff
- 00455828 ["INT_ADD", "register:40f0:8", ["const:455828:8", "const:4:8"]]
- 00455828 ["CALL", null, ["callee:00c58040:8"]]
+ 00455868 ["INT_ADD", "register:40f0:8", ["const:455868:8", "const:4:8"]]
+ 00455868 ["CALL", null, ["callee:00c58040:8"]]
- 00455828 bytes d2092094
+ 00455868 bytes f6092094
- 00455868 ["COPY", "tmp:0:8", ["const:a90:8"]]
- 00455868 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00455868 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00455868 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004558a8 ["COPY", "tmp:0:8", ["const:b60:8"]]
+ 004558a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004558a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004558a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00455868 bytes 08412a91
+ 004558a8 bytes 08812d91
- 00455a74 ["INT_ADD", "register:40f0:8", ["const:455a74:8", "const:4:8"]]
- 00455a74 ["CALL", null, ["callee:004509f0:8"]]
+ 00455ab4 ["INT_ADD", "register:40f0:8", ["const:455ab4:8", "const:4:8"]]
+ 00455ab4 ["CALL", null, ["callee:004509f0:8"]]
- 00455a74 bytes cfebff97
+ 00455ab4 bytes cfebff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b6b0ab0278b9406d4a58915d487bc86"></a>

### [`00455d58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00455/00455d58.md) → [`00455d98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00455/00455d98.md) FUN_00455d98

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0089bc8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089b/0089bc8c.md) · 呼出先 13件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044b3f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b3f4.md) [`004509b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/004509b0.md) [`0045179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/0045179c.md) [`0045bdcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bdcc.md)
- 新版 呼出元 1件 [`0089bce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089b/0089bce4.md) · 呼出先 13件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0044b434`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b434.md) [`004509f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/004509f0.md) [`004517dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/004517dc.md) [`0045be0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045be0c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.78% / 新版 94.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00455e28",
      "incomplete_value": false,
      "site": "00455e30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:b60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00455de8",
      "incomplete_value": false,
      "site": "00455df0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:a90:8"
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00455e50",
      "incomplete_value": false,
      "site": "00455e50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:bb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00455e10",
      "incomplete_value": false,
      "site": "00455e10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
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
      "definition_site": "00455e88",
      "incomplete_value": true,
      "site": "00455e88",
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
                "const:2a0000:8"
              ],
              [
                "leaf",
                "const:f4e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00455e48",
      "incomplete_value": true,
      "site": "00455e48",
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
                "const:2a0000:8"
              ],
              [
                "leaf",
                "const:f9b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 30,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00455de0",
      "PARAM",
      [
        "storage",
        "002b4ba1",
        null,
        "string"
      ]
    ],
    [
      "00455e30",
      "DATA",
      [
        "storage",
        "00c63a90",
        null,
        "pointer"
      ]
    ],
    [
      "00455e50",
      "DATA",
      [
        "storage",
        "00c63ae0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00455de0",
      "PARAM",
      [
        "storage",
        "002b4bd2",
        null,
        "string"
      ]
    ],
    [
      "00455e30",
      "DATA",
      [
        "storage",
        "00c63b60",
        null,
        "pointer"
      ]
    ],
    [
      "00455e50",
      "DATA",
      [
        "storage",
        "00c63bb0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00455da8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00455/00455d58.md#insn-00455da8) · [`00455de8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00455/00455d58.md#insn-00455de8) · [`00456030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00455/00455d58.md#insn-00456030)
- 新版 [`00455de8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00455/00455d98.md#insn-00455de8) · [`00455e28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00455/00455d98.md#insn-00455e28) · [`00456070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00455/00455d98.md#insn-00456070)

~~~diff
- 00455da8 ["INT_ADD", "register:40f0:8", ["const:455da8:8", "const:4:8"]]
- 00455da8 ["CALL", null, ["callee:00c58040:8"]]
+ 00455de8 ["INT_ADD", "register:40f0:8", ["const:455de8:8", "const:4:8"]]
+ 00455de8 ["CALL", null, ["callee:00c58040:8"]]
- 00455da8 bytes 72082094
+ 00455de8 bytes 96082094
- 00455de8 ["COPY", "tmp:0:8", ["const:a90:8"]]
- 00455de8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00455de8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00455de8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00455e28 ["COPY", "tmp:0:8", ["const:b60:8"]]
+ 00455e28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00455e28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00455e28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00455de8 bytes 08412a91
+ 00455e28 bytes 08812d91
- 00456030 ["INT_ADD", "register:40f0:8", ["const:456030:8", "const:4:8"]]
- 00456030 ["CALL", null, ["callee:004509f0:8"]]
+ 00456070 ["INT_ADD", "register:40f0:8", ["const:456070:8", "const:4:8"]]
+ 00456070 ["CALL", null, ["callee:004509f0:8"]]
- 00456030 bytes 60eaff97
+ 00456070 bytes 60eaff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-325f222efeb7078d63b5b49f5186e12c"></a>

### [`00456324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00456/00456324.md) → [`00456364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00456/00456364.md) FUN_00456364

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) [`00881758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00881/00881758.md) · 呼出先 9件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044b4e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b4e4.md) [`004509b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/004509b0.md) [`00463fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463fd8.md) [`00464cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464cdc.md)
- 新版 呼出元 2件 [`00856e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856e84.md) [`008817b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00881/008817b0.md) · 呼出先 9件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0044b524`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b524.md) [`004509f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/004509f0.md) [`00464018`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00464/00464018.md) [`00464d1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00464/00464d1c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.25% / 新版 97.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004564a4",
      "incomplete_value": false,
      "site": "004564a4",
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
            "const:7e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00456464",
      "incomplete_value": false,
      "site": "00456464",
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
            "const:718:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00456544",
      "incomplete_value": false,
      "site": "00456544",
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
            "const:868:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00456504",
      "incomplete_value": false,
      "site": "00456504",
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
            "const:798:8"
          ]
        ]
      ]
    },
    "ordinal": 36,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004563a4",
      "incomplete_value": false,
      "site": "004563ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ac000:8"
          ],
          [
            "leaf",
            "const:5c4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00456364",
      "incomplete_value": false,
      "site": "0045636c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ac000:8"
          ],
          [
            "leaf",
            "const:620:8"
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
      "004563a4",
      "PARAM",
      [
        "storage",
        "002ac620",
        null,
        "string"
      ]
    ],
    [
      "004564a4",
      "DATA",
      [
        "storage",
        "00c64718",
        null,
        "undefined *"
      ]
    ],
    [
      "00456544",
      "DATA",
      [
        "storage",
        "00c64798",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004563a4",
      "PARAM",
      [
        "storage",
        "002ac5c4",
        null,
        "string"
      ]
    ],
    [
      "004564a4",
      "DATA",
      [
        "storage",
        "00c647e8",
        null,
        "undefined *"
      ]
    ],
    [
      "00456544",
      "DATA",
      [
        "storage",
        "00c64868",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045636c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00456/00456324.md#insn-0045636c) · [`00456568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00456/00456324.md#insn-00456568) · [`0045635c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00456/00456324.md#insn-0045635c)
- 新版 [`004563ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00456/00456364.md#insn-004563ac) · [`004565a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00456/00456364.md#insn-004565a8) · [`0045639c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00456/00456364.md#insn-0045639c)

~~~diff
- 0045636c ["INT_ADD", "register:40f0:8", ["const:45636c:8", "const:4:8"]]
- 0045636c ["CALL", null, ["callee:00c58040:8"]]
+ 004563ac ["INT_ADD", "register:40f0:8", ["const:4563ac:8", "const:4:8"]]
+ 004563ac ["CALL", null, ["callee:00c58040:8"]]
- 0045636c bytes 01072094
+ 004563ac bytes 25072094
- 00456568 ["INT_ADD", "register:40f0:8", ["const:456568:8", "const:4:8"]]
- 00456568 ["CALL", null, ["callee:004509f0:8"]]
+ 004565a8 ["INT_ADD", "register:40f0:8", ["const:4565a8:8", "const:4:8"]]
+ 004565a8 ["CALL", null, ["callee:004509f0:8"]]
- 00456568 bytes 12e9ff97
+ 004565a8 bytes 12e9ff97
- 0045635c ["INT_ADD", "register:40f0:8", ["const:45635c:8", "const:4:8"]]
- 0045635c ["CALL", null, ["callee:0044b524:8"]]
+ 0045639c ["INT_ADD", "register:40f0:8", ["const:45639c:8", "const:4:8"]]
+ 0045639c ["CALL", null, ["callee:0044b524:8"]]
- 0045635c bytes 62d4ff97
+ 0045639c bytes 62d4ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5cb3ecfc04c7ecc9e1912b7148cdefb6"></a>

### [`00456808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00456/00456808.md) → [`00456848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00456/00456848.md) FUN_00456848

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0086d71c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086d/0086d71c.md) [`00886aa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886aa4.md) · 呼出先 11件 [`00464fe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464fe4.md) [`00561014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561014.md) [`00561064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561064.md) [`005610b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/005610b4.md) [`005618a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/005618a8.md)
- 新版 呼出元 2件 [`0086d774`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086d/0086d774.md) [`00886afc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886afc.md) · 呼出先 11件 [`00465024`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00465/00465024.md) [`00561054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/00561054.md) [`005610a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/005610a4.md) [`005610f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/005610f4.md) [`005618e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/005618e8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.13% / 新版 91.13%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004568d4",
      "incomplete_value": true,
      "site": "004568d4",
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
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:fee:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00456894",
      "incomplete_value": true,
      "site": "00456894",
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
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:fae:8"
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
      "definition_site": "004569a0",
      "incomplete_value": true,
      "site": "004569a0",
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
                "const:2a8000:8"
              ],
              [
                "leaf",
                "const:a58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00456960",
      "incomplete_value": true,
      "site": "00456960",
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
                "const:2a8000:8"
              ],
              [
                "leaf",
                "const:ab4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004569a4",
      "incomplete_value": true,
      "site": "004569a4",
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
      "definition_site": "00456964",
      "incomplete_value": true,
      "site": "00456964",
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
      "00456884",
      "READ",
      [
        "storage",
        "00c9ac08",
        null,
        "pointer"
      ]
    ],
    [
      "00456884",
      "PARAM",
      [
        "storage",
        "00ca5ce8",
        null,
        "undefined1"
      ]
    ],
    [
      "004568b0",
      "DATA",
      [
        "storage",
        "0079656b",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00456884",
      "READ",
      [
        "storage",
        "00c9acd8",
        null,
        "pointer"
      ]
    ],
    [
      "00456884",
      "PARAM",
      [
        "storage",
        "00ca5de8",
        null,
        "undefined1"
      ]
    ],
    [
      "004568bc",
      "READ",
      [
        "storage",
        "002b7fee",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045684c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00456/00456808.md#insn-0045684c) · [`00456854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00456/00456808.md#insn-00456854) · [`00456920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00456/00456808.md#insn-00456920)
- 新版 [`0045688c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00456/00456848.md#insn-0045688c) · [`00456894`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00456/00456848.md#insn-00456894) · [`00456960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00456/00456848.md#insn-00456960)

~~~diff
- 0045684c ["INT_ADD", "register:40f0:8", ["const:45684c:8", "const:4:8"]]
- 0045684c ["CALL", null, ["callee:00561d74:8"]]
+ 0045688c ["INT_ADD", "register:40f0:8", ["const:45688c:8", "const:4:8"]]
+ 0045688c ["CALL", null, ["callee:00561d74:8"]]
- 0045684c bytes 3a2d0494
+ 0045688c bytes 3a2d0494
- 00456854 ["INT_ADD", "register:40f0:8", ["const:456854:8", "const:4:8"]]
- 00456854 ["CALL", null, ["callee:005618e8:8"]]
+ 00456894 ["INT_ADD", "register:40f0:8", ["const:456894:8", "const:4:8"]]
+ 00456894 ["CALL", null, ["callee:005618e8:8"]]
- 00456854 bytes 152c0494
+ 00456894 bytes 152c0494
- 00456920 ["INT_ADD", "register:40f0:8", ["const:456920:8", "const:4:8"]]
- 00456920 ["CALL", null, ["callee:00c57f80:8"]]
+ 00456960 ["INT_ADD", "register:40f0:8", ["const:456960:8", "const:4:8"]]
+ 00456960 ["CALL", null, ["callee:00c57f80:8"]]
- 00456920 bytes 64052094
+ 00456960 bytes 88052094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cfceefa9040ef05886023fc582edc6ea"></a>

### [`00456efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00456/00456efc.md) → [`00456f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00456/00456f3c.md) FUN_00456f3c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 22件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044b4e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b4e4.md) [`004509b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/004509b0.md) [`0045179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/0045179c.md) [`004518b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004518b0.md)
- 新版 呼出元 1件 [`00856e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856e84.md) · 呼出先 22件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0044b524`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b524.md) [`004509f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/004509f0.md) [`004517dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/004517dc.md) [`004518f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/004518f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 94.47% / 新版 94.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 1件, `store_value` 5件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00457120",
      "incomplete_value": false,
      "site": "00457120",
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
            "const:968:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004570e0",
      "incomplete_value": false,
      "site": "004570e0",
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
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 34,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00457124",
      "incomplete_value": false,
      "site": "00457124",
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
            "const:9e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004570e4",
      "incomplete_value": false,
      "site": "004570e4",
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
            "const:918:8"
          ]
        ]
      ]
    },
    "ordinal": 35,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00457210",
      "incomplete_value": true,
      "site": "00457218",
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
      "definition_site": "004571d0",
      "incomplete_value": true,
      "site": "004571d8",
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
    "ordinal": 37,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00456f84",
      "PARAM",
      [
        "storage",
        "002b098e",
        null,
        "string"
      ]
    ],
    [
      "00457120",
      "DATA",
      [
        "storage",
        "00c64898",
        null,
        "undefined *"
      ]
    ],
    [
      "00457124",
      "DATA",
      [
        "storage",
        "00c64918",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00456f84",
      "PARAM",
      [
        "storage",
        "002b0932",
        null,
        "string"
      ]
    ],
    [
      "00457120",
      "DATA",
      [
        "storage",
        "00c64968",
        null,
        "undefined *"
      ]
    ],
    [
      "00457124",
      "DATA",
      [
        "storage",
        "00c649e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00456f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00456/00456efc.md#insn-00456f4c) · [`00456f8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00456/00456efc.md#insn-00456f8c) · [`0045710c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00456/00456efc.md#insn-0045710c)
- 新版 [`00456f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00456/00456f3c.md#insn-00456f8c) · [`00456fcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00456/00456f3c.md#insn-00456fcc) · [`0045714c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00456/00456f3c.md#insn-0045714c)

~~~diff
- 00456f4c ["INT_ADD", "register:40f0:8", ["const:456f4c:8", "const:4:8"]]
- 00456f4c ["CALL", null, ["callee:00c58040:8"]]
+ 00456f8c ["INT_ADD", "register:40f0:8", ["const:456f8c:8", "const:4:8"]]
+ 00456f8c ["CALL", null, ["callee:00c58040:8"]]
- 00456f4c bytes 09042094
+ 00456f8c bytes 2d042094
- 00456f8c ["INT_ADD", "register:40f0:8", ["const:456f8c:8", "const:4:8"]]
- 00456f8c ["CALL", null, ["callee:00560494:8"]]
+ 00456fcc ["INT_ADD", "register:40f0:8", ["const:456fcc:8", "const:4:8"]]
+ 00456fcc ["CALL", null, ["callee:00560494:8"]]
- 00456f8c bytes 32250494
+ 00456fcc bytes 32250494
- 0045710c ["INT_ADD", "register:40f0:8", ["const:45710c:8", "const:4:8"]]
- 0045710c ["CALL", null, ["callee:004509f0:8"]]
+ 0045714c ["INT_ADD", "register:40f0:8", ["const:45714c:8", "const:4:8"]]
+ 0045714c ["CALL", null, ["callee:004509f0:8"]]
- 0045710c bytes 29e6ff97
+ 0045714c bytes 29e6ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83560d973d7b7b7607efcc669574d1be"></a>

### [`00457400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00457/00457400.md) → [`00457440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00457/00457440.md) FUN_00457440

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00886f44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886f44.md) · 呼出先 20件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044b4e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b4e4.md) [`004509b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/004509b0.md) [`0045179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/0045179c.md) [`004518b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004518b0.md)
- 新版 呼出元 1件 [`00886f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00886/00886f9c.md) · 呼出先 20件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0044b524`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b524.md) [`004509f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/004509f0.md) [`004517dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/004517dc.md) [`004518f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/004518f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 93.87% / 新版 93.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 1件, `store_value` 5件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004575f8",
      "incomplete_value": false,
      "site": "004575f8",
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
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004575b8",
      "incomplete_value": false,
      "site": "004575b8",
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
            "const:998:8"
          ]
        ]
      ]
    },
    "ordinal": 34,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004575fc",
      "incomplete_value": false,
      "site": "004575fc",
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
            "const:ae8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004575bc",
      "incomplete_value": false,
      "site": "004575bc",
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
            "const:a18:8"
          ]
        ]
      ]
    },
    "ordinal": 35,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004576b8",
      "incomplete_value": true,
      "site": "004576c0",
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
      "definition_site": "00457678",
      "incomplete_value": true,
      "site": "00457680",
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
    "ordinal": 37,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00457488",
      "PARAM",
      [
        "storage",
        "002a7670",
        null,
        "string"
      ]
    ],
    [
      "004575f8",
      "DATA",
      [
        "storage",
        "00c64998",
        null,
        "undefined *"
      ]
    ],
    [
      "004575fc",
      "DATA",
      [
        "storage",
        "00c64a18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00457488",
      "PARAM",
      [
        "storage",
        "002a7614",
        null,
        "string"
      ]
    ],
    [
      "004575f8",
      "DATA",
      [
        "storage",
        "00c64a68",
        null,
        "undefined *"
      ]
    ],
    [
      "004575fc",
      "DATA",
      [
        "storage",
        "00c64ae8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00457450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00457/00457400.md#insn-00457450) · [`00457490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00457/00457400.md#insn-00457490) · [`004575e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00457/00457400.md#insn-004575e4)
- 新版 [`00457490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00457/00457440.md#insn-00457490) · [`004574d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00457/00457440.md#insn-004574d0) · [`00457624`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00457/00457440.md#insn-00457624)

~~~diff
- 00457450 ["INT_ADD", "register:40f0:8", ["const:457450:8", "const:4:8"]]
- 00457450 ["CALL", null, ["callee:00c58040:8"]]
+ 00457490 ["INT_ADD", "register:40f0:8", ["const:457490:8", "const:4:8"]]
+ 00457490 ["CALL", null, ["callee:00c58040:8"]]
- 00457450 bytes c8022094
+ 00457490 bytes ec022094
- 00457490 ["INT_ADD", "register:40f0:8", ["const:457490:8", "const:4:8"]]
- 00457490 ["CALL", null, ["callee:00560494:8"]]
+ 004574d0 ["INT_ADD", "register:40f0:8", ["const:4574d0:8", "const:4:8"]]
+ 004574d0 ["CALL", null, ["callee:00560494:8"]]
- 00457490 bytes f1230494
+ 004574d0 bytes f1230494
- 004575e4 ["INT_ADD", "register:40f0:8", ["const:4575e4:8", "const:4:8"]]
- 004575e4 ["CALL", null, ["callee:004509f0:8"]]
+ 00457624 ["INT_ADD", "register:40f0:8", ["const:457624:8", "const:4:8"]]
+ 00457624 ["CALL", null, ["callee:004509f0:8"]]
- 004575e4 bytes f3e4ff97
+ 00457624 bytes f3e4ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac167731ab66fa8d45a1085c4c0a059b"></a>

### [`00457878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00457/00457878.md) → [`004578b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00457/004578b8.md) FUN_004578b8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00893dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/00893dbc.md) · 呼出先 25件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044b4e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b4e4.md) [`0045179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/0045179c.md) [`004518b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004518b0.md) [`004519d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004519d8.md)
- 新版 呼出元 1件 [`00893e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/00893e14.md) · 呼出先 25件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0044b524`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b524.md) [`004517dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/004517dc.md) [`004518f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/004518f0.md) [`00451a18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/00451a18.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 1件, `store_value` 11件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00457910",
      "incomplete_value": false,
      "site": "00457918",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:b60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004578d0",
      "incomplete_value": false,
      "site": "004578d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:a90:8"
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
      "definition_site": "00457924",
      "incomplete_value": false,
      "site": "00457924",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:bb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004578e4",
      "incomplete_value": false,
      "site": "004578e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
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
      "definition_site": "004579dc",
      "incomplete_value": true,
      "site": "004579dc",
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
                "const:2a8000:8"
              ],
              [
                "leaf",
                "const:a4d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045799c",
      "incomplete_value": true,
      "site": "0045799c",
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
                "const:2a8000:8"
              ],
              [
                "leaf",
                "const:aa9:8"
              ]
            ]
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
      "00457918",
      "DATA",
      [
        "storage",
        "00c63a90",
        null,
        "pointer"
      ]
    ],
    [
      "00457924",
      "DATA",
      [
        "storage",
        "00c63ae0",
        null,
        "pointer"
      ]
    ],
    [
      "004579cc",
      "READ",
      [
        "storage",
        "002a8aa9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00457918",
      "DATA",
      [
        "storage",
        "00c63b60",
        null,
        "pointer"
      ]
    ],
    [
      "00457924",
      "DATA",
      [
        "storage",
        "00c63bb0",
        null,
        "pointer"
      ]
    ],
    [
      "004579cc",
      "READ",
      [
        "storage",
        "002a8a4d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004579dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00457/00457878.md#insn-004579dc) · [`00457a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00457/00457878.md#insn-00457a60) · [`00457ac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00457/00457878.md#insn-00457ac0)
- 新版 [`00457a1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00457/004578b8.md#insn-00457a1c) · [`00457aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00457/004578b8.md#insn-00457aa0) · [`00457b00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00457/004578b8.md#insn-00457b00)

~~~diff
- 004579dc ["COPY", "register:0:8", ["register:4040:8"]]
- 004579dc ["INT_ADD", "register:40f0:8", ["const:4579dc:8", "const:4:8"]]
- 004579dc ["CALLIND", null, ["register:0:8"]]
+ 00457a1c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00457a1c ["INT_ADD", "register:40f0:8", ["const:457a1c:8", "const:4:8"]]
+ 00457a1c ["CALLIND", null, ["register:0:8"]]
- 004579dc bytes 00013fd6
+ 00457a1c bytes 00013fd6
- 00457a60 ["INT_ADD", "register:40f0:8", ["const:457a60:8", "const:4:8"]]
- 00457a60 ["CALL", null, ["callee:00c58040:8"]]
+ 00457aa0 ["INT_ADD", "register:40f0:8", ["const:457aa0:8", "const:4:8"]]
+ 00457aa0 ["CALL", null, ["callee:00c58040:8"]]
- 00457a60 bytes 44012094
+ 00457aa0 bytes 68012094
- 00457ac0 ["INT_ADD", "register:40f0:8", ["const:457ac0:8", "const:4:8"]]
- 00457ac0 ["CALL", null, ["callee:00c58040:8"]]
+ 00457b00 ["INT_ADD", "register:40f0:8", ["const:457b00:8", "const:4:8"]]
+ 00457b00 ["CALL", null, ["callee:00c58040:8"]]
- 00457ac0 bytes 2c012094
+ 00457b00 bytes 50012094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37d85948080e023a92dd8faabe4e982e"></a>

### [`00458230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/00458230.md) → [`00458270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00458/00458270.md) FUN_00458270

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0087f368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f368.md) · 呼出先 18件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044b4e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b4e4.md) [`004509b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/004509b0.md) [`0045179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/0045179c.md) [`00459ad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459ad0.md)
- 新版 呼出元 1件 [`0087f3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f3c0.md) · 呼出先 18件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0044b524`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b524.md) [`004509f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/004509f0.md) [`004517dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/004517dc.md) [`00459b10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00458348",
      "incomplete_value": false,
      "site": "00458350",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:b60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00458308",
      "incomplete_value": false,
      "site": "00458310",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:a90:8"
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0045836c",
      "incomplete_value": false,
      "site": "0045836c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:bb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045832c",
      "incomplete_value": false,
      "site": "0045832c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004583d4",
      "incomplete_value": true,
      "site": "004583d4",
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
                "const:2a8000:8"
              ],
              [
                "leaf",
                "const:a4d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00458394",
      "incomplete_value": true,
      "site": "00458394",
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
                "const:2a8000:8"
              ],
              [
                "leaf",
                "const:aa9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 37,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004582b4",
      "PARAM",
      [
        "storage",
        "002b392c",
        null,
        "string"
      ]
    ],
    [
      "00458350",
      "DATA",
      [
        "storage",
        "00c63a90",
        null,
        "pointer"
      ]
    ],
    [
      "0045836c",
      "DATA",
      [
        "storage",
        "00c63ae0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004582b4",
      "PARAM",
      [
        "storage",
        "002b395d",
        null,
        "string"
      ]
    ],
    [
      "00458350",
      "DATA",
      [
        "storage",
        "00c63b60",
        null,
        "pointer"
      ]
    ],
    [
      "0045836c",
      "DATA",
      [
        "storage",
        "00c63bb0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045827c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/00458230.md#insn-0045827c) · [`004583d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/00458230.md#insn-004583d4) · [`004583fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/00458230.md#insn-004583fc)
- 新版 [`004582bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00458/00458270.md#insn-004582bc) · [`00458414`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00458/00458270.md#insn-00458414) · [`0045843c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00458/00458270.md#insn-0045843c)

~~~diff
- 0045827c ["INT_ADD", "register:40f0:8", ["const:45827c:8", "const:4:8"]]
- 0045827c ["CALL", null, ["callee:00c58040:8"]]
+ 004582bc ["INT_ADD", "register:40f0:8", ["const:4582bc:8", "const:4:8"]]
+ 004582bc ["CALL", null, ["callee:00c58040:8"]]
- 0045827c bytes 3dff1f94
+ 004582bc bytes 61ff1f94
- 004583d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 004583d4 ["INT_ADD", "register:40f0:8", ["const:4583d4:8", "const:4:8"]]
- 004583d4 ["CALLIND", null, ["register:0:8"]]
+ 00458414 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00458414 ["INT_ADD", "register:40f0:8", ["const:458414:8", "const:4:8"]]
+ 00458414 ["CALLIND", null, ["register:0:8"]]
- 004583d4 bytes 00013fd6
+ 00458414 bytes 00013fd6
- 004583fc ["INT_ADD", "register:40f0:8", ["const:4583fc:8", "const:4:8"]]
- 004583fc ["CALL", null, ["callee:00c57f80:8"]]
+ 0045843c ["INT_ADD", "register:40f0:8", ["const:45843c:8", "const:4:8"]]
+ 0045843c ["CALL", null, ["callee:00c57f80:8"]]
- 004583fc bytes adfe1f94
+ 0045843c bytes d1fe1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-866f2f1f6b6546682d99184c52f39c3f"></a>

### [`004586cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/004586cc.md) → [`0045870c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00458/0045870c.md) FUN_0045870c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00458af0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/00458af0.md) · 呼出先 11件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00466d0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/00466d0c.md) [`00561d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561d34.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`00458b30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00458/00458b30.md) · 呼出先 11件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00466d4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00466/00466d4c.md) [`00561d74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/00561d74.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.65% / 新版 97.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00458914",
      "incomplete_value": false,
      "site": "00458914",
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
            "const:ce8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004588d4",
      "incomplete_value": false,
      "site": "004588d4",
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
            "const:c18:8"
          ]
        ]
      ]
    },
    "ordinal": 30,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004588a4",
      "incomplete_value": true,
      "site": "004588ac",
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
                "const:c98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00458864",
      "incomplete_value": true,
      "site": "0045886c",
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
                "const:bc8:8"
              ]
            ]
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
      "00458834",
      "READ",
      [
        "storage",
        "002a5354",
        null,
        "undefined4"
      ]
    ],
    [
      "00458838",
      "READ",
      [
        "storage",
        "002a5358",
        null,
        "undefined1"
      ]
    ],
    [
      "004588a4",
      "READ",
      [
        "storage",
        "00c9abc8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00458834",
      "READ",
      [
        "storage",
        "002a52f8",
        null,
        "undefined4"
      ]
    ],
    [
      "00458838",
      "READ",
      [
        "storage",
        "002a52fc",
        null,
        "undefined1"
      ]
    ],
    [
      "004588a4",
      "READ",
      [
        "storage",
        "00c9ac98",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045886c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/004586cc.md#insn-0045886c) · [`00458730`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/004586cc.md#insn-00458730) · [`00458770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/004586cc.md#insn-00458770)
- 新版 [`004588ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00458/0045870c.md#insn-004588ac) · [`00458770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00458/0045870c.md#insn-00458770) · [`004587b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00458/0045870c.md#insn-004587b0)

~~~diff
- 0045886c ["INT_ADD", "register:40f0:8", ["const:45886c:8", "const:4:8"]]
- 0045886c ["CALL", null, ["callee:00561d74:8"]]
+ 004588ac ["INT_ADD", "register:40f0:8", ["const:4588ac:8", "const:4:8"]]
+ 004588ac ["CALL", null, ["callee:00561d74:8"]]
- 0045886c bytes 32250494
+ 004588ac bytes 32250494
- 00458730 ["INT_ADD", "register:40f0:8", ["const:458730:8", "const:4:8"]]
- 00458730 ["CALL", null, ["callee:00c580a0:8"]]
+ 00458770 ["INT_ADD", "register:40f0:8", ["const:458770:8", "const:4:8"]]
+ 00458770 ["CALL", null, ["callee:00c580a0:8"]]
- 00458730 bytes 28fe1f94
+ 00458770 bytes 4cfe1f94
- 00458770 ["COPY", "tmp:0:8", ["const:ac4:8"]]
- 00458770 ["INT_CARRY", "register:105:1", ["register:40d0:8", "tmp:0:8"]]
- 00458770 ["INT_SCARRY", "register:106:1", ["register:40d0:8", "tmp:0:8"]]
- 00458770 ["INT_ADD", "tmp:1:8", ["register:40d0:8", "tmp:0:8"]]
+ 004587b0 ["COPY", "tmp:0:8", ["const:a68:8"]]
+ 004587b0 ["INT_CARRY", "register:105:1", ["register:40d0:8", "tmp:0:8"]]
+ 004587b0 ["INT_SCARRY", "register:106:1", ["register:40d0:8", "tmp:0:8"]]
+ 004587b0 ["INT_ADD", "tmp:1:8", ["register:40d0:8", "tmp:0:8"]]
- 00458770 bytes 5a132b91
+ 004587b0 bytes 5aa32991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b7a96d8fe9c7a58a983e84798e8a946"></a>

### [`00458af0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/00458af0.md) → [`00458b30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00458/00458b30.md) FUN_00458b30

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0075eb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075eb80.md) · 呼出先 11件 [`0043dba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043dba4.md) [`0044b844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b844.md) [`0044b958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b958.md) [`004586cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/004586cc.md) [`00466f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/00466f40.md)
- 新版 呼出元 1件 [`0075ebd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075e/0075ebd8.md) · 呼出先 11件 [`0043dbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043dbe4.md) [`0044b884`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b884.md) [`0044b998`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b998.md) [`0045870c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00458/0045870c.md) [`00466f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00466/00466f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.73% / 新版 97.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00458bb8",
      "incomplete_value": false,
      "site": "00458bc0",
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
            "const:d68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00458b78",
      "incomplete_value": false,
      "site": "00458b80",
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
            "const:c98:8"
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
      "00458bc0",
      "DATA",
      [
        "storage",
        "00c64c98",
        null,
        "undefined *"
      ]
    ],
    [
      "00458c20",
      "READ",
      [
        "storage",
        "00c64cb8",
        null,
        "pointer"
      ]
    ],
    [
      "00458c20",
      "READ",
      [
        "storage",
        "00c64cc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00458bc0",
      "DATA",
      [
        "storage",
        "00c64d68",
        null,
        "undefined *"
      ]
    ],
    [
      "00458c20",
      "READ",
      [
        "storage",
        "00c64d88",
        null,
        "pointer"
      ]
    ],
    [
      "00458c20",
      "READ",
      [
        "storage",
        "00c64d90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00458b18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/00458af0.md#insn-00458b18) · [`00458b20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/00458af0.md#insn-00458b20) · [`00458b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00458/00458af0.md#insn-00458b30)
- 新版 [`00458b58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00458/00458b30.md#insn-00458b58) · [`00458b60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00458/00458b30.md#insn-00458b60) · [`00458b70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00458/00458b30.md#insn-00458b70)

~~~diff
- 00458b18 ["INT_ADD", "register:40f0:8", ["const:458b18:8", "const:4:8"]]
- 00458b18 ["CALL", null, ["callee:0044b884:8"]]
+ 00458b58 ["INT_ADD", "register:40f0:8", ["const:458b58:8", "const:4:8"]]
+ 00458b58 ["CALL", null, ["callee:0044b884:8"]]
- 00458b18 bytes 4bcbff97
+ 00458b58 bytes 4bcbff97
- 00458b20 ["INT_ADD", "register:40f0:8", ["const:458b20:8", "const:4:8"]]
- 00458b20 ["CALL", null, ["callee:0044b998:8"]]
+ 00458b60 ["INT_ADD", "register:40f0:8", ["const:458b60:8", "const:4:8"]]
+ 00458b60 ["CALL", null, ["callee:0044b998:8"]]
- 00458b20 bytes 8ecbff97
+ 00458b60 bytes 8ecbff97
- 00458b30 ["INT_ADD", "register:40f0:8", ["const:458b30:8", "const:4:8"]]
- 00458b30 ["CALL", null, ["callee:0043dbe4:8"]]
+ 00458b70 ["INT_ADD", "register:40f0:8", ["const:458b70:8", "const:4:8"]]
+ 00458b70 ["CALL", null, ["callee:0043dbe4:8"]]
- 00458b30 bytes 1d94ff97
+ 00458b70 bytes 1d94ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed2031ab5caa4bcfb0f0eebd9e439009"></a>

### [`004593d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004593d0.md) → [`00459410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459410.md) FUN_00459410

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00459418",
      "incomplete_value": false,
      "site": "0045941c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:830:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004593d8",
      "incomplete_value": false,
      "site": "004593dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:760:8"
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
      "0045941c",
      "DATA",
      [
        "storage",
        "00c63760",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0045941c",
      "DATA",
      [
        "storage",
        "00c63830",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004593d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004593d0.md#insn-004593d8)
- 新版 [`00459418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459410.md#insn-00459418)

~~~diff
- 004593d8 ["COPY", "tmp:0:8", ["const:760:8"]]
- 004593d8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004593d8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004593d8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00459418 ["COPY", "tmp:0:8", ["const:830:8"]]
+ 00459418 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00459418 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00459418 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004593d8 bytes 29811d91
+ 00459418 bytes 29c12091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89f6522c8b8e9f60b95042a4b7bba38c"></a>

### [`004593f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004593f0.md) → [`00459430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459430.md) FUN_00459430

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 6件 [`0045179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/0045179c.md) [`0059bae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059bae4.md) [`005a1470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a1/005a1470.md) [`0076625c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00766/0076625c.md) [`00798ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00798/00798ea0.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 6件 [`004517dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/004517dc.md) [`0059bb24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059b/0059bb24.md) [`005a14b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a1/005a14b0.md) [`007662b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00766/007662b4.md) [`00798ef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00798/00798ef8.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00459438",
      "incomplete_value": false,
      "site": "0045943c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:830:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004593f8",
      "incomplete_value": false,
      "site": "004593fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:760:8"
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
      "0045943c",
      "DATA",
      [
        "storage",
        "00c63760",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0045943c",
      "DATA",
      [
        "storage",
        "00c63830",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004593f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004593f0.md#insn-004593f8) · [`0045941c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004593f0.md#insn-0045941c)
- 新版 [`00459438`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459430.md#insn-00459438) · [`0045945c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459430.md#insn-0045945c)

~~~diff
- 004593f8 ["COPY", "tmp:0:8", ["const:760:8"]]
- 004593f8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004593f8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004593f8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00459438 ["COPY", "tmp:0:8", ["const:830:8"]]
+ 00459438 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00459438 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00459438 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004593f8 bytes 29811d91
+ 00459438 bytes 29c12091
- 0045941c ["INT_ADD", "register:40f0:8", ["const:45941c:8", "const:4:8"]]
- 0045941c ["CALL", null, ["callee:00c57f80:8"]]
+ 0045945c ["INT_ADD", "register:40f0:8", ["const:45945c:8", "const:4:8"]]
+ 0045945c ["CALL", null, ["callee:00c57f80:8"]]
- 0045941c bytes a5fa1f94
+ 0045945c bytes c9fa1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fcc854ea92067fc34d8aef3e63e7b645"></a>

### [`004594d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004594d0.md) → [`00459510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459510.md) FUN_00459510

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 25件 [`004519d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004519d8.md) [`00466f48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/00466f48.md) [`00478314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478314.md) [`00488584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488584.md) [`0048cf68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048cf68.md) · 呼出先 8件 [`00459668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459668.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58260.md) [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md)
- 新版 呼出元 25件 [`00451a18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/00451a18.md) [`00466f88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00466/00466f88.md) [`00478354`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00478/00478354.md) [`004885c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/004885c4.md) [`0048cfa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cfa8.md) · 呼出先 8件 [`004596a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/004596a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58330.md) [`00c58340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58340.md) [`00c58350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58350.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.67% / 新版 98.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00459590",
      "incomplete_value": true,
      "site": "00459594",
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
    "old": {
      "definition_site": "00459550",
      "incomplete_value": true,
      "site": "00459554",
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
                "const:c30:8"
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
      "00459590",
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ],
    [
      "00459590",
      "PARAM",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00459590",
      "READ",
      [
        "storage",
        "00c9ad00",
        null,
        "pointer"
      ]
    ],
    [
      "00459590",
      "PARAM",
      [
        "storage",
        "01127f18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00459554`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004594d0.md#insn-00459554) · [`0045950c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004594d0.md#insn-0045950c) · [`00459544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004594d0.md#insn-00459544)
- 新版 [`00459594`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459510.md#insn-00459594) · [`0045954c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459510.md#insn-0045954c) · [`00459584`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459510.md#insn-00459584)

~~~diff
- 00459554 ["INT_ADD", "register:40f0:8", ["const:459554:8", "const:4:8"]]
- 00459554 ["CALL", null, ["callee:00c58350:8"]]
+ 00459594 ["INT_ADD", "register:40f0:8", ["const:459594:8", "const:4:8"]]
+ 00459594 ["CALL", null, ["callee:00c58350:8"]]
- 00459554 bytes 4bfb1f94
+ 00459594 bytes 6ffb1f94
- 0045950c ["INT_ADD", "register:40f0:8", ["const:45950c:8", "const:4:8"]]
- 0045950c ["CALL", null, ["callee:00c58330:8"]]
+ 0045954c ["INT_ADD", "register:40f0:8", ["const:45954c:8", "const:4:8"]]
+ 0045954c ["CALL", null, ["callee:00c58330:8"]]
- 0045950c bytes 55fb1f94
+ 0045954c bytes 79fb1f94
- 00459544 ["INT_ADD", "register:40f0:8", ["const:459544:8", "const:4:8"]]
- 00459544 ["CALL", null, ["callee:00c58340:8"]]
+ 00459584 ["INT_ADD", "register:40f0:8", ["const:459584:8", "const:4:8"]]
+ 00459584 ["CALL", null, ["callee:00c58340:8"]]
- 00459544 bytes 4bfb1f94
+ 00459584 bytes 6ffb1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-770a737a6d4b8ce814156e5a8585cc10"></a>

### [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) → [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) FUN_00459db4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 207件 [`00459ff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459ff0.md) [`0045ab6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045ab6c.md) [`0045b8d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b8d4.md) [`0045c0b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045c0b8.md) [`0045c908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045c908.md) · 呼出先 3件 [`00c37ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ba4.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 207件 [`0045a030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a030.md) [`0045abac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045abac.md) [`0045b914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045b914.md) [`0045c0f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045c0f8.md) [`0045c948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045c948.md) · 呼出先 3件 [`00c37c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c40.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00459dd4",
      "incomplete_value": true,
      "site": "00459dd8",
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
      "definition_site": "00459d94",
      "incomplete_value": true,
      "site": "00459d98",
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00459ddc",
      "incomplete_value": true,
      "site": "00459de4",
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00459d9c",
      "incomplete_value": true,
      "site": "00459da4",
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
                "const:c40:8"
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
      "definition_site": "00459de0",
      "incomplete_value": true,
      "site": "00459de4",
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
                "const:d18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00459da0",
      "incomplete_value": true,
      "site": "00459da4",
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
                "const:c48:8"
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
      "00459dd0",
      "READ",
      [
        "storage",
        "00c9ac38",
        null,
        "pointer"
      ]
    ],
    [
      "00459dd8",
      "DATA",
      [
        "storage",
        "00c637f8",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "00459ddc",
      "READ",
      [
        "storage",
        "00c9ac40",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00459dd0",
      "READ",
      [
        "storage",
        "00c9ad08",
        null,
        "pointer"
      ]
    ],
    [
      "00459dd8",
      "DATA",
      [
        "storage",
        "00c638c8",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "00459ddc",
      "READ",
      [
        "storage",
        "00c9ad10",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00459da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md#insn-00459da4) · [`00459d80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md#insn-00459d80) · [`00459d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md#insn-00459d90)
- 新版 [`00459de4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md#insn-00459de4) · [`00459dc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md#insn-00459dc0) · [`00459dd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md#insn-00459dd0)

~~~diff
- 00459da4 ["INT_ADD", "register:40f0:8", ["const:459da4:8", "const:4:8"]]
- 00459da4 ["CALL", null, ["callee:00c57fe0:8"]]
+ 00459de4 ["INT_ADD", "register:40f0:8", ["const:459de4:8", "const:4:8"]]
+ 00459de4 ["CALL", null, ["callee:00c57fe0:8"]]
- 00459da4 bytes 5bf81f94
+ 00459de4 bytes 7ff81f94
- 00459d80 ["INT_ADD", "register:40f0:8", ["const:459d80:8", "const:4:8"]]
- 00459d80 ["CALL", null, ["callee:00c57fc0:8"]]
+ 00459dc0 ["INT_ADD", "register:40f0:8", ["const:459dc0:8", "const:4:8"]]
+ 00459dc0 ["CALL", null, ["callee:00c57fc0:8"]]
- 00459d80 bytes 5cf81f94
+ 00459dc0 bytes 80f81f94
- 00459d90 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c38:8"]]
- 00459d90 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00459dd0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d08:8"]]
+ 00459dd0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00459d90 bytes 081d46f9
+ 00459dd0 bytes 088546f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9621a057bd6c1dd942806d4d553a36e"></a>

### [`00459dcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459dcc.md) → [`00459e0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459e0c.md) FUN_00459e0c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00459e18",
      "incomplete_value": false,
      "site": "00459e24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:8f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00459dd8",
      "incomplete_value": false,
      "site": "00459de4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:820:8"
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
      "00459e24",
      "DATA",
      [
        "storage",
        "00c63820",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00459e24",
      "DATA",
      [
        "storage",
        "00c638f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00459dd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459dcc.md#insn-00459dd8)
- 新版 [`00459e18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459e0c.md#insn-00459e18)

~~~diff
- 00459dd8 ["COPY", "tmp:0:8", ["const:820:8"]]
- 00459dd8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00459dd8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00459dd8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00459e18 ["COPY", "tmp:0:8", ["const:8f0:8"]]
+ 00459e18 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00459e18 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00459e18 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00459dd8 bytes 4a812091
+ 00459e18 bytes 4ac12391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0bfd2239991a4a285195776158b51fc1"></a>

### [`00459e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459e10.md) → [`00459e50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459e50.md) FUN_00459e50

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00459e68",
      "incomplete_value": false,
      "site": "00459e74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:8f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00459e28",
      "incomplete_value": false,
      "site": "00459e34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:820:8"
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
      "00459e74",
      "DATA",
      [
        "storage",
        "00c63820",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00459e74",
      "DATA",
      [
        "storage",
        "00c638f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00459e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459e10.md#insn-00459e28) · [`00459e58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459e10.md#insn-00459e58)
- 新版 [`00459e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459e50.md#insn-00459e68) · [`00459e98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459e50.md#insn-00459e98)

~~~diff
- 00459e28 ["COPY", "tmp:0:8", ["const:820:8"]]
- 00459e28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00459e28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00459e28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00459e68 ["COPY", "tmp:0:8", ["const:8f0:8"]]
+ 00459e68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00459e68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00459e68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00459e28 bytes 08812091
+ 00459e68 bytes 08c12391
- 00459e58 ["COPY", "register:0:8", ["register:4040:8"]]
- 00459e58 ["INT_ADD", "register:40f0:8", ["const:459e58:8", "const:4:8"]]
- 00459e58 ["CALLIND", null, ["register:0:8"]]
+ 00459e98 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00459e98 ["INT_ADD", "register:40f0:8", ["const:459e98:8", "const:4:8"]]
+ 00459e98 ["CALLIND", null, ["register:0:8"]]
- 00459e58 bytes 00013fd6
+ 00459e98 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ccee24c45184e8a58cac26cd48a932b4"></a>

### [`00459e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459e6c.md) → [`00459eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459eac.md) FUN_00459eac

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "00459ed8",
      "incomplete_value": false,
      "site": "00459ed8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:8f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00459e98",
      "incomplete_value": false,
      "site": "00459e98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:820:8"
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
      "00459ed8",
      "DATA",
      [
        "storage",
        "00c63820",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00459ed8",
      "DATA",
      [
        "storage",
        "00c638f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00459e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459e6c.md#insn-00459e80) · [`00459e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459e6c.md#insn-00459e90) · [`00459eb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459e6c.md#insn-00459eb4)
- 新版 [`00459ec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459eac.md#insn-00459ec0) · [`00459ed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459eac.md#insn-00459ed0) · [`00459ef4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459eac.md#insn-00459ef4)

~~~diff
- 00459e80 ["INT_ADD", "register:40f0:8", ["const:459e80:8", "const:4:8"]]
- 00459e80 ["CALL", null, ["callee:00c57f60:8"]]
+ 00459ec0 ["INT_ADD", "register:40f0:8", ["const:459ec0:8", "const:4:8"]]
+ 00459ec0 ["CALL", null, ["callee:00c57f60:8"]]
- 00459e80 bytes 04f81f94
+ 00459ec0 bytes 28f81f94
- 00459e90 ["COPY", "tmp:0:8", ["const:820:8"]]
- 00459e90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00459e90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00459e90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00459ed0 ["COPY", "tmp:0:8", ["const:8f0:8"]]
+ 00459ed0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00459ed0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00459ed0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00459e90 bytes 08812091
+ 00459ed0 bytes 08c12391
- 00459eb4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00459eb4 ["INT_ADD", "register:40f0:8", ["const:459eb4:8", "const:4:8"]]
- 00459eb4 ["CALLIND", null, ["register:0:8"]]
+ 00459ef4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00459ef4 ["INT_ADD", "register:40f0:8", ["const:459ef4:8", "const:4:8"]]
+ 00459ef4 ["CALLIND", null, ["register:0:8"]]
- 00459eb4 bytes 00013fd6
+ 00459ef4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b4fac0916a2a0674d85158b58fbbd54"></a>

### [`00459ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459ef4.md) → [`00459f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459f34.md) FUN_00459f34

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00459f50",
      "incomplete_value": false,
      "site": "00459f50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:8f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00459f10",
      "incomplete_value": false,
      "site": "00459f10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:820:8"
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
      "00459f50",
      "DATA",
      [
        "storage",
        "00c63820",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00459f50",
      "DATA",
      [
        "storage",
        "00c638f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00459f0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459ef4.md#insn-00459f0c) · [`00459f30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459ef4.md#insn-00459f30)
- 新版 [`00459f4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459f34.md#insn-00459f4c) · [`00459f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459f34.md#insn-00459f70)

~~~diff
- 00459f0c ["COPY", "tmp:0:8", ["const:820:8"]]
- 00459f0c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00459f0c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00459f0c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00459f4c ["COPY", "tmp:0:8", ["const:8f0:8"]]
+ 00459f4c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00459f4c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00459f4c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00459f0c bytes 29812091
+ 00459f4c bytes 29c12391
- 00459f30 ["COPY", "register:0:8", ["register:4048:8"]]
- 00459f30 ["INT_ADD", "register:40f0:8", ["const:459f30:8", "const:4:8"]]
- 00459f30 ["CALLIND", null, ["register:0:8"]]
+ 00459f70 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00459f70 ["INT_ADD", "register:40f0:8", ["const:459f70:8", "const:4:8"]]
+ 00459f70 ["CALLIND", null, ["register:0:8"]]
- 00459f30 bytes 20013fd6
+ 00459f70 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db2d268fa6327c194b8870ff81de0718"></a>

### [`00459ff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459ff0.md) → [`0045a030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a030.md) FUN_0045a030

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00596d10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596d10.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)
- 新版 呼出元 0件  · 呼出先 11件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00596d50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596d50.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.45% / 新版 93.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 4件, `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0045a154",
      "incomplete_value": true,
      "site": "0045a154",
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
                "const:2b5000:8"
              ],
              [
                "leaf",
                "const:ecf:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045a114",
      "incomplete_value": true,
      "site": "0045a114",
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
                "const:2b5000:8"
              ],
              [
                "leaf",
                "const:e8f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0045a1b4",
      "incomplete_value": true,
      "site": "0045a1b4",
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
              [
                "leaf",
                "const:40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045a174",
      "incomplete_value": true,
      "site": "0045a174",
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
              [
                "leaf",
                "const:40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0045a1a4",
      "incomplete_value": true,
      "site": "0045a1b4",
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
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:b98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045a164",
      "incomplete_value": true,
      "site": "0045a174",
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
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:a98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0045a144",
      "READ",
      [
        "storage",
        "002b5e8f",
        null,
        "string"
      ]
    ],
    [
      "0045a198",
      "READ",
      [
        "storage",
        "00ca4aa0",
        null,
        "undefined1"
      ]
    ],
    [
      "0045a1a4",
      "READ",
      [
        "storage",
        "00ca4a98",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0045a144",
      "READ",
      [
        "storage",
        "002b5ecf",
        null,
        "string"
      ]
    ],
    [
      "0045a198",
      "READ",
      [
        "storage",
        "00ca4ba0",
        null,
        "undefined1"
      ]
    ],
    [
      "0045a1a4",
      "READ",
      [
        "storage",
        "00ca4b98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045a154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459ff0.md#insn-0045a154) · [`0045a174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459ff0.md#insn-0045a174) · [`0045a1b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459ff0.md#insn-0045a1b4)
- 新版 [`0045a194`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a030.md#insn-0045a194) · [`0045a1b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a030.md#insn-0045a1b4) · [`0045a1f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a030.md#insn-0045a1f4)

~~~diff
- 0045a154 ["COPY", "tmp:0:8", ["const:aa0:8"]]
- 0045a154 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045a154 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045a154 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045a194 ["COPY", "tmp:0:8", ["const:ba0:8"]]
+ 0045a194 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045a194 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045a194 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045a154 bytes 08812a91
+ 0045a194 bytes 08812e91
- 0045a174 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045a174 ["INT_ADD", "register:40f0:8", ["const:45a174:8", "const:4:8"]]
- 0045a174 ["CALLIND", null, ["register:0:8"]]
+ 0045a1b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045a1b4 ["INT_ADD", "register:40f0:8", ["const:45a1b4:8", "const:4:8"]]
+ 0045a1b4 ["CALLIND", null, ["register:0:8"]]
- 0045a174 bytes 00013fd6
+ 0045a1b4 bytes 00013fd6
- 0045a1b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045a1b4 ["INT_ADD", "register:40f0:8", ["const:45a1b4:8", "const:4:8"]]
- 0045a1b4 ["CALLIND", null, ["register:0:8"]]
+ 0045a1f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045a1f4 ["INT_ADD", "register:40f0:8", ["const:45a1f4:8", "const:4:8"]]
+ 0045a1f4 ["CALLIND", null, ["register:0:8"]]
- 0045a1b4 bytes 00013fd6
+ 0045a1f4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14fa143eb84b1eee18d7655ecde29d4a"></a>

### [`0045a560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a560.md) → [`0045a5a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a5a0.md) FUN_0045a5a0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 76.92% / 新版 76.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0045a5b8",
      "incomplete_value": true,
      "site": "0045a5bc",
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
      "definition_site": "0045a578",
      "incomplete_value": true,
      "site": "0045a57c",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0045a5b4",
      "READ",
      [
        "storage",
        "00c9ac00",
        null,
        "pointer"
      ]
    ],
    [
      "0045a5bc",
      "DATA",
      [
        "storage",
        "00c638a0",
        null,
        "undefined1[56]"
      ]
    ]
  ],
  "added": [
    [
      "0045a5b4",
      "READ",
      [
        "storage",
        "00c9acd0",
        null,
        "pointer"
      ]
    ],
    [
      "0045a5bc",
      "DATA",
      [
        "storage",
        "00c63970",
        null,
        "undefined1[56]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045a574`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a560.md#insn-0045a574) · [`0045a580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a560.md#insn-0045a580)
- 新版 [`0045a5b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a5a0.md#insn-0045a5b4) · [`0045a5c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a5a0.md#insn-0045a5c0)

~~~diff
- 0045a574 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c00:8"]]
- 0045a574 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0045a5b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cd0:8"]]
+ 0045a5b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0045a574 bytes 080146f9
+ 0045a5b4 bytes 086946f9
- 0045a580 ["INT_ADD", "register:40f0:8", ["const:45a580:8", "const:4:8"]]
- 0045a580 ["CALL", null, ["callee:00c57f70:8"]]
+ 0045a5c0 ["INT_ADD", "register:40f0:8", ["const:45a5c0:8", "const:4:8"]]
+ 0045a5c0 ["CALL", null, ["callee:00c57f70:8"]]
- 0045a580 bytes 48f61f94
+ 0045a5c0 bytes 6cf61f94
~~~


<a id="compare-a146a15e2fd02b3700bd6a494cecf7c1"></a>

### [`0045a5a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a5a0.md) → [`0045a5e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a5e0.md) FUN_0045a5e0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0045a594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a594.md) · 呼出先 12件 [`0045a6c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a6c8.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c582f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582f0.md)
- 新版 呼出元 1件 [`0045a5d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a5d4.md) · 呼出先 12件 [`0045a708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a708.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c583c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.52% / 新版 94.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0045a684",
      "incomplete_value": true,
      "site": "0045a688",
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
      "definition_site": "0045a644",
      "incomplete_value": true,
      "site": "0045a648",
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
      "definition_site": "0045a660",
      "incomplete_value": true,
      "site": "0045a668",
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
                "const:d28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045a620",
      "incomplete_value": true,
      "site": "0045a628",
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
                "const:c58:8"
              ]
            ]
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
      "definition_site": "0045a65c",
      "incomplete_value": false,
      "site": "0045a668",
      "value": [
        "leaf",
        "const:45a708:8"
      ]
    },
    "old": {
      "definition_site": "0045a61c",
      "incomplete_value": false,
      "site": "0045a628",
      "value": [
        "leaf",
        "const:45a6c8:8"
      ]
    },
    "ordinal": 4,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0045a65c",
      "PARAM",
      [
        "storage",
        "0045a6c8",
        null,
        null
      ]
    ],
    [
      "0045a660",
      "READ",
      [
        "storage",
        "00c9ac58",
        null,
        "pointer"
      ]
    ],
    [
      "0045a660",
      "PARAM",
      [
        "storage",
        "00c92cb0",
        "_ZTINSt6__ndk112future_errorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0045a65c",
      "PARAM",
      [
        "storage",
        "0045a708",
        null,
        null
      ]
    ],
    [
      "0045a660",
      "READ",
      [
        "storage",
        "00c9ad28",
        null,
        "pointer"
      ]
    ],
    [
      "0045a660",
      "PARAM",
      [
        "storage",
        "00c92d80",
        "_ZTINSt6__ndk112future_errorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045a608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a5a0.md#insn-0045a608) · [`0045a628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a5a0.md#insn-0045a628) · [`0045a5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a5a0.md#insn-0045a5e0)
- 新版 [`0045a648`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a5e0.md#insn-0045a648) · [`0045a668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a5e0.md#insn-0045a668) · [`0045a620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a5e0.md#insn-0045a620)

~~~diff
- 0045a608 ["INT_ADD", "register:40f0:8", ["const:45a608:8", "const:4:8"]]
- 0045a608 ["CALL", null, ["callee:00c583f0:8"]]
+ 0045a648 ["INT_ADD", "register:40f0:8", ["const:45a648:8", "const:4:8"]]
+ 0045a648 ["CALL", null, ["callee:00c583f0:8"]]
- 0045a608 bytes 46f71f94
+ 0045a648 bytes 6af71f94
- 0045a628 ["INT_ADD", "register:40f0:8", ["const:45a628:8", "const:4:8"]]
- 0045a628 ["CALL", null, ["callee:00c58400:8"]]
+ 0045a668 ["INT_ADD", "register:40f0:8", ["const:45a668:8", "const:4:8"]]
+ 0045a668 ["CALL", null, ["callee:00c58400:8"]]
- 0045a628 bytes 42f71f94
+ 0045a668 bytes 66f71f94
- 0045a5e0 ["INT_ADD", "register:40f0:8", ["const:45a5e0:8", "const:4:8"]]
- 0045a5e0 ["CALL", null, ["callee:00c583c0:8"]]
+ 0045a620 ["INT_ADD", "register:40f0:8", ["const:45a620:8", "const:4:8"]]
+ 0045a620 ["CALL", null, ["callee:00c583c0:8"]]
- 0045a5e0 bytes 44f71f94
+ 0045a620 bytes 68f71f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e1f0e70447b228aa6bc100c8f4f8447"></a>

### [`0045a6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a6d4.md) → [`0045a714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a714.md) FUN_0045a714

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 20件 [`004539dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/004539dc.md) [`0045f03c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f03c.md) [`0045fadc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fadc.md) [`00538340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00538/00538340.md) [`005385f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00538/005385f0.md) · 呼出先 5件 [`00bf9638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9638.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c58310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58310.md) [`00c58320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58320.md)
- 新版 呼出元 20件 [`00453a1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00453/00453a1c.md) [`0045f07c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f07c.md) [`0045fb1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045fb1c.md) [`00538380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00538/00538380.md) [`00538630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00538/00538630.md) · 呼出先 5件 [`00bf96d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf9/00bf96d4.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c583e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583e0.md) [`00c583f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0045a750",
      "incomplete_value": true,
      "site": "0045a758",
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
                "const:d28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045a710",
      "incomplete_value": true,
      "site": "0045a718",
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
                "const:c58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0045a754",
      "incomplete_value": true,
      "site": "0045a758",
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
                "const:d38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045a714",
      "incomplete_value": true,
      "site": "0045a718",
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
                "const:c68:8"
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
      "0045a750",
      "READ",
      [
        "storage",
        "00c9ac58",
        null,
        "pointer"
      ]
    ],
    [
      "0045a750",
      "PARAM",
      [
        "storage",
        "00c92cb0",
        "_ZTINSt6__ndk112future_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0045a754",
      "READ",
      [
        "storage",
        "00c9ac68",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0045a750",
      "READ",
      [
        "storage",
        "00c9ad28",
        null,
        "pointer"
      ]
    ],
    [
      "0045a750",
      "PARAM",
      [
        "storage",
        "00c92d80",
        "_ZTINSt6__ndk112future_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0045a754",
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045a718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a6d4.md#insn-0045a718) · [`0045a6e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a6d4.md#insn-0045a6e8) · [`0045a6f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a6d4.md#insn-0045a6f0)
- 新版 [`0045a758`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a714.md#insn-0045a758) · [`0045a728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a714.md#insn-0045a728) · [`0045a730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a714.md#insn-0045a730)

~~~diff
- 0045a718 ["INT_ADD", "register:40f0:8", ["const:45a718:8", "const:4:8"]]
- 0045a718 ["CALL", null, ["callee:00c57fe0:8"]]
+ 0045a758 ["INT_ADD", "register:40f0:8", ["const:45a758:8", "const:4:8"]]
+ 0045a758 ["CALL", null, ["callee:00c57fe0:8"]]
- 0045a718 bytes fef51f94
+ 0045a758 bytes 22f61f94
- 0045a6e8 ["INT_ADD", "register:40f0:8", ["const:45a6e8:8", "const:4:8"]]
- 0045a6e8 ["CALL", null, ["callee:00c57fc0:8"]]
+ 0045a728 ["INT_ADD", "register:40f0:8", ["const:45a728:8", "const:4:8"]]
+ 0045a728 ["CALL", null, ["callee:00c57fc0:8"]]
- 0045a6e8 bytes 02f61f94
+ 0045a728 bytes 26f61f94
- 0045a6f0 ["INT_ADD", "register:40f0:8", ["const:45a6f0:8", "const:4:8"]]
- 0045a6f0 ["CALL", null, ["callee:00c583e0:8"]]
+ 0045a730 ["INT_ADD", "register:40f0:8", ["const:45a730:8", "const:4:8"]]
+ 0045a730 ["CALL", null, ["callee:00c583e0:8"]]
- 0045a6f0 bytes 08f71f94
+ 0045a730 bytes 2cf71f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-241d12611c3e61aec4fc0170c114fe12"></a>

### [`0045a734`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a734.md) → [`0045a774`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a774.md) FUN_0045a774

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "0045a788",
      "incomplete_value": false,
      "site": "0045a78c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:9d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045a748",
      "incomplete_value": false,
      "site": "0045a74c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:900:8"
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
      "0045a78c",
      "DATA",
      [
        "storage",
        "00c63900",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045a78c",
      "DATA",
      [
        "storage",
        "00c639d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045a740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a734.md#insn-0045a740) · [`0045a748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a734.md#insn-0045a748)
- 新版 [`0045a780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a774.md#insn-0045a780) · [`0045a788`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a774.md#insn-0045a788)

~~~diff
- 0045a740 ["INT_ADD", "register:40f0:8", ["const:45a740:8", "const:4:8"]]
- 0045a740 ["CALL", null, ["callee:00c57f60:8"]]
+ 0045a780 ["INT_ADD", "register:40f0:8", ["const:45a780:8", "const:4:8"]]
+ 0045a780 ["CALL", null, ["callee:00c57f60:8"]]
- 0045a740 bytes d4f51f94
+ 0045a780 bytes f8f51f94
- 0045a748 ["COPY", "tmp:0:8", ["const:900:8"]]
- 0045a748 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045a748 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045a748 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045a788 ["COPY", "tmp:0:8", ["const:9d0:8"]]
+ 0045a788 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045a788 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045a788 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045a748 bytes 08012491
+ 0045a788 bytes 08412791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4fd32f57e8cf9976eacf02ce4c9e3085"></a>

### [`0045a758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a758.md) → [`0045a798`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a798.md) FUN_0045a798

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0045a79c",
      "incomplete_value": false,
      "site": "0045a7a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:9d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045a75c",
      "incomplete_value": false,
      "site": "0045a760",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
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
      "0045a7a0",
      "DATA",
      [
        "storage",
        "00c63900",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045a7a0",
      "DATA",
      [
        "storage",
        "00c639d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045a75c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a758.md#insn-0045a75c)
- 新版 [`0045a79c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a798.md#insn-0045a79c)

~~~diff
- 0045a75c ["COPY", "tmp:0:8", ["const:900:8"]]
- 0045a75c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045a75c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045a75c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045a79c ["COPY", "tmp:0:8", ["const:9d0:8"]]
+ 0045a79c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045a79c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045a79c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045a75c bytes 08012491
+ 0045a79c bytes 08412791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5becbffc94ddac12b94fb5cbd3ba995b"></a>

### [`0045a770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a770.md) → [`0045a7b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a7b0.md) FUN_0045a7b0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00596d10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596d10.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md)
- 新版 呼出元 0件  · 呼出先 9件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00596d50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596d50.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 91.72% / 新版 91.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件

アドレスに依存する影響 `call_argument_candidate` 3件, `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0045a8dc",
      "incomplete_value": true,
      "site": "0045a8dc",
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
              [
                "leaf",
                "const:50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045a89c",
      "incomplete_value": true,
      "site": "0045a89c",
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
              [
                "leaf",
                "const:50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0045a8d0",
      "incomplete_value": true,
      "site": "0045a8dc",
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
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:b98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045a890",
      "incomplete_value": true,
      "site": "0045a89c",
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
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:a98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0045a94c",
      "incomplete_value": true,
      "site": "0045a94c",
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
              [
                "leaf",
                "const:58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045a90c",
      "incomplete_value": true,
      "site": "0045a90c",
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
              [
                "leaf",
                "const:58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0045a8c0",
      "READ",
      [
        "storage",
        "00ca4aa0",
        null,
        "undefined1"
      ]
    ],
    [
      "0045a8d0",
      "READ",
      [
        "storage",
        "00ca4a98",
        null,
        "undefined8"
      ]
    ],
    [
      "0045a8ec",
      "READ",
      [
        "storage",
        "00ca4aa0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0045a8c0",
      "READ",
      [
        "storage",
        "00ca4ba0",
        null,
        "undefined1"
      ]
    ],
    [
      "0045a8d0",
      "READ",
      [
        "storage",
        "00ca4b98",
        null,
        "undefined8"
      ]
    ],
    [
      "0045a8ec",
      "READ",
      [
        "storage",
        "00ca4ba0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045a89c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a770.md#insn-0045a89c) · [`0045a90c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a770.md#insn-0045a90c) · [`0045a968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a770.md#insn-0045a968)
- 新版 [`0045a8dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a7b0.md#insn-0045a8dc) · [`0045a94c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a7b0.md#insn-0045a94c) · [`0045a9a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a7b0.md#insn-0045a9a8)

~~~diff
- 0045a89c ["COPY", "register:0:8", ["register:4040:8"]]
- 0045a89c ["INT_ADD", "register:40f0:8", ["const:45a89c:8", "const:4:8"]]
- 0045a89c ["CALLIND", null, ["register:0:8"]]
+ 0045a8dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045a8dc ["INT_ADD", "register:40f0:8", ["const:45a8dc:8", "const:4:8"]]
+ 0045a8dc ["CALLIND", null, ["register:0:8"]]
- 0045a89c bytes 00013fd6
+ 0045a8dc bytes 00013fd6
- 0045a90c ["COPY", "register:0:8", ["register:4040:8"]]
- 0045a90c ["INT_ADD", "register:40f0:8", ["const:45a90c:8", "const:4:8"]]
- 0045a90c ["CALLIND", null, ["register:0:8"]]
+ 0045a94c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045a94c ["INT_ADD", "register:40f0:8", ["const:45a94c:8", "const:4:8"]]
+ 0045a94c ["CALLIND", null, ["register:0:8"]]
- 0045a90c bytes 00013fd6
+ 0045a94c bytes 00013fd6
- 0045a968 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a98:8"]]
- 0045a968 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0045a9a8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b98:8"]]
+ 0045a9a8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0045a968 bytes 004d45f9
+ 0045a9a8 bytes 00cd45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

