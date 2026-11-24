# v16.0.2 → v16.0.3 · 最優先の変更候補 (58)

[一覧の目次](README.md)

<a id="compare-2a435d049ef61dabcad57ab2b5ee1e96"></a>

### [`009a3d28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a3/009a3d28.md) → [`009a4cd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a4/009a4cd4.md) _INIT_191

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 82.49% / 新版 82.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 3件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009a4d10",
      "incomplete_value": true,
      "site": "009a4d2c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "009a3d64",
      "incomplete_value": true,
      "site": "009a3d80",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "009a4d34",
      "incomplete_value": true,
      "site": "009a4d50",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "009a3d88",
      "incomplete_value": true,
      "site": "009a3da4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "kind": "store_value",
    "new": {
      "definition_site": "009a4d54",
      "incomplete_value": true,
      "site": "009a4d70",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e3d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009a3da8",
      "incomplete_value": true,
      "site": "009a3dc4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "009a4d10",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "009a4d34",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "009a4d54",
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
      "009a4d10",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "009a4d34",
      "READ",
      [
        "storage",
        "002b8048",
        null,
        "string"
      ]
    ],
    [
      "009a4d54",
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

- 旧版 [`009a3e88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a3/009a3d28.md#insn-009a3e88) · [`009a3f5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a3/009a3d28.md#insn-009a3f5c) · [`009a3d50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a3/009a3d28.md#insn-009a3d50)
- 新版 [`009a4e34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a4/009a4cd4.md#insn-009a4e34) · [`009a4f08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a4/009a4cd4.md#insn-009a4f08) · [`009a4cfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a4/009a4cd4.md#insn-009a4cfc)

~~~diff
- 009a3e88 ["INT_ADD", "register:40f0:8", ["const:9a3e88:8", "const:4:8"]]
- 009a3e88 ["CALL", null, ["callee:0043bb58:8"]]
+ 009a4e34 ["INT_ADD", "register:40f0:8", ["const:9a4e34:8", "const:4:8"]]
+ 009a4e34 ["CALL", null, ["callee:0043bb58:8"]]
- 009a3e88 bytes 6c5eea97
+ 009a4e34 bytes 495bea97
- 009a3f5c ["INT_ADD", "register:40f0:8", ["const:9a3f5c:8", "const:4:8"]]
- 009a3f5c ["CALL", null, ["callee:00c58ed0:8"]]
+ 009a4f08 ["INT_ADD", "register:40f0:8", ["const:9a4f08:8", "const:4:8"]]
+ 009a4f08 ["CALL", null, ["callee:00c58ed0:8"]]
- 009a3f5c bytes e9cf0a94
+ 009a4f08 bytes f2cf0a94
- 009a3d50 ["COPY", "register:4098:8", ["const:1123000:8"]]
+ 009a4cfc ["COPY", "register:4098:8", ["const:1124000:8"]]
- 009a3d50 bytes 133c0090
+ 009a4cfc bytes 133c0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a820079f883c3bb14c730bc6f75c8f68"></a>

### [`009a4788`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a4/009a4788.md) → [`009a5734`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a5/009a5734.md) _INIT_192

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.57% / 新版 87.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009a5770",
      "incomplete_value": true,
      "site": "009a578c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "009a47c4",
      "incomplete_value": true,
      "site": "009a47e0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "009a57f0",
      "incomplete_value": true,
      "site": "009a580c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:643:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009a4844",
      "incomplete_value": true,
      "site": "009a4860",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 21,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009a5810",
      "incomplete_value": true,
      "site": "009a582c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009a4864",
      "incomplete_value": true,
      "site": "009a4880",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "009a5770",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "009a5794",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "009a57b4",
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
      "009a5770",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "009a5794",
      "READ",
      [
        "storage",
        "002b8048",
        null,
        "string"
      ]
    ],
    [
      "009a57b4",
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

- 旧版 [`009a49bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a4/009a4788.md#insn-009a49bc) · [`009a47b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a4/009a4788.md#insn-009a47b0) · [`009a47b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a4/009a4788.md#insn-009a47b4)
- 新版 [`009a5968`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a5/009a5734.md#insn-009a5968) · [`009a575c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a5/009a5734.md#insn-009a575c) · [`009a5760`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a5/009a5734.md#insn-009a5760)

~~~diff
- 009a49bc ["INT_ADD", "register:40f0:8", ["const:9a49bc:8", "const:4:8"]]
- 009a49bc ["CALL", null, ["callee:00c58ed0:8"]]
+ 009a5968 ["INT_ADD", "register:40f0:8", ["const:9a5968:8", "const:4:8"]]
+ 009a5968 ["CALL", null, ["callee:00c58ed0:8"]]
- 009a49bc bytes 51cd0a94
+ 009a5968 bytes 5acd0a94
- 009a47b0 ["COPY", "register:4098:8", ["const:1123000:8"]]
+ 009a575c ["COPY", "register:4098:8", ["const:1124000:8"]]
- 009a47b0 bytes f33b00f0
+ 009a575c bytes f33b00f0
- 009a47b4 ["COPY", "tmp:0:8", ["const:c58:8"]]
- 009a47b4 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 009a47b4 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 009a47b4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 009a5760 ["COPY", "tmp:0:8", ["const:c18:8"]]
+ 009a5760 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 009a5760 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 009a5760 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 009a47b4 bytes 73623191
+ 009a5760 bytes 73623091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-736d58678d0f0affefffbd45335c3c21"></a>

### [`009a4b18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a4/009a4b18.md) → [`009a5ac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a5/009a5ac4.md) _INIT_193

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

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
      "definition_site": "009a5b00",
      "incomplete_value": true,
      "site": "009a5b1c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "009a4b54",
      "incomplete_value": true,
      "site": "009a4b70",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "009a5b24",
      "incomplete_value": true,
      "site": "009a5b40",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "009a4b78",
      "incomplete_value": true,
      "site": "009a4b94",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "kind": "store_value",
    "new": {
      "definition_site": "009a5b44",
      "incomplete_value": true,
      "site": "009a5b60",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e3d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009a4b98",
      "incomplete_value": true,
      "site": "009a4bb4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "009a5b00",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "009a5b24",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "009a5b44",
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
      "009a5b00",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "009a5b24",
      "READ",
      [
        "storage",
        "002b8048",
        null,
        "string"
      ]
    ],
    [
      "009a5b44",
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

- 旧版 [`009a4c78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a4/009a4b18.md#insn-009a4c78) · [`009a4d4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a4/009a4b18.md#insn-009a4d4c) · [`009a4b40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a4/009a4b18.md#insn-009a4b40)
- 新版 [`009a5c24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a5/009a5ac4.md#insn-009a5c24) · [`009a5cf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a5/009a5ac4.md#insn-009a5cf8) · [`009a5aec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a5/009a5ac4.md#insn-009a5aec)

~~~diff
- 009a4c78 ["INT_ADD", "register:40f0:8", ["const:9a4c78:8", "const:4:8"]]
- 009a4c78 ["CALL", null, ["callee:0043bb58:8"]]
+ 009a5c24 ["INT_ADD", "register:40f0:8", ["const:9a5c24:8", "const:4:8"]]
+ 009a5c24 ["CALL", null, ["callee:0043bb58:8"]]
- 009a4c78 bytes f05aea97
+ 009a5c24 bytes cd57ea97
- 009a4d4c ["INT_ADD", "register:40f0:8", ["const:9a4d4c:8", "const:4:8"]]
- 009a4d4c ["CALL", null, ["callee:00c58ed0:8"]]
+ 009a5cf8 ["INT_ADD", "register:40f0:8", ["const:9a5cf8:8", "const:4:8"]]
+ 009a5cf8 ["CALL", null, ["callee:00c58ed0:8"]]
- 009a4d4c bytes 6dcc0a94
+ 009a5cf8 bytes 76cc0a94
- 009a4b40 ["COPY", "register:4098:8", ["const:1123000:8"]]
+ 009a5aec ["COPY", "register:4098:8", ["const:1124000:8"]]
- 009a4b40 bytes f33b00f0
+ 009a5aec bytes f33b00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53302975fc2267565d615cbfefe0b3e0"></a>

### [`009a4eb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a4/009a4eb0.md) → [`009a5e5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a5/009a5e5c.md) FUN_009a5e5c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0089bce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089b/0089bce4.md) · 呼出先 1件 [`0048e0f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048e0f8.md)
- 新版 呼出元 1件 [`0089cc90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0089c/0089cc90.md) · 呼出先 1件 [`0048e418`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048e/0048e418.md)

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
      "definition_site": "009a5e6c",
      "incomplete_value": false,
      "site": "009a5e74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1124000:8"
          ],
          [
            "leaf",
            "const:c60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009a4ec0",
      "incomplete_value": false,
      "site": "009a4ec8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1123000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
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
      "009a5e6c",
      "PARAM",
      [
        "storage",
        "01123ca0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009a5e6c",
      "PARAM",
      [
        "storage",
        "01124c60",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a4ec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a4/009a4eb0.md#insn-009a4ec8) · [`009a4ebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a4/009a4eb0.md#insn-009a4ebc) · [`009a4ec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a4/009a4eb0.md#insn-009a4ec0)
- 新版 [`009a5e74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a5/009a5e5c.md#insn-009a5e74) · [`009a5e68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a5/009a5e5c.md#insn-009a5e68) · [`009a5e6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a5/009a5e5c.md#insn-009a5e6c)

~~~diff
- 009a4ec8 ["INT_ADD", "register:40f0:8", ["const:9a4ec8:8", "const:4:8"]]
- 009a4ec8 ["CALL", null, ["callee:0048e418:8"]]
+ 009a5e74 ["INT_ADD", "register:40f0:8", ["const:9a5e74:8", "const:4:8"]]
+ 009a5e74 ["CALL", null, ["callee:0048e418:8"]]
- 009a4ec8 bytes 8ca4eb97
+ 009a5e74 bytes 69a1eb97
- 009a4ebc ["COPY", "register:4008:8", ["const:1123000:8"]]
+ 009a5e68 ["COPY", "register:4008:8", ["const:1124000:8"]]
- 009a4ebc bytes e13b00f0
+ 009a5e68 bytes e13b00f0
- 009a4ec0 ["COPY", "tmp:0:8", ["const:ca0:8"]]
- 009a4ec0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 009a4ec0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 009a4ec0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 009a5e6c ["COPY", "tmp:0:8", ["const:c60:8"]]
+ 009a5e6c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 009a5e6c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 009a5e6c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 009a4ec0 bytes 21803291
+ 009a5e6c bytes 21803191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c33cf8ce197d1309b919e82b5073255a"></a>

### [`009a4edc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a4/009a4edc.md) → [`009a5e88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a5/009a5e88.md) FUN_009a5e88

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0089bce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089b/0089bce4.md) · 呼出先 1件 [`0048e0f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048e0f8.md)
- 新版 呼出元 1件 [`0089cc90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0089c/0089cc90.md) · 呼出先 1件 [`0048e418`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048e/0048e418.md)

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
      "definition_site": "009a5e98",
      "incomplete_value": false,
      "site": "009a5ea0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1124000:8"
          ],
          [
            "leaf",
            "const:c80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009a4eec",
      "incomplete_value": false,
      "site": "009a4ef4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1123000:8"
          ],
          [
            "leaf",
            "const:cc0:8"
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
      "009a5e98",
      "PARAM",
      [
        "storage",
        "01123cc0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009a5e98",
      "PARAM",
      [
        "storage",
        "01124c80",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a4ef4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a4/009a4edc.md#insn-009a4ef4) · [`009a4ee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a4/009a4edc.md#insn-009a4ee8) · [`009a4eec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a4/009a4edc.md#insn-009a4eec)
- 新版 [`009a5ea0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a5/009a5e88.md#insn-009a5ea0) · [`009a5e94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a5/009a5e88.md#insn-009a5e94) · [`009a5e98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a5/009a5e88.md#insn-009a5e98)

~~~diff
- 009a4ef4 ["INT_ADD", "register:40f0:8", ["const:9a4ef4:8", "const:4:8"]]
- 009a4ef4 ["CALL", null, ["callee:0048e418:8"]]
+ 009a5ea0 ["INT_ADD", "register:40f0:8", ["const:9a5ea0:8", "const:4:8"]]
+ 009a5ea0 ["CALL", null, ["callee:0048e418:8"]]
- 009a4ef4 bytes 81a4eb97
+ 009a5ea0 bytes 5ea1eb97
- 009a4ee8 ["COPY", "register:4008:8", ["const:1123000:8"]]
+ 009a5e94 ["COPY", "register:4008:8", ["const:1124000:8"]]
- 009a4ee8 bytes e13b00f0
+ 009a5e94 bytes e13b00f0
- 009a4eec ["COPY", "tmp:0:8", ["const:cc0:8"]]
- 009a4eec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 009a4eec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 009a4eec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 009a5e98 ["COPY", "tmp:0:8", ["const:c80:8"]]
+ 009a5e98 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 009a5e98 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 009a5e98 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 009a4eec bytes 21003391
+ 009a5e98 bytes 21003291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-165ad603669942c304d7d0a77dfdeca2"></a>

### [`009a4f08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a4/009a4f08.md) → [`009a5eb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a5/009a5eb4.md) FUN_009a5eb4

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0089bce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089b/0089bce4.md) · 呼出先 12件 [`0048e1d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048e1d4.md) [`00493cb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493cb8.md) [`00493cc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493cc0.md) [`00493d28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493d28.md) [`009a5114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a5/009a5114.md)
- 新版 呼出元 1件 [`0089cc90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0089c/0089cc90.md) · 呼出先 12件 [`0048e4f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048e/0048e4f4.md) [`00493fd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493fd8.md) [`00493fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493fe0.md) [`00494048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494048.md) [`009a60c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a6/009a60c0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.29% / 新版 95.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009a5f40",
      "incomplete_value": false,
      "site": "009a5f40",
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
            "const:6b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009a4f94",
      "incomplete_value": false,
      "site": "009a4f94",
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
            "const:6e0:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009a5f58",
      "incomplete_value": false,
      "site": "009a5f5c",
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
            "const:740:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009a4fac",
      "incomplete_value": false,
      "site": "009a4fb0",
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
            "const:770:8"
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
      "009a5f40",
      "DATA",
      [
        "storage",
        "00c886e0",
        null,
        "undefined *"
      ]
    ],
    [
      "009a5f5c",
      "DATA",
      [
        "storage",
        "00c88770",
        null,
        "undefined *"
      ]
    ],
    [
      "009a5f94",
      "READ",
      [
        "storage",
        "00c88790",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "009a5f40",
      "DATA",
      [
        "storage",
        "00c896b0",
        null,
        "undefined *"
      ]
    ],
    [
      "009a5f5c",
      "DATA",
      [
        "storage",
        "00c89740",
        null,
        "undefined *"
      ]
    ],
    [
      "009a5f94",
      "READ",
      [
        "storage",
        "00c89760",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a4f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a4/009a4f08.md#insn-009a4f40) · [`009a4f4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a4/009a4f08.md#insn-009a4f4c) · [`009a4f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a4/009a4f08.md#insn-009a4f60)
- 新版 [`009a5eec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a5/009a5eb4.md#insn-009a5eec) · [`009a5ef8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a5/009a5eb4.md#insn-009a5ef8) · [`009a5f0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a5/009a5eb4.md#insn-009a5f0c)

~~~diff
- 009a4f40 ["INT_ADD", "register:40f0:8", ["const:9a4f40:8", "const:4:8"]]
- 009a4f40 ["CALL", null, ["callee:0048e4f4:8"]]
+ 009a5eec ["INT_ADD", "register:40f0:8", ["const:9a5eec:8", "const:4:8"]]
+ 009a5eec ["CALL", null, ["callee:0048e4f4:8"]]
- 009a4f40 bytes a5a4eb97
+ 009a5eec bytes 82a1eb97
- 009a4f4c ["INT_ADD", "register:40f0:8", ["const:9a4f4c:8", "const:4:8"]]
- 009a4f4c ["CALL", null, ["callee:00494048:8"]]
+ 009a5ef8 ["INT_ADD", "register:40f0:8", ["const:9a5ef8:8", "const:4:8"]]
+ 009a5ef8 ["CALL", null, ["callee:00494048:8"]]
- 009a4f4c bytes 77bbeb97
+ 009a5ef8 bytes 54b8eb97
- 009a4f60 ["INT_ADD", "register:40f0:8", ["const:9a4f60:8", "const:4:8"]]
- 009a4f60 ["CALL", null, ["callee:00493fe0:8"]]
+ 009a5f0c ["INT_ADD", "register:40f0:8", ["const:9a5f0c:8", "const:4:8"]]
+ 009a5f0c ["CALL", null, ["callee:00493fe0:8"]]
- 009a4f60 bytes 58bbeb97
+ 009a5f0c bytes 35b8eb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e12b1174f6eef6d01ca987d58c37b942"></a>

### [`009a5114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a5/009a5114.md) → [`009a60c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a6/009a60c0.md) FUN_009a60c0

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009a4f08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a4/009a4f08.md) · 呼出先 13件 [`00598b74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598b74.md) [`00598d34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598d34.md) [`005a7574`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a7/005a7574.md) [`00795e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795e7c.md) [`00795eb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795eb4.md)
- 新版 呼出元 1件 [`009a5eb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a5/009a5eb4.md) · 呼出先 13件 [`00598e94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00598/00598e94.md) [`00599054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00599/00599054.md) [`005a7924`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005a7/005a7924.md) [`00796258`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00796/00796258.md) [`00796290`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00796/00796290.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.51% / 新版 98.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009a6204",
      "incomplete_value": true,
      "site": "009a6204",
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
            "const:8d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009a5258",
      "incomplete_value": true,
      "site": "009a5258",
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
            "const:900:8"
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
      "009a6134",
      "DATA",
      [
        "storage",
        "00c6daf0",
        null,
        "undefined *"
      ]
    ],
    [
      "009a6204",
      "DATA",
      [
        "storage",
        "00c88900",
        null,
        "undefined *"
      ]
    ],
    [
      "009a62b8",
      "READ",
      [
        "storage",
        "00c88928",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009a6134",
      "DATA",
      [
        "storage",
        "00c6eac0",
        null,
        "undefined *"
      ]
    ],
    [
      "009a6204",
      "DATA",
      [
        "storage",
        "00c898d0",
        null,
        "undefined *"
      ]
    ],
    [
      "009a62b8",
      "READ",
      [
        "storage",
        "00c898f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a5148`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a5/009a5114.md#insn-009a5148) · [`009a5154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a5/009a5114.md#insn-009a5154) · [`009a5168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a5/009a5114.md#insn-009a5168)
- 新版 [`009a60f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a6/009a60c0.md#insn-009a60f4) · [`009a6100`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a6/009a60c0.md#insn-009a6100) · [`009a6114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a6/009a60c0.md#insn-009a6114)

~~~diff
- 009a5148 ["INT_ADD", "register:40f0:8", ["const:9a5148:8", "const:4:8"]]
- 009a5148 ["CALL", null, ["callee:00c58f30:8"]]
+ 009a60f4 ["INT_ADD", "register:40f0:8", ["const:9a60f4:8", "const:4:8"]]
+ 009a60f4 ["CALL", null, ["callee:00c58f30:8"]]
- 009a5148 bytes 86cb0a94
+ 009a60f4 bytes 8fcb0a94
- 009a5154 ["INT_ADD", "register:40f0:8", ["const:9a5154:8", "const:4:8"]]
- 009a5154 ["CALL", null, ["callee:005a7924:8"]]
+ 009a6100 ["INT_ADD", "register:40f0:8", ["const:9a6100:8", "const:4:8"]]
+ 009a6100 ["CALL", null, ["callee:005a7924:8"]]
- 009a5154 bytes 0809f097
+ 009a6100 bytes 0906f097
- 009a5168 ["INT_ADD", "register:40f0:8", ["const:9a5168:8", "const:4:8"]]
- 009a5168 ["CALL", null, ["callee:009a901c:8"]]
+ 009a6114 ["INT_ADD", "register:40f0:8", ["const:9a6114:8", "const:4:8"]]
+ 009a6114 ["CALL", null, ["callee:009a901c:8"]]
- 009a5168 bytes c20b0094
+ 009a6114 bytes c20b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f6adb5674f81278be6ff1a26388efbe"></a>

### [`009a555c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a5/009a555c.md) → [`009a6508`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a6/009a6508.md) FUN_009a6508

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0089bce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089b/0089bce4.md) · 呼出先 12件 [`0048e1d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048e1d4.md) [`00493cb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493cb8.md) [`00493cc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493cc0.md) [`00493d28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493d28.md) [`009a5808`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a5/009a5808.md)
- 新版 呼出元 1件 [`0089cc90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0089c/0089cc90.md) · 呼出先 12件 [`0048e4f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048e/0048e4f4.md) [`00493fd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493fd8.md) [`00493fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493fe0.md) [`00494048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494048.md) [`009a67b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a6/009a67b4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.58% / 新版 96.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009a65fc",
      "incomplete_value": false,
      "site": "009a65fc",
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
            "const:7c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009a5650",
      "incomplete_value": false,
      "site": "009a5650",
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
            "const:7f0:8"
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
      "definition_site": "009a6618",
      "incomplete_value": false,
      "site": "009a661c",
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
            "const:850:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009a566c",
      "incomplete_value": false,
      "site": "009a5670",
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
            "const:880:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009a65fc",
      "DATA",
      [
        "storage",
        "00c887f0",
        null,
        "undefined *"
      ]
    ],
    [
      "009a661c",
      "DATA",
      [
        "storage",
        "00c88880",
        null,
        "undefined *"
      ]
    ],
    [
      "009a6654",
      "READ",
      [
        "storage",
        "00c888a0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "009a65fc",
      "DATA",
      [
        "storage",
        "00c897c0",
        null,
        "undefined *"
      ]
    ],
    [
      "009a661c",
      "DATA",
      [
        "storage",
        "00c89850",
        null,
        "undefined *"
      ]
    ],
    [
      "009a6654",
      "READ",
      [
        "storage",
        "00c89870",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a55b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a5/009a555c.md#insn-009a55b8) · [`009a55c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a5/009a555c.md#insn-009a55c4) · [`009a55d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a5/009a555c.md#insn-009a55d4)
- 新版 [`009a6564`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a6/009a6508.md#insn-009a6564) · [`009a6570`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a6/009a6508.md#insn-009a6570) · [`009a6580`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a6/009a6508.md#insn-009a6580)

~~~diff
- 009a55b8 ["INT_ADD", "register:40f0:8", ["const:9a55b8:8", "const:4:8"]]
- 009a55b8 ["CALL", null, ["callee:0048e4f4:8"]]
+ 009a6564 ["INT_ADD", "register:40f0:8", ["const:9a6564:8", "const:4:8"]]
+ 009a6564 ["CALL", null, ["callee:0048e4f4:8"]]
- 009a55b8 bytes 07a3eb97
+ 009a6564 bytes e49feb97
- 009a55c4 ["INT_ADD", "register:40f0:8", ["const:9a55c4:8", "const:4:8"]]
- 009a55c4 ["CALL", null, ["callee:00494048:8"]]
+ 009a6570 ["INT_ADD", "register:40f0:8", ["const:9a6570:8", "const:4:8"]]
+ 009a6570 ["CALL", null, ["callee:00494048:8"]]
- 009a55c4 bytes d9b9eb97
+ 009a6570 bytes b6b6eb97
- 009a55d4 ["INT_ADD", "register:40f0:8", ["const:9a55d4:8", "const:4:8"]]
- 009a55d4 ["CALL", null, ["callee:00494048:8"]]
+ 009a6580 ["INT_ADD", "register:40f0:8", ["const:9a6580:8", "const:4:8"]]
+ 009a6580 ["CALL", null, ["callee:00494048:8"]]
- 009a55d4 bytes d5b9eb97
+ 009a6580 bytes b2b6eb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3b36e78d1969f776134308ba9768e77"></a>

### [`009a5808`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a5/009a5808.md) → [`009a67b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a6/009a67b4.md) FUN_009a67b4

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009a555c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a5/009a555c.md) · 呼出先 13件 [`00598b74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598b74.md) [`00598d34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598d34.md) [`005a8578`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a8/005a8578.md) [`00795e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795e7c.md) [`00795eb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795eb4.md)
- 新版 呼出元 1件 [`009a6508`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a6/009a6508.md) · 呼出先 13件 [`00598e94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00598/00598e94.md) [`00599054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00599/00599054.md) [`005a8928`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005a8/005a8928.md) [`00796258`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00796/00796258.md) [`00796290`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00796/00796290.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.54% / 新版 97.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009a682c",
      "incomplete_value": false,
      "site": "009a6830",
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
                "const:c6e000:8"
              ],
              [
                "leaf",
                "const:ab0:8"
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
      "definition_site": "009a5880",
      "incomplete_value": false,
      "site": "009a5884",
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
                "const:ae0:8"
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009a6900",
      "incomplete_value": false,
      "site": "009a6900",
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
            "const:950:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009a5954",
      "incomplete_value": false,
      "site": "009a5954",
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
      "009a6830",
      "DATA",
      [
        "storage",
        "00c6daf0",
        null,
        "undefined *"
      ]
    ],
    [
      "009a6900",
      "DATA",
      [
        "storage",
        "00c88980",
        null,
        "undefined *"
      ]
    ],
    [
      "009a69b4",
      "READ",
      [
        "storage",
        "00c889a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009a6830",
      "DATA",
      [
        "storage",
        "00c6eac0",
        null,
        "undefined *"
      ]
    ],
    [
      "009a6900",
      "DATA",
      [
        "storage",
        "00c89950",
        null,
        "undefined *"
      ]
    ],
    [
      "009a69b4",
      "READ",
      [
        "storage",
        "00c89978",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a5840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a5/009a5808.md#insn-009a5840) · [`009a5850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a5/009a5808.md#insn-009a5850) · [`009a5864`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a5/009a5808.md#insn-009a5864)
- 新版 [`009a67ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a6/009a67b4.md#insn-009a67ec) · [`009a67fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a6/009a67b4.md#insn-009a67fc) · [`009a6810`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a6/009a67b4.md#insn-009a6810)

~~~diff
- 009a5840 ["INT_ADD", "register:40f0:8", ["const:9a5840:8", "const:4:8"]]
- 009a5840 ["CALL", null, ["callee:00c58f30:8"]]
+ 009a67ec ["INT_ADD", "register:40f0:8", ["const:9a67ec:8", "const:4:8"]]
+ 009a67ec ["CALL", null, ["callee:00c58f30:8"]]
- 009a5840 bytes c8c90a94
+ 009a67ec bytes d1c90a94
- 009a5850 ["INT_ADD", "register:40f0:8", ["const:9a5850:8", "const:4:8"]]
- 009a5850 ["CALL", null, ["callee:005a8928:8"]]
+ 009a67fc ["INT_ADD", "register:40f0:8", ["const:9a67fc:8", "const:4:8"]]
+ 009a67fc ["CALL", null, ["callee:005a8928:8"]]
- 009a5850 bytes 4a0bf097
+ 009a67fc bytes 4b08f097
- 009a5864 ["INT_ADD", "register:40f0:8", ["const:9a5864:8", "const:4:8"]]
- 009a5864 ["CALL", null, ["callee:009a9778:8"]]
+ 009a6810 ["INT_ADD", "register:40f0:8", ["const:9a6810:8", "const:4:8"]]
+ 009a6810 ["CALL", null, ["callee:009a9778:8"]]
- 009a5864 bytes da0b0094
+ 009a6810 bytes da0b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c6c94c989a712d0abe50c49d1795b66"></a>

### [`009a5c58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a5/009a5c58.md) → [`009a6c04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a6/009a6c04.md) FUN_009a6c04

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`009a63f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a6/009a63f4.md) [`009a6d50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a6/009a6d50.md) · 呼出先 12件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`004741d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00474/004741d8.md) [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`00492d0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492d0c.md) [`00749010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00749/00749010.md)
- 新版 呼出元 2件 [`009a73a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a7/009a73a0.md) [`009a7cfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a7/009a7cfc.md) · 呼出先 12件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`004744f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00474/004744f8.md) [`0048d058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d058.md) [`0049302c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/0049302c.md) [`007493c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00749/007493c0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.01% / 新版 91.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009a6c64",
      "incomplete_value": true,
      "site": "009a6c64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a57:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009a5cb8",
      "incomplete_value": true,
      "site": "009a5cb8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:979:8"
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
      "definition_site": "009a6e20",
      "incomplete_value": true,
      "site": "009a6e20",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2af000:8"
              ],
              [
                "leaf",
                "const:86:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009a5e74",
      "incomplete_value": true,
      "site": "009a5e74",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:faf:8"
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
      "definition_site": "009a6e08",
      "incomplete_value": true,
      "site": "009a6e24",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "009a5e5c",
      "incomplete_value": true,
      "site": "009a5e78",
      "value": [
        "LOAD",
        "8",
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
      "009a6c54",
      "READ",
      [
        "storage",
        "002ba979",
        null,
        "string"
      ]
    ],
    [
      "009a6ca4",
      "READ",
      [
        "storage",
        "002c32d0",
        null,
        null
      ]
    ],
    [
      "009a6d34",
      "READ",
      [
        "storage",
        "002c0670",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009a6c54",
      "READ",
      [
        "storage",
        "002baa57",
        null,
        "string"
      ]
    ],
    [
      "009a6ca4",
      "READ",
      [
        "storage",
        "002c3320",
        null,
        null
      ]
    ],
    [
      "009a6d34",
      "READ",
      [
        "storage",
        "002c06ba",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a5f7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a5/009a5c58.md#insn-009a5f7c) · [`009a6000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a5/009a5c58.md#insn-009a6000) · [`009a5ca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a5/009a5c58.md#insn-009a5ca4)
- 新版 [`009a6f28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a6/009a6c04.md#insn-009a6f28) · [`009a6fac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a6/009a6c04.md#insn-009a6fac) · [`009a6c50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a6/009a6c04.md#insn-009a6c50)

~~~diff
- 009a5f7c ["INT_ADD", "register:40f0:8", ["const:9a5f7c:8", "const:4:8"]]
- 009a5f7c ["CALL", null, ["callee:00c59010:8"]]
+ 009a6f28 ["INT_ADD", "register:40f0:8", ["const:9a6f28:8", "const:4:8"]]
+ 009a6f28 ["CALL", null, ["callee:00c59010:8"]]
- 009a5f7c bytes 31c80a94
+ 009a6f28 bytes 3ac80a94
- 009a6000 ["INT_ADD", "register:40f0:8", ["const:9a6000:8", "const:4:8"]]
- 009a6000 ["CALL", null, ["ram:48cd38:8"]]
+ 009a6fac ["INT_ADD", "register:40f0:8", ["const:9a6fac:8", "const:4:8"]]
+ 009a6fac ["CALL", null, ["ram:48d058:8"]]
- 009a6000 bytes 4e9beb97
+ 009a6fac bytes 2b98eb97
- 009a5ca4 ["COPY", "tmp:0:8", ["const:979:8"]]
- 009a5ca4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 009a5ca4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 009a5ca4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 009a6c50 ["COPY", "tmp:0:8", ["const:a57:8"]]
+ 009a6c50 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 009a6c50 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 009a6c50 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 009a5ca4 bytes 29e52591
+ 009a6c50 bytes 295d2991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dce53b7c4b99f2345c87d7931d5256fc"></a>

### [`009a62ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a6/009a62ac.md) → [`009a7258`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a7/009a7258.md) FUN_009a7258

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009a727c",
      "incomplete_value": true,
      "site": "009a7280",
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
                "register:4040:8"
              ],
              [
                "leaf",
                "const:ab0:8"
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
      "definition_site": "009a62d0",
      "incomplete_value": true,
      "site": "009a62d4",
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
                "register:4040:8"
              ],
              [
                "leaf",
                "const:ae0:8"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009a7280",
      "DATA",
      [
        "storage",
        "00c6daf0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009a7280",
      "DATA",
      [
        "storage",
        "00c6eac0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a62c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a6/009a62ac.md#insn-009a62c4) · [`009a62c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a6/009a62ac.md#insn-009a62c8) · [`009a62e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a6/009a62ac.md#insn-009a62e0)
- 新版 [`009a7270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a7/009a7258.md#insn-009a7270) · [`009a7274`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a7/009a7258.md#insn-009a7274) · [`009a728c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a7/009a7258.md#insn-009a728c)

~~~diff
- 009a62c4 ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 009a7270 ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 009a62c4 bytes 281600f0
+ 009a7270 bytes 281600f0
- 009a62c8 ["COPY", "tmp:0:8", ["const:ae0:8"]]
- 009a62c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009a62c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009a62c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009a7274 ["COPY", "tmp:0:8", ["const:ab0:8"]]
+ 009a7274 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009a7274 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009a7274 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009a62c8 bytes 08812b91
+ 009a7274 bytes 08c12a91
- 009a62e0 ["INT_ADD", "register:40f0:8", ["const:9a62e0:8", "const:4:8"]]
- 009a62e0 ["CALL", null, ["callee:00c58f50:8"]]
+ 009a728c ["INT_ADD", "register:40f0:8", ["const:9a728c:8", "const:4:8"]]
+ 009a728c ["CALL", null, ["callee:00c58f50:8"]]
- 009a62e0 bytes 28c70a94
+ 009a728c bytes 31c70a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2e77378eb2b1a3717618972d4bf193c"></a>

### [`009a63d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a6/009a63d4.md) → [`009a7380`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a7/009a7380.md) FUN_009a7380

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009a7388",
      "incomplete_value": false,
      "site": "009a738c",
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
            "const:6b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009a63dc",
      "incomplete_value": false,
      "site": "009a63e0",
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
            "const:6e0:8"
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
      "009a738c",
      "DATA",
      [
        "storage",
        "00c886e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009a738c",
      "DATA",
      [
        "storage",
        "00c896b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a63d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a6/009a63d4.md#insn-009a63d8) · [`009a63dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a6/009a63d4.md#insn-009a63dc)
- 新版 [`009a7384`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a7/009a7380.md#insn-009a7384) · [`009a7388`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a7/009a7380.md#insn-009a7388)

~~~diff
- 009a63d8 ["COPY", "register:4048:8", ["const:c88000:8"]]
+ 009a7384 ["COPY", "register:4048:8", ["const:c89000:8"]]
- 009a63d8 bytes 091700d0
+ 009a7384 bytes 091700d0
- 009a63dc ["COPY", "tmp:0:8", ["const:6e0:8"]]
- 009a63dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 009a63dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 009a63dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 009a7388 ["COPY", "tmp:0:8", ["const:6b0:8"]]
+ 009a7388 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 009a7388 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 009a7388 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 009a63dc bytes 29811b91
+ 009a7388 bytes 29c11a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3087186d052997a17ca3319814fa1636"></a>

### [`009a63f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a6/009a63f4.md) → [`009a73a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a7/009a73a0.md) FUN_009a73a0

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`005a784c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a7/005a784c.md) [`009a5c58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a5/009a5c58.md) [`009a68f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a6/009a68f0.md) [`009a6aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a6/009a6aa0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`005a7bfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005a7/005a7bfc.md) [`009a6c04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a6/009a6c04.md) [`009a789c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a7/009a789c.md) [`009a7a4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a7/009a7a4c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.58% / 新版 98.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009a75bc",
      "incomplete_value": true,
      "site": "009a75bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9c7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009a6610",
      "incomplete_value": true,
      "site": "009a6610",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8f8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 42,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009a75a0",
      "READ",
      [
        "storage",
        "002b68f8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009a75a0",
      "READ",
      [
        "storage",
        "002b69c7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a6450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a6/009a63f4.md#insn-009a6450) · [`009a64ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a6/009a63f4.md#insn-009a64ac) · [`009a64dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a6/009a63f4.md#insn-009a64dc)
- 新版 [`009a73fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a7/009a73a0.md#insn-009a73fc) · [`009a7458`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a7/009a73a0.md#insn-009a7458) · [`009a7488`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a7/009a73a0.md#insn-009a7488)

~~~diff
- 009a6450 ["INT_ADD", "register:40f0:8", ["const:9a6450:8", "const:4:8"]]
- 009a6450 ["CALL", null, ["callee:005a7bfc:8"]]
+ 009a73fc ["INT_ADD", "register:40f0:8", ["const:9a73fc:8", "const:4:8"]]
+ 009a73fc ["CALL", null, ["callee:005a7bfc:8"]]
- 009a6450 bytes ff04f097
+ 009a73fc bytes 0002f097
- 009a64ac ["INT_ADD", "register:40f0:8", ["const:9a64ac:8", "const:4:8"]]
- 009a64ac ["CALL", null, ["callee:0043be80:8"]]
+ 009a7458 ["INT_ADD", "register:40f0:8", ["const:9a7458:8", "const:4:8"]]
+ 009a7458 ["CALL", null, ["callee:0043be80:8"]]
- 009a64ac bytes ad55ea97
+ 009a7458 bytes 8a52ea97
- 009a64dc ["INT_ADD", "register:40f0:8", ["const:9a64dc:8", "const:4:8"]]
- 009a64dc ["CALL", null, ["callee:0043be80:8"]]
+ 009a7488 ["INT_ADD", "register:40f0:8", ["const:9a7488:8", "const:4:8"]]
+ 009a7488 ["CALL", null, ["callee:0043be80:8"]]
- 009a64dc bytes a155ea97
+ 009a7488 bytes 7e52ea97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80aa61b4bc866863e5ecf4a56056e213"></a>

### [`009a6a38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a6/009a6a38.md) → [`009a79e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a7/009a79e4.md) FUN_009a79e4

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`009a68f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a6/009a68f0.md) [`009a6aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a6/009a6aa0.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 2件 [`009a789c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a7/009a789c.md) [`009a7a4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a7/009a7a4c.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "009a79f0",
      "incomplete_value": false,
      "site": "009a79f4",
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
      "definition_site": "009a6a44",
      "incomplete_value": false,
      "site": "009a6a48",
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
      "009a79f0",
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
      "009a79f0",
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

- 旧版 [`009a6a48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a6/009a6a38.md#insn-009a6a48) · [`009a6a40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a6/009a6a38.md#insn-009a6a40) · [`009a6a44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a6/009a6a38.md#insn-009a6a44)
- 新版 [`009a79f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a7/009a79e4.md#insn-009a79f4) · [`009a79ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a7/009a79e4.md#insn-009a79ec) · [`009a79f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a7/009a79e4.md#insn-009a79f0)

~~~diff
- 009a6a48 ["INT_ADD", "register:40f0:8", ["const:9a6a48:8", "const:4:8"]]
- 009a6a48 ["CALL", null, ["callee:0043bad8:8"]]
+ 009a79f4 ["INT_ADD", "register:40f0:8", ["const:9a79f4:8", "const:4:8"]]
+ 009a79f4 ["CALL", null, ["callee:0043bad8:8"]]
- 009a6a48 bytes 5c53ea97
+ 009a79f4 bytes 3950ea97
- 009a6a40 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 009a79ec ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 009a6a40 bytes 80c8ffb0
+ 009a79ec bytes 80c8ffb0
- 009a6a44 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 009a6a44 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 009a6a44 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 009a6a44 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 009a79f0 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 009a79f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 009a79f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 009a79f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 009a6a44 bytes 00303e91
+ 009a79f0 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c30057c1ed3ec1854f8f9affbd893d0"></a>

### [`009a6c88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a6/009a6c88.md) → [`009a7c34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a7/009a7c34.md) FUN_009a7c34

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009a7c48",
      "incomplete_value": false,
      "site": "009a7c4c",
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
            "const:740:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009a6c9c",
      "incomplete_value": false,
      "site": "009a6ca0",
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
            "const:770:8"
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
      "009a7c4c",
      "DATA",
      [
        "storage",
        "00c88770",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009a7c4c",
      "DATA",
      [
        "storage",
        "00c89740",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a6c94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a6/009a6c88.md#insn-009a6c94) · [`009a6c98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a6/009a6c88.md#insn-009a6c98) · [`009a6c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a6/009a6c88.md#insn-009a6c9c)
- 新版 [`009a7c40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a7/009a7c34.md#insn-009a7c40) · [`009a7c44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a7/009a7c34.md#insn-009a7c44) · [`009a7c48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a7/009a7c34.md#insn-009a7c48)

~~~diff
- 009a6c94 ["INT_ADD", "register:40f0:8", ["const:9a6c94:8", "const:4:8"]]
- 009a6c94 ["CALL", null, ["callee:00c58f30:8"]]
+ 009a7c40 ["INT_ADD", "register:40f0:8", ["const:9a7c40:8", "const:4:8"]]
+ 009a7c40 ["CALL", null, ["callee:00c58f30:8"]]
- 009a6c94 bytes b3c40a94
+ 009a7c40 bytes bcc40a94
- 009a6c98 ["COPY", "register:4040:8", ["const:c88000:8"]]
+ 009a7c44 ["COPY", "register:4040:8", ["const:c89000:8"]]
- 009a6c98 bytes 081700d0
+ 009a7c44 bytes 081700d0
- 009a6c9c ["COPY", "tmp:0:8", ["const:770:8"]]
- 009a6c9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009a6c9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009a6c9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009a7c48 ["COPY", "tmp:0:8", ["const:740:8"]]
+ 009a7c48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009a7c48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009a7c48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009a6c9c bytes 08c11d91
+ 009a7c48 bytes 08011d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89c822864659897825997299e8386983"></a>

### [`009a6cac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a6/009a6cac.md) → [`009a7c58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a7/009a7c58.md) FUN_009a7c58

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009a7c5c",
      "incomplete_value": false,
      "site": "009a7c60",
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
            "const:740:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009a6cb0",
      "incomplete_value": false,
      "site": "009a6cb4",
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
            "const:770:8"
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
      "009a7c60",
      "DATA",
      [
        "storage",
        "00c88770",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009a7c60",
      "DATA",
      [
        "storage",
        "00c89740",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a6cac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a6/009a6cac.md#insn-009a6cac) · [`009a6cb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a6/009a6cac.md#insn-009a6cb0)
- 新版 [`009a7c58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a7/009a7c58.md#insn-009a7c58) · [`009a7c5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a7/009a7c58.md#insn-009a7c5c)

~~~diff
- 009a6cac ["COPY", "register:4040:8", ["const:c88000:8"]]
+ 009a7c58 ["COPY", "register:4040:8", ["const:c89000:8"]]
- 009a6cac bytes 081700d0
+ 009a7c58 bytes 081700d0
- 009a6cb0 ["COPY", "tmp:0:8", ["const:770:8"]]
- 009a6cb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009a6cb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009a6cb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009a7c5c ["COPY", "tmp:0:8", ["const:740:8"]]
+ 009a7c5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009a7c5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009a7c5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009a6cb0 bytes 08c11d91
+ 009a7c5c bytes 08011d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5308a07366cca71b4c9e3f2656692930"></a>

### [`009a6cf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a6/009a6cf8.md) → [`009a7ca4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a7/009a7ca4.md) FUN_009a7ca4

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009a7cc4",
      "incomplete_value": false,
      "site": "009a7cc8",
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
            "const:7c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009a6d18",
      "incomplete_value": false,
      "site": "009a6d1c",
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
            "const:7f0:8"
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
      "009a7cc8",
      "DATA",
      [
        "storage",
        "00c887f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009a7cc8",
      "DATA",
      [
        "storage",
        "00c897c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a6d0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a6/009a6cf8.md#insn-009a6d0c) · [`009a6d14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a6/009a6cf8.md#insn-009a6d14) · [`009a6d18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a6/009a6cf8.md#insn-009a6d18)
- 新版 [`009a7cb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a7/009a7ca4.md#insn-009a7cb8) · [`009a7cc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a7/009a7ca4.md#insn-009a7cc0) · [`009a7cc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a7/009a7ca4.md#insn-009a7cc4)

~~~diff
- 009a6d0c ["INT_ADD", "register:40f0:8", ["const:9a6d0c:8", "const:4:8"]]
- 009a6d0c ["CALL", null, ["callee:00c58f30:8"]]
+ 009a7cb8 ["INT_ADD", "register:40f0:8", ["const:9a7cb8:8", "const:4:8"]]
+ 009a7cb8 ["CALL", null, ["callee:00c58f30:8"]]
- 009a6d0c bytes 95c40a94
+ 009a7cb8 bytes 9ec40a94
- 009a6d14 ["COPY", "register:4040:8", ["const:c88000:8"]]
+ 009a7cc0 ["COPY", "register:4040:8", ["const:c89000:8"]]
- 009a6d14 bytes 081700d0
+ 009a7cc0 bytes 081700d0
- 009a6d18 ["COPY", "tmp:0:8", ["const:7f0:8"]]
- 009a6d18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009a6d18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009a6d18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009a7cc4 ["COPY", "tmp:0:8", ["const:7c0:8"]]
+ 009a7cc4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009a7cc4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009a7cc4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009a6d18 bytes 08c11f91
+ 009a7cc4 bytes 08011f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-adfc2f1b460357d39f0dff56974db05d"></a>

### [`009a6d30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a6/009a6d30.md) → [`009a7cdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a7/009a7cdc.md) FUN_009a7cdc

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009a7ce4",
      "incomplete_value": false,
      "site": "009a7ce8",
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
            "const:7c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009a6d38",
      "incomplete_value": false,
      "site": "009a6d3c",
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
            "const:7f0:8"
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
      "009a7ce8",
      "DATA",
      [
        "storage",
        "00c887f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009a7ce8",
      "DATA",
      [
        "storage",
        "00c897c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a6d34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a6/009a6d30.md#insn-009a6d34) · [`009a6d38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a6/009a6d30.md#insn-009a6d38)
- 新版 [`009a7ce0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a7/009a7cdc.md#insn-009a7ce0) · [`009a7ce4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a7/009a7cdc.md#insn-009a7ce4)

~~~diff
- 009a6d34 ["COPY", "register:4048:8", ["const:c88000:8"]]
+ 009a7ce0 ["COPY", "register:4048:8", ["const:c89000:8"]]
- 009a6d34 bytes 091700d0
+ 009a7ce0 bytes 091700d0
- 009a6d38 ["COPY", "tmp:0:8", ["const:7f0:8"]]
- 009a6d38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 009a6d38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 009a6d38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 009a7ce4 ["COPY", "tmp:0:8", ["const:7c0:8"]]
+ 009a7ce4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 009a7ce4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 009a7ce4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 009a6d38 bytes 29c11f91
+ 009a7ce4 bytes 29011f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f59de815134f91fbb805b3915c43fced"></a>

### [`009a6ed4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a6/009a6ed4.md) → [`009a7e80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a7/009a7e80.md) FUN_009a7e80

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009a7e94",
      "incomplete_value": false,
      "site": "009a7e98",
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
            "const:850:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009a6ee8",
      "incomplete_value": false,
      "site": "009a6eec",
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
            "const:880:8"
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
      "009a7e98",
      "DATA",
      [
        "storage",
        "00c88880",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009a7e98",
      "DATA",
      [
        "storage",
        "00c89850",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a6ee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a6/009a6ed4.md#insn-009a6ee0) · [`009a6ee4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a6/009a6ed4.md#insn-009a6ee4) · [`009a6ee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a6/009a6ed4.md#insn-009a6ee8)
- 新版 [`009a7e8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a7/009a7e80.md#insn-009a7e8c) · [`009a7e90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a7/009a7e80.md#insn-009a7e90) · [`009a7e94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a7/009a7e80.md#insn-009a7e94)

~~~diff
- 009a6ee0 ["INT_ADD", "register:40f0:8", ["const:9a6ee0:8", "const:4:8"]]
- 009a6ee0 ["CALL", null, ["callee:00c58f30:8"]]
+ 009a7e8c ["INT_ADD", "register:40f0:8", ["const:9a7e8c:8", "const:4:8"]]
+ 009a7e8c ["CALL", null, ["callee:00c58f30:8"]]
- 009a6ee0 bytes 20c40a94
+ 009a7e8c bytes 29c40a94
- 009a6ee4 ["COPY", "register:4040:8", ["const:c88000:8"]]
+ 009a7e90 ["COPY", "register:4040:8", ["const:c89000:8"]]
- 009a6ee4 bytes 081700d0
+ 009a7e90 bytes 081700d0
- 009a6ee8 ["COPY", "tmp:0:8", ["const:880:8"]]
- 009a6ee8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009a6ee8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009a6ee8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009a7e94 ["COPY", "tmp:0:8", ["const:850:8"]]
+ 009a7e94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009a7e94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009a7e94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009a6ee8 bytes 08012291
+ 009a7e94 bytes 08412191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1f6f05e769f4f63bb1945b7293ce369"></a>

### [`009a6ef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a6/009a6ef8.md) → [`009a7ea4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a7/009a7ea4.md) FUN_009a7ea4

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009a7ea8",
      "incomplete_value": false,
      "site": "009a7eac",
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
            "const:850:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009a6efc",
      "incomplete_value": false,
      "site": "009a6f00",
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
            "const:880:8"
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
      "009a7eac",
      "DATA",
      [
        "storage",
        "00c88880",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009a7eac",
      "DATA",
      [
        "storage",
        "00c89850",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a6ef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a6/009a6ef8.md#insn-009a6ef8) · [`009a6efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a6/009a6ef8.md#insn-009a6efc)
- 新版 [`009a7ea4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a7/009a7ea4.md#insn-009a7ea4) · [`009a7ea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a7/009a7ea4.md#insn-009a7ea8)

~~~diff
- 009a6ef8 ["COPY", "register:4040:8", ["const:c88000:8"]]
+ 009a7ea4 ["COPY", "register:4040:8", ["const:c89000:8"]]
- 009a6ef8 bytes 081700d0
+ 009a7ea4 bytes 081700d0
- 009a6efc ["COPY", "tmp:0:8", ["const:880:8"]]
- 009a6efc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009a6efc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009a6efc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009a7ea8 ["COPY", "tmp:0:8", ["const:850:8"]]
+ 009a7ea8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009a7ea8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009a7ea8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009a6efc bytes 08012291
+ 009a7ea8 bytes 08412191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e22ab2c30ee5dace0da88ac959a9443b"></a>

### [`009a6f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a6/009a6f3c.md) → [`009a7ee8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a7/009a7ee8.md) FUN_009a7ee8

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`009a5c58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a5/009a5c58.md) [`009a6f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a6/009a6f3c.md) · 呼出先 22件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) [`00441d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441d2c.md)
- 新版 呼出元 2件 [`009a6c04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a6/009a6c04.md) [`009a7ee8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a7/009a7ee8.md) · 呼出先 22件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`004412d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004412d0.md) [`0044204c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/0044204c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.48% / 新版 98.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009a803c",
      "incomplete_value": false,
      "site": "009a8044",
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
            "const:62:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009a7090",
      "incomplete_value": false,
      "site": "009a7098",
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009a8060",
      "incomplete_value": false,
      "site": "009a806c",
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
            "const:f73:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009a70b4",
      "incomplete_value": false,
      "site": "009a70c0",
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009a8194",
      "incomplete_value": false,
      "site": "009a819c",
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
            "const:ef6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009a71e8",
      "incomplete_value": false,
      "site": "009a71f0",
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
      "009a803c",
      "PARAM",
      [
        "storage",
        "002b7f93",
        null,
        null
      ]
    ],
    [
      "009a8060",
      "PARAM",
      [
        "storage",
        "002c0f29",
        null,
        "string"
      ]
    ],
    [
      "009a8194",
      "PARAM",
      [
        "storage",
        "002b5e27",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009a803c",
      "PARAM",
      [
        "storage",
        "002b8062",
        null,
        null
      ]
    ],
    [
      "009a8060",
      "PARAM",
      [
        "storage",
        "002c0f73",
        null,
        "string"
      ]
    ],
    [
      "009a8194",
      "PARAM",
      [
        "storage",
        "002b5ef6",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a7098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a6/009a6f3c.md#insn-009a7098) · [`009a70c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a6/009a6f3c.md#insn-009a70c0) · [`009a71f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a6/009a6f3c.md#insn-009a71f0)
- 新版 [`009a8044`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a7/009a7ee8.md#insn-009a8044) · [`009a806c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a7/009a7ee8.md#insn-009a806c) · [`009a819c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a7/009a7ee8.md#insn-009a819c)

~~~diff
- 009a7098 ["INT_ADD", "register:40f0:8", ["const:9a7098:8", "const:4:8"]]
- 009a7098 ["CALL", null, ["callee:004421f4:8"]]
+ 009a8044 ["INT_ADD", "register:40f0:8", ["const:9a8044:8", "const:4:8"]]
+ 009a8044 ["CALL", null, ["callee:004421f4:8"]]
- 009a7098 bytes 8f6bea97
+ 009a8044 bytes 6c68ea97
- 009a70c0 ["INT_ADD", "register:40f0:8", ["const:9a70c0:8", "const:4:8"]]
- 009a70c0 ["CALL", null, ["callee:00442b54:8"]]
+ 009a806c ["INT_ADD", "register:40f0:8", ["const:9a806c:8", "const:4:8"]]
+ 009a806c ["CALL", null, ["callee:00442b54:8"]]
- 009a70c0 bytes dd6dea97
+ 009a806c bytes ba6aea97
- 009a71f0 ["INT_ADD", "register:40f0:8", ["const:9a71f0:8", "const:4:8"]]
- 009a71f0 ["CALL", null, ["callee:004421f4:8"]]
+ 009a819c ["INT_ADD", "register:40f0:8", ["const:9a819c:8", "const:4:8"]]
+ 009a819c ["CALL", null, ["callee:004421f4:8"]]
- 009a71f0 bytes 396bea97
+ 009a819c bytes 1668ea97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6045dbe355a30117be25c278337c1d0a"></a>

### [`009a773c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a7/009a773c.md) → [`009a86e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a8/009a86e8.md) FUN_009a86e8

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`009a5c58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a5/009a5c58.md) [`009a773c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a7/009a773c.md) [`009b0558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b0/009b0558.md) [`00b0e9d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0e/00b0e9d0.md) · 呼出先 23件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) [`00441d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441d2c.md)
- 新版 呼出元 4件 [`009a6c04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a6/009a6c04.md) [`009a86e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a8/009a86e8.md) [`009b1504`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b1/009b1504.md) [`00b0f9c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b0f/00b0f9c4.md) · 呼出先 23件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`004412d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004412d0.md) [`0044204c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/0044204c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.69% / 新版 98.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009a883c",
      "incomplete_value": false,
      "site": "009a8844",
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
            "const:62:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009a7890",
      "incomplete_value": false,
      "site": "009a7898",
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009a88f8",
      "incomplete_value": false,
      "site": "009a8900",
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
            "const:ef6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009a794c",
      "incomplete_value": false,
      "site": "009a7954",
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009a8910",
      "incomplete_value": false,
      "site": "009a891c",
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
            "const:f73:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009a7964",
      "incomplete_value": false,
      "site": "009a7970",
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
      "009a883c",
      "PARAM",
      [
        "storage",
        "002b7f93",
        null,
        null
      ]
    ],
    [
      "009a88f8",
      "PARAM",
      [
        "storage",
        "002b5e27",
        null,
        null
      ]
    ],
    [
      "009a8910",
      "PARAM",
      [
        "storage",
        "002c0f29",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009a883c",
      "PARAM",
      [
        "storage",
        "002b8062",
        null,
        null
      ]
    ],
    [
      "009a88f8",
      "PARAM",
      [
        "storage",
        "002b5ef6",
        null,
        null
      ]
    ],
    [
      "009a8910",
      "PARAM",
      [
        "storage",
        "002c0f73",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a7898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a7/009a773c.md#insn-009a7898) · [`009a7954`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a7/009a773c.md#insn-009a7954) · [`009a7970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a7/009a773c.md#insn-009a7970)
- 新版 [`009a8844`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a8/009a86e8.md#insn-009a8844) · [`009a8900`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a8/009a86e8.md#insn-009a8900) · [`009a891c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a8/009a86e8.md#insn-009a891c)

~~~diff
- 009a7898 ["INT_ADD", "register:40f0:8", ["const:9a7898:8", "const:4:8"]]
- 009a7898 ["CALL", null, ["callee:004421f4:8"]]
+ 009a8844 ["INT_ADD", "register:40f0:8", ["const:9a8844:8", "const:4:8"]]
+ 009a8844 ["CALL", null, ["callee:004421f4:8"]]
- 009a7898 bytes 8f69ea97
+ 009a8844 bytes 6c66ea97
- 009a7954 ["INT_ADD", "register:40f0:8", ["const:9a7954:8", "const:4:8"]]
- 009a7954 ["CALL", null, ["callee:004421f4:8"]]
+ 009a8900 ["INT_ADD", "register:40f0:8", ["const:9a8900:8", "const:4:8"]]
+ 009a8900 ["CALL", null, ["callee:004421f4:8"]]
- 009a7954 bytes 6069ea97
+ 009a8900 bytes 3d66ea97
- 009a7970 ["INT_ADD", "register:40f0:8", ["const:9a7970:8", "const:4:8"]]
- 009a7970 ["CALL", null, ["callee:00442b54:8"]]
+ 009a891c ["INT_ADD", "register:40f0:8", ["const:9a891c:8", "const:4:8"]]
+ 009a891c ["CALL", null, ["callee:00442b54:8"]]
- 009a7970 bytes b16bea97
+ 009a891c bytes 8e68ea97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f61b9a813b47fc6253c7d7a20ab75825"></a>

### [`009a8070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a8/009a8070.md) → [`009a901c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a9/009a901c.md) FUN_009a901c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`009a5114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a5/009a5114.md) · 呼出先 7件 [`00597f10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f10.md) [`005b737c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b737c.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 1件 [`009a60c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a6/009a60c0.md) · 呼出先 7件 [`00598230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00598/00598230.md) [`005b772c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b772c.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.10% / 新版 96.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009a9054",
      "incomplete_value": false,
      "site": "009a905c",
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
            "const:660:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009a80a8",
      "incomplete_value": false,
      "site": "009a80b0",
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
            "const:690:8"
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
      "009a905c",
      "DATA",
      [
        "storage",
        "00c70690",
        null,
        "pointer"
      ]
    ],
    [
      "009a9114",
      "READ",
      [
        "storage",
        "00c706a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009a905c",
      "DATA",
      [
        "storage",
        "00c71660",
        null,
        "pointer"
      ]
    ],
    [
      "009a9114",
      "READ",
      [
        "storage",
        "00c71670",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a80a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a8/009a8070.md#insn-009a80a0) · [`009a80a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a8/009a8070.md#insn-009a80a4) · [`009a80a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a8/009a8070.md#insn-009a80a8)
- 新版 [`009a904c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a9/009a901c.md#insn-009a904c) · [`009a9050`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a9/009a901c.md#insn-009a9050) · [`009a9054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a9/009a901c.md#insn-009a9054)

~~~diff
- 009a80a0 ["INT_ADD", "register:40f0:8", ["const:9a80a0:8", "const:4:8"]]
- 009a80a0 ["CALL", null, ["callee:00c58f30:8"]]
+ 009a904c ["INT_ADD", "register:40f0:8", ["const:9a904c:8", "const:4:8"]]
+ 009a904c ["CALL", null, ["callee:00c58f30:8"]]
- 009a80a0 bytes b0bf0a94
+ 009a904c bytes b9bf0a94
- 009a80a4 ["COPY", "register:4040:8", ["const:c70000:8"]]
+ 009a9050 ["COPY", "register:4040:8", ["const:c71000:8"]]
- 009a80a4 bytes 48160090
+ 009a9050 bytes 48160090
- 009a80a8 ["COPY", "tmp:0:8", ["const:690:8"]]
- 009a80a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009a80a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009a80a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009a9054 ["COPY", "tmp:0:8", ["const:660:8"]]
+ 009a9054 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009a9054 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009a9054 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009a80a8 bytes 08411a91
+ 009a9054 bytes 08811991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dbc04749f393399c23b64dbfe19d582c"></a>

### [`009a840c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a8/009a840c.md) → [`009a93b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a9/009a93b8.md) FUN_009a93b8

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

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
      "definition_site": "009a93e0",
      "incomplete_value": false,
      "site": "009a93e0",
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
            "const:8d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009a8434",
      "incomplete_value": false,
      "site": "009a8434",
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
      "009a93e0",
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
      "009a93e0",
      "DATA",
      [
        "storage",
        "00c898d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a8428`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a8/009a840c.md#insn-009a8428) · [`009a842c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a8/009a840c.md#insn-009a842c) · [`009a8430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a8/009a840c.md#insn-009a8430)
- 新版 [`009a93d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a9/009a93b8.md#insn-009a93d4) · [`009a93d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a9/009a93b8.md#insn-009a93d8)

~~~diff
- 009a8428 ["COPY", "register:4040:8", ["const:c88000:8"]]
+ 009a93d4 ["COPY", "register:4040:8", ["const:c89000:8"]]
- 009a8428 bytes 08170090
+ 009a93d4 bytes 08170090
- 009a842c ["COPY", "tmp:0:8", ["const:900:8"]]
- 009a842c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009a842c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009a842c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009a93d8 ["COPY", "tmp:0:8", ["const:8d0:8"]]
+ 009a93d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009a93d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009a93d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009a842c bytes 08012491
+ 009a93d8 bytes 08412391
- 009a8430 ["COPY", "register:40a0:8", ["register:4008:8"]]
- 009a8430 bytes f40301aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a4668dec4271796ef44a9a8d1f26073"></a>

### [`009a87cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a8/009a87cc.md) → [`009a9778`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a9/009a9778.md) FUN_009a9778

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`009a5808`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a5/009a5808.md) · 呼出先 7件 [`00597f10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f10.md) [`005b737c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b737c.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 1件 [`009a67b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a6/009a67b4.md) · 呼出先 7件 [`00598230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00598/00598230.md) [`005b772c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b772c.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.10% / 新版 96.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009a97b0",
      "incomplete_value": false,
      "site": "009a97b8",
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
            "const:660:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009a8804",
      "incomplete_value": false,
      "site": "009a880c",
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
            "const:690:8"
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
      "009a97b8",
      "DATA",
      [
        "storage",
        "00c70690",
        null,
        "pointer"
      ]
    ],
    [
      "009a9870",
      "READ",
      [
        "storage",
        "00c706a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009a97b8",
      "DATA",
      [
        "storage",
        "00c71660",
        null,
        "pointer"
      ]
    ],
    [
      "009a9870",
      "READ",
      [
        "storage",
        "00c71670",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a87fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a8/009a87cc.md#insn-009a87fc) · [`009a8800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a8/009a87cc.md#insn-009a8800) · [`009a8804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a8/009a87cc.md#insn-009a8804)
- 新版 [`009a97a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a9/009a9778.md#insn-009a97a8) · [`009a97ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a9/009a9778.md#insn-009a97ac) · [`009a97b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a9/009a9778.md#insn-009a97b0)

~~~diff
- 009a87fc ["INT_ADD", "register:40f0:8", ["const:9a87fc:8", "const:4:8"]]
- 009a87fc ["CALL", null, ["callee:00c58f30:8"]]
+ 009a97a8 ["INT_ADD", "register:40f0:8", ["const:9a97a8:8", "const:4:8"]]
+ 009a97a8 ["CALL", null, ["callee:00c58f30:8"]]
- 009a87fc bytes d9bd0a94
+ 009a97a8 bytes e2bd0a94
- 009a8800 ["COPY", "register:4040:8", ["const:c70000:8"]]
+ 009a97ac ["COPY", "register:4040:8", ["const:c71000:8"]]
- 009a8800 bytes 48160090
+ 009a97ac bytes 48160090
- 009a8804 ["COPY", "tmp:0:8", ["const:690:8"]]
- 009a8804 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009a8804 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009a8804 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009a97b0 ["COPY", "tmp:0:8", ["const:660:8"]]
+ 009a97b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009a97b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009a97b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009a8804 bytes 08411a91
+ 009a97b0 bytes 08811991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57aaca9d5eb5cdb0aaf019befd2ee932"></a>

### [`009a8944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a8/009a8944.md) → [`009a98f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a9/009a98f0.md) FUN_009a98f0

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "009a9908",
      "incomplete_value": false,
      "site": "009a9918",
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
            "const:950:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009a895c",
      "incomplete_value": false,
      "site": "009a896c",
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
      "009a9918",
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
      "009a9918",
      "DATA",
      [
        "storage",
        "00c89950",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a8958`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a8/009a8944.md#insn-009a8958) · [`009a895c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a8/009a8944.md#insn-009a895c) · [`009a8990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a8/009a8944.md#insn-009a8990)
- 新版 [`009a9904`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a9/009a98f0.md#insn-009a9904) · [`009a9908`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a9/009a98f0.md#insn-009a9908) · [`009a993c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a9/009a98f0.md#insn-009a993c)

~~~diff
- 009a8958 ["COPY", "register:4040:8", ["const:c88000:8"]]
+ 009a9904 ["COPY", "register:4040:8", ["const:c89000:8"]]
- 009a8958 bytes 08170090
+ 009a9904 bytes 08170090
- 009a895c ["COPY", "tmp:0:8", ["const:980:8"]]
- 009a895c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009a895c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009a895c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009a9908 ["COPY", "tmp:0:8", ["const:950:8"]]
+ 009a9908 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009a9908 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009a9908 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009a895c bytes 08012691
+ 009a9908 bytes 08412591
- 009a8990 ["COPY", "register:0:8", ["register:4040:8"]]
- 009a8990 ["INT_ADD", "register:40f0:8", ["const:9a8990:8", "const:4:8"]]
- 009a8990 ["CALLIND", null, ["register:0:8"]]
+ 009a993c ["COPY", "register:0:8", ["register:4040:8"]]
+ 009a993c ["INT_ADD", "register:40f0:8", ["const:9a993c:8", "const:4:8"]]
+ 009a993c ["CALLIND", null, ["register:0:8"]]
- 009a8990 bytes 00013fd6
+ 009a993c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3cf40ae9e6585fb95e37b8d700fbb2a8"></a>

### [`009a89d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a8/009a89d4.md) → [`009a9980`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a9/009a9980.md) FUN_009a9980

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.29% / 新版 94.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009a9998",
      "incomplete_value": false,
      "site": "009a99a8",
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
            "const:950:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009a89ec",
      "incomplete_value": false,
      "site": "009a89fc",
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
      "009a99a8",
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
      "009a99a8",
      "DATA",
      [
        "storage",
        "00c89950",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a89e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a8/009a89d4.md#insn-009a89e8) · [`009a89ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a8/009a89d4.md#insn-009a89ec) · [`009a8a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a8/009a89d4.md#insn-009a8a20)
- 新版 [`009a9994`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a9/009a9980.md#insn-009a9994) · [`009a9998`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a9/009a9980.md#insn-009a9998) · [`009a99cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a9/009a9980.md#insn-009a99cc)

~~~diff
- 009a89e8 ["COPY", "register:4040:8", ["const:c88000:8"]]
+ 009a9994 ["COPY", "register:4040:8", ["const:c89000:8"]]
- 009a89e8 bytes 08170090
+ 009a9994 bytes 08170090
- 009a89ec ["COPY", "tmp:0:8", ["const:980:8"]]
- 009a89ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009a89ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009a89ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009a9998 ["COPY", "tmp:0:8", ["const:950:8"]]
+ 009a9998 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009a9998 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009a9998 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009a89ec bytes 08012691
+ 009a9998 bytes 08412591
- 009a8a20 ["COPY", "register:0:8", ["register:4040:8"]]
- 009a8a20 ["INT_ADD", "register:40f0:8", ["const:9a8a20:8", "const:4:8"]]
- 009a8a20 ["CALLIND", null, ["register:0:8"]]
+ 009a99cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 009a99cc ["INT_ADD", "register:40f0:8", ["const:9a99cc:8", "const:4:8"]]
+ 009a99cc ["CALLIND", null, ["register:0:8"]]
- 009a8a20 bytes 00013fd6
+ 009a99cc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e278fddc8f1b3edd8844226252e64826"></a>

### [`009a8b68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a8/009a8b68.md) → [`009a9b14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a9/009a9b14.md) FUN_009a9b14

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.15% / 新版 96.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009a9b3c",
      "incomplete_value": true,
      "site": "009a9b3c",
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
            "const:950:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009a8b90",
      "incomplete_value": true,
      "site": "009a8b90",
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
      "009a9b3c",
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
      "009a9b3c",
      "DATA",
      [
        "storage",
        "00c89950",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a8b84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a8/009a8b68.md#insn-009a8b84) · [`009a8b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a8/009a8b68.md#insn-009a8b88) · [`009a8bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a8/009a8b68.md#insn-009a8bac)
- 新版 [`009a9b30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a9/009a9b14.md#insn-009a9b30) · [`009a9b34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a9/009a9b14.md#insn-009a9b34) · [`009a9b58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a9/009a9b14.md#insn-009a9b58)

~~~diff
- 009a8b84 ["COPY", "register:4040:8", ["const:c88000:8"]]
+ 009a9b30 ["COPY", "register:4040:8", ["const:c89000:8"]]
- 009a8b84 bytes 08170090
+ 009a9b30 bytes 08170090
- 009a8b88 ["COPY", "tmp:0:8", ["const:980:8"]]
- 009a8b88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009a8b88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009a8b88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009a9b34 ["COPY", "tmp:0:8", ["const:950:8"]]
+ 009a9b34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009a9b34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009a9b34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009a8b88 bytes 08012691
+ 009a9b34 bytes 08412591
- 009a8bac ["COPY", "register:0:8", ["register:4040:8"]]
- 009a8bac ["INT_ADD", "register:40f0:8", ["const:9a8bac:8", "const:4:8"]]
- 009a8bac ["CALLIND", null, ["register:0:8"]]
+ 009a9b58 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009a9b58 ["INT_ADD", "register:40f0:8", ["const:9a9b58:8", "const:4:8"]]
+ 009a9b58 ["CALLIND", null, ["register:0:8"]]
- 009a8bac bytes 00013fd6
+ 009a9b58 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a26c2d57bbd0c8c2fbb52baaeb592e7"></a>

### [`009a8f28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a8/009a8f28.md) → [`009a9ed4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a9/009a9ed4.md) _INIT_194

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00bc488c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc4/00bc488c.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00bc5880`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc5/00bc5880.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 7件, `store_value` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009a9f10",
      "incomplete_value": true,
      "site": "009a9f2c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "009a8f64",
      "incomplete_value": true,
      "site": "009a8f80",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "009a9f34",
      "incomplete_value": true,
      "site": "009a9f50",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "009a8f88",
      "incomplete_value": true,
      "site": "009a8fa4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "kind": "store_value",
    "new": {
      "definition_site": "009a9f54",
      "incomplete_value": true,
      "site": "009a9f70",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e3d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009a8fa8",
      "incomplete_value": true,
      "site": "009a8fc4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "009a9f10",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "009a9f34",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "009a9f54",
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
      "009a9f10",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "009a9f34",
      "READ",
      [
        "storage",
        "002b8048",
        null,
        "string"
      ]
    ],
    [
      "009a9f54",
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

- 旧版 [`009a9088`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a8/009a8f28.md#insn-009a9088) · [`009a91b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a8/009a8f28.md#insn-009a91b4) · [`009a91f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a8/009a8f28.md#insn-009a91f8)
- 新版 [`009aa034`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a9/009a9ed4.md#insn-009aa034) · [`009aa160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a9/009a9ed4.md#insn-009aa160) · [`009aa1a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009a9/009a9ed4.md#insn-009aa1a4)

~~~diff
- 009a9088 ["INT_ADD", "register:40f0:8", ["const:9a9088:8", "const:4:8"]]
- 009a9088 ["CALL", null, ["callee:0043bb58:8"]]
+ 009aa034 ["INT_ADD", "register:40f0:8", ["const:9aa034:8", "const:4:8"]]
+ 009aa034 ["CALL", null, ["callee:0043bb58:8"]]
- 009a9088 bytes ec49ea97
+ 009aa034 bytes c946ea97
- 009a91b4 ["INT_ADD", "register:40f0:8", ["const:9a91b4:8", "const:4:8"]]
- 009a91b4 ["CALL", null, ["callee:00c58ed0:8"]]
+ 009aa160 ["INT_ADD", "register:40f0:8", ["const:9aa160:8", "const:4:8"]]
+ 009aa160 ["CALL", null, ["callee:00c58ed0:8"]]
- 009a91b4 bytes 53bb0a94
+ 009aa160 bytes 5cbb0a94
- 009a91f8 ["INT_ADD", "register:40f0:8", ["const:9a91f8:8", "const:4:8"]]
- 009a91f8 ["CALL", null, ["callee:00c58ed0:8"]]
+ 009aa1a4 ["INT_ADD", "register:40f0:8", ["const:9aa1a4:8", "const:4:8"]]
+ 009aa1a4 ["CALL", null, ["callee:00c58ed0:8"]]
- 009a91f8 bytes 42bb0a94
+ 009aa1a4 bytes 4bbb0a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ca1b090c465bd6602ca48dd92f2bcac"></a>

### [`009a9354`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a9/009a9354.md) → [`009aa300`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009aa/009aa300.md) FUN_009aa300

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`0076453c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/0076453c.md) [`009acc84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ac/009acc84.md) [`009b5c0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b5/009b5c0c.md) [`009b5c80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b5/009b5c80.md) · 呼出先 2件 [`00a33bf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a33/00a33bf0.md) [`00c58260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58260.md)
- 新版 呼出元 4件 [`00764918`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00764/00764918.md) [`009adc30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ad/009adc30.md) [`009b6bb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b6/009b6bb8.md) [`009b6c2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b6/009b6c2c.md) · 呼出先 2件 [`00a34be4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a34/00a34be4.md) [`00c59230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59230.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009aa320",
      "incomplete_value": false,
      "site": "009aa328",
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
            "const:4e6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009a9374",
      "incomplete_value": false,
      "site": "009a937c",
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
      "009aa320",
      "PARAM",
      [
        "storage",
        "002a638e",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "009aa320",
      "PARAM",
      [
        "storage",
        "002a64e6",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a937c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a9/009a9354.md#insn-009a937c) · [`009a9374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a9/009a9354.md#insn-009a9374) · [`009a93a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a9/009a9354.md#insn-009a93a0)
- 新版 [`009aa328`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009aa/009aa300.md#insn-009aa328) · [`009aa320`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009aa/009aa300.md#insn-009aa320) · [`009aa34c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009aa/009aa300.md#insn-009aa34c)

~~~diff
- 009a937c ["INT_ADD", "register:40f0:8", ["const:9a937c:8", "const:4:8"]]
- 009a937c ["CALL", null, ["callee:00c59230:8"]]
+ 009aa328 ["INT_ADD", "register:40f0:8", ["const:9aa328:8", "const:4:8"]]
+ 009aa328 ["CALL", null, ["callee:00c59230:8"]]
- 009a937c bytes b9bb0a94
+ 009aa328 bytes c2bb0a94
- 009a9374 ["COPY", "tmp:0:8", ["const:38e:8"]]
- 009a9374 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 009a9374 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 009a9374 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 009aa320 ["COPY", "tmp:0:8", ["const:4e6:8"]]
+ 009aa320 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 009aa320 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 009aa320 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 009a9374 bytes 21380e91
+ 009aa320 bytes 21981391
- 009a93a0 ["INT_ADD", "register:40f0:8", ["const:9a93a0:8", "const:4:8"]]
- 009a93a0 ["CALL", null, ["callee:00a34be4:8"]]
+ 009aa34c ["INT_ADD", "register:40f0:8", ["const:9aa34c:8", "const:4:8"]]
+ 009aa34c ["CALL", null, ["callee:00a34be4:8"]]
- 009a93a0 bytes 142a0294
+ 009aa34c bytes 262a0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ec04650537b6c2e8e370c92a9fcfcc9"></a>

### [`009a97e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a9/009a97e4.md) → [`009aa790`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009aa/009aa790.md) FUN_009aa790

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`009aa0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009aa/009aa0d0.md) · 呼出先 15件 [`0044b794`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b794.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00561d74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/00561d74.md) [`007522d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00752/007522d8.md) [`009ab13c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ab/009ab13c.md)
- 新版 呼出元 1件 [`009ab07c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ab/009ab07c.md) · 呼出先 15件 [`0044bab4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044b/0044bab4.md) [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`00562094`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00562/00562094.md) [`00752688`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00752/00752688.md) [`009ac0e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ac/009ac0e8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.15% / 新版 95.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009aa9a0",
      "incomplete_value": true,
      "site": "009aa9a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:989:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009a99f4",
      "incomplete_value": true,
      "site": "009a99f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:93f:8"
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
      "definition_site": "009aa998",
      "incomplete_value": true,
      "site": "009aa9ac",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:75a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009a99ec",
      "incomplete_value": true,
      "site": "009a9a00",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:68d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 44,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009aac08",
      "incomplete_value": false,
      "site": "009aac0c",
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
            "const:9d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009a9c5c",
      "incomplete_value": false,
      "site": "009a9c60",
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
            "const:a00:8"
          ]
        ]
      ]
    },
    "ordinal": 66,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009aa80c",
      "PARAM",
      [
        "storage",
        "002b7a4f",
        null,
        "string"
      ]
    ],
    [
      "009aa870",
      "PARAM",
      [
        "storage",
        "002b962e",
        null,
        "string"
      ]
    ],
    [
      "009aa8e0",
      "PARAM",
      [
        "storage",
        "002b3115",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009aa80c",
      "PARAM",
      [
        "storage",
        "002b7b1e",
        null,
        "string"
      ]
    ],
    [
      "009aa870",
      "PARAM",
      [
        "storage",
        "002b96fd",
        null,
        "string"
      ]
    ],
    [
      "009aa8e0",
      "PARAM",
      [
        "storage",
        "002b315f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009a9868`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a9/009a97e4.md#insn-009a9868) · [`009a98cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a9/009a97e4.md#insn-009a98cc) · [`009a993c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a9/009a97e4.md#insn-009a993c)
- 新版 [`009aa814`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009aa/009aa790.md#insn-009aa814) · [`009aa878`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009aa/009aa790.md#insn-009aa878) · [`009aa8e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009aa/009aa790.md#insn-009aa8e8)

~~~diff
- 009a9868 ["INT_ADD", "register:40f0:8", ["const:9a9868:8", "const:4:8"]]
- 009a9868 ["CALL", null, ["callee:00c59010:8"]]
+ 009aa814 ["INT_ADD", "register:40f0:8", ["const:9aa814:8", "const:4:8"]]
+ 009aa814 ["CALL", null, ["callee:00c59010:8"]]
- 009a9868 bytes f6b90a94
+ 009aa814 bytes ffb90a94
- 009a98cc ["INT_ADD", "register:40f0:8", ["const:9a98cc:8", "const:4:8"]]
- 009a98cc ["CALL", null, ["callee:00c59010:8"]]
+ 009aa878 ["INT_ADD", "register:40f0:8", ["const:9aa878:8", "const:4:8"]]
+ 009aa878 ["CALL", null, ["callee:00c59010:8"]]
- 009a98cc bytes ddb90a94
+ 009aa878 bytes e6b90a94
- 009a993c ["INT_ADD", "register:40f0:8", ["const:9a993c:8", "const:4:8"]]
- 009a993c ["CALL", null, ["callee:00c59010:8"]]
+ 009aa8e8 ["INT_ADD", "register:40f0:8", ["const:9aa8e8:8", "const:4:8"]]
+ 009aa8e8 ["CALL", null, ["callee:00c59010:8"]]
- 009a993c bytes c1b90a94
+ 009aa8e8 bytes cab90a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9aded7336b8b3082084e68c83c7c625f"></a>

### [`009aa0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009aa/009aa0d0.md) → [`009ab07c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ab/009ab07c.md) FUN_009ab07c

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009bf72c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009bf/009bf72c.md) · 呼出先 16件 [`0044b794`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b794.md) [`00561d74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/00561d74.md) [`007522d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00752/007522d8.md) [`009a97e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a9/009a97e4.md) [`009ab794`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ab/009ab794.md)
- 新版 呼出元 1件 [`009c06d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009c0/009c06d8.md) · 呼出先 16件 [`0044bab4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044b/0044bab4.md) [`00562094`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00562/00562094.md) [`00752688`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00752/00752688.md) [`009aa790`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009aa/009aa790.md) [`009ac740`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ac/009ac740.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.02% / 新版 94.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009ab0cc",
      "incomplete_value": false,
      "site": "009ab0cc",
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
            "const:a50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009aa120",
      "incomplete_value": false,
      "site": "009aa120",
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
            "const:a80:8"
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
      "definition_site": "009ab2a0",
      "incomplete_value": true,
      "site": "009ab2a0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a3000:8"
              ],
              [
                "leaf",
                "const:fd2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009aa2f4",
      "incomplete_value": true,
      "site": "009aa2f4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a3000:8"
              ],
              [
                "leaf",
                "const:f07:8"
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
      "definition_site": "009ab2a4",
      "incomplete_value": true,
      "site": "009ab2a4",
      "value": [
        "LOAD",
        "8",
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
                "const:5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009aa2f8",
      "incomplete_value": true,
      "site": "009aa2f8",
      "value": [
        "LOAD",
        "8",
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
                "const:5:8"
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
      "009ab0cc",
      "DATA",
      [
        "storage",
        "00c88a80",
        null,
        "undefined *"
      ]
    ],
    [
      "009ab128",
      "PARAM",
      [
        "storage",
        "002b7a4f",
        null,
        "string"
      ]
    ],
    [
      "009ab18c",
      "PARAM",
      [
        "storage",
        "002b962e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009ab0cc",
      "DATA",
      [
        "storage",
        "00c89a50",
        null,
        "undefined *"
      ]
    ],
    [
      "009ab128",
      "PARAM",
      [
        "storage",
        "002b7b1e",
        null,
        "string"
      ]
    ],
    [
      "009ab18c",
      "PARAM",
      [
        "storage",
        "002b96fd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009aa258`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009aa/009aa0d0.md#insn-009aa258) · [`009aa288`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009aa/009aa0d0.md#insn-009aa288) · [`009aa310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009aa/009aa0d0.md#insn-009aa310)
- 新版 [`009ab204`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ab/009ab07c.md#insn-009ab204) · [`009ab234`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ab/009ab07c.md#insn-009ab234) · [`009ab2bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ab/009ab07c.md#insn-009ab2bc)

~~~diff
- 009aa258 ["INT_ADD", "register:40f0:8", ["const:9aa258:8", "const:4:8"]]
- 009aa258 ["CALL", null, ["callee:00c59010:8"]]
+ 009ab204 ["INT_ADD", "register:40f0:8", ["const:9ab204:8", "const:4:8"]]
+ 009ab204 ["CALL", null, ["callee:00c59010:8"]]
- 009aa258 bytes 7ab70a94
+ 009ab204 bytes 83b70a94
- 009aa288 ["INT_ADD", "register:40f0:8", ["const:9aa288:8", "const:4:8"]]
- 009aa288 ["CALL", null, ["callee:00562094:8"]]
+ 009ab234 ["INT_ADD", "register:40f0:8", ["const:9ab234:8", "const:4:8"]]
+ 009ab234 ["CALL", null, ["callee:00562094:8"]]
- 009aa288 bytes bbdeee97
+ 009ab234 bytes 98dbee97
- 009aa310 ["INT_ADD", "register:40f0:8", ["const:9aa310:8", "const:4:8"]]
- 009aa310 ["CALL", null, ["callee:00c59150:8"]]
+ 009ab2bc ["INT_ADD", "register:40f0:8", ["const:9ab2bc:8", "const:4:8"]]
+ 009ab2bc ["CALL", null, ["callee:00c59150:8"]]
- 009aa310 bytes 9cb70a94
+ 009ab2bc bytes a5b70a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7cfc022d1a760829368cea70bb62770"></a>

### [`009aa678`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009aa/009aa678.md) → [`009ab624`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ab/009ab624.md) FUN_009ab624

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`009b6cac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b6/009b6cac.md) · 呼出先 18件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00440f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f9c.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`005a9f94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a9/005a9f94.md) [`005aa1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005aa/005aa1b0.md)
- 新版 呼出元 1件 [`009b7c58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b7/009b7c58.md) · 呼出先 18件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`004412bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004412bc.md) [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`005aa344`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005aa/005aa344.md) [`005aa560`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005aa/005aa560.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.75% / 新版 99.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009ab9bc",
      "incomplete_value": false,
      "site": "009ab9c0",
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
            "const:bc7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009aaa10",
      "incomplete_value": false,
      "site": "009aaa14",
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
            "const:ae9:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009ab958",
      "DATA",
      [
        "storage",
        "003965a4",
        null,
        "qword"
      ]
    ],
    [
      "009ab9bc",
      "PARAM",
      [
        "storage",
        "002bbae9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009ab958",
      "DATA",
      [
        "storage",
        "003965a4",
        "fde_003965a4",
        "dword"
      ]
    ],
    [
      "009ab9bc",
      "PARAM",
      [
        "storage",
        "002bbbc7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009aaa14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009aa/009aa678.md#insn-009aaa14) · [`009aa6f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009aa/009aa678.md#insn-009aa6f0) · [`009aa728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009aa/009aa678.md#insn-009aa728)
- 新版 [`009ab9c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ab/009ab624.md#insn-009ab9c0) · [`009ab69c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ab/009ab624.md#insn-009ab69c) · [`009ab6d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ab/009ab624.md#insn-009ab6d4)

~~~diff
- 009aaa14 ["INT_ADD", "register:40f0:8", ["const:9aaa14:8", "const:4:8"]]
- 009aaa14 ["CALL", null, ["callee:00c59230:8"]]
+ 009ab9c0 ["INT_ADD", "register:40f0:8", ["const:9ab9c0:8", "const:4:8"]]
+ 009ab9c0 ["CALL", null, ["callee:00c59230:8"]]
- 009aaa14 bytes 13b60a94
+ 009ab9c0 bytes 1cb60a94
- 009aa6f0 ["INT_ADD", "register:40f0:8", ["const:9aa6f0:8", "const:4:8"]]
- 009aa6f0 ["CALL", null, ["callee:005aa344:8"]]
+ 009ab69c ["INT_ADD", "register:40f0:8", ["const:9ab69c:8", "const:4:8"]]
+ 009ab69c ["CALL", null, ["callee:005aa344:8"]]
- 009aa6f0 bytes 29feef97
+ 009ab69c bytes 2afbef97
- 009aa728 ["INT_ADD", "register:40f0:8", ["const:9aa728:8", "const:4:8"]]
- 009aa728 ["CALL", null, ["callee:00c58f30:8"]]
+ 009ab6d4 ["INT_ADD", "register:40f0:8", ["const:9ab6d4:8", "const:4:8"]]
+ 009ab6d4 ["CALL", null, ["callee:00c58f30:8"]]
- 009aa728 bytes 0eb60a94
+ 009ab6d4 bytes 17b60a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc522c0d830de0f3c8ceb50ce6ad4ff8"></a>

### [`009aaf48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009aa/009aaf48.md) → [`009abef4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ab/009abef4.md) FUN_009abef4

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "009abf00",
      "incomplete_value": false,
      "site": "009abf0c",
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
            "const:9d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009aaf54",
      "incomplete_value": false,
      "site": "009aaf60",
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
            "const:a00:8"
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
      "009abf0c",
      "DATA",
      [
        "storage",
        "00c88a00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009abf0c",
      "DATA",
      [
        "storage",
        "00c899d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009aaf50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009aa/009aaf48.md#insn-009aaf50) · [`009aaf54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009aa/009aaf48.md#insn-009aaf54)
- 新版 [`009abefc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ab/009abef4.md#insn-009abefc) · [`009abf00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ab/009abef4.md#insn-009abf00)

~~~diff
- 009aaf50 ["COPY", "register:4050:8", ["const:c88000:8"]]
+ 009abefc ["COPY", "register:4050:8", ["const:c89000:8"]]
- 009aaf50 bytes ea1600d0
+ 009abefc bytes ea1600d0
- 009aaf54 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 009aaf54 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 009aaf54 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 009aaf54 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 009abf00 ["COPY", "tmp:0:8", ["const:9d0:8"]]
+ 009abf00 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 009abf00 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 009abf00 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 009aaf54 bytes 4a012891
+ 009abf00 bytes 4a412791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37a60d466cc47dcf74689bb8d08608fe"></a>

### [`009aaf8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009aa/009aaf8c.md) → [`009abf38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ab/009abf38.md) FUN_009abf38

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "009abf50",
      "incomplete_value": false,
      "site": "009abf5c",
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
            "const:9d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009aafa4",
      "incomplete_value": false,
      "site": "009aafb0",
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
            "const:a00:8"
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
      "009abf5c",
      "DATA",
      [
        "storage",
        "00c88a00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009abf5c",
      "DATA",
      [
        "storage",
        "00c899d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009aafa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009aa/009aaf8c.md#insn-009aafa0) · [`009aafa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009aa/009aaf8c.md#insn-009aafa4) · [`009aafd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009aa/009aaf8c.md#insn-009aafd4)
- 新版 [`009abf4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ab/009abf38.md#insn-009abf4c) · [`009abf50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ab/009abf38.md#insn-009abf50) · [`009abf80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ab/009abf38.md#insn-009abf80)

~~~diff
- 009aafa0 ["COPY", "register:4040:8", ["const:c88000:8"]]
+ 009abf4c ["COPY", "register:4040:8", ["const:c89000:8"]]
- 009aafa0 bytes e81600d0
+ 009abf4c bytes e81600d0
- 009aafa4 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 009aafa4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009aafa4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009aafa4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009abf50 ["COPY", "tmp:0:8", ["const:9d0:8"]]
+ 009abf50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009abf50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009abf50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009aafa4 bytes 08012891
+ 009abf50 bytes 08412791
- 009aafd4 ["COPY", "register:0:8", ["register:4040:8"]]
- 009aafd4 ["INT_ADD", "register:40f0:8", ["const:9aafd4:8", "const:4:8"]]
- 009aafd4 ["CALLIND", null, ["register:0:8"]]
+ 009abf80 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009abf80 ["INT_ADD", "register:40f0:8", ["const:9abf80:8", "const:4:8"]]
+ 009abf80 ["CALLIND", null, ["register:0:8"]]
- 009aafd4 bytes 00013fd6
+ 009abf80 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fcd8f94d4e87b091ae2c278ee44c9689"></a>

### [`009aafe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009aa/009aafe8.md) → [`009abf94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ab/009abf94.md) FUN_009abf94

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009abfbc",
      "incomplete_value": false,
      "site": "009abfc0",
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
            "const:9d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ab010",
      "incomplete_value": false,
      "site": "009ab014",
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
            "const:a00:8"
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
      "009abfc0",
      "DATA",
      [
        "storage",
        "00c88a00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009abfc0",
      "DATA",
      [
        "storage",
        "00c899d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009aaffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009aa/009aafe8.md#insn-009aaffc) · [`009ab00c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009aa/009aafe8.md#insn-009ab00c) · [`009ab010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009aa/009aafe8.md#insn-009ab010)
- 新版 [`009abfa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ab/009abf94.md#insn-009abfa8) · [`009abfb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ab/009abf94.md#insn-009abfb8) · [`009abfbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ab/009abf94.md#insn-009abfbc)

~~~diff
- 009aaffc ["INT_ADD", "register:40f0:8", ["const:9aaffc:8", "const:4:8"]]
- 009aaffc ["CALL", null, ["callee:00c58f30:8"]]
+ 009abfa8 ["INT_ADD", "register:40f0:8", ["const:9abfa8:8", "const:4:8"]]
+ 009abfa8 ["CALL", null, ["callee:00c58f30:8"]]
- 009aaffc bytes d9b30a94
+ 009abfa8 bytes e2b30a94
- 009ab00c ["COPY", "register:4048:8", ["const:c88000:8"]]
+ 009abfb8 ["COPY", "register:4048:8", ["const:c89000:8"]]
- 009ab00c bytes e91600b0
+ 009abfb8 bytes e91600d0
- 009ab010 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 009ab010 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 009ab010 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 009ab010 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 009abfbc ["COPY", "tmp:0:8", ["const:9d0:8"]]
+ 009abfbc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 009abfbc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 009abfbc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 009ab010 bytes 29012891
+ 009abfbc bytes 29412791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-582716d58cabf38ff13de30f042a0d50"></a>

### [`009ab080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ab/009ab080.md) → [`009ac02c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ac/009ac02c.md) FUN_009ac02c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009ac04c",
      "incomplete_value": false,
      "site": "009ac050",
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
            "const:9d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ab0a0",
      "incomplete_value": false,
      "site": "009ab0a4",
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
            "const:a00:8"
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
      "009ac050",
      "DATA",
      [
        "storage",
        "00c88a00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009ac050",
      "DATA",
      [
        "storage",
        "00c899d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009ab09c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ab/009ab080.md#insn-009ab09c) · [`009ab0a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ab/009ab080.md#insn-009ab0a0) · [`009ab0c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ab/009ab080.md#insn-009ab0c4)
- 新版 [`009ac048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ac/009ac02c.md#insn-009ac048) · [`009ac04c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ac/009ac02c.md#insn-009ac04c) · [`009ac070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ac/009ac02c.md#insn-009ac070)

~~~diff
- 009ab09c ["COPY", "register:4048:8", ["const:c88000:8"]]
+ 009ac048 ["COPY", "register:4048:8", ["const:c89000:8"]]
- 009ab09c bytes e91600b0
+ 009ac048 bytes e91600b0
- 009ab0a0 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 009ab0a0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 009ab0a0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 009ab0a0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 009ac04c ["COPY", "tmp:0:8", ["const:9d0:8"]]
+ 009ac04c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 009ac04c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 009ac04c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 009ab0a0 bytes 29012891
+ 009ac04c bytes 29412791
- 009ab0c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 009ab0c4 ["INT_ADD", "register:40f0:8", ["const:9ab0c4:8", "const:4:8"]]
- 009ab0c4 ["CALLIND", null, ["register:0:8"]]
+ 009ac070 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009ac070 ["INT_ADD", "register:40f0:8", ["const:9ac070:8", "const:4:8"]]
+ 009ac070 ["CALLIND", null, ["register:0:8"]]
- 009ab0c4 bytes 00013fd6
+ 009ac070 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-908d89865139a58ce1c8a4fe7ce77c36"></a>

### [`009ab18c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ab/009ab18c.md) → [`009ac138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ac/009ac138.md) FUN_009ac138

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00596f6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596f6c.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`004413ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004413ec.md) [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`0059728c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/0059728c.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.53% / 新版 97.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009ac304",
      "incomplete_value": true,
      "site": "009ac304",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:14d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ab358",
      "incomplete_value": true,
      "site": "009ab358",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7e:8"
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
      "definition_site": "009ac2f8",
      "incomplete_value": true,
      "site": "009ac308",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "009ab34c",
      "incomplete_value": true,
      "site": "009ab35c",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 21,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009ac484",
      "incomplete_value": true,
      "site": "009ac484",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1dc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ab4d8",
      "incomplete_value": true,
      "site": "009ab4d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:19c:8"
              ]
            ]
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
      "009ac2f4",
      "READ",
      [
        "storage",
        "002b907e",
        null,
        "string"
      ]
    ],
    [
      "009ac2f8",
      "READ",
      [
        "storage",
        "002b9085",
        null,
        "string"
      ]
    ],
    [
      "009ac474",
      "READ",
      [
        "storage",
        "0029f19c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009ac2f4",
      "READ",
      [
        "storage",
        "002b914d",
        null,
        "string"
      ]
    ],
    [
      "009ac2f8",
      "READ",
      [
        "storage",
        "002b9154",
        null,
        "string"
      ]
    ],
    [
      "009ac474",
      "READ",
      [
        "storage",
        "0029f1dc",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009ab1d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ab/009ab18c.md#insn-009ab1d0) · [`009ab1f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ab/009ab18c.md#insn-009ab1f0) · [`009ab1fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ab/009ab18c.md#insn-009ab1fc)
- 新版 [`009ac17c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ac/009ac138.md#insn-009ac17c) · [`009ac19c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ac/009ac138.md#insn-009ac19c) · [`009ac1a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ac/009ac138.md#insn-009ac1a8)

~~~diff
- 009ab1d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 009ab1d0 ["INT_ADD", "register:40f0:8", ["const:9ab1d0:8", "const:4:8"]]
- 009ab1d0 ["CALLIND", null, ["register:0:8"]]
+ 009ac17c ["COPY", "register:0:8", ["register:4040:8"]]
+ 009ac17c ["INT_ADD", "register:40f0:8", ["const:9ac17c:8", "const:4:8"]]
+ 009ac17c ["CALLIND", null, ["register:0:8"]]
- 009ab1d0 bytes 00013fd6
+ 009ac17c bytes 00013fd6
- 009ab1f0 ["INT_ADD", "register:40f0:8", ["const:9ab1f0:8", "const:4:8"]]
- 009ab1f0 ["CALL", null, ["callee:00c54d60:8"]]
+ 009ac19c ["INT_ADD", "register:40f0:8", ["const:9ac19c:8", "const:4:8"]]
+ 009ac19c ["CALL", null, ["callee:00c54d60:8"]]
- 009ab1f0 bytes e0a20a94
+ 009ac19c bytes f1a20a94
- 009ab1fc ["INT_ADD", "register:40f0:8", ["const:9ab1fc:8", "const:4:8"]]
- 009ab1fc ["CALL", null, ["callee:0059728c:8"]]
+ 009ac1a8 ["INT_ADD", "register:40f0:8", ["const:9ac1a8:8", "const:4:8"]]
+ 009ac1a8 ["CALL", null, ["callee:0059728c:8"]]
- 009ab1fc bytes 5cafef97
+ 009ac1a8 bytes 39acef97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e90d85fa8fa6733c161c06693c93d008"></a>

### [`009ab760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ab/009ab760.md) → [`009ac70c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ac/009ac70c.md) FUN_009ac70c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009ac720",
      "incomplete_value": false,
      "site": "009ac724",
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
            "const:a50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ab774",
      "incomplete_value": false,
      "site": "009ab778",
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
            "const:a80:8"
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
      "009ac724",
      "DATA",
      [
        "storage",
        "00c88a80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009ac724",
      "DATA",
      [
        "storage",
        "00c89a50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009ab76c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ab/009ab760.md#insn-009ab76c) · [`009ab770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ab/009ab760.md#insn-009ab770) · [`009ab774`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ab/009ab760.md#insn-009ab774)
- 新版 [`009ac718`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ac/009ac70c.md#insn-009ac718) · [`009ac71c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ac/009ac70c.md#insn-009ac71c) · [`009ac720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ac/009ac70c.md#insn-009ac720)

~~~diff
- 009ab76c ["INT_ADD", "register:40f0:8", ["const:9ab76c:8", "const:4:8"]]
- 009ab76c ["CALL", null, ["callee:00c58f30:8"]]
+ 009ac718 ["INT_ADD", "register:40f0:8", ["const:9ac718:8", "const:4:8"]]
+ 009ac718 ["CALL", null, ["callee:00c58f30:8"]]
- 009ab76c bytes fdb10a94
+ 009ac718 bytes 06b20a94
- 009ab770 ["COPY", "register:4040:8", ["const:c88000:8"]]
+ 009ac71c ["COPY", "register:4040:8", ["const:c89000:8"]]
- 009ab770 bytes e81600b0
+ 009ac71c bytes e81600b0
- 009ab774 ["COPY", "tmp:0:8", ["const:a80:8"]]
- 009ab774 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009ab774 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009ab774 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009ac720 ["COPY", "tmp:0:8", ["const:a50:8"]]
+ 009ac720 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009ac720 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009ac720 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009ab774 bytes 08012a91
+ 009ac720 bytes 08412991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-514f5478e1113091dafc43bc0a93ff28"></a>

### [`009ab784`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ab/009ab784.md) → [`009ac730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ac/009ac730.md) FUN_009ac730

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009ac734",
      "incomplete_value": false,
      "site": "009ac738",
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
            "const:a50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ab788",
      "incomplete_value": false,
      "site": "009ab78c",
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
            "const:a80:8"
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
      "009ac738",
      "DATA",
      [
        "storage",
        "00c88a80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009ac738",
      "DATA",
      [
        "storage",
        "00c89a50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009ab784`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ab/009ab784.md#insn-009ab784) · [`009ab788`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ab/009ab784.md#insn-009ab788)
- 新版 [`009ac730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ac/009ac730.md#insn-009ac730) · [`009ac734`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ac/009ac730.md#insn-009ac734)

~~~diff
- 009ab784 ["COPY", "register:4040:8", ["const:c88000:8"]]
+ 009ac730 ["COPY", "register:4040:8", ["const:c89000:8"]]
- 009ab784 bytes e81600b0
+ 009ac730 bytes e81600b0
- 009ab788 ["COPY", "tmp:0:8", ["const:a80:8"]]
- 009ab788 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009ab788 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009ab788 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009ac734 ["COPY", "tmp:0:8", ["const:a50:8"]]
+ 009ac734 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009ac734 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009ac734 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009ab788 bytes 08012a91
+ 009ac734 bytes 08412991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3032c007d297ee9881bb10a116b099de"></a>

### [`009ab7cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ab/009ab7cc.md) → [`009ac778`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ac/009ac778.md) FUN_009ac778

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009ac79c",
      "incomplete_value": false,
      "site": "009ac79c",
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
            "const:ad0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ab7f0",
      "incomplete_value": false,
      "site": "009ab7f0",
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
      "009ac79c",
      "DATA",
      [
        "storage",
        "00c88b00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009ac79c",
      "DATA",
      [
        "storage",
        "00c89ad0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009ab7e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ab/009ab7cc.md#insn-009ab7e0) · [`009ab7e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ab/009ab7cc.md#insn-009ab7e8) · [`009ab7ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ab/009ab7cc.md#insn-009ab7ec)
- 新版 [`009ac78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ac/009ac778.md#insn-009ac78c) · [`009ac794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ac/009ac778.md#insn-009ac794) · [`009ac798`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ac/009ac778.md#insn-009ac798)

~~~diff
- 009ab7e0 ["INT_ADD", "register:40f0:8", ["const:9ab7e0:8", "const:4:8"]]
- 009ab7e0 ["CALL", null, ["callee:00c58f30:8"]]
+ 009ac78c ["INT_ADD", "register:40f0:8", ["const:9ac78c:8", "const:4:8"]]
+ 009ac78c ["CALL", null, ["callee:00c58f30:8"]]
- 009ab7e0 bytes e0b10a94
+ 009ac78c bytes e9b10a94
- 009ab7e8 ["COPY", "register:4040:8", ["const:c88000:8"]]
+ 009ac794 ["COPY", "register:4040:8", ["const:c89000:8"]]
- 009ab7e8 bytes e81600b0
+ 009ac794 bytes e81600b0
- 009ab7ec ["COPY", "tmp:0:8", ["const:b00:8"]]
- 009ab7ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009ab7ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009ab7ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009ac798 ["COPY", "tmp:0:8", ["const:ad0:8"]]
+ 009ac798 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009ac798 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009ac798 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009ab7ec bytes 08012c91
+ 009ac798 bytes 08412b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eba0ffe1c79a1a77064927e1f941bca0"></a>

### [`009ab800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ab/009ab800.md) → [`009ac7ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ac/009ac7ac.md) FUN_009ac7ac

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009ac7b8",
      "incomplete_value": false,
      "site": "009ac7b8",
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
            "const:ad0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ab80c",
      "incomplete_value": false,
      "site": "009ab80c",
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
      "009ac7b8",
      "DATA",
      [
        "storage",
        "00c88b00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009ac7b8",
      "DATA",
      [
        "storage",
        "00c89ad0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009ab804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ab/009ab800.md#insn-009ab804) · [`009ab808`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ab/009ab800.md#insn-009ab808)
- 新版 [`009ac7b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ac/009ac7ac.md#insn-009ac7b0) · [`009ac7b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ac/009ac7ac.md#insn-009ac7b4)

~~~diff
- 009ab804 ["COPY", "register:4048:8", ["const:c88000:8"]]
+ 009ac7b0 ["COPY", "register:4048:8", ["const:c89000:8"]]
- 009ab804 bytes e91600b0
+ 009ac7b0 bytes e91600b0
- 009ab808 ["COPY", "tmp:0:8", ["const:b00:8"]]
- 009ab808 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 009ab808 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 009ab808 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 009ac7b4 ["COPY", "tmp:0:8", ["const:ad0:8"]]
+ 009ac7b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 009ac7b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 009ac7b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 009ab808 bytes 29012c91
+ 009ac7b4 bytes 29412b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ac7e81d9ae94da33ec888ffb82ae218"></a>

### [`009ab81c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ab/009ab81c.md) → [`009ac7c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ac/009ac7c8.md) FUN_009ac7c8

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00596f6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596f6c.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 7件 [`004413ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004413ec.md) [`0059728c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00597/0059728c.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.07% / 新版 97.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009ac8f4",
      "incomplete_value": true,
      "site": "009ac8f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:14d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ab948",
      "incomplete_value": true,
      "site": "009ab948",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7e:8"
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
      "definition_site": "009ac8e8",
      "incomplete_value": true,
      "site": "009ac8f8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "009ab93c",
      "incomplete_value": true,
      "site": "009ab94c",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009aca6c",
      "incomplete_value": true,
      "site": "009aca6c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1dc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009abac0",
      "incomplete_value": true,
      "site": "009abac0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:19c:8"
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
      "009ac8e4",
      "READ",
      [
        "storage",
        "002b907e",
        null,
        "string"
      ]
    ],
    [
      "009ac8e8",
      "READ",
      [
        "storage",
        "002b9085",
        null,
        "string"
      ]
    ],
    [
      "009aca5c",
      "READ",
      [
        "storage",
        "0029f19c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009ac8e4",
      "READ",
      [
        "storage",
        "002b914d",
        null,
        "string"
      ]
    ],
    [
      "009ac8e8",
      "READ",
      [
        "storage",
        "002b9154",
        null,
        "string"
      ]
    ],
    [
      "009aca5c",
      "READ",
      [
        "storage",
        "0029f1dc",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009ab85c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ab/009ab81c.md#insn-009ab85c) · [`009ab87c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ab/009ab81c.md#insn-009ab87c) · [`009ab888`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ab/009ab81c.md#insn-009ab888)
- 新版 [`009ac808`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ac/009ac7c8.md#insn-009ac808) · [`009ac828`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ac/009ac7c8.md#insn-009ac828) · [`009ac834`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ac/009ac7c8.md#insn-009ac834)

~~~diff
- 009ab85c ["COPY", "register:0:8", ["register:4048:8"]]
- 009ab85c ["INT_ADD", "register:40f0:8", ["const:9ab85c:8", "const:4:8"]]
- 009ab85c ["CALLIND", null, ["register:0:8"]]
+ 009ac808 ["COPY", "register:0:8", ["register:4048:8"]]
+ 009ac808 ["INT_ADD", "register:40f0:8", ["const:9ac808:8", "const:4:8"]]
+ 009ac808 ["CALLIND", null, ["register:0:8"]]
- 009ab85c bytes 20013fd6
+ 009ac808 bytes 20013fd6
- 009ab87c ["INT_ADD", "register:40f0:8", ["const:9ab87c:8", "const:4:8"]]
- 009ab87c ["CALL", null, ["callee:00c54d60:8"]]
+ 009ac828 ["INT_ADD", "register:40f0:8", ["const:9ac828:8", "const:4:8"]]
+ 009ac828 ["CALL", null, ["callee:00c54d60:8"]]
- 009ab87c bytes 3da10a94
+ 009ac828 bytes 4ea10a94
- 009ab888 ["INT_ADD", "register:40f0:8", ["const:9ab888:8", "const:4:8"]]
- 009ab888 ["CALL", null, ["callee:0059728c:8"]]
+ 009ac834 ["INT_ADD", "register:40f0:8", ["const:9ac834:8", "const:4:8"]]
+ 009ac834 ["CALL", null, ["callee:0059728c:8"]]
- 009ab888 bytes b9adef97
+ 009ac834 bytes 96aaef97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-abdd7dd114d494e59a5a237ff95027c1"></a>

### [`009ac09c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ac/009ac09c.md) → [`009ad048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ad/009ad048.md) FUN_009ad048

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`009abd14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ab/009abd14.md) [`009ac30c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ac/009ac30c.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 2件 [`009accc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ac/009accc0.md) [`009ad2b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ad/009ad2b8.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "009ad054",
      "incomplete_value": false,
      "site": "009ad058",
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
      "definition_site": "009ac0a8",
      "incomplete_value": false,
      "site": "009ac0ac",
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
      "009ad054",
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
      "009ad054",
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

- 旧版 [`009ac0ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ac/009ac09c.md#insn-009ac0ac) · [`009ac0a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ac/009ac09c.md#insn-009ac0a4) · [`009ac0a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ac/009ac09c.md#insn-009ac0a8)
- 新版 [`009ad058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ad/009ad048.md#insn-009ad058) · [`009ad050`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ad/009ad048.md#insn-009ad050) · [`009ad054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ad/009ad048.md#insn-009ad054)

~~~diff
- 009ac0ac ["INT_ADD", "register:40f0:8", ["const:9ac0ac:8", "const:4:8"]]
- 009ac0ac ["CALL", null, ["callee:0043bad8:8"]]
+ 009ad058 ["INT_ADD", "register:40f0:8", ["const:9ad058:8", "const:4:8"]]
+ 009ad058 ["CALL", null, ["callee:0043bad8:8"]]
- 009ac0ac bytes c33dea97
+ 009ad058 bytes a03aea97
- 009ac0a4 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 009ad050 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 009ac0a4 bytes 40c8fff0
+ 009ad050 bytes 40c8fff0
- 009ac0a8 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 009ac0a8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 009ac0a8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 009ac0a8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 009ad054 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 009ad054 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 009ad054 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 009ad054 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 009ac0a8 bytes 00303e91
+ 009ad054 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0de4996e1a01c73a76826d2248fa5a8"></a>

### [`009ac498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ac/009ac498.md) → [`009ad444`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ad/009ad444.md) _INIT_195

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 85.31% / 新版 85.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009ad480",
      "incomplete_value": true,
      "site": "009ad49c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "009ac4d4",
      "incomplete_value": true,
      "site": "009ac4f0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "009ad4c4",
      "incomplete_value": true,
      "site": "009ad4e0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e3d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ac518",
      "incomplete_value": true,
      "site": "009ac534",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009ad4e4",
      "incomplete_value": true,
      "site": "009ad4fc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:fe0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ac538",
      "incomplete_value": true,
      "site": "009ac550",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "009ad480",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "009ad4a4",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "009ad4c4",
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
      "009ad480",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "009ad4a4",
      "READ",
      [
        "storage",
        "002b8048",
        null,
        "string"
      ]
    ],
    [
      "009ad4c4",
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

- 旧版 [`009ac6cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ac/009ac498.md#insn-009ac6cc) · [`009ac4c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ac/009ac498.md#insn-009ac4c0) · [`009ac4c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ac/009ac498.md#insn-009ac4c4)
- 新版 [`009ad678`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ad/009ad444.md#insn-009ad678) · [`009ad46c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ad/009ad444.md#insn-009ad46c) · [`009ad470`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ad/009ad444.md#insn-009ad470)

~~~diff
- 009ac6cc ["INT_ADD", "register:40f0:8", ["const:9ac6cc:8", "const:4:8"]]
- 009ac6cc ["CALL", null, ["callee:00c58ed0:8"]]
+ 009ad678 ["INT_ADD", "register:40f0:8", ["const:9ad678:8", "const:4:8"]]
+ 009ad678 ["CALL", null, ["callee:00c58ed0:8"]]
- 009ac6cc bytes 0dae0a94
+ 009ad678 bytes 16ae0a94
- 009ac4c0 ["COPY", "register:4098:8", ["const:1123000:8"]]
+ 009ad46c ["COPY", "register:4098:8", ["const:1124000:8"]]
- 009ac4c0 bytes b33b00f0
+ 009ad46c bytes b33b00f0
- 009ac4c4 ["COPY", "tmp:0:8", ["const:cd8:8"]]
- 009ac4c4 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 009ac4c4 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 009ac4c4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 009ad470 ["COPY", "tmp:0:8", ["const:c98:8"]]
+ 009ad470 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 009ad470 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 009ad470 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 009ac4c4 bytes 73623391
+ 009ad470 bytes 73623291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d2d09ba87761530e8f9a4ad05dca5ec"></a>

### [`009acc84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ac/009acc84.md) → [`009adc30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ad/009adc30.md) FUN_009adc30

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a8a488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a8a/00a8a488.md) · 呼出先 16件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00869f4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00869/00869f4c.md) [`009a9354`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a9/009a9354.md) [`009a97bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a9/009a97bc.md) [`009ac30c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ac/009ac30c.md)
- 新版 呼出元 1件 [`00a8b47c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a8b/00a8b47c.md) · 呼出先 16件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0086aef8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086a/0086aef8.md) [`009aa300`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009aa/009aa300.md) [`009aa768`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009aa/009aa768.md) [`009ad2b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ad/009ad2b8.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.67% / 新版 98.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009add94",
      "incomplete_value": false,
      "site": "009adda0",
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
            "const:b50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009acde8",
      "incomplete_value": false,
      "site": "009acdf4",
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
            "const:b80:8"
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
      "009adda0",
      "DATA",
      [
        "storage",
        "00c88b80",
        null,
        "pointer"
      ]
    ],
    [
      "009ade10",
      "READ",
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
      "009adda0",
      "DATA",
      [
        "storage",
        "00c89b50",
        null,
        "pointer"
      ]
    ],
    [
      "009ade10",
      "READ",
      [
        "storage",
        "00c89b60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009accfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ac/009acc84.md#insn-009accfc) · [`009acd48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ac/009acc84.md#insn-009acd48) · [`009acd50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ac/009acc84.md#insn-009acd50)
- 新版 [`009adca8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ad/009adc30.md#insn-009adca8) · [`009adcf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ad/009adc30.md#insn-009adcf4) · [`009adcfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ad/009adc30.md#insn-009adcfc)

~~~diff
- 009accfc ["INT_ADD", "register:40f0:8", ["const:9accfc:8", "const:4:8"]]
- 009accfc ["CALL", null, ["callee:0043be80:8"]]
+ 009adca8 ["INT_ADD", "register:40f0:8", ["const:9adca8:8", "const:4:8"]]
+ 009adca8 ["CALL", null, ["callee:0043be80:8"]]
- 009accfc bytes 993bea97
+ 009adca8 bytes 7638ea97
- 009acd48 ["INT_ADD", "register:40f0:8", ["const:9acd48:8", "const:4:8"]]
- 009acd48 ["CALL", null, ["callee:009ad2b8:8"]]
+ 009adcf4 ["INT_ADD", "register:40f0:8", ["const:9adcf4:8", "const:4:8"]]
+ 009adcf4 ["CALL", null, ["callee:009ad2b8:8"]]
- 009acd48 bytes 71fdff97
+ 009adcf4 bytes 71fdff97
- 009acd50 ["INT_ADD", "register:40f0:8", ["const:9acd50:8", "const:4:8"]]
- 009acd50 ["CALL", null, ["callee:009aa768:8"]]
+ 009adcfc ["INT_ADD", "register:40f0:8", ["const:9adcfc:8", "const:4:8"]]
+ 009adcfc ["CALL", null, ["callee:009aa768:8"]]
- 009acd50 bytes 9bf2ff97
+ 009adcfc bytes 9bf2ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7be858d47d9ac7d1a9e9e5cbe22e16d8"></a>

### [`009ad4f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ad/009ad4f8.md) → [`009ae4a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ae/009ae4a4.md) FUN_009ae4a4

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0076453c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/0076453c.md) · 呼出先 11件 [`009b0c30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b0/009b0c30.md) [`009b0c3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b0/009b0c3c.md) [`009b3b54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b3/009b3b54.md) [`009b41a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b4/009b41a8.md) [`009b5c80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b5/009b5c80.md)
- 新版 呼出元 1件 [`00764918`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00764/00764918.md) · 呼出先 11件 [`009b1bdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b1/009b1bdc.md) [`009b1be8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b1/009b1be8.md) [`009b4b00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b4/009b4b00.md) [`009b5154`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b5/009b5154.md) [`009b6c2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b6/009b6c2c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.67% / 新版 98.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009ae5f4",
      "incomplete_value": false,
      "site": "009ae600",
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
            "const:b50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ad648",
      "incomplete_value": false,
      "site": "009ad654",
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
            "const:b80:8"
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009ae600",
      "DATA",
      [
        "storage",
        "00c88b80",
        null,
        "pointer"
      ]
    ],
    [
      "009ae6b8",
      "READ",
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
      "009ae600",
      "DATA",
      [
        "storage",
        "00c89b50",
        null,
        "pointer"
      ]
    ],
    [
      "009ae6b8",
      "READ",
      [
        "storage",
        "00c89b60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009ad56c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ad/009ad4f8.md#insn-009ad56c) · [`009ad574`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ad/009ad4f8.md#insn-009ad574) · [`009ad580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ad/009ad4f8.md#insn-009ad580)
- 新版 [`009ae518`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ae/009ae4a4.md#insn-009ae518) · [`009ae520`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ae/009ae4a4.md#insn-009ae520) · [`009ae52c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ae/009ae4a4.md#insn-009ae52c)

~~~diff
- 009ad56c ["INT_ADD", "register:40f0:8", ["const:9ad56c:8", "const:4:8"]]
- 009ad56c ["CALL", null, ["callee:00c54d60:8"]]
+ 009ae518 ["INT_ADD", "register:40f0:8", ["const:9ae518:8", "const:4:8"]]
+ 009ae518 ["CALL", null, ["callee:00c54d60:8"]]
- 009ad56c bytes 019a0a94
+ 009ae518 bytes 129a0a94
- 009ad574 ["INT_ADD", "register:40f0:8", ["const:9ad574:8", "const:4:8"]]
- 009ad574 ["CALL", null, ["callee:009b5154:8"]]
+ 009ae520 ["INT_ADD", "register:40f0:8", ["const:9ae520:8", "const:4:8"]]
+ 009ae520 ["CALL", null, ["callee:009b5154:8"]]
- 009ad574 bytes 0d1b0094
+ 009ae520 bytes 0d1b0094
- 009ad580 ["INT_ADD", "register:40f0:8", ["const:9ad580:8", "const:4:8"]]
- 009ad580 ["CALL", null, ["callee:00a388bc:8"]]
+ 009ae52c ["INT_ADD", "register:40f0:8", ["const:9ae52c:8", "const:4:8"]]
+ 009ae52c ["CALL", null, ["callee:00a388bc:8"]]
- 009ad580 bytes d2280294
+ 009ae52c bytes e4280294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21a1575b07a41e62a6489565d4507c69"></a>

### [`009ae2c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ae/009ae2c0.md) → [`009af26c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009af/009af26c.md) FUN_009af26c

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`0078bdb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078b/0078bdb0.md) [`009ae2c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ae/009ae2c0.md) [`009b2264`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b2264.md) [`00a91824`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a91/00a91824.md) · 呼出先 15件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`007522d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00752/007522d8.md) [`009ae2c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ae/009ae2c0.md) [`009b21e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b21e4.md) [`009b2608`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b2608.md)
- 新版 呼出元 4件 [`0078c18c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078c/0078c18c.md) [`009af26c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009af/009af26c.md) [`009b3210`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b3210.md) [`00a92818`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a92/00a92818.md) · 呼出先 15件 [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`00752688`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00752/00752688.md) [`009af26c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009af/009af26c.md) [`009b3190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b3190.md) [`009b35b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b35b4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.10% / 新版 99.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009af474",
      "incomplete_value": false,
      "site": "009af480",
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
            "const:ba0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ae4c8",
      "incomplete_value": false,
      "site": "009ae4d4",
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
            "const:bd0:8"
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
      "009af480",
      "DATA",
      [
        "storage",
        "00c88bd0",
        null,
        "undefined *"
      ]
    ],
    [
      "009af544",
      "DATA",
      [
        "storage",
        "00c88c50",
        null,
        "undefined *"
      ]
    ],
    [
      "009af5c4",
      "READ",
      [
        "storage",
        "00c88c78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009af480",
      "DATA",
      [
        "storage",
        "00c89ba0",
        null,
        "undefined *"
      ]
    ],
    [
      "009af544",
      "DATA",
      [
        "storage",
        "00c89c20",
        null,
        "undefined *"
      ]
    ],
    [
      "009af5c4",
      "READ",
      [
        "storage",
        "00c89c48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009ae324`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ae/009ae2c0.md#insn-009ae324) · [`009ae334`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ae/009ae2c0.md#insn-009ae334) · [`009ae348`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ae/009ae2c0.md#insn-009ae348)
- 新版 [`009af2d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009af/009af26c.md#insn-009af2d0) · [`009af2e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009af/009af26c.md#insn-009af2e0) · [`009af2f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009af/009af26c.md#insn-009af2f4)

~~~diff
- 009ae324 ["INT_ADD", "register:40f0:8", ["const:9ae324:8", "const:4:8"]]
- 009ae324 ["CALL", null, ["callee:00c54d60:8"]]
+ 009af2d0 ["INT_ADD", "register:40f0:8", ["const:9af2d0:8", "const:4:8"]]
+ 009af2d0 ["CALL", null, ["callee:00c54d60:8"]]
- 009ae324 bytes 93960a94
+ 009af2d0 bytes a4960a94
- 009ae334 ["INT_ADD", "register:40f0:8", ["const:9ae334:8", "const:4:8"]]
- 009ae334 ["CALL", null, ["callee:009b6ca4:8"]]
+ 009af2e0 ["INT_ADD", "register:40f0:8", ["const:9af2e0:8", "const:4:8"]]
+ 009af2e0 ["CALL", null, ["callee:009b6ca4:8"]]
- 009ae334 bytes 711e0094
+ 009af2e0 bytes 711e0094
- 009ae348 ["INT_ADD", "register:40f0:8", ["const:9ae348:8", "const:4:8"]]
- 009ae348 ["CALL", null, ["callee:009b5154:8"]]
+ 009af2f4 ["INT_ADD", "register:40f0:8", ["const:9af2f4:8", "const:4:8"]]
+ 009af2f4 ["CALL", null, ["callee:009b5154:8"]]
- 009ae348 bytes 98170094
+ 009af2f4 bytes 98170094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be8105102cfabd6d9d551e083bf2c207"></a>

### [`009aedd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ae/009aedd4.md) → [`009afd80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009af/009afd80.md) FUN_009afd80

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) · 呼出先 13件 [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`0062fa98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0062f/0062fa98.md) [`008b98b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b98b0.md) [`008bad20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ba/008bad20.md) [`009b2798`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b2798.md)
- 新版 呼出元 1件 [`0076a1b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0076a/0076a1b8.md) · 呼出先 13件 [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md) [`0062fe48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0062f/0062fe48.md) [`008ba85c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba85c.md) [`008bbccc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008bb/008bbccc.md) [`009b3744`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b3744.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.46% / 新版 93.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009afe08",
      "incomplete_value": true,
      "site": "009afe08",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2bc000:8"
              ],
              [
                "leaf",
                "const:f01:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009aee5c",
      "incomplete_value": true,
      "site": "009aee5c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2bc000:8"
              ],
              [
                "leaf",
                "const:e23:8"
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
      "definition_site": "009afe0c",
      "incomplete_value": true,
      "site": "009afe0c",
      "value": [
        "LOAD",
        "8",
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
                "const:5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009aee60",
      "incomplete_value": true,
      "site": "009aee60",
      "value": [
        "LOAD",
        "8",
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
                "const:5:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009afe68",
      "incomplete_value": false,
      "site": "009afe68",
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
            "const:d20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009aeebc",
      "incomplete_value": false,
      "site": "009aeebc",
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
            "const:d50:8"
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
      "009afdf8",
      "READ",
      [
        "storage",
        "002bce23",
        null,
        "string"
      ]
    ],
    [
      "009afdfc",
      "READ",
      [
        "storage",
        "002bce28",
        null,
        "string"
      ]
    ],
    [
      "009afe68",
      "DATA",
      [
        "storage",
        "00c88d50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009afdf8",
      "READ",
      [
        "storage",
        "002bcf01",
        null,
        "string"
      ]
    ],
    [
      "009afdfc",
      "READ",
      [
        "storage",
        "002bcf06",
        null,
        "string"
      ]
    ],
    [
      "009afe68",
      "DATA",
      [
        "storage",
        "00c89d20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009aee1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ae/009aedd4.md#insn-009aee1c) · [`009aee30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ae/009aedd4.md#insn-009aee30) · [`009aee3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ae/009aedd4.md#insn-009aee3c)
- 新版 [`009afdc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009af/009afd80.md#insn-009afdc8) · [`009afddc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009af/009afd80.md#insn-009afddc) · [`009afde8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009af/009afd80.md#insn-009afde8)

~~~diff
- 009aee1c ["INT_ADD", "register:40f0:8", ["const:9aee1c:8", "const:4:8"]]
- 009aee1c ["CALL", null, ["callee:00c54d60:8"]]
+ 009afdc8 ["INT_ADD", "register:40f0:8", ["const:9afdc8:8", "const:4:8"]]
+ 009afdc8 ["CALL", null, ["callee:00c54d60:8"]]
- 009aee1c bytes d5930a94
+ 009afdc8 bytes e6930a94
- 009aee30 ["INT_ADD", "register:40f0:8", ["const:9aee30:8", "const:4:8"]]
- 009aee30 ["CALL", null, ["callee:009b6d64:8"]]
+ 009afddc ["INT_ADD", "register:40f0:8", ["const:9afddc:8", "const:4:8"]]
+ 009afddc ["CALL", null, ["callee:009b6d64:8"]]
- 009aee30 bytes e21b0094
+ 009afddc bytes e21b0094
- 009aee3c ["INT_ADD", "register:40f0:8", ["const:9aee3c:8", "const:4:8"]]
- 009aee3c ["CALL", null, ["callee:009b6d74:8"]]
+ 009afde8 ["INT_ADD", "register:40f0:8", ["const:9afde8:8", "const:4:8"]]
+ 009afde8 ["CALL", null, ["callee:009b6d74:8"]]
- 009aee3c bytes e31b0094
+ 009afde8 bytes e31b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3eaf47b30c53444a6395646ec0495af"></a>

### [`009af254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009af/009af254.md) → [`009b0200`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b0/009b0200.md) FUN_009b0200

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) · 呼出先 15件 [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`008b01f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b0/008b01f8.md) [`008b98b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b98b0.md) [`008bad20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ba/008bad20.md) [`009b2848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b2848.md)
- 新版 呼出元 1件 [`0076a1b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0076a/0076a1b8.md) · 呼出先 15件 [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md) [`008b11a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b1/008b11a4.md) [`008ba85c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba85c.md) [`008bbccc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008bb/008bbccc.md) [`009b37f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b37f4.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009b0328",
      "incomplete_value": false,
      "site": "009b0328",
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
            "const:da0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009af37c",
      "incomplete_value": false,
      "site": "009af37c",
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
            "const:dd0:8"
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009b028c",
      "READ",
      [
        "storage",
        "002b6905",
        null,
        "string"
      ]
    ],
    [
      "009b028c",
      "READ",
      [
        "storage",
        "002a0770",
        null,
        "string"
      ]
    ],
    [
      "009b0290",
      "READ",
      [
        "storage",
        "002b6915",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009b028c",
      "READ",
      [
        "storage",
        "002b69d4",
        null,
        "string"
      ]
    ],
    [
      "009b028c",
      "READ",
      [
        "storage",
        "002a07b0",
        null,
        "string"
      ]
    ],
    [
      "009b0290",
      "READ",
      [
        "storage",
        "002b69e4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009af2a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009af/009af254.md#insn-009af2a8) · [`009af2bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009af/009af254.md#insn-009af2bc) · [`009af2c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009af/009af254.md#insn-009af2c4)
- 新版 [`009b0254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b0/009b0200.md#insn-009b0254) · [`009b0268`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b0/009b0200.md#insn-009b0268) · [`009b0270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b0/009b0200.md#insn-009b0270)

~~~diff
- 009af2a8 ["INT_ADD", "register:40f0:8", ["const:9af2a8:8", "const:4:8"]]
- 009af2a8 ["CALL", null, ["callee:00c54d60:8"]]
+ 009b0254 ["INT_ADD", "register:40f0:8", ["const:9b0254:8", "const:4:8"]]
+ 009b0254 ["CALL", null, ["callee:00c54d60:8"]]
- 009af2a8 bytes b2920a94
+ 009b0254 bytes c3920a94
- 009af2bc ["INT_ADD", "register:40f0:8", ["const:9af2bc:8", "const:4:8"]]
- 009af2bc ["CALL", null, ["callee:009b6d0c:8"]]
+ 009b0268 ["INT_ADD", "register:40f0:8", ["const:9b0268:8", "const:4:8"]]
+ 009b0268 ["CALL", null, ["callee:009b6d0c:8"]]
- 009af2bc bytes a91a0094
+ 009b0268 bytes a91a0094
- 009af2c4 ["COPY", "tmp:0:8", ["const:905:8"]]
- 009af2c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009af2c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009af2c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009b0270 ["COPY", "tmp:0:8", ["const:9d4:8"]]
+ 009b0270 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009b0270 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009b0270 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009af2c4 bytes 08152491
+ 009b0270 bytes 08512791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-007ce30f8b44b0fa15e87718cea16cd9"></a>

### [`009af9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009af/009af9dc.md) → [`009b0988`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b0/009b0988.md) FUN_009b0988

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) · 呼出先 13件 [`009ac8e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ac/009ac8e4.md) [`009aca78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ac/009aca78.md) [`009afe78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009af/009afe78.md) [`009b0d98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b0/009b0d98.md) [`009b2c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b2c9c.md)
- 新版 呼出元 1件 [`0076a1b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0076a/0076a1b8.md) · 呼出先 13件 [`009ad890`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ad/009ad890.md) [`009ada24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ad/009ada24.md) [`009b0e24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b0/009b0e24.md) [`009b1d44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b1/009b1d44.md) [`009b3c48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b3c48.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.23% / 新版 99.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009b0b20",
      "incomplete_value": false,
      "site": "009b0b20",
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
            "const:e20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009afb74",
      "incomplete_value": false,
      "site": "009afb74",
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
            "const:e50:8"
          ]
        ]
      ]
    },
    "ordinal": 31,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009b0b20",
      "DATA",
      [
        "storage",
        "00c88e50",
        null,
        "undefined *"
      ]
    ],
    [
      "009b0bd4",
      "READ",
      [
        "storage",
        "00c88e78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b0b20",
      "DATA",
      [
        "storage",
        "00c89e20",
        null,
        "undefined *"
      ]
    ],
    [
      "009b0bd4",
      "READ",
      [
        "storage",
        "00c89e48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009afa38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009af/009af9dc.md#insn-009afa38) · [`009afa88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009af/009af9dc.md#insn-009afa88) · [`009afac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009af/009af9dc.md#insn-009afac0)
- 新版 [`009b09e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b0/009b0988.md#insn-009b09e4) · [`009b0a34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b0/009b0988.md#insn-009b0a34) · [`009b0a6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b0/009b0988.md#insn-009b0a6c)

~~~diff
- 009afa38 ["INT_ADD", "register:40f0:8", ["const:9afa38:8", "const:4:8"]]
- 009afa38 ["CALL", null, ["callee:00c58f30:8"]]
+ 009b09e4 ["INT_ADD", "register:40f0:8", ["const:9b09e4:8", "const:4:8"]]
+ 009b09e4 ["CALL", null, ["callee:00c58f30:8"]]
- 009afa38 bytes 4aa10a94
+ 009b09e4 bytes 53a10a94
- 009afa88 ["INT_ADD", "register:40f0:8", ["const:9afa88:8", "const:4:8"]]
- 009afa88 ["CALL", null, ["callee:00c54d60:8"]]
+ 009b0a34 ["INT_ADD", "register:40f0:8", ["const:9b0a34:8", "const:4:8"]]
+ 009b0a34 ["CALL", null, ["callee:00c54d60:8"]]
- 009afa88 bytes ba900a94
+ 009b0a34 bytes cb900a94
- 009afac0 ["INT_ADD", "register:40f0:8", ["const:9afac0:8", "const:4:8"]]
- 009afac0 ["CALL", null, ["callee:00c54d60:8"]]
+ 009b0a6c ["INT_ADD", "register:40f0:8", ["const:9b0a6c:8", "const:4:8"]]
+ 009b0a6c ["CALL", null, ["callee:00c54d60:8"]]
- 009afac0 bytes ac900a94
+ 009b0a6c bytes bd900a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be72188d73be4ca54db10ebbcfd9b8c9"></a>

### [`009afefc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009af/009afefc.md) → [`009b0ea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b0/009b0ea8.md) FUN_009b0ea8

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0089e8d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089e/0089e8d4.md) · 呼出先 18件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`00492d0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492d0c.md) [`007299cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00729/007299cc.md)
- 新版 呼出元 1件 [`0089f880`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0089f/0089f880.md) · 呼出先 18件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0048d058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d058.md) [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md) [`0049302c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/0049302c.md) [`00729d7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00729/00729d7c.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.08% / 新版 96.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009b0f68",
      "incomplete_value": true,
      "site": "009b0f74",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "009affbc",
      "incomplete_value": true,
      "site": "009affc8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:290:8"
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
      "definition_site": "009b1004",
      "incomplete_value": true,
      "site": "009b101c",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:4e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b0058",
      "incomplete_value": true,
      "site": "009b0070",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:490:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009b0f04",
      "value": [
        "leaf",
        "ram:48d058:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009aff58",
      "value": [
        "leaf",
        "ram:48cd38:8"
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
      "009b0f04",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ],
    [
      "009b0f40",
      "READ",
      [
        "storage",
        "002a4915",
        null,
        null
      ]
    ],
    [
      "009b0f40",
      "READ",
      [
        "storage",
        "002a4925",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "009b0f04",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048d058"
      ]
    ],
    [
      "009b0f40",
      "READ",
      [
        "storage",
        "002a49e0",
        null,
        null
      ]
    ],
    [
      "009b0f40",
      "READ",
      [
        "storage",
        "002a49f0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009aff58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009af/009afefc.md#insn-009aff58) · [`009aff38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009af/009afefc.md#insn-009aff38) · [`009aff70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009af/009afefc.md#insn-009aff70)
- 新版 [`009b0f04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b0/009b0ea8.md#insn-009b0f04) · [`009b0ee4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b0/009b0ea8.md#insn-009b0ee4) · [`009b0f1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b0/009b0ea8.md#insn-009b0f1c)

~~~diff
- 009aff58 ["INT_ADD", "register:40f0:8", ["const:9aff58:8", "const:4:8"]]
- 009aff58 ["CALL", null, ["ram:48cd38:8"]]
+ 009b0f04 ["INT_ADD", "register:40f0:8", ["const:9b0f04:8", "const:4:8"]]
+ 009b0f04 ["CALL", null, ["ram:48d058:8"]]
- 009aff58 bytes 7873eb97
+ 009b0f04 bytes 5570eb97
- 009aff38 ["INT_ADD", "register:40f0:8", ["const:9aff38:8", "const:4:8"]]
- 009aff38 ["CALL", null, ["callee:009ae980:8"]]
+ 009b0ee4 ["INT_ADD", "register:40f0:8", ["const:9b0ee4:8", "const:4:8"]]
+ 009b0ee4 ["CALL", null, ["callee:009ae980:8"]]
- 009aff38 bytes a7f6ff97
+ 009b0ee4 bytes a7f6ff97
- 009aff70 ["INT_ADD", "register:40f0:8", ["const:9aff70:8", "const:4:8"]]
- 009aff70 ["CALL", null, ["callee:009abda8:8"]]
+ 009b0f1c ["INT_ADD", "register:40f0:8", ["const:9b0f1c:8", "const:4:8"]]
+ 009b0f1c ["CALL", null, ["callee:009abda8:8"]]
- 009aff70 bytes a3ebff97
+ 009b0f1c bytes a3ebff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fbabc824b5e3a759e389aecbd8e00e72"></a>

### [`009b0558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b0/009b0558.md) → [`009b1504`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b1/009b1504.md) FUN_009b1504

採用 · 移動量 `+0xfac` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009afefc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009af/009afefc.md) · 呼出先 22件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`004741d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00474/004741d8.md) [`0048c040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048c040.md) [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md)
- 新版 呼出元 1件 [`009b0ea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b0/009b0ea8.md) · 呼出先 22件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`004744f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00474/004744f8.md) [`0048c360`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048c/0048c360.md) [`0048d058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d058.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.76% / 新版 95.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009b16dc",
      "incomplete_value": true,
      "site": "009b16f0",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:d40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b0730",
      "incomplete_value": true,
      "site": "009b0744",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:cf0:8"
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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009b16d8",
      "incomplete_value": true,
      "site": "009b16f8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a63:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b072c",
      "incomplete_value": true,
      "site": "009b074c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:985:8"
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
      "definition_site": "009b16d8",
      "incomplete_value": true,
      "site": "009b16f8",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "009b072c",
      "incomplete_value": true,
      "site": "009b074c",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 31,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009b15c4",
      "DATA",
      [
        "storage",
        "003965a4",
        null,
        "qword"
      ]
    ],
    [
      "009b16d8",
      "READ",
      [
        "storage",
        "002ba985",
        null,
        "string"
      ]
    ],
    [
      "009b16d8",
      "READ",
      [
        "storage",
        "002ba995",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009b15c4",
      "DATA",
      [
        "storage",
        "003965a4",
        "fde_003965a4",
        "dword"
      ]
    ],
    [
      "009b16d8",
      "READ",
      [
        "storage",
        "002baa63",
        null,
        "string"
      ]
    ],
    [
      "009b16d8",
      "READ",
      [
        "storage",
        "002baa73",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b09f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b0/009b0558.md#insn-009b09f8) · [`009b05a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b0/009b0558.md#insn-009b05a4) · [`009b060c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b0/009b0558.md#insn-009b060c)
- 新版 [`009b19a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b1/009b1504.md#insn-009b19a4) · [`009b1550`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b1/009b1504.md#insn-009b1550) · [`009b15b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b1/009b1504.md#insn-009b15b8)

~~~diff
- 009b09f8 ["INT_ADD", "register:40f0:8", ["const:9b09f8:8", "const:4:8"]]
- 009b09f8 ["CALL", null, ["ram:48cd38:8"]]
+ 009b19a4 ["INT_ADD", "register:40f0:8", ["const:9b19a4:8", "const:4:8"]]
+ 009b19a4 ["CALL", null, ["ram:48d058:8"]]
- 009b09f8 bytes d070eb97
+ 009b19a4 bytes ad6deb97
- 009b05a4 ["INT_ADD", "register:40f0:8", ["const:9b05a4:8", "const:4:8"]]
- 009b05a4 ["CALL", null, ["callee:009abdd0:8"]]
+ 009b1550 ["INT_ADD", "register:40f0:8", ["const:9b1550:8", "const:4:8"]]
+ 009b1550 ["CALL", null, ["callee:009abdd0:8"]]
- 009b05a4 bytes 20eaff97
+ 009b1550 bytes 20eaff97
- 009b060c ["INT_ADD", "register:40f0:8", ["const:9b060c:8", "const:4:8"]]
- 009b060c ["CALL", null, ["callee:008524fc:8"]]
+ 009b15b8 ["INT_ADD", "register:40f0:8", ["const:9b15b8:8", "const:4:8"]]
+ 009b15b8 ["CALL", null, ["callee:008524fc:8"]]
- 009b060c bytes d183fa97
+ 009b15b8 bytes d183fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4088d05cf2041b2e797d288b34b51f9e"></a>

### [`009b0bf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b0/009b0bf0.md) → [`009b1b9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b1/009b1b9c.md) FUN_009b1b9c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f40.md)

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
      "definition_site": "009b1ba0",
      "incomplete_value": false,
      "site": "009b1ba4",
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
            "const:b50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b0bf4",
      "incomplete_value": false,
      "site": "009b0bf8",
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
            "const:b80:8"
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
      "009b1ba4",
      "DATA",
      [
        "storage",
        "00c88b80",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "009b1ba4",
      "DATA",
      [
        "storage",
        "00c89b50",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b0bf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b0/009b0bf0.md#insn-009b0bf0) · [`009b0bf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b0/009b0bf0.md#insn-009b0bf4)
- 新版 [`009b1b9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b1/009b1b9c.md#insn-009b1b9c) · [`009b1ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b1/009b1b9c.md#insn-009b1ba0)

~~~diff
- 009b0bf0 ["COPY", "register:4040:8", ["const:c88000:8"]]
+ 009b1b9c ["COPY", "register:4040:8", ["const:c89000:8"]]
- 009b0bf0 bytes c8160090
+ 009b1b9c bytes c8160090
- 009b0bf4 ["COPY", "tmp:0:8", ["const:b80:8"]]
- 009b0bf4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009b0bf4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009b0bf4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009b1ba0 ["COPY", "tmp:0:8", ["const:b50:8"]]
+ 009b1ba0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009b1ba0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009b1ba0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009b0bf4 bytes 08012e91
+ 009b1ba0 bytes 08412d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4273b1c6e17c9939780bcd86ab7dc8d3"></a>

### [`009b0c00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b0/009b0c00.md) → [`009b1bac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b1/009b1bac.md) FUN_009b1bac

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f40.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

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
      "definition_site": "009b1bbc",
      "incomplete_value": false,
      "site": "009b1bc4",
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
            "const:b50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b0c10",
      "incomplete_value": false,
      "site": "009b0c18",
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
            "const:b80:8"
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
      "009b1bc4",
      "DATA",
      [
        "storage",
        "00c88b80",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "009b1bc4",
      "DATA",
      [
        "storage",
        "00c89b50",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b0c0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b0/009b0c00.md#insn-009b0c0c) · [`009b0c10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b0/009b0c00.md#insn-009b0c10) · [`009b0c1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b0/009b0c00.md#insn-009b0c1c)
- 新版 [`009b1bb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b1/009b1bac.md#insn-009b1bb8) · [`009b1bbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b1/009b1bac.md#insn-009b1bbc) · [`009b1bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b1/009b1bac.md#insn-009b1bc8)

~~~diff
- 009b0c0c ["COPY", "register:4040:8", ["const:c88000:8"]]
+ 009b1bb8 ["COPY", "register:4040:8", ["const:c89000:8"]]
- 009b0c0c bytes c8160090
+ 009b1bb8 bytes c8160090
- 009b0c10 ["COPY", "tmp:0:8", ["const:b80:8"]]
- 009b0c10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009b0c10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009b0c10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009b1bbc ["COPY", "tmp:0:8", ["const:b50:8"]]
+ 009b1bbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009b1bbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009b1bbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009b0c10 bytes 08012e91
+ 009b1bbc bytes 08412d91
- 009b0c1c ["INT_ADD", "register:40f0:8", ["const:9b0c1c:8", "const:4:8"]]
- 009b0c1c ["CALL", null, ["callee:00c58f40:8"]]
+ 009b1bc8 ["INT_ADD", "register:40f0:8", ["const:9b1bc8:8", "const:4:8"]]
+ 009b1bc8 ["CALL", null, ["callee:00c58f40:8"]]
- 009b0c1c bytes d59c0a94
+ 009b1bc8 bytes de9c0a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb5e922db9900f327a5557b839ddec99"></a>

### [`009b0d98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b0/009b0d98.md) → [`009b1d44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b1/009b1d44.md) FUN_009b1d44

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`009acfbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ac/009acfbc.md) [`009af9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009af/009af9dc.md) [`009b0c3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b0/009b0c3c.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 3件 [`009adf68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ad/009adf68.md) [`009b0988`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b0/009b0988.md) [`009b1be8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b1/009b1be8.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

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
      "definition_site": "009b1d50",
      "incomplete_value": false,
      "site": "009b1d54",
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
      "definition_site": "009b0da4",
      "incomplete_value": false,
      "site": "009b0da8",
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
      "009b1d50",
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
      "009b1d50",
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

- 旧版 [`009b0da8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b0/009b0d98.md#insn-009b0da8) · [`009b0da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b0/009b0d98.md#insn-009b0da0) · [`009b0da4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b0/009b0d98.md#insn-009b0da4)
- 新版 [`009b1d54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b1/009b1d44.md#insn-009b1d54) · [`009b1d4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b1/009b1d44.md#insn-009b1d4c) · [`009b1d50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b1/009b1d44.md#insn-009b1d50)

~~~diff
- 009b0da8 ["INT_ADD", "register:40f0:8", ["const:9b0da8:8", "const:4:8"]]
- 009b0da8 ["CALL", null, ["callee:0043bad8:8"]]
+ 009b1d54 ["INT_ADD", "register:40f0:8", ["const:9b1d54:8", "const:4:8"]]
+ 009b1d54 ["CALL", null, ["callee:0043bad8:8"]]
- 009b0da8 bytes 842aea97
+ 009b1d54 bytes 6127ea97
- 009b0da0 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 009b1d4c ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 009b0da0 bytes 20c8fff0
+ 009b1d4c bytes 20c8fff0
- 009b0da4 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 009b0da4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 009b0da4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 009b0da4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 009b1d50 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 009b1d50 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 009b1d50 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 009b1d50 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 009b0da4 bytes 00303e91
+ 009b1d50 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-906fd147d42b06a0b0cf7744bd9fc3b9"></a>

### [`009b1f88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b1/009b1f88.md) → [`009b2f34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b2/009b2f34.md) FUN_009b2f34

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.29% / 新版 94.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009b2f4c",
      "incomplete_value": false,
      "site": "009b2f50",
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
            "const:ba0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b1fa0",
      "incomplete_value": false,
      "site": "009b1fa4",
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
            "const:bd0:8"
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
      "009b2f50",
      "DATA",
      [
        "storage",
        "00c88bd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b2f50",
      "DATA",
      [
        "storage",
        "00c89ba0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b1f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b1/009b1f88.md#insn-009b1f9c) · [`009b1fa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b1/009b1f88.md#insn-009b1fa0) · [`009b1fb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b1/009b1f88.md#insn-009b1fb4)
- 新版 [`009b2f48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b2/009b2f34.md#insn-009b2f48) · [`009b2f4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b2/009b2f34.md#insn-009b2f4c) · [`009b2f60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b2/009b2f34.md#insn-009b2f60)

~~~diff
- 009b1f9c ["COPY", "register:4040:8", ["const:c88000:8"]]
+ 009b2f48 ["COPY", "register:4040:8", ["const:c89000:8"]]
- 009b1f9c bytes a81600f0
+ 009b2f48 bytes a81600f0
- 009b1fa0 ["COPY", "tmp:0:8", ["const:bd0:8"]]
- 009b1fa0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009b1fa0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009b1fa0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009b2f4c ["COPY", "tmp:0:8", ["const:ba0:8"]]
+ 009b2f4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009b2f4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009b2f4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009b1fa0 bytes 08412f91
+ 009b2f4c bytes 08812e91
- 009b1fb4 ["INT_ADD", "register:40f0:8", ["const:9b1fb4:8", "const:4:8"]]
- 009b1fb4 ["CALL", null, ["callee:00c54d90:8"]]
+ 009b2f60 ["INT_ADD", "register:40f0:8", ["const:9b2f60:8", "const:4:8"]]
+ 009b2f60 ["CALL", null, ["callee:00c54d90:8"]]
- 009b1fb4 bytes 7b870a94
+ 009b2f60 bytes 8c870a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b82ddf42ab523fa1b03151381392a730"></a>

### [`009b2014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b2014.md) → [`009b2fc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b2/009b2fc0.md) FUN_009b2fc0

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009b2fdc",
      "incomplete_value": false,
      "site": "009b2fec",
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
            "const:ba0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b2030",
      "incomplete_value": false,
      "site": "009b2040",
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
            "const:bd0:8"
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
      "009b2fec",
      "DATA",
      [
        "storage",
        "00c88bd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b2fec",
      "DATA",
      [
        "storage",
        "00c89ba0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b2028`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b2014.md#insn-009b2028) · [`009b202c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b2014.md#insn-009b202c) · [`009b2030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b2014.md#insn-009b2030)
- 新版 [`009b2fd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b2/009b2fc0.md#insn-009b2fd4) · [`009b2fd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b2/009b2fc0.md#insn-009b2fd8) · [`009b2fdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b2/009b2fc0.md#insn-009b2fdc)

~~~diff
- 009b2028 ["INT_ADD", "register:40f0:8", ["const:9b2028:8", "const:4:8"]]
- 009b2028 ["CALL", null, ["callee:00c58f30:8"]]
+ 009b2fd4 ["INT_ADD", "register:40f0:8", ["const:9b2fd4:8", "const:4:8"]]
+ 009b2fd4 ["CALL", null, ["callee:00c58f30:8"]]
- 009b2028 bytes ce970a94
+ 009b2fd4 bytes d7970a94
- 009b202c ["COPY", "register:4040:8", ["const:c88000:8"]]
+ 009b2fd8 ["COPY", "register:4040:8", ["const:c89000:8"]]
- 009b202c bytes a81600d0
+ 009b2fd8 bytes a81600f0
- 009b2030 ["COPY", "tmp:0:8", ["const:bd0:8"]]
- 009b2030 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009b2030 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009b2030 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009b2fdc ["COPY", "tmp:0:8", ["const:ba0:8"]]
+ 009b2fdc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009b2fdc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009b2fdc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009b2030 bytes 08412f91
+ 009b2fdc bytes 08812e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60e2412f510ba5a75b3e18e3a87e1f2c"></a>

### [`009b20c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b20c4.md) → [`009b3070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b3070.md) FUN_009b3070

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009b3080",
      "incomplete_value": false,
      "site": "009b3088",
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
            "const:ba0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b20d4",
      "incomplete_value": false,
      "site": "009b20dc",
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
            "const:bd0:8"
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
      "009b3088",
      "DATA",
      [
        "storage",
        "00c88bd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b3088",
      "DATA",
      [
        "storage",
        "00c89ba0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b20d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b20c4.md#insn-009b20d0) · [`009b20d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b20c4.md#insn-009b20d4) · [`009b2110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b20c4.md#insn-009b2110)
- 新版 [`009b307c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b3070.md#insn-009b307c) · [`009b3080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b3070.md#insn-009b3080) · [`009b30bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b3070.md#insn-009b30bc)

~~~diff
- 009b20d0 ["COPY", "register:4040:8", ["const:c88000:8"]]
+ 009b307c ["COPY", "register:4040:8", ["const:c89000:8"]]
- 009b20d0 bytes a81600d0
+ 009b307c bytes a81600d0
- 009b20d4 ["COPY", "tmp:0:8", ["const:bd0:8"]]
- 009b20d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009b20d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009b20d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009b3080 ["COPY", "tmp:0:8", ["const:ba0:8"]]
+ 009b3080 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009b3080 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009b3080 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009b20d4 bytes 08412f91
+ 009b3080 bytes 08812e91
- 009b2110 ["COPY", "register:0:8", ["register:4040:8"]]
- 009b2110 ["INT_ADD", "register:40f0:8", ["const:9b2110:8", "const:4:8"]]
- 009b2110 ["CALLIND", null, ["register:0:8"]]
+ 009b30bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 009b30bc ["INT_ADD", "register:40f0:8", ["const:9b30bc:8", "const:4:8"]]
+ 009b30bc ["CALLIND", null, ["register:0:8"]]
- 009b2110 bytes 00013fd6
+ 009b30bc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4be8bdf177280e40e1f3667cf42069e7"></a>

### [`009b2434`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b2434.md) → [`009b33e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b33e0.md) FUN_009b33e0

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "009b33ec",
      "incomplete_value": false,
      "site": "009b33f8",
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
            "const:c20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b2440",
      "incomplete_value": false,
      "site": "009b244c",
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
            "const:c50:8"
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
      "009b33f8",
      "DATA",
      [
        "storage",
        "00c88c50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b33f8",
      "DATA",
      [
        "storage",
        "00c89c20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b243c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b2434.md#insn-009b243c) · [`009b2440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b2434.md#insn-009b2440)
- 新版 [`009b33e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b33e0.md#insn-009b33e8) · [`009b33ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b33e0.md#insn-009b33ec)

~~~diff
- 009b243c ["COPY", "register:4050:8", ["const:c88000:8"]]
+ 009b33e8 ["COPY", "register:4050:8", ["const:c89000:8"]]
- 009b243c bytes aa1600d0
+ 009b33e8 bytes aa1600d0
- 009b2440 ["COPY", "tmp:0:8", ["const:c50:8"]]
- 009b2440 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 009b2440 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 009b2440 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 009b33ec ["COPY", "tmp:0:8", ["const:c20:8"]]
+ 009b33ec ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 009b33ec ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 009b33ec ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 009b2440 bytes 4a413191
+ 009b33ec bytes 4a813091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e50e70e11c9b5982fbccafbb2ac467a"></a>

### [`009b2478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b2478.md) → [`009b3424`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b3424.md) FUN_009b3424

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "009b343c",
      "incomplete_value": false,
      "site": "009b3448",
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
            "const:c20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b2490",
      "incomplete_value": false,
      "site": "009b249c",
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
            "const:c50:8"
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
      "009b3448",
      "DATA",
      [
        "storage",
        "00c88c50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b3448",
      "DATA",
      [
        "storage",
        "00c89c20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b248c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b2478.md#insn-009b248c) · [`009b2490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b2478.md#insn-009b2490) · [`009b24c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b2478.md#insn-009b24c0)
- 新版 [`009b3438`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b3424.md#insn-009b3438) · [`009b343c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b3424.md#insn-009b343c) · [`009b346c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b3424.md#insn-009b346c)

~~~diff
- 009b248c ["COPY", "register:4040:8", ["const:c88000:8"]]
+ 009b3438 ["COPY", "register:4040:8", ["const:c89000:8"]]
- 009b248c bytes a81600d0
+ 009b3438 bytes a81600d0
- 009b2490 ["COPY", "tmp:0:8", ["const:c50:8"]]
- 009b2490 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009b2490 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009b2490 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009b343c ["COPY", "tmp:0:8", ["const:c20:8"]]
+ 009b343c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009b343c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009b343c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009b2490 bytes 08413191
+ 009b343c bytes 08813091
- 009b24c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 009b24c0 ["INT_ADD", "register:40f0:8", ["const:9b24c0:8", "const:4:8"]]
- 009b24c0 ["CALLIND", null, ["register:0:8"]]
+ 009b346c ["COPY", "register:0:8", ["register:4040:8"]]
+ 009b346c ["INT_ADD", "register:40f0:8", ["const:9b346c:8", "const:4:8"]]
+ 009b346c ["CALLIND", null, ["register:0:8"]]
- 009b24c0 bytes 00013fd6
+ 009b346c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10de056c1a513329cd7b4adbea4b2b81"></a>

### [`009b24d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b24d4.md) → [`009b3480`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b3480.md) FUN_009b3480

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "009b34ac",
      "incomplete_value": false,
      "site": "009b34ac",
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
            "const:c20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b2500",
      "incomplete_value": false,
      "site": "009b2500",
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
            "const:c50:8"
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
      "009b34ac",
      "DATA",
      [
        "storage",
        "00c88c50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b34ac",
      "DATA",
      [
        "storage",
        "00c89c20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b24e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b24d4.md#insn-009b24e8) · [`009b24f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b24d4.md#insn-009b24f4) · [`009b24f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b24d4.md#insn-009b24f8)
- 新版 [`009b3494`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b3480.md#insn-009b3494) · [`009b34a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b3480.md#insn-009b34a0) · [`009b34a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b3480.md#insn-009b34a4)

~~~diff
- 009b24e8 ["INT_ADD", "register:40f0:8", ["const:9b24e8:8", "const:4:8"]]
- 009b24e8 ["CALL", null, ["callee:00c58f30:8"]]
+ 009b3494 ["INT_ADD", "register:40f0:8", ["const:9b3494:8", "const:4:8"]]
+ 009b3494 ["CALL", null, ["callee:00c58f30:8"]]
- 009b24e8 bytes 9e960a94
+ 009b3494 bytes a7960a94
- 009b24f4 ["COPY", "register:4040:8", ["const:c88000:8"]]
+ 009b34a0 ["COPY", "register:4040:8", ["const:c89000:8"]]
- 009b24f4 bytes a81600d0
+ 009b34a0 bytes a81600d0
- 009b24f8 ["COPY", "tmp:0:8", ["const:c50:8"]]
- 009b24f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009b24f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009b24f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009b34a4 ["COPY", "tmp:0:8", ["const:c20:8"]]
+ 009b34a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009b34a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009b34a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009b24f8 bytes 08413191
+ 009b34a4 bytes 08813091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d23abbb1bae496363b479b0a7c6025ad"></a>

### [`009b255c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b255c.md) → [`009b3508`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b3508.md) FUN_009b3508

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009b3524",
      "incomplete_value": true,
      "site": "009b3524",
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
            "const:c20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b2578",
      "incomplete_value": true,
      "site": "009b2578",
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
            "const:c50:8"
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
      "009b3524",
      "DATA",
      [
        "storage",
        "00c88c50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b3524",
      "DATA",
      [
        "storage",
        "00c89c20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b2570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b255c.md#insn-009b2570) · [`009b2574`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b255c.md#insn-009b2574) · [`009b2598`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b255c.md#insn-009b2598)
- 新版 [`009b351c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b3508.md#insn-009b351c) · [`009b3520`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b3508.md#insn-009b3520) · [`009b3544`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b3508.md#insn-009b3544)

~~~diff
- 009b2570 ["COPY", "register:4048:8", ["const:c88000:8"]]
+ 009b351c ["COPY", "register:4048:8", ["const:c89000:8"]]
- 009b2570 bytes a91600d0
+ 009b351c bytes a91600d0
- 009b2574 ["COPY", "tmp:0:8", ["const:c50:8"]]
- 009b2574 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 009b2574 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 009b2574 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 009b3520 ["COPY", "tmp:0:8", ["const:c20:8"]]
+ 009b3520 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 009b3520 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 009b3520 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 009b2574 bytes 29413191
+ 009b3520 bytes 29813091
- 009b2598 ["COPY", "register:0:8", ["register:4048:8"]]
- 009b2598 ["INT_ADD", "register:40f0:8", ["const:9b2598:8", "const:4:8"]]
- 009b2598 ["CALLIND", null, ["register:0:8"]]
+ 009b3544 ["COPY", "register:0:8", ["register:4048:8"]]
+ 009b3544 ["INT_ADD", "register:40f0:8", ["const:9b3544:8", "const:4:8"]]
+ 009b3544 ["CALLIND", null, ["register:0:8"]]
- 009b2598 bytes 20013fd6
+ 009b3544 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ffdc0333a418efa3dd9b6782d8de5895"></a>

### [`009b26f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b26f8.md) → [`009b36a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b36a4.md) FUN_009b36a4

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009b36b8",
      "incomplete_value": false,
      "site": "009b36bc",
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
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b270c",
      "incomplete_value": false,
      "site": "009b2710",
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
            "const:cd0:8"
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
      "009b36bc",
      "DATA",
      [
        "storage",
        "00c88cd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b36bc",
      "DATA",
      [
        "storage",
        "00c89ca0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b2704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b26f8.md#insn-009b2704) · [`009b2708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b26f8.md#insn-009b2708) · [`009b270c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b26f8.md#insn-009b270c)
- 新版 [`009b36b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b36a4.md#insn-009b36b0) · [`009b36b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b36a4.md#insn-009b36b4) · [`009b36b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b36a4.md#insn-009b36b8)

~~~diff
- 009b2704 ["INT_ADD", "register:40f0:8", ["const:9b2704:8", "const:4:8"]]
- 009b2704 ["CALL", null, ["callee:00c58f30:8"]]
+ 009b36b0 ["INT_ADD", "register:40f0:8", ["const:9b36b0:8", "const:4:8"]]
+ 009b36b0 ["CALL", null, ["callee:00c58f30:8"]]
- 009b2704 bytes 17960a94
+ 009b36b0 bytes 20960a94
- 009b2708 ["COPY", "register:4040:8", ["const:c88000:8"]]
+ 009b36b4 ["COPY", "register:4040:8", ["const:c89000:8"]]
- 009b2708 bytes a81600d0
+ 009b36b4 bytes a81600d0
- 009b270c ["COPY", "tmp:0:8", ["const:cd0:8"]]
- 009b270c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009b270c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009b270c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009b36b8 ["COPY", "tmp:0:8", ["const:ca0:8"]]
+ 009b36b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009b36b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009b36b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009b270c bytes 08413391
+ 009b36b8 bytes 08813291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b09450f8009ef0d834d45639e4779d1"></a>

### [`009b271c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b271c.md) → [`009b36c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b36c8.md) FUN_009b36c8

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009b36cc",
      "incomplete_value": false,
      "site": "009b36d0",
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
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b2720",
      "incomplete_value": false,
      "site": "009b2724",
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
            "const:cd0:8"
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
      "009b36d0",
      "DATA",
      [
        "storage",
        "00c88cd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b36d0",
      "DATA",
      [
        "storage",
        "00c89ca0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b271c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b271c.md#insn-009b271c) · [`009b2720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b271c.md#insn-009b2720)
- 新版 [`009b36c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b36c8.md#insn-009b36c8) · [`009b36cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b36c8.md#insn-009b36cc)

~~~diff
- 009b271c ["COPY", "register:4040:8", ["const:c88000:8"]]
+ 009b36c8 ["COPY", "register:4040:8", ["const:c89000:8"]]
- 009b271c bytes a81600d0
+ 009b36c8 bytes a81600d0
- 009b2720 ["COPY", "tmp:0:8", ["const:cd0:8"]]
- 009b2720 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009b2720 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009b2720 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009b36cc ["COPY", "tmp:0:8", ["const:ca0:8"]]
+ 009b36cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009b36cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009b36cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009b2720 bytes 08413391
+ 009b36cc bytes 08813291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e4676e7199d9dcc61d0b76ba12c1bf8"></a>

### [`009b2764`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b2764.md) → [`009b3710`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b3710.md) FUN_009b3710

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009b3724",
      "incomplete_value": false,
      "site": "009b3728",
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
            "const:d20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b2778",
      "incomplete_value": false,
      "site": "009b277c",
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
            "const:d50:8"
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
      "009b3728",
      "DATA",
      [
        "storage",
        "00c88d50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b3728",
      "DATA",
      [
        "storage",
        "00c89d20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b2770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b2764.md#insn-009b2770) · [`009b2774`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b2764.md#insn-009b2774) · [`009b2778`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b2764.md#insn-009b2778)
- 新版 [`009b371c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b3710.md#insn-009b371c) · [`009b3720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b3710.md#insn-009b3720) · [`009b3724`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b3710.md#insn-009b3724)

~~~diff
- 009b2770 ["INT_ADD", "register:40f0:8", ["const:9b2770:8", "const:4:8"]]
- 009b2770 ["CALL", null, ["callee:00c58f30:8"]]
+ 009b371c ["INT_ADD", "register:40f0:8", ["const:9b371c:8", "const:4:8"]]
+ 009b371c ["CALL", null, ["callee:00c58f30:8"]]
- 009b2770 bytes fc950a94
+ 009b371c bytes 05960a94
- 009b2774 ["COPY", "register:4040:8", ["const:c88000:8"]]
+ 009b3720 ["COPY", "register:4040:8", ["const:c89000:8"]]
- 009b2774 bytes a81600d0
+ 009b3720 bytes a81600d0
- 009b2778 ["COPY", "tmp:0:8", ["const:d50:8"]]
- 009b2778 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009b2778 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009b2778 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009b3724 ["COPY", "tmp:0:8", ["const:d20:8"]]
+ 009b3724 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009b3724 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009b3724 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009b2778 bytes 08413591
+ 009b3724 bytes 08813491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de5051063b8c1fd82d64f0c4e8392a72"></a>

### [`009b2788`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b2788.md) → [`009b3734`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b3734.md) FUN_009b3734

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009b3738",
      "incomplete_value": false,
      "site": "009b373c",
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
            "const:d20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b278c",
      "incomplete_value": false,
      "site": "009b2790",
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
            "const:d50:8"
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
      "009b373c",
      "DATA",
      [
        "storage",
        "00c88d50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b373c",
      "DATA",
      [
        "storage",
        "00c89d20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b2788`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b2788.md#insn-009b2788) · [`009b278c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b2788.md#insn-009b278c)
- 新版 [`009b3734`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b3734.md#insn-009b3734) · [`009b3738`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b3734.md#insn-009b3738)

~~~diff
- 009b2788 ["COPY", "register:4040:8", ["const:c88000:8"]]
+ 009b3734 ["COPY", "register:4040:8", ["const:c89000:8"]]
- 009b2788 bytes a81600d0
+ 009b3734 bytes a81600d0
- 009b278c ["COPY", "tmp:0:8", ["const:d50:8"]]
- 009b278c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009b278c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009b278c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009b3738 ["COPY", "tmp:0:8", ["const:d20:8"]]
+ 009b3738 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009b3738 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009b3738 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009b278c bytes 08413591
+ 009b3738 bytes 08813491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1314c2e0ebc1f63aa59a980237962249"></a>

### [`009b27a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b27a0.md) → [`009b374c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b374c.md) FUN_009b374c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008ba17c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba17c.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.44% / 新版 94.44%

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
      "site": "009b3770",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009b27c4",
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
      "009b3770",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "009b3770",
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

- 旧版 [`009b27c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b27a0.md#insn-009b27c4) · [`009b27d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b27a0.md#insn-009b27d0)
- 新版 [`009b3770`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b374c.md#insn-009b3770) · [`009b377c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b374c.md#insn-009b377c)

~~~diff
- 009b27c4 ["INT_ADD", "register:40f0:8", ["const:9b27c4:8", "const:4:8"]]
- 009b27c4 ["CALL", null, ["ram:47ad34:8"]]
+ 009b3770 ["INT_ADD", "register:40f0:8", ["const:9b3770:8", "const:4:8"]]
+ 009b3770 ["CALL", null, ["ram:47b054:8"]]
- 009b27c4 bytes 5c21eb97
+ 009b3770 bytes 391eeb97
- 009b27d0 ["INT_ADD", "register:40f0:8", ["const:9b27d0:8", "const:4:8"]]
- 009b27d0 ["CALL", null, ["callee:0047d134:8"]]
+ 009b377c ["INT_ADD", "register:40f0:8", ["const:9b377c:8", "const:4:8"]]
+ 009b377c ["CALL", null, ["callee:0047d134:8"]]
- 009b27d0 bytes 9129eb97
+ 009b377c bytes 6e26eb97
~~~


<a id="compare-2db8393143257960cb84b39171565926"></a>

### [`009b2814`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b2814.md) → [`009b37c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b37c0.md) FUN_009b37c0

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009b37d4",
      "incomplete_value": false,
      "site": "009b37d8",
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
            "const:da0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b2828",
      "incomplete_value": false,
      "site": "009b282c",
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
            "const:dd0:8"
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
      "009b37d8",
      "DATA",
      [
        "storage",
        "00c88dd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b37d8",
      "DATA",
      [
        "storage",
        "00c89da0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b2820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b2814.md#insn-009b2820) · [`009b2824`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b2814.md#insn-009b2824) · [`009b2828`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b2814.md#insn-009b2828)
- 新版 [`009b37cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b37c0.md#insn-009b37cc) · [`009b37d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b37c0.md#insn-009b37d0) · [`009b37d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b37c0.md#insn-009b37d4)

~~~diff
- 009b2820 ["INT_ADD", "register:40f0:8", ["const:9b2820:8", "const:4:8"]]
- 009b2820 ["CALL", null, ["callee:00c58f30:8"]]
+ 009b37cc ["INT_ADD", "register:40f0:8", ["const:9b37cc:8", "const:4:8"]]
+ 009b37cc ["CALL", null, ["callee:00c58f30:8"]]
- 009b2820 bytes d0950a94
+ 009b37cc bytes d9950a94
- 009b2824 ["COPY", "register:4040:8", ["const:c88000:8"]]
+ 009b37d0 ["COPY", "register:4040:8", ["const:c89000:8"]]
- 009b2824 bytes a81600d0
+ 009b37d0 bytes a81600d0
- 009b2828 ["COPY", "tmp:0:8", ["const:dd0:8"]]
- 009b2828 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009b2828 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009b2828 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009b37d4 ["COPY", "tmp:0:8", ["const:da0:8"]]
+ 009b37d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009b37d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009b37d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009b2828 bytes 08413791
+ 009b37d4 bytes 08813691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6537b3c67fb15c3195a625d580ca3db1"></a>

### [`009b2838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b2838.md) → [`009b37e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b37e4.md) FUN_009b37e4

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009b37e8",
      "incomplete_value": false,
      "site": "009b37ec",
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
            "const:da0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b283c",
      "incomplete_value": false,
      "site": "009b2840",
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
            "const:dd0:8"
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
      "009b37ec",
      "DATA",
      [
        "storage",
        "00c88dd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b37ec",
      "DATA",
      [
        "storage",
        "00c89da0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b2838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b2838.md#insn-009b2838) · [`009b283c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b2838.md#insn-009b283c)
- 新版 [`009b37e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b37e4.md#insn-009b37e4) · [`009b37e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b37e4.md#insn-009b37e8)

~~~diff
- 009b2838 ["COPY", "register:4040:8", ["const:c88000:8"]]
+ 009b37e4 ["COPY", "register:4040:8", ["const:c89000:8"]]
- 009b2838 bytes a81600d0
+ 009b37e4 bytes a81600d0
- 009b283c ["COPY", "tmp:0:8", ["const:dd0:8"]]
- 009b283c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009b283c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009b283c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009b37e8 ["COPY", "tmp:0:8", ["const:da0:8"]]
+ 009b37e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009b37e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009b37e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009b283c bytes 08413791
+ 009b37e8 bytes 08813691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91ea0f81fdffdc1af46aea5c5b21b668"></a>

### [`009b2850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b2850.md) → [`009b37fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b37fc.md) FUN_009b37fc

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008ba17c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba17c.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 92.86% / 新版 92.86%

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
      "site": "009b3820",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009b2874",
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
      "site": "009b3848",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009b289c",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "009b3820",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "009b3848",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "009b3820",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      "009b3848",
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

- 旧版 [`009b2874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b2850.md#insn-009b2874) · [`009b289c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b2850.md#insn-009b289c) · [`009b2880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b2850.md#insn-009b2880)
- 新版 [`009b3820`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b37fc.md#insn-009b3820) · [`009b3848`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b37fc.md#insn-009b3848) · [`009b382c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b37fc.md#insn-009b382c)

~~~diff
- 009b2874 ["INT_ADD", "register:40f0:8", ["const:9b2874:8", "const:4:8"]]
- 009b2874 ["CALL", null, ["ram:47ad34:8"]]
+ 009b3820 ["INT_ADD", "register:40f0:8", ["const:9b3820:8", "const:4:8"]]
+ 009b3820 ["CALL", null, ["ram:47b054:8"]]
- 009b2874 bytes 3021eb97
+ 009b3820 bytes 0d1eeb97
- 009b289c ["INT_ADD", "register:40f0:8", ["const:9b289c:8", "const:4:8"]]
- 009b289c ["CALL", null, ["ram:47ad34:8"]]
+ 009b3848 ["INT_ADD", "register:40f0:8", ["const:9b3848:8", "const:4:8"]]
+ 009b3848 ["CALL", null, ["ram:47b054:8"]]
- 009b289c bytes 2621eb97
+ 009b3848 bytes 031eeb97
- 009b2880 ["INT_ADD", "register:40f0:8", ["const:9b2880:8", "const:4:8"]]
- 009b2880 ["CALL", null, ["callee:0047d134:8"]]
+ 009b382c ["INT_ADD", "register:40f0:8", ["const:9b382c:8", "const:4:8"]]
+ 009b382c ["CALL", null, ["callee:0047d134:8"]]
- 009b2880 bytes 6529eb97
+ 009b382c bytes 4226eb97
~~~


<a id="compare-2f3921b84d889312341d256cff2316fb"></a>

### [`009b2978`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b2978.md) → [`009b3924`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b3924.md) FUN_009b3924

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.29% / 新版 94.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009b393c",
      "incomplete_value": false,
      "site": "009b394c",
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
            "const:e20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b2990",
      "incomplete_value": false,
      "site": "009b29a0",
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
            "const:e50:8"
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
      "009b394c",
      "DATA",
      [
        "storage",
        "00c88e50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b394c",
      "DATA",
      [
        "storage",
        "00c89e20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b298c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b2978.md#insn-009b298c) · [`009b2990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b2978.md#insn-009b2990) · [`009b29c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b2978.md#insn-009b29c4)
- 新版 [`009b3938`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b3924.md#insn-009b3938) · [`009b393c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b3924.md#insn-009b393c) · [`009b3970`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b3924.md#insn-009b3970)

~~~diff
- 009b298c ["COPY", "register:4040:8", ["const:c88000:8"]]
+ 009b3938 ["COPY", "register:4040:8", ["const:c89000:8"]]
- 009b298c bytes a81600d0
+ 009b3938 bytes a81600d0
- 009b2990 ["COPY", "tmp:0:8", ["const:e50:8"]]
- 009b2990 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009b2990 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009b2990 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009b393c ["COPY", "tmp:0:8", ["const:e20:8"]]
+ 009b393c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009b393c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009b393c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009b2990 bytes 08413991
+ 009b393c bytes 08813891
- 009b29c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 009b29c4 ["INT_ADD", "register:40f0:8", ["const:9b29c4:8", "const:4:8"]]
- 009b29c4 ["CALLIND", null, ["register:0:8"]]
+ 009b3970 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009b3970 ["INT_ADD", "register:40f0:8", ["const:9b3970:8", "const:4:8"]]
+ 009b3970 ["CALLIND", null, ["register:0:8"]]
- 009b29c4 bytes 00013fd6
+ 009b3970 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec6eb52fe52d53e13eed3b68da51ae4b"></a>

### [`009b2a04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b2a04.md) → [`009b39b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b39b0.md) FUN_009b39b0

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "009b39e0",
      "incomplete_value": false,
      "site": "009b39e0",
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
            "const:e20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b2a34",
      "incomplete_value": false,
      "site": "009b2a34",
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
            "const:e50:8"
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
      "009b39e0",
      "DATA",
      [
        "storage",
        "00c88e50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b39e0",
      "DATA",
      [
        "storage",
        "00c89e20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b2a1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b2a04.md#insn-009b2a1c) · [`009b2a28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b2a04.md#insn-009b2a28) · [`009b2a2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b2a04.md#insn-009b2a2c)
- 新版 [`009b39c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b39b0.md#insn-009b39c8) · [`009b39d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b39b0.md#insn-009b39d4) · [`009b39d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b39b0.md#insn-009b39d8)

~~~diff
- 009b2a1c ["INT_ADD", "register:40f0:8", ["const:9b2a1c:8", "const:4:8"]]
- 009b2a1c ["CALL", null, ["callee:00c58f30:8"]]
+ 009b39c8 ["INT_ADD", "register:40f0:8", ["const:9b39c8:8", "const:4:8"]]
+ 009b39c8 ["CALL", null, ["callee:00c58f30:8"]]
- 009b2a1c bytes 51950a94
+ 009b39c8 bytes 5a950a94
- 009b2a28 ["COPY", "register:4040:8", ["const:c88000:8"]]
+ 009b39d4 ["COPY", "register:4040:8", ["const:c89000:8"]]
- 009b2a28 bytes a81600d0
+ 009b39d4 bytes a81600d0
- 009b2a2c ["COPY", "tmp:0:8", ["const:e50:8"]]
- 009b2a2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009b2a2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009b2a2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009b39d8 ["COPY", "tmp:0:8", ["const:e20:8"]]
+ 009b39d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009b39d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009b39d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009b2a2c bytes 08413991
+ 009b39d8 bytes 08813891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e12cc0c6a0e8acf62af40231d4a9df38"></a>

### [`009b2b0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b2b0c.md) → [`009b3ab8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b3ab8.md) FUN_009b3ab8

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

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
      "definition_site": "009b3ae0",
      "incomplete_value": false,
      "site": "009b3ae0",
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
            "const:e20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b2b34",
      "incomplete_value": false,
      "site": "009b2b34",
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
            "const:e50:8"
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
      "009b3ae0",
      "DATA",
      [
        "storage",
        "00c88e50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b3ae0",
      "DATA",
      [
        "storage",
        "00c89e20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b2b28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b2b0c.md#insn-009b2b28) · [`009b2b2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b2b0c.md#insn-009b2b2c) · [`009b2b30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b2b0c.md#insn-009b2b30)
- 新版 [`009b3ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b3ab8.md#insn-009b3ad4) · [`009b3ad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b3ab8.md#insn-009b3ad8)

~~~diff
- 009b2b28 ["COPY", "register:4040:8", ["const:c88000:8"]]
+ 009b3ad4 ["COPY", "register:4040:8", ["const:c89000:8"]]
- 009b2b28 bytes a81600d0
+ 009b3ad4 bytes a81600d0
- 009b2b2c ["COPY", "tmp:0:8", ["const:e50:8"]]
- 009b2b2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009b2b2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009b2b2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009b3ad8 ["COPY", "tmp:0:8", ["const:e20:8"]]
+ 009b3ad8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009b3ad8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009b3ad8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009b2b2c bytes 08413991
+ 009b3ad8 bytes 08813891
- 009b2b30 ["COPY", "register:40a0:8", ["register:4008:8"]]
- 009b2b30 bytes f40301aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f9ad46d8fb4b2c3dee095b05be58723"></a>

### [`009b2df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b2df8.md) → [`009b3da4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b3da4.md) _INIT_196

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.14% / 新版 88.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009b3de0",
      "incomplete_value": true,
      "site": "009b3dfc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "009b2e34",
      "incomplete_value": true,
      "site": "009b2e50",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "009b3e44",
      "incomplete_value": true,
      "site": "009b3e5c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:fe0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b2e98",
      "incomplete_value": true,
      "site": "009b2eb0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009b3e80",
      "incomplete_value": true,
      "site": "009b3e9c",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:f50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b2ed4",
      "incomplete_value": true,
      "site": "009b2ef0",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:f10:8"
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
      "009b3de0",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "009b3e04",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "009b3e24",
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
      "009b3de0",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "009b3e04",
      "READ",
      [
        "storage",
        "002b8048",
        null,
        "string"
      ]
    ],
    [
      "009b3e24",
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

- 旧版 [`009b302c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b2df8.md#insn-009b302c) · [`009b2e20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b2df8.md#insn-009b2e20) · [`009b2e24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b2/009b2df8.md#insn-009b2e24)
- 新版 [`009b3fd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b3da4.md#insn-009b3fd8) · [`009b3dcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b3da4.md#insn-009b3dcc) · [`009b3dd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b3/009b3da4.md#insn-009b3dd0)

~~~diff
- 009b302c ["INT_ADD", "register:40f0:8", ["const:9b302c:8", "const:4:8"]]
- 009b302c ["CALL", null, ["callee:00c58ed0:8"]]
+ 009b3fd8 ["INT_ADD", "register:40f0:8", ["const:9b3fd8:8", "const:4:8"]]
+ 009b3fd8 ["CALL", null, ["callee:00c58ed0:8"]]
- 009b302c bytes b5930a94
+ 009b3fd8 bytes be930a94
- 009b2e20 ["COPY", "register:4098:8", ["const:1123000:8"]]
+ 009b3dcc ["COPY", "register:4098:8", ["const:1124000:8"]]
- 009b2e20 bytes 933b00b0
+ 009b3dcc bytes 933b00b0
- 009b2e24 ["COPY", "tmp:0:8", ["const:cf0:8"]]
- 009b2e24 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 009b2e24 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 009b2e24 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 009b3dd0 ["COPY", "tmp:0:8", ["const:cb0:8"]]
+ 009b3dd0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 009b3dd0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 009b3dd0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 009b2e24 bytes 73c23391
+ 009b3dd0 bytes 73c23291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5782125085f70e8728c0617663248f1d"></a>

### [`009b3188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b3/009b3188.md) → [`009b4134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b4/009b4134.md) FUN_009b4134

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005a8e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a8/005a8e68.md) · 呼出先 6件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`005a9f94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a9/005a9f94.md) [`009b37ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b3/009b37ec.md) [`009b5dd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b5/009b5dd8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`005a9218`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005a9/005a9218.md) · 呼出先 6件 [`004413ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004413ec.md) [`005aa344`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005aa/005aa344.md) [`009b4798`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b4/009b4798.md) [`009b6d84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b6/009b6d84.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.68% / 新版 98.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009b42a0",
      "incomplete_value": true,
      "site": "009b42b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:14d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b32f4",
      "incomplete_value": true,
      "site": "009b3304",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7e:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "009b42b4",
      "incomplete_value": true,
      "site": "009b42b4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "009b3308",
      "incomplete_value": true,
      "site": "009b3308",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 33,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009b42a0",
      "READ",
      [
        "storage",
        "002b907e",
        null,
        "string"
      ]
    ],
    [
      "009b42a8",
      "READ",
      [
        "storage",
        "002b9085",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009b42a0",
      "READ",
      [
        "storage",
        "002b914d",
        null,
        "string"
      ]
    ],
    [
      "009b42a8",
      "READ",
      [
        "storage",
        "002b9154",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b3254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b3/009b3188.md#insn-009b3254) · [`009b3270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b3/009b3188.md#insn-009b3270) · [`009b328c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b3/009b3188.md#insn-009b328c)
- 新版 [`009b4200`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b4/009b4134.md#insn-009b4200) · [`009b421c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b4/009b4134.md#insn-009b421c) · [`009b4238`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b4/009b4134.md#insn-009b4238)

~~~diff
- 009b3254 ["INT_ADD", "register:40f0:8", ["const:9b3254:8", "const:4:8"]]
- 009b3254 ["CALL", null, ["callee:004413ec:8"]]
+ 009b4200 ["INT_ADD", "register:40f0:8", ["const:9b4200:8", "const:4:8"]]
+ 009b4200 ["CALL", null, ["callee:004413ec:8"]]
- 009b3254 bytes 9e37ea97
+ 009b4200 bytes 7b34ea97
- 009b3270 ["COPY", "register:0:8", ["register:4040:8"]]
- 009b3270 ["INT_ADD", "register:40f0:8", ["const:9b3270:8", "const:4:8"]]
- 009b3270 ["CALLIND", null, ["register:0:8"]]
+ 009b421c ["COPY", "register:0:8", ["register:4040:8"]]
+ 009b421c ["INT_ADD", "register:40f0:8", ["const:9b421c:8", "const:4:8"]]
+ 009b421c ["CALLIND", null, ["register:0:8"]]
- 009b3270 bytes 00013fd6
+ 009b421c bytes 00013fd6
- 009b328c ["INT_ADD", "register:40f0:8", ["const:9b328c:8", "const:4:8"]]
- 009b328c ["CALL", null, ["callee:00c58f50:8"]]
+ 009b4238 ["INT_ADD", "register:40f0:8", ["const:9b4238:8", "const:4:8"]]
+ 009b4238 ["CALL", null, ["callee:00c58f50:8"]]
- 009b328c bytes 3d930a94
+ 009b4238 bytes 46930a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d162f52b1e2b1ce36b08ad57e478e1c"></a>

### [`009b37ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b3/009b37ec.md) → [`009b4798`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b4/009b4798.md) FUN_009b4798

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`005aa7ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005aa/005aa7ec.md) [`005ab954`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ab/005ab954.md) [`009b3188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b3/009b3188.md) · 呼出先 7件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`005aa1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005aa/005aa1b0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 3件 [`005aab9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005aa/005aab9c.md) [`005abd04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ab/005abd04.md) [`009b4134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b4/009b4134.md) · 呼出先 7件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`004413ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004413ec.md) [`005aa560`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005aa/005aa560.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.53% / 新版 98.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009b4804",
      "incomplete_value": true,
      "site": "009b4804",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b3858",
      "incomplete_value": true,
      "site": "009b3858",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fdb:8"
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
      "009b47ec",
      "READ",
      [
        "storage",
        "002b9fdb",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "009b47ec",
      "READ",
      [
        "storage",
        "002ba0b9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b3838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b3/009b37ec.md#insn-009b3838) · [`009b383c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b3/009b37ec.md#insn-009b383c) · [`009b38b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b3/009b37ec.md#insn-009b38b4)
- 新版 [`009b47e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b4/009b4798.md#insn-009b47e4) · [`009b47e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b4/009b4798.md#insn-009b47e8) · [`009b4860`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b4/009b4798.md#insn-009b4860)

~~~diff
- 009b3838 ["COPY", "register:4048:8", ["const:2b9000:8"]]
+ 009b47e4 ["COPY", "register:4048:8", ["const:2ba000:8"]]
- 009b3838 bytes 29c8ffd0
+ 009b47e4 bytes 29c8ffd0
- 009b383c ["COPY", "tmp:0:8", ["const:fdb:8"]]
- 009b383c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 009b383c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 009b383c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 009b47e8 ["COPY", "tmp:0:8", ["const:b9:8"]]
+ 009b47e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 009b47e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 009b47e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 009b383c bytes 296d3f91
+ 009b47e8 bytes 29e50291
- 009b38b4 ["INT_ADD", "register:40f0:8", ["const:9b38b4:8", "const:4:8"]]
- 009b38b4 ["CALL", null, ["callee:004413ec:8"]]
+ 009b4860 ["INT_ADD", "register:40f0:8", ["const:9b4860:8", "const:4:8"]]
+ 009b4860 ["CALL", null, ["callee:004413ec:8"]]
- 009b38b4 bytes 0636ea97
+ 009b4860 bytes e332ea97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-507d1ac259306ec5b26b5415ba8da514"></a>

### [`009b3bbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b3/009b3bbc.md) → [`009b4b68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b4/009b4b68.md) FUN_009b4b68

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`009ae184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ae/009ae184.md) [`009ae9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ae/009ae9dc.md) [`009b46f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b4/009b46f4.md) · 呼出先 10件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`007522d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00752/007522d8.md) [`009a97bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a9/009a97bc.md) [`009a97cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a9/009a97cc.md) [`009b41b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b4/009b41b8.md)
- 新版 呼出元 3件 [`009af130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009af/009af130.md) [`009af988`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009af/009af988.md) [`009b56a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b5/009b56a0.md) · 呼出先 10件 [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`00752688`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00752/00752688.md) [`009aa768`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009aa/009aa768.md) [`009aa778`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009aa/009aa778.md) [`009b5164`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b5/009b5164.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.55% / 新版 98.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009b4cf0",
      "incomplete_value": false,
      "site": "009b4cfc",
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
            "const:eb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b3d44",
      "incomplete_value": false,
      "site": "009b3d50",
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
            "const:ee0:8"
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
      "definition_site": "009b4db0",
      "incomplete_value": false,
      "site": "009b4dbc",
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
            "const:f30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b3e04",
      "incomplete_value": false,
      "site": "009b3e10",
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
            "const:f60:8"
          ]
        ]
      ]
    },
    "ordinal": 40,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009b4cfc",
      "DATA",
      [
        "storage",
        "00c88ee0",
        null,
        "undefined *"
      ]
    ],
    [
      "009b4dbc",
      "DATA",
      [
        "storage",
        "00c88f60",
        null,
        "undefined *"
      ]
    ],
    [
      "009b4e4c",
      "READ",
      [
        "storage",
        "00c88f88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b4cfc",
      "DATA",
      [
        "storage",
        "00c89eb0",
        null,
        "undefined *"
      ]
    ],
    [
      "009b4dbc",
      "DATA",
      [
        "storage",
        "00c89f30",
        null,
        "undefined *"
      ]
    ],
    [
      "009b4e4c",
      "READ",
      [
        "storage",
        "00c89f58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b3bfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b3/009b3bbc.md#insn-009b3bfc) · [`009b3c08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b3/009b3bbc.md#insn-009b3c08) · [`009b3c38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b3/009b3bbc.md#insn-009b3c38)
- 新版 [`009b4ba8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b4/009b4b68.md#insn-009b4ba8) · [`009b4bb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b4/009b4b68.md#insn-009b4bb4) · [`009b4be4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b4/009b4b68.md#insn-009b4be4)

~~~diff
- 009b3bfc ["INT_ADD", "register:40f0:8", ["const:9b3bfc:8", "const:4:8"]]
- 009b3bfc ["CALL", null, ["callee:009aa778:8"]]
+ 009b4ba8 ["INT_ADD", "register:40f0:8", ["const:9b4ba8:8", "const:4:8"]]
+ 009b4ba8 ["CALL", null, ["callee:009aa778:8"]]
- 009b3bfc bytes f4d6ff97
+ 009b4ba8 bytes f4d6ff97
- 009b3c08 ["INT_ADD", "register:40f0:8", ["const:9b3c08:8", "const:4:8"]]
- 009b3c08 ["CALL", null, ["callee:009aa768:8"]]
+ 009b4bb4 ["INT_ADD", "register:40f0:8", ["const:9b4bb4:8", "const:4:8"]]
+ 009b4bb4 ["CALL", null, ["callee:009aa768:8"]]
- 009b3c08 bytes edd6ff97
+ 009b4bb4 bytes edd6ff97
- 009b3c38 ["COPY", "register:0:8", ["register:4040:8"]]
- 009b3c38 ["INT_ADD", "register:40f0:8", ["const:9b3c38:8", "const:4:8"]]
- 009b3c38 ["CALLIND", null, ["register:0:8"]]
+ 009b4be4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009b4be4 ["INT_ADD", "register:40f0:8", ["const:9b4be4:8", "const:4:8"]]
+ 009b4be4 ["CALLIND", null, ["register:0:8"]]
- 009b3c38 bytes 00013fd6
+ 009b4be4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6c2698b5f07883a5d4dd0eaabb9a865"></a>

### [`009b41b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b4/009b41b8.md) → [`009b5164`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b5/009b5164.md) FUN_009b5164

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0074600c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00746/0074600c.md) [`009b3bbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b3/009b3bbc.md) · 呼出先 15件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00598b74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598b74.md) [`00598d34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598d34.md) [`005ac030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ac/005ac030.md) [`00795e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795e7c.md)
- 新版 呼出元 2件 [`007463bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00746/007463bc.md) [`009b4b68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b4/009b4b68.md) · 呼出先 15件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00598e94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00598/00598e94.md) [`00599054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00599/00599054.md) [`005ac3e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ac/005ac3e0.md) [`00796258`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00796/00796258.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.15% / 新版 97.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009b5234",
      "incomplete_value": false,
      "site": "009b5238",
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
                "const:c6e000:8"
              ],
              [
                "leaf",
                "const:ab0:8"
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
      "definition_site": "009b4288",
      "incomplete_value": false,
      "site": "009b428c",
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
                "const:ae0:8"
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009b52c4",
      "incomplete_value": false,
      "site": "009b52c4",
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
    "old": {
      "definition_site": "009b4318",
      "incomplete_value": false,
      "site": "009b4318",
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
            "const:460:8"
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009b53d4",
      "incomplete_value": false,
      "site": "009b53d4",
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
    "old": {
      "definition_site": "009b4428",
      "incomplete_value": false,
      "site": "009b4428",
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
            "const:4e0:8"
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
      "009b5238",
      "DATA",
      [
        "storage",
        "00c6daf0",
        null,
        "undefined *"
      ]
    ],
    [
      "009b52c4",
      "DATA",
      [
        "storage",
        "00c89460",
        null,
        "undefined *"
      ]
    ],
    [
      "009b5338",
      "READ",
      [
        "storage",
        "00c89488",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b5238",
      "DATA",
      [
        "storage",
        "00c6eac0",
        null,
        "undefined *"
      ]
    ],
    [
      "009b52c4",
      "DATA",
      [
        "storage",
        "00c8a430",
        null,
        "undefined *"
      ]
    ],
    [
      "009b5338",
      "READ",
      [
        "storage",
        "00c8a458",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b41f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b4/009b41b8.md#insn-009b41f8) · [`009b4224`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b4/009b41b8.md#insn-009b4224) · [`009b4238`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b4/009b41b8.md#insn-009b4238)
- 新版 [`009b51a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b5/009b5164.md#insn-009b51a4) · [`009b51d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b5/009b5164.md#insn-009b51d0) · [`009b51e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b5/009b5164.md#insn-009b51e4)

~~~diff
- 009b41f8 ["INT_ADD", "register:40f0:8", ["const:9b41f8:8", "const:4:8"]]
- 009b41f8 ["CALL", null, ["callee:00c58f30:8"]]
+ 009b51a4 ["INT_ADD", "register:40f0:8", ["const:9b51a4:8", "const:4:8"]]
+ 009b51a4 ["CALL", null, ["callee:00c58f30:8"]]
- 009b41f8 bytes 5a8f0a94
+ 009b51a4 bytes 638f0a94
- 009b4224 ["INT_ADD", "register:40f0:8", ["const:9b4224:8", "const:4:8"]]
- 009b4224 ["CALL", null, ["callee:0043be80:8"]]
+ 009b51d0 ["INT_ADD", "register:40f0:8", ["const:9b51d0:8", "const:4:8"]]
+ 009b51d0 ["CALL", null, ["callee:0043be80:8"]]
- 009b4224 bytes 4f1eea97
+ 009b51d0 bytes 2c1bea97
- 009b4238 ["INT_ADD", "register:40f0:8", ["const:9b4238:8", "const:4:8"]]
- 009b4238 ["CALL", null, ["callee:005ac3e0:8"]]
+ 009b51e4 ["INT_ADD", "register:40f0:8", ["const:9b51e4:8", "const:4:8"]]
+ 009b51e4 ["CALL", null, ["callee:005ac3e0:8"]]
- 009b4238 bytes 7edfef97
+ 009b51e4 bytes 7fdcef97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1873f65591a08f7850144474ce118b5f"></a>

### [`009b46f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b4/009b46f4.md) → [`009b56a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b5/009b56a0.md) FUN_009b56a0

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009ad8d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ad/009ad8d0.md) · 呼出先 15件 [`007522d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00752/007522d8.md) [`009a97bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a9/009a97bc.md) [`009a97c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a9/009a97c4.md) [`009aad6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009aa/009aad6c.md) [`009aadf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009aa/009aadf4.md)
- 新版 呼出元 1件 [`009ae87c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ae/009ae87c.md) · 呼出先 15件 [`00752688`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00752/00752688.md) [`009aa768`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009aa/009aa768.md) [`009aa770`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009aa/009aa770.md) [`009abd18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ab/009abd18.md) [`009abda0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ab/009abda0.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.23% / 新版 92.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009b5708",
      "incomplete_value": false,
      "site": "009b5708",
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
    "old": {
      "definition_site": "009b475c",
      "incomplete_value": false,
      "site": "009b475c",
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
            "const:fe0:8"
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
      "definition_site": "009b575c",
      "incomplete_value": false,
      "site": "009b575c",
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
            "const:30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b47b0",
      "incomplete_value": false,
      "site": "009b47b0",
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
            "const:60:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009b5770",
      "incomplete_value": false,
      "site": "009b5774",
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
            "const:b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b47c4",
      "incomplete_value": false,
      "site": "009b47c8",
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
            "const:e0:8"
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
      "009b56d4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "009a97c4"
      ]
    ],
    [
      "009b56e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "009a97c4"
      ]
    ],
    [
      "009b5708",
      "DATA",
      [
        "storage",
        "00c88fe0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b56d4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "009aa770"
      ]
    ],
    [
      "009b56e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "009aa770"
      ]
    ],
    [
      "009b5708",
      "DATA",
      [
        "storage",
        "00c89fb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b4728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b4/009b46f4.md#insn-009b4728) · [`009b4738`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b4/009b46f4.md#insn-009b4738) · [`009b471c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b4/009b46f4.md#insn-009b471c)
- 新版 [`009b56d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b5/009b56a0.md#insn-009b56d4) · [`009b56e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b5/009b56a0.md#insn-009b56e4) · [`009b56c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b5/009b56a0.md#insn-009b56c8)

~~~diff
- 009b4728 ["INT_ADD", "register:40f0:8", ["const:9b4728:8", "const:4:8"]]
- 009b4728 ["CALL", null, ["ram:9a97c4:8"]]
+ 009b56d4 ["INT_ADD", "register:40f0:8", ["const:9b56d4:8", "const:4:8"]]
+ 009b56d4 ["CALL", null, ["ram:9aa770:8"]]
- 009b4728 bytes 27d4ff97
+ 009b56d4 bytes 27d4ff97
- 009b4738 ["INT_ADD", "register:40f0:8", ["const:9b4738:8", "const:4:8"]]
- 009b4738 ["CALL", null, ["ram:9a97c4:8"]]
+ 009b56e4 ["INT_ADD", "register:40f0:8", ["const:9b56e4:8", "const:4:8"]]
+ 009b56e4 ["CALL", null, ["ram:9aa770:8"]]
- 009b4738 bytes 23d4ff97
+ 009b56e4 bytes 23d4ff97
- 009b471c ["INT_ADD", "register:40f0:8", ["const:9b471c:8", "const:4:8"]]
- 009b471c ["CALL", null, ["callee:009abda0:8"]]
+ 009b56c8 ["INT_ADD", "register:40f0:8", ["const:9b56c8:8", "const:4:8"]]
+ 009b56c8 ["CALL", null, ["callee:009abda0:8"]]
- 009b471c bytes b6d9ff97
+ 009b56c8 bytes b6d9ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce888233399e571d6c085fed653463b4"></a>

### [`009b4954`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b4/009b4954.md) → [`009b5900`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b5/009b5900.md) FUN_009b5900

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`00745a7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00745/00745a7c.md) [`0074670c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00746/0074670c.md) [`009ae2c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ae/009ae2c0.md) [`009b46f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b4/009b46f4.md) · 呼出先 15件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00598b74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598b74.md) [`00598d34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598d34.md) [`005aaec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005aa/005aaec8.md) [`00795e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795e7c.md)
- 新版 呼出元 4件 [`00745e2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00745/00745e2c.md) [`00746abc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00746/00746abc.md) [`009af26c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009af/009af26c.md) [`009b56a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b5/009b56a0.md) · 呼出先 15件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00598e94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00598/00598e94.md) [`00599054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00599/00599054.md) [`005ab278`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ab/005ab278.md) [`00796258`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00796/00796258.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.93% / 新版 97.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009b5a54",
      "incomplete_value": false,
      "site": "009b5a54",
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
    "old": {
      "definition_site": "009b4aa8",
      "incomplete_value": false,
      "site": "009b4aa8",
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
            "const:360:8"
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
      "definition_site": "009b5b64",
      "incomplete_value": false,
      "site": "009b5b64",
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
    "old": {
      "definition_site": "009b4bb8",
      "incomplete_value": false,
      "site": "009b4bb8",
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
            "const:3e0:8"
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
      "009b59c8",
      "DATA",
      [
        "storage",
        "00c6daf0",
        null,
        "undefined *"
      ]
    ],
    [
      "009b5a54",
      "DATA",
      [
        "storage",
        "00c89360",
        null,
        "undefined *"
      ]
    ],
    [
      "009b5ac8",
      "READ",
      [
        "storage",
        "00c89388",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b59c8",
      "DATA",
      [
        "storage",
        "00c6eac0",
        null,
        "undefined *"
      ]
    ],
    [
      "009b5a54",
      "DATA",
      [
        "storage",
        "00c8a330",
        null,
        "undefined *"
      ]
    ],
    [
      "009b5ac8",
      "READ",
      [
        "storage",
        "00c8a358",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b498c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b4/009b4954.md#insn-009b498c) · [`009b49b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b4/009b4954.md#insn-009b49b8) · [`009b49c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b4/009b4954.md#insn-009b49c8)
- 新版 [`009b5938`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b5/009b5900.md#insn-009b5938) · [`009b5964`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b5/009b5900.md#insn-009b5964) · [`009b5974`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b5/009b5900.md#insn-009b5974)

~~~diff
- 009b498c ["INT_ADD", "register:40f0:8", ["const:9b498c:8", "const:4:8"]]
- 009b498c ["CALL", null, ["callee:00c58f30:8"]]
+ 009b5938 ["INT_ADD", "register:40f0:8", ["const:9b5938:8", "const:4:8"]]
+ 009b5938 ["CALL", null, ["callee:00c58f30:8"]]
- 009b498c bytes 758d0a94
+ 009b5938 bytes 7e8d0a94
- 009b49b8 ["INT_ADD", "register:40f0:8", ["const:9b49b8:8", "const:4:8"]]
- 009b49b8 ["CALL", null, ["callee:0043be80:8"]]
+ 009b5964 ["INT_ADD", "register:40f0:8", ["const:9b5964:8", "const:4:8"]]
+ 009b5964 ["CALL", null, ["callee:0043be80:8"]]
- 009b49b8 bytes 6a1cea97
+ 009b5964 bytes 4719ea97
- 009b49c8 ["INT_ADD", "register:40f0:8", ["const:9b49c8:8", "const:4:8"]]
- 009b49c8 ["CALL", null, ["callee:005ab278:8"]]
+ 009b5974 ["INT_ADD", "register:40f0:8", ["const:9b5974:8", "const:4:8"]]
+ 009b5974 ["CALL", null, ["callee:005ab278:8"]]
- 009b49c8 bytes 40d9ef97
+ 009b5974 bytes 41d6ef97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c23e805566796e2a03b1c6450919c8d7"></a>

### [`009b4e80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b4/009b4e80.md) → [`009b5e2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b5/009b5e2c.md) FUN_009b5e2c

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009af9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009af/009af9dc.md) · 呼出先 10件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`007522d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00752/007522d8.md) [`009a97bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a9/009a97bc.md) [`009aa670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009aa/009aa670.md) [`009b5410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b5/009b5410.md)
- 新版 呼出元 1件 [`009b0988`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b0/009b0988.md) · 呼出先 10件 [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`00752688`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00752/00752688.md) [`009aa768`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009aa/009aa768.md) [`009ab61c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ab/009ab61c.md) [`009b63bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b6/009b63bc.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.46% / 新版 98.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009b5f88",
      "incomplete_value": false,
      "site": "009b5f88",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b4fdc",
      "incomplete_value": false,
      "site": "009b4fdc",
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
            "const:160:8"
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
      "definition_site": "009b6048",
      "incomplete_value": false,
      "site": "009b6048",
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
            "const:1b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b509c",
      "incomplete_value": false,
      "site": "009b509c",
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
            "const:1e0:8"
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
      "009b5f88",
      "DATA",
      [
        "storage",
        "00c89160",
        null,
        "undefined *"
      ]
    ],
    [
      "009b6048",
      "DATA",
      [
        "storage",
        "00c891e0",
        null,
        "undefined *"
      ]
    ],
    [
      "009b60d0",
      "READ",
      [
        "storage",
        "00c89208",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b5f88",
      "DATA",
      [
        "storage",
        "00c8a130",
        null,
        "undefined *"
      ]
    ],
    [
      "009b6048",
      "DATA",
      [
        "storage",
        "00c8a1b0",
        null,
        "undefined *"
      ]
    ],
    [
      "009b60d0",
      "READ",
      [
        "storage",
        "00c8a1d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b4eb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b4/009b4e80.md#insn-009b4eb4) · [`009b4ec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b4/009b4e80.md#insn-009b4ec0) · [`009b4ef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b4/009b4e80.md#insn-009b4ef0)
- 新版 [`009b5e60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b5/009b5e2c.md#insn-009b5e60) · [`009b5e6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b5/009b5e2c.md#insn-009b5e6c) · [`009b5e9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b5/009b5e2c.md#insn-009b5e9c)

~~~diff
- 009b4eb4 ["INT_ADD", "register:40f0:8", ["const:9b4eb4:8", "const:4:8"]]
- 009b4eb4 ["CALL", null, ["callee:009ab61c:8"]]
+ 009b5e60 ["INT_ADD", "register:40f0:8", ["const:9b5e60:8", "const:4:8"]]
+ 009b5e60 ["CALL", null, ["callee:009ab61c:8"]]
- 009b4eb4 bytes efd5ff97
+ 009b5e60 bytes efd5ff97
- 009b4ec0 ["INT_ADD", "register:40f0:8", ["const:9b4ec0:8", "const:4:8"]]
- 009b4ec0 ["CALL", null, ["callee:009aa768:8"]]
+ 009b5e6c ["INT_ADD", "register:40f0:8", ["const:9b5e6c:8", "const:4:8"]]
+ 009b5e6c ["CALL", null, ["callee:009aa768:8"]]
- 009b4ec0 bytes 3fd2ff97
+ 009b5e6c bytes 3fd2ff97
- 009b4ef0 ["COPY", "register:0:8", ["register:4040:8"]]
- 009b4ef0 ["INT_ADD", "register:40f0:8", ["const:9b4ef0:8", "const:4:8"]]
- 009b4ef0 ["CALLIND", null, ["register:0:8"]]
+ 009b5e9c ["COPY", "register:0:8", ["register:4040:8"]]
+ 009b5e9c ["INT_ADD", "register:40f0:8", ["const:9b5e9c:8", "const:4:8"]]
+ 009b5e9c ["CALLIND", null, ["register:0:8"]]
- 009b4ef0 bytes 00013fd6
+ 009b5e9c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62294413ec4721e3c8257aafd6701051"></a>

### [`009b5410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b5/009b5410.md) → [`009b63bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b6/009b63bc.md) FUN_009b63bc

採用 · 移動量 `+0xfac` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00746d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00746/00746d44.md) [`009b4e80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b4/009b4e80.md) · 呼出先 15件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00598b74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598b74.md) [`00598d34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598d34.md) [`005a97a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a9/005a97a0.md) [`00795e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795e7c.md)
- 新版 呼出元 2件 [`007470f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00747/007470f4.md) [`009b5e2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b5/009b5e2c.md) · 呼出先 15件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00598e94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00598/00598e94.md) [`00599054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00599/00599054.md) [`005a9b50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005a9/005a9b50.md) [`00796258`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00796/00796258.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.11% / 新版 97.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009b6480",
      "incomplete_value": false,
      "site": "009b6484",
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
                "const:c6e000:8"
              ],
              [
                "leaf",
                "const:ab0:8"
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
      "definition_site": "009b54d4",
      "incomplete_value": false,
      "site": "009b54d8",
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
                "const:ae0:8"
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
      "definition_site": "009b6510",
      "incomplete_value": false,
      "site": "009b6510",
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
            "const:230:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b5564",
      "incomplete_value": false,
      "site": "009b5564",
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
            "const:260:8"
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
      "definition_site": "009b6620",
      "incomplete_value": false,
      "site": "009b6620",
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
            "const:2b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b5674",
      "incomplete_value": false,
      "site": "009b5674",
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
            "const:2e0:8"
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
      "009b6484",
      "DATA",
      [
        "storage",
        "00c6daf0",
        null,
        "undefined *"
      ]
    ],
    [
      "009b6510",
      "DATA",
      [
        "storage",
        "00c89260",
        null,
        "undefined *"
      ]
    ],
    [
      "009b6584",
      "READ",
      [
        "storage",
        "00c89288",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b6484",
      "DATA",
      [
        "storage",
        "00c6eac0",
        null,
        "undefined *"
      ]
    ],
    [
      "009b6510",
      "DATA",
      [
        "storage",
        "00c8a230",
        null,
        "undefined *"
      ]
    ],
    [
      "009b6584",
      "READ",
      [
        "storage",
        "00c8a258",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b5448`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b5/009b5410.md#insn-009b5448) · [`009b5474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b5/009b5410.md#insn-009b5474) · [`009b5484`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b5/009b5410.md#insn-009b5484)
- 新版 [`009b63f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b6/009b63bc.md#insn-009b63f4) · [`009b6420`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b6/009b63bc.md#insn-009b6420) · [`009b6430`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b6/009b63bc.md#insn-009b6430)

~~~diff
- 009b5448 ["INT_ADD", "register:40f0:8", ["const:9b5448:8", "const:4:8"]]
- 009b5448 ["CALL", null, ["callee:00c58f30:8"]]
+ 009b63f4 ["INT_ADD", "register:40f0:8", ["const:9b63f4:8", "const:4:8"]]
+ 009b63f4 ["CALL", null, ["callee:00c58f30:8"]]
- 009b5448 bytes c68a0a94
+ 009b63f4 bytes cf8a0a94
- 009b5474 ["INT_ADD", "register:40f0:8", ["const:9b5474:8", "const:4:8"]]
- 009b5474 ["CALL", null, ["callee:0043be80:8"]]
+ 009b6420 ["INT_ADD", "register:40f0:8", ["const:9b6420:8", "const:4:8"]]
+ 009b6420 ["CALL", null, ["callee:0043be80:8"]]
- 009b5474 bytes bb19ea97
+ 009b6420 bytes 9816ea97
- 009b5484 ["INT_ADD", "register:40f0:8", ["const:9b5484:8", "const:4:8"]]
- 009b5484 ["CALL", null, ["callee:005a9b50:8"]]
+ 009b6430 ["INT_ADD", "register:40f0:8", ["const:9b6430:8", "const:4:8"]]
+ 009b6430 ["CALL", null, ["callee:005a9b50:8"]]
- 009b5484 bytes c7d0ef97
+ 009b6430 bytes c8cdef97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35368efa31bbe6ba2f9f10ce6c384484"></a>

### [`009b5a70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b5/009b5a70.md) → [`009b6a1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b6/009b6a1c.md) FUN_009b6a1c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009b6a50",
      "incomplete_value": true,
      "site": "009b6a54",
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
                "register:4040:8"
              ],
              [
                "leaf",
                "const:ab0:8"
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
      "definition_site": "009b5aa4",
      "incomplete_value": true,
      "site": "009b5aa8",
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
                "register:4040:8"
              ],
              [
                "leaf",
                "const:ae0:8"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009b6a54",
      "DATA",
      [
        "storage",
        "00c6daf0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b6a54",
      "DATA",
      [
        "storage",
        "00c6eac0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b5a94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b5/009b5a70.md#insn-009b5a94) · [`009b5a98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b5/009b5a70.md#insn-009b5a98) · [`009b5a9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b5/009b5a70.md#insn-009b5a9c)
- 新版 [`009b6a40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b6/009b6a1c.md#insn-009b6a40) · [`009b6a44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b6/009b6a1c.md#insn-009b6a44) · [`009b6a48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b6/009b6a1c.md#insn-009b6a48)

~~~diff
- 009b5a94 ["INT_ADD", "register:40f0:8", ["const:9b5a94:8", "const:4:8"]]
- 009b5a94 ["CALL", null, ["callee:00c58f50:8"]]
+ 009b6a40 ["INT_ADD", "register:40f0:8", ["const:9b6a40:8", "const:4:8"]]
+ 009b6a40 ["CALL", null, ["callee:00c58f50:8"]]
- 009b5a94 bytes 3b890a94
+ 009b6a40 bytes 44890a94
- 009b5a98 ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 009b6a44 ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 009b5a98 bytes c8150090
+ 009b6a44 bytes c8150090
- 009b5a9c ["COPY", "tmp:0:8", ["const:ae0:8"]]
- 009b5a9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009b5a9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009b5a9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009b6a48 ["COPY", "tmp:0:8", ["const:ab0:8"]]
+ 009b6a48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009b6a48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009b6a48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009b5a9c bytes 08812b91
+ 009b6a48 bytes 08c12a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f56ea6024ae7707607f9fc69fee7065"></a>

### [`009b5ae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b5/009b5ae4.md) → [`009b6a90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b6/009b6a90.md) FUN_009b6a90

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

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
      "definition_site": "009b6ac4",
      "incomplete_value": false,
      "site": "009b6ac8",
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
                "const:c6e000:8"
              ],
              [
                "leaf",
                "const:ab0:8"
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
      "definition_site": "009b5b18",
      "incomplete_value": false,
      "site": "009b5b1c",
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
                "const:ae0:8"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "009b6ac8",
      "DATA",
      [
        "storage",
        "00c6daf0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b6ac8",
      "DATA",
      [
        "storage",
        "00c6eac0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b5b08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b5/009b5ae4.md#insn-009b5b08) · [`009b5b0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b5/009b5ae4.md#insn-009b5b0c) · [`009b5b10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b5/009b5ae4.md#insn-009b5b10)
- 新版 [`009b6ab4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b6/009b6a90.md#insn-009b6ab4) · [`009b6ab8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b6/009b6a90.md#insn-009b6ab8) · [`009b6abc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b6/009b6a90.md#insn-009b6abc)

~~~diff
- 009b5b08 ["INT_ADD", "register:40f0:8", ["const:9b5b08:8", "const:4:8"]]
- 009b5b08 ["CALL", null, ["callee:00c58f50:8"]]
+ 009b6ab4 ["INT_ADD", "register:40f0:8", ["const:9b6ab4:8", "const:4:8"]]
+ 009b6ab4 ["CALL", null, ["callee:00c58f50:8"]]
- 009b5b08 bytes 1e890a94
+ 009b6ab4 bytes 27890a94
- 009b5b0c ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 009b6ab8 ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 009b5b0c bytes c8150090
+ 009b6ab8 bytes c8150090
- 009b5b10 ["COPY", "tmp:0:8", ["const:ae0:8"]]
- 009b5b10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009b5b10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009b5b10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009b6abc ["COPY", "tmp:0:8", ["const:ab0:8"]]
+ 009b6abc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009b6abc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009b6abc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009b5b10 bytes 08812b91
+ 009b6abc bytes 08c12a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61e45848e52af0da3fbf62fe9fd3f1a7"></a>

### [`009b607c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b6/009b607c.md) → [`009b7028`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b7/009b7028.md) FUN_009b7028

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "009b7034",
      "incomplete_value": false,
      "site": "009b7040",
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
            "const:eb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b6088",
      "incomplete_value": false,
      "site": "009b6094",
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
            "const:ee0:8"
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
      "009b7040",
      "DATA",
      [
        "storage",
        "00c88ee0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b7040",
      "DATA",
      [
        "storage",
        "00c89eb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b6084`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b6/009b607c.md#insn-009b6084) · [`009b6088`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b6/009b607c.md#insn-009b6088)
- 新版 [`009b7030`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b7/009b7028.md#insn-009b7030) · [`009b7034`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b7/009b7028.md#insn-009b7034)

~~~diff
- 009b6084 ["COPY", "register:4050:8", ["const:c88000:8"]]
+ 009b7030 ["COPY", "register:4050:8", ["const:c89000:8"]]
- 009b6084 bytes 8a1600d0
+ 009b7030 bytes 8a1600d0
- 009b6088 ["COPY", "tmp:0:8", ["const:ee0:8"]]
- 009b6088 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 009b6088 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 009b6088 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 009b7034 ["COPY", "tmp:0:8", ["const:eb0:8"]]
+ 009b7034 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 009b7034 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 009b7034 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 009b6088 bytes 4a813b91
+ 009b7034 bytes 4ac13a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50288a7b68b2a197ea62d3572f7af810"></a>

### [`009b60c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b6/009b60c0.md) → [`009b706c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b7/009b706c.md) FUN_009b706c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "009b7084",
      "incomplete_value": false,
      "site": "009b7090",
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
            "const:eb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b60d8",
      "incomplete_value": false,
      "site": "009b60e4",
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
            "const:ee0:8"
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
      "009b7090",
      "DATA",
      [
        "storage",
        "00c88ee0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b7090",
      "DATA",
      [
        "storage",
        "00c89eb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b60d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b6/009b60c0.md#insn-009b60d4) · [`009b60d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b6/009b60c0.md#insn-009b60d8) · [`009b6108`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b6/009b60c0.md#insn-009b6108)
- 新版 [`009b7080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b7/009b706c.md#insn-009b7080) · [`009b7084`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b7/009b706c.md#insn-009b7084) · [`009b70b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b7/009b706c.md#insn-009b70b4)

~~~diff
- 009b60d4 ["COPY", "register:4040:8", ["const:c88000:8"]]
+ 009b7080 ["COPY", "register:4040:8", ["const:c89000:8"]]
- 009b60d4 bytes 881600d0
+ 009b7080 bytes 881600d0
- 009b60d8 ["COPY", "tmp:0:8", ["const:ee0:8"]]
- 009b60d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009b60d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009b60d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009b7084 ["COPY", "tmp:0:8", ["const:eb0:8"]]
+ 009b7084 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009b7084 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009b7084 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009b60d8 bytes 08813b91
+ 009b7084 bytes 08c13a91
- 009b6108 ["COPY", "register:0:8", ["register:4040:8"]]
- 009b6108 ["INT_ADD", "register:40f0:8", ["const:9b6108:8", "const:4:8"]]
- 009b6108 ["CALLIND", null, ["register:0:8"]]
+ 009b70b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009b70b4 ["INT_ADD", "register:40f0:8", ["const:9b70b4:8", "const:4:8"]]
+ 009b70b4 ["CALLIND", null, ["register:0:8"]]
- 009b6108 bytes 00013fd6
+ 009b70b4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21b6bcf53e90768d99c0d2510e7f5227"></a>

### [`009b611c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b6/009b611c.md) → [`009b70c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b7/009b70c8.md) FUN_009b70c8

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009b70e4",
      "incomplete_value": false,
      "site": "009b70f4",
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
            "const:eb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b6138",
      "incomplete_value": false,
      "site": "009b6148",
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
            "const:ee0:8"
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
      "009b70f4",
      "DATA",
      [
        "storage",
        "00c88ee0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b70f4",
      "DATA",
      [
        "storage",
        "00c89eb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b6130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b6/009b611c.md#insn-009b6130) · [`009b6134`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b6/009b611c.md#insn-009b6134) · [`009b6138`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b6/009b611c.md#insn-009b6138)
- 新版 [`009b70dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b7/009b70c8.md#insn-009b70dc) · [`009b70e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b7/009b70c8.md#insn-009b70e0) · [`009b70e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b7/009b70c8.md#insn-009b70e4)

~~~diff
- 009b6130 ["INT_ADD", "register:40f0:8", ["const:9b6130:8", "const:4:8"]]
- 009b6130 ["CALL", null, ["callee:00c58f30:8"]]
+ 009b70dc ["INT_ADD", "register:40f0:8", ["const:9b70dc:8", "const:4:8"]]
+ 009b70dc ["CALL", null, ["callee:00c58f30:8"]]
- 009b6130 bytes 8c870a94
+ 009b70dc bytes 95870a94
- 009b6134 ["COPY", "register:4040:8", ["const:c88000:8"]]
+ 009b70e0 ["COPY", "register:4040:8", ["const:c89000:8"]]
- 009b6134 bytes 881600d0
+ 009b70e0 bytes 881600d0
- 009b6138 ["COPY", "tmp:0:8", ["const:ee0:8"]]
- 009b6138 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009b6138 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009b6138 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009b70e4 ["COPY", "tmp:0:8", ["const:eb0:8"]]
+ 009b70e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009b70e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009b70e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009b6138 bytes 08813b91
+ 009b70e4 bytes 08c13a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e87e7f6ff499564cec5c5f4f9f51c17"></a>

### [`009b61b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b6/009b61b4.md) → [`009b7160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b7/009b7160.md) FUN_009b7160

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "009b7170",
      "incomplete_value": false,
      "site": "009b7178",
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
            "const:eb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b61c4",
      "incomplete_value": false,
      "site": "009b61cc",
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
            "const:ee0:8"
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
      "009b7178",
      "DATA",
      [
        "storage",
        "00c88ee0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b7178",
      "DATA",
      [
        "storage",
        "00c89eb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b61c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b6/009b61b4.md#insn-009b61c0) · [`009b61c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b6/009b61b4.md#insn-009b61c4) · [`009b6200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b6/009b61b4.md#insn-009b6200)
- 新版 [`009b716c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b7/009b7160.md#insn-009b716c) · [`009b7170`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b7/009b7160.md#insn-009b7170) · [`009b71ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b7/009b7160.md#insn-009b71ac)

~~~diff
- 009b61c0 ["COPY", "register:4040:8", ["const:c88000:8"]]
+ 009b716c ["COPY", "register:4040:8", ["const:c89000:8"]]
- 009b61c0 bytes 881600d0
+ 009b716c bytes 881600d0
- 009b61c4 ["COPY", "tmp:0:8", ["const:ee0:8"]]
- 009b61c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009b61c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009b61c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009b7170 ["COPY", "tmp:0:8", ["const:eb0:8"]]
+ 009b7170 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009b7170 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009b7170 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009b61c4 bytes 08813b91
+ 009b7170 bytes 08c13a91
- 009b6200 ["COPY", "register:0:8", ["register:4048:8"]]
- 009b6200 ["INT_ADD", "register:40f0:8", ["const:9b6200:8", "const:4:8"]]
- 009b6200 ["CALLIND", null, ["register:0:8"]]
+ 009b71ac ["COPY", "register:0:8", ["register:4048:8"]]
+ 009b71ac ["INT_ADD", "register:40f0:8", ["const:9b71ac:8", "const:4:8"]]
+ 009b71ac ["CALLIND", null, ["register:0:8"]]
- 009b6200 bytes 20013fd6
+ 009b71ac bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47a62cbda9cf5d0d7394917379b44718"></a>

### [`009b64d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b6/009b64d0.md) → [`009b747c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b7/009b747c.md) FUN_009b747c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "009b7488",
      "incomplete_value": false,
      "site": "009b7494",
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
            "const:f30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b64dc",
      "incomplete_value": false,
      "site": "009b64e8",
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
            "const:f60:8"
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
      "009b7494",
      "DATA",
      [
        "storage",
        "00c88f60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b7494",
      "DATA",
      [
        "storage",
        "00c89f30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b64d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b6/009b64d0.md#insn-009b64d8) · [`009b64dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b6/009b64d0.md#insn-009b64dc)
- 新版 [`009b7484`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b7/009b747c.md#insn-009b7484) · [`009b7488`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b7/009b747c.md#insn-009b7488)

~~~diff
- 009b64d8 ["COPY", "register:4050:8", ["const:c88000:8"]]
+ 009b7484 ["COPY", "register:4050:8", ["const:c89000:8"]]
- 009b64d8 bytes 8a1600d0
+ 009b7484 bytes 8a1600d0
- 009b64dc ["COPY", "tmp:0:8", ["const:f60:8"]]
- 009b64dc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 009b64dc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 009b64dc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 009b7488 ["COPY", "tmp:0:8", ["const:f30:8"]]
+ 009b7488 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 009b7488 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 009b7488 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 009b64dc bytes 4a813d91
+ 009b7488 bytes 4ac13c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21c45a62fa2d0f4db740180890ad10fb"></a>

### [`009b6514`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b6/009b6514.md) → [`009b74c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b7/009b74c0.md) FUN_009b74c0

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "009b74d8",
      "incomplete_value": false,
      "site": "009b74e4",
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
            "const:f30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b652c",
      "incomplete_value": false,
      "site": "009b6538",
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
            "const:f60:8"
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
      "009b74e4",
      "DATA",
      [
        "storage",
        "00c88f60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b74e4",
      "DATA",
      [
        "storage",
        "00c89f30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b6528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b6/009b6514.md#insn-009b6528) · [`009b652c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b6/009b6514.md#insn-009b652c) · [`009b655c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b6/009b6514.md#insn-009b655c)
- 新版 [`009b74d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b7/009b74c0.md#insn-009b74d4) · [`009b74d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b7/009b74c0.md#insn-009b74d8) · [`009b7508`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b7/009b74c0.md#insn-009b7508)

~~~diff
- 009b6528 ["COPY", "register:4040:8", ["const:c88000:8"]]
+ 009b74d4 ["COPY", "register:4040:8", ["const:c89000:8"]]
- 009b6528 bytes 881600d0
+ 009b74d4 bytes 881600d0
- 009b652c ["COPY", "tmp:0:8", ["const:f60:8"]]
- 009b652c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009b652c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009b652c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009b74d8 ["COPY", "tmp:0:8", ["const:f30:8"]]
+ 009b74d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009b74d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009b74d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009b652c bytes 08813d91
+ 009b74d8 bytes 08c13c91
- 009b655c ["COPY", "register:0:8", ["register:4040:8"]]
- 009b655c ["INT_ADD", "register:40f0:8", ["const:9b655c:8", "const:4:8"]]
- 009b655c ["CALLIND", null, ["register:0:8"]]
+ 009b7508 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009b7508 ["INT_ADD", "register:40f0:8", ["const:9b7508:8", "const:4:8"]]
+ 009b7508 ["CALLIND", null, ["register:0:8"]]
- 009b655c bytes 00013fd6
+ 009b7508 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-733e347d1874ba5623f90e42ec81ee4e"></a>

### [`009b6570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b6/009b6570.md) → [`009b751c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b7/009b751c.md) FUN_009b751c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009b7538",
      "incomplete_value": false,
      "site": "009b7548",
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
            "const:f30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b658c",
      "incomplete_value": false,
      "site": "009b659c",
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
            "const:f60:8"
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
      "009b7548",
      "DATA",
      [
        "storage",
        "00c88f60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b7548",
      "DATA",
      [
        "storage",
        "00c89f30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b6584`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b6/009b6570.md#insn-009b6584) · [`009b6588`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b6/009b6570.md#insn-009b6588) · [`009b658c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b6/009b6570.md#insn-009b658c)
- 新版 [`009b7530`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b7/009b751c.md#insn-009b7530) · [`009b7534`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b7/009b751c.md#insn-009b7534) · [`009b7538`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b7/009b751c.md#insn-009b7538)

~~~diff
- 009b6584 ["INT_ADD", "register:40f0:8", ["const:9b6584:8", "const:4:8"]]
- 009b6584 ["CALL", null, ["callee:00c58f30:8"]]
+ 009b7530 ["INT_ADD", "register:40f0:8", ["const:9b7530:8", "const:4:8"]]
+ 009b7530 ["CALL", null, ["callee:00c58f30:8"]]
- 009b6584 bytes 77860a94
+ 009b7530 bytes 80860a94
- 009b6588 ["COPY", "register:4040:8", ["const:c88000:8"]]
+ 009b7534 ["COPY", "register:4040:8", ["const:c89000:8"]]
- 009b6588 bytes 881600d0
+ 009b7534 bytes 881600d0
- 009b658c ["COPY", "tmp:0:8", ["const:f60:8"]]
- 009b658c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009b658c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009b658c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009b7538 ["COPY", "tmp:0:8", ["const:f30:8"]]
+ 009b7538 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009b7538 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009b7538 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009b658c bytes 08813d91
+ 009b7538 bytes 08c13c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e7e6bad03558a874beb83af63bc0051"></a>

### [`009b6608`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b6/009b6608.md) → [`009b75b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b7/009b75b4.md) FUN_009b75b4

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "009b75c4",
      "incomplete_value": false,
      "site": "009b75cc",
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
            "const:f30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b6618",
      "incomplete_value": false,
      "site": "009b6620",
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
            "const:f60:8"
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
      "009b75cc",
      "DATA",
      [
        "storage",
        "00c88f60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b75cc",
      "DATA",
      [
        "storage",
        "00c89f30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b6614`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b6/009b6608.md#insn-009b6614) · [`009b6618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b6/009b6608.md#insn-009b6618) · [`009b6654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b6/009b6608.md#insn-009b6654)
- 新版 [`009b75c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b7/009b75b4.md#insn-009b75c0) · [`009b75c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b7/009b75b4.md#insn-009b75c4) · [`009b7600`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b7/009b75b4.md#insn-009b7600)

~~~diff
- 009b6614 ["COPY", "register:4040:8", ["const:c88000:8"]]
+ 009b75c0 ["COPY", "register:4040:8", ["const:c89000:8"]]
- 009b6614 bytes 881600d0
+ 009b75c0 bytes 881600d0
- 009b6618 ["COPY", "tmp:0:8", ["const:f60:8"]]
- 009b6618 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009b6618 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009b6618 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009b75c4 ["COPY", "tmp:0:8", ["const:f30:8"]]
+ 009b75c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009b75c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009b75c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009b6618 bytes 08813d91
+ 009b75c4 bytes 08c13c91
- 009b6654 ["COPY", "register:0:8", ["register:4048:8"]]
- 009b6654 ["INT_ADD", "register:40f0:8", ["const:9b6654:8", "const:4:8"]]
- 009b6654 ["CALLIND", null, ["register:0:8"]]
+ 009b7600 ["COPY", "register:0:8", ["register:4048:8"]]
+ 009b7600 ["INT_ADD", "register:40f0:8", ["const:9b7600:8", "const:4:8"]]
+ 009b7600 ["CALLIND", null, ["register:0:8"]]
- 009b6654 bytes 20013fd6
+ 009b7600 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e03788e0634e51c74ff5346eb7801aae"></a>

### [`009b67e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b6/009b67e0.md) → [`009b778c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b7/009b778c.md) FUN_009b778c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009b77a0",
      "incomplete_value": false,
      "site": "009b77a4",
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
    "old": {
      "definition_site": "009b67f4",
      "incomplete_value": false,
      "site": "009b67f8",
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
            "const:fe0:8"
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
      "009b77a4",
      "DATA",
      [
        "storage",
        "00c88fe0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b77a4",
      "DATA",
      [
        "storage",
        "00c89fb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b67ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b6/009b67e0.md#insn-009b67ec) · [`009b67f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b6/009b67e0.md#insn-009b67f0) · [`009b67f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b6/009b67e0.md#insn-009b67f4)
- 新版 [`009b7798`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b7/009b778c.md#insn-009b7798) · [`009b779c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b7/009b778c.md#insn-009b779c) · [`009b77a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b7/009b778c.md#insn-009b77a0)

~~~diff
- 009b67ec ["INT_ADD", "register:40f0:8", ["const:9b67ec:8", "const:4:8"]]
- 009b67ec ["CALL", null, ["callee:00c58f30:8"]]
+ 009b7798 ["INT_ADD", "register:40f0:8", ["const:9b7798:8", "const:4:8"]]
+ 009b7798 ["CALL", null, ["callee:00c58f30:8"]]
- 009b67ec bytes dd850a94
+ 009b7798 bytes e6850a94
- 009b67f0 ["COPY", "register:4040:8", ["const:c88000:8"]]
+ 009b779c ["COPY", "register:4040:8", ["const:c89000:8"]]
- 009b67f0 bytes 881600d0
+ 009b779c bytes 881600d0
- 009b67f4 ["COPY", "tmp:0:8", ["const:fe0:8"]]
- 009b67f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009b67f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009b67f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009b77a0 ["COPY", "tmp:0:8", ["const:fb0:8"]]
+ 009b77a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009b77a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009b77a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009b67f4 bytes 08813f91
+ 009b77a0 bytes 08c13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de8a432bee5e26a61ce6ebb763924b24"></a>

### [`009b6804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b6/009b6804.md) → [`009b77b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b7/009b77b0.md) FUN_009b77b0

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009b77b4",
      "incomplete_value": false,
      "site": "009b77b8",
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
    "old": {
      "definition_site": "009b6808",
      "incomplete_value": false,
      "site": "009b680c",
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
            "const:fe0:8"
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
      "009b77b8",
      "DATA",
      [
        "storage",
        "00c88fe0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b77b8",
      "DATA",
      [
        "storage",
        "00c89fb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b6804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b6/009b6804.md#insn-009b6804) · [`009b6808`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b6/009b6804.md#insn-009b6808)
- 新版 [`009b77b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b7/009b77b0.md#insn-009b77b0) · [`009b77b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b7/009b77b0.md#insn-009b77b4)

~~~diff
- 009b6804 ["COPY", "register:4040:8", ["const:c88000:8"]]
+ 009b77b0 ["COPY", "register:4040:8", ["const:c89000:8"]]
- 009b6804 bytes 881600d0
+ 009b77b0 bytes 881600d0
- 009b6808 ["COPY", "tmp:0:8", ["const:fe0:8"]]
- 009b6808 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009b6808 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009b6808 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009b77b4 ["COPY", "tmp:0:8", ["const:fb0:8"]]
+ 009b77b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009b77b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009b77b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009b6808 bytes 08813f91
+ 009b77b4 bytes 08c13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7dcccb5d3d142ccb1c90ec735ddaa4e3"></a>

### [`009b684c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b6/009b684c.md) → [`009b77f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b7/009b77f8.md) FUN_009b77f8

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009b781c",
      "incomplete_value": false,
      "site": "009b781c",
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
            "const:30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b6870",
      "incomplete_value": false,
      "site": "009b6870",
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
            "const:60:8"
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
      "009b781c",
      "DATA",
      [
        "storage",
        "00c89060",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b781c",
      "DATA",
      [
        "storage",
        "00c8a030",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b6860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b6/009b684c.md#insn-009b6860) · [`009b6868`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b6/009b684c.md#insn-009b6868) · [`009b686c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b6/009b684c.md#insn-009b686c)
- 新版 [`009b780c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b7/009b77f8.md#insn-009b780c) · [`009b7814`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b7/009b77f8.md#insn-009b7814) · [`009b7818`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b7/009b77f8.md#insn-009b7818)

~~~diff
- 009b6860 ["INT_ADD", "register:40f0:8", ["const:9b6860:8", "const:4:8"]]
- 009b6860 ["CALL", null, ["callee:00c58f30:8"]]
+ 009b780c ["INT_ADD", "register:40f0:8", ["const:9b780c:8", "const:4:8"]]
+ 009b780c ["CALL", null, ["callee:00c58f30:8"]]
- 009b6860 bytes c0850a94
+ 009b780c bytes c9850a94
- 009b6868 ["COPY", "register:4040:8", ["const:c89000:8"]]
+ 009b7814 ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 009b6868 bytes 881600f0
+ 009b7814 bytes 881600f0
- 009b686c ["COPY", "tmp:0:8", ["const:60:8"]]
- 009b686c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009b686c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009b686c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009b7818 ["COPY", "tmp:0:8", ["const:30:8"]]
+ 009b7818 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009b7818 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009b7818 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009b686c bytes 08810191
+ 009b7818 bytes 08c10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2186df7b2f240bd89b3bb4d341aa9ca8"></a>

### [`009b6880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b6/009b6880.md) → [`009b782c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b7/009b782c.md) FUN_009b782c

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009b7838",
      "incomplete_value": false,
      "site": "009b7838",
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
            "const:30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b688c",
      "incomplete_value": false,
      "site": "009b688c",
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
            "const:60:8"
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
      "009b7838",
      "DATA",
      [
        "storage",
        "00c89060",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b7838",
      "DATA",
      [
        "storage",
        "00c8a030",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b6884`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b6/009b6880.md#insn-009b6884) · [`009b6888`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b6/009b6880.md#insn-009b6888)
- 新版 [`009b7830`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b7/009b782c.md#insn-009b7830) · [`009b7834`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b7/009b782c.md#insn-009b7834)

~~~diff
- 009b6884 ["COPY", "register:4048:8", ["const:c89000:8"]]
+ 009b7830 ["COPY", "register:4048:8", ["const:c8a000:8"]]
- 009b6884 bytes 891600f0
+ 009b7830 bytes 891600f0
- 009b6888 ["COPY", "tmp:0:8", ["const:60:8"]]
- 009b6888 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 009b6888 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 009b6888 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 009b7834 ["COPY", "tmp:0:8", ["const:30:8"]]
+ 009b7834 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 009b7834 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 009b7834 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 009b6888 bytes 29810191
+ 009b7834 bytes 29c10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c24625da9d9cdd82734d99c8ce07114"></a>

### [`009b6a14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b6/009b6a14.md) → [`009b79c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b7/009b79c0.md) FUN_009b79c0

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009b79d4",
      "incomplete_value": false,
      "site": "009b79d8",
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
            "const:b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b6a28",
      "incomplete_value": false,
      "site": "009b6a2c",
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
            "const:e0:8"
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
      "009b79d8",
      "DATA",
      [
        "storage",
        "00c890e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b79d8",
      "DATA",
      [
        "storage",
        "00c8a0b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b6a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b6/009b6a14.md#insn-009b6a20) · [`009b6a24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b6/009b6a14.md#insn-009b6a24) · [`009b6a28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b6/009b6a14.md#insn-009b6a28)
- 新版 [`009b79cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b7/009b79c0.md#insn-009b79cc) · [`009b79d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b7/009b79c0.md#insn-009b79d0) · [`009b79d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b7/009b79c0.md#insn-009b79d4)

~~~diff
- 009b6a20 ["INT_ADD", "register:40f0:8", ["const:9b6a20:8", "const:4:8"]]
- 009b6a20 ["CALL", null, ["callee:00c58f30:8"]]
+ 009b79cc ["INT_ADD", "register:40f0:8", ["const:9b79cc:8", "const:4:8"]]
+ 009b79cc ["CALL", null, ["callee:00c58f30:8"]]
- 009b6a20 bytes 50850a94
+ 009b79cc bytes 59850a94
- 009b6a24 ["COPY", "register:4040:8", ["const:c89000:8"]]
+ 009b79d0 ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 009b6a24 bytes 881600f0
+ 009b79d0 bytes 881600f0
- 009b6a28 ["COPY", "tmp:0:8", ["const:e0:8"]]
- 009b6a28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009b6a28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009b6a28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009b79d4 ["COPY", "tmp:0:8", ["const:b0:8"]]
+ 009b79d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009b79d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009b79d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009b6a28 bytes 08810391
+ 009b79d4 bytes 08c10291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5de9082e3da6e23d1bf0e36574f48495"></a>

### [`009b6a38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b6/009b6a38.md) → [`009b79e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b7/009b79e4.md) FUN_009b79e4

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "009b79e8",
      "incomplete_value": false,
      "site": "009b79ec",
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
            "const:b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b6a3c",
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
            "const:e0:8"
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
      "009b79ec",
      "DATA",
      [
        "storage",
        "00c890e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b79ec",
      "DATA",
      [
        "storage",
        "00c8a0b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b6a38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b6/009b6a38.md#insn-009b6a38) · [`009b6a3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b6/009b6a38.md#insn-009b6a3c)
- 新版 [`009b79e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b7/009b79e4.md#insn-009b79e4) · [`009b79e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b7/009b79e4.md#insn-009b79e8)

~~~diff
- 009b6a38 ["COPY", "register:4040:8", ["const:c89000:8"]]
+ 009b79e4 ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 009b6a38 bytes 881600f0
+ 009b79e4 bytes 881600f0
- 009b6a3c ["COPY", "tmp:0:8", ["const:e0:8"]]
- 009b6a3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009b6a3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009b6a3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009b79e8 ["COPY", "tmp:0:8", ["const:b0:8"]]
+ 009b79e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009b79e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009b79e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009b6a3c bytes 08810391
+ 009b79e8 bytes 08c10291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-802c8431da05d14bda0be18f8828cb88"></a>

### [`009b6a7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b6/009b6a7c.md) → [`009b7a28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b7/009b7a28.md) FUN_009b7a28

採用 · 移動量 `+0xfac` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "009b7a34",
      "incomplete_value": false,
      "site": "009b7a40",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009b6a88",
      "incomplete_value": false,
      "site": "009b6a94",
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
            "const:160:8"
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
      "009b7a40",
      "DATA",
      [
        "storage",
        "00c89160",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009b7a40",
      "DATA",
      [
        "storage",
        "00c8a130",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009b6a84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b6/009b6a7c.md#insn-009b6a84) · [`009b6a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009b6/009b6a7c.md#insn-009b6a88)
- 新版 [`009b7a30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b7/009b7a28.md#insn-009b7a30) · [`009b7a34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009b7/009b7a28.md#insn-009b7a34)

~~~diff
- 009b6a84 ["COPY", "register:4050:8", ["const:c89000:8"]]
+ 009b7a30 ["COPY", "register:4050:8", ["const:c8a000:8"]]
- 009b6a84 bytes 8a1600f0
+ 009b7a30 bytes 8a1600f0
- 009b6a88 ["COPY", "tmp:0:8", ["const:160:8"]]
- 009b6a88 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 009b6a88 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 009b6a88 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 009b7a34 ["COPY", "tmp:0:8", ["const:130:8"]]
+ 009b7a34 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 009b7a34 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 009b7a34 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 009b6a88 bytes 4a810591
+ 009b7a34 bytes 4ac10491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

