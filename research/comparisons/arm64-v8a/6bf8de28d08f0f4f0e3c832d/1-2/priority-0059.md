# v16.0.1 → v16.0.2 · 最優先の変更候補 (59)

[一覧の目次](README.md)

<a id="compare-0ba73256c8d9da5d3a7a0487f069d60f"></a>

### [`009d5cf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d5/009d5cf8.md) → [`009d5d4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d5/009d5d4c.md) FUN_009d5d4c

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) [`007ef684`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007ef684.md) [`0089e87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089e/0089e87c.md) [`009d7b7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d7/009d7b7c.md) [`00a47f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47f00.md) · 呼出先 36件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`004476f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/004476f4.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md)
- 新版 呼出元 5件 [`007bda9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bd/007bda9c.md) [`007ef6dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ef/007ef6dc.md) [`0089e8d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089e/0089e8d4.md) [`009d7bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d7/009d7bd0.md) [`00a47f54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a47/00a47f54.md) · 呼出先 36件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00447734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447734.md) [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 95.81% / 新版 95.81%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 34件, `call_target` 1件, `store_destination` 1件, `store_value` 7件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009d5e0c",
      "incomplete_value": false,
      "site": "009d5e18",
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
    "old": {
      "definition_site": "009d5db8",
      "incomplete_value": false,
      "site": "009d5dc4",
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
            "const:d38:8"
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
      "definition_site": "009d5e38",
      "incomplete_value": true,
      "site": "009d5e58",
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
                "const:2b4000:8"
              ],
              [
                "leaf",
                "const:30f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009d5de4",
      "incomplete_value": true,
      "site": "009d5e04",
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
                "const:2b4000:8"
              ],
              [
                "leaf",
                "const:2de:8"
              ]
            ]
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
      "definition_site": "009d610c",
      "incomplete_value": false,
      "site": "009d6110",
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
    "old": {
      "definition_site": "009d60b8",
      "incomplete_value": false,
      "site": "009d60bc",
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
            "const:d38:8"
          ]
        ]
      ]
    },
    "ordinal": 54,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009d5da8",
      "READ",
      [
        "storage",
        "00c9b610",
        null,
        "pointer"
      ]
    ],
    [
      "009d5dac",
      "PARAM",
      [
        "storage",
        "011218f0",
        null,
        "undefined1"
      ]
    ],
    [
      "009d5dbc",
      "READ",
      [
        "storage",
        "00c9b620",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "009d5da8",
      "READ",
      [
        "storage",
        "00c9b6e0",
        null,
        "pointer"
      ]
    ],
    [
      "009d5dac",
      "PARAM",
      [
        "storage",
        "011219f0",
        null,
        "undefined1"
      ]
    ],
    [
      "009d5dbc",
      "READ",
      [
        "storage",
        "00c9b6f0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009d5d5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d5/009d5cf8.md#insn-009d5d5c) · [`009d5d6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d5/009d5cf8.md#insn-009d5d6c) · [`009d5e18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d5/009d5cf8.md#insn-009d5e18)
- 新版 [`009d5db0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d5/009d5d4c.md#insn-009d5db0) · [`009d5dc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d5/009d5d4c.md#insn-009d5dc0) · [`009d5e6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d5/009d5d4c.md#insn-009d5e6c)

~~~diff
- 009d5d5c ["INT_ADD", "register:40f0:8", ["const:9d5d5c:8", "const:4:8"]]
- 009d5d5c ["CALL", null, ["callee:00484800:8"]]
+ 009d5db0 ["INT_ADD", "register:40f0:8", ["const:9d5db0:8", "const:4:8"]]
+ 009d5db0 ["CALL", null, ["callee:00484800:8"]]
- 009d5d5c bytes 99baea97
+ 009d5db0 bytes 94baea97
- 009d5d6c ["INT_ADD", "register:40f0:8", ["const:9d5d6c:8", "const:4:8"]]
- 009d5d6c ["CALL", null, ["callee:004939d8:8"]]
+ 009d5dc0 ["INT_ADD", "register:40f0:8", ["const:9d5dc0:8", "const:4:8"]]
+ 009d5dc0 ["CALL", null, ["callee:004939d8:8"]]
- 009d5d6c bytes 0bf7ea97
+ 009d5dc0 bytes 06f7ea97
- 009d5e18 ["INT_ADD", "register:40f0:8", ["const:9d5e18:8", "const:4:8"]]
- 009d5e18 ["CALL", null, ["callee:00447734:8"]]
+ 009d5e6c ["INT_ADD", "register:40f0:8", ["const:9d5e6c:8", "const:4:8"]]
+ 009d5e6c ["CALL", null, ["callee:00447734:8"]]
- 009d5e18 bytes 37c6e997
+ 009d5e6c bytes 32c6e997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4edf59d2eee312c009dec7aa29f990d"></a>

### [`009dc6f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dc/009dc6f0.md) → [`009dc744`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dc/009dc744.md) FUN_009dc744

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b28f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b28/00b28f54.md) · 呼出先 14件 [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0048791c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048791c.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00487a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487a64.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md)
- 新版 呼出元 1件 [`00b28ff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b28/00b28ff0.md) · 呼出先 14件 [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0048795c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048795c.md) [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md) [`00487aa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487aa4.md) [`00487e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487e60.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 93.80% / 新版 93.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 5件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009dc78c",
      "incomplete_value": false,
      "site": "009dc794",
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
    "old": {
      "definition_site": "009dc738",
      "incomplete_value": false,
      "site": "009dc740",
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
            "const:d38:8"
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
      "definition_site": "009dc7b8",
      "incomplete_value": true,
      "site": "009dc7b8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a4000:8"
              ],
              [
                "leaf",
                "const:a9b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009dc764",
      "incomplete_value": true,
      "site": "009dc764",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a4000:8"
              ],
              [
                "leaf",
                "const:ae8:8"
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
      "definition_site": "009dca5c",
      "incomplete_value": true,
      "site": "009dca60",
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
      "definition_site": "009dca08",
      "incomplete_value": true,
      "site": "009dca0c",
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
    "ordinal": 69,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009dc794",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "009dc7ac",
      "READ",
      [
        "storage",
        "002a4ae8",
        null,
        "string"
      ]
    ],
    [
      "009dc840",
      "READ",
      [
        "storage",
        "002c4030",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "009dc794",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ],
    [
      "009dc7ac",
      "READ",
      [
        "storage",
        "002a4a9b",
        null,
        "string"
      ]
    ],
    [
      "009dc840",
      "READ",
      [
        "storage",
        "002c4070",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009dc730`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dc/009dc6f0.md#insn-009dc730) · [`009dc738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dc/009dc6f0.md#insn-009dc738) · [`009dc754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dc/009dc6f0.md#insn-009dc754)
- 新版 [`009dc784`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dc/009dc744.md#insn-009dc784) · [`009dc78c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dc/009dc744.md#insn-009dc78c) · [`009dc7a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dc/009dc744.md#insn-009dc7a8)

~~~diff
- 009dc730 ["INT_ADD", "register:40f0:8", ["const:9dc730:8", "const:4:8"]]
- 009dc730 ["CALL", null, ["callee:00487e60:8"]]
+ 009dc784 ["INT_ADD", "register:40f0:8", ["const:9dc784:8", "const:4:8"]]
+ 009dc784 ["CALL", null, ["callee:00487e60:8"]]
- 009dc730 bytes bcadea97
+ 009dc784 bytes b7adea97
- 009dc738 ["COPY", "tmp:0:8", ["const:d38:8"]]
- 009dc738 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009dc738 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009dc738 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009dc78c ["COPY", "tmp:0:8", ["const:e08:8"]]
+ 009dc78c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009dc78c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009dc78c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009dc738 bytes 08e13491
+ 009dc78c bytes 08213891
- 009dc754 ["COPY", "tmp:0:8", ["const:ae8:8"]]
- 009dc754 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009dc754 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009dc754 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009dc7a8 ["COPY", "tmp:0:8", ["const:a9b:8"]]
+ 009dc7a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009dc7a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009dc7a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009dc754 bytes 08a12b91
+ 009dc7a8 bytes 086d2a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2944c0e00fc1ca3888b3d6bdb8a5e7eb"></a>

### [`009dcb64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dc/009dcb64.md) → [`009dcbb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dc/009dcbb8.md) FUN_009dcbb8

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00b28f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b28/00b28f54.md) · 呼出先 11件 [`0048791c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048791c.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md) [`00488558`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488558.md) [`00488658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488658.md)
- 新版 呼出元 1件 [`00b28ff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b28/00b28ff0.md) · 呼出先 11件 [`0048795c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048795c.md) [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md) [`00487e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487e60.md) [`00488598`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/00488598.md) [`00488698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/00488698.md)

変更の種類 comparison, comparison_count, constant, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 90.96% / 新版 90.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009dcbf8",
      "incomplete_value": false,
      "site": "009dcc00",
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
    "old": {
      "definition_site": "009dcba4",
      "incomplete_value": false,
      "site": "009dcbac",
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
            "const:d38:8"
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
      "definition_site": "009dcc20",
      "incomplete_value": true,
      "site": "009dcc20",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ac000:8"
              ],
              [
                "leaf",
                "const:da3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009dcbcc",
      "incomplete_value": true,
      "site": "009dcbcc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ac000:8"
              ],
              [
                "leaf",
                "const:dff:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "009dcd50"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009dcc00",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "009dcc14",
      "READ",
      [
        "storage",
        "002acdff",
        null,
        "string"
      ]
    ],
    [
      "009dcc58",
      "READ",
      [
        "storage",
        "002c4030",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "009dcc00",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ],
    [
      "009dcc14",
      "READ",
      [
        "storage",
        "002acda3",
        null,
        "string"
      ]
    ],
    [
      "009dcc58",
      "READ",
      [
        "storage",
        "002c4070",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009dcd50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dc/009dcb64.md#insn-009dcd50) · [`009dcd54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dc/009dcb64.md#insn-009dcd54) · [`009dcd60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dc/009dcb64.md#insn-009dcd60)

~~~diff
- 009dcd50 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 009dcd50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 009dcd50 bytes e80f00f9
- 009dcd54 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:60:8"]]
- 009dcd54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 009dcd54 bytes e93300f9
- 009dcd60 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 009dcd60 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 009dcd60 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 009dcd60 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
- 009dcd60 bytes 696a28f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-533e9519733a6a02becc1c4720f8790c"></a>

### [`009dcfd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dc/009dcfd8.md) → [`009dd02c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dd/009dd02c.md) FUN_009dd02c

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`007562a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00756/007562a4.md) [`0082ccfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082c/0082ccfc.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`0085bb70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085bb70.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`007562fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00756/007562fc.md) [`0082cd54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082c/0082cd54.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`0085bbc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085b/0085bbc8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 87.27% / 新版 87.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_destination` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "009dd068",
      "incomplete_value": true,
      "site": "009dd068",
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
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009dd014",
      "incomplete_value": true,
      "site": "009dd014",
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
            "const:968:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009dd05c",
      "incomplete_value": true,
      "site": "009dd068",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:a78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009dd008",
      "incomplete_value": true,
      "site": "009dd014",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:978:8"
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
    "kind": "store_destination",
    "new": {
      "definition_site": "009dd06c",
      "incomplete_value": true,
      "site": "009dd06c",
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
            "const:a78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009dd018",
      "incomplete_value": true,
      "site": "009dd018",
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
            "const:978:8"
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
      "009dd05c",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "009dd060",
      "READ",
      [
        "storage",
        "00ca4968",
        null,
        "undefined8"
      ]
    ],
    [
      "009dd068",
      "WRITE",
      [
        "storage",
        "00ca4968",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "009dd05c",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "009dd060",
      "READ",
      [
        "storage",
        "00ca4a68",
        null,
        "undefined8"
      ]
    ],
    [
      "009dd068",
      "WRITE",
      [
        "storage",
        "00ca4a68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009dd014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dc/009dcfd8.md#insn-009dd014) · [`009dd018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dc/009dcfd8.md#insn-009dd018) · [`009dd028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dc/009dcfd8.md#insn-009dd028)
- 新版 [`009dd068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dd/009dd02c.md#insn-009dd068) · [`009dd06c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dd/009dd02c.md#insn-009dd06c) · [`009dd07c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dd/009dd02c.md#insn-009dd07c)

~~~diff
- 009dd014 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:968:8"]]
- 009dd014 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 009dd068 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a68:8"]]
+ 009dd068 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 009dd014 bytes 09b504f9
+ 009dd068 bytes 093505f9
- 009dd018 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:978:8"]]
- 009dd018 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 009dd06c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a78:8"]]
+ 009dd06c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 009dd018 bytes aabe04f9
+ 009dd06c bytes aa3e05f9
- 009dd028 ["INT_ADD", "register:40f0:8", ["const:9dd028:8", "const:4:8"]]
- 009dd028 ["CALL", null, ["ram:7562a4:8"]]
+ 009dd07c ["INT_ADD", "register:40f0:8", ["const:9dd07c:8", "const:4:8"]]
+ 009dd07c ["CALL", null, ["ram:7562fc:8"]]
- 009dd028 bytes 9fe4f597
+ 009dd07c bytes a0e4f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d232f27ed7a778a6c549083e17cd8eab"></a>

### [`009dd0f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dd/009dd0f0.md) → [`009dd144`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dd/009dd144.md) FUN_009dd144

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`009d5cf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d5/009d5cf8.md) [`009d7a2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d7/009d7a2c.md) [`00a1a750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a750.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 3件 [`009d5d4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d5/009d5d4c.md) [`009d7a80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d7/009d7a80.md) [`00a1a7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a1a/00a1a7a4.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "009dd150",
      "incomplete_value": false,
      "site": "009dd154",
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
      "definition_site": "009dd0fc",
      "incomplete_value": false,
      "site": "009dd100",
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
      "009dd150",
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
      "009dd150",
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

- 旧版 [`009dd100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dd/009dd0f0.md#insn-009dd100) · [`009dd0fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dd/009dd0f0.md#insn-009dd0fc)
- 新版 [`009dd154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dd/009dd144.md#insn-009dd154) · [`009dd150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dd/009dd144.md#insn-009dd150)

~~~diff
- 009dd100 ["INT_ADD", "register:40f0:8", ["const:9dd100:8", "const:4:8"]]
- 009dd100 ["CALL", null, ["callee:0043b7b8:8"]]
+ 009dd154 ["INT_ADD", "register:40f0:8", ["const:9dd154:8", "const:4:8"]]
+ 009dd154 ["CALL", null, ["callee:0043b7b8:8"]]
- 009dd100 bytes 9e79e997
+ 009dd154 bytes 9979e997
- 009dd0fc ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 009dd0fc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 009dd0fc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 009dd0fc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 009dd150 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 009dd150 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 009dd150 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 009dd150 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 009dd0fc bytes 00303d91
+ 009dd150 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aff725572e2dfead7755a79c7444cb48"></a>

### [`009dd104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dd/009dd104.md) → [`009dd158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dd/009dd158.md) FUN_009dd158

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`009d992c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d9/009d992c.md) [`009dd104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dd/009dd104.md) [`00a47f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47f00.md) · 呼出先 22件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)
- 新版 呼出元 3件 [`009d9980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d9/009d9980.md) [`009dd158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dd/009dd158.md) [`00a47f54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a47/00a47f54.md) · 呼出先 22件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) [`00441d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441d2c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.50% / 新版 98.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009dd2b4",
      "incomplete_value": false,
      "site": "009dd2bc",
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
            "const:f93:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009dd260",
      "incomplete_value": false,
      "site": "009dd268",
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
            "const:f53:8"
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
      "definition_site": "009dd40c",
      "incomplete_value": false,
      "site": "009dd414",
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
            "const:e27:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009dd3b8",
      "incomplete_value": false,
      "site": "009dd3c0",
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
            "const:de7:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009dd424",
      "incomplete_value": false,
      "site": "009dd430",
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
            "const:f29:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009dd3d0",
      "incomplete_value": false,
      "site": "009dd3dc",
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
            "const:ee9:8"
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
      "009dd2b4",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "009dd2d8",
      "PARAM",
      [
        "storage",
        "002c0ee9",
        null,
        "string"
      ]
    ],
    [
      "009dd40c",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009dd2b4",
      "PARAM",
      [
        "storage",
        "002b7f93",
        null,
        null
      ]
    ],
    [
      "009dd2d8",
      "PARAM",
      [
        "storage",
        "002c0f29",
        null,
        "string"
      ]
    ],
    [
      "009dd40c",
      "PARAM",
      [
        "storage",
        "002b5e27",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009dd268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dd/009dd104.md#insn-009dd268) · [`009dd3c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dd/009dd104.md#insn-009dd3c0) · [`009dd3dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dd/009dd104.md#insn-009dd3dc)
- 新版 [`009dd2bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dd/009dd158.md#insn-009dd2bc) · [`009dd414`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dd/009dd158.md#insn-009dd414) · [`009dd430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dd/009dd158.md#insn-009dd430)

~~~diff
- 009dd268 ["INT_ADD", "register:40f0:8", ["const:9dd268:8", "const:4:8"]]
- 009dd268 ["CALL", null, ["callee:00441ed4:8"]]
+ 009dd2bc ["INT_ADD", "register:40f0:8", ["const:9dd2bc:8", "const:4:8"]]
+ 009dd2bc ["CALL", null, ["callee:00441ed4:8"]]
- 009dd268 bytes 0b93e997
+ 009dd2bc bytes 0693e997
- 009dd3c0 ["INT_ADD", "register:40f0:8", ["const:9dd3c0:8", "const:4:8"]]
- 009dd3c0 ["CALL", null, ["callee:00441ed4:8"]]
+ 009dd414 ["INT_ADD", "register:40f0:8", ["const:9dd414:8", "const:4:8"]]
+ 009dd414 ["CALL", null, ["callee:00441ed4:8"]]
- 009dd3c0 bytes b592e997
+ 009dd414 bytes b092e997
- 009dd3dc ["INT_ADD", "register:40f0:8", ["const:9dd3dc:8", "const:4:8"]]
- 009dd3dc ["CALL", null, ["callee:00442834:8"]]
+ 009dd430 ["INT_ADD", "register:40f0:8", ["const:9dd430:8", "const:4:8"]]
+ 009dd430 ["CALL", null, ["callee:00442834:8"]]
- 009dd3dc bytes 0695e997
+ 009dd430 bytes 0195e997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f4569a5890d4e1ce63b2611a3c3f134"></a>

### [`009dd91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dd/009dd91c.md) → [`009dd970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dd/009dd970.md) FUN_009dd970

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`009d7fe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d7/009d7fe8.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 1件 [`009d803c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d8/009d803c.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "009dd97c",
      "incomplete_value": false,
      "site": "009dd980",
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
      "definition_site": "009dd928",
      "incomplete_value": false,
      "site": "009dd92c",
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
      "009dd97c",
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
      "009dd97c",
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

- 旧版 [`009dd92c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dd/009dd91c.md#insn-009dd92c) · [`009dd928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dd/009dd91c.md#insn-009dd928)
- 新版 [`009dd980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dd/009dd970.md#insn-009dd980) · [`009dd97c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dd/009dd970.md#insn-009dd97c)

~~~diff
- 009dd92c ["INT_ADD", "register:40f0:8", ["const:9dd92c:8", "const:4:8"]]
- 009dd92c ["CALL", null, ["callee:0043b7b8:8"]]
+ 009dd980 ["INT_ADD", "register:40f0:8", ["const:9dd980:8", "const:4:8"]]
+ 009dd980 ["CALL", null, ["callee:0043b7b8:8"]]
- 009dd92c bytes 9377e997
+ 009dd980 bytes 8e77e997
- 009dd928 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 009dd928 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 009dd928 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 009dd928 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 009dd97c ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 009dd97c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 009dd97c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 009dd97c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 009dd928 bytes 00303d91
+ 009dd97c bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b59ade99c8e68a6d41dfe0692f7344ff"></a>

### [`009dd930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dd/009dd930.md) → [`009dd984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dd/009dd984.md) FUN_009dd984

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`009d7fe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d7/009d7fe8.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 1件 [`009d803c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d8/009d803c.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "009dd990",
      "incomplete_value": false,
      "site": "009dd994",
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
      "definition_site": "009dd93c",
      "incomplete_value": false,
      "site": "009dd940",
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
      "009dd990",
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
      "009dd990",
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

- 旧版 [`009dd940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dd/009dd930.md#insn-009dd940) · [`009dd93c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dd/009dd930.md#insn-009dd93c)
- 新版 [`009dd994`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dd/009dd984.md#insn-009dd994) · [`009dd990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dd/009dd984.md#insn-009dd990)

~~~diff
- 009dd940 ["INT_ADD", "register:40f0:8", ["const:9dd940:8", "const:4:8"]]
- 009dd940 ["CALL", null, ["callee:0043b7b8:8"]]
+ 009dd994 ["INT_ADD", "register:40f0:8", ["const:9dd994:8", "const:4:8"]]
+ 009dd994 ["CALL", null, ["callee:0043b7b8:8"]]
- 009dd940 bytes 8e77e997
+ 009dd994 bytes 8977e997
- 009dd93c ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 009dd93c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 009dd93c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 009dd93c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 009dd990 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 009dd990 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 009dd990 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 009dd990 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 009dd93c bytes 00303d91
+ 009dd990 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca52605f4d88fabd597b1b513e66fbd3"></a>

### [`009dd944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dd/009dd944.md) → [`009dd998`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dd/009dd998.md) _INIT_202

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.70% / 新版 88.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009dda38",
      "incomplete_value": true,
      "site": "009dda50",
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
                "const:2a2000:8"
              ],
              [
                "leaf",
                "const:f15:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009dd9e4",
      "incomplete_value": true,
      "site": "009dd9fc",
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
                "const:2a2000:8"
              ],
              [
                "leaf",
                "const:f62:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009dda54",
      "incomplete_value": true,
      "site": "009dda70",
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
                "const:2ac000:8"
              ],
              [
                "leaf",
                "const:576:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009dda00",
      "incomplete_value": true,
      "site": "009dda1c",
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
                "const:2ac000:8"
              ],
              [
                "leaf",
                "const:5d2:8"
              ]
            ]
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
      "definition_site": "009dda74",
      "incomplete_value": true,
      "site": "009dda90",
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
                "const:2a0000:8"
              ],
              [
                "leaf",
                "const:f10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009dda20",
      "incomplete_value": true,
      "site": "009dda3c",
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
                "const:2a0000:8"
              ],
              [
                "leaf",
                "const:f5d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 24,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009dd9d4",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "009dd9f8",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "009dda18",
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
      "009dd9d4",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "009dd9f8",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "009dda18",
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

- 旧版 [`009ddb78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dd/009dd944.md#insn-009ddb78) · [`009dd970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dd/009dd944.md#insn-009dd970) · [`009dd978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dd/009dd944.md#insn-009dd978)
- 新版 [`009ddbcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dd/009dd998.md#insn-009ddbcc) · [`009dd9c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dd/009dd998.md#insn-009dd9c4)

~~~diff
- 009ddb78 ["INT_ADD", "register:40f0:8", ["const:9ddb78:8", "const:4:8"]]
- 009ddb78 ["CALL", null, ["callee:00c57f00:8"]]
+ 009ddbcc ["INT_ADD", "register:40f0:8", ["const:9ddbcc:8", "const:4:8"]]
+ 009ddbcc ["CALL", null, ["callee:00c57f00:8"]]
- 009ddb78 bytes aee80994
+ 009ddbcc bytes cde80994
- 009dd970 ["COPY", "tmp:0:8", ["const:cf0:8"]]
- 009dd970 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 009dd970 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 009dd970 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 009dd9c4 ["COPY", "tmp:0:8", ["const:df0:8"]]
+ 009dd9c4 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 009dd9c4 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 009dd9c4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 009dd970 bytes 73c23391
+ 009dd9c4 bytes 73c23791
- 009dd978 ["COPY", "register:4048:8", ["const:2b7000:8"]]
- 009dd978 bytes c9c6ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b42a68290f86d847e9543a9b05e83614"></a>

### [`009ddce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dd/009ddce0.md) → [`009ddd34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dd/009ddd34.md) FUN_009ddd34

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00b28f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b28/00b28f54.md) · 呼出先 18件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0048791c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048791c.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md)
- 新版 呼出元 1件 [`00b28ff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b28/00b28ff0.md) · 呼出先 18件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`0048795c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048795c.md) [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 91.00% / 新版 91.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 7件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009ddd74",
      "incomplete_value": false,
      "site": "009ddd80",
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
    "old": {
      "definition_site": "009ddd20",
      "incomplete_value": false,
      "site": "009ddd2c",
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
            "const:d38:8"
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
      "definition_site": "009ddda8",
      "incomplete_value": true,
      "site": "009dddb8",
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
                "const:699:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ddd54",
      "incomplete_value": true,
      "site": "009ddd64",
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
                "const:6e6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009dddbc",
      "incomplete_value": true,
      "site": "009dddbc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "009ddd68",
      "incomplete_value": true,
      "site": "009ddd68",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 19,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009ddd80",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "009ddda8",
      "READ",
      [
        "storage",
        "0029f6e6",
        null,
        "string"
      ]
    ],
    [
      "009dddac",
      "READ",
      [
        "storage",
        "0029f6f5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009ddd80",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ],
    [
      "009ddda8",
      "READ",
      [
        "storage",
        "0029f699",
        null,
        "string"
      ]
    ],
    [
      "009dddac",
      "READ",
      [
        "storage",
        "0029f6a8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009ddd14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dd/009ddce0.md#insn-009ddd14) · [`009dddc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dd/009ddce0.md#insn-009dddc0) · [`009ddd20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dd/009ddce0.md#insn-009ddd20)
- 新版 [`009ddd68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dd/009ddd34.md#insn-009ddd68) · [`009dde14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dd/009ddd34.md#insn-009dde14) · [`009ddd74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dd/009ddd34.md#insn-009ddd74)

~~~diff
- 009ddd14 ["INT_ADD", "register:40f0:8", ["const:9ddd14:8", "const:4:8"]]
- 009ddd14 ["CALL", null, ["callee:00487e60:8"]]
+ 009ddd68 ["INT_ADD", "register:40f0:8", ["const:9ddd68:8", "const:4:8"]]
+ 009ddd68 ["CALL", null, ["callee:00487e60:8"]]
- 009ddd14 bytes 43a8ea97
+ 009ddd68 bytes 3ea8ea97
- 009dddc0 ["INT_ADD", "register:40f0:8", ["const:9dddc0:8", "const:4:8"]]
- 009dddc0 ["CALL", null, ["callee:00487bc0:8"]]
+ 009dde14 ["INT_ADD", "register:40f0:8", ["const:9dde14:8", "const:4:8"]]
+ 009dde14 ["CALL", null, ["callee:00487bc0:8"]]
- 009dddc0 bytes 70a7ea97
+ 009dde14 bytes 6ba7ea97
- 009ddd20 ["COPY", "tmp:0:8", ["const:d38:8"]]
- 009ddd20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009ddd20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009ddd20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009ddd74 ["COPY", "tmp:0:8", ["const:e08:8"]]
+ 009ddd74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009ddd74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009ddd74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009ddd20 bytes 08e13491
+ 009ddd74 bytes 08213891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f14ec3a8bf65d1d17132c8c8487bfe43"></a>

### [`009de080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009de/009de080.md) → [`009de0d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009de/009de0d4.md) FUN_009de0d4

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a87ad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a87/00a87ad0.md) · 呼出先 3件 [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00a87b40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a87/00a87b40.md) · 呼出先 3件 [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`0048cec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cec4.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.15% / 新版 96.15%

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
      "site": "009de0f8",
      "value": [
        "leaf",
        "ram:48cd38:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009de0a4",
      "value": [
        "leaf",
        "ram:48ccf8:8"
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
      "009de0f8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ]
  ],
  "added": [
    [
      "009de0f8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009de0a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009de/009de080.md#insn-009de0a4) · [`009de0a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009de/009de080.md#insn-009de0a8) · [`009de0bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009de/009de080.md#insn-009de0bc)
- 新版 [`009de0f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009de/009de0d4.md#insn-009de0f8) · [`009de0fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009de/009de0d4.md#insn-009de0fc) · [`009de110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009de/009de0d4.md#insn-009de110)

~~~diff
- 009de0a4 ["INT_ADD", "register:40f0:8", ["const:9de0a4:8", "const:4:8"]]
- 009de0a4 ["CALL", null, ["ram:48ccf8:8"]]
+ 009de0f8 ["INT_ADD", "register:40f0:8", ["const:9de0f8:8", "const:4:8"]]
+ 009de0f8 ["CALL", null, ["ram:48cd38:8"]]
- 009de0a4 bytes 15bbea97
+ 009de0f8 bytes 10bbea97
- 009de0a8 ["INT_ADD", "register:40f0:8", ["const:9de0a8:8", "const:4:8"]]
- 009de0a8 ["CALL", null, ["callee:0048cec4:8"]]
+ 009de0fc ["INT_ADD", "register:40f0:8", ["const:9de0fc:8", "const:4:8"]]
+ 009de0fc ["CALL", null, ["callee:0048cec4:8"]]
- 009de0a8 bytes 77bbea97
+ 009de0fc bytes 72bbea97
- 009de0bc ["INT_ADD", "register:40f0:8", ["const:9de0bc:8", "const:4:8"]]
- 009de0bc ["CALL", null, ["callee:00851550:8"]]
+ 009de110 ["INT_ADD", "register:40f0:8", ["const:9de110:8", "const:4:8"]]
+ 009de110 ["CALL", null, ["callee:00851550:8"]]
- 009de0bc bytes 0fcdf997
+ 009de110 bytes 10cdf997
~~~


<a id="compare-f518b01dc0c8f43cb2fc66acf00f6974"></a>

### [`009de610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009de/009de610.md) → [`009de664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009de/009de664.md) FUN_009de664

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`006bbc98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006bb/006bbc98.md) [`007dd364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007dd/007dd364.md) · 呼出先 3件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00a84bf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a84/00a84bf0.md) [`00a84d88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a84/00a84d88.md)
- 新版 呼出元 2件 [`006bbcf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bb/006bbcf0.md) [`007dd3bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007dd/007dd3bc.md) · 呼出先 3件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00a84c60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a84/00a84c60.md) [`00a84df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a84/00a84df8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 91.67% / 新版 91.67%

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
      "site": "009de690",
      "value": [
        "leaf",
        "ram:a84df8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009de63c",
      "value": [
        "leaf",
        "ram:a84d88:8"
      ]
    },
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009de6ac",
      "value": [
        "leaf",
        "ram:a84df8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009de658",
      "value": [
        "leaf",
        "ram:a84d88:8"
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
      "009de690",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a84d88"
      ]
    ],
    [
      "009de6ac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a84d88"
      ]
    ]
  ],
  "added": [
    [
      "009de690",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a84df8"
      ]
    ],
    [
      "009de6ac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a84df8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009de63c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009de/009de610.md#insn-009de63c) · [`009de658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009de/009de610.md#insn-009de658) · [`009de62c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009de/009de610.md#insn-009de62c)
- 新版 [`009de690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009de/009de664.md#insn-009de690) · [`009de6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009de/009de664.md#insn-009de6ac) · [`009de680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009de/009de664.md#insn-009de680)

~~~diff
- 009de63c ["INT_ADD", "register:40f0:8", ["const:9de63c:8", "const:4:8"]]
- 009de63c ["CALL", null, ["ram:a84d88:8"]]
+ 009de690 ["INT_ADD", "register:40f0:8", ["const:9de690:8", "const:4:8"]]
+ 009de690 ["CALL", null, ["ram:a84df8:8"]]
- 009de63c bytes d3990294
+ 009de690 bytes da990294
- 009de658 ["INT_ADD", "register:40f0:8", ["const:9de658:8", "const:4:8"]]
- 009de658 ["CALL", null, ["ram:a84d88:8"]]
+ 009de6ac ["INT_ADD", "register:40f0:8", ["const:9de6ac:8", "const:4:8"]]
+ 009de6ac ["CALL", null, ["ram:a84df8:8"]]
- 009de658 bytes cc990294
+ 009de6ac bytes d3990294
- 009de62c ["INT_ADD", "register:40f0:8", ["const:9de62c:8", "const:4:8"]]
- 009de62c ["CALL", null, ["callee:00851550:8"]]
+ 009de680 ["INT_ADD", "register:40f0:8", ["const:9de680:8", "const:4:8"]]
+ 009de680 ["CALL", null, ["callee:00851550:8"]]
- 009de62c bytes b3cbf997
+ 009de680 bytes b4cbf997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a74088caacf293ae1295ecc19b4af3a7"></a>

### [`009de890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009de/009de890.md) → [`009de8e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009de/009de8e4.md) _INIT_203

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 82.49% / 新版 82.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 3件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009de920",
      "incomplete_value": true,
      "site": "009de93c",
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
      "definition_site": "009de8cc",
      "incomplete_value": true,
      "site": "009de8e8",
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
      "definition_site": "009de944",
      "incomplete_value": true,
      "site": "009de960",
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
      "definition_site": "009de8f0",
      "incomplete_value": true,
      "site": "009de90c",
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
      "definition_site": "009de964",
      "incomplete_value": true,
      "site": "009de980",
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
      "definition_site": "009de910",
      "incomplete_value": true,
      "site": "009de92c",
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
      "009de920",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "009de944",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "009de964",
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
      "009de920",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "009de944",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "009de964",
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

- 旧版 [`009de984`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009de/009de890.md#insn-009de984) · [`009de9f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009de/009de890.md#insn-009de9f0) · [`009dea2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009de/009de890.md#insn-009dea2c)
- 新版 [`009de9d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009de/009de8e4.md#insn-009de9d8) · [`009dea44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009de/009de8e4.md#insn-009dea44) · [`009dea80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009de/009de8e4.md#insn-009dea80)

~~~diff
- 009de984 ["COPY", "tmp:0:8", ["const:f09:8"]]
- 009de984 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 009de984 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 009de984 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 009de9d8 ["COPY", "tmp:0:8", ["const:ebc:8"]]
+ 009de9d8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 009de9d8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 009de9d8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 009de984 bytes 29253c91
+ 009de9d8 bytes 29f13a91
- 009de9f0 ["INT_ADD", "register:40f0:8", ["const:9de9f0:8", "const:4:8"]]
- 009de9f0 ["CALL", null, ["callee:0043b838:8"]]
+ 009dea44 ["INT_ADD", "register:40f0:8", ["const:9dea44:8", "const:4:8"]]
+ 009dea44 ["CALL", null, ["callee:0043b838:8"]]
- 009de9f0 bytes 8273e997
+ 009dea44 bytes 7d73e997
- 009dea2c ["INT_ADD", "register:40f0:8", ["const:9dea2c:8", "const:4:8"]]
- 009dea2c ["CALL", null, ["callee:0043b838:8"]]
+ 009dea80 ["INT_ADD", "register:40f0:8", ["const:9dea80:8", "const:4:8"]]
+ 009dea80 ["CALL", null, ["callee:0043b838:8"]]
- 009dea2c bytes 7373e997
+ 009dea80 bytes 6e73e997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c6a1b819c5291d7f24893a0ea208c39b"></a>

### [`009df8ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009df/009df8ec.md) → [`009df940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009df/009df940.md) FUN_009df940

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 11件 [`00606ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00606/00606ae4.md) [`0093b770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093b/0093b770.md) [`009dfa9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009df/009dfa9c.md) [`009e1278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e1/009e1278.md) [`009e33b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e3/009e33b8.md) · 呼出先 8件 [`0046dad4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046dad4.md) [`0066506c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00665/0066506c.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`009365c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00936/009365c4.md) [`009df668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009df/009df668.md)
- 新版 呼出元 11件 [`00606b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00606/00606b24.md) [`0093b7c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0093b/0093b7c4.md) [`009dfaf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009df/009dfaf0.md) [`009e12cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e1/009e12cc.md) [`009e340c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e3/009e340c.md) · 呼出先 8件 [`0046db14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046db14.md) [`006650ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00665/006650ac.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00936618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00936/00936618.md) [`009df6bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009df/009df6bc.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.72% / 新版 90.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009dfa00",
      "incomplete_value": true,
      "site": "009dfa10",
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
                "const:2b6000:8"
              ],
              [
                "leaf",
                "const:983:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009df9ac",
      "incomplete_value": true,
      "site": "009df9bc",
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
                "const:2b6000:8"
              ],
              [
                "leaf",
                "const:943:8"
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
      "definition_site": "009dfa04",
      "incomplete_value": true,
      "site": "009dfa14",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009df9b0",
      "incomplete_value": true,
      "site": "009df9c0",
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
                "const:e:8"
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
      "definition_site": "009dfa08",
      "incomplete_value": true,
      "site": "009dfa18",
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
                "const:470:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009df9b4",
      "incomplete_value": true,
      "site": "009df9c4",
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
      "009dfa00",
      "READ",
      [
        "storage",
        "002b6943",
        null,
        "string"
      ]
    ],
    [
      "009dfa04",
      "READ",
      [
        "storage",
        "002b6951",
        null,
        "string"
      ]
    ],
    [
      "009dfa08",
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
      "009dfa00",
      "READ",
      [
        "storage",
        "002b6983",
        null,
        "string"
      ]
    ],
    [
      "009dfa04",
      "READ",
      [
        "storage",
        "002b6991",
        null,
        "string"
      ]
    ],
    [
      "009dfa08",
      "READ",
      [
        "storage",
        "002c2470",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009dfa24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009df/009df8ec.md#insn-009dfa24) · [`009df920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009df/009df8ec.md#insn-009df920) · [`009df930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009df/009df8ec.md#insn-009df930)
- 新版 [`009dfa78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009df/009df940.md#insn-009dfa78) · [`009df974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009df/009df940.md#insn-009df974) · [`009df984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009df/009df940.md#insn-009df984)

~~~diff
- 009dfa24 ["INT_ADD", "register:40f0:8", ["const:9dfa24:8", "const:4:8"]]
- 009dfa24 ["CALL", null, ["ram:66506c:8"]]
+ 009dfa78 ["INT_ADD", "register:40f0:8", ["const:9dfa78:8", "const:4:8"]]
+ 009dfa78 ["CALL", null, ["ram:6650ac:8"]]
- 009dfa24 bytes 9215f297
+ 009dfa78 bytes 8d15f297
- 009df920 ["INT_ADD", "register:40f0:8", ["const:9df920:8", "const:4:8"]]
- 009df920 ["CALL", null, ["callee:009df6bc:8"]]
+ 009df974 ["INT_ADD", "register:40f0:8", ["const:9df974:8", "const:4:8"]]
+ 009df974 ["CALL", null, ["callee:009df6bc:8"]]
- 009df920 bytes 52ffff97
+ 009df974 bytes 52ffff97
- 009df930 ["INT_ADD", "register:40f0:8", ["const:9df930:8", "const:4:8"]]
- 009df930 ["CALL", null, ["callee:00851550:8"]]
+ 009df984 ["INT_ADD", "register:40f0:8", ["const:9df984:8", "const:4:8"]]
+ 009df984 ["CALL", null, ["callee:00851550:8"]]
- 009df930 bytes f2c6f997
+ 009df984 bytes f3c6f997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24bfce31c9e4f239c95e6b3ce4355865"></a>

### [`009dfb18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009df/009dfb18.md) → [`009dfb6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009df/009dfb6c.md) FUN_009dfb6c

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`00658bec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00658/00658bec.md) [`00658dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00658/00658dac.md) [`0065ad40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065a/0065ad40.md) [`009dfdac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009df/009dfdac.md) [`00a47f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47f00.md) · 呼出先 7件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00688178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00688/00688178.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 5件 [`00658c2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00658/00658c2c.md) [`00658dec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00658/00658dec.md) [`0065ad80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0065a/0065ad80.md) [`009dfe00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009df/009dfe00.md) [`00a47f54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a47/00a47f54.md) · 呼出先 7件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`006881b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00688/006881b8.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.65% / 新版 98.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009dfb9c",
      "incomplete_value": true,
      "site": "009dfbc0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:120:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009dfb48",
      "incomplete_value": true,
      "site": "009dfb6c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009dfb9c",
      "READ",
      [
        "storage",
        "002c40e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "009dfb9c",
      "READ",
      [
        "storage",
        "002c4120",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009dfb48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009df/009dfb18.md#insn-009dfb48) · [`009dfb70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009df/009dfb18.md#insn-009dfb70) · [`009dfb88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009df/009dfb18.md#insn-009dfb88)
- 新版 [`009dfb9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009df/009dfb6c.md#insn-009dfb9c) · [`009dfbc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009df/009dfb6c.md#insn-009dfbc4) · [`009dfbdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009df/009dfb6c.md#insn-009dfbdc)

~~~diff
- 009dfb48 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e0:8"]]
- 009dfb48 ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
- 009dfb48 ["COPY", "register:5008:8", ["const:0:8"]]
- 009dfb48 ["COPY", "register:5010:8", ["const:0:8"]]
+ 009dfb9c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:120:8"]]
+ 009dfb9c ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
+ 009dfb9c ["COPY", "register:5008:8", ["const:0:8"]]
+ 009dfb9c ["COPY", "register:5010:8", ["const:0:8"]]
- 009dfb48 bytes 007140fd
+ 009dfb9c bytes 009140fd
- 009dfb70 ["INT_ADD", "register:40f0:8", ["const:9dfb70:8", "const:4:8"]]
- 009dfb70 ["CALL", null, ["callee:006881b8:8"]]
+ 009dfbc4 ["INT_ADD", "register:40f0:8", ["const:9dfbc4:8", "const:4:8"]]
+ 009dfbc4 ["CALL", null, ["callee:006881b8:8"]]
- 009dfb70 bytes 82a1f297
+ 009dfbc4 bytes 7da1f297
- 009dfb88 ["INT_ADD", "register:40f0:8", ["const:9dfb88:8", "const:4:8"]]
- 009dfb88 ["CALL", null, ["callee:00c53d70:8"]]
+ 009dfbdc ["INT_ADD", "register:40f0:8", ["const:9dfbdc:8", "const:4:8"]]
+ 009dfbdc ["CALL", null, ["callee:00c53d70:8"]]
- 009dfb88 bytes 52d00994
+ 009dfbdc bytes 65d00994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56d9a48945449e4ca0cf1a9a46912b2a"></a>

### [`009e01d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e0/009e01d4.md) → [`009e0228`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e0/009e0228.md) FUN_009e0228

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0084e59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0084e/0084e59c.md) · 呼出先 7件 [`0086aadc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086aadc.md) [`009e650c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e6/009e650c.md) [`009e6510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e6/009e6510.md) [`009f2604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2604.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)
- 新版 呼出元 1件 [`0084e5f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0084e/0084e5f4.md) · 呼出先 7件 [`0086ab34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086ab34.md) [`009e6560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e6560.md) [`009e6564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e6564.md) [`009f2658`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2658.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.37% / 新版 97.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009e0270",
      "incomplete_value": false,
      "site": "009e0278",
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
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e021c",
      "incomplete_value": false,
      "site": "009e0224",
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
            "const:c58:8"
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
      "009e0278",
      "DATA",
      [
        "storage",
        "00c89c58",
        null,
        "undefined *"
      ]
    ],
    [
      "009e0320",
      "READ",
      [
        "storage",
        "00c89c78",
        null,
        "pointer"
      ]
    ],
    [
      "009e0320",
      "READ",
      [
        "storage",
        "00c89c80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009e0278",
      "DATA",
      [
        "storage",
        "00c89d28",
        null,
        "undefined *"
      ]
    ],
    [
      "009e0320",
      "READ",
      [
        "storage",
        "00c89d48",
        null,
        "pointer"
      ]
    ],
    [
      "009e0320",
      "READ",
      [
        "storage",
        "00c89d50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e0204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e0/009e01d4.md#insn-009e0204) · [`009e021c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e0/009e01d4.md#insn-009e021c) · [`009e0234`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e0/009e01d4.md#insn-009e0234)
- 新版 [`009e0258`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e0/009e0228.md#insn-009e0258) · [`009e0270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e0/009e0228.md#insn-009e0270) · [`009e0288`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e0/009e0228.md#insn-009e0288)

~~~diff
- 009e0204 ["INT_ADD", "register:40f0:8", ["const:9e0204:8", "const:4:8"]]
- 009e0204 ["CALL", null, ["callee:0086ab34:8"]]
+ 009e0258 ["INT_ADD", "register:40f0:8", ["const:9e0258:8", "const:4:8"]]
+ 009e0258 ["CALL", null, ["callee:0086ab34:8"]]
- 009e0204 bytes 362afa97
+ 009e0258 bytes 372afa97
- 009e021c ["COPY", "tmp:0:8", ["const:c58:8"]]
- 009e021c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009e021c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009e021c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009e0270 ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 009e0270 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009e0270 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009e0270 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009e021c bytes 08613191
+ 009e0270 bytes 08a13491
- 009e0234 ["INT_ADD", "register:40f0:8", ["const:9e0234:8", "const:4:8"]]
- 009e0234 ["CALL", null, ["callee:009f2658:8"]]
+ 009e0288 ["INT_ADD", "register:40f0:8", ["const:9e0288:8", "const:4:8"]]
+ 009e0288 ["CALL", null, ["callee:009f2658:8"]]
- 009e0234 bytes f4480094
+ 009e0288 bytes f4480094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f84b4f9e4f58fcee5321b8f1212ef1a"></a>

### [`009e037c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e0/009e037c.md) → [`009e03d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e0/009e03d0.md) FUN_009e03d0

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`009e0350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e0/009e0350.md) · 呼出先 22件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md)
- 新版 呼出元 1件 [`009e03a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e0/009e03a4.md) · 呼出先 22件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`00487e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487e60.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 95.71% / 新版 95.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 9件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009e0414",
      "incomplete_value": false,
      "site": "009e0420",
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
    "old": {
      "definition_site": "009e03c0",
      "incomplete_value": false,
      "site": "009e03cc",
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
            "const:d38:8"
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
      "definition_site": "009e044c",
      "incomplete_value": true,
      "site": "009e045c",
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
                "const:2c0000:8"
              ],
              [
                "leaf",
                "const:6a4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e03f8",
      "incomplete_value": true,
      "site": "009e0408",
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
                "const:2c0000:8"
              ],
              [
                "leaf",
                "const:664:8"
              ]
            ]
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
      "definition_site": "009e0450",
      "incomplete_value": true,
      "site": "009e0460",
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
                "const:9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e03fc",
      "incomplete_value": true,
      "site": "009e040c",
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
                "const:9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 21,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009e0420",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "009e044c",
      "READ",
      [
        "storage",
        "002c0664",
        null,
        "string"
      ]
    ],
    [
      "009e0450",
      "READ",
      [
        "storage",
        "002c066d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009e0420",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ],
    [
      "009e044c",
      "READ",
      [
        "storage",
        "002c06a4",
        null,
        "string"
      ]
    ],
    [
      "009e0450",
      "READ",
      [
        "storage",
        "002c06ad",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e03b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e0/009e037c.md#insn-009e03b4) · [`009e0464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e0/009e037c.md#insn-009e0464) · [`009e0b24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e0/009e037c.md#insn-009e0b24)
- 新版 [`009e0408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e0/009e03d0.md#insn-009e0408) · [`009e04b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e0/009e03d0.md#insn-009e04b8) · [`009e0b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e0/009e03d0.md#insn-009e0b78)

~~~diff
- 009e03b4 ["INT_ADD", "register:40f0:8", ["const:9e03b4:8", "const:4:8"]]
- 009e03b4 ["CALL", null, ["callee:00487e60:8"]]
+ 009e0408 ["INT_ADD", "register:40f0:8", ["const:9e0408:8", "const:4:8"]]
+ 009e0408 ["CALL", null, ["callee:00487e60:8"]]
- 009e03b4 bytes 9b9eea97
+ 009e0408 bytes 969eea97
- 009e0464 ["INT_ADD", "register:40f0:8", ["const:9e0464:8", "const:4:8"]]
- 009e0464 ["CALL", null, ["callee:00596f6c:8"]]
+ 009e04b8 ["INT_ADD", "register:40f0:8", ["const:9e04b8:8", "const:4:8"]]
+ 009e04b8 ["CALL", null, ["callee:00596f6c:8"]]
- 009e0464 bytes b2daee97
+ 009e04b8 bytes addaee97
- 009e0b24 ["INT_ADD", "register:40f0:8", ["const:9e0b24:8", "const:4:8"]]
- 009e0b24 ["CALL", null, ["callee:00488698:8"]]
+ 009e0b78 ["INT_ADD", "register:40f0:8", ["const:9e0b78:8", "const:4:8"]]
+ 009e0b78 ["CALL", null, ["callee:00488698:8"]]
- 009e0b24 bytes cd9eea97
+ 009e0b78 bytes c89eea97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb3cc5f6708960cf8a0a829c167ef778"></a>

### [`009e470c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e4/009e470c.md) → [`009e4760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e4/009e4760.md) FUN_009e4760

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`009f5ab4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f5/009f5ab4.md) [`00a02be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a02be8.md) · 呼出先 9件 [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`0052dd00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052dd00.md) [`005cd0f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cd/005cd0f0.md)
- 新版 呼出元 2件 [`009f5b08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f5/009f5b08.md) [`00a02c3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a02/00a02c3c.md) · 呼出先 9件 [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`0052dd40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052dd40.md) [`005cd130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cd130.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.62% / 新版 95.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009e47fc",
      "incomplete_value": true,
      "site": "009e480c",
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
                "live",
                "register:4050:8"
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
      "definition_site": "009e47a8",
      "incomplete_value": true,
      "site": "009e47b8",
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
                "live",
                "register:4050:8"
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009e489c",
      "incomplete_value": false,
      "site": "009e48a8",
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
            "const:a21:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e4848",
      "incomplete_value": false,
      "site": "009e4854",
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
            "const:a75:8"
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
      "009e47f4",
      "READ",
      [
        "storage",
        "002beee4",
        null,
        "string"
      ]
    ],
    [
      "009e47f8",
      "READ",
      [
        "storage",
        "002beed4",
        null,
        "string"
      ]
    ],
    [
      "009e47fc",
      "READ",
      [
        "storage",
        "002c22a0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009e47f4",
      "READ",
      [
        "storage",
        "002bee90",
        null,
        "string"
      ]
    ],
    [
      "009e47f8",
      "READ",
      [
        "storage",
        "002bee80",
        null,
        "string"
      ]
    ],
    [
      "009e47fc",
      "READ",
      [
        "storage",
        "002c22e0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e4854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e4/009e470c.md#insn-009e4854) · [`009e4740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e4/009e470c.md#insn-009e4740) · [`009e4754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e4/009e470c.md#insn-009e4754)
- 新版 [`009e48a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e4/009e4760.md#insn-009e48a8) · [`009e4794`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e4/009e4760.md#insn-009e4794) · [`009e47a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e4/009e4760.md#insn-009e47a8)

~~~diff
- 009e4854 ["INT_ADD", "register:40f0:8", ["const:9e4854:8", "const:4:8"]]
- 009e4854 ["CALL", null, ["callee:0060d4a8:8"]]
+ 009e48a8 ["INT_ADD", "register:40f0:8", ["const:9e48a8:8", "const:4:8"]]
+ 009e48a8 ["CALL", null, ["callee:0060d4a8:8"]]
- 009e4854 bytes 05a3f097
+ 009e48a8 bytes 00a3f097
- 009e4740 ["COPY", "register:0:8", ["register:4040:8"]]
- 009e4740 ["INT_ADD", "register:40f0:8", ["const:9e4740:8", "const:4:8"]]
- 009e4740 ["CALLIND", null, ["register:0:8"]]
+ 009e4794 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009e4794 ["INT_ADD", "register:40f0:8", ["const:9e4794:8", "const:4:8"]]
+ 009e4794 ["CALLIND", null, ["register:0:8"]]
- 009e4740 bytes 00013fd6
+ 009e4794 bytes 00013fd6
- 009e4754 ["COPY", "register:0:8", ["register:4040:8"]]
- 009e4754 ["INT_ADD", "register:40f0:8", ["const:9e4754:8", "const:4:8"]]
- 009e4754 ["CALLIND", null, ["register:0:8"]]
+ 009e47a8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009e47a8 ["INT_ADD", "register:40f0:8", ["const:9e47a8:8", "const:4:8"]]
+ 009e47a8 ["CALLIND", null, ["register:0:8"]]
- 009e4754 bytes 00013fd6
+ 009e47a8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b7ca5986683c9cc818cb63973988eb6"></a>

### [`009e4a08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e4/009e4a08.md) → [`009e4a5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e4/009e4a5c.md) FUN_009e4a5c

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 6件 [`00606ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00606/00606ae4.md) [`0061452c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00614/0061452c.md) [`0093b770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093b/0093b770.md) [`009f92c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f9/009f92c8.md) [`009f981c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f9/009f981c.md) · 呼出先 14件 [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`0052dd00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052dd00.md) [`005cd0f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cd/005cd0f0.md)
- 新版 呼出元 6件 [`00606b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00606/00606b24.md) [`0061456c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00614/0061456c.md) [`0093b7c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0093b/0093b7c4.md) [`009f931c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f9/009f931c.md) [`009f9870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f9/009f9870.md) · 呼出先 14件 [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`0052dd40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052dd40.md) [`005cd130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cd/005cd130.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.71% / 新版 92.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 1件, `store_value` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009e4b7c",
      "incomplete_value": true,
      "site": "009e4b7c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:426:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e4b28",
      "incomplete_value": true,
      "site": "009e4b28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:473:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009e4b80",
      "incomplete_value": true,
      "site": "009e4b80",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "009e4b2c",
      "incomplete_value": true,
      "site": "009e4b2c",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 30,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009e4cb8",
      "incomplete_value": true,
      "site": "009e4cc8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "009e4c64",
      "incomplete_value": true,
      "site": "009e4c74",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 38,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009e4b24",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006648a0"
      ]
    ],
    [
      "009e4b6c",
      "READ",
      [
        "storage",
        "002a1473",
        null,
        "string"
      ]
    ],
    [
      "009e4b70",
      "READ",
      [
        "storage",
        "002a1479",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009e4b24",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006648e0"
      ]
    ],
    [
      "009e4b6c",
      "READ",
      [
        "storage",
        "002a1426",
        null,
        "string"
      ]
    ],
    [
      "009e4b70",
      "READ",
      [
        "storage",
        "002a142c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e4ad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e4/009e4a08.md#insn-009e4ad0) · [`009e4d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e4/009e4a08.md#insn-009e4d8c) · [`009e4df4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e4/009e4a08.md#insn-009e4df4)
- 新版 [`009e4b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e4/009e4a5c.md#insn-009e4b24) · [`009e4de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e4/009e4a5c.md#insn-009e4de0) · [`009e4e48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e4/009e4a5c.md#insn-009e4e48)

~~~diff
- 009e4ad0 ["INT_ADD", "register:40f0:8", ["const:9e4ad0:8", "const:4:8"]]
- 009e4ad0 ["CALL", null, ["ram:6648a0:8"]]
+ 009e4b24 ["INT_ADD", "register:40f0:8", ["const:9e4b24:8", "const:4:8"]]
+ 009e4b24 ["CALL", null, ["ram:6648e0:8"]]
- 009e4ad0 bytes 74fff197
+ 009e4b24 bytes 6ffff197
- 009e4d8c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:660:8"]]
- 009e4d8c ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
- 009e4d8c ["COPY", "register:5010:8", ["const:0:8"]]
- 009e4d8c ["COPY", "register:5018:8", ["const:0:8"]]
+ 009e4de0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:6a0:8"]]
+ 009e4de0 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
+ 009e4de0 ["COPY", "register:5010:8", ["const:0:8"]]
+ 009e4de0 ["COPY", "register:5018:8", ["const:0:8"]]
- 009e4d8c bytes 0099c13d
+ 009e4de0 bytes 00a9c13d
- 009e4df4 ["INT_ADD", "register:40f0:8", ["const:9e4df4:8", "const:4:8"]]
- 009e4df4 ["CALL", null, ["callee:0048ce94:8"]]
+ 009e4e48 ["INT_ADD", "register:40f0:8", ["const:9e4e48:8", "const:4:8"]]
+ 009e4e48 ["CALL", null, ["callee:0048ce94:8"]]
- 009e4df4 bytes 18a0ea97
+ 009e4e48 bytes 13a0ea97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-189ce8ff5c995febc69b6e65eafb4b9c"></a>

### [`009e5260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e5/009e5260.md) → [`009e52b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e5/009e52b4.md) FUN_009e52b4

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00a02be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a02be8.md) · 呼出先 11件 [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9858.md) [`008bacc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ba/008bacc8.md) [`009e2f94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e2/009e2f94.md)
- 新版 呼出元 1件 [`00a02c3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a02/00a02c3c.md) · 呼出先 11件 [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b98b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b98b0.md) [`008bad20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ba/008bad20.md) [`009e2fe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e2/009e2fe8.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 85.42% / 新版 85.42%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009e5360",
      "incomplete_value": true,
      "site": "009e5370",
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
                "const:5be:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e530c",
      "incomplete_value": true,
      "site": "009e531c",
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
                "const:58d:8"
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
      "definition_site": "009e5364",
      "incomplete_value": true,
      "site": "009e5374",
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
      "definition_site": "009e5310",
      "incomplete_value": true,
      "site": "009e5320",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009e5368",
      "incomplete_value": true,
      "site": "009e5378",
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
                "const:ad0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e5314",
      "incomplete_value": true,
      "site": "009e5324",
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
      "009e5360",
      "READ",
      [
        "storage",
        "002b558d",
        null,
        "string"
      ]
    ],
    [
      "009e5364",
      "READ",
      [
        "storage",
        "002b5597",
        null,
        "string"
      ]
    ],
    [
      "009e5368",
      "READ",
      [
        "storage",
        "002c2a90",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009e5360",
      "READ",
      [
        "storage",
        "002b55be",
        null,
        "string"
      ]
    ],
    [
      "009e5364",
      "READ",
      [
        "storage",
        "002b55c8",
        null,
        "string"
      ]
    ],
    [
      "009e5368",
      "READ",
      [
        "storage",
        "002c2ad0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e5370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e5/009e5260.md#insn-009e5370) · [`009e5424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e5/009e5260.md#insn-009e5424) · [`009e528c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e5/009e5260.md#insn-009e528c)
- 新版 [`009e53c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e5/009e52b4.md#insn-009e53c4) · [`009e5478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e5/009e52b4.md#insn-009e5478) · [`009e52e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e5/009e52b4.md#insn-009e52e0)

~~~diff
- 009e5370 ["INT_ADD", "register:40f0:8", ["const:9e5370:8", "const:4:8"]]
- 009e5370 ["CALL", null, ["callee:008b98b0:8"]]
+ 009e53c4 ["INT_ADD", "register:40f0:8", ["const:9e53c4:8", "const:4:8"]]
+ 009e53c4 ["CALL", null, ["callee:008b98b0:8"]]
- 009e5370 bytes 3a51fb97
+ 009e53c4 bytes 3b51fb97
- 009e5424 ["INT_ADD", "register:40f0:8", ["const:9e5424:8", "const:4:8"]]
- 009e5424 ["CALL", null, ["callee:008b98b0:8"]]
+ 009e5478 ["INT_ADD", "register:40f0:8", ["const:9e5478:8", "const:4:8"]]
+ 009e5478 ["CALL", null, ["callee:008b98b0:8"]]
- 009e5424 bytes 0d51fb97
+ 009e5478 bytes 0e51fb97
- 009e528c ["INT_ADD", "register:40f0:8", ["const:9e528c:8", "const:4:8"]]
- 009e528c ["CALL", null, ["callee:009e2fe8:8"]]
+ 009e52e0 ["INT_ADD", "register:40f0:8", ["const:9e52e0:8", "const:4:8"]]
+ 009e52e0 ["CALL", null, ["callee:009e2fe8:8"]]
- 009e528c bytes 42f7ff97
+ 009e52e0 bytes 42f7ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fec4c58df7e62d3f330bf3f5d0633fe6"></a>

### [`009e561c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e5/009e561c.md) → [`009e5670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e5/009e5670.md) FUN_009e5670

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00606ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00606/00606ae4.md) [`0061452c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00614/0061452c.md) · 呼出先 9件 [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9858.md) [`008bacc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ba/008bacc8.md) [`009e8c6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e8c6c.md)
- 新版 呼出元 2件 [`00606b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00606/00606b24.md) [`0061456c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00614/0061456c.md) · 呼出先 9件 [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b98b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b98b0.md) [`008bad20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ba/008bad20.md) [`009e8cc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8cc0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 86.49% / 新版 86.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009e56b8",
      "incomplete_value": true,
      "site": "009e56c8",
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
                "const:d0b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e5664",
      "incomplete_value": true,
      "site": "009e5674",
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
                "const:d67:8"
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
      "definition_site": "009e56bc",
      "incomplete_value": true,
      "site": "009e56cc",
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
      "definition_site": "009e5668",
      "incomplete_value": true,
      "site": "009e5678",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009e56c0",
      "incomplete_value": true,
      "site": "009e56d0",
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
                "const:ad0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e566c",
      "incomplete_value": true,
      "site": "009e567c",
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
      "009e56b8",
      "READ",
      [
        "storage",
        "002a5d67",
        null,
        "string"
      ]
    ],
    [
      "009e56bc",
      "READ",
      [
        "storage",
        "002a5d71",
        null,
        "string"
      ]
    ],
    [
      "009e56c0",
      "READ",
      [
        "storage",
        "002c2a90",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009e56b8",
      "READ",
      [
        "storage",
        "002a5d0b",
        null,
        "string"
      ]
    ],
    [
      "009e56bc",
      "READ",
      [
        "storage",
        "002a5d15",
        null,
        "string"
      ]
    ],
    [
      "009e56c0",
      "READ",
      [
        "storage",
        "002c2ad0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e56c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e5/009e561c.md#insn-009e56c8) · [`009e5648`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e5/009e561c.md#insn-009e5648) · [`009e5654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e5/009e561c.md#insn-009e5654)
- 新版 [`009e571c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e5/009e5670.md#insn-009e571c) · [`009e569c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e5/009e5670.md#insn-009e569c) · [`009e56a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e5/009e5670.md#insn-009e56a8)

~~~diff
- 009e56c8 ["INT_ADD", "register:40f0:8", ["const:9e56c8:8", "const:4:8"]]
- 009e56c8 ["CALL", null, ["callee:008b98b0:8"]]
+ 009e571c ["INT_ADD", "register:40f0:8", ["const:9e571c:8", "const:4:8"]]
+ 009e571c ["CALL", null, ["callee:008b98b0:8"]]
- 009e56c8 bytes 6450fb97
+ 009e571c bytes 6550fb97
- 009e5648 ["INT_ADD", "register:40f0:8", ["const:9e5648:8", "const:4:8"]]
- 009e5648 ["CALL", null, ["callee:00851550:8"]]
+ 009e569c ["INT_ADD", "register:40f0:8", ["const:9e569c:8", "const:4:8"]]
+ 009e569c ["CALL", null, ["callee:00851550:8"]]
- 009e5648 bytes acaff997
+ 009e569c bytes adaff997
- 009e5654 ["INT_ADD", "register:40f0:8", ["const:9e5654:8", "const:4:8"]]
- 009e5654 ["CALL", null, ["callee:00c57f60:8"]]
+ 009e56a8 ["INT_ADD", "register:40f0:8", ["const:9e56a8:8", "const:4:8"]]
+ 009e56a8 ["CALL", null, ["callee:00c57f60:8"]]
- 009e5654 bytes 0fca0994
+ 009e56a8 bytes 2eca0994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b65a72e57cba8401f7755b2d1f9e8921"></a>

### [`009e64c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e6/009e64c0.md) → [`009e6514`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e6514.md) FUN_009e6514

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 6件 [`009dec20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009de/009dec20.md) [`009dfe0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009df/009dfe0c.md) [`009e1278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e1/009e1278.md) [`009e33b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e3/009e33b8.md) [`009f92c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f9/009f92c8.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 6件 [`009dec74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009de/009dec74.md) [`009dfe60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009df/009dfe60.md) [`009e12cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e1/009e12cc.md) [`009e340c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e3/009e340c.md) [`009f931c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f9/009f931c.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "009e6520",
      "incomplete_value": false,
      "site": "009e6524",
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
      "definition_site": "009e64cc",
      "incomplete_value": false,
      "site": "009e64d0",
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
      "009e6520",
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
      "009e6520",
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

- 旧版 [`009e64d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e6/009e64c0.md#insn-009e64d0) · [`009e64cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e6/009e64c0.md#insn-009e64cc)
- 新版 [`009e6524`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e6514.md#insn-009e6524) · [`009e6520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e6514.md#insn-009e6520)

~~~diff
- 009e64d0 ["INT_ADD", "register:40f0:8", ["const:9e64d0:8", "const:4:8"]]
- 009e64d0 ["CALL", null, ["callee:0043b7b8:8"]]
+ 009e6524 ["INT_ADD", "register:40f0:8", ["const:9e6524:8", "const:4:8"]]
+ 009e6524 ["CALL", null, ["callee:0043b7b8:8"]]
- 009e64d0 bytes aa54e997
+ 009e6524 bytes a554e997
- 009e64cc ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 009e64cc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 009e64cc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 009e64cc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 009e6520 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 009e6520 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 009e6520 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 009e6520 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 009e64cc bytes 00303d91
+ 009e6520 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-acda1543dd496e541287ca70101bc172"></a>

### [`009e64d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e6/009e64d8.md) → [`009e652c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e652c.md) FUN_009e652c

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009e6540",
      "incomplete_value": false,
      "site": "009e6544",
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
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e64ec",
      "incomplete_value": false,
      "site": "009e64f0",
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
            "const:c58:8"
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
      "009e6544",
      "DATA",
      [
        "storage",
        "00c89c58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009e6544",
      "DATA",
      [
        "storage",
        "00c89d28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e64e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e6/009e64d8.md#insn-009e64e4) · [`009e64ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e6/009e64d8.md#insn-009e64ec)
- 新版 [`009e6538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e652c.md#insn-009e6538) · [`009e6540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e652c.md#insn-009e6540)

~~~diff
- 009e64e4 ["INT_ADD", "register:40f0:8", ["const:9e64e4:8", "const:4:8"]]
- 009e64e4 ["CALL", null, ["callee:00c57f60:8"]]
+ 009e6538 ["INT_ADD", "register:40f0:8", ["const:9e6538:8", "const:4:8"]]
+ 009e6538 ["CALL", null, ["callee:00c57f60:8"]]
- 009e64e4 bytes 6bc60994
+ 009e6538 bytes 8ac60994
- 009e64ec ["COPY", "tmp:0:8", ["const:c58:8"]]
- 009e64ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009e64ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009e64ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009e6540 ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 009e6540 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009e6540 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009e6540 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009e64ec bytes 08613191
+ 009e6540 bytes 08a13491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-541c2a8d37b51c2c5d40944f16b8a0b9"></a>

### [`009e64fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e6/009e64fc.md) → [`009e6550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e6550.md) FUN_009e6550

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009e6554",
      "incomplete_value": false,
      "site": "009e6558",
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
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e6500",
      "incomplete_value": false,
      "site": "009e6504",
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
            "const:c58:8"
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
      "009e6558",
      "DATA",
      [
        "storage",
        "00c89c58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009e6558",
      "DATA",
      [
        "storage",
        "00c89d28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e6500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e6/009e64fc.md#insn-009e6500)
- 新版 [`009e6554`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e6550.md#insn-009e6554)

~~~diff
- 009e6500 ["COPY", "tmp:0:8", ["const:c58:8"]]
- 009e6500 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009e6500 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009e6500 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009e6554 ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 009e6554 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009e6554 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009e6554 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009e6500 bytes 08613191
+ 009e6554 bytes 08a13491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e85a792543d1a503c1157e97d803d3a"></a>

### [`009e6774`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e6/009e6774.md) → [`009e67c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e67c8.md) FUN_009e67c8

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`009e6540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e6/009e6540.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 1件 [`009e6594`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e6594.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "009e67d4",
      "incomplete_value": false,
      "site": "009e67d8",
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
      "definition_site": "009e6780",
      "incomplete_value": false,
      "site": "009e6784",
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
      "009e67d4",
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
      "009e67d4",
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

- 旧版 [`009e6784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e6/009e6774.md#insn-009e6784) · [`009e6780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e6/009e6774.md#insn-009e6780)
- 新版 [`009e67d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e67c8.md#insn-009e67d8) · [`009e67d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e67c8.md#insn-009e67d4)

~~~diff
- 009e6784 ["INT_ADD", "register:40f0:8", ["const:9e6784:8", "const:4:8"]]
- 009e6784 ["CALL", null, ["callee:0043b7b8:8"]]
+ 009e67d8 ["INT_ADD", "register:40f0:8", ["const:9e67d8:8", "const:4:8"]]
+ 009e67d8 ["CALL", null, ["callee:0043b7b8:8"]]
- 009e6784 bytes fd53e997
+ 009e67d8 bytes f853e997
- 009e6780 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 009e6780 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 009e6780 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 009e6780 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 009e67d4 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 009e67d4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 009e67d4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 009e67d4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 009e6780 bytes 00303d91
+ 009e67d4 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf70728a73029692b57f2be819972e35"></a>

### [`009e6c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e6/009e6c80.md) → [`009e6cd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e6cd4.md) FUN_009e6cd4

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`009e30ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e3/009e30ec.md) [`009e6c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e6/009e6c80.md) · 呼出先 7件 [`009e6c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e6/009e6c80.md) [`009e7bb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e7/009e7bb0.md) [`009e7e40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e7/009e7e40.md) [`009e8124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e8124.md) [`009e8458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e8458.md)
- 新版 呼出元 2件 [`009e3140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e3/009e3140.md) [`009e6cd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e6cd4.md) · 呼出先 7件 [`009e6cd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e6cd4.md) [`009e7c04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e7/009e7c04.md) [`009e7e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e7/009e7e94.md) [`009e8178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8178.md) [`009e84ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e84ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.07% / 新版 99.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009e7438",
      "incomplete_value": false,
      "site": "009e7440",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:735:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e73e4",
      "incomplete_value": false,
      "site": "009e73ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:6f5:8"
          ]
        ]
      ]
    },
    "ordinal": 33,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009e6e88",
      "PARAM",
      [
        "storage",
        "002c86f5",
        null,
        null
      ]
    ],
    [
      "009e6ea8",
      "PARAM",
      [
        "storage",
        "002c86f5",
        null,
        null
      ]
    ],
    [
      "009e6eec",
      "PARAM",
      [
        "storage",
        "002c86f5",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009e6e88",
      "PARAM",
      [
        "storage",
        "002c8735",
        null,
        null
      ]
    ],
    [
      "009e6ea8",
      "PARAM",
      [
        "storage",
        "002c8735",
        null,
        null
      ]
    ],
    [
      "009e6eec",
      "PARAM",
      [
        "storage",
        "002c8735",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e73ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e6/009e6c80.md#insn-009e73ec) · [`009e6cc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e6/009e6c80.md#insn-009e6cc4) · [`009e6d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e6/009e6c80.md#insn-009e6d70)
- 新版 [`009e7440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e6cd4.md#insn-009e7440) · [`009e6d18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e6cd4.md#insn-009e6d18) · [`009e6dc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e6cd4.md#insn-009e6dc4)

~~~diff
- 009e73ec ["INT_ADD", "register:40f0:8", ["const:9e73ec:8", "const:4:8"]]
- 009e73ec ["CALL", null, ["callee:009e84ac:8"]]
+ 009e7440 ["INT_ADD", "register:40f0:8", ["const:9e7440:8", "const:4:8"]]
+ 009e7440 ["CALL", null, ["callee:009e84ac:8"]]
- 009e73ec bytes 1b040094
+ 009e7440 bytes 1b040094
- 009e6cc4 ["COPY", "tmp:0:8", ["const:6f5:8"]]
- 009e6cc4 ["INT_CARRY", "register:105:1", ["register:40c0:8", "tmp:0:8"]]
- 009e6cc4 ["INT_SCARRY", "register:106:1", ["register:40c0:8", "tmp:0:8"]]
- 009e6cc4 ["INT_ADD", "tmp:1:8", ["register:40c0:8", "tmp:0:8"]]
+ 009e6d18 ["COPY", "tmp:0:8", ["const:735:8"]]
+ 009e6d18 ["INT_CARRY", "register:105:1", ["register:40c0:8", "tmp:0:8"]]
+ 009e6d18 ["INT_SCARRY", "register:106:1", ["register:40c0:8", "tmp:0:8"]]
+ 009e6d18 ["INT_ADD", "tmp:1:8", ["register:40c0:8", "tmp:0:8"]]
- 009e6cc4 bytes 18d71b91
+ 009e6d18 bytes 18d71c91
- 009e6d70 ["INT_ADD", "register:40f0:8", ["const:9e6d70:8", "const:4:8"]]
- 009e6d70 ["CALL", null, ["callee:009e7e94:8"]]
+ 009e6dc4 ["INT_ADD", "register:40f0:8", ["const:9e6dc4:8", "const:4:8"]]
+ 009e6dc4 ["CALL", null, ["callee:009e7e94:8"]]
- 009e6d70 bytes 34040094
+ 009e6dc4 bytes 34040094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-395bc56d3b5ab96ed6d24baaa92c0fe0"></a>

### [`009e7bb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e7/009e7bb0.md) → [`009e7c04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e7/009e7c04.md) FUN_009e7c04

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`009e6c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e6/009e6c80.md) [`009e8124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e8124.md) · 呼出先 3件 [`009e8458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e8458.md) [`009e871c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e871c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 2件 [`009e6cd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e6cd4.md) [`009e8178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8178.md) · 呼出先 3件 [`009e84ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e84ac.md) [`009e8770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8770.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.12% / 新版 95.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009e7c68",
      "incomplete_value": false,
      "site": "009e7c70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:735:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e7c14",
      "incomplete_value": false,
      "site": "009e7c1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:6f5:8"
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
      "definition_site": "009e7cec",
      "incomplete_value": false,
      "site": "009e7cf4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:735:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e7c98",
      "incomplete_value": false,
      "site": "009e7ca0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:6f5:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009e7d70",
      "incomplete_value": false,
      "site": "009e7d78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:735:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e7d1c",
      "incomplete_value": false,
      "site": "009e7d24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:6f5:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009e7c68",
      "PARAM",
      [
        "storage",
        "002c86f5",
        null,
        null
      ]
    ],
    [
      "009e7c88",
      "PARAM",
      [
        "storage",
        "002c86f5",
        null,
        null
      ]
    ],
    [
      "009e7cec",
      "PARAM",
      [
        "storage",
        "002c86f5",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009e7c68",
      "PARAM",
      [
        "storage",
        "002c8735",
        null,
        null
      ]
    ],
    [
      "009e7c88",
      "PARAM",
      [
        "storage",
        "002c8735",
        null,
        null
      ]
    ],
    [
      "009e7cec",
      "PARAM",
      [
        "storage",
        "002c8735",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e7c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e7/009e7bb0.md#insn-009e7c1c) · [`009e7ca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e7/009e7bb0.md#insn-009e7ca0) · [`009e7d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e7/009e7bb0.md#insn-009e7d24)
- 新版 [`009e7c70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e7/009e7c04.md#insn-009e7c70) · [`009e7cf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e7/009e7c04.md#insn-009e7cf4) · [`009e7d78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e7/009e7c04.md#insn-009e7d78)

~~~diff
- 009e7c1c ["INT_ADD", "register:40f0:8", ["const:9e7c1c:8", "const:4:8"]]
- 009e7c1c ["CALL", null, ["callee:009e84ac:8"]]
+ 009e7c70 ["INT_ADD", "register:40f0:8", ["const:9e7c70:8", "const:4:8"]]
+ 009e7c70 ["CALL", null, ["callee:009e84ac:8"]]
- 009e7c1c bytes 0f020094
+ 009e7c70 bytes 0f020094
- 009e7ca0 ["INT_ADD", "register:40f0:8", ["const:9e7ca0:8", "const:4:8"]]
- 009e7ca0 ["CALL", null, ["callee:009e84ac:8"]]
+ 009e7cf4 ["INT_ADD", "register:40f0:8", ["const:9e7cf4:8", "const:4:8"]]
+ 009e7cf4 ["CALL", null, ["callee:009e84ac:8"]]
- 009e7ca0 bytes ee010094
+ 009e7cf4 bytes ee010094
- 009e7d24 ["INT_ADD", "register:40f0:8", ["const:9e7d24:8", "const:4:8"]]
- 009e7d24 ["CALL", null, ["callee:009e84ac:8"]]
+ 009e7d78 ["INT_ADD", "register:40f0:8", ["const:9e7d78:8", "const:4:8"]]
+ 009e7d78 ["CALL", null, ["callee:009e84ac:8"]]
- 009e7d24 bytes cd010094
+ 009e7d78 bytes cd010094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78b5f9bd70dcac0022b36549abc007ba"></a>

### [`009e7e40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e7/009e7e40.md) → [`009e7e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e7/009e7e94.md) FUN_009e7e94

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`009e6c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e6/009e6c80.md) [`009e8124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e8124.md) [`009e871c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e871c.md) · 呼出先 2件 [`009e8458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e8458.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 3件 [`009e6cd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e6cd4.md) [`009e8178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8178.md) [`009e8770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8770.md) · 呼出先 2件 [`009e84ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e84ac.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.76% / 新版 96.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009e7ed0",
      "incomplete_value": false,
      "site": "009e7ee8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:735:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e7e7c",
      "incomplete_value": false,
      "site": "009e7e94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:6f5:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009e8024",
      "incomplete_value": false,
      "site": "009e802c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:735:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e7fd0",
      "incomplete_value": false,
      "site": "009e7fd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:6f5:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009e80d8",
      "incomplete_value": false,
      "site": "009e80e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:735:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e8084",
      "incomplete_value": false,
      "site": "009e8090",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:6f5:8"
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
      "009e7ed0",
      "PARAM",
      [
        "storage",
        "002c86f5",
        null,
        null
      ]
    ],
    [
      "009e7f00",
      "PARAM",
      [
        "storage",
        "002c86f5",
        null,
        null
      ]
    ],
    [
      "009e7f30",
      "PARAM",
      [
        "storage",
        "002c86f5",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009e7ed0",
      "PARAM",
      [
        "storage",
        "002c8735",
        null,
        null
      ]
    ],
    [
      "009e7f00",
      "PARAM",
      [
        "storage",
        "002c8735",
        null,
        null
      ]
    ],
    [
      "009e7f30",
      "PARAM",
      [
        "storage",
        "002c8735",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e7e94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e7/009e7e40.md#insn-009e7e94) · [`009e7fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e7/009e7e40.md#insn-009e7fd8) · [`009e8090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e7/009e7e40.md#insn-009e8090)
- 新版 [`009e7ee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e7/009e7e94.md#insn-009e7ee8) · [`009e802c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e7/009e7e94.md#insn-009e802c) · [`009e80e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e7/009e7e94.md#insn-009e80e4)

~~~diff
- 009e7e94 ["INT_ADD", "register:40f0:8", ["const:9e7e94:8", "const:4:8"]]
- 009e7e94 ["CALL", null, ["callee:009e84ac:8"]]
+ 009e7ee8 ["INT_ADD", "register:40f0:8", ["const:9e7ee8:8", "const:4:8"]]
+ 009e7ee8 ["CALL", null, ["callee:009e84ac:8"]]
- 009e7e94 bytes 71010094
+ 009e7ee8 bytes 71010094
- 009e7fd8 ["INT_ADD", "register:40f0:8", ["const:9e7fd8:8", "const:4:8"]]
- 009e7fd8 ["CALL", null, ["callee:009e84ac:8"]]
+ 009e802c ["INT_ADD", "register:40f0:8", ["const:9e802c:8", "const:4:8"]]
+ 009e802c ["CALL", null, ["callee:009e84ac:8"]]
- 009e7fd8 bytes 20010094
+ 009e802c bytes 20010094
- 009e8090 ["INT_ADD", "register:40f0:8", ["const:9e8090:8", "const:4:8"]]
- 009e8090 ["CALL", null, ["callee:009e84ac:8"]]
+ 009e80e4 ["INT_ADD", "register:40f0:8", ["const:9e80e4:8", "const:4:8"]]
+ 009e80e4 ["CALL", null, ["callee:009e84ac:8"]]
- 009e8090 bytes f2000094
+ 009e80e4 bytes f2000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-816c206a957193bbb3d31eb43fb5cc5e"></a>

### [`009e8124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e8124.md) → [`009e8178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8178.md) FUN_009e8178

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`009e6c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e6/009e6c80.md) · 呼出先 5件 [`009e7bb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e7/009e7bb0.md) [`009e7e40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e7/009e7e40.md) [`009e8458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e8458.md) [`009e871c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e871c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`009e6cd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e6cd4.md) · 呼出先 5件 [`009e7c04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e7/009e7c04.md) [`009e7e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e7/009e7e94.md) [`009e84ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e84ac.md) [`009e8770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8770.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.54% / 新版 98.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009e8244",
      "incomplete_value": false,
      "site": "009e8250",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:735:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e81f0",
      "incomplete_value": false,
      "site": "009e81fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:6f5:8"
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
      "009e8244",
      "PARAM",
      [
        "storage",
        "002c86f5",
        null,
        null
      ]
    ],
    [
      "009e8268",
      "PARAM",
      [
        "storage",
        "002c86f5",
        null,
        null
      ]
    ],
    [
      "009e836c",
      "PARAM",
      [
        "storage",
        "002c86f5",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009e8244",
      "PARAM",
      [
        "storage",
        "002c8735",
        null,
        null
      ]
    ],
    [
      "009e8268",
      "PARAM",
      [
        "storage",
        "002c8735",
        null,
        null
      ]
    ],
    [
      "009e836c",
      "PARAM",
      [
        "storage",
        "002c8735",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e81fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e8124.md#insn-009e81fc) · [`009e81c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e8124.md#insn-009e81c0) · [`009e81e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e8124.md#insn-009e81e0)
- 新版 [`009e8250`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8178.md#insn-009e8250) · [`009e8214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8178.md#insn-009e8214) · [`009e8234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8178.md#insn-009e8234)

~~~diff
- 009e81fc ["INT_ADD", "register:40f0:8", ["const:9e81fc:8", "const:4:8"]]
- 009e81fc ["CALL", null, ["callee:009e84ac:8"]]
+ 009e8250 ["INT_ADD", "register:40f0:8", ["const:9e8250:8", "const:4:8"]]
+ 009e8250 ["CALL", null, ["callee:009e84ac:8"]]
- 009e81fc bytes 97000094
+ 009e8250 bytes 97000094
- 009e81c0 ["INT_ADD", "register:40f0:8", ["const:9e81c0:8", "const:4:8"]]
- 009e81c0 ["CALL", null, ["callee:009e7c04:8"]]
+ 009e8214 ["INT_ADD", "register:40f0:8", ["const:9e8214:8", "const:4:8"]]
+ 009e8214 ["CALL", null, ["callee:009e7c04:8"]]
- 009e81c0 bytes 7cfeff97
+ 009e8214 bytes 7cfeff97
- 009e81e0 ["COPY", "tmp:0:8", ["const:6f5:8"]]
- 009e81e0 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
- 009e81e0 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
- 009e81e0 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
+ 009e8234 ["COPY", "tmp:0:8", ["const:735:8"]]
+ 009e8234 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
+ 009e8234 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
+ 009e8234 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
- 009e81e0 bytes d6d61b91
+ 009e8234 bytes d6d61c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afd95705a0b77b65276b8a57eb3f72e9"></a>

### [`009e871c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e871c.md) → [`009e8770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8770.md) FUN_009e8770

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`009e6c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e6/009e6c80.md) [`009e7bb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e7/009e7bb0.md) [`009e8124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e8124.md) · 呼出先 3件 [`009e7e40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e7/009e7e40.md) [`009e8458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e8458.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 3件 [`009e6cd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e6cd4.md) [`009e7c04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e7/009e7c04.md) [`009e8178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8178.md) · 呼出先 3件 [`009e7e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e7/009e7e94.md) [`009e84ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e84ac.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.09% / 新版 96.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009e8850",
      "incomplete_value": false,
      "site": "009e8858",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:735:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e87fc",
      "incomplete_value": false,
      "site": "009e8804",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:6f5:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009e88d4",
      "incomplete_value": false,
      "site": "009e88dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:735:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e8880",
      "incomplete_value": false,
      "site": "009e8888",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:6f5:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009e87cc",
      "PARAM",
      [
        "storage",
        "002c86f5",
        null,
        null
      ]
    ],
    [
      "009e87ec",
      "PARAM",
      [
        "storage",
        "002c86f5",
        null,
        null
      ]
    ],
    [
      "009e8850",
      "PARAM",
      [
        "storage",
        "002c86f5",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009e87cc",
      "PARAM",
      [
        "storage",
        "002c8735",
        null,
        null
      ]
    ],
    [
      "009e87ec",
      "PARAM",
      [
        "storage",
        "002c8735",
        null,
        null
      ]
    ],
    [
      "009e8850",
      "PARAM",
      [
        "storage",
        "002c8735",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e8804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e871c.md#insn-009e8804) · [`009e8888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e871c.md#insn-009e8888) · [`009e875c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e871c.md#insn-009e875c)
- 新版 [`009e8858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8770.md#insn-009e8858) · [`009e88dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8770.md#insn-009e88dc) · [`009e87b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8770.md#insn-009e87b0)

~~~diff
- 009e8804 ["INT_ADD", "register:40f0:8", ["const:9e8804:8", "const:4:8"]]
- 009e8804 ["CALL", null, ["callee:009e84ac:8"]]
+ 009e8858 ["INT_ADD", "register:40f0:8", ["const:9e8858:8", "const:4:8"]]
+ 009e8858 ["CALL", null, ["callee:009e84ac:8"]]
- 009e8804 bytes 15ffff97
+ 009e8858 bytes 15ffff97
- 009e8888 ["INT_ADD", "register:40f0:8", ["const:9e8888:8", "const:4:8"]]
- 009e8888 ["CALL", null, ["callee:009e84ac:8"]]
+ 009e88dc ["INT_ADD", "register:40f0:8", ["const:9e88dc:8", "const:4:8"]]
+ 009e88dc ["CALL", null, ["callee:009e84ac:8"]]
- 009e8888 bytes f4feff97
+ 009e88dc bytes f4feff97
- 009e875c ["INT_ADD", "register:40f0:8", ["const:9e875c:8", "const:4:8"]]
- 009e875c ["CALL", null, ["callee:009e7e94:8"]]
+ 009e87b0 ["INT_ADD", "register:40f0:8", ["const:9e87b0:8", "const:4:8"]]
+ 009e87b0 ["CALL", null, ["callee:009e7e94:8"]]
- 009e875c bytes b9fdff97
+ 009e87b0 bytes b9fdff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78e7c698dbf3169468565b8cad52d31c"></a>

### [`009e8a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e8a44.md) → [`009e8a98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8a98.md) FUN_009e8a98

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "009e8abc",
      "incomplete_value": false,
      "site": "009e8abc",
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
            "const:da8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e8a68",
      "incomplete_value": false,
      "site": "009e8a68",
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
            "const:cd8:8"
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
      "009e8abc",
      "DATA",
      [
        "storage",
        "00c89cd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009e8abc",
      "DATA",
      [
        "storage",
        "00c89da8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e8a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e8a44.md#insn-009e8a58) · [`009e8a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e8a44.md#insn-009e8a64)
- 新版 [`009e8aac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8a98.md#insn-009e8aac) · [`009e8ab8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8a98.md#insn-009e8ab8)

~~~diff
- 009e8a58 ["INT_ADD", "register:40f0:8", ["const:9e8a58:8", "const:4:8"]]
- 009e8a58 ["CALL", null, ["callee:00c57f60:8"]]
+ 009e8aac ["INT_ADD", "register:40f0:8", ["const:9e8aac:8", "const:4:8"]]
+ 009e8aac ["CALL", null, ["callee:00c57f60:8"]]
- 009e8a58 bytes 0ebd0994
+ 009e8aac bytes 2dbd0994
- 009e8a64 ["COPY", "tmp:0:8", ["const:cd8:8"]]
- 009e8a64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009e8a64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009e8a64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009e8ab8 ["COPY", "tmp:0:8", ["const:da8:8"]]
+ 009e8ab8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009e8ab8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009e8ab8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009e8a64 bytes 08613391
+ 009e8ab8 bytes 08a13691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb35ab5cc47d2116e6b45cf09df919bf"></a>

### [`009e8a78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e8a78.md) → [`009e8acc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8acc.md) FUN_009e8acc

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009e8ad8",
      "incomplete_value": false,
      "site": "009e8ad8",
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
            "const:da8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e8a84",
      "incomplete_value": false,
      "site": "009e8a84",
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
            "const:cd8:8"
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
      "009e8ad8",
      "DATA",
      [
        "storage",
        "00c89cd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009e8ad8",
      "DATA",
      [
        "storage",
        "00c89da8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e8a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e8a78.md#insn-009e8a80)
- 新版 [`009e8ad4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8acc.md#insn-009e8ad4)

~~~diff
- 009e8a80 ["COPY", "tmp:0:8", ["const:cd8:8"]]
- 009e8a80 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 009e8a80 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 009e8a80 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 009e8ad4 ["COPY", "tmp:0:8", ["const:da8:8"]]
+ 009e8ad4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 009e8ad4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 009e8ad4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 009e8a80 bytes 29613391
+ 009e8ad4 bytes 29a13691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3e6102a1959a0086d048e880423a6e2"></a>

### [`009e8a94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e8a94.md) → [`009e8ae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8ae8.md) FUN_009e8ae8

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`00a1a6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a6a4.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md) [`00a1a6f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a1a/00a1a6f8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.55% / 新版 96.55%

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
      "site": "009e8b10",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009e8abc",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "009e8b10",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "009e8b10",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e8abc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e8a94.md#insn-009e8abc) · [`009e8ac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e8a94.md#insn-009e8ac8) · [`009e8aec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e8a94.md#insn-009e8aec)
- 新版 [`009e8b10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8ae8.md#insn-009e8b10) · [`009e8b1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8ae8.md#insn-009e8b1c) · [`009e8b40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8ae8.md#insn-009e8b40)

~~~diff
- 009e8abc ["INT_ADD", "register:40f0:8", ["const:9e8abc:8", "const:4:8"]]
- 009e8abc ["CALL", null, ["ram:47acf4:8"]]
+ 009e8b10 ["INT_ADD", "register:40f0:8", ["const:9e8b10:8", "const:4:8"]]
+ 009e8b10 ["CALL", null, ["ram:47ad34:8"]]
- 009e8abc bytes 8e48ea97
+ 009e8b10 bytes 8948ea97
- 009e8ac8 ["INT_ADD", "register:40f0:8", ["const:9e8ac8:8", "const:4:8"]]
- 009e8ac8 ["CALL", null, ["callee:0047ce14:8"]]
+ 009e8b1c ["INT_ADD", "register:40f0:8", ["const:9e8b1c:8", "const:4:8"]]
+ 009e8b1c ["CALL", null, ["callee:0047ce14:8"]]
- 009e8ac8 bytes c350ea97
+ 009e8b1c bytes be50ea97
- 009e8aec ["INT_ADD", "register:40f0:8", ["const:9e8aec:8", "const:4:8"]]
- 009e8aec ["CALL", null, ["callee:00851550:8"]]
+ 009e8b40 ["INT_ADD", "register:40f0:8", ["const:9e8b40:8", "const:4:8"]]
+ 009e8b40 ["CALL", null, ["callee:00851550:8"]]
- 009e8aec bytes 83a2f997
+ 009e8b40 bytes 84a2f997
~~~


<a id="compare-f5885293f9aab2634a0371c069b26d00"></a>

### [`009e8b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e8b34.md) → [`009e8b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8b88.md) FUN_009e8b88

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "009e8bac",
      "incomplete_value": false,
      "site": "009e8bac",
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
            "const:e28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e8b58",
      "incomplete_value": false,
      "site": "009e8b58",
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
            "const:d58:8"
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
      "009e8bac",
      "DATA",
      [
        "storage",
        "00c89d58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009e8bac",
      "DATA",
      [
        "storage",
        "00c89e28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e8b48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e8b34.md#insn-009e8b48) · [`009e8b54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e8b34.md#insn-009e8b54)
- 新版 [`009e8b9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8b88.md#insn-009e8b9c) · [`009e8ba8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8b88.md#insn-009e8ba8)

~~~diff
- 009e8b48 ["INT_ADD", "register:40f0:8", ["const:9e8b48:8", "const:4:8"]]
- 009e8b48 ["CALL", null, ["callee:00c57f60:8"]]
+ 009e8b9c ["INT_ADD", "register:40f0:8", ["const:9e8b9c:8", "const:4:8"]]
+ 009e8b9c ["CALL", null, ["callee:00c57f60:8"]]
- 009e8b48 bytes d2bc0994
+ 009e8b9c bytes f1bc0994
- 009e8b54 ["COPY", "tmp:0:8", ["const:d58:8"]]
- 009e8b54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009e8b54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009e8b54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009e8ba8 ["COPY", "tmp:0:8", ["const:e28:8"]]
+ 009e8ba8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009e8ba8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009e8ba8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009e8b54 bytes 08613591
+ 009e8ba8 bytes 08a13891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef3f887bcae2436b8ec77d95f1990abf"></a>

### [`009e8b68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e8b68.md) → [`009e8bbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8bbc.md) FUN_009e8bbc

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009e8bc8",
      "incomplete_value": false,
      "site": "009e8bc8",
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
            "const:e28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e8b74",
      "incomplete_value": false,
      "site": "009e8b74",
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
            "const:d58:8"
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
      "009e8bc8",
      "DATA",
      [
        "storage",
        "00c89d58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009e8bc8",
      "DATA",
      [
        "storage",
        "00c89e28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e8b70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e8b68.md#insn-009e8b70)
- 新版 [`009e8bc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8bbc.md#insn-009e8bc4)

~~~diff
- 009e8b70 ["COPY", "tmp:0:8", ["const:d58:8"]]
- 009e8b70 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 009e8b70 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 009e8b70 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 009e8bc4 ["COPY", "tmp:0:8", ["const:e28:8"]]
+ 009e8bc4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 009e8bc4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 009e8bc4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 009e8b70 bytes 29613591
+ 009e8bc4 bytes 29a13891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5fffb412ea4fe54dd754222bd2b802f8"></a>

### [`009e8b84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e8b84.md) → [`009e8bd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8bd8.md) FUN_009e8bd8

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`00a1a6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a6a4.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md) [`00a1a6f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a1a/00a1a6f8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.55% / 新版 96.55%

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
      "site": "009e8c00",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009e8bac",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "009e8c00",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "009e8c00",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e8bac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e8b84.md#insn-009e8bac) · [`009e8bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e8b84.md#insn-009e8bb8) · [`009e8bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e8b84.md#insn-009e8bdc)
- 新版 [`009e8c00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8bd8.md#insn-009e8c00) · [`009e8c0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8bd8.md#insn-009e8c0c) · [`009e8c30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8bd8.md#insn-009e8c30)

~~~diff
- 009e8bac ["INT_ADD", "register:40f0:8", ["const:9e8bac:8", "const:4:8"]]
- 009e8bac ["CALL", null, ["ram:47acf4:8"]]
+ 009e8c00 ["INT_ADD", "register:40f0:8", ["const:9e8c00:8", "const:4:8"]]
+ 009e8c00 ["CALL", null, ["ram:47ad34:8"]]
- 009e8bac bytes 5248ea97
+ 009e8c00 bytes 4d48ea97
- 009e8bb8 ["INT_ADD", "register:40f0:8", ["const:9e8bb8:8", "const:4:8"]]
- 009e8bb8 ["CALL", null, ["callee:0047ce14:8"]]
+ 009e8c0c ["INT_ADD", "register:40f0:8", ["const:9e8c0c:8", "const:4:8"]]
+ 009e8c0c ["CALL", null, ["callee:0047ce14:8"]]
- 009e8bb8 bytes 8750ea97
+ 009e8c0c bytes 8250ea97
- 009e8bdc ["INT_ADD", "register:40f0:8", ["const:9e8bdc:8", "const:4:8"]]
- 009e8bdc ["CALL", null, ["callee:00851550:8"]]
+ 009e8c30 ["INT_ADD", "register:40f0:8", ["const:9e8c30:8", "const:4:8"]]
+ 009e8c30 ["CALL", null, ["callee:00851550:8"]]
- 009e8bdc bytes 47a2f997
+ 009e8c30 bytes 48a2f997
~~~


<a id="compare-ee407da7c6c5586c3768f00915aea6c3"></a>

### [`009e8c24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e8c24.md) → [`009e8c78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8c78.md) FUN_009e8c78

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "009e8c9c",
      "incomplete_value": false,
      "site": "009e8c9c",
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
            "const:ea8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e8c48",
      "incomplete_value": false,
      "site": "009e8c48",
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
            "const:dd8:8"
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
      "009e8c9c",
      "DATA",
      [
        "storage",
        "00c89dd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009e8c9c",
      "DATA",
      [
        "storage",
        "00c89ea8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e8c38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e8c24.md#insn-009e8c38) · [`009e8c44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e8c24.md#insn-009e8c44)
- 新版 [`009e8c8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8c78.md#insn-009e8c8c) · [`009e8c98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8c78.md#insn-009e8c98)

~~~diff
- 009e8c38 ["INT_ADD", "register:40f0:8", ["const:9e8c38:8", "const:4:8"]]
- 009e8c38 ["CALL", null, ["callee:00c57f60:8"]]
+ 009e8c8c ["INT_ADD", "register:40f0:8", ["const:9e8c8c:8", "const:4:8"]]
+ 009e8c8c ["CALL", null, ["callee:00c57f60:8"]]
- 009e8c38 bytes 96bc0994
+ 009e8c8c bytes b5bc0994
- 009e8c44 ["COPY", "tmp:0:8", ["const:dd8:8"]]
- 009e8c44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009e8c44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009e8c44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009e8c98 ["COPY", "tmp:0:8", ["const:ea8:8"]]
+ 009e8c98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009e8c98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009e8c98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009e8c44 bytes 08613791
+ 009e8c98 bytes 08a13a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30f53aa63a534fd495c6d7f2e557e21e"></a>

### [`009e8c58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e8c58.md) → [`009e8cac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8cac.md) FUN_009e8cac

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009e8cb8",
      "incomplete_value": false,
      "site": "009e8cb8",
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
            "const:ea8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e8c64",
      "incomplete_value": false,
      "site": "009e8c64",
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
            "const:dd8:8"
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
      "009e8cb8",
      "DATA",
      [
        "storage",
        "00c89dd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009e8cb8",
      "DATA",
      [
        "storage",
        "00c89ea8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e8c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e8c58.md#insn-009e8c60)
- 新版 [`009e8cb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8cac.md#insn-009e8cb4)

~~~diff
- 009e8c60 ["COPY", "tmp:0:8", ["const:dd8:8"]]
- 009e8c60 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 009e8c60 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 009e8c60 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 009e8cb4 ["COPY", "tmp:0:8", ["const:ea8:8"]]
+ 009e8cb4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 009e8cb4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 009e8cb4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 009e8c60 bytes 29613791
+ 009e8cb4 bytes 29a13a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-413c1ff357c5caedd0dde63a9b20228f"></a>

### [`009e8c74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e8c74.md) → [`009e8cc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8cc8.md) FUN_009e8cc8

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`00a1a6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a6a4.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md) [`00a1a6f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a1a/00a1a6f8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.55% / 新版 96.55%

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
      "site": "009e8cf0",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009e8c9c",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "009e8cf0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "009e8cf0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e8c9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e8c74.md#insn-009e8c9c) · [`009e8ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e8c74.md#insn-009e8ca8) · [`009e8ccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e8c74.md#insn-009e8ccc)
- 新版 [`009e8cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8cc8.md#insn-009e8cf0) · [`009e8cfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8cc8.md#insn-009e8cfc) · [`009e8d20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8cc8.md#insn-009e8d20)

~~~diff
- 009e8c9c ["INT_ADD", "register:40f0:8", ["const:9e8c9c:8", "const:4:8"]]
- 009e8c9c ["CALL", null, ["ram:47acf4:8"]]
+ 009e8cf0 ["INT_ADD", "register:40f0:8", ["const:9e8cf0:8", "const:4:8"]]
+ 009e8cf0 ["CALL", null, ["ram:47ad34:8"]]
- 009e8c9c bytes 1648ea97
+ 009e8cf0 bytes 1148ea97
- 009e8ca8 ["INT_ADD", "register:40f0:8", ["const:9e8ca8:8", "const:4:8"]]
- 009e8ca8 ["CALL", null, ["callee:0047ce14:8"]]
+ 009e8cfc ["INT_ADD", "register:40f0:8", ["const:9e8cfc:8", "const:4:8"]]
+ 009e8cfc ["CALL", null, ["callee:0047ce14:8"]]
- 009e8ca8 bytes 4b50ea97
+ 009e8cfc bytes 4650ea97
- 009e8ccc ["INT_ADD", "register:40f0:8", ["const:9e8ccc:8", "const:4:8"]]
- 009e8ccc ["CALL", null, ["callee:00851550:8"]]
+ 009e8d20 ["INT_ADD", "register:40f0:8", ["const:9e8d20:8", "const:4:8"]]
+ 009e8d20 ["CALL", null, ["callee:00851550:8"]]
- 009e8ccc bytes 0ba2f997
+ 009e8d20 bytes 0ca2f997
~~~


<a id="compare-8344b044689b6f2c3148c9500baf065e"></a>

### [`009e8d10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e8d10.md) → [`009e8d64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8d64.md) _INIT_204

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 82.49% / 新版 82.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 3件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009e8da0",
      "incomplete_value": true,
      "site": "009e8dbc",
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
      "definition_site": "009e8d4c",
      "incomplete_value": true,
      "site": "009e8d68",
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
      "definition_site": "009e8dc4",
      "incomplete_value": true,
      "site": "009e8de0",
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
      "definition_site": "009e8d70",
      "incomplete_value": true,
      "site": "009e8d8c",
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
      "definition_site": "009e8de4",
      "incomplete_value": true,
      "site": "009e8e00",
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
      "definition_site": "009e8d90",
      "incomplete_value": true,
      "site": "009e8dac",
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
      "009e8da0",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "009e8dc4",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "009e8de4",
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
      "009e8da0",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "009e8dc4",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "009e8de4",
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

- 旧版 [`009e8e04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e8d10.md#insn-009e8e04) · [`009e8e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e8d10.md#insn-009e8e70) · [`009e8eac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e8d10.md#insn-009e8eac)
- 新版 [`009e8e58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8d64.md#insn-009e8e58) · [`009e8ec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8d64.md#insn-009e8ec4) · [`009e8f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8d64.md#insn-009e8f00)

~~~diff
- 009e8e04 ["COPY", "tmp:0:8", ["const:f09:8"]]
- 009e8e04 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 009e8e04 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 009e8e04 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 009e8e58 ["COPY", "tmp:0:8", ["const:ebc:8"]]
+ 009e8e58 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 009e8e58 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 009e8e58 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 009e8e04 bytes 29253c91
+ 009e8e58 bytes 29f13a91
- 009e8e70 ["INT_ADD", "register:40f0:8", ["const:9e8e70:8", "const:4:8"]]
- 009e8e70 ["CALL", null, ["callee:0043b838:8"]]
+ 009e8ec4 ["INT_ADD", "register:40f0:8", ["const:9e8ec4:8", "const:4:8"]]
+ 009e8ec4 ["CALL", null, ["callee:0043b838:8"]]
- 009e8e70 bytes 624ae997
+ 009e8ec4 bytes 5d4ae997
- 009e8eac ["INT_ADD", "register:40f0:8", ["const:9e8eac:8", "const:4:8"]]
- 009e8eac ["CALL", null, ["callee:0043b838:8"]]
+ 009e8f00 ["INT_ADD", "register:40f0:8", ["const:9e8f00:8", "const:4:8"]]
+ 009e8f00 ["CALL", null, ["callee:0043b838:8"]]
- 009e8eac bytes 534ae997
+ 009e8f00 bytes 4e4ae997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d91114bf9b190689ee36bf0e099d40ac"></a>

### [`009e90a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e9/009e90a0.md) → [`009e90f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e9/009e90f4.md) FUN_009e90f4

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`009e9460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e9/009e9460.md) · 呼出先 5件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`009e94b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e9/009e94b4.md) · 呼出先 5件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.76% / 新版 91.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009e915c",
      "incomplete_value": true,
      "site": "009e9168",
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
                "const:620:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e9108",
      "incomplete_value": true,
      "site": "009e9114",
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
                "const:5e0:8"
              ]
            ]
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
      "definition_site": "009e9158",
      "incomplete_value": true,
      "site": "009e916c",
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e9104",
      "incomplete_value": true,
      "site": "009e9118",
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
                "const:20:8"
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
      "definition_site": "009e9158",
      "incomplete_value": true,
      "site": "009e916c",
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
      "definition_site": "009e9104",
      "incomplete_value": true,
      "site": "009e9118",
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
      "009e9158",
      "READ",
      [
        "storage",
        "002a800c",
        null,
        "string"
      ]
    ],
    [
      "009e9158",
      "READ",
      [
        "storage",
        "002a801c",
        null,
        "string"
      ]
    ],
    [
      "009e915c",
      "READ",
      [
        "storage",
        "002c25e0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009e9158",
      "READ",
      [
        "storage",
        "002a7fb0",
        null,
        "string"
      ]
    ],
    [
      "009e9158",
      "READ",
      [
        "storage",
        "002a7fc0",
        null,
        "string"
      ]
    ],
    [
      "009e915c",
      "READ",
      [
        "storage",
        "002c2620",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e9180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e9/009e90a0.md#insn-009e9180) · [`009e929c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e9/009e90a0.md#insn-009e929c) · [`009e90f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e9/009e90a0.md#insn-009e90f4)
- 新版 [`009e91d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e9/009e90f4.md#insn-009e91d4) · [`009e92f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e9/009e90f4.md#insn-009e92f0) · [`009e9148`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e9/009e90f4.md#insn-009e9148)

~~~diff
- 009e9180 ["COPY", "register:0:8", ["register:4040:8"]]
- 009e9180 ["INT_ADD", "register:40f0:8", ["const:9e9180:8", "const:4:8"]]
- 009e9180 ["CALLIND", null, ["register:0:8"]]
+ 009e91d4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009e91d4 ["INT_ADD", "register:40f0:8", ["const:9e91d4:8", "const:4:8"]]
+ 009e91d4 ["CALLIND", null, ["register:0:8"]]
- 009e9180 bytes 00013fd6
+ 009e91d4 bytes 00013fd6
- 009e929c ["INT_ADD", "register:40f0:8", ["const:9e929c:8", "const:4:8"]]
- 009e929c ["CALL", null, ["callee:004410cc:8"]]
+ 009e92f0 ["INT_ADD", "register:40f0:8", ["const:9e92f0:8", "const:4:8"]]
+ 009e92f0 ["CALL", null, ["callee:004410cc:8"]]
- 009e929c bytes 7c5fe997
+ 009e92f0 bytes 775fe997
- 009e90f4 ["INT_ADD", "register:40f0:8", ["const:9e90f4:8", "const:4:8"]]
- 009e90f4 ["CALL", null, ["callee:00c57f60:8"]]
+ 009e9148 ["INT_ADD", "register:40f0:8", ["const:9e9148:8", "const:4:8"]]
+ 009e9148 ["CALL", null, ["callee:00c57f60:8"]]
- 009e90f4 bytes 67bb0994
+ 009e9148 bytes 86bb0994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24d6972c01a24aafca3b496b19335cf5"></a>

### [`009e9460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e9/009e9460.md) → [`009e94b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e9/009e94b4.md) FUN_009e94b4

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`009ef8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ef/009ef8e0.md) · 呼出先 19件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md) [`00488434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488434.md)
- 新版 呼出元 1件 [`009ef934`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ef/009ef934.md) · 呼出先 19件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00487e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487e60.md) [`00488474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/00488474.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 88.05% / 新版 88.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 13件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009e94f8",
      "incomplete_value": false,
      "site": "009e94fc",
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
    "old": {
      "definition_site": "009e94a4",
      "incomplete_value": false,
      "site": "009e94a8",
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
            "const:d38:8"
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
      "definition_site": "009e9514",
      "incomplete_value": true,
      "site": "009e9524",
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
                "const:2a0000:8"
              ],
              [
                "leaf",
                "const:7d7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e94c0",
      "incomplete_value": true,
      "site": "009e94d0",
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
                "const:2a0000:8"
              ],
              [
                "leaf",
                "const:824:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "009e9518",
      "incomplete_value": true,
      "site": "009e9528",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "009e94c4",
      "incomplete_value": true,
      "site": "009e94d4",
      "value": [
        "LOAD",
        "8",
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
      "009e94fc",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "009e9514",
      "READ",
      [
        "storage",
        "002a0824",
        null,
        "string"
      ]
    ],
    [
      "009e9518",
      "READ",
      [
        "storage",
        "002a0834",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009e94fc",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ],
    [
      "009e9514",
      "READ",
      [
        "storage",
        "002a07d7",
        null,
        "string"
      ]
    ],
    [
      "009e9518",
      "READ",
      [
        "storage",
        "002a07e7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e952c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e9/009e9460.md#insn-009e952c) · [`009e9808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e9/009e9460.md#insn-009e9808) · [`009e949c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e9/009e9460.md#insn-009e949c)
- 新版 [`009e9580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e9/009e94b4.md#insn-009e9580) · [`009e985c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e9/009e94b4.md#insn-009e985c) · [`009e94f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e9/009e94b4.md#insn-009e94f0)

~~~diff
- 009e952c ["INT_ADD", "register:40f0:8", ["const:9e952c:8", "const:4:8"]]
- 009e952c ["CALL", null, ["callee:00596f6c:8"]]
+ 009e9580 ["INT_ADD", "register:40f0:8", ["const:9e9580:8", "const:4:8"]]
+ 009e9580 ["CALL", null, ["callee:00596f6c:8"]]
- 009e952c bytes 80b6ee97
+ 009e9580 bytes 7bb6ee97
- 009e9808 ["COPY", "tmp:0:8", ["const:75d:8"]]
- 009e9808 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009e9808 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009e9808 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009e985c ["COPY", "tmp:0:8", ["const:710:8"]]
+ 009e985c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009e985c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009e985c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009e9808 bytes 08751d91
+ 009e985c bytes 08411c91
- 009e949c ["INT_ADD", "register:40f0:8", ["const:9e949c:8", "const:4:8"]]
- 009e949c ["CALL", null, ["callee:00487e60:8"]]
+ 009e94f0 ["INT_ADD", "register:40f0:8", ["const:9e94f0:8", "const:4:8"]]
+ 009e94f0 ["CALL", null, ["callee:00487e60:8"]]
- 009e949c bytes 617aea97
+ 009e94f0 bytes 5c7aea97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-174fd0de7316e352978303d5079dbe1e"></a>

### [`009e9a74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e9/009e9a74.md) → [`009e9ac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e9/009e9ac8.md) FUN_009e9ac8

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`009ef8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ef/009ef8e0.md) · 呼出先 18件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md) [`00488434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488434.md) [`00488658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488658.md)
- 新版 呼出元 1件 [`009ef934`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ef/009ef934.md) · 呼出先 18件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00487e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487e60.md) [`00488474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/00488474.md) [`00488698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/00488698.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 86.79% / 新版 86.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 17件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009e9b0c",
      "incomplete_value": false,
      "site": "009e9b10",
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
    "old": {
      "definition_site": "009e9ab8",
      "incomplete_value": false,
      "site": "009e9abc",
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
            "const:d38:8"
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
      "definition_site": "009e9b2c",
      "incomplete_value": true,
      "site": "009e9b34",
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
                "const:7c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e9ad8",
      "incomplete_value": true,
      "site": "009e9ae0",
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
                "const:780:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "009e9b28",
      "incomplete_value": true,
      "site": "009e9b38",
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
                "const:2a4000:8"
              ],
              [
                "leaf",
                "const:ab3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e9ad4",
      "incomplete_value": true,
      "site": "009e9ae4",
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
                "const:2a4000:8"
              ],
              [
                "leaf",
                "const:b00:8"
              ]
            ]
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
      "009e9b10",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "009e9b28",
      "READ",
      [
        "storage",
        "002a4b00",
        null,
        "string"
      ]
    ],
    [
      "009e9b28",
      "READ",
      [
        "storage",
        "002a4b10",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009e9b10",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ],
    [
      "009e9b28",
      "READ",
      [
        "storage",
        "002a4ab3",
        null,
        "string"
      ]
    ],
    [
      "009e9b28",
      "READ",
      [
        "storage",
        "002a4ac3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009e9b10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e9/009e9a74.md#insn-009e9b10) · [`009e9b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e9/009e9a74.md#insn-009e9b38) · [`009e9d30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e9/009e9a74.md#insn-009e9d30)
- 新版 [`009e9b64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e9/009e9ac8.md#insn-009e9b64) · [`009e9b8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e9/009e9ac8.md#insn-009e9b8c) · [`009e9d84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e9/009e9ac8.md#insn-009e9d84)

~~~diff
- 009e9b10 ["INT_ADD", "register:40f0:8", ["const:9e9b10:8", "const:4:8"]]
- 009e9b10 ["CALL", null, ["callee:00c57f80:8"]]
+ 009e9b64 ["INT_ADD", "register:40f0:8", ["const:9e9b64:8", "const:4:8"]]
+ 009e9b64 ["CALL", null, ["callee:00c57f80:8"]]
- 009e9b10 bytes e8b80994
+ 009e9b64 bytes 07b90994
- 009e9b38 ["INT_ADD", "register:40f0:8", ["const:9e9b38:8", "const:4:8"]]
- 009e9b38 ["CALL", null, ["callee:00596f6c:8"]]
+ 009e9b8c ["INT_ADD", "register:40f0:8", ["const:9e9b8c:8", "const:4:8"]]
+ 009e9b8c ["CALL", null, ["callee:00596f6c:8"]]
- 009e9b38 bytes fdb4ee97
+ 009e9b8c bytes f8b4ee97
- 009e9d30 ["INT_ADD", "register:40f0:8", ["const:9e9d30:8", "const:4:8"]]
- 009e9d30 ["CALL", null, ["callee:00c57f60:8"]]
+ 009e9d84 ["INT_ADD", "register:40f0:8", ["const:9e9d84:8", "const:4:8"]]
+ 009e9d84 ["CALL", null, ["callee:00c57f60:8"]]
- 009e9d30 bytes 58b80994
+ 009e9d84 bytes 77b80994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc2fc6502d197814af1fd9d518a01864"></a>

### [`009e9f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e9/009e9f80.md) → [`009e9fd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e9/009e9fd4.md) FUN_009e9fd4

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`009e9a74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e9/009e9a74.md) · 呼出先 5件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`009e9ac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e9/009e9ac8.md) · 呼出先 5件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.27% / 新版 93.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009ea038",
      "incomplete_value": true,
      "site": "009ea040",
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
                "const:2c3000:8"
              ],
              [
                "leaf",
                "const:f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e9fe4",
      "incomplete_value": true,
      "site": "009e9fec",
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
                "const:2c3000:8"
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009ea034",
      "incomplete_value": true,
      "site": "009ea044",
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009e9fe0",
      "incomplete_value": true,
      "site": "009e9ff0",
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
                "const:20:8"
              ]
            ]
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
      "definition_site": "009ea034",
      "incomplete_value": true,
      "site": "009ea044",
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
      "definition_site": "009e9fe0",
      "incomplete_value": true,
      "site": "009e9ff0",
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
    "ordinal": 14,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009ea034",
      "READ",
      [
        "storage",
        "002be12f",
        null,
        "string"
      ]
    ],
    [
      "009ea034",
      "READ",
      [
        "storage",
        "002be13f",
        null,
        "string"
      ]
    ],
    [
      "009ea038",
      "READ",
      [
        "storage",
        "002c30b0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009ea034",
      "READ",
      [
        "storage",
        "002be0db",
        null,
        "string"
      ]
    ],
    [
      "009ea034",
      "READ",
      [
        "storage",
        "002be0eb",
        null,
        "string"
      ]
    ],
    [
      "009ea038",
      "READ",
      [
        "storage",
        "002c30f0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009ea10c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e9/009e9f80.md#insn-009ea10c) · [`009e9fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e9/009e9f80.md#insn-009e9fd0) · [`009e9fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e9/009e9f80.md#insn-009e9fd8)
- 新版 [`009ea160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e9/009e9fd4.md#insn-009ea160) · [`009ea024`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e9/009e9fd4.md#insn-009ea024) · [`009ea02c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e9/009e9fd4.md#insn-009ea02c)

~~~diff
- 009ea10c ["INT_ADD", "register:40f0:8", ["const:9ea10c:8", "const:4:8"]]
- 009ea10c ["CALL", null, ["callee:004410cc:8"]]
+ 009ea160 ["INT_ADD", "register:40f0:8", ["const:9ea160:8", "const:4:8"]]
+ 009ea160 ["CALL", null, ["callee:004410cc:8"]]
- 009ea10c bytes e05be997
+ 009ea160 bytes db5be997
- 009e9fd0 ["INT_ADD", "register:40f0:8", ["const:9e9fd0:8", "const:4:8"]]
- 009e9fd0 ["CALL", null, ["callee:00c57f60:8"]]
+ 009ea024 ["INT_ADD", "register:40f0:8", ["const:9ea024:8", "const:4:8"]]
+ 009ea024 ["CALL", null, ["callee:00c57f60:8"]]
- 009e9fd0 bytes b0b70994
+ 009ea024 bytes cfb70994
- 009e9fd8 ["COPY", "tmp:0:8", ["const:10f:8"]]
- 009e9fd8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009e9fd8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009e9fd8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009ea02c ["COPY", "tmp:0:8", ["const:bb:8"]]
+ 009ea02c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009ea02c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009ea02c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009e9fd8 bytes 083d0491
+ 009ea02c bytes 08ed0291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a919793288d8049b00ac4db8f7030fb7"></a>

### [`009ea364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ea/009ea364.md) → [`009ea3b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ea/009ea3b8.md) FUN_009ea3b8

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`009ea974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ea/009ea974.md) · 呼出先 9件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md)
- 新版 呼出元 1件 [`009ea9c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ea/009ea9c8.md) · 呼出先 9件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 20件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009ea42c",
      "incomplete_value": true,
      "site": "009ea434",
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
                "const:2c3000:8"
              ],
              [
                "leaf",
                "const:f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ea3d8",
      "incomplete_value": true,
      "site": "009ea3e0",
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
                "const:2c3000:8"
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
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009ea428",
      "incomplete_value": true,
      "site": "009ea438",
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ea3d4",
      "incomplete_value": true,
      "site": "009ea3e4",
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009ea428",
      "incomplete_value": true,
      "site": "009ea438",
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
      "definition_site": "009ea3d4",
      "incomplete_value": true,
      "site": "009ea3e4",
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
    "ordinal": 19,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009ea3e8",
      "READ",
      [
        "storage",
        "002a933d",
        null,
        "string"
      ]
    ],
    [
      "009ea428",
      "READ",
      [
        "storage",
        "002b4328",
        null,
        "string"
      ]
    ],
    [
      "009ea428",
      "READ",
      [
        "storage",
        "002b4338",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009ea3e8",
      "READ",
      [
        "storage",
        "002a936c",
        null,
        "string"
      ]
    ],
    [
      "009ea428",
      "READ",
      [
        "storage",
        "002b4359",
        null,
        "string"
      ]
    ],
    [
      "009ea428",
      "READ",
      [
        "storage",
        "002b4369",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009ea38c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ea/009ea364.md#insn-009ea38c) · [`009ea668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ea/009ea364.md#insn-009ea668) · [`009ea3c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ea/009ea364.md#insn-009ea3c4)
- 新版 [`009ea3e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ea/009ea3b8.md#insn-009ea3e0) · [`009ea6bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ea/009ea3b8.md#insn-009ea6bc) · [`009ea418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ea/009ea3b8.md#insn-009ea418)

~~~diff
- 009ea38c ["COPY", "tmp:0:8", ["const:33d:8"]]
- 009ea38c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 009ea38c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 009ea38c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 009ea3e0 ["COPY", "tmp:0:8", ["const:36c:8"]]
+ 009ea3e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 009ea3e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 009ea3e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 009ea38c bytes 29f50c91
+ 009ea3e0 bytes 29b10d91
- 009ea668 ["COPY", "register:0:8", ["register:4040:8"]]
- 009ea668 ["INT_ADD", "register:40f0:8", ["const:9ea668:8", "const:4:8"]]
- 009ea668 ["CALLIND", null, ["register:0:8"]]
+ 009ea6bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 009ea6bc ["INT_ADD", "register:40f0:8", ["const:9ea6bc:8", "const:4:8"]]
+ 009ea6bc ["CALLIND", null, ["register:0:8"]]
- 009ea668 bytes 00013fd6
+ 009ea6bc bytes 00013fd6
- 009ea3c4 ["INT_ADD", "register:40f0:8", ["const:9ea3c4:8", "const:4:8"]]
- 009ea3c4 ["CALL", null, ["callee:00c57f60:8"]]
+ 009ea418 ["INT_ADD", "register:40f0:8", ["const:9ea418:8", "const:4:8"]]
+ 009ea418 ["CALL", null, ["callee:00c57f60:8"]]
- 009ea3c4 bytes b3b60994
+ 009ea418 bytes d2b60994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-270f827f93ccddcbb157972cfe15ea1e"></a>

### [`009ea974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ea/009ea974.md) → [`009ea9c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ea/009ea9c8.md) FUN_009ea9c8

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`009ef8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ef/009ef8e0.md) · 呼出先 19件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md) [`00488434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488434.md)
- 新版 呼出元 1件 [`009ef934`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ef/009ef934.md) · 呼出先 19件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00487e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487e60.md) [`00488474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/00488474.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.86% / 新版 88.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 17件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009eaa0c",
      "incomplete_value": false,
      "site": "009eaa10",
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
    "old": {
      "definition_site": "009ea9b8",
      "incomplete_value": false,
      "site": "009ea9bc",
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
            "const:d38:8"
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
      "definition_site": "009eaa28",
      "incomplete_value": true,
      "site": "009eaa38",
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
                "const:2a0000:8"
              ],
              [
                "leaf",
                "const:7f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ea9d4",
      "incomplete_value": true,
      "site": "009ea9e4",
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
                "const:2a0000:8"
              ],
              [
                "leaf",
                "const:83d:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "009eaa2c",
      "incomplete_value": true,
      "site": "009eaa3c",
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
                "const:c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ea9d8",
      "incomplete_value": true,
      "site": "009ea9e8",
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
                "const:c:8"
              ]
            ]
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
      "009eaa10",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "009eaa28",
      "READ",
      [
        "storage",
        "002a083d",
        null,
        "string"
      ]
    ],
    [
      "009eaa2c",
      "READ",
      [
        "storage",
        "002a0849",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009eaa10",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ],
    [
      "009eaa28",
      "READ",
      [
        "storage",
        "002a07f0",
        null,
        "string"
      ]
    ],
    [
      "009eaa2c",
      "READ",
      [
        "storage",
        "002a07fc",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009eaa38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ea/009ea974.md#insn-009eaa38) · [`009eacfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ea/009ea974.md#insn-009eacfc) · [`009ead1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ea/009ea974.md#insn-009ead1c)
- 新版 [`009eaa8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ea/009ea9c8.md#insn-009eaa8c) · [`009ead50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ea/009ea9c8.md#insn-009ead50) · [`009ead70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ea/009ea9c8.md#insn-009ead70)

~~~diff
- 009eaa38 ["INT_ADD", "register:40f0:8", ["const:9eaa38:8", "const:4:8"]]
- 009eaa38 ["CALL", null, ["callee:00597648:8"]]
+ 009eaa8c ["INT_ADD", "register:40f0:8", ["const:9eaa8c:8", "const:4:8"]]
+ 009eaa8c ["CALL", null, ["callee:00597648:8"]]
- 009eaa38 bytes f4b2ee97
+ 009eaa8c bytes efb2ee97
- 009eacfc ["COPY", "register:0:8", ["register:4048:8"]]
- 009eacfc ["INT_ADD", "register:40f0:8", ["const:9eacfc:8", "const:4:8"]]
- 009eacfc ["CALLIND", null, ["register:0:8"]]
+ 009ead50 ["COPY", "register:0:8", ["register:4048:8"]]
+ 009ead50 ["INT_ADD", "register:40f0:8", ["const:9ead50:8", "const:4:8"]]
+ 009ead50 ["CALLIND", null, ["register:0:8"]]
- 009eacfc bytes 20013fd6
+ 009ead50 bytes 20013fd6
- 009ead1c ["COPY", "register:4040:8", ["const:2af000:8"]]
+ 009ead70 ["COPY", "register:4040:8", ["const:2ae000:8"]]
- 009ead1c bytes 28c6ffb0
+ 009ead70 bytes 28c6ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f57ae9ddcd490fff005cb376dd67ac2"></a>

### [`009eaf84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ea/009eaf84.md) → [`009eafd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ea/009eafd8.md) FUN_009eafd8

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`009ec250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ec/009ec250.md) · 呼出先 15件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`009e93d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e9/009e93d8.md)
- 新版 呼出元 1件 [`009ec2a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ec/009ec2a4.md) · 呼出先 15件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`009e942c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e9/009e942c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.06% / 新版 88.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 17件, `store_value` 45件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009eb048",
      "incomplete_value": true,
      "site": "009eb054",
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
                "const:2c3000:8"
              ],
              [
                "leaf",
                "const:60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009eaff4",
      "incomplete_value": true,
      "site": "009eb000",
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
                "const:2c3000:8"
              ],
              [
                "leaf",
                "const:20:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "009eb044",
      "incomplete_value": true,
      "site": "009eb058",
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009eaff0",
      "incomplete_value": true,
      "site": "009eb004",
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009eb044",
      "incomplete_value": true,
      "site": "009eb058",
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
      "definition_site": "009eaff0",
      "incomplete_value": true,
      "site": "009eb004",
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
      "009eb044",
      "READ",
      [
        "storage",
        "002b4386",
        null,
        "string"
      ]
    ],
    [
      "009eb044",
      "READ",
      [
        "storage",
        "002b4396",
        null,
        "string"
      ]
    ],
    [
      "009eb048",
      "READ",
      [
        "storage",
        "002c3020",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009eb044",
      "READ",
      [
        "storage",
        "002b43b7",
        null,
        "string"
      ]
    ],
    [
      "009eb044",
      "READ",
      [
        "storage",
        "002b43c7",
        null,
        "string"
      ]
    ],
    [
      "009eb048",
      "READ",
      [
        "storage",
        "002c3060",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009eb06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ea/009eaf84.md#insn-009eb06c) · [`009eb0c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ea/009eaf84.md#insn-009eb0c8) · [`009eb0fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ea/009eaf84.md#insn-009eb0fc)
- 新版 [`009eb0c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ea/009eafd8.md#insn-009eb0c0) · [`009eb11c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ea/009eafd8.md#insn-009eb11c) · [`009eb150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ea/009eafd8.md#insn-009eb150)

~~~diff
- 009eb06c ["COPY", "register:0:8", ["register:4040:8"]]
- 009eb06c ["INT_ADD", "register:40f0:8", ["const:9eb06c:8", "const:4:8"]]
- 009eb06c ["CALLIND", null, ["register:0:8"]]
+ 009eb0c0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009eb0c0 ["INT_ADD", "register:40f0:8", ["const:9eb0c0:8", "const:4:8"]]
+ 009eb0c0 ["CALLIND", null, ["register:0:8"]]
- 009eb06c bytes 00013fd6
+ 009eb0c0 bytes 00013fd6
- 009eb0c8 ["INT_ADD", "register:40f0:8", ["const:9eb0c8:8", "const:4:8"]]
- 009eb0c8 ["CALL", null, ["callee:004410cc:8"]]
+ 009eb11c ["INT_ADD", "register:40f0:8", ["const:9eb11c:8", "const:4:8"]]
+ 009eb11c ["CALL", null, ["callee:004410cc:8"]]
- 009eb0c8 bytes f157e997
+ 009eb11c bytes ec57e997
- 009eb0fc ["INT_ADD", "register:40f0:8", ["const:9eb0fc:8", "const:4:8"]]
- 009eb0fc ["CALL", null, ["callee:00c57f80:8"]]
+ 009eb150 ["INT_ADD", "register:40f0:8", ["const:9eb150:8", "const:4:8"]]
+ 009eb150 ["CALL", null, ["callee:00c57f80:8"]]
- 009eb0fc bytes 6db30994
+ 009eb150 bytes 8cb30994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7e68db277e86bd457a5409dd76df3fd"></a>

### [`009ec898`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ec/009ec898.md) → [`009ec8ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ec/009ec8ec.md) FUN_009ec8ec

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.92% / 新版 95.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009ec908",
      "incomplete_value": false,
      "site": "009ec90c",
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
            "const:80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ec8b4",
      "incomplete_value": false,
      "site": "009ec8b8",
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
            "const:fb0:8"
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
      "009ec90c",
      "DATA",
      [
        "storage",
        "00c89fb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009ec90c",
      "DATA",
      [
        "storage",
        "00c8a080",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009ec90c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ec/009ec898.md#insn-009ec90c) · [`009ec8b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ec/009ec898.md#insn-009ec8b0) · [`009ec8b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ec/009ec898.md#insn-009ec8b4)
- 新版 [`009ec960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ec/009ec8ec.md#insn-009ec960) · [`009ec904`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ec/009ec8ec.md#insn-009ec904) · [`009ec908`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ec/009ec8ec.md#insn-009ec908)

~~~diff
- 009ec90c ["INT_ADD", "register:40f0:8", ["const:9ec90c:8", "const:4:8"]]
- 009ec90c ["CALL", null, ["callee:00c57f50:8"]]
+ 009ec960 ["INT_ADD", "register:40f0:8", ["const:9ec960:8", "const:4:8"]]
+ 009ec960 ["CALL", null, ["callee:00c57f50:8"]]
- 009ec90c bytes 5dad0994
+ 009ec960 bytes 7cad0994
- 009ec8b0 ["COPY", "register:4040:8", ["const:c89000:8"]]
+ 009ec904 ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 009ec8b0 bytes e81400b0
+ 009ec904 bytes e81400d0
- 009ec8b4 ["COPY", "tmp:0:8", ["const:fb0:8"]]
- 009ec8b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009ec8b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009ec8b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009ec908 ["COPY", "tmp:0:8", ["const:80:8"]]
+ 009ec908 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009ec908 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009ec908 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009ec8b4 bytes 08c13e91
+ 009ec908 bytes 08010291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89c23661c0e4a0439e9db244ae405cf2"></a>

### [`009ec95c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ec/009ec95c.md) → [`009ec9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ec/009ec9b0.md) FUN_009ec9b0

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`009ef8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ef/009ef8e0.md) · 呼出先 18件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md) [`00488434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488434.md) [`00488658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488658.md)
- 新版 呼出元 1件 [`009ef934`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ef/009ef934.md) · 呼出先 18件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00487e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487e60.md) [`00488474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/00488474.md) [`00488698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/00488698.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 85.61% / 新版 85.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_destination` 1件, `store_value` 15件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009ec9f0",
      "incomplete_value": false,
      "site": "009ec9f4",
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
    "old": {
      "definition_site": "009ec99c",
      "incomplete_value": false,
      "site": "009ec9a0",
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
            "const:d38:8"
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
      "definition_site": "009eca0c",
      "incomplete_value": true,
      "site": "009eca1c",
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
                "const:b26:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ec9b8",
      "incomplete_value": true,
      "site": "009ec9c8",
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
                "const:b7a:8"
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
      "definition_site": "009ecab8",
      "incomplete_value": true,
      "site": "009ecac0",
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009eca64",
      "incomplete_value": true,
      "site": "009eca6c",
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 21,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009ec9f4",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "009eca0c",
      "READ",
      [
        "storage",
        "002bbb7a",
        null,
        "string"
      ]
    ],
    [
      "009eca10",
      "READ",
      [
        "storage",
        "002bbb89",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009ec9f4",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ],
    [
      "009eca0c",
      "READ",
      [
        "storage",
        "002bbb26",
        null,
        "string"
      ]
    ],
    [
      "009eca10",
      "READ",
      [
        "storage",
        "002bbb35",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009eca18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ec/009ec95c.md#insn-009eca18) · [`009eca28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ec/009ec95c.md#insn-009eca28) · [`009eca34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ec/009ec95c.md#insn-009eca34)
- 新版 [`009eca6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ec/009ec9b0.md#insn-009eca6c) · [`009eca7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ec/009ec9b0.md#insn-009eca7c) · [`009eca88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ec/009ec9b0.md#insn-009eca88)

~~~diff
- 009eca18 ["INT_ADD", "register:40f0:8", ["const:9eca18:8", "const:4:8"]]
- 009eca18 ["CALL", null, ["callee:00597648:8"]]
+ 009eca6c ["INT_ADD", "register:40f0:8", ["const:9eca6c:8", "const:4:8"]]
+ 009eca6c ["CALL", null, ["callee:00597648:8"]]
- 009eca18 bytes fcaaee97
+ 009eca6c bytes f7aaee97
- 009eca28 ["INT_ADD", "register:40f0:8", ["const:9eca28:8", "const:4:8"]]
- 009eca28 ["CALL", null, ["callee:00c57f60:8"]]
+ 009eca7c ["INT_ADD", "register:40f0:8", ["const:9eca7c:8", "const:4:8"]]
+ 009eca7c ["CALL", null, ["callee:00c57f60:8"]]
- 009eca28 bytes 1aad0994
+ 009eca7c bytes 39ad0994
- 009eca34 ["INT_ADD", "register:40f0:8", ["const:9eca34:8", "const:4:8"]]
- 009eca34 ["CALL", null, ["callee:009f32f8:8"]]
+ 009eca88 ["INT_ADD", "register:40f0:8", ["const:9eca88:8", "const:4:8"]]
+ 009eca88 ["CALL", null, ["callee:009f32f8:8"]]
- 009eca34 bytes 1c1a0094
+ 009eca88 bytes 1c1a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-845dd4ffe84c72b1642ce8a856def8d6"></a>

### [`009ed118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ed/009ed118.md) → [`009ed16c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ed/009ed16c.md) FUN_009ed16c

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`009ed5b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ed/009ed5b8.md) · 呼出先 8件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`009f35fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f35fc.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`009ed60c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ed/009ed60c.md) · 呼出先 8件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`009f3650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3650.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.04% / 新版 90.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009ed1c4",
      "incomplete_value": true,
      "site": "009ed1c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:760:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ed170",
      "incomplete_value": true,
      "site": "009ed170",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7ad:8"
              ]
            ]
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
      "definition_site": "009ed1e0",
      "incomplete_value": true,
      "site": "009ed1f4",
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
                "const:2c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ed18c",
      "incomplete_value": true,
      "site": "009ed1a0",
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
                "const:280:8"
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
      "definition_site": "009ed1ec",
      "incomplete_value": true,
      "site": "009ed1fc",
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ed198",
      "incomplete_value": true,
      "site": "009ed1a8",
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 21,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009ed19c",
      "READ",
      [
        "storage",
        "002a17ad",
        null,
        "string"
      ]
    ],
    [
      "009ed1e0",
      "READ",
      [
        "storage",
        "002c2280",
        null,
        null
      ]
    ],
    [
      "009ed1ec",
      "READ",
      [
        "storage",
        "002abd87",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009ed19c",
      "READ",
      [
        "storage",
        "002a1760",
        null,
        "string"
      ]
    ],
    [
      "009ed1e0",
      "READ",
      [
        "storage",
        "002c22c0",
        null,
        null
      ]
    ],
    [
      "009ed1ec",
      "READ",
      [
        "storage",
        "002abd2b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009ed1c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ed/009ed118.md#insn-009ed1c4) · [`009ed260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ed/009ed118.md#insn-009ed260) · [`009ed30c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ed/009ed118.md#insn-009ed30c)
- 新版 [`009ed218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ed/009ed16c.md#insn-009ed218) · [`009ed2b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ed/009ed16c.md#insn-009ed2b4) · [`009ed360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ed/009ed16c.md#insn-009ed360)

~~~diff
- 009ed1c4 ["INT_ADD", "register:40f0:8", ["const:9ed1c4:8", "const:4:8"]]
- 009ed1c4 ["CALL", null, ["callee:004410cc:8"]]
+ 009ed218 ["INT_ADD", "register:40f0:8", ["const:9ed218:8", "const:4:8"]]
+ 009ed218 ["CALL", null, ["callee:004410cc:8"]]
- 009ed1c4 bytes b24fe997
+ 009ed218 bytes ad4fe997
- 009ed260 ["INT_ADD", "register:40f0:8", ["const:9ed260:8", "const:4:8"]]
- 009ed260 ["CALL", null, ["callee:004410cc:8"]]
+ 009ed2b4 ["INT_ADD", "register:40f0:8", ["const:9ed2b4:8", "const:4:8"]]
+ 009ed2b4 ["CALL", null, ["callee:004410cc:8"]]
- 009ed260 bytes 8b4fe997
+ 009ed2b4 bytes 864fe997
- 009ed30c ["INT_ADD", "register:40f0:8", ["const:9ed30c:8", "const:4:8"]]
- 009ed30c ["CALL", null, ["callee:004410cc:8"]]
+ 009ed360 ["INT_ADD", "register:40f0:8", ["const:9ed360:8", "const:4:8"]]
+ 009ed360 ["CALL", null, ["callee:004410cc:8"]]
- 009ed30c bytes 604fe997
+ 009ed360 bytes 5b4fe997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-515168db225b9afb0291d175d76f99a5"></a>

### [`009ed5b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ed/009ed5b8.md) → [`009ed60c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ed/009ed60c.md) FUN_009ed60c

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`009ef8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ef/009ef8e0.md) · 呼出先 19件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md) [`00488434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488434.md) [`00488658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488658.md)
- 新版 呼出元 1件 [`009ef934`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ef/009ef934.md) · 呼出先 19件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00487e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487e60.md) [`00488474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/00488474.md) [`00488698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/00488698.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 83.11% / 新版 83.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 22件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009ed648",
      "incomplete_value": false,
      "site": "009ed64c",
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
    "old": {
      "definition_site": "009ed5f4",
      "incomplete_value": false,
      "site": "009ed5f8",
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
            "const:d38:8"
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
      "definition_site": "009ed664",
      "incomplete_value": true,
      "site": "009ed674",
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
                "const:2b6000:8"
              ],
              [
                "leaf",
                "const:9af:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ed610",
      "incomplete_value": true,
      "site": "009ed620",
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
                "const:2b6000:8"
              ],
              [
                "leaf",
                "const:96f:8"
              ]
            ]
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
      "definition_site": "009ed668",
      "incomplete_value": true,
      "site": "009ed678",
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
      "definition_site": "009ed614",
      "incomplete_value": true,
      "site": "009ed624",
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
    "ordinal": 14,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009ed64c",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "009ed664",
      "READ",
      [
        "storage",
        "002b696f",
        null,
        "string"
      ]
    ],
    [
      "009ed668",
      "READ",
      [
        "storage",
        "002b697e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009ed64c",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ],
    [
      "009ed664",
      "READ",
      [
        "storage",
        "002b69af",
        null,
        "string"
      ]
    ],
    [
      "009ed668",
      "READ",
      [
        "storage",
        "002b69be",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009ed67c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ed/009ed5b8.md#insn-009ed67c) · [`009ed86c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ed/009ed5b8.md#insn-009ed86c) · [`009ed8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ed/009ed5b8.md#insn-009ed8e0)
- 新版 [`009ed6d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ed/009ed60c.md#insn-009ed6d0) · [`009ed8c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ed/009ed60c.md#insn-009ed8c0) · [`009ed934`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ed/009ed60c.md#insn-009ed934)

~~~diff
- 009ed67c ["INT_ADD", "register:40f0:8", ["const:9ed67c:8", "const:4:8"]]
- 009ed67c ["CALL", null, ["callee:00596f6c:8"]]
+ 009ed6d0 ["INT_ADD", "register:40f0:8", ["const:9ed6d0:8", "const:4:8"]]
+ 009ed6d0 ["CALL", null, ["callee:00596f6c:8"]]
- 009ed67c bytes 2ca6ee97
+ 009ed6d0 bytes 27a6ee97
- 009ed86c ["INT_ADD", "register:40f0:8", ["const:9ed86c:8", "const:4:8"]]
- 009ed86c ["CALL", null, ["callee:00c57f60:8"]]
+ 009ed8c0 ["INT_ADD", "register:40f0:8", ["const:9ed8c0:8", "const:4:8"]]
+ 009ed8c0 ["CALL", null, ["callee:00c57f60:8"]]
- 009ed86c bytes 89a90994
+ 009ed8c0 bytes a8a90994
- 009ed8e0 ["COPY", "tmp:0:8", ["const:85a:8"]]
- 009ed8e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009ed8e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009ed8e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009ed934 ["COPY", "tmp:0:8", ["const:80d:8"]]
+ 009ed934 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009ed934 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009ed934 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009ed8e0 bytes 08692191
+ 009ed934 bytes 08352091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef7811af5060e924f1385ebe21bdaa4d"></a>

### [`009edb3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ed/009edb3c.md) → [`009edb90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ed/009edb90.md) FUN_009edb90

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`009edefc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ed/009edefc.md) · 呼出先 8件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`009f2de4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2de4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`009edf50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ed/009edf50.md) · 呼出先 8件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`009f2e38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2e38.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.59% / 新版 91.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009edbe8",
      "incomplete_value": true,
      "site": "009edbe8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2aa000:8"
              ],
              [
                "leaf",
                "const:39f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009edb94",
      "incomplete_value": true,
      "site": "009edb94",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2aa000:8"
              ],
              [
                "leaf",
                "const:3fb:8"
              ]
            ]
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
      "definition_site": "009edc08",
      "incomplete_value": true,
      "site": "009edc14",
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
                "const:800:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009edbb4",
      "incomplete_value": true,
      "site": "009edbc0",
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
                "const:7c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009edc04",
      "incomplete_value": true,
      "site": "009edc18",
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
                "const:40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009edbb0",
      "incomplete_value": true,
      "site": "009edbc4",
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
                "const:40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009edbc0",
      "READ",
      [
        "storage",
        "002aa3fb",
        null,
        "string"
      ]
    ],
    [
      "009edc04",
      "READ",
      [
        "storage",
        "002b55e8",
        null,
        "string"
      ]
    ],
    [
      "009edc04",
      "READ",
      [
        "storage",
        "002b55f8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009edbc0",
      "READ",
      [
        "storage",
        "002aa39f",
        null,
        "string"
      ]
    ],
    [
      "009edc04",
      "READ",
      [
        "storage",
        "002b5619",
        null,
        "string"
      ]
    ],
    [
      "009edc04",
      "READ",
      [
        "storage",
        "002b5629",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009edbe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ed/009edb3c.md#insn-009edbe8) · [`009edb64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ed/009edb3c.md#insn-009edb64) · [`009edba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ed/009edb3c.md#insn-009edba0)
- 新版 [`009edc3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ed/009edb90.md#insn-009edc3c) · [`009edbb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ed/009edb90.md#insn-009edbb8) · [`009edbf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ed/009edb90.md#insn-009edbf4)

~~~diff
- 009edbe8 ["INT_ADD", "register:40f0:8", ["const:9edbe8:8", "const:4:8"]]
- 009edbe8 ["CALL", null, ["callee:004410cc:8"]]
+ 009edc3c ["INT_ADD", "register:40f0:8", ["const:9edc3c:8", "const:4:8"]]
+ 009edc3c ["CALL", null, ["callee:004410cc:8"]]
- 009edbe8 bytes 294de997
+ 009edc3c bytes 244de997
- 009edb64 ["COPY", "tmp:0:8", ["const:3fb:8"]]
- 009edb64 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 009edb64 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 009edb64 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 009edbb8 ["COPY", "tmp:0:8", ["const:39f:8"]]
+ 009edbb8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 009edbb8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 009edbb8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 009edb64 bytes 4aed0f91
+ 009edbb8 bytes 4a7d0e91
- 009edba0 ["INT_ADD", "register:40f0:8", ["const:9edba0:8", "const:4:8"]]
- 009edba0 ["CALL", null, ["callee:00c57f60:8"]]
+ 009edbf4 ["INT_ADD", "register:40f0:8", ["const:9edbf4:8", "const:4:8"]]
+ 009edbf4 ["CALL", null, ["callee:00c57f60:8"]]
- 009edba0 bytes bca80994
+ 009edbf4 bytes dba80994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8975f6ed778e7b4d1d5641cd7034b802"></a>

### [`009ee334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ee/009ee334.md) → [`009ee388`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ee/009ee388.md) FUN_009ee388

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`009ef8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ef/009ef8e0.md) · 呼出先 20件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md) [`00488434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488434.md)
- 新版 呼出元 1件 [`009ef934`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ef/009ef934.md) · 呼出先 20件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00487e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487e60.md) [`00488474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/00488474.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.97% / 新版 89.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 16件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009ee3cc",
      "incomplete_value": false,
      "site": "009ee3d0",
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
    "old": {
      "definition_site": "009ee378",
      "incomplete_value": false,
      "site": "009ee37c",
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
            "const:d38:8"
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
      "definition_site": "009ee3ec",
      "incomplete_value": true,
      "site": "009ee3fc",
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
                "const:2c3000:8"
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
      "definition_site": "009ee398",
      "incomplete_value": true,
      "site": "009ee3a8",
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
                "const:2c3000:8"
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
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009ee3e8",
      "incomplete_value": true,
      "site": "009ee400",
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
                "const:2ba000:8"
              ],
              [
                "leaf",
                "const:abc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ee394",
      "incomplete_value": true,
      "site": "009ee3ac",
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
                "const:2ba000:8"
              ],
              [
                "leaf",
                "const:b10:8"
              ]
            ]
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
      "009ee3d0",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "009ee3e8",
      "READ",
      [
        "storage",
        "002bab10",
        null,
        "string"
      ]
    ],
    [
      "009ee3e8",
      "READ",
      [
        "storage",
        "002bab20",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009ee3d0",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ],
    [
      "009ee3e8",
      "READ",
      [
        "storage",
        "002baabc",
        null,
        "string"
      ]
    ],
    [
      "009ee3e8",
      "READ",
      [
        "storage",
        "002baacc",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009ee400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ee/009ee334.md#insn-009ee400) · [`009ee6d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ee/009ee334.md#insn-009ee6d0) · [`009ee6f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ee/009ee334.md#insn-009ee6f4)
- 新版 [`009ee454`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ee/009ee388.md#insn-009ee454) · [`009ee724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ee/009ee388.md#insn-009ee724) · [`009ee748`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ee/009ee388.md#insn-009ee748)

~~~diff
- 009ee400 ["INT_ADD", "register:40f0:8", ["const:9ee400:8", "const:4:8"]]
- 009ee400 ["CALL", null, ["callee:00596f6c:8"]]
+ 009ee454 ["INT_ADD", "register:40f0:8", ["const:9ee454:8", "const:4:8"]]
+ 009ee454 ["CALL", null, ["callee:00596f6c:8"]]
- 009ee400 bytes cba2ee97
+ 009ee454 bytes c6a2ee97
- 009ee6d0 ["COPY", "register:0:8", ["register:4048:8"]]
- 009ee6d0 ["INT_ADD", "register:40f0:8", ["const:9ee6d0:8", "const:4:8"]]
- 009ee6d0 ["CALLIND", null, ["register:0:8"]]
+ 009ee724 ["COPY", "register:0:8", ["register:4048:8"]]
+ 009ee724 ["INT_ADD", "register:40f0:8", ["const:9ee724:8", "const:4:8"]]
+ 009ee724 ["CALLIND", null, ["register:0:8"]]
- 009ee6d0 bytes 20013fd6
+ 009ee724 bytes 20013fd6
- 009ee6f4 ["COPY", "tmp:0:8", ["const:73a:8"]]
- 009ee6f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009ee6f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009ee6f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009ee748 ["COPY", "tmp:0:8", ["const:6ed:8"]]
+ 009ee748 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009ee748 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009ee748 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009ee6f4 bytes 08e91c91
+ 009ee748 bytes 08b51b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4e7217b1c7ab38eb04d9b7dcf86bfd2"></a>

### [`009ee970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ee/009ee970.md) → [`009ee9c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ee/009ee9c4.md) FUN_009ee9c4

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`009eecb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ee/009eecb0.md) · 呼出先 8件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`009f2de4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2de4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`009eed04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ee/009eed04.md) · 呼出先 8件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`009f2e38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2e38.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.72% / 新版 95.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009eea1c",
      "incomplete_value": true,
      "site": "009eea1c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2aa000:8"
              ],
              [
                "leaf",
                "const:39f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ee9c8",
      "incomplete_value": true,
      "site": "009ee9c8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2aa000:8"
              ],
              [
                "leaf",
                "const:3fb:8"
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
      "009ee9f4",
      "READ",
      [
        "storage",
        "002aa3fb",
        null,
        "string"
      ]
    ],
    [
      "009eea38",
      "READ",
      [
        "storage",
        "002b55e8",
        null,
        "string"
      ]
    ],
    [
      "009eea38",
      "READ",
      [
        "storage",
        "002b55f8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009ee9f4",
      "READ",
      [
        "storage",
        "002aa39f",
        null,
        "string"
      ]
    ],
    [
      "009eea38",
      "READ",
      [
        "storage",
        "002b5619",
        null,
        "string"
      ]
    ],
    [
      "009eea38",
      "READ",
      [
        "storage",
        "002b5629",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009eea1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ee/009ee970.md#insn-009eea1c) · [`009ee998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ee/009ee970.md#insn-009ee998) · [`009ee9d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ee/009ee970.md#insn-009ee9d4)
- 新版 [`009eea70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ee/009ee9c4.md#insn-009eea70) · [`009ee9ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ee/009ee9c4.md#insn-009ee9ec) · [`009eea28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ee/009ee9c4.md#insn-009eea28)

~~~diff
- 009eea1c ["INT_ADD", "register:40f0:8", ["const:9eea1c:8", "const:4:8"]]
- 009eea1c ["CALL", null, ["callee:004410cc:8"]]
+ 009eea70 ["INT_ADD", "register:40f0:8", ["const:9eea70:8", "const:4:8"]]
+ 009eea70 ["CALL", null, ["callee:004410cc:8"]]
- 009eea1c bytes 9c49e997
+ 009eea70 bytes 9749e997
- 009ee998 ["COPY", "tmp:0:8", ["const:3fb:8"]]
- 009ee998 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 009ee998 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 009ee998 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 009ee9ec ["COPY", "tmp:0:8", ["const:39f:8"]]
+ 009ee9ec ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 009ee9ec ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 009ee9ec ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 009ee998 bytes 4aed0f91
+ 009ee9ec bytes 4a7d0e91
- 009ee9d4 ["INT_ADD", "register:40f0:8", ["const:9ee9d4:8", "const:4:8"]]
- 009ee9d4 ["CALL", null, ["callee:00c57f60:8"]]
+ 009eea28 ["INT_ADD", "register:40f0:8", ["const:9eea28:8", "const:4:8"]]
+ 009eea28 ["CALL", null, ["callee:00c57f60:8"]]
- 009ee9d4 bytes 2fa50994
+ 009eea28 bytes 4ea50994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6fc44b4cfa80f3f5032b22a489a00402"></a>

### [`009ef024`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ef/009ef024.md) → [`009ef078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ef/009ef078.md) FUN_009ef078

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`009ef8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ef/009ef8e0.md) · 呼出先 20件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md) [`00488434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488434.md)
- 新版 呼出元 1件 [`009ef934`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ef/009ef934.md) · 呼出先 20件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00487e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487e60.md) [`00488474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/00488474.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.05% / 新版 92.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 9件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009ef0bc",
      "incomplete_value": false,
      "site": "009ef0c0",
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
    "old": {
      "definition_site": "009ef068",
      "incomplete_value": false,
      "site": "009ef06c",
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
            "const:d38:8"
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
      "definition_site": "009ef0d8",
      "incomplete_value": true,
      "site": "009ef0e8",
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
                "const:2aa000:8"
              ],
              [
                "leaf",
                "const:3ac:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ef084",
      "incomplete_value": true,
      "site": "009ef094",
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
                "const:2aa000:8"
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009ef0dc",
      "incomplete_value": true,
      "site": "009ef0ec",
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
                "const:c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ef088",
      "incomplete_value": true,
      "site": "009ef098",
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
                "const:c:8"
              ]
            ]
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
      "009ef0c0",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "009ef0d8",
      "READ",
      [
        "storage",
        "002aa408",
        null,
        "string"
      ]
    ],
    [
      "009ef0dc",
      "READ",
      [
        "storage",
        "002aa414",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009ef0c0",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ],
    [
      "009ef0d8",
      "READ",
      [
        "storage",
        "002aa3ac",
        null,
        "string"
      ]
    ],
    [
      "009ef0dc",
      "READ",
      [
        "storage",
        "002aa3b8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009ef0f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ef/009ef024.md#insn-009ef0f0) · [`009ef060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ef/009ef024.md#insn-009ef060) · [`009ef068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ef/009ef024.md#insn-009ef068)
- 新版 [`009ef144`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ef/009ef078.md#insn-009ef144) · [`009ef0b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ef/009ef078.md#insn-009ef0b4) · [`009ef0bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ef/009ef078.md#insn-009ef0bc)

~~~diff
- 009ef0f0 ["INT_ADD", "register:40f0:8", ["const:9ef0f0:8", "const:4:8"]]
- 009ef0f0 ["CALL", null, ["callee:00596f6c:8"]]
+ 009ef144 ["INT_ADD", "register:40f0:8", ["const:9ef144:8", "const:4:8"]]
+ 009ef144 ["CALL", null, ["callee:00596f6c:8"]]
- 009ef0f0 bytes 8f9fee97
+ 009ef144 bytes 8a9fee97
- 009ef060 ["INT_ADD", "register:40f0:8", ["const:9ef060:8", "const:4:8"]]
- 009ef060 ["CALL", null, ["callee:00487e60:8"]]
+ 009ef0b4 ["INT_ADD", "register:40f0:8", ["const:9ef0b4:8", "const:4:8"]]
+ 009ef0b4 ["CALL", null, ["callee:00487e60:8"]]
- 009ef060 bytes 7063ea97
+ 009ef0b4 bytes 6b63ea97
- 009ef068 ["COPY", "tmp:0:8", ["const:d38:8"]]
- 009ef068 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009ef068 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009ef068 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009ef0bc ["COPY", "tmp:0:8", ["const:e08:8"]]
+ 009ef0bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009ef0bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009ef0bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009ef068 bytes 08e13491
+ 009ef0bc bytes 08213891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e991a7c593f7fe23a5ac737bd7ee3943"></a>

### [`009ef66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ef/009ef66c.md) → [`009ef6c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ef/009ef6c0.md) FUN_009ef6c0

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009f2604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2604.md) · 呼出先 2件 [`009f38e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f38e4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`009f2658`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2658.md) · 呼出先 2件 [`009f3938`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3938.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.27% / 新版 97.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009ef70c",
      "incomplete_value": false,
      "site": "009ef710",
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
            "const:f28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ef6b8",
      "incomplete_value": false,
      "site": "009ef6bc",
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
            "const:e58:8"
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
      "009ef710",
      "DATA",
      [
        "storage",
        "00c89e58",
        null,
        "undefined *"
      ]
    ],
    [
      "009ef7e0",
      "DATA",
      [
        "storage",
        "00c8a3b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009ef710",
      "DATA",
      [
        "storage",
        "00c89f28",
        null,
        "undefined *"
      ]
    ],
    [
      "009ef7e0",
      "DATA",
      [
        "storage",
        "00c8a480",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009ef6b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ef/009ef66c.md#insn-009ef6b8) · [`009ef76c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ef/009ef66c.md#insn-009ef76c) · [`009ef77c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ef/009ef66c.md#insn-009ef77c)
- 新版 [`009ef70c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ef/009ef6c0.md#insn-009ef70c) · [`009ef7c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ef/009ef6c0.md#insn-009ef7c0) · [`009ef7d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ef/009ef6c0.md#insn-009ef7d0)

~~~diff
- 009ef6b8 ["COPY", "tmp:0:8", ["const:e58:8"]]
- 009ef6b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009ef6b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009ef6b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009ef70c ["COPY", "tmp:0:8", ["const:f28:8"]]
+ 009ef70c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009ef70c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009ef70c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009ef6b8 bytes 08613991
+ 009ef70c bytes 08a13c91
- 009ef76c ["COPY", "register:0:8", ["register:4048:8"]]
- 009ef76c ["INT_ADD", "register:40f0:8", ["const:9ef76c:8", "const:4:8"]]
- 009ef76c ["CALLIND", null, ["register:0:8"]]
+ 009ef7c0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 009ef7c0 ["INT_ADD", "register:40f0:8", ["const:9ef7c0:8", "const:4:8"]]
+ 009ef7c0 ["CALLIND", null, ["register:0:8"]]
- 009ef76c bytes 20013fd6
+ 009ef7c0 bytes 20013fd6
- 009ef77c ["COPY", "tmp:0:8", ["const:3b0:8"]]
- 009ef77c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009ef77c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009ef77c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009ef7d0 ["COPY", "tmp:0:8", ["const:480:8"]]
+ 009ef7d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009ef7d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009ef7d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009ef77c bytes 08c10e91
+ 009ef7d0 bytes 08011291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0148e33bd1a855f924ca6dfda033dd2"></a>

### [`009efde8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ef/009efde8.md) → [`009efe3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ef/009efe3c.md) FUN_009efe3c

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`009f050c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f0/009f050c.md) [`009f0d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f0/009f0d34.md) · 呼出先 9件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`009f3ab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3ab8.md) [`009f3acc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3acc.md)
- 新版 呼出元 2件 [`009f0560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f0/009f0560.md) [`009f0d88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f0/009f0d88.md) · 呼出先 9件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`009f3b0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3b0c.md) [`009f3b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3b20.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.05% / 新版 95.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009f0218",
      "incomplete_value": true,
      "site": "009f0220",
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
                "const:280:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f01c4",
      "incomplete_value": true,
      "site": "009f01cc",
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
                "const:240:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 48,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009f0214",
      "incomplete_value": true,
      "site": "009f0224",
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
                "const:d97:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f01c0",
      "incomplete_value": true,
      "site": "009f01d0",
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
                "const:df3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 49,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009f0214",
      "incomplete_value": true,
      "site": "009f0224",
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
      "definition_site": "009f01c0",
      "incomplete_value": true,
      "site": "009f01d0",
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
    "ordinal": 50,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009f0214",
      "READ",
      [
        "storage",
        "002a5df3",
        null,
        "string"
      ]
    ],
    [
      "009f0214",
      "READ",
      [
        "storage",
        "002a5e03",
        null,
        "string"
      ]
    ],
    [
      "009f0218",
      "READ",
      [
        "storage",
        "002c2240",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009f0214",
      "READ",
      [
        "storage",
        "002a5d97",
        null,
        "string"
      ]
    ],
    [
      "009f0214",
      "READ",
      [
        "storage",
        "002a5da7",
        null,
        "string"
      ]
    ],
    [
      "009f0218",
      "READ",
      [
        "storage",
        "002c2280",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f017c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ef/009efde8.md#insn-009f017c) · [`009f01f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ef/009efde8.md#insn-009f01f4) · [`009f0224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ef/009efde8.md#insn-009f0224)
- 新版 [`009f01d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ef/009efe3c.md#insn-009f01d0) · [`009f0248`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ef/009efe3c.md#insn-009f0248) · [`009f0278`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ef/009efe3c.md#insn-009f0278)

~~~diff
- 009f017c ["INT_ADD", "register:40f0:8", ["const:9f017c:8", "const:4:8"]]
- 009f017c ["CALL", null, ["callee:009f3b20:8"]]
+ 009f01d0 ["INT_ADD", "register:40f0:8", ["const:9f01d0:8", "const:4:8"]]
+ 009f01d0 ["CALL", null, ["callee:009f3b20:8"]]
- 009f017c bytes 540e0094
+ 009f01d0 bytes 540e0094
- 009f01f4 ["INT_ADD", "register:40f0:8", ["const:9f01f4:8", "const:4:8"]]
- 009f01f4 ["CALL", null, ["callee:00447f34:8"]]
+ 009f0248 ["INT_ADD", "register:40f0:8", ["const:9f0248:8", "const:4:8"]]
+ 009f0248 ["CALL", null, ["callee:00447f34:8"]]
- 009f01f4 bytes 405fe997
+ 009f0248 bytes 3b5fe997
- 009f0224 ["COPY", "tmp:0:8", ["const:3f2:8"]]
- 009f0224 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f0224 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f0224 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f0278 ["COPY", "tmp:0:8", ["const:423:8"]]
+ 009f0278 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f0278 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f0278 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f0224 bytes 08c90f91
+ 009f0278 bytes 088d1091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6917f7586a7052d13adcc3c4f9721b70"></a>

### [`009f050c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f0/009f050c.md) → [`009f0560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f0/009f0560.md) FUN_009f0560

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009f24a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f24a4.md) · 呼出先 11件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0046d7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7b0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`009efde8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ef/009efde8.md) [`009f3ab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3ab8.md)
- 新版 呼出元 1件 [`009f24f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f24f8.md) · 呼出先 11件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0046d7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d7f0.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`009efe3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ef/009efe3c.md) [`009f3b0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3b0c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.18% / 新版 99.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009f064c",
      "incomplete_value": false,
      "site": "009f065c",
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
            "const:f88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f05f8",
      "incomplete_value": false,
      "site": "009f0608",
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
            "const:eb8:8"
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
      "definition_site": "009f0654",
      "incomplete_value": false,
      "site": "009f065c",
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
            "const:fe0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f0600",
      "incomplete_value": false,
      "site": "009f0608",
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
            "const:f10:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009f06c0",
      "incomplete_value": false,
      "site": "009f06d0",
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
            "const:f88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f066c",
      "incomplete_value": false,
      "site": "009f067c",
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
            "const:eb8:8"
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
      "009f064c",
      "PARAM",
      [
        "storage",
        "00c89eb8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009f0654",
      "PARAM",
      [
        "storage",
        "00c89f10",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009f06c0",
      "PARAM",
      [
        "storage",
        "00c89eb8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "009f064c",
      "PARAM",
      [
        "storage",
        "00c89f88",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009f0654",
      "PARAM",
      [
        "storage",
        "00c89fe0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009f06c0",
      "PARAM",
      [
        "storage",
        "00c89f88",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f0608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f0/009f050c.md#insn-009f0608) · [`009f067c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f0/009f050c.md#insn-009f067c) · [`009f0558`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f0/009f050c.md#insn-009f0558)
- 新版 [`009f065c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f0/009f0560.md#insn-009f065c) · [`009f06d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f0/009f0560.md#insn-009f06d0) · [`009f05ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f0/009f0560.md#insn-009f05ac)

~~~diff
- 009f0608 ["INT_ADD", "register:40f0:8", ["const:9f0608:8", "const:4:8"]]
- 009f0608 ["CALL", null, ["callee:00c586e0:8"]]
+ 009f065c ["INT_ADD", "register:40f0:8", ["const:9f065c:8", "const:4:8"]]
+ 009f065c ["CALL", null, ["callee:00c586e0:8"]]
- 009f0608 bytes 02a00994
+ 009f065c bytes 21a00994
- 009f067c ["INT_ADD", "register:40f0:8", ["const:9f067c:8", "const:4:8"]]
- 009f067c ["CALL", null, ["callee:00c586e0:8"]]
+ 009f06d0 ["INT_ADD", "register:40f0:8", ["const:9f06d0:8", "const:4:8"]]
+ 009f06d0 ["CALL", null, ["callee:00c586e0:8"]]
- 009f067c bytes e59f0994
+ 009f06d0 bytes 04a00994
- 009f0558 ["INT_ADD", "register:40f0:8", ["const:9f0558:8", "const:4:8"]]
- 009f0558 ["CALL", null, ["callee:009efe3c:8"]]
+ 009f05ac ["INT_ADD", "register:40f0:8", ["const:9f05ac:8", "const:4:8"]]
+ 009f05ac ["CALL", null, ["callee:009efe3c:8"]]
- 009f0558 bytes 24feff97
+ 009f05ac bytes 24feff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bec440c95d73f06cfab653ab53c0b691"></a>

### [`009f0d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f0/009f0d34.md) → [`009f0d88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f0/009f0d88.md) FUN_009f0d88

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`009efde8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ef/009efde8.md) [`009f1048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f1/009f1048.md) [`009f37fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f37fc.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`009efe3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ef/009efe3c.md) [`009f109c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f1/009f109c.md) [`009f3850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3850.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.71% / 新版 95.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009f0e48",
      "incomplete_value": true,
      "site": "009f0e58",
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
                "const:100:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f0df4",
      "incomplete_value": true,
      "site": "009f0e04",
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
                "const:c0:8"
              ]
            ]
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
      "definition_site": "009f0e4c",
      "incomplete_value": true,
      "site": "009f0e68",
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
                "const:217:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f0df8",
      "incomplete_value": true,
      "site": "009f0e14",
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
                "const:1e6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009f0e4c",
      "incomplete_value": true,
      "site": "009f0e68",
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
      "definition_site": "009f0df8",
      "incomplete_value": true,
      "site": "009f0e14",
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
      "009f0e48",
      "READ",
      [
        "storage",
        "002c20c0",
        null,
        null
      ]
    ],
    [
      "009f0e4c",
      "READ",
      [
        "storage",
        "002b31e6",
        null,
        "string"
      ]
    ],
    [
      "009f0e4c",
      "READ",
      [
        "storage",
        "002b31f6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009f0e48",
      "READ",
      [
        "storage",
        "002c2100",
        null,
        null
      ]
    ],
    [
      "009f0e4c",
      "READ",
      [
        "storage",
        "002b3217",
        null,
        "string"
      ]
    ],
    [
      "009f0e4c",
      "READ",
      [
        "storage",
        "002b3227",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f0e58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f0/009f0d34.md#insn-009f0e58) · [`009f0e68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f0/009f0d34.md#insn-009f0e68) · [`009f0d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f0/009f0d34.md#insn-009f0d8c)
- 新版 [`009f0eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f0/009f0d88.md#insn-009f0eac) · [`009f0ebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f0/009f0d88.md#insn-009f0ebc) · [`009f0de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f0/009f0d88.md#insn-009f0de0)

~~~diff
- 009f0e58 ["INT_ADD", "register:40f0:8", ["const:9f0e58:8", "const:4:8"]]
- 009f0e58 ["CALL", null, ["callee:00c57f80:8"]]
+ 009f0eac ["INT_ADD", "register:40f0:8", ["const:9f0eac:8", "const:4:8"]]
+ 009f0eac ["CALL", null, ["callee:00c57f80:8"]]
- 009f0e58 bytes 169c0994
+ 009f0eac bytes 359c0994
- 009f0e68 ["INT_ADD", "register:40f0:8", ["const:9f0e68:8", "const:4:8"]]
- 009f0e68 ["CALL", null, ["callee:00c57f80:8"]]
+ 009f0ebc ["INT_ADD", "register:40f0:8", ["const:9f0ebc:8", "const:4:8"]]
+ 009f0ebc ["CALL", null, ["callee:00c57f80:8"]]
- 009f0e68 bytes 129c0994
+ 009f0ebc bytes 319c0994
- 009f0d8c ["INT_ADD", "register:40f0:8", ["const:9f0d8c:8", "const:4:8"]]
- 009f0d8c ["CALL", null, ["callee:009f3f88:8"]]
+ 009f0de0 ["INT_ADD", "register:40f0:8", ["const:9f0de0:8", "const:4:8"]]
+ 009f0de0 ["CALL", null, ["callee:009f3f88:8"]]
- 009f0d8c bytes 6a0c0094
+ 009f0de0 bytes 6a0c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de2f34e18276134aa6a827a2ea41841b"></a>

### [`009f1978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f1/009f1978.md) → [`009f19cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f1/009f19cc.md) FUN_009f19cc

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 9件 [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`009f35fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f35fc.md) [`009f3894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3894.md) [`009f3f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3f34.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`009f3650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3650.md) [`009f38e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f38e8.md) [`009f3f88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3f88.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.73% / 新版 93.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009f1a90",
      "incomplete_value": true,
      "site": "009f1aa0",
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
                "const:100:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f1a3c",
      "incomplete_value": true,
      "site": "009f1a4c",
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
                "const:c0:8"
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
      "definition_site": "009f1a94",
      "incomplete_value": true,
      "site": "009f1ab0",
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
                "const:217:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f1a40",
      "incomplete_value": true,
      "site": "009f1a5c",
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
                "const:1e6:8"
              ]
            ]
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
      "definition_site": "009f1a94",
      "incomplete_value": true,
      "site": "009f1ab0",
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
      "definition_site": "009f1a40",
      "incomplete_value": true,
      "site": "009f1a5c",
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
    "ordinal": 22,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009f1a90",
      "READ",
      [
        "storage",
        "002c20c0",
        null,
        null
      ]
    ],
    [
      "009f1a94",
      "READ",
      [
        "storage",
        "002b31e6",
        null,
        "string"
      ]
    ],
    [
      "009f1a94",
      "READ",
      [
        "storage",
        "002b31f6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009f1a90",
      "READ",
      [
        "storage",
        "002c2100",
        null,
        null
      ]
    ],
    [
      "009f1a94",
      "READ",
      [
        "storage",
        "002b3217",
        null,
        "string"
      ]
    ],
    [
      "009f1a94",
      "READ",
      [
        "storage",
        "002b3227",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f1d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f1/009f1978.md#insn-009f1d08) · [`009f1d18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f1/009f1978.md#insn-009f1d18) · [`009f19d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f1/009f1978.md#insn-009f19d4)
- 新版 [`009f1d5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f1/009f19cc.md#insn-009f1d5c) · [`009f1d6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f1/009f19cc.md#insn-009f1d6c) · [`009f1a28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f1/009f19cc.md#insn-009f1a28)

~~~diff
- 009f1d08 ["INT_ADD", "register:40f0:8", ["const:9f1d08:8", "const:4:8"]]
- 009f1d08 ["CALL", null, ["callee:00c57f80:8"]]
+ 009f1d5c ["INT_ADD", "register:40f0:8", ["const:9f1d5c:8", "const:4:8"]]
+ 009f1d5c ["CALL", null, ["callee:00c57f80:8"]]
- 009f1d08 bytes 6a980994
+ 009f1d5c bytes 89980994
- 009f1d18 ["INT_ADD", "register:40f0:8", ["const:9f1d18:8", "const:4:8"]]
- 009f1d18 ["CALL", null, ["callee:00c57f80:8"]]
+ 009f1d6c ["INT_ADD", "register:40f0:8", ["const:9f1d6c:8", "const:4:8"]]
+ 009f1d6c ["CALL", null, ["callee:00c57f80:8"]]
- 009f1d18 bytes 66980994
+ 009f1d6c bytes 85980994
- 009f19d4 ["INT_ADD", "register:40f0:8", ["const:9f19d4:8", "const:4:8"]]
- 009f19d4 ["CALL", null, ["callee:009f3f88:8"]]
+ 009f1a28 ["INT_ADD", "register:40f0:8", ["const:9f1a28:8", "const:4:8"]]
+ 009f1a28 ["CALL", null, ["callee:009f3f88:8"]]
- 009f19d4 bytes 58090094
+ 009f1a28 bytes 58090094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0dd7b64415ee3bbeeeb566c69bb966c1"></a>

### [`009f1e4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f1/009f1e4c.md) → [`009f1ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f1/009f1ea0.md) FUN_009f1ea0

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 13件 [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`009f35fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f35fc.md) [`009f3764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3764.md) [`009f37fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f37fc.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`009f3650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3650.md) [`009f37b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f37b8.md) [`009f3850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3850.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.99% / 新版 96.99%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009f1f68",
      "incomplete_value": true,
      "site": "009f1f78",
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
                "const:100:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f1f14",
      "incomplete_value": true,
      "site": "009f1f24",
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
                "const:c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009f1f6c",
      "incomplete_value": true,
      "site": "009f1f88",
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
                "const:217:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f1f18",
      "incomplete_value": true,
      "site": "009f1f34",
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
                "const:1e6:8"
              ]
            ]
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
      "definition_site": "009f1f6c",
      "incomplete_value": true,
      "site": "009f1f88",
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
      "definition_site": "009f1f18",
      "incomplete_value": true,
      "site": "009f1f34",
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
    "ordinal": 21,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009f1f68",
      "READ",
      [
        "storage",
        "002c20c0",
        null,
        null
      ]
    ],
    [
      "009f1f6c",
      "READ",
      [
        "storage",
        "002b31e6",
        null,
        "string"
      ]
    ],
    [
      "009f1f6c",
      "READ",
      [
        "storage",
        "002b31f6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009f1f68",
      "READ",
      [
        "storage",
        "002c2100",
        null,
        null
      ]
    ],
    [
      "009f1f6c",
      "READ",
      [
        "storage",
        "002b3217",
        null,
        "string"
      ]
    ],
    [
      "009f1f6c",
      "READ",
      [
        "storage",
        "002b3227",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f1f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f1/009f1e4c.md#insn-009f1f78) · [`009f1f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f1/009f1e4c.md#insn-009f1f88) · [`009f1eac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f1/009f1e4c.md#insn-009f1eac)
- 新版 [`009f1fcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f1/009f1ea0.md#insn-009f1fcc) · [`009f1fdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f1/009f1ea0.md#insn-009f1fdc) · [`009f1f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f1/009f1ea0.md#insn-009f1f00)

~~~diff
- 009f1f78 ["INT_ADD", "register:40f0:8", ["const:9f1f78:8", "const:4:8"]]
- 009f1f78 ["CALL", null, ["callee:00c57f80:8"]]
+ 009f1fcc ["INT_ADD", "register:40f0:8", ["const:9f1fcc:8", "const:4:8"]]
+ 009f1fcc ["CALL", null, ["callee:00c57f80:8"]]
- 009f1f78 bytes ce970994
+ 009f1fcc bytes ed970994
- 009f1f88 ["INT_ADD", "register:40f0:8", ["const:9f1f88:8", "const:4:8"]]
- 009f1f88 ["CALL", null, ["callee:00c57f80:8"]]
+ 009f1fdc ["INT_ADD", "register:40f0:8", ["const:9f1fdc:8", "const:4:8"]]
+ 009f1fdc ["CALL", null, ["callee:00c57f80:8"]]
- 009f1f88 bytes ca970994
+ 009f1fdc bytes e9970994
- 009f1eac ["INT_ADD", "register:40f0:8", ["const:9f1eac:8", "const:4:8"]]
- 009f1eac ["CALL", null, ["callee:009f3f88:8"]]
+ 009f1f00 ["INT_ADD", "register:40f0:8", ["const:9f1f00:8", "const:4:8"]]
+ 009f1f00 ["CALL", null, ["callee:009f3f88:8"]]
- 009f1eac bytes 22080094
+ 009f1f00 bytes 22080094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73f2d9d2592474e74b9f4d6d7cfb808f"></a>

### [`009f2604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2604.md) → [`009f2658`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2658.md) FUN_009f2658

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`009e01d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e0/009e01d4.md) · 呼出先 2件 [`009ef66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ef/009ef66c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`009e0228`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e0/009e0228.md) · 呼出先 2件 [`009ef6c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ef/009ef6c0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009f2680",
      "incomplete_value": false,
      "site": "009f268c",
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
            "const:500:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f262c",
      "incomplete_value": false,
      "site": "009f2638",
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
            "const:430:8"
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
      "009f268c",
      "DATA",
      [
        "storage",
        "00c8a430",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f268c",
      "DATA",
      [
        "storage",
        "00c8a500",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f2620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2604.md#insn-009f2620) · [`009f262c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2604.md#insn-009f262c) · [`009f2644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2604.md#insn-009f2644)
- 新版 [`009f2674`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2658.md#insn-009f2674) · [`009f2680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2658.md#insn-009f2680) · [`009f2698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2658.md#insn-009f2698)

~~~diff
- 009f2620 ["INT_ADD", "register:40f0:8", ["const:9f2620:8", "const:4:8"]]
- 009f2620 ["CALL", null, ["callee:00c57f60:8"]]
+ 009f2674 ["INT_ADD", "register:40f0:8", ["const:9f2674:8", "const:4:8"]]
+ 009f2674 ["CALL", null, ["callee:00c57f60:8"]]
- 009f2620 bytes 1c960994
+ 009f2674 bytes 3b960994
- 009f262c ["COPY", "tmp:0:8", ["const:430:8"]]
- 009f262c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f262c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f262c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f2680 ["COPY", "tmp:0:8", ["const:500:8"]]
+ 009f2680 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f2680 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f2680 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f262c bytes 08c11091
+ 009f2680 bytes 08011491
- 009f2644 ["INT_ADD", "register:40f0:8", ["const:9f2644:8", "const:4:8"]]
- 009f2644 ["CALL", null, ["callee:009ef6c0:8"]]
+ 009f2698 ["INT_ADD", "register:40f0:8", ["const:9f2698:8", "const:4:8"]]
+ 009f2698 ["CALL", null, ["callee:009ef6c0:8"]]
- 009f2644 bytes 0af4ff97
+ 009f2698 bytes 0af4ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c02e0d1138a8822d5383646518b80e8f"></a>

### [`009f26ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f26ac.md) → [`009f2700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2700.md) FUN_009f2700

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.74% / 新版 95.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009f271c",
      "incomplete_value": false,
      "site": "009f2720",
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
            "const:80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f26c8",
      "incomplete_value": false,
      "site": "009f26cc",
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
            "const:fb0:8"
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
      "009f2720",
      "DATA",
      [
        "storage",
        "00c89fb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f2720",
      "DATA",
      [
        "storage",
        "00c8a080",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f2720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f26ac.md#insn-009f2720) · [`009f26c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f26ac.md#insn-009f26c4) · [`009f26c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f26ac.md#insn-009f26c8)
- 新版 [`009f2774`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2700.md#insn-009f2774) · [`009f2718`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2700.md#insn-009f2718) · [`009f271c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2700.md#insn-009f271c)

~~~diff
- 009f2720 ["INT_ADD", "register:40f0:8", ["const:9f2720:8", "const:4:8"]]
- 009f2720 ["CALL", null, ["callee:00c57f50:8"]]
+ 009f2774 ["INT_ADD", "register:40f0:8", ["const:9f2774:8", "const:4:8"]]
+ 009f2774 ["CALL", null, ["callee:00c57f50:8"]]
- 009f2720 bytes d8950994
+ 009f2774 bytes f7950994
- 009f26c4 ["COPY", "register:4040:8", ["const:c89000:8"]]
+ 009f2718 ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 009f26c4 bytes a81400f0
+ 009f2718 bytes c8140090
- 009f26c8 ["COPY", "tmp:0:8", ["const:fb0:8"]]
- 009f26c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f26c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f26c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f271c ["COPY", "tmp:0:8", ["const:80:8"]]
+ 009f271c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f271c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f271c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f26c8 bytes 08c13e91
+ 009f271c bytes 08010291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57e409545440bca49fe7d8c93f3b76b2"></a>

### [`009f2a14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2a14.md) → [`009f2a68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2a68.md) FUN_009f2a68

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009f29c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f29c8.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`009f2a1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2a1c.md) · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.92% / 新版 95.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009f2a84",
      "incomplete_value": false,
      "site": "009f2a88",
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
            "const:80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f2a30",
      "incomplete_value": false,
      "site": "009f2a34",
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
            "const:fb0:8"
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
      "009f2a88",
      "DATA",
      [
        "storage",
        "00c89fb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f2a88",
      "DATA",
      [
        "storage",
        "00c8a080",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f2a88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2a14.md#insn-009f2a88) · [`009f2a2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2a14.md#insn-009f2a2c) · [`009f2a30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2a14.md#insn-009f2a30)
- 新版 [`009f2adc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2a68.md#insn-009f2adc) · [`009f2a80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2a68.md#insn-009f2a80) · [`009f2a84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2a68.md#insn-009f2a84)

~~~diff
- 009f2a88 ["INT_ADD", "register:40f0:8", ["const:9f2a88:8", "const:4:8"]]
- 009f2a88 ["CALL", null, ["callee:00c57f50:8"]]
+ 009f2adc ["INT_ADD", "register:40f0:8", ["const:9f2adc:8", "const:4:8"]]
+ 009f2adc ["CALL", null, ["callee:00c57f50:8"]]
- 009f2a88 bytes fe940994
+ 009f2adc bytes 1d950994
- 009f2a2c ["COPY", "register:4040:8", ["const:c89000:8"]]
+ 009f2a80 ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 009f2a2c bytes a81400f0
+ 009f2a80 bytes c8140090
- 009f2a30 ["COPY", "tmp:0:8", ["const:fb0:8"]]
- 009f2a30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f2a30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f2a30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f2a84 ["COPY", "tmp:0:8", ["const:80:8"]]
+ 009f2a84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f2a84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f2a84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f2a30 bytes 08c13e91
+ 009f2a84 bytes 08010291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a38f060d8f38907344ce6f231ee4edae"></a>

### [`009f2de4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2de4.md) → [`009f2e38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2e38.md) FUN_009f2e38

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`009edb3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ed/009edb3c.md) [`009ee970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ee/009ee970.md) [`009f2b1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2b1c.md) [`009f45a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f45a4.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 4件 [`009edb90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ed/009edb90.md) [`009ee9c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ee/009ee9c4.md) [`009f2b70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2b70.md) [`009f45f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f45f8.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "009f2e44",
      "incomplete_value": false,
      "site": "009f2e48",
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
      "definition_site": "009f2df0",
      "incomplete_value": false,
      "site": "009f2df4",
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
      "009f2e44",
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
      "009f2e44",
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

- 旧版 [`009f2df4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2de4.md#insn-009f2df4) · [`009f2df0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2de4.md#insn-009f2df0)
- 新版 [`009f2e48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2e38.md#insn-009f2e48) · [`009f2e44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2e38.md#insn-009f2e44)

~~~diff
- 009f2df4 ["INT_ADD", "register:40f0:8", ["const:9f2df4:8", "const:4:8"]]
- 009f2df4 ["CALL", null, ["callee:0043b7b8:8"]]
+ 009f2e48 ["INT_ADD", "register:40f0:8", ["const:9f2e48:8", "const:4:8"]]
+ 009f2e48 ["CALL", null, ["callee:0043b7b8:8"]]
- 009f2df4 bytes 6122e997
+ 009f2e48 bytes 5c22e997
- 009f2df0 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 009f2df0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 009f2df0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 009f2df0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 009f2e44 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 009f2e44 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 009f2e44 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 009f2e44 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 009f2df0 bytes 00303d91
+ 009f2e44 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b84a7c47e55365fb18317d11c06c61ba"></a>

### [`009f2df8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2df8.md) → [`009f2e4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2e4c.md) FUN_009f2e4c

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md)

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
      "definition_site": "009f2e50",
      "incomplete_value": false,
      "site": "009f2e54",
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
            "const:e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f2dfc",
      "incomplete_value": false,
      "site": "009f2e00",
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
      "009f2e54",
      "DATA",
      [
        "storage",
        "00c8a010",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f2e54",
      "DATA",
      [
        "storage",
        "00c8a0e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f2dfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2df8.md#insn-009f2dfc)
- 新版 [`009f2e50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2e4c.md#insn-009f2e50)

~~~diff
- 009f2dfc ["COPY", "tmp:0:8", ["const:10:8"]]
- 009f2dfc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f2dfc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f2dfc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f2e50 ["COPY", "tmp:0:8", ["const:e0:8"]]
+ 009f2e50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f2e50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f2e50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f2dfc bytes 08410091
+ 009f2e50 bytes 08810391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ef21baab94667fc1713da72ca0d61f9"></a>

### [`009f2e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2e08.md) → [`009f2e5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2e5c.md) FUN_009f2e5c

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009f2e6c",
      "incomplete_value": false,
      "site": "009f2e74",
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
            "const:e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f2e18",
      "incomplete_value": false,
      "site": "009f2e20",
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
      "009f2e74",
      "DATA",
      [
        "storage",
        "00c8a010",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f2e74",
      "DATA",
      [
        "storage",
        "00c8a0e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f2e18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2e08.md#insn-009f2e18) · [`009f2e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2e08.md#insn-009f2e24)
- 新版 [`009f2e6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2e5c.md#insn-009f2e6c) · [`009f2e78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2e5c.md#insn-009f2e78)

~~~diff
- 009f2e18 ["COPY", "tmp:0:8", ["const:10:8"]]
- 009f2e18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f2e18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f2e18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f2e6c ["COPY", "tmp:0:8", ["const:e0:8"]]
+ 009f2e6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f2e6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f2e6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f2e18 bytes 08410091
+ 009f2e6c bytes 08810391
- 009f2e24 ["INT_ADD", "register:40f0:8", ["const:9f2e24:8", "const:4:8"]]
- 009f2e24 ["CALL", null, ["callee:00c57f70:8"]]
+ 009f2e78 ["INT_ADD", "register:40f0:8", ["const:9f2e78:8", "const:4:8"]]
+ 009f2e78 ["CALL", null, ["callee:00c57f70:8"]]
- 009f2e24 bytes 1f940994
+ 009f2e78 bytes 3e940994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-503059bbcf0fec5e9d4deef8307a0b45"></a>

### [`009f2fa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2fa4.md) → [`009f2ff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2ff8.md) FUN_009f2ff8

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`009f2e64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2e64.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 1件 [`009f2eb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2eb8.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "009f3004",
      "incomplete_value": false,
      "site": "009f3008",
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
      "definition_site": "009f2fb0",
      "incomplete_value": false,
      "site": "009f2fb4",
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
      "009f3004",
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
      "009f3004",
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

- 旧版 [`009f2fb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2fa4.md#insn-009f2fb4) · [`009f2fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2fa4.md#insn-009f2fb0)
- 新版 [`009f3008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2ff8.md#insn-009f3008) · [`009f3004`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2ff8.md#insn-009f3004)

~~~diff
- 009f2fb4 ["INT_ADD", "register:40f0:8", ["const:9f2fb4:8", "const:4:8"]]
- 009f2fb4 ["CALL", null, ["callee:0043b7b8:8"]]
+ 009f3008 ["INT_ADD", "register:40f0:8", ["const:9f3008:8", "const:4:8"]]
+ 009f3008 ["CALL", null, ["callee:0043b7b8:8"]]
- 009f2fb4 bytes f121e997
+ 009f3008 bytes ec21e997
- 009f2fb0 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 009f2fb0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 009f2fb0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 009f2fb0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 009f3004 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 009f3004 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 009f3004 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 009f3004 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 009f2fb0 bytes 00303d91
+ 009f3004 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2bcc75eec59774a03e6ce27cb810626b"></a>

### [`009f3088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3088.md) → [`009f30dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f30dc.md) FUN_009f30dc

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md)

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
      "definition_site": "009f30e0",
      "incomplete_value": false,
      "site": "009f30e4",
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
            "const:290:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f308c",
      "incomplete_value": false,
      "site": "009f3090",
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
            "const:1c0:8"
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
      "009f30e4",
      "DATA",
      [
        "storage",
        "00c8a1c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f30e4",
      "DATA",
      [
        "storage",
        "00c8a290",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f308c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3088.md#insn-009f308c)
- 新版 [`009f30e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f30dc.md#insn-009f30e0)

~~~diff
- 009f308c ["COPY", "tmp:0:8", ["const:1c0:8"]]
- 009f308c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f308c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f308c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f30e0 ["COPY", "tmp:0:8", ["const:290:8"]]
+ 009f30e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f30e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f30e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f308c bytes 08010791
+ 009f30e0 bytes 08410a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2696eb4c7e4dfd5f1a74e0c776c32675"></a>

### [`009f3098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3098.md) → [`009f30ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f30ec.md) FUN_009f30ec

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009f30fc",
      "incomplete_value": false,
      "site": "009f3104",
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
            "const:290:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f30a8",
      "incomplete_value": false,
      "site": "009f30b0",
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
            "const:1c0:8"
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
      "009f3104",
      "DATA",
      [
        "storage",
        "00c8a1c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f3104",
      "DATA",
      [
        "storage",
        "00c8a290",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f30a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3098.md#insn-009f30a8) · [`009f30b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3098.md#insn-009f30b4)
- 新版 [`009f30fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f30ec.md#insn-009f30fc) · [`009f3108`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f30ec.md#insn-009f3108)

~~~diff
- 009f30a8 ["COPY", "tmp:0:8", ["const:1c0:8"]]
- 009f30a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f30a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f30a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f30fc ["COPY", "tmp:0:8", ["const:290:8"]]
+ 009f30fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f30fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f30fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f30a8 bytes 08010791
+ 009f30fc bytes 08410a91
- 009f30b4 ["INT_ADD", "register:40f0:8", ["const:9f30b4:8", "const:4:8"]]
- 009f30b4 ["CALL", null, ["callee:00c57f70:8"]]
+ 009f3108 ["INT_ADD", "register:40f0:8", ["const:9f3108:8", "const:4:8"]]
+ 009f3108 ["CALL", null, ["callee:00c57f70:8"]]
- 009f30b4 bytes 7b930994
+ 009f3108 bytes 9a930994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fda04184c38d49fa91dd5580548cb7f8"></a>

### [`009f30f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f30f4.md) → [`009f3148`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3148.md) FUN_009f3148

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md)

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
      "definition_site": "009f314c",
      "incomplete_value": false,
      "site": "009f3150",
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
            "const:348:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f30f8",
      "incomplete_value": false,
      "site": "009f30fc",
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
            "const:278:8"
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
      "009f3150",
      "DATA",
      [
        "storage",
        "00c8a278",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f3150",
      "DATA",
      [
        "storage",
        "00c8a348",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f30f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f30f4.md#insn-009f30f8)
- 新版 [`009f314c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3148.md#insn-009f314c)

~~~diff
- 009f30f8 ["COPY", "tmp:0:8", ["const:278:8"]]
- 009f30f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f30f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f30f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f314c ["COPY", "tmp:0:8", ["const:348:8"]]
+ 009f314c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f314c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f314c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f30f8 bytes 08e10991
+ 009f314c bytes 08210d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4978698da272ad9aef00eb9b53fc4c4"></a>

### [`009f3104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3104.md) → [`009f3158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3158.md) FUN_009f3158

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009f3168",
      "incomplete_value": false,
      "site": "009f3170",
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
            "const:348:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f3114",
      "incomplete_value": false,
      "site": "009f311c",
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
            "const:278:8"
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
      "009f3170",
      "DATA",
      [
        "storage",
        "00c8a278",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f3170",
      "DATA",
      [
        "storage",
        "00c8a348",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f3114`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3104.md#insn-009f3114) · [`009f3120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3104.md#insn-009f3120)
- 新版 [`009f3168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3158.md#insn-009f3168) · [`009f3174`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3158.md#insn-009f3174)

~~~diff
- 009f3114 ["COPY", "tmp:0:8", ["const:278:8"]]
- 009f3114 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f3114 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f3114 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f3168 ["COPY", "tmp:0:8", ["const:348:8"]]
+ 009f3168 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f3168 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f3168 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f3114 bytes 08e10991
+ 009f3168 bytes 08210d91
- 009f3120 ["INT_ADD", "register:40f0:8", ["const:9f3120:8", "const:4:8"]]
- 009f3120 ["CALL", null, ["callee:00c57f70:8"]]
+ 009f3174 ["INT_ADD", "register:40f0:8", ["const:9f3174:8", "const:4:8"]]
+ 009f3174 ["CALL", null, ["callee:00c57f70:8"]]
- 009f3120 bytes 60930994
+ 009f3174 bytes 7f930994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be36f3a0211bf39beabfd02372908539"></a>

### [`009f3164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3164.md) → [`009f31b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f31b8.md) FUN_009f31b8

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`009ec250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ec/009ec250.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`009ec2a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ec/009ec2a4.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.50% / 新版 97.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009f3244",
      "incomplete_value": false,
      "site": "009f32ac",
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
            "const:80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f31f0",
      "incomplete_value": false,
      "site": "009f3258",
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
            "const:fb0:8"
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
      "009f32ac",
      "DATA",
      [
        "storage",
        "00c89fb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f32ac",
      "DATA",
      [
        "storage",
        "00c8a080",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f31d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3164.md#insn-009f31d8) · [`009f31ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3164.md#insn-009f31ec) · [`009f31f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3164.md#insn-009f31f0)
- 新版 [`009f322c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f31b8.md#insn-009f322c) · [`009f3240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f31b8.md#insn-009f3240) · [`009f3244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f31b8.md#insn-009f3244)

~~~diff
- 009f31d8 ["INT_ADD", "register:40f0:8", ["const:9f31d8:8", "const:4:8"]]
- 009f31d8 ["CALL", null, ["callee:00c57f60:8"]]
+ 009f322c ["INT_ADD", "register:40f0:8", ["const:9f322c:8", "const:4:8"]]
+ 009f322c ["CALL", null, ["callee:00c57f60:8"]]
- 009f31d8 bytes 2e930994
+ 009f322c bytes 4d930994
- 009f31ec ["COPY", "register:4048:8", ["const:c89000:8"]]
+ 009f3240 ["COPY", "register:4048:8", ["const:c8a000:8"]]
- 009f31ec bytes a91400d0
+ 009f3240 bytes a91400f0
- 009f31f0 ["COPY", "tmp:0:8", ["const:fb0:8"]]
- 009f31f0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 009f31f0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 009f31f0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 009f3244 ["COPY", "tmp:0:8", ["const:80:8"]]
+ 009f3244 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 009f3244 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 009f3244 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 009f31f0 bytes 29c13e91
+ 009f3244 bytes 29010291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e414db7cb6ecd60066e43e5d71415af"></a>

### [`009f32a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f32a4.md) → [`009f32f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f32f8.md) FUN_009f32f8

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`009ec95c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ec/009ec95c.md) · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)
- 新版 呼出元 1件 [`009ec9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ec/009ec9b0.md) · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.23% / 新版 91.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009f3314",
      "incomplete_value": false,
      "site": "009f3314",
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
            "const:400:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f32c0",
      "incomplete_value": false,
      "site": "009f32c0",
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
            "const:330:8"
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
      "definition_site": "009f3320",
      "incomplete_value": false,
      "site": "009f3320",
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
            "const:450:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f32cc",
      "incomplete_value": false,
      "site": "009f32cc",
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
            "const:380:8"
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
      "009f3314",
      "DATA",
      [
        "storage",
        "00c8a330",
        null,
        "undefined *"
      ]
    ],
    [
      "009f3320",
      "DATA",
      [
        "storage",
        "00c8a380",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f3314",
      "DATA",
      [
        "storage",
        "00c8a400",
        null,
        "undefined *"
      ]
    ],
    [
      "009f3320",
      "DATA",
      [
        "storage",
        "00c8a450",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f3320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f32a4.md#insn-009f3320) · [`009f32b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f32a4.md#insn-009f32b8) · [`009f32c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f32a4.md#insn-009f32c4)
- 新版 [`009f3374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f32f8.md#insn-009f3374) · [`009f330c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f32f8.md#insn-009f330c)

~~~diff
- 009f3320 ["COPY", "register:0:8", ["register:4040:8"]]
- 009f3320 ["INT_ADD", "register:40f0:8", ["const:9f3320:8", "const:4:8"]]
- 009f3320 ["CALLIND", null, ["register:0:8"]]
+ 009f3374 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009f3374 ["INT_ADD", "register:40f0:8", ["const:9f3374:8", "const:4:8"]]
+ 009f3374 ["CALLIND", null, ["register:0:8"]]
- 009f3320 bytes 00013fd6
+ 009f3374 bytes 00013fd6
- 009f32b8 ["COPY", "tmp:0:8", ["const:330:8"]]
- 009f32b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f32b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f32b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f330c ["COPY", "tmp:0:8", ["const:400:8"]]
+ 009f330c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f330c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f330c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f32b8 bytes 08c10c91
+ 009f330c bytes 08011091
- 009f32c4 ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 009f32c4 bytes a81400f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a71b946a22a096142ad41880dc41a38d"></a>

### [`009f33a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f33a4.md) → [`009f33f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f33f8.md) FUN_009f33f8

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md)

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
      "definition_site": "009f33fc",
      "incomplete_value": false,
      "site": "009f3400",
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
            "const:400:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f33a8",
      "incomplete_value": false,
      "site": "009f33ac",
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
            "const:330:8"
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
      "009f3400",
      "DATA",
      [
        "storage",
        "00c8a330",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f3400",
      "DATA",
      [
        "storage",
        "00c8a400",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f33a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f33a4.md#insn-009f33a8)
- 新版 [`009f33fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f33f8.md#insn-009f33fc)

~~~diff
- 009f33a8 ["COPY", "tmp:0:8", ["const:330:8"]]
- 009f33a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f33a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f33a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f33fc ["COPY", "tmp:0:8", ["const:400:8"]]
+ 009f33fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f33fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f33fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f33a8 bytes 08c10c91
+ 009f33fc bytes 08011091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f23fd08fa3c2b6007873774bb8249871"></a>

### [`009f33b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f33b4.md) → [`009f3408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3408.md) FUN_009f3408

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009f3418",
      "incomplete_value": false,
      "site": "009f3420",
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
            "const:400:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f33c4",
      "incomplete_value": false,
      "site": "009f33cc",
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
            "const:330:8"
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
      "009f3420",
      "DATA",
      [
        "storage",
        "00c8a330",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f3420",
      "DATA",
      [
        "storage",
        "00c8a400",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f33c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f33b4.md#insn-009f33c4) · [`009f33d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f33b4.md#insn-009f33d0)
- 新版 [`009f3418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3408.md#insn-009f3418) · [`009f3424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3408.md#insn-009f3424)

~~~diff
- 009f33c4 ["COPY", "tmp:0:8", ["const:330:8"]]
- 009f33c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f33c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f33c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f3418 ["COPY", "tmp:0:8", ["const:400:8"]]
+ 009f3418 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f3418 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f3418 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f33c4 bytes 08c10c91
+ 009f3418 bytes 08011091
- 009f33d0 ["INT_ADD", "register:40f0:8", ["const:9f33d0:8", "const:4:8"]]
- 009f33d0 ["CALL", null, ["callee:00c57f70:8"]]
+ 009f3424 ["INT_ADD", "register:40f0:8", ["const:9f3424:8", "const:4:8"]]
+ 009f3424 ["CALL", null, ["callee:00c57f70:8"]]
- 009f33d0 bytes b4920994
+ 009f3424 bytes d3920994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf14a120c38148e95ab41ddfe4c2cd1f"></a>

### [`009f33f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f33f4.md) → [`009f3448`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3448.md) FUN_009f3448

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

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
      "definition_site": "009f345c",
      "incomplete_value": false,
      "site": "009f3460",
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
            "const:450:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f3408",
      "incomplete_value": false,
      "site": "009f340c",
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
            "const:380:8"
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
      "009f3460",
      "DATA",
      [
        "storage",
        "00c8a380",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f3460",
      "DATA",
      [
        "storage",
        "00c8a450",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f3408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f33f4.md#insn-009f3408) · [`009f341c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f33f4.md#insn-009f341c) · [`009f343c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f33f4.md#insn-009f343c)
- 新版 [`009f345c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3448.md#insn-009f345c) · [`009f3470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3448.md#insn-009f3470) · [`009f3490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3448.md#insn-009f3490)

~~~diff
- 009f3408 ["COPY", "tmp:0:8", ["const:380:8"]]
- 009f3408 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f3408 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f3408 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f345c ["COPY", "tmp:0:8", ["const:450:8"]]
+ 009f345c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f345c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f345c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f3408 bytes 08010e91
+ 009f345c bytes 08411191
- 009f341c ["INT_ADD", "register:40f0:8", ["const:9f341c:8", "const:4:8"]]
- 009f341c ["CALL", null, ["callee:00c53da0:8"]]
+ 009f3470 ["INT_ADD", "register:40f0:8", ["const:9f3470:8", "const:4:8"]]
+ 009f3470 ["CALL", null, ["callee:00c53da0:8"]]
- 009f341c bytes 39820994
+ 009f3470 bytes 4c820994
- 009f343c ["COPY", "register:0:8", ["register:4040:8"]]
- 009f343c ["INT_ADD", "register:40f0:8", ["const:9f343c:8", "const:4:8"]]
- 009f343c ["CALLIND", null, ["register:0:8"]]
+ 009f3490 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009f3490 ["INT_ADD", "register:40f0:8", ["const:9f3490:8", "const:4:8"]]
+ 009f3490 ["CALLIND", null, ["register:0:8"]]
- 009f343c bytes 00013fd6
+ 009f3490 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33870a6bc9c7fbf9db76cbedebe62691"></a>

### [`009f3450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3450.md) → [`009f34a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f34a4.md) FUN_009f34a4

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "009f34bc",
      "incomplete_value": false,
      "site": "009f34c0",
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
            "const:450:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f3468",
      "incomplete_value": false,
      "site": "009f346c",
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
            "const:380:8"
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
      "009f34c0",
      "DATA",
      [
        "storage",
        "00c8a380",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f34c0",
      "DATA",
      [
        "storage",
        "00c8a450",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f3468`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3450.md#insn-009f3468) · [`009f347c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3450.md#insn-009f347c) · [`009f3490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3450.md#insn-009f3490)
- 新版 [`009f34bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f34a4.md#insn-009f34bc) · [`009f34d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f34a4.md#insn-009f34d0) · [`009f34e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f34a4.md#insn-009f34e4)

~~~diff
- 009f3468 ["COPY", "tmp:0:8", ["const:380:8"]]
- 009f3468 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f3468 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f3468 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f34bc ["COPY", "tmp:0:8", ["const:450:8"]]
+ 009f34bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f34bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f34bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f3468 bytes 08010e91
+ 009f34bc bytes 08411191
- 009f347c ["INT_ADD", "register:40f0:8", ["const:9f347c:8", "const:4:8"]]
- 009f347c ["CALL", null, ["callee:00c53da0:8"]]
+ 009f34d0 ["INT_ADD", "register:40f0:8", ["const:9f34d0:8", "const:4:8"]]
+ 009f34d0 ["CALL", null, ["callee:00c53da0:8"]]
- 009f347c bytes 21820994
+ 009f34d0 bytes 34820994
- 009f3490 ["COPY", "register:0:8", ["register:4040:8"]]
- 009f3490 ["INT_ADD", "register:40f0:8", ["const:9f3490:8", "const:4:8"]]
- 009f3490 ["CALLIND", null, ["register:0:8"]]
+ 009f34e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009f34e4 ["INT_ADD", "register:40f0:8", ["const:9f34e4:8", "const:4:8"]]
+ 009f34e4 ["CALLIND", null, ["register:0:8"]]
- 009f3490 bytes 00013fd6
+ 009f34e4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0595c7b9e0fd9224a65cd4d5048f5317"></a>

### [`009f35fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f35fc.md) → [`009f3650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3650.md) FUN_009f3650

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`009ed118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ed/009ed118.md) [`009f1978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f1/009f1978.md) [`009f1e4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f1/009f1e4c.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 3件 [`009ed16c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ed/009ed16c.md) [`009f19cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f1/009f19cc.md) [`009f1ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f1/009f1ea0.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "009f365c",
      "incomplete_value": false,
      "site": "009f3660",
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
      "definition_site": "009f3608",
      "incomplete_value": false,
      "site": "009f360c",
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
      "009f365c",
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
      "009f365c",
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

- 旧版 [`009f360c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f35fc.md#insn-009f360c) · [`009f3608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f35fc.md#insn-009f3608)
- 新版 [`009f3660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3650.md#insn-009f3660) · [`009f365c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3650.md#insn-009f365c)

~~~diff
- 009f360c ["INT_ADD", "register:40f0:8", ["const:9f360c:8", "const:4:8"]]
- 009f360c ["CALL", null, ["callee:0043b7b8:8"]]
+ 009f3660 ["INT_ADD", "register:40f0:8", ["const:9f3660:8", "const:4:8"]]
+ 009f3660 ["CALL", null, ["callee:0043b7b8:8"]]
- 009f360c bytes 5b20e997
+ 009f3660 bytes 5620e997
- 009f3608 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 009f3608 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 009f3608 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 009f3608 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 009f365c ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 009f365c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 009f365c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 009f365c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 009f3608 bytes 00303d91
+ 009f365c bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12cd9230f4be479c30571cef16a7b59c"></a>

### [`009f3a74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3a74.md) → [`009f3ac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3ac8.md) FUN_009f3ac8

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009f3acc",
      "incomplete_value": false,
      "site": "009f3ad0",
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
            "const:480:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f3a78",
      "incomplete_value": false,
      "site": "009f3a7c",
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
            "const:3b0:8"
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
      "009f3ad0",
      "DATA",
      [
        "storage",
        "00c8a3b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f3ad0",
      "DATA",
      [
        "storage",
        "00c8a480",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f3a78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3a74.md#insn-009f3a78)
- 新版 [`009f3acc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3ac8.md#insn-009f3acc)

~~~diff
- 009f3a78 ["COPY", "tmp:0:8", ["const:3b0:8"]]
- 009f3a78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f3a78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f3a78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f3acc ["COPY", "tmp:0:8", ["const:480:8"]]
+ 009f3acc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f3acc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f3acc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f3a78 bytes 08c10e91
+ 009f3acc bytes 08011291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76d652c6744c87d1508ad40f9ef06b80"></a>

### [`009f3ab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3ab8.md) → [`009f3b0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3b0c.md) FUN_009f3b0c

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`009efde8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ef/009efde8.md) [`009f050c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f0/009f050c.md) [`009f1200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f1/009f1200.md) [`009f3c6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3c6c.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 4件 [`009efe3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ef/009efe3c.md) [`009f0560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f0/009f0560.md) [`009f1254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f1/009f1254.md) [`009f3cc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3cc0.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "009f3b18",
      "incomplete_value": false,
      "site": "009f3b1c",
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
      "definition_site": "009f3ac4",
      "incomplete_value": false,
      "site": "009f3ac8",
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
      "009f3b18",
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
      "009f3b18",
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

- 旧版 [`009f3ac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3ab8.md#insn-009f3ac8) · [`009f3ac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3ab8.md#insn-009f3ac4)
- 新版 [`009f3b1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3b0c.md#insn-009f3b1c) · [`009f3b18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3b0c.md#insn-009f3b18)

~~~diff
- 009f3ac8 ["INT_ADD", "register:40f0:8", ["const:9f3ac8:8", "const:4:8"]]
- 009f3ac8 ["CALL", null, ["callee:0043b7b8:8"]]
+ 009f3b1c ["INT_ADD", "register:40f0:8", ["const:9f3b1c:8", "const:4:8"]]
+ 009f3b1c ["CALL", null, ["callee:0043b7b8:8"]]
- 009f3ac8 bytes 2c1fe997
+ 009f3b1c bytes 271fe997
- 009f3ac4 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 009f3ac4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 009f3ac4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 009f3ac4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 009f3b18 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 009f3b18 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 009f3b18 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 009f3b18 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 009f3ac4 bytes 00303d91
+ 009f3b18 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dfb144f9e83b8bed759e0e2001d390c0"></a>

### [`009f3c58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3c58.md) → [`009f3cac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3cac.md) FUN_009f3cac

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`009f3acc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3acc.md) [`009f4950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4950.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 2件 [`009f3b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3b20.md) [`009f49a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f49a4.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "009f3cb8",
      "incomplete_value": false,
      "site": "009f3cbc",
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
      "definition_site": "009f3c64",
      "incomplete_value": false,
      "site": "009f3c68",
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
      "009f3cb8",
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
      "009f3cb8",
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

- 旧版 [`009f3c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3c58.md#insn-009f3c68) · [`009f3c64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3c58.md#insn-009f3c64)
- 新版 [`009f3cbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3cac.md#insn-009f3cbc) · [`009f3cb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3cac.md#insn-009f3cb8)

~~~diff
- 009f3c68 ["INT_ADD", "register:40f0:8", ["const:9f3c68:8", "const:4:8"]]
- 009f3c68 ["CALL", null, ["callee:0043b7b8:8"]]
+ 009f3cbc ["INT_ADD", "register:40f0:8", ["const:9f3cbc:8", "const:4:8"]]
+ 009f3cbc ["CALL", null, ["callee:0043b7b8:8"]]
- 009f3c68 bytes c41ee997
+ 009f3cbc bytes bf1ee997
- 009f3c64 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 009f3c64 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 009f3c64 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 009f3c64 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 009f3cb8 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 009f3cb8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 009f3cb8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 009f3cb8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 009f3c64 bytes 00303d91
+ 009f3cb8 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d46f79c5aae029c6ae68038642c7bea"></a>

### [`009f4adc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4adc.md) → [`009f4b30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4b30.md) FUN_009f4b30

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`009f15bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f1/009f15bc.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 1件 [`009f1610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f1/009f1610.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "009f4b3c",
      "incomplete_value": false,
      "site": "009f4b40",
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
      "definition_site": "009f4ae8",
      "incomplete_value": false,
      "site": "009f4aec",
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
      "009f4b3c",
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
      "009f4b3c",
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

- 旧版 [`009f4aec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4adc.md#insn-009f4aec) · [`009f4ae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4adc.md#insn-009f4ae8)
- 新版 [`009f4b40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4b30.md#insn-009f4b40) · [`009f4b3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4b30.md#insn-009f4b3c)

~~~diff
- 009f4aec ["INT_ADD", "register:40f0:8", ["const:9f4aec:8", "const:4:8"]]
- 009f4aec ["CALL", null, ["callee:0043b7b8:8"]]
+ 009f4b40 ["INT_ADD", "register:40f0:8", ["const:9f4b40:8", "const:4:8"]]
+ 009f4b40 ["CALL", null, ["callee:0043b7b8:8"]]
- 009f4aec bytes 231be997
+ 009f4b40 bytes 1e1be997
- 009f4ae8 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 009f4ae8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 009f4ae8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 009f4ae8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 009f4b3c ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 009f4b3c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 009f4b3c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 009f4b3c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 009f4ae8 bytes 00303d91
+ 009f4b3c bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-caa7c4a1ab9baded9bb8b6da978d5610"></a>

### [`009f4af0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4af0.md) → [`009f4b44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4b44.md) FUN_009f4b44

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`009f1700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f1/009f1700.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 1件 [`009f1754`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f1/009f1754.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "009f4b50",
      "incomplete_value": false,
      "site": "009f4b54",
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
      "definition_site": "009f4afc",
      "incomplete_value": false,
      "site": "009f4b00",
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
      "009f4b50",
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
      "009f4b50",
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

- 旧版 [`009f4b00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4af0.md#insn-009f4b00) · [`009f4afc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4af0.md#insn-009f4afc)
- 新版 [`009f4b54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4b44.md#insn-009f4b54) · [`009f4b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4b44.md#insn-009f4b50)

~~~diff
- 009f4b00 ["INT_ADD", "register:40f0:8", ["const:9f4b00:8", "const:4:8"]]
- 009f4b00 ["CALL", null, ["callee:0043b7b8:8"]]
+ 009f4b54 ["INT_ADD", "register:40f0:8", ["const:9f4b54:8", "const:4:8"]]
+ 009f4b54 ["CALL", null, ["callee:0043b7b8:8"]]
- 009f4b00 bytes 1e1be997
+ 009f4b54 bytes 191be997
- 009f4afc ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 009f4afc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 009f4afc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 009f4afc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 009f4b50 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 009f4b50 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 009f4b50 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 009f4b50 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 009f4afc bytes 00303d91
+ 009f4b50 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-847967738ab7260962fb504355deea37"></a>

### [`009f4b04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4b04.md) → [`009f4b58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4b58.md) FUN_009f4b58

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md)

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
      "definition_site": "009f4b5c",
      "incomplete_value": false,
      "site": "009f4b60",
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
            "const:500:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f4b08",
      "incomplete_value": false,
      "site": "009f4b0c",
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
            "const:430:8"
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
      "009f4b60",
      "DATA",
      [
        "storage",
        "00c8a430",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f4b60",
      "DATA",
      [
        "storage",
        "00c8a500",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f4b08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4b04.md#insn-009f4b08)
- 新版 [`009f4b5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4b58.md#insn-009f4b5c)

~~~diff
- 009f4b08 ["COPY", "tmp:0:8", ["const:430:8"]]
- 009f4b08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f4b08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f4b08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f4b5c ["COPY", "tmp:0:8", ["const:500:8"]]
+ 009f4b5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f4b5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f4b5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f4b08 bytes 08c11091
+ 009f4b5c bytes 08011491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db4a3cecd019188284a6261a81fef073"></a>

### [`009f4b14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4b14.md) → [`009f4b68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4b68.md) FUN_009f4b68

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009f4b78",
      "incomplete_value": false,
      "site": "009f4b80",
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
            "const:500:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f4b24",
      "incomplete_value": false,
      "site": "009f4b2c",
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
            "const:430:8"
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
      "009f4b80",
      "DATA",
      [
        "storage",
        "00c8a430",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f4b80",
      "DATA",
      [
        "storage",
        "00c8a500",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f4b24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4b14.md#insn-009f4b24) · [`009f4b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4b14.md#insn-009f4b30)
- 新版 [`009f4b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4b68.md#insn-009f4b78) · [`009f4b84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4b68.md#insn-009f4b84)

~~~diff
- 009f4b24 ["COPY", "tmp:0:8", ["const:430:8"]]
- 009f4b24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f4b24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f4b24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f4b78 ["COPY", "tmp:0:8", ["const:500:8"]]
+ 009f4b78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f4b78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f4b78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f4b24 bytes 08c11091
+ 009f4b78 bytes 08011491
- 009f4b30 ["INT_ADD", "register:40f0:8", ["const:9f4b30:8", "const:4:8"]]
- 009f4b30 ["CALL", null, ["callee:00c57f70:8"]]
+ 009f4b84 ["INT_ADD", "register:40f0:8", ["const:9f4b84:8", "const:4:8"]]
+ 009f4b84 ["CALL", null, ["callee:00c57f70:8"]]
- 009f4b30 bytes dc8c0994
+ 009f4b84 bytes fb8c0994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4778119f5fb0f6c1635dae04f832cbff"></a>

### [`009f4b50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4b50.md) → [`009f4ba4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4ba4.md) FUN_009f4ba4

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009f4b44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4b44.md) · 呼出先 8件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`009f2894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2894.md) [`009f28e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f28e4.md) [`009f2934`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2934.md) [`009f2978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2978.md)
- 新版 呼出元 1件 [`009f4b98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4b98.md) · 呼出先 8件 [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`009f28e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f28e8.md) [`009f2938`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2938.md) [`009f2988`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2988.md) [`009f29cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f29cc.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.74% / 新版 95.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009f4bc0",
      "incomplete_value": false,
      "site": "009f4bc0",
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
            "const:f28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f4b6c",
      "incomplete_value": false,
      "site": "009f4b6c",
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
            "const:e58:8"
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
      "009f4bc0",
      "DATA",
      [
        "storage",
        "00c89e58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f4bc0",
      "DATA",
      [
        "storage",
        "00c89f28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f4b64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4b50.md#insn-009f4b64) · [`009f4b70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4b50.md#insn-009f4b70) · [`009f4b7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4b50.md#insn-009f4b7c)
- 新版 [`009f4bb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4ba4.md#insn-009f4bb8) · [`009f4bc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4ba4.md#insn-009f4bc4) · [`009f4bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4ba4.md#insn-009f4bd0)

~~~diff
- 009f4b64 ["COPY", "tmp:0:8", ["const:e58:8"]]
- 009f4b64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f4b64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f4b64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f4bb8 ["COPY", "tmp:0:8", ["const:f28:8"]]
+ 009f4bb8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f4bb8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f4bb8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f4b64 bytes 08613991
+ 009f4bb8 bytes 08a13c91
- 009f4b70 ["INT_ADD", "register:40f0:8", ["const:9f4b70:8", "const:4:8"]]
- 009f4b70 ["CALL", null, ["callee:009f38e8:8"]]
+ 009f4bc4 ["INT_ADD", "register:40f0:8", ["const:9f4bc4:8", "const:4:8"]]
+ 009f4bc4 ["CALL", null, ["callee:009f38e8:8"]]
- 009f4b70 bytes 49fbff97
+ 009f4bc4 bytes 49fbff97
- 009f4b7c ["INT_ADD", "register:40f0:8", ["const:9f4b7c:8", "const:4:8"]]
- 009f4b7c ["CALL", null, ["callee:009f28e8:8"]]
+ 009f4bd0 ["INT_ADD", "register:40f0:8", ["const:9f4bd0:8", "const:4:8"]]
+ 009f4bd0 ["CALL", null, ["callee:009f28e8:8"]]
- 009f4b7c bytes 46f7ff97
+ 009f4bd0 bytes 46f7ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f06ec859d1fa50cabc141965f57108f"></a>

### [`009f4c0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4c0c.md) → [`009f4c60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4c60.md) _INIT_205

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.01% / 新版 87.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009f4c9c",
      "incomplete_value": true,
      "site": "009f4cb8",
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
      "definition_site": "009f4c48",
      "incomplete_value": true,
      "site": "009f4c64",
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
      "definition_site": "009f4d1c",
      "incomplete_value": true,
      "site": "009f4d38",
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
                "const:2ac000:8"
              ],
              [
                "leaf",
                "const:576:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f4cc8",
      "incomplete_value": true,
      "site": "009f4ce4",
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
                "const:2ac000:8"
              ],
              [
                "leaf",
                "const:5d2:8"
              ]
            ]
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
      "definition_site": "009f4d3c",
      "incomplete_value": true,
      "site": "009f4d58",
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
                "const:2a0000:8"
              ],
              [
                "leaf",
                "const:f10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f4ce8",
      "incomplete_value": true,
      "site": "009f4d04",
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
                "const:2a0000:8"
              ],
              [
                "leaf",
                "const:f5d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 24,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009f4c9c",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "009f4cc0",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "009f4ce0",
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
      "009f4c9c",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "009f4cc0",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "009f4ce0",
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

- 旧版 [`009f4e40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4c0c.md#insn-009f4e40) · [`009f4c38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4c0c.md#insn-009f4c38) · [`009f4c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4c0c.md#insn-009f4c40)
- 新版 [`009f4e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4c60.md#insn-009f4e94) · [`009f4c8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4c60.md#insn-009f4c8c)

~~~diff
- 009f4e40 ["INT_ADD", "register:40f0:8", ["const:9f4e40:8", "const:4:8"]]
- 009f4e40 ["CALL", null, ["callee:00c57f00:8"]]
+ 009f4e94 ["INT_ADD", "register:40f0:8", ["const:9f4e94:8", "const:4:8"]]
+ 009f4e94 ["CALL", null, ["callee:00c57f00:8"]]
- 009f4e40 bytes fc8b0994
+ 009f4e94 bytes 1b8c0994
- 009f4c38 ["COPY", "tmp:0:8", ["const:d38:8"]]
- 009f4c38 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 009f4c38 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 009f4c38 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 009f4c8c ["COPY", "tmp:0:8", ["const:e38:8"]]
+ 009f4c8c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 009f4c8c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 009f4c8c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 009f4c38 bytes 73e23491
+ 009f4c8c bytes 73e23891
- 009f4c40 ["COPY", "register:4048:8", ["const:2b7000:8"]]
- 009f4c40 bytes 09c6fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4c25d49fbcd46c4626bc895562471e2"></a>

### [`009f4fa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4fa4.md) → [`009f4ff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4ff8.md) FUN_009f4ff8

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009fb44c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fb/009fb44c.md) · 呼出先 14件 [`0057bea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bea8.md) [`006648a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/006648a0.md) [`006667a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00666/006667a8.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`009df8c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009df/009df8c4.md)
- 新版 呼出元 1件 [`009fb4a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fb/009fb4a0.md) · 呼出先 14件 [`0057bee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057bee8.md) [`006648e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00664/006648e0.md) [`006667e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00666/006667e8.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`009df918`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009df/009df918.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.08% / 新版 99.08%

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
      "site": "009f52dc",
      "value": [
        "leaf",
        "ram:6648e0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009f5288",
      "value": [
        "leaf",
        "ram:6648a0:8"
      ]
    },
    "ordinal": 30,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009f5050",
      "DATA",
      [
        "storage",
        "00c8a4b0",
        null,
        "undefined *"
      ]
    ],
    [
      "009f5058",
      "READ",
      [
        "storage",
        "002c4208",
        null,
        "undefined8"
      ]
    ],
    [
      "009f52dc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006648a0"
      ]
    ]
  ],
  "added": [
    [
      "009f5050",
      "DATA",
      [
        "storage",
        "00c8a580",
        null,
        "undefined *"
      ]
    ],
    [
      "009f5058",
      "READ",
      [
        "storage",
        "002c4248",
        null,
        "undefined8"
      ]
    ],
    [
      "009f52dc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006648e0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f5288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4fa4.md#insn-009f5288) · [`009f4fe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4fa4.md#insn-009f4fe8) · [`009f4ff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4fa4.md#insn-009f4ff4)
- 新版 [`009f52dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4ff8.md#insn-009f52dc) · [`009f503c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4ff8.md#insn-009f503c) · [`009f5048`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4ff8.md#insn-009f5048)

~~~diff
- 009f5288 ["INT_ADD", "register:40f0:8", ["const:9f5288:8", "const:4:8"]]
- 009f5288 ["CALL", null, ["ram:6648a0:8"]]
+ 009f52dc ["INT_ADD", "register:40f0:8", ["const:9f52dc:8", "const:4:8"]]
+ 009f52dc ["CALL", null, ["ram:6648e0:8"]]
- 009f5288 bytes 86bdf197
+ 009f52dc bytes 81bdf197
- 009f4fe8 ["INT_ADD", "register:40f0:8", ["const:9f4fe8:8", "const:4:8"]]
- 009f4fe8 ["CALL", null, ["callee:00c57f60:8"]]
+ 009f503c ["INT_ADD", "register:40f0:8", ["const:9f503c:8", "const:4:8"]]
+ 009f503c ["CALL", null, ["callee:00c57f60:8"]]
- 009f4fe8 bytes aa8b0994
+ 009f503c bytes c98b0994
- 009f4ff4 ["COPY", "tmp:0:8", ["const:4b0:8"]]
- 009f4ff4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f4ff4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f4ff4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f5048 ["COPY", "tmp:0:8", ["const:580:8"]]
+ 009f5048 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f5048 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f5048 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f4ff4 bytes 08c11291
+ 009f5048 bytes 08011691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32019cb8ab252f35d4c7868da524f182"></a>

### [`009f53a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f5/009f53a8.md) → [`009f53fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f5/009f53fc.md) FUN_009f53fc

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.70% / 新版 90.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009f541c",
      "incomplete_value": false,
      "site": "009f5420",
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
            "const:580:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f53c8",
      "incomplete_value": false,
      "site": "009f53cc",
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
            "const:4b0:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009f545c",
      "incomplete_value": false,
      "site": "009f5464",
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
            "const:550:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f5408",
      "incomplete_value": false,
      "site": "009f5410",
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
            "const:480:8"
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
      "009f5420",
      "DATA",
      [
        "storage",
        "00c8a4b0",
        null,
        "undefined *"
      ]
    ],
    [
      "009f5464",
      "DATA",
      [
        "storage",
        "00c8a480",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f5420",
      "DATA",
      [
        "storage",
        "00c8a580",
        null,
        "undefined *"
      ]
    ],
    [
      "009f5464",
      "DATA",
      [
        "storage",
        "00c8a550",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f53c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f5/009f53a8.md#insn-009f53c8) · [`009f53dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f5/009f53a8.md#insn-009f53dc) · [`009f53f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f5/009f53a8.md#insn-009f53f0)
- 新版 [`009f541c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f5/009f53fc.md#insn-009f541c) · [`009f5430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f5/009f53fc.md#insn-009f5430) · [`009f5444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f5/009f53fc.md#insn-009f5444)

~~~diff
- 009f53c8 ["COPY", "tmp:0:8", ["const:4b0:8"]]
- 009f53c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f53c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f53c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f541c ["COPY", "tmp:0:8", ["const:580:8"]]
+ 009f541c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f541c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f541c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f53c8 bytes 08c11291
+ 009f541c bytes 08011691
- 009f53dc ["INT_ADD", "register:40f0:8", ["const:9f53dc:8", "const:4:8"]]
- 009f53dc ["CALL", null, ["callee:00c53da0:8"]]
+ 009f5430 ["INT_ADD", "register:40f0:8", ["const:9f5430:8", "const:4:8"]]
+ 009f5430 ["CALL", null, ["callee:00c53da0:8"]]
- 009f53dc bytes 497a0994
+ 009f5430 bytes 5c7a0994
- 009f53f0 ["COPY", "register:0:8", ["register:4040:8"]]
- 009f53f0 ["INT_ADD", "register:40f0:8", ["const:9f53f0:8", "const:4:8"]]
- 009f53f0 ["CALLIND", null, ["register:0:8"]]
+ 009f5444 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009f5444 ["INT_ADD", "register:40f0:8", ["const:9f5444:8", "const:4:8"]]
+ 009f5444 ["CALLIND", null, ["register:0:8"]]
- 009f53f0 bytes 00013fd6
+ 009f5444 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3916cbcbf3d97ad29b1eba1fd12b3cf2"></a>

### [`009f5454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f5/009f5454.md) → [`009f54a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f5/009f54a8.md) FUN_009f54a8

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00859b4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00859/00859b4c.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00859ba4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00859/00859ba4.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.88% / 新版 96.88%

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
      "site": "009f5510",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009f54bc",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "site": "009f556c",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009f5518",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "009f5510",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "009f556c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "009f5510",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "009f556c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f54bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f5/009f5454.md#insn-009f54bc) · [`009f5510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f5/009f5454.md#insn-009f5510) · [`009f5518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f5/009f5454.md#insn-009f5518)
- 新版 [`009f5510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f5/009f54a8.md#insn-009f5510) · [`009f5564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f5/009f54a8.md#insn-009f5564) · [`009f556c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f5/009f54a8.md#insn-009f556c)

~~~diff
- 009f54bc ["INT_ADD", "register:40f0:8", ["const:9f54bc:8", "const:4:8"]]
- 009f54bc ["CALL", null, ["ram:47acf4:8"]]
+ 009f5510 ["INT_ADD", "register:40f0:8", ["const:9f5510:8", "const:4:8"]]
+ 009f5510 ["CALL", null, ["ram:47ad34:8"]]
- 009f54bc bytes 0e16ea97
+ 009f5510 bytes 0916ea97
- 009f5510 ["INT_ADD", "register:40f0:8", ["const:9f5510:8", "const:4:8"]]
- 009f5510 ["CALL", null, ["callee:009dce94:8"]]
+ 009f5564 ["INT_ADD", "register:40f0:8", ["const:9f5564:8", "const:4:8"]]
+ 009f5564 ["CALL", null, ["callee:009dce94:8"]]
- 009f5510 bytes 4c9eff97
+ 009f5564 bytes 4c9eff97
- 009f5518 ["INT_ADD", "register:40f0:8", ["const:9f5518:8", "const:4:8"]]
- 009f5518 ["CALL", null, ["ram:47acf4:8"]]
+ 009f556c ["INT_ADD", "register:40f0:8", ["const:9f556c:8", "const:4:8"]]
+ 009f556c ["CALL", null, ["ram:47ad34:8"]]
- 009f5518 bytes f715ea97
+ 009f556c bytes f215ea97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3342c46f0d1d2074f9413f65b7b59be"></a>

### [`009f5554`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f5/009f5554.md) → [`009f55a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f5/009f55a8.md) FUN_009f55a8

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 19件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00469c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469c04.md) [`0046a250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046a250.md) [`0046af18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046af18.md) [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md)
- 新版 呼出元 0件  · 呼出先 19件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00469c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00469/00469c44.md) [`0046a290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046a/0046a290.md) [`0046af58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046a/0046af58.md) [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.88% / 新版 97.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 3件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009f5938",
      "incomplete_value": true,
      "site": "009f5950",
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f58e4",
      "incomplete_value": true,
      "site": "009f58fc",
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
                "const:20:8"
              ]
            ]
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
      "definition_site": "009f5934",
      "incomplete_value": true,
      "site": "009f5954",
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
                "const:302000:8"
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
    "old": {
      "definition_site": "009f58e0",
      "incomplete_value": true,
      "site": "009f5900",
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
                "const:302000:8"
              ],
              [
                "leaf",
                "const:c70:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "009f5934",
      "incomplete_value": true,
      "site": "009f5954",
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
      "definition_site": "009f58e0",
      "incomplete_value": true,
      "site": "009f5900",
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
      "009f55e8",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "009f55f4",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009f55fc",
      "PARAM",
      [
        "storage",
        "00c71990",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "009f55e8",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "009f55f4",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009f55fc",
      "PARAM",
      [
        "storage",
        "00c71a60",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f55b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f5/009f5554.md#insn-009f55b4) · [`009f55ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f5/009f5554.md#insn-009f55ec) · [`009f5594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f5/009f5554.md#insn-009f5594)
- 新版 [`009f5608`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f5/009f55a8.md#insn-009f5608) · [`009f5640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f5/009f55a8.md#insn-009f5640) · [`009f55e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f5/009f55a8.md#insn-009f55e8)

~~~diff
- 009f55b4 ["INT_ADD", "register:40f0:8", ["const:9f55b4:8", "const:4:8"]]
- 009f55b4 ["CALL", null, ["callee:00c586e0:8"]]
+ 009f5608 ["INT_ADD", "register:40f0:8", ["const:9f5608:8", "const:4:8"]]
+ 009f5608 ["CALL", null, ["callee:00c586e0:8"]]
- 009f55b4 bytes 178c0994
+ 009f5608 bytes 368c0994
- 009f55ec ["INT_ADD", "register:40f0:8", ["const:9f55ec:8", "const:4:8"]]
- 009f55ec ["CALL", null, ["callee:00851550:8"]]
+ 009f5640 ["INT_ADD", "register:40f0:8", ["const:9f5640:8", "const:4:8"]]
+ 009f5640 ["CALL", null, ["callee:00851550:8"]]
- 009f55ec bytes c36ff997
+ 009f5640 bytes c46ff997
- 009f5594 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:978:8"]]
- 009f5594 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 009f55e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 009f55e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 009f5594 bytes 08bd44f9
+ 009f55e8 bytes 083d45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92a8667c8eb18c96233598354ee679fa"></a>

### [`009f5ab4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f5/009f5ab4.md) → [`009f5b08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f5/009f5b08.md) FUN_009f5b08

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009fb44c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fb/009fb44c.md) · 呼出先 20件 [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`0057bea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bea8.md) [`005c3e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c3/005c3e7c.md) [`00665d64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00665/00665d64.md)
- 新版 呼出元 1件 [`009fb4a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fb/009fb4a0.md) · 呼出先 20件 [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`0057bee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057bee8.md) [`005c3ebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c3/005c3ebc.md) [`00665da4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00665/00665da4.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.72% / 新版 98.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009f5b60",
      "incomplete_value": false,
      "site": "009f5b6c",
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
            "const:5b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f5b0c",
      "incomplete_value": false,
      "site": "009f5b18",
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
            "const:4e8:8"
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
      "definition_site": "009f5ba4",
      "incomplete_value": true,
      "site": "009f5bac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:248:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f5b50",
      "incomplete_value": true,
      "site": "009f5b58",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:208:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 32,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009f5fe8",
      "value": [
        "leaf",
        "ram:6c63ec:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009f5f94",
      "value": [
        "leaf",
        "ram:6c6394:8"
      ]
    },
    "ordinal": 49,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009f5b6c",
      "DATA",
      [
        "storage",
        "00c8a4e8",
        null,
        "undefined *"
      ]
    ],
    [
      "009f5ba4",
      "READ",
      [
        "storage",
        "002c4208",
        null,
        "undefined8"
      ]
    ],
    [
      "009f5fe8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006c6394"
      ]
    ]
  ],
  "added": [
    [
      "009f5b6c",
      "DATA",
      [
        "storage",
        "00c8a5b8",
        null,
        "undefined *"
      ]
    ],
    [
      "009f5ba4",
      "READ",
      [
        "storage",
        "002c4248",
        null,
        "undefined8"
      ]
    ],
    [
      "009f5fe8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006c63ec"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f5bac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f5/009f5ab4.md#insn-009f5bac) · [`009f5f94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f5/009f5ab4.md#insn-009f5f94) · [`009f5b00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f5/009f5ab4.md#insn-009f5b00)
- 新版 [`009f5c00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f5/009f5b08.md#insn-009f5c00) · [`009f5fe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f5/009f5b08.md#insn-009f5fe8) · [`009f5b54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f5/009f5b08.md#insn-009f5b54)

~~~diff
- 009f5bac ["COPY", "register:0:8", ["register:4040:8"]]
- 009f5bac ["INT_ADD", "register:40f0:8", ["const:9f5bac:8", "const:4:8"]]
- 009f5bac ["CALLIND", null, ["register:0:8"]]
+ 009f5c00 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009f5c00 ["INT_ADD", "register:40f0:8", ["const:9f5c00:8", "const:4:8"]]
+ 009f5c00 ["CALLIND", null, ["register:0:8"]]
- 009f5bac bytes 00013fd6
+ 009f5c00 bytes 00013fd6
- 009f5f94 ["INT_ADD", "register:40f0:8", ["const:9f5f94:8", "const:4:8"]]
- 009f5f94 ["CALL", null, ["ram:6c6394:8"]]
+ 009f5fe8 ["INT_ADD", "register:40f0:8", ["const:9f5fe8:8", "const:4:8"]]
+ 009f5fe8 ["CALL", null, ["ram:6c63ec:8"]]
- 009f5f94 bytes 0041f397
+ 009f5fe8 bytes 0141f397
- 009f5b00 ["INT_ADD", "register:40f0:8", ["const:9f5b00:8", "const:4:8"]]
- 009f5b00 ["CALL", null, ["callee:00c57f60:8"]]
+ 009f5b54 ["INT_ADD", "register:40f0:8", ["const:9f5b54:8", "const:4:8"]]
+ 009f5b54 ["CALL", null, ["callee:00c57f60:8"]]
- 009f5b00 bytes e4880994
+ 009f5b54 bytes 03890994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d91b52a54df88de054d354524a4228c7"></a>

### [`009f68e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f6/009f68e4.md) → [`009f6938`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f6/009f6938.md) FUN_009f6938

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.70% / 新版 90.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009f6958",
      "incomplete_value": false,
      "site": "009f695c",
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
            "const:5b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f6904",
      "incomplete_value": false,
      "site": "009f6908",
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
            "const:4e8:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009f6998",
      "incomplete_value": false,
      "site": "009f69a0",
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
            "const:550:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f6944",
      "incomplete_value": false,
      "site": "009f694c",
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
            "const:480:8"
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
      "009f695c",
      "DATA",
      [
        "storage",
        "00c8a4e8",
        null,
        "undefined *"
      ]
    ],
    [
      "009f69a0",
      "DATA",
      [
        "storage",
        "00c8a480",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009f695c",
      "DATA",
      [
        "storage",
        "00c8a5b8",
        null,
        "undefined *"
      ]
    ],
    [
      "009f69a0",
      "DATA",
      [
        "storage",
        "00c8a550",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f6904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f6/009f68e4.md#insn-009f6904) · [`009f6918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f6/009f68e4.md#insn-009f6918) · [`009f692c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f6/009f68e4.md#insn-009f692c)
- 新版 [`009f6958`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f6/009f6938.md#insn-009f6958) · [`009f696c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f6/009f6938.md#insn-009f696c) · [`009f6980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f6/009f6938.md#insn-009f6980)

~~~diff
- 009f6904 ["COPY", "tmp:0:8", ["const:4e8:8"]]
- 009f6904 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009f6904 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009f6904 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009f6958 ["COPY", "tmp:0:8", ["const:5b8:8"]]
+ 009f6958 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009f6958 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009f6958 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009f6904 bytes 08a11391
+ 009f6958 bytes 08e11691
- 009f6918 ["INT_ADD", "register:40f0:8", ["const:9f6918:8", "const:4:8"]]
- 009f6918 ["CALL", null, ["callee:00c53da0:8"]]
+ 009f696c ["INT_ADD", "register:40f0:8", ["const:9f696c:8", "const:4:8"]]
+ 009f696c ["CALL", null, ["callee:00c53da0:8"]]
- 009f6918 bytes fa740994
+ 009f696c bytes 0d750994
- 009f692c ["COPY", "register:0:8", ["register:4040:8"]]
- 009f692c ["INT_ADD", "register:40f0:8", ["const:9f692c:8", "const:4:8"]]
- 009f692c ["CALLIND", null, ["register:0:8"]]
+ 009f6980 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009f6980 ["INT_ADD", "register:40f0:8", ["const:9f6980:8", "const:4:8"]]
+ 009f6980 ["CALLIND", null, ["register:0:8"]]
- 009f692c bytes 00013fd6
+ 009f6980 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8c96f234d1df81acfdc03a2f7d1e768"></a>

### [`009f6990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f6/009f6990.md) → [`009f69e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f6/009f69e4.md) FUN_009f69e4

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`0046da5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046da5c.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`0046da9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046da9c.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.76% / 新版 98.76%

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
      "site": "009f6bb0",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009f6b5c",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "ordinal": 18,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009f6c24",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009f6bd0",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "ordinal": 26,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009f6b50",
      "DATA",
      [
        "storage",
        "00436bcc",
        null,
        "byte[59]"
      ]
    ],
    [
      "009f6b60",
      "DATA",
      [
        "storage",
        "00436bcc",
        null,
        "byte[59]"
      ]
    ],
    [
      "009f6bb0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "009f6b50",
      "DATA",
      [
        "storage",
        "00436bcc",
        null,
        "byte[47]"
      ]
    ],
    [
      "009f6b60",
      "DATA",
      [
        "storage",
        "00436bcc",
        null,
        "byte[47]"
      ]
    ],
    [
      "009f6bb0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f6b5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f6/009f6990.md#insn-009f6b5c) · [`009f6bd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f6/009f6990.md#insn-009f6bd0) · [`009f69d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f6/009f6990.md#insn-009f69d4)
- 新版 [`009f6bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f6/009f69e4.md#insn-009f6bb0) · [`009f6c24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f6/009f69e4.md#insn-009f6c24) · [`009f6a28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f6/009f69e4.md#insn-009f6a28)

~~~diff
- 009f6b5c ["INT_ADD", "register:40f0:8", ["const:9f6b5c:8", "const:4:8"]]
- 009f6b5c ["CALL", null, ["ram:47acf4:8"]]
+ 009f6bb0 ["INT_ADD", "register:40f0:8", ["const:9f6bb0:8", "const:4:8"]]
+ 009f6bb0 ["CALL", null, ["ram:47ad34:8"]]
- 009f6b5c bytes 6610ea97
+ 009f6bb0 bytes 6110ea97
- 009f6bd0 ["INT_ADD", "register:40f0:8", ["const:9f6bd0:8", "const:4:8"]]
- 009f6bd0 ["CALL", null, ["ram:47acf4:8"]]
+ 009f6c24 ["INT_ADD", "register:40f0:8", ["const:9f6c24:8", "const:4:8"]]
+ 009f6c24 ["CALL", null, ["ram:47ad34:8"]]
- 009f6bd0 bytes 4910ea97
+ 009f6c24 bytes 4410ea97
- 009f69d4 ["INT_ADD", "register:40f0:8", ["const:9f69d4:8", "const:4:8"]]
- 009f69d4 ["CALL", null, ["callee:0046da9c:8"]]
+ 009f6a28 ["INT_ADD", "register:40f0:8", ["const:9f6a28:8", "const:4:8"]]
+ 009f6a28 ["CALL", null, ["callee:0046da9c:8"]]
- 009f69d4 bytes 22dce997
+ 009f6a28 bytes 1ddce997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c58440559802d8a8de878ea6cd1dd07e"></a>

### [`009f6c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f6/009f6c14.md) → [`009f6c68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f6/009f6c68.md) FUN_009f6c68

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 21件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`00469068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469068.md) [`0046965c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/0046965c.md) [`00469c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469c04.md)
- 新版 呼出元 0件  · 呼出先 21件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00468fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468fc8.md) [`004690a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00469/004690a8.md) [`0046969c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00469/0046969c.md) [`00469c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00469/00469c44.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.64% / 新版 98.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 3件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009f733c",
      "incomplete_value": true,
      "site": "009f7354",
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f72e8",
      "incomplete_value": true,
      "site": "009f7300",
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 37,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009f7338",
      "incomplete_value": true,
      "site": "009f7358",
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
                "const:302000:8"
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
    "old": {
      "definition_site": "009f72e4",
      "incomplete_value": true,
      "site": "009f7304",
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
                "const:302000:8"
              ],
              [
                "leaf",
                "const:c70:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 38,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009f7338",
      "incomplete_value": true,
      "site": "009f7358",
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
      "definition_site": "009f72e4",
      "incomplete_value": true,
      "site": "009f7304",
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
      "009f6ca8",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "009f6cb4",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009f6cbc",
      "PARAM",
      [
        "storage",
        "00c71990",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "009f6ca8",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "009f6cb4",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009f6cbc",
      "PARAM",
      [
        "storage",
        "00c71a60",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f6c74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f6/009f6c14.md#insn-009f6c74) · [`009f6cac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f6/009f6c14.md#insn-009f6cac) · [`009f6c54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f6/009f6c14.md#insn-009f6c54)
- 新版 [`009f6cc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f6/009f6c68.md#insn-009f6cc8) · [`009f6d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f6/009f6c68.md#insn-009f6d00) · [`009f6ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f6/009f6c68.md#insn-009f6ca8)

~~~diff
- 009f6c74 ["INT_ADD", "register:40f0:8", ["const:9f6c74:8", "const:4:8"]]
- 009f6c74 ["CALL", null, ["callee:00c586e0:8"]]
+ 009f6cc8 ["INT_ADD", "register:40f0:8", ["const:9f6cc8:8", "const:4:8"]]
+ 009f6cc8 ["CALL", null, ["callee:00c586e0:8"]]
- 009f6c74 bytes 67860994
+ 009f6cc8 bytes 86860994
- 009f6cac ["INT_ADD", "register:40f0:8", ["const:9f6cac:8", "const:4:8"]]
- 009f6cac ["CALL", null, ["callee:0046969c:8"]]
+ 009f6d00 ["INT_ADD", "register:40f0:8", ["const:9f6d00:8", "const:4:8"]]
+ 009f6d00 ["CALL", null, ["callee:0046969c:8"]]
- 009f6cac bytes 6ccae997
+ 009f6d00 bytes 67cae997
- 009f6c54 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:978:8"]]
- 009f6c54 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 009f6ca8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 009f6ca8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 009f6c54 bytes 08bd44f9
+ 009f6ca8 bytes 083d45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fdaec8bf3151b97d37f41f1a83088283"></a>

### [`009f7478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f7/009f7478.md) → [`009f74cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f7/009f74cc.md) FUN_009f74cc

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`009f7de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f7/009f7de0.md) [`009f9ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f9/009f9ee0.md) [`009fabcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fa/009fabcc.md) · 呼出先 14件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`00665d64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00665/00665d64.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 3件 [`009f7e34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f7/009f7e34.md) [`009f9f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f9/009f9f34.md) [`009fac20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fa/009fac20.md) · 呼出先 14件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`0047e64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e64c.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`00665da4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00665/00665da4.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 86.56% / 新版 86.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 15件, `store_destination` 14件, `store_value` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "009f77a8",
      "incomplete_value": false,
      "site": "009f77a8",
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
                "const:ca5000:8"
              ],
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f7754",
      "incomplete_value": false,
      "site": "009f7754",
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
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:f00:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "ordinal": 28,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "009f77ac",
      "incomplete_value": false,
      "site": "009f77ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca5000:8"
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f7758",
      "incomplete_value": false,
      "site": "009f7758",
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
            "const:f00:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009f77a8",
      "incomplete_value": false,
      "site": "009f77ac",
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
                "const:ca5000:8"
              ],
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f7754",
      "incomplete_value": false,
      "site": "009f7758",
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
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:f00:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:8:8"
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
      "009f7500",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "009f750c",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009f7514",
      "PARAM",
      [
        "storage",
        "00c71990",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "009f7500",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "009f750c",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009f7514",
      "PARAM",
      [
        "storage",
        "00c71a60",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f74c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f7/009f7478.md#insn-009f74c8) · [`009f7680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f7/009f7478.md#insn-009f7680) · [`009f76d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f7/009f7478.md#insn-009f76d4)
- 新版 [`009f751c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f7/009f74cc.md#insn-009f751c) · [`009f76d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f7/009f74cc.md#insn-009f76d4) · [`009f7728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f7/009f74cc.md#insn-009f7728)

~~~diff
- 009f74c8 ["INT_ADD", "register:40f0:8", ["const:9f74c8:8", "const:4:8"]]
- 009f74c8 ["CALL", null, ["callee:00c586e0:8"]]
+ 009f751c ["INT_ADD", "register:40f0:8", ["const:9f751c:8", "const:4:8"]]
+ 009f751c ["CALL", null, ["callee:00c586e0:8"]]
- 009f74c8 bytes 52840994
+ 009f751c bytes 71840994
- 009f7680 ["INT_ADD", "register:40f0:8", ["const:9f7680:8", "const:4:8"]]
- 009f7680 ["CALL", null, ["callee:0047e64c:8"]]
+ 009f76d4 ["INT_ADD", "register:40f0:8", ["const:9f76d4:8", "const:4:8"]]
+ 009f76d4 ["CALL", null, ["callee:0047e64c:8"]]
- 009f7680 bytes e31bea97
+ 009f76d4 bytes de1bea97
- 009f76d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 009f76d4 ["INT_ADD", "register:40f0:8", ["const:9f76d4:8", "const:4:8"]]
- 009f76d4 ["CALLIND", null, ["register:0:8"]]
+ 009f7728 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009f7728 ["INT_ADD", "register:40f0:8", ["const:9f7728:8", "const:4:8"]]
+ 009f7728 ["CALLIND", null, ["register:0:8"]]
- 009f76d4 bytes 00013fd6
+ 009f7728 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38c245b2a7bf26743b3955b20c6ff27e"></a>

### [`009f7b74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f7/009f7b74.md) → [`009f7bc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f7/009f7bc8.md) FUN_009f7bc8

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00a03e68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03e68.md) · 呼出先 14件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00467f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467f54.md) [`00468c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468c68.md) [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md)
- 新版 呼出元 1件 [`00a03ebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a03/00a03ebc.md) · 呼出先 14件 [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00467b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467b6c.md) [`00467f94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467f94.md) [`00468ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468ca8.md) [`00468fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468fc8.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.42% / 新版 97.42%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "009f7bf0",
      "incomplete_value": true,
      "site": "009f7bf0",
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
      "definition_site": "009f7b9c",
      "incomplete_value": true,
      "site": "009f7b9c",
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
      "definition_site": "009f7bf8",
      "incomplete_value": false,
      "site": "009f7c08",
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
            "const:f28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f7ba4",
      "incomplete_value": false,
      "site": "009f7bb4",
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
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009f7c00",
      "incomplete_value": false,
      "site": "009f7c08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:a60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f7bac",
      "incomplete_value": false,
      "site": "009f7bb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:990:8"
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
      "009f7bec",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "009f7bf8",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009f7c00",
      "PARAM",
      [
        "storage",
        "00c71990",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "009f7bec",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "009f7bf8",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009f7c00",
      "PARAM",
      [
        "storage",
        "00c71a60",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f7bb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f7/009f7b74.md#insn-009f7bb4) · [`009f7b98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f7/009f7b74.md#insn-009f7b98) · [`009f7ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f7/009f7b74.md#insn-009f7ba4)
- 新版 [`009f7c08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f7/009f7bc8.md#insn-009f7c08) · [`009f7bec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f7/009f7bc8.md#insn-009f7bec) · [`009f7bf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f7/009f7bc8.md#insn-009f7bf8)

~~~diff
- 009f7bb4 ["INT_ADD", "register:40f0:8", ["const:9f7bb4:8", "const:4:8"]]
- 009f7bb4 ["CALL", null, ["callee:00c586e0:8"]]
+ 009f7c08 ["INT_ADD", "register:40f0:8", ["const:9f7c08:8", "const:4:8"]]
+ 009f7c08 ["CALL", null, ["callee:00c586e0:8"]]
- 009f7bb4 bytes 97820994
+ 009f7c08 bytes b6820994
- 009f7b98 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:978:8"]]
- 009f7b98 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 009f7bec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 009f7bec ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 009f7b98 bytes 00bd44f9
+ 009f7bec bytes 003d45f9
- 009f7ba4 ["COPY", "tmp:0:8", ["const:e58:8"]]
- 009f7ba4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 009f7ba4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 009f7ba4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 009f7bf8 ["COPY", "tmp:0:8", ["const:f28:8"]]
+ 009f7bf8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 009f7bf8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 009f7bf8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 009f7ba4 bytes 21603991
+ 009f7bf8 bytes 21a03c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3bed71c5af816e87d6ed32b009554e1d"></a>

### [`009f7de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f7/009f7de0.md) → [`009f7e34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f7/009f7e34.md) FUN_009f7e34

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00a052a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a052a4.md) · 呼出先 33件 [`0046daf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046daf4.md) [`005d8bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8bc8.md) [`006648a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/006648a0.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b6fec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6fec.md)
- 新版 呼出元 1件 [`00a052f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a05/00a052f8.md) · 呼出先 33件 [`0046db34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046db34.md) [`005d8c08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d8/005d8c08.md) [`006648e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00664/006648e0.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b7044`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b7044.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.37% / 新版 96.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009f7f88",
      "incomplete_value": false,
      "site": "009f7f88",
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
            "const:5f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f7f34",
      "incomplete_value": false,
      "site": "009f7f34",
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
            "const:520:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009f8028",
      "incomplete_value": false,
      "site": "009f8028",
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
            "const:670:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f7fd4",
      "incomplete_value": false,
      "site": "009f7fd4",
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
            "const:5a0:8"
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
      "definition_site": "009f8070",
      "incomplete_value": false,
      "site": "009f8078",
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
            "const:6f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f801c",
      "incomplete_value": false,
      "site": "009f8024",
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
            "const:620:8"
          ]
        ]
      ]
    },
    "ordinal": 21,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009f7e68",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "009f7e74",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009f7e7c",
      "PARAM",
      [
        "storage",
        "00c71990",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "009f7e68",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "009f7e74",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009f7e7c",
      "PARAM",
      [
        "storage",
        "00c71a60",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f7e34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f7/009f7de0.md#insn-009f7e34) · [`009f7ec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f7/009f7de0.md#insn-009f7ec8) · [`009f7ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f7/009f7de0.md#insn-009f7ee0)
- 新版 [`009f7e88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f7/009f7e34.md#insn-009f7e88) · [`009f7f1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f7/009f7e34.md#insn-009f7f1c) · [`009f7f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f7/009f7e34.md#insn-009f7f34)

~~~diff
- 009f7e34 ["INT_ADD", "register:40f0:8", ["const:9f7e34:8", "const:4:8"]]
- 009f7e34 ["CALL", null, ["callee:00c586e0:8"]]
+ 009f7e88 ["INT_ADD", "register:40f0:8", ["const:9f7e88:8", "const:4:8"]]
+ 009f7e88 ["CALL", null, ["callee:00c586e0:8"]]
- 009f7e34 bytes f7810994
+ 009f7e88 bytes 16820994
- 009f7ec8 ["INT_ADD", "register:40f0:8", ["const:9f7ec8:8", "const:4:8"]]
- 009f7ec8 ["CALL", null, ["ram:6648a0:8"]]
+ 009f7f1c ["INT_ADD", "register:40f0:8", ["const:9f7f1c:8", "const:4:8"]]
+ 009f7f1c ["CALL", null, ["ram:6648e0:8"]]
- 009f7ec8 bytes 76b2f197
+ 009f7f1c bytes 71b2f197
- 009f7ee0 ["INT_ADD", "register:40f0:8", ["const:9f7ee0:8", "const:4:8"]]
- 009f7ee0 ["CALL", null, ["callee:00a834bc:8"]]
+ 009f7f34 ["INT_ADD", "register:40f0:8", ["const:9f7f34:8", "const:4:8"]]
+ 009f7f34 ["CALL", null, ["callee:00a834bc:8"]]
- 009f7ee0 bytes 5b2d0294
+ 009f7f34 bytes 622d0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9ae79c134c6cf292c3a7091116a4be5"></a>

### [`009f8cac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f8/009f8cac.md) → [`009f8d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f8/009f8d00.md) FUN_009f8d00

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00a022d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a022d8.md) · 呼出先 20件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b60.md) [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md)
- 新版 呼出元 1件 [`00a0232c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a02/00a0232c.md) · 呼出先 20件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00467ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467ba0.md) [`00468fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468fc8.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition

命令の説明率　旧版 97.83% / 新版 97.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `call_target` 2件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "009f8d4c",
      "incomplete_value": true,
      "site": "009f8d4c",
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
      "definition_site": "009f8cf8",
      "incomplete_value": true,
      "site": "009f8cf8",
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
      "definition_site": "009f8d54",
      "incomplete_value": false,
      "site": "009f8d68",
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
            "const:f28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f8d00",
      "incomplete_value": false,
      "site": "009f8d14",
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
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009f8d5c",
      "incomplete_value": false,
      "site": "009f8d68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:a60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009f8d08",
      "incomplete_value": false,
      "site": "009f8d14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:990:8"
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
      "009f8d48",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "009f8d54",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009f8d5c",
      "PARAM",
      [
        "storage",
        "00c71990",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "009f8d48",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      "009f8d54",
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "009f8d5c",
      "PARAM",
      [
        "storage",
        "00c71a60",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009f8d14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f8/009f8cac.md#insn-009f8d14) · [`009f8e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f8/009f8cac.md#insn-009f8e10) · [`009f8e1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f8/009f8cac.md#insn-009f8e1c)
- 新版 [`009f8d68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f8/009f8d00.md#insn-009f8d68) · [`009f8e64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f8/009f8d00.md#insn-009f8e64) · [`009f8e70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f8/009f8d00.md#insn-009f8e70)

~~~diff
- 009f8d14 ["INT_ADD", "register:40f0:8", ["const:9f8d14:8", "const:4:8"]]
- 009f8d14 ["CALL", null, ["callee:00c586e0:8"]]
+ 009f8d68 ["INT_ADD", "register:40f0:8", ["const:9f8d68:8", "const:4:8"]]
+ 009f8d68 ["CALL", null, ["callee:00c586e0:8"]]
- 009f8d14 bytes 3f7e0994
+ 009f8d68 bytes 5e7e0994
- 009f8e10 ["INT_ADD", "register:40f0:8", ["const:9f8e10:8", "const:4:8"]]
- 009f8e10 ["CALL", null, ["ram:6cba74:8"]]
+ 009f8e64 ["INT_ADD", "register:40f0:8", ["const:9f8e64:8", "const:4:8"]]
+ 009f8e64 ["CALL", null, ["ram:6cbacc:8"]]
- 009f8e10 bytes 194bf397
+ 009f8e64 bytes 1a4bf397
- 009f8e1c ["INT_ADD", "register:40f0:8", ["const:9f8e1c:8", "const:4:8"]]
- 009f8e1c ["CALL", null, ["ram:6ccb78:8"]]
+ 009f8e70 ["INT_ADD", "register:40f0:8", ["const:9f8e70:8", "const:4:8"]]
+ 009f8e70 ["CALL", null, ["ram:6ccbd0:8"]]
- 009f8e1c bytes 574ff397
+ 009f8e70 bytes 584ff397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

